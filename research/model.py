"""Train / validate / test comparison of forecasting models for Bitcoin.

Targets (daily data, t = one UTC day close):
  r1   log return over the next day
  r7   log return over the next 7 days
  r30  log return over the next 30 days
  m30  log of (mean close over the next 30 days / today's close); this is the only unknown
       part of the 50/100/200-day moving averages 30 days ahead, so it is used to forecast them.

Models: zero (random walk), historical mean, ridge, polynomial ridge (degree 2 on principal
components), XGBoost, GRU (deep learning, 30-day sequences, 5-seed ensemble).

Split: train 2018-03-01..2022-12-31, validation 2023, test 2024-01-01..latest. Rows whose
target window crosses into the next block are purged. Hyperparameters are chosen on the
validation year only; each model is then refit on train+validation and scored once on test.

Usage: python research/model.py --data out/data --out out/results
"""
import argparse
import json
import time
import traceback
import warnings
from pathlib import Path

import numpy as np
import pandas as pd
from scipy.stats import norm
from sklearn.decomposition import PCA
from sklearn.linear_model import Ridge
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import PolynomialFeatures, StandardScaler

warnings.filterwarnings("ignore")
START, TRAIN_END, VAL_END = pd.Timestamp("2018-03-01"), pd.Timestamp("2022-12-31"), pd.Timestamp("2023-12-31")
TARGETS = {"r1": 1, "r7": 7, "r30": 30, "m30": 30}
TARGET_LABEL = {"r1": "Next 1 day return", "r7": "Next 7 day return", "r30": "Next 30 day return",
                "m30": "Mean price over next 30 days (drives 50/100/200-day MA forecasts)"}
NOISY = ("epu_", "emu_", "gpr", "news_")
SEEDS = [11, 23, 37, 51, 73]
LOG = []


def log(msg):
    print(msg, flush=True)
    LOG.append(msg)


# ------------------------------------------------------------------ data and features
def load_series(data_dir):
    status = json.loads((data_dir / "status.json").read_text())
    out = {}
    for name, meta in status["series"].items():
        f = data_dir / "raw" / f"{name}.csv"
        if meta.get("status") != "ok" or not f.exists():
            continue
        df = pd.read_csv(f)
        s = pd.Series(pd.to_numeric(df["value"], errors="coerce").values, index=pd.to_datetime(df["date"])).dropna()
        out[name] = (s[~s.index.duplicated(keep="last")].sort_index(), meta)
    return out, status


def daily(s, index, lag):
    gaps = np.diff(s.index.values).astype("timedelta64[D]").astype(float)
    spacing = float(np.median(gaps)) if len(gaps) else 1.0
    limit = 5 if spacing <= 1.5 else 10 if spacing <= 8 else 40
    full = s.reindex(index.union(s.index)).sort_index().ffill(limit=limit).reindex(index)
    return full.shift(lag)


def zscore(x, w=365, mp=90):
    return (x - x.rolling(w, min_periods=mp).mean()) / x.rolling(w, min_periods=mp).std()


def rsi(c, n=14):
    d = c.diff()
    up, dn = d.clip(lower=0).ewm(alpha=1 / n).mean(), (-d.clip(upper=0)).ewm(alpha=1 / n).mean()
    return 100 - 100 / (1 + up / dn)


