"""Track A: Bitcoin realized-volatility forecasts and a volatility-targeted holding (see OUTCOMES.md).

Usage: python research/vol.py --hf out/hf --data out/data --out out/results/volatility
"""
import argparse
import time
import traceback
from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.linear_model import Ridge

from common import COST, WF_START, daily_aligned, dm, jdump, load_daily_research, load_hourly, num, pct, perf, yearly

LOG = []
TARGET_VOL = 0.50


def log(m):
    print(m, flush=True)
    LOG.append(m)


def build(hf, data):
    h = load_hourly(hf, "BTCUSDT")
    lr = np.log(h["close"]).diff()
    day = lr.index.floor("D")
    rv2 = (lr ** 2).groupby(day).sum()
    n = lr.groupby(day).count()
    neg = (lr.clip(upper=0) ** 2).groupby(day).sum()
    bv = (np.pi / 2 * lr.abs() * lr.abs().shift(1)).groupby(day).sum()
    close = h["close"].groupby(day).last()
    qv = h["quote_volume"].groupby(day).sum()
    tbq = h["taker_buy_quote"].groupby(day).sum()
    d = pd.DataFrame({"rv2": rv2, "neg": neg, "bv": bv, "close": close, "qv": qv, "tbq": tbq, "n": n})
    d = d[d["n"] >= 20]
    d = d.asfreq("D")
    d["rv2"] = d["rv2"].clip(lower=1e-8)
    lv = 0.5 * np.log(d["rv2"])
    F = pd.DataFrame(index=d.index)
    F["lv_d"] = lv
    F["lv_w"] = 0.5 * np.log(d["rv2"].rolling(7, min_periods=5).mean())
    F["lv_m"] = 0.5 * np.log(d["rv2"].rolling(30, min_periods=20).mean())
    HAR = ["lv_d", "lv_w", "lv_m"]
    F["neg_share"] = d["neg"] / d["rv2"]
    F["jump_share"] = ((d["rv2"] - d["bv"]).clip(lower=0) / d["rv2"]).clip(0, 1)
    ret = np.log(d["close"]).diff()
    F["abs_ret"] = ret.abs()
    F["neg_ret"] = ret.clip(upper=0)
    EXT = HAR + ["neg_share", "jump_share", "abs_ret", "neg_ret"]
    F["next_is_weekend"] = (pd.Series(d.index + pd.Timedelta(days=1), index=d.index).dt.dayofweek >= 5).astype(float)
    lqv = np.log(d["qv"].where(d["qv"] > 0))
    F["volume_z"] = (lqv - lqv.rolling(90, min_periods=30).mean()) / lqv.rolling(90, min_periods=30).std()
    F["flow_imbalance"] = (2 * d["tbq"] - d["qv"]) / d["qv"].where(d["qv"] > 0)
    series = load_daily_research(data)
    exog = []
    picks = {"vix": "log", "move": "log", "epu_us": "log7", "emu_us": "log7", "gpr": "log7", "news_tone_bitcoin": "mean7",
             "news_volume_bitcoin": "log7", "news_tone_conflict": "mean7", "fear_greed": "level", "funding_rate": "mean7",
             "wiki_bitcoin": "log7", "ust10y": "level", "dxy": "ret30", "sp500": "absret7"}
    for name, how in picks.items():
        if name not in series:
            continue
        s, meta = series[name]
        x = daily_aligned(s, d.index, int(meta.get("lag_days", 1)))
        if x.notna().sum() < 300:
            continue
        if how == "log":
            v = np.log(x.where(x > 0))
        elif how == "log7":
            v = np.log(x.where(x > 0)).rolling(7, min_periods=3).mean()
        elif how == "mean7":
            v = x.rolling(7, min_periods=3).mean()
        elif how == "ret30":
            v = np.log(x).diff(30)
        elif how == "absret7":
            v = np.log(x).diff().abs().rolling(7, min_periods=3).mean()
        else:
            v = x
        F[f"x_{name}"] = v
        exog.append(f"x_{name}")
    ALL = EXT + ["next_is_weekend", "volume_z", "flow_imbalance"] + exog
    rv2 = d["rv2"]
    Y = pd.DataFrame(index=d.index)
    Y["v1"] = rv2.shift(-1)
    Y["v7"] = rv2[::-1].rolling(7).mean()[::-1].shift(-1)   # mean daily variance over the next 7 days
    simple_ret = d["close"].pct_change()
    return F.replace([np.inf, -np.inf], np.nan), Y, HAR, EXT, ALL, simple_ret, exog