def build_panel(series):
    base = "btc" if "btc" in series and len(series["btc"][0]) > 2000 else "cm_price"
    px = series[base][0]
    index = pd.date_range(px.index.min(), px.index.max(), freq="D")
    C = px.reindex(index).ffill(limit=3)
    f = {}
    lr = np.log(C).diff()
    for k in [1, 3, 7, 14, 30, 60, 90, 180, 365]:
        f[f"btc_mom_{k}"] = np.log(C / C.shift(k))
    for k in [7, 30, 90]:
        f[f"btc_vol_{k}"] = lr.rolling(k).std()
    f["btc_vol_ratio_7_30"] = f["btc_vol_7"] / f["btc_vol_30"]
    for k in [20, 50, 100, 200]:
        f[f"btc_ma_gap_{k}"] = np.log(C / C.rolling(k).mean())
    f["btc_ma50_over_ma200"] = np.log(C.rolling(50).mean() / C.rolling(200).mean())
    f["btc_drawdown_365"] = np.log(C / C.rolling(365, min_periods=30).max())
    f["btc_rsi_14"] = rsi(C)
    if "btc_volume" in series:
        lv = np.log(daily(series["btc_volume"][0], index, 0))
        f["btc_volume_z90"] = (lv - lv.rolling(90).mean()) / lv.rolling(90).std()
    used = []
    for name, (s, meta) in series.items():
        if name in ("btc", "btc_volume", "cm_price"):
            continue
        x = daily(s, index, int(meta.get("lag_days", 1)))
        if x.notna().sum() < 200:
            continue
        kind = meta.get("kind", "level")
        if name.startswith(NOISY):
            x = x.rolling(7, min_periods=3).mean()
        if kind == "price":
            lx = np.log(x.where(x > 0))
            for k in (1, 7, 30):
                f[f"{name}_ret_{k}"] = lx.diff(k)
            f[f"{name}_gap_200"] = lx - lx.rolling(200, min_periods=100).mean()
        elif kind == "count":
            lx = np.log(x.where(x > 0))
            for k in (7, 30, 90):
                f[f"{name}_chg_{k}"] = lx.diff(k)
            f[f"{name}_z365"] = zscore(lx)
        else:
            f[f"{name}_lvl"] = x
            f[f"{name}_chg_7"] = x.diff(7)
            f[f"{name}_chg_30"] = x.diff(30)
            f[f"{name}_z365"] = zscore(x)
        used.append(name)
    X = pd.DataFrame(f, index=index).replace([np.inf, -np.inf], np.nan)
    logC = np.log(C)
    Y = pd.DataFrame(index=index)
    for t, h in TARGETS.items():
        if t.startswith("r"):
            Y[t] = logC.shift(-h) - logC
    Y["m30"] = np.log(C.rolling(30).mean().shift(-30) / C)
    return X, Y, C, base, used


# ------------------------------------------------------------------ evaluation helpers
def dm_test(y, p, h, base=None):
    """Diebold-Mariano vs a benchmark (default: zero forecast), squared loss, Newey-West variance. stat > 0: model better."""
    b = np.zeros_like(y) if base is None else np.asarray(base, float)
    d = (y - b) ** 2 - (y - p) ** 2
    n = len(d)
    if n < 30 or np.allclose(d, 0):
        return np.nan, np.nan
    dc = d - d.mean()
    L = max(int(h), 1)
    v = dc @ dc / n
    for k in range(1, L + 1):
        v += 2 * (1 - k / (L + 1)) * (dc[k:] @ dc[:-k]) / n
    if v <= 0:
        return np.nan, np.nan
    stat = d.mean() / np.sqrt(v / n)
    return float(stat), float(2 * (1 - norm.cdf(abs(stat))))


def score(y, p, h):
    y, p = np.asarray(y, float), np.asarray(p, float)
    r2 = 1 - ((y - p) ** 2).sum() / (y ** 2).sum()
    m = (y != 0) & (p != 0)
    hit = float(np.mean(np.sign(y[m]) == np.sign(p[m]))) if m.sum() > 10 else np.nan
    corr = float(np.corrcoef(y, p)[0, 1]) if p.std() > 1e-12 else np.nan
    stat, pv = dm_test(y, p, h)
    return {"r2_oos": float(r2), "mae_ratio": float(np.abs(y - p).mean() / np.abs(y).mean()),
            "hit_rate": hit, "corr": corr, "dm_stat": stat, "dm_p": pv, "n": int(len(y))}


def blocks_r2(dates, y, p, days=182):
    out = []
    d0 = dates.min()
    while d0 <= dates.max():
        m = (dates >= d0) & (dates < d0 + pd.Timedelta(days=days))
        if m.sum() > 40:
            out.append(float(1 - ((y[m] - p[m]) ** 2).sum() / (y[m] ** 2).sum()))
        d0 += pd.Timedelta(days=days)
    return out


class Prep:
    """Median impute, standardize and clip, fitted on the fitting rows only."""
    def fit(self, X):
        self.med = X.median()
        Z = X.fillna(self.med)
        self.mu, self.sd = Z.mean(), Z.std().replace(0, 1)
        return self

    def transform(self, X):
        return ((X.fillna(self.med) - self.mu) / self.sd).clip(-5, 5).fillna(0).values


# ------------------------------------------------------------------ models
def fit_ridge(Ztr, ytr, Zva, yva):
    best = None
    for a in np.logspace(-1, 5, 13):
        m = Ridge(alpha=a).fit(Ztr, ytr)
        e = np.mean((m.predict(Zva) - yva) ** 2)
        if best is None or e < best[0]:
            best = (e, {"alpha": float(a)})
    return best[1]


def make_ridge(prm):
    return Ridge(alpha=prm["alpha"])


def fit_poly(Ztr, ytr, Zva, yva):
    best = None
    for k in (5, 10, 20):
        k = min(k, Ztr.shape[1])
        for a in np.logspace(0, 6, 13):
            m = make_poly({"k": k, "alpha": a}).fit(Ztr, ytr)
            e = np.mean((m.predict(Zva) - yva) ** 2)
            if best is None or e < best[0]:
                best = (e, {"k": int(k), "alpha": float(a)})
    return best[1]


def make_poly(prm):
    return make_pipeline(PCA(n_components=prm["k"], random_state=0), PolynomialFeatures(2, include_bias=False),
                         StandardScaler(), Ridge(alpha=prm["alpha"]))


def xgb_model(prm, n_est=None):
    import xgboost as xgb
    return xgb.XGBRegressor(n_estimators=n_est or 3000, learning_rate=0.02, max_depth=prm["max_depth"],
                            min_child_weight=prm["min_child_weight"], subsample=0.7, colsample_bytree=0.5,
                            reg_lambda=5.0, reg_alpha=0.0, objective="reg:squarederror", tree_method="hist",
                            n_jobs=4, random_state=0, **({} if n_est else {"early_stopping_rounds": 150}))


def fit_xgb(Xtr, ytr, Xva, yva):
    best = None
    for md in (2, 3, 4):
        for mcw in (10, 50):
            prm = {"max_depth": md, "min_child_weight": mcw}
            m = xgb_model(prm).fit(Xtr, ytr, eval_set=[(Xva, yva)], verbose=False)
            e = np.mean((m.predict(Xva, iteration_range=(0, m.best_iteration + 1)) - yva) ** 2)
            if best is None or e < best[0]:
                best = (e, dict(prm, n_estimators=int(m.best_iteration + 1)))
    return best[1]


def gru_sequences(Zfull, rows, L):
    return np.stack([Zfull[r - L + 1:r + 1] for r in rows]).astype(np.float32)


def gru_train(Xs, ys, Xv=None, yv=None, epochs=150, seed=0, patience=20):
    import torch
    from torch import nn
    torch.manual_seed(seed)
    np.random.seed(seed)

    class Net(nn.Module):
        def __init__(self, F, H=32):
            super().__init__()
            self.gru = nn.GRU(F, H, batch_first=True)
            self.drop = nn.Dropout(0.3)
            self.head = nn.Linear(H, 1)

        def forward(self, x):
            o, _ = self.gru(x)
            return self.head(self.drop(o[:, -1])).squeeze(-1)

    net = Net(Xs.shape[2])
    opt = torch.optim.AdamW(net.parameters(), lr=1e-3, weight_decay=1e-3)
    Xt, yt = torch.tensor(Xs), torch.tensor(ys, dtype=torch.float32)
    Xvt = torch.tensor(Xv) if Xv is not None else None
    best, best_ep, best_state, wait = np.inf, epochs, None, 0
    for ep in range(1, epochs + 1):
        net.train()
        perm = torch.randperm(len(Xt))
        for i in range(0, len(Xt), 64):
            b = perm[i:i + 64]
            opt.zero_grad()
            loss = ((net(Xt[b]) - yt[b]) ** 2).mean()
            loss.backward()
            nn.utils.clip_grad_norm_(net.parameters(), 1.0)
            opt.step()
        if Xvt is not None:
            net.eval()
            with torch.no_grad():
                e = float(((net(Xvt).numpy() - yv) ** 2).mean())
            if e < best - 1e-9:
                best, best_ep, wait = e, ep, 0
                best_state = {k: v.clone() for k, v in net.state_dict().items()}
            else:
                wait += 1
                if wait >= patience:
                    break
    if best_state is not None:
        net.load_state_dict(best_state)
    net.eval()

    def predict(X):
        with torch.no_grad():
            return net(torch.tensor(X)).numpy()
    return predict, best_ep