def qlike(var, h):
    r = var / h
    return r - np.log(r) - 1


class Std:
    def fit(self, X):
        self.med = X.median()
        Z = X.fillna(self.med)
        self.mu, self.sd = Z.mean(), Z.std().replace(0, 1)
        return self

    def tr(self, X):
        return ((X.fillna(self.med) - self.mu) / self.sd).clip(-6, 6).fillna(0).values


def forecast_all(F, Y, HAR, EXT, ALL, tgt, horizon, start, models=("ridge", "xgboost", "gru"),
                 linear=("har", "har_ext"), min_cov=0.6):
    """Walk-forward variance forecasts for every model. Returns DataFrame of variance forecasts.
    `models`, `linear` and `min_cov` exist for the version 2 study; the defaults are version 1."""
    y = 0.5 * np.log(Y[tgt])                      # log volatility target
    idx = F.index
    test_days = idx[(idx >= start) & y.notna().values]
    out = pd.DataFrame(index=test_days)
    # HAR and HAR-ext: OLS re-estimated every day on a rolling 3-year window
    for name, cols in (("har", HAR), ("har_ext", EXT)):
        if name not in linear:
            continue
        t0 = time.time()
        X = F[cols]
        preds = []
        for d in test_days:
            m = (idx <= d - pd.Timedelta(days=horizon)) & (idx > d - pd.Timedelta(days=1095 + horizon))
            mm = m & X.notna().all(axis=1).values & y.notna().values
            A = np.c_[np.ones(mm.sum()), X.values[mm]]
            b, *_ = np.linalg.lstsq(A, y.values[mm], rcond=None)
            res = y.values[mm] - A @ b
            c = np.mean(np.exp(2 * res))
            xd = X.loc[d].values
            if np.isnan(xd).any():
                preds.append(np.nan)
                continue
            preds.append(np.exp(2 * (b[0] + xd @ b[1:])) * c)
        out[name] = preds
        log(f"[{tgt}] {name} done in {time.time() - t0:.0f}s")
    # ridge / xgboost / gru: refit every 30 days on all earlier data, tuned on the trailing year
    refit_days = test_days[::30]
    for name in models:
        t0 = time.time()
        preds = pd.Series(np.nan, index=test_days)
        try:
            for k, r0 in enumerate(refit_days):
                r1 = refit_days[k + 1] if k + 1 < len(refit_days) else test_days[-1] + pd.Timedelta(days=1)
                block = test_days[(test_days >= r0) & (test_days < r1)]
                cut = r0 - pd.Timedelta(days=horizon)
                fit = (idx <= cut) & (idx >= pd.Timestamp("2018-03-01")) & y.notna().values
                val = fit & (idx > cut - pd.Timedelta(days=365))
                itr = fit & (idx <= cut - pd.Timedelta(days=365 + horizon))
                cols = [c for c in ALL if F.loc[fit, c].notna().mean() > min_cov and F.loc[itr, c].notna().sum() >= 100]
                if name == "ridge":
                    P1 = Std().fit(F.loc[itr, cols])
                    best = None
                    for a in np.logspace(-2, 4, 13):
                        m = Ridge(alpha=a).fit(P1.tr(F.loc[itr, cols]), y[itr])
                        e = np.mean((m.predict(P1.tr(F.loc[val, cols])) - y[val]) ** 2)
                        if best is None or e < best[0]:
                            best = (e, a)
                    P2 = Std().fit(F.loc[fit, cols])
                    m = Ridge(alpha=best[1]).fit(P2.tr(F.loc[fit, cols]), y[fit])
                    vres = y[val] - Ridge(alpha=best[1]).fit(P1.tr(F.loc[itr, cols]), y[itr]).predict(P1.tr(F.loc[val, cols]))
                    c = np.mean(np.exp(2 * vres))
                    preds[block] = np.exp(2 * m.predict(P2.tr(F.loc[block, cols]))) * c
                elif name == "xgboost":
                    import xgboost as xgb
                    best = None
                    for md in (2, 3):
                        m = xgb.XGBRegressor(n_estimators=2000, learning_rate=0.03, max_depth=md, min_child_weight=20,
                                             subsample=0.7, colsample_bytree=0.7, reg_lambda=5, early_stopping_rounds=100,
                                             n_jobs=4, random_state=0)
                        m.fit(F.loc[itr, cols].values, y[itr], eval_set=[(F.loc[val, cols].values, y[val])], verbose=False)
                        e = np.mean((m.predict(F.loc[val, cols].values) - y[val]) ** 2)
                        if best is None or e < best[0]:
                            best = (e, md, m.best_iteration + 1, y[val] - m.predict(F.loc[val, cols].values))
                    c = np.mean(np.exp(2 * best[3]))
                    m = xgb.XGBRegressor(n_estimators=int(best[2] * 1.1) + 1, learning_rate=0.03, max_depth=best[1],
                                         min_child_weight=20, subsample=0.7, colsample_bytree=0.7, reg_lambda=5, n_jobs=4, random_state=0)
                    m.fit(F.loc[fit, cols].values, y[fit])
                    preds[block] = np.exp(2 * m.predict(F.loc[block, cols].values)) * c
                else:
                    if k % 3:
                        continue                   # GRU is refit every 90 days to keep run time reasonable
                    blk = test_days[(test_days >= r0) & (test_days < (refit_days[k + 3] if k + 3 < len(refit_days) else r1 + pd.Timedelta(days=3650)))]
                    preds[blk] = gru_block(F, y, cols, itr, val, blk)
            out[name] = preds.values
            log(f"[{tgt}] {name} done in {time.time() - t0:.0f}s")
        except ImportError as e:
            log(f"[{tgt}] {name} skipped: {e}")
        except Exception:
            log(f"[{tgt}] {name} failed:\n{traceback.format_exc()}")
    return out, y


def gru_block(F, y, cols, itr, val, block, L=30):
    import torch
    from torch import nn
    torch.set_num_threads(4)
    P = Std().fit(F.loc[itr, cols])
    Z = P.tr(F[cols]).astype(np.float32)
    pos = np.arange(len(F))
    yy = y.values.astype(np.float32)
    mu, sd = np.nanmean(yy[itr]), np.nanstd(yy[itr])

    def seqs(mask):
        rows = pos[mask & (pos >= L - 1)]
        return torch.tensor(np.stack([Z[r - L + 1:r + 1] for r in rows])), rows

    Xi, ri = seqs(itr)
    Xv, rv = seqs(val)
    blk_mask = F.index.isin(block)
    Xb, rb = seqs(blk_mask)
    yi = torch.tensor((yy[ri] - mu) / sd)
    preds, cs = [], []
    for seed in (1, 2, 3):
        torch.manual_seed(seed)
        gru, head = nn.GRU(Z.shape[1], 24, batch_first=True), nn.Linear(24, 1)
        params = list(gru.parameters()) + list(head.parameters())
        opt = torch.optim.AdamW(params, lr=1e-3, weight_decay=1e-3)

        def fwd(X, train=False):
            o, _ = gru(X)
            hdn = o[:, -1]
            if train:
                hdn = nn.functional.dropout(hdn, 0.2, True)
            return head(hdn).squeeze(-1)

        best, state, wait = np.inf, None, 0
        for ep in range(150):
            perm = torch.randperm(len(Xi))
            for i in range(0, len(Xi), 64):
                b = perm[i:i + 64]
                opt.zero_grad()
                loss = ((fwd(Xi[b], True) - yi[b]) ** 2).mean()
                loss.backward()
                opt.step()
            with torch.no_grad():
                pv = fwd(Xv).numpy() * sd + mu
            e = float(np.mean((pv - yy[rv]) ** 2))
            if e < best - 1e-9:
                best, wait = e, 0
                state = ([p.detach().clone() for p in params], pv)
            else:
                wait += 1
                if wait >= 15:
                    break
        for p, s in zip(params, state[0]):
            p.data.copy_(s)
        with torch.no_grad():
            preds.append(fwd(Xb).numpy() * sd + mu)
        cs.append(np.mean(np.exp(2 * (yy[rv] - state[1]))))
    out = pd.Series(np.exp(2 * np.mean(preds, 0)) * np.mean(cs), index=F.index[rb])
    return out.reindex(block).values