# ------------------------------------------------------------------ one target
def run_target(tname, X, Y, C, results, preds_out, importances):
    h = TARGETS[tname]
    y_all = Y[tname]
    ok = y_all.notna() & (X.index >= START)
    idx = X.index
    tr = ok & (idx <= TRAIN_END - pd.Timedelta(days=h))
    va = ok & (idx > TRAIN_END) & (idx <= VAL_END)
    trva = ok & (idx <= VAL_END - pd.Timedelta(days=h))
    te = ok & (idx > VAL_END)
    keep = X.loc[tr].notna().mean() >= 0.6
    keep &= X.loc[tr].std() > 1e-12
    Xs = X.loc[:, keep[keep].index]
    log(f"[{tname}] rows train={tr.sum()} val={va.sum()} train+val={trva.sum()} test={te.sum()} features={Xs.shape[1]}")
    y = y_all.values
    res = {}

    def record(model, p_tr, p_va, p_fit, p_te, params, fit_rows, extra=None):
        r = {"params": params,
             "train": score(y[tr], p_tr, h), "val": score(y[va], p_va, h),
             "refit_in_sample": score(y[fit_rows], p_fit, h), "test": score(y[te], p_te, h)}
        r["overfit_gap"] = r["refit_in_sample"]["r2_oos"] - r["test"]["r2_oos"]
        r["val_to_test_drop"] = r["val"]["r2_oos"] - r["test"]["r2_oos"]
        r["test_blocks_r2"] = blocks_r2(idx[te], y[te], np.asarray(p_te))
        r["test"]["dm_vs_drift_p"] = dm_test(y[te], np.asarray(p_te, float), h, base=np.full(te.sum(), mu_trva))[1] if model not in ("zero", "mean") else np.nan
        if extra:
            r.update(extra)
        res[model] = r
        preds_out[(tname, model)] = pd.Series(np.asarray(p_te), index=idx[te])
        log(f"[{tname}] {model:8s} val R2oos={r['val']['r2_oos']:+.4f} test R2oos={r['test']['r2_oos']:+.4f} "
            f"hit={r['test']['hit_rate']:.3f} gap={r['overfit_gap']:+.4f} dm_p={r['test']['dm_p']}")

    zeros = lambda m: np.zeros(int(m.sum()))
    mu_tr, mu_trva = float(y[tr].mean()), float(y[trva].mean())
    record("zero", zeros(tr), zeros(va), zeros(trva), zeros(te), {}, trva)
    record("mean", np.full(tr.sum(), mu_tr), np.full(va.sum(), mu_tr), np.full(trva.sum(), mu_trva),
           np.full(te.sum(), mu_trva), {"train_mean": mu_tr}, trva)

    # linear and polynomial on standardized features
    for name, fitter, maker in (("ridge", fit_ridge, make_ridge), ("poly2", fit_poly, make_poly)):
        try:
            t0 = time.time()
            P1 = Prep().fit(Xs.loc[tr])
            Ztr, Zva = P1.transform(Xs.loc[tr]), P1.transform(Xs.loc[va])
            prm = fitter(Ztr, y[tr], Zva, y[va])
            m1 = maker(prm).fit(Ztr, y[tr])
            P2 = Prep().fit(Xs.loc[trva])
            Zf, Zte = P2.transform(Xs.loc[trva]), P2.transform(Xs.loc[te])
            m2 = maker(prm).fit(Zf, y[trva])
            record(name, m1.predict(Ztr), m1.predict(Zva), m2.predict(Zf), m2.predict(Zte), prm, trva,
                   {"seconds": round(time.time() - t0, 1)})
        except Exception:
            log(f"[{tname}] {name} failed:\n{traceback.format_exc()}")

    # XGBoost (falls back to sklearn gradient boosting only when xgboost is not installed, e.g. local tests)
    try:
        t0 = time.time()
        try:
            import xgboost  # noqa: F401
            prm = fit_xgb(Xs.loc[tr].values, y[tr], Xs.loc[va].values, y[va])
            m1 = xgb_model(prm, prm["n_estimators"]).fit(Xs.loc[tr].values, y[tr])
            m2 = xgb_model(prm, int(prm["n_estimators"] * 1.15)).fit(Xs.loc[trva].values, y[trva])
            label = "xgboost"
            gain = m2.get_booster().get_score(importance_type="gain")
            names = list(Xs.columns)
            imp = {names[int(k[1:])]: v for k, v in gain.items()}
            importances[tname] = dict(sorted(imp.items(), key=lambda kv: -kv[1])[:20])
        except ImportError:
            from sklearn.ensemble import HistGradientBoostingRegressor as HGB
            prm = {"fallback": "sklearn HistGradientBoosting", "max_depth": 3}
            m1 = HGB(max_depth=3, learning_rate=0.03, max_iter=300, l2_regularization=5.0).fit(Xs.loc[tr].values, y[tr])
            m2 = HGB(max_depth=3, learning_rate=0.03, max_iter=300, l2_regularization=5.0).fit(Xs.loc[trva].values, y[trva])
            label = "xgboost"
        record(label, m1.predict(Xs.loc[tr].values), m1.predict(Xs.loc[va].values),
               m2.predict(Xs.loc[trva].values), m2.predict(Xs.loc[te].values), prm, trva,
               {"seconds": round(time.time() - t0, 1)})
    except Exception:
        log(f"[{tname}] xgboost failed:\n{traceback.format_exc()}")

    # GRU on 30-day sequences of 32 principal components
    try:
        import torch
        torch.set_num_threads(4)
        t0 = time.time()
        L = 30
        pos = np.arange(len(idx))

        def seq_rows(mask):
            return pos[mask.values & (pos >= L - 1)]

        def prep_seq(fit_mask):
            P = Prep().fit(Xs.loc[fit_mask])
            Zfull = P.transform(Xs)
            pca = PCA(n_components=min(32, Zfull.shape[1]), random_state=0).fit(Zfull[fit_mask.values])
            Zp = pca.transform(Zfull)
            return Zp / Zp[fit_mask.values].std(axis=0).clip(1e-6)

        Zp1 = prep_seq(tr)
        rtr, rva = seq_rows(tr), seq_rows(va)
        sy = y[tr].std()
        Str, Sva = gru_sequences(Zp1, rtr, L), gru_sequences(Zp1, rva, L)
        p_tr, p_va, eps = [], [], []
        for s in SEEDS:
            f, ep = gru_train(Str, (y[rtr] / sy).astype(np.float32), Sva, (y[rva] / sy).astype(np.float32), seed=s)
            p_tr.append(f(Str) * sy)
            p_va.append(f(Sva) * sy)
            eps.append(ep)
        n_ep = max(5, int(np.median(eps)))
        Zp2 = prep_seq(trva)
        rf, rte = seq_rows(trva), seq_rows(te)
        sy2 = y[trva].std()
        Sf, Ste = gru_sequences(Zp2, rf, L), gru_sequences(Zp2, rte, L)
        p_f, p_te, seed_test = [], [], []
        for s in SEEDS:
            f, _ = gru_train(Sf, (y[rf] / sy2).astype(np.float32), epochs=n_ep, seed=s)
            p_f.append(f(Sf) * sy2)
            pt = f(Ste) * sy2
            p_te.append(pt)
            seed_test.append(score(y[rte], pt, h)["r2_oos"])
        record_rows = (np.mean(p_tr, 0), np.mean(p_va, 0), np.mean(p_f, 0), np.mean(p_te, 0))
        # score train and refit on the rows the GRU actually used (the first 29 days have no full window)
        tr_g = np.zeros(len(idx), bool); tr_g[rtr] = True
        trva_g = np.zeros(len(idx), bool); trva_g[rf] = True
        r = {"params": {"window_days": L, "pca_components": int(Zp1.shape[1]), "hidden": 32, "dropout": 0.3,
                        "weight_decay": 1e-3, "epochs_refit": n_ep, "val_best_epochs": eps, "seeds": len(SEEDS)},
             "train": score(y[tr_g], record_rows[0], h), "val": score(y[va], record_rows[1], h),
             "refit_in_sample": score(y[trva_g], record_rows[2], h), "test": score(y[te], record_rows[3], h),
             "seed_test_r2": seed_test, "seconds": round(time.time() - t0, 1)}
        r["overfit_gap"] = r["refit_in_sample"]["r2_oos"] - r["test"]["r2_oos"]
        r["val_to_test_drop"] = r["val"]["r2_oos"] - r["test"]["r2_oos"]
        r["test_blocks_r2"] = blocks_r2(idx[te], y[te], record_rows[3])
        r["test"]["dm_vs_drift_p"] = dm_test(y[te], record_rows[3], h, base=np.full(te.sum(), mu_trva))[1]
        res["gru"] = r
        preds_out[(tname, "gru")] = pd.Series(record_rows[3], index=idx[te])
        log(f"[{tname}] gru      val R2oos={r['val']['r2_oos']:+.4f} test R2oos={r['test']['r2_oos']:+.4f} "
            f"hit={r['test']['hit_rate']:.3f} gap={r['overfit_gap']:+.4f} seeds={['%+.3f' % v for v in seed_test]}")
    except ImportError:
        log(f"[{tname}] gru skipped: PyTorch not installed")
    except Exception:
        log(f"[{tname}] gru failed:\n{traceback.format_exc()}")

    results[tname] = {"horizon_days": h, "label": TARGET_LABEL[tname], "features": int(Xs.shape[1]),
                      "rows": {"train": int(tr.sum()), "val": int(va.sum()), "train_val": int(trva.sum()), "test": int(te.sum())},
                      "test_period": [str(idx[te].min().date()), str(idx[te].max().date())], "models": res}
    return te