def vol_target(var_fc, ret, name):
    """Daily weight = min(1, target / forecast annualized vol), set at day d close, earns day d+1 return."""
    w = np.minimum(1.0, TARGET_VOL / np.sqrt(var_fc * 365))
    w = w.reindex(ret.index).ffill(limit=2)
    w_lag = w.shift(1)                              # decided yesterday, applied today
    gross = w_lag * ret
    cost = COST * w_lag.diff().abs().fillna(0)
    net = (gross - cost).dropna()
    p = perf(net, 365)
    p["avg_weight"] = float(w_lag.mean())
    p["yearly"] = yearly(net.values, net.index)
    return net, p


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--hf", default="out/hf")
    ap.add_argument("--data", default="out/data")
    ap.add_argument("--out", default="out/results/volatility")
    a = ap.parse_args()
    out = Path(a.out)
    out.mkdir(parents=True, exist_ok=True)
    t0 = time.time()
    F, Y, HAR, EXT, ALL, ret, exog = build(a.hf, a.data)
    log(f"daily panel {F.index.min().date()}..{F.index.max().date()} · {len(ALL)} features ({len(exog)} news/macro/sentiment)")
    res, fc_store = {}, {}
    for tgt, hz in (("v1", 1), ("v7", 7)):
        fc, y = forecast_all(F, Y, HAR, EXT, ALL, tgt, hz, WF_START)
        fc_store[tgt] = fc
        var = Y[tgt].reindex(fc.index)
        rows = {}
        base_loss = qlike(var, fc["har"])
        for m in fc.columns:
            ok = fc[m].notna() & fc["har"].notna() & var.notna()
            L = qlike(var[ok], fc[m][ok])
            lb = base_loss[ok]
            s, p = dm(lb.values, L.values, hz)
            lvol_err = 0.5 * np.log(var[ok]) - 0.5 * np.log(fc[m][ok])
            rows[m] = {"qlike": float(L.mean()), "qlike_vs_har": float(L.mean() / lb.mean()), "dm_stat": s, "dm_p": p,
                       "mse_logvol": float((lvol_err ** 2).mean()), "n": int(ok.sum()),
                       "yearly_qlike_ratio": {int(yy): float(L[L.index.year == yy].mean() / lb[lb.index.year == yy].mean())
                                              for yy in sorted(set(L.index.year))}}
            log(f"[{tgt}] {m:8s} QLIKE {L.mean():.4f} ratio vs HAR {rows[m]['qlike_vs_har']:.3f} DM p {p}")
        res[tgt] = rows
    # A3: volatility-targeted holding using one-day forecasts
    fc1 = fc_store["v1"]
    strat = {}
    bh = ret.reindex(fc1.index).shift(-1).dropna()   # buy and hold over the same days (d+1 returns)
    bh = ret[(ret.index > fc1.index.min()) & (ret.index <= fc1.index.max() + pd.Timedelta(days=1))].dropna()
    strat["buy_and_hold"] = perf(bh, 365)
    strat["buy_and_hold"]["yearly"] = yearly(bh.values, bh.index)
    trailing = (Y["v1"].shift(1)).rolling(30, min_periods=20).mean()   # 30-day average of realized variance, no model
    _, strat["trailing_30d_vol"] = vol_target(trailing.reindex(fc1.index), ret, "trailing")
    for m in fc1.columns:
        _, strat[m] = vol_target(fc1[m], ret, m)
    bhp = strat["buy_and_hold"]
    for m, p in strat.items():
        if m == "buy_and_hold":
            continue
        p["passes_A3"] = bool(p.get("sharpe", -9) > bhp["sharpe"] and abs(p.get("max_drawdown", -1)) <= 0.75 * abs(bhp["max_drawdown"]))
    score = []
    for tgt, oid, lab in (("v1", "A1", "Next-day realized volatility"), ("v7", "A2", "Next-7-day realized volatility")):
        ch = {m: r for m, r in res[tgt].items() if m != "har"}
        best = min(ch, key=lambda m: ch[m]["qlike"]) if ch else None
        passed = [m for m, r in ch.items() if r["qlike_vs_har"] < 1 and r["dm_p"] is not None and r["dm_p"] == r["dm_p"] and r["dm_p"] < 0.05]
        score.append({"id": oid, "outcome": lab, "pass": bool(passed),
                      "result": (f"best challenger {best}: QLIKE {res[tgt][best]['qlike_vs_har']:.3f}× HAR, DM p {num(res[tgt][best]['dm_p'], 3)}"
                                 if best else "no challenger ran") + (f"; passing: {', '.join(passed)}" if passed else "")})
    a3 = strat.get("har", {})
    score.append({"id": "A3", "outcome": "Volatility-targeted Bitcoin (HAR forecast, primary)", "pass": bool(a3.get("passes_A3")),
                  "result": f"Sharpe {num(a3.get('sharpe'))} vs {num(bhp['sharpe'])} buy-and-hold; max drawdown {pct(a3.get('max_drawdown'), 0)} vs {pct(bhp['max_drawdown'], 0)}"})
    jdump({"forecast_quality": res, "vol_target": strat, "scorecard": score, "features": ALL}, out / "metrics.json")
    write_report(res, strat, score, F, out, time.time() - t0, exog)
    (out / "run.log").write_text("\n".join(LOG))