def ma_forecasts(C, preds, te_mask):
    """Score 50/100/200-day MA forecasts 30 days ahead built from m30 predictions."""
    out = {}
    for model in sorted({m for (t, m) in preds if t == "m30"}):
        p = preds[("m30", model)]
        rows = {}
        for N in (50, 100, 200):
            actual = C.rolling(N).mean().shift(-30)
            known = C.rolling(N - 30).sum()
            d = p.index
            a = actual.reindex(d)
            pred = (known.reindex(d) + 30 * C.reindex(d) * np.exp(p.values)) / N
            naive = (known.reindex(d) + 30 * C.reindex(d)) / N
            m = a.notna() & pred.notna()
            mape = float((np.abs(pred[m] - a[m]) / a[m]).mean())
            mape0 = float((np.abs(naive[m] - a[m]) / a[m]).mean())
            r2_level_naive = float(1 - ((naive[m] - a[m]) ** 2).sum() / ((a[m] - a[m].mean()) ** 2).sum())
            rows[f"ma{N}"] = {"mape": mape, "mape_naive": mape0, "mape_ratio": mape / mape0 if mape0 else np.nan,
                              "naive_level_r2": r2_level_naive, "n": int(m.sum())}
        out[model] = rows
    return out


# ------------------------------------------------------------------ report
def pct(x, d=1):
    return "–" if x is None or (isinstance(x, float) and np.isnan(x)) else f"{100 * x:+.{d}f}%"


def fnum(x, d=3):
    return "–" if x is None or (isinstance(x, float) and np.isnan(x)) else f"{x:.{d}f}"


def verdict(models):
    """Pick the best model on test that also shows low overfitting risk."""
    rows = []
    for name, r in models.items():
        if name in ("zero", "mean"):
            continue
        t = r["test"]
        blocks = r.get("test_blocks_r2") or []
        risk = []
        if r["overfit_gap"] > 0.05:
            risk.append("large in-sample vs test gap")
        if r["val_to_test_drop"] > 0.05:
            risk.append("validation result did not hold on test")
        if blocks and np.mean([b > 0 for b in blocks]) < 0.5:
            risk.append("loses to random walk in most half-years")
        if "seed_test_r2" in r and np.std(r["seed_test_r2"]) > 0.02:
            risk.append("unstable across seeds")
        drift = models.get("mean", {}).get("test", {}).get("r2_oos", 0.0)
        if t["r2_oos"] <= drift:
            risk.append("no better than the constant-drift forecast")
        rows.append((name, t["r2_oos"], t["dm_p"], risk, t.get("dm_vs_drift_p")))
    rows.sort(key=lambda x: -x[1])
    winners = [r for r in rows if r[1] > 0 and r[2] == r[2] and r[2] < 0.05 and not r[3]
               and r[4] == r[4] and r[4] is not None and r[4] < 0.05]
    return rows, winners