def write_report(res, strat, score, F, out, secs, exog):
    L = ["# Track A: Bitcoin volatility", "",
         f"Walk-forward from {WF_START.date()} · daily panel from hourly Binance candles · {len(exog)} news, sentiment and macro inputs · runtime {secs/60:.1f} min", "",
         "QLIKE is the standard loss for variance forecasts (lower is better). The ratio compares each model with HAR; below 1.00 is better. "
         "DM p tests whether the difference from HAR is more than chance.", ""]
    for tgt, lab in (("v1", "Next-day realized volatility"), ("v7", "Next-7-day realized volatility")):
        R = res[tgt]
        yrs = sorted({y for r in R.values() for y in r["yearly_qlike_ratio"]})
        L += [f"## {lab}", "", "| Model | QLIKE | vs HAR | DM p | " + " | ".join(str(y) for y in yrs) + " |",
              "|---|---|---|---|" + "---|" * len(yrs)]
        for m, r in R.items():
            L.append(f"| {m} | {r['qlike']:.4f} | **{r['qlike_vs_har']:.3f}×** | {num(r['dm_p'], 3)} | "
                     + " | ".join(num(r["yearly_qlike_ratio"].get(y), 2) for y in yrs) + " |")
        L.append("")
    L += ["## Volatility-targeted Bitcoin holding", "",
          f"Each day the position is set to {int(TARGET_VOL*100)}% ÷ forecast annualized volatility, capped at 100% (no leverage), with 0.10% cost per unit traded.", "",
          "| Forecast used | Annual return | Volatility | Sharpe | Max drawdown | Average position | Meets A3 |", "|---|---|---|---|---|---|---|"]
    for m, p in strat.items():
        if not p:
            continue
        L.append(f"| {m} | {pct(p['ann_return'])} | {pct(p['ann_vol'], 0)} | {num(p['sharpe'])} | {pct(p['max_drawdown'], 0)} | "
                 f"{('%.0f%%' % (100 * p['avg_weight'])) if 'avg_weight' in p else '100%'} | {'yes' if p.get('passes_A3') else ('–' if m == 'buy_and_hold' else 'no')} |")
    L += ["", "## Scorecard", "", "| ID | Outcome | Result | Pass |", "|---|---|---|---|"]
    for s in score:
        L.append(f"| {s['id']} | {s['outcome']} | {s['result']} | {'PASS' if s['pass'] else 'fail'} |")
    (out / "REPORT.md").write_text("\n".join(L) + "\n")


if __name__ == "__main__":
    main()