def write_report(results, ma, importances, status, out, base, used, run_secs):
    L = []
    ser = status["series"]
    ok = [k for k, v in ser.items() if v.get("status") == "ok"]
    bad = [k for k, v in ser.items() if v.get("status") != "ok"]
    L += ["# Bitcoin model comparison: train, validate, test", "",
          f"Run: {pd.Timestamp.utcnow():%Y-%m-%d %H:%M} UTC · data collected {status.get('collected_utc', '?')} · "
          f"{len(ok)} of {len(ser)} series loaded · price base `{base}` · runtime {run_secs/60:.1f} min", "",
          "**How to read this.** R²oos compares each model with the random-walk forecast (tomorrow's price = today's). "
          "0 means no better than the random walk, negative means worse. The Diebold-Mariano p-value (DM p) tests "
          "whether a model beats the random walk by more than chance. A model should also beat the constant-drift forecast "
          "(the average past return, row `mean`). The overfit gap is in-sample R²oos minus test R²oos.", ""]
    L += ["## Split", "",
          "| Block | Period | Used for |", "|---|---|---|",
          f"| Train | {START.date()} to {TRAIN_END.date()} | fitting |",
          f"| Validation | 2023-01-01 to {VAL_END.date()} | choosing hyperparameters and early stopping |",
          f"| Test | 2024-01-01 to latest | scored once, after refitting on train + validation |", "",
          "![Test R² by model and target](test_r2_by_model.png)", "",
          "![30-day return: running advantage over the random walk](r30_cumulative_advantage.png)", ""]
    for t, R in results.items():
        L += [f"## {R['label']} (`{t}`, {R['horizon_days']} d)", "",
              f"Rows: train {R['rows']['train']}, validation {R['rows']['val']}, test {R['rows']['test']} "
              f"({R['test_period'][0]} to {R['test_period'][1]}) · {R['features']} features", "",
              "| Model | Train R²oos | Val R²oos | Test R²oos | Test direction hit | Test DM p | Overfit gap | Half-years beating RW |",
              "|---|---|---|---|---|---|---|---|"]
        for name, r in R["models"].items():
            b = r.get("test_blocks_r2") or []
            share = f"{sum(x > 0 for x in b)}/{len(b)}" if b else "–"
            L.append(f"| {name} | {pct(r['train']['r2_oos'], 2)} | {pct(r['val']['r2_oos'], 2)} | **{pct(r['test']['r2_oos'], 2)}** | "
                     f"{fnum(r['test']['hit_rate'])} | {fnum(r['test']['dm_p'])} | {pct(r['overfit_gap'], 2)} | {share} |")
        rows, winners = verdict(R["models"])
        L += ["", "Ranking on test with overfitting flags:", ""]
        for name, r2, p, risk, pd_ in rows:
            L.append(f"- **{name}**: test R²oos {pct(r2, 2)}, DM p vs random walk {fnum(p)}, vs drift {fnum(pd_)}"
                     + (f" · risk: {', '.join(risk)}" if risk else " · no risk flags"))
        L += ["", ("**Verdict:** " + (f"`{winners[0][0]}` beats both the random walk and the constant drift significantly, with no overfitting flags."
                                       if winners else "no model beats both the random walk and the constant drift significantly without an overfitting flag.")), ""]
        if "gru" in R["models"] and R["models"]["gru"].get("seed_test_r2"):
            L.append("GRU test R²oos by seed: " + ", ".join(pct(v, 2) for v in R["models"]["gru"]["seed_test_r2"]))
            L.append("")
    if ma:
        L += ["## 50/100/200-day moving averages, 30 days ahead", "",
              "Forecast = known part of the average + 30 predicted days (from the `m30` model). "
              "The naive forecast fills the 30 unknown days with today's price.", "",
              "| Model | MA50 error | MA100 error | MA200 error | MA50 vs naive | MA100 vs naive | MA200 vs naive |",
              "|---|---|---|---|---|---|---|"]
        for model, rows in ma.items():
            L.append(f"| {model} | " + " | ".join(f"{100*rows[k]['mape']:.2f}%" for k in ("ma50", "ma100", "ma200")) + " | " +
                     " | ".join(f"{rows[k]['mape_ratio']:.3f}×" for k in ("ma50", "ma100", "ma200")) + " |")
        z = ma.get("zero", {})
        if z:
            L += ["", "The naive forecast alone already explains "
                  + ", ".join(f"{k.upper()} {100*z[k]['naive_level_r2']:.1f}%" for k in ("ma50", "ma100", "ma200"))
                  + " of the variation in moving-average levels on test, so high R² on moving averages says nothing about skill.", ""]
    if importances:
        L += ["## XGBoost: most used features (gain, final refit)", ""]
        for t, imp in importances.items():
            L.append(f"- `{t}`: " + ", ".join(f"{k}" for k in list(imp)[:12]))
        L.append("")
    L += ["## Data sources", "", "| Series | Source | Kind | Lag (days) | From | To | Status |", "|---|---|---|---|---|---|---|"]
    for k, v in sorted(ser.items()):
        if v.get("status") == "ok":
            L.append(f"| {k} | {v.get('source','')} | {v.get('kind','')} | {v.get('lag_days','')} | {v.get('first','')} | {v.get('last','')} | ok{'' if k in used or k in ('btc','btc_volume','cm_price') else ' (too short, not used)'} |")
        else:
            L.append(f"| {k} | {v.get('source','')} | | | | | failed: {str(v.get('error',''))[:90]} |")
    L += ["", "Lag is the number of days a value is held back before the model may use it, so that only data "
          "that was public at the time enters each prediction.", ""]
    (out / "REPORT.md").write_text("\n".join(L))


def charts(results, preds, Y, out):
    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
    except Exception:
        return
    models = ["mean", "ridge", "poly2", "xgboost", "gru"]
    colors = {"mean": "#98a3b2", "ridge": "#2a78d6", "poly2": "#a8449a", "xgboost": "#d9582a", "gru": "#0d6b66"}
    fig, ax = plt.subplots(figsize=(9, 4.2), dpi=140)
    tg = list(results)
    w = 0.16
    for i, m in enumerate(models):
        vals = [results[t]["models"].get(m, {}).get("test", {}).get("r2_oos", np.nan) * 100 for t in tg]
        ax.bar(np.arange(len(tg)) + (i - 2) * w, vals, w * 0.9, label=m, color=colors[m])
    ax.axhline(0, color="#111822", lw=1)
    ax.set_xticks(np.arange(len(tg)), [results[t]["label"].split(" (")[0] for t in tg], fontsize=8)
    ax.set_ylabel("Test R² vs random walk (%)")
    ax.set_title("Out-of-sample skill on the test period (above 0 = beats the random walk)", fontsize=10)
    ax.legend(fontsize=8, ncol=5, frameon=False)
    ax.spines[["top", "right"]].set_visible(False)
    fig.tight_layout()
    fig.savefig(out / "test_r2_by_model.png")
    plt.close(fig)
    if "r30" in results:
        fig, ax = plt.subplots(figsize=(9, 4.2), dpi=140)
        y = Y["r30"]
        for m in models:
            if ("r30", m) not in preds:
                continue
            p = preds[("r30", m)]
            yy = y.reindex(p.index).values
            ax.plot(p.index, np.cumsum(yy ** 2 - (yy - p.values) ** 2), label=m, color=colors[m], lw=1.6)
        ax.axhline(0, color="#111822", lw=1)
        ax.set_ylabel("Cumulative squared-error advantage")
        ax.set_title("30-day return: running advantage over the random walk on test (rising = winning)", fontsize=10)
        ax.legend(fontsize=8, ncol=5, frameon=False)
        ax.spines[["top", "right"]].set_visible(False)
        fig.tight_layout()
        fig.savefig(out / "r30_cumulative_advantage.png")
        plt.close(fig)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--data", default="out/data")
    ap.add_argument("--out", default="out/results")
    ap.add_argument("--targets", default=",".join(TARGETS))
    a = ap.parse_args()
    t0 = time.time()
    data_dir, out = Path(a.data), Path(a.out)
    out.mkdir(parents=True, exist_ok=True)
    series, status = load_series(data_dir)
    X, Y, C, base, used = build_panel(series)
    log(f"panel {X.index.min().date()}..{X.index.max().date()} · {X.shape[1]} features from {len(used)} series · base {base}")
    results, preds, importances = {}, {}, {}
    te = None
    for t in a.targets.split(","):
        te = run_target(t, X, Y, C, results, preds, importances)
    ma = ma_forecasts(C, preds, te) if any(k[0] == "m30" for k in preds) else {}
    (out / "metrics.json").write_text(json.dumps({"results": results, "moving_averages": ma, "xgb_importance": importances},
                                                 indent=1, default=lambda o: None if isinstance(o, float) and np.isnan(o) else str(o)))
    pd.DataFrame({f"{t}__{m}": s for (t, m), s in preds.items()}).to_csv(out / "test_predictions.csv")
    X.tail(1).T.to_csv(out / "latest_features.csv")
    write_report(results, ma, importances, status, out, base, used, time.time() - t0)
    charts(results, preds, Y, out)
    (out / "model.log").write_text("\n".join(LOG))
    log(f"done in {time.time() - t0:.0f}s")


if __name__ == "__main__":
    main()
