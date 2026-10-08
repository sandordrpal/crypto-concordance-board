"""Track C: Bitcoin intraday order flow, 1 to 12 hours ahead (see OUTCOMES.md).

Usage: python research/intraday.py --hf out/hf --data out/data --out out/results/intraday
"""
import argparse
import time
import traceback
from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.linear_model import Ridge

from common import COST, daily_aligned, dm, hourly_symbols, jdump, load_daily_research, load_hourly, num, pct, perf, yearly

LOG = []
HORIZONS = (1, 4, 12)
TEST_YEARS = (2021, 2022, 2023, 2024, 2025, 2026)
START = pd.Timestamp("2018-01-01")


def log(m):
    print(m, flush=True)
    LOG.append(m)


def ofi(df, k):
    v = df["volume"].rolling(k).sum()
    return (2 * df["taker_buy_base"].rolling(k).sum() - v) / v.where(v > 0)


def build(hf, data):
    btc = load_hourly(hf, "BTCUSDT")
    idx = btc.index
    lp = np.log(btc["close"])
    r1 = lp.diff()
    F = pd.DataFrame(index=idx)
    for k in (1, 2, 4, 8, 12, 24, 48, 168):
        F[f"ret_{k}h"] = lp - lp.shift(k)
    has_flow = btc["taker_buy_base"].abs().sum() > 0
    if has_flow:
        for k in (1, 4, 12, 24):
            F[f"flow_{k}h"] = ofi(btc, k)
        F["flow_4h_minus_24h"] = F["flow_4h"] - F["flow_24h"]
    lq = np.log(btc["quote_volume"].where(btc["quote_volume"] > 0))
    F["volume_z"] = (lq - lq.rolling(168, min_periods=48).mean()) / lq.rolling(168, min_periods=48).std()
    if btc["trades"].abs().sum() > 0:
        lt = np.log(btc["trades"].where(btc["trades"] > 0))
        F["trades_z"] = (lt - lt.rolling(168, min_periods=48).mean()) / lt.rolling(168, min_periods=48).std()
    F["rv_24h"] = np.sqrt((r1 ** 2).rolling(24).sum())
    F["rv_168h"] = np.sqrt((r1 ** 2).rolling(168).sum() / 7)
    F["rv_ratio"] = F["rv_24h"] / F["rv_168h"]
    F["from_24h_high"] = lp - np.log(btc["high"].rolling(24).max())
    F["from_24h_low"] = lp - np.log(btc["low"].rolling(24).min())
    hr, dow = idx.hour.values, idx.dayofweek.values
    F["hour_sin"], F["hour_cos"] = np.sin(2 * np.pi * hr / 24), np.cos(2 * np.pi * hr / 24)
    F["dow_sin"], F["dow_cos"] = np.sin(2 * np.pi * dow / 7), np.cos(2 * np.pi * dow / 7)
    F["weekend"] = (dow >= 5).astype(float)
    syms = hourly_symbols(hf)
    if "ETHUSDT" in syms:
        eth = load_hourly(hf, "ETHUSDT").reindex(idx)
        le = np.log(eth["close"])
        for k in (1, 4, 24):
            F[f"eth_ret_{k}h"] = le - le.shift(k)
        F["eth_minus_btc_24h"] = F["eth_ret_24h"] - F["ret_24h"]
        if has_flow:
            F["eth_flow_4h"] = ofi(eth, 4)
    alts = [s for s in syms if s not in ("BTCUSDT", "ETHUSDT")]
    if alts:
        rets, bq, qq = [], [], []
        for s in alts:
            a = load_hourly(hf, s).reindex(idx)
            rets.append(np.log(a["close"]).diff())
            bq.append(a["taker_buy_quote"])
            qq.append(a["quote_volume"])
        R = pd.concat(rets, axis=1)
        n = R.notna().sum(1)
        alt = R.mean(1).where(n >= 5)
        F["alt_ret_1h"] = alt
        F["alt_ret_4h"] = alt.rolling(4).sum()
        F["alt_ret_24h"] = alt.rolling(24).sum()
        if has_flow:
            Bq, Qq = pd.concat(bq, axis=1).sum(1), pd.concat(qq, axis=1).sum(1)
            F["alt_flow_4h"] = (2 * Bq.rolling(4).sum() - Qq.rolling(4).sum()) / Qq.rolling(4).sum().where(Qq.rolling(4).sum() > 0)
    series = load_daily_research(data)
    days = pd.date_range(idx.min().floor("D"), idx.max().floor("D"), freq="D")
    for name in ("fear_greed", "funding_rate"):
        if name in series:
            s, meta = series[name]
            x = daily_aligned(s, days, int(meta.get("lag_days", 1)) + 1)    # extra day: daily values are known only after the day ends
            F[f"daily_{name}"] = x.reindex(idx.floor("D")).values
    Y = pd.DataFrame({f"y{h}": lp.shift(-h) - lp for h in HORIZONS}, index=idx)
    return F.replace([np.inf, -np.inf], np.nan), Y, has_flow, len(alts)


class Std:
    def fit(self, X):
        self.med = np.nanmedian(X, 0)
        Z = np.where(np.isnan(X), self.med, X)
        self.mu, self.sd = Z.mean(0), Z.std(0)
        self.sd[self.sd == 0] = 1
        return self

    def tr(self, X):
        Z = np.where(np.isnan(X), self.med, X)
        return np.clip((Z - self.mu) / self.sd, -6, 6).astype(np.float32)


def gru_fit_predict(Zi, yi, Zv, yv, Zt, L=24, seeds=(1, 2, 3)):
    """GRU on the last 24 hours of features. Z* are full standardized arrays with row positions handled outside."""
    import torch
    from torch import nn
    torch.set_num_threads(4)
    preds = []
    for seed in seeds:
        torch.manual_seed(seed)
        gru, head = nn.GRU(Zi.shape[2], 32, batch_first=True), nn.Linear(32, 1)
        params = list(gru.parameters()) + list(head.parameters())
        opt = torch.optim.AdamW(params, lr=1e-3, weight_decay=1e-3)

        def fwd(X, train=False):
            out = []
            for i in range(0, len(X), 4096):
                o, _ = gru(X[i:i + 4096])
                hdn = o[:, -1]
                if train:
                    hdn = nn.functional.dropout(hdn, 0.2, True)
                out.append(head(hdn).squeeze(-1))
            return torch.cat(out)

        best, state, wait = np.inf, None, 0
        for ep in range(12):
            perm = torch.randperm(len(Zi))
            for i in range(0, len(Zi), 512):
                b = perm[i:i + 512]
                opt.zero_grad()
                o, _ = gru(Zi[b])
                loss = ((head(nn.functional.dropout(o[:, -1], 0.2, True)).squeeze(-1) - yi[b]) ** 2).mean()
                loss.backward()
                nn.utils.clip_grad_norm_(params, 1.0)
                opt.step()
            with torch.no_grad():
                e = float(((fwd(Zv) - yv) ** 2).mean())
            if e < best - 1e-9:
                best, wait, state = e, 0, [p.detach().clone() for p in params]
            else:
                wait += 1
                if wait >= 3:
                    break
        for p, s in zip(params, state):
            p.data.copy_(s)
        with torch.no_grad():
            preds.append(fwd(Zt).numpy())
    return np.mean(preds, 0)


def walk_forward(F, Y, h, use_gru):
    y = Y[f"y{h}"].values
    idx = F.index
    X = F.values
    ok = ~np.isnan(y) & (idx >= START)
    P = {m: np.full(len(idx), np.nan) for m in ("zero", "ridge", "xgboost") + (("gru",) if use_gru else ())}
    for yr in TEST_YEARS:
        t0 = time.time()
        ts = pd.Timestamp(f"{yr}-01-01")
        test = ok & (idx >= ts) & (idx < pd.Timestamp(f"{yr + 1}-01-01"))
        if not test.any():
            continue
        cut = ts - pd.Timedelta(hours=h)
        fit = ok & (idx < cut)
        vstart = cut - pd.Timedelta(days=180)
        val = fit & (idx >= vstart)
        itr = fit & (idx < vstart - pd.Timedelta(hours=h))
        P["zero"][test] = 0.0
        S1 = Std().fit(X[itr])
        best = None
        for a in np.logspace(0, 6, 13):
            m = Ridge(alpha=a).fit(S1.tr(X[itr]), y[itr])
            e = np.mean((m.predict(S1.tr(X[val])) - y[val]) ** 2)
            if best is None or e < best[0]:
                best = (e, a)
        S2 = Std().fit(X[fit])
        P["ridge"][test] = Ridge(alpha=best[1]).fit(S2.tr(X[fit]), y[fit]).predict(S2.tr(X[test]))
        try:
            import xgboost as xgb
            bx = None
            for md in (3, 5):
                m = xgb.XGBRegressor(n_estimators=3000, learning_rate=0.03, max_depth=md, min_child_weight=200, subsample=0.7,
                                     colsample_bytree=0.7, reg_lambda=10, early_stopping_rounds=150, n_jobs=4, random_state=0,
                                     tree_method="hist")
                m.fit(X[itr], y[itr], eval_set=[(X[val], y[val])], verbose=False)
                e = np.mean((m.predict(X[val]) - y[val]) ** 2)
                if bx is None or e < bx[0]:
                    bx = (e, md, m.best_iteration + 1)
            m = xgb.XGBRegressor(n_estimators=int(bx[2] * 1.1) + 1, learning_rate=0.03, max_depth=bx[1], min_child_weight=200,
                                 subsample=0.7, colsample_bytree=0.7, reg_lambda=10, n_jobs=4, random_state=0, tree_method="hist")
            P["xgboost"][test] = m.fit(X[fit], y[fit]).predict(X[test])
        except ImportError:
            P.pop("xgboost", None)
        except Exception:
            log(f"[y{h}] xgboost {yr} failed:\n{traceback.format_exc()}")
        if use_gru:
            try:
                import torch
                L = 24
                S3 = Std().fit(X[itr])
                Z = S3.tr(X)
                pos = np.arange(len(idx))
                sd = np.std(y[itr])

                def seqs(mask, stride=1):
                    rows = pos[mask & (pos >= L - 1)][::stride]
                    return torch.tensor(np.stack([Z[r - L + 1:r + 1] for r in rows])), rows
                Zi, ri = seqs(itr, 2)
                Zv, rv = seqs(val, 2)
                Zt, rt = seqs(test)
                p = gru_fit_predict(Zi, torch.tensor(y[ri] / sd, dtype=torch.float32), Zv,
                                    torch.tensor(y[rv] / sd, dtype=torch.float32), Zt) * sd
                P["gru"][rt] = p
            except ImportError:
                P.pop("gru", None)
                use_gru = False
            except Exception:
                log(f"[y{h}] gru {yr} failed:\n{traceback.format_exc()}")
        log(f"[y{h}] {yr}: fit {fit.sum()} rows, test {test.sum()}, ridge alpha {best[1]:.0f}, {time.time() - t0:.0f}s")
    return P


def evaluate(P, y, idx, h):
    mask = ~np.isnan(P["zero"])
    years = idx[mask].year
    res = {}
    for m, p in P.items():
        pm = p[mask]
        if np.isnan(pm).all():
            continue
        yy = y[mask]
        okm = ~np.isnan(pm)
        yy, pm, yrs = yy[okm], pm[okm], years[okm]
        r2 = 1 - ((yy - pm) ** 2).sum() / (yy ** 2).sum()
        nz = (yy != 0) & (pm != 0)
        s, pv = dm(yy ** 2, (yy - pm) ** 2, h)
        res[m] = {"r2_oos": float(r2), "hit_rate": float(np.mean(np.sign(yy[nz]) == np.sign(pm[nz]))) if nz.sum() > 100 else np.nan,
                  "dm_p": pv, "n": int(len(yy)),
                  "yearly_r2": {int(t): float(1 - ((yy[yrs == t] - pm[yrs == t]) ** 2).sum() / (yy[yrs == t] ** 2).sum()) for t in sorted(set(yrs))}}
    return res


def strategy(pred, y4, idx):
    """Long/flat on non-overlapping 4-hour blocks. Enter when the forecast clears the round trip, stay while positive."""
    sel = (idx.hour % 4 == 0) & ~np.isnan(pred) & ~np.isnan(y4)
    p, r = pred[sel], np.exp(y4[sel]) - 1
    di = idx[sel]
    pos, prev, net, ls = np.zeros(len(p)), 0.0, np.zeros(len(p)), np.zeros(len(p))
    prev_ls = 0.0
    for i in range(len(p)):
        cur = 1.0 if (p[i] > 2 * COST or (prev == 1.0 and p[i] > 0)) else 0.0
        net[i] = cur * r[i] - COST * abs(cur - prev)
        pos[i], prev = cur, cur
        c2 = 1.0 if p[i] > 2 * COST else (-1.0 if p[i] < -2 * COST else (prev_ls if abs(p[i]) > 0 and np.sign(p[i]) == prev_ls else 0.0))
        ls[i] = c2 * r[i] - COST * abs(c2 - prev_ls)
        prev_ls = c2
    ppy = 365 * 6
    out = perf(pd.Series(net, index=di), ppy)
    out["exposure"] = float(pos.mean())
    out["trades_per_year"] = float(np.abs(np.diff(np.r_[0, pos])).sum() / (len(p) / ppy))
    out["yearly"] = yearly(net, di)
    out["long_short"] = perf(pd.Series(ls, index=di), ppy)
    bh = perf(pd.Series(r, index=di), ppy)
    bh["yearly"] = yearly(r, di)
    return out, bh


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--hf", default="out/hf")
    ap.add_argument("--data", default="out/data")
    ap.add_argument("--out", default="out/results/intraday")
    ap.add_argument("--no-gru", action="store_true")
    a = ap.parse_args()
    out = Path(a.out)
    out.mkdir(parents=True, exist_ok=True)
    t0 = time.time()
    F, Y, has_flow, n_alts = build(a.hf, a.data)
    log(f"hourly panel {F.index.min()}..{F.index.max()} · {F.shape[1]} features · order flow {'yes' if has_flow else 'NO (fallback data)'} · {n_alts} altcoins in basket")
    results, preds4 = {}, None
    for h in HORIZONS:
        P = walk_forward(F, Y, h, use_gru=(h == 4 and not a.no_gru))
        results[f"y{h}"] = evaluate(P, Y[f"y{h}"].values, F.index, h)
        for m, r in results[f"y{h}"].items():
            log(f"[y{h}] {m:8s} R2oos {r['r2_oos']:+.5f} hit {r['hit_rate']:.4f} DM p {r['dm_p']}")
        if h == 4:
            preds4 = P
    strat, bh = {}, None
    for m, p in preds4.items():
        if m == "zero" or np.isnan(p).all():
            continue
        try:
            strat[m], bh = strategy(p, Y["y4"].values, F.index)
        except Exception:
            log(f"strategy {m} failed:\n{traceback.format_exc()}")
    score = []
    r4 = {m: r for m, r in results["y4"].items() if m != "zero"}
    c1 = [m for m, r in r4.items() if r["r2_oos"] > 0 and r["dm_p"] == r["dm_p"] and r["dm_p"] is not None and r["dm_p"] < 0.05 and r["hit_rate"] > 0.51]
    best = max(r4, key=lambda m: r4[m]["r2_oos"])
    score.append({"id": "C1", "outcome": "Next-4-hour Bitcoin return", "pass": bool(c1),
                  "result": f"best {best}: R²oos {pct(r4[best]['r2_oos'], 2)}, hit {100*r4[best]['hit_rate']:.1f}%, DM p {num(r4[best]['dm_p'], 3)}"})
    c2 = []
    for m, s in strat.items():
        pos_years = sum(v > 0 for v in s["yearly"].values())
        s["passes_C2"] = bool(s.get("sharpe", -9) > bh.get("sharpe", 9) and pos_years >= 4)
        s["positive_years"] = int(pos_years)
        if s["passes_C2"]:
            c2.append(m)
    def _sh(m):
        v = strat[m].get("sharpe")
        return v if v is not None and v == v else -9.0   # strategies that never traded have no Sharpe
    bs = max(strat, key=_sh)
    score.append({"id": "C2", "outcome": "Cost-aware long/flat on the 4-hour forecast", "pass": bool(c2),
                  "result": f"best {bs}: net Sharpe {num(strat[bs].get('sharpe'))} vs {num(bh.get('sharpe'))} buy-and-hold, positive in {strat[bs]['positive_years']} of {len(strat[bs]['yearly'])} years"})
    jdump({"forecasts": results, "strategy": strat, "buy_and_hold": bh, "scorecard": score, "features": list(F.columns),
           "order_flow": has_flow}, out / "metrics.json")
    L = ["# Track C: Bitcoin intraday order flow", "",
         f"Hourly Binance candles {F.index.min():%Y-%m-%d} to {F.index.max():%Y-%m-%d} · {F.shape[1]} features "
         f"(taker buy/sell imbalance for Bitcoin, Ether and a {n_alts}-coin altcoin basket, returns, volume, volatility, time of day) · "
         f"yearly walk-forward {TEST_YEARS[0]}–{TEST_YEARS[-1]} · runtime {(time.time()-t0)/60:.1f} min", "",
         "R²oos compares each forecast with the random walk (0 = equal). Hit is the share of hours where the forecast had the right sign.", ""]
    for h in HORIZONS:
        R = results[f"y{h}"]
        yrs = sorted({y for r in R.values() for y in r["yearly_r2"]})
        L += [f"## Next {h} hour{'s' if h > 1 else ''}", "", "| Model | R²oos | Hit rate | DM p | " + " | ".join(map(str, yrs)) + " |",
              "|---|---|---|---|" + "---|" * len(yrs)]
        for m, r in R.items():
            L.append(f"| {m} | **{pct(r['r2_oos'], 3)}** | {('%.1f%%' % (100*r['hit_rate'])) if r['hit_rate'] == r['hit_rate'] else '–'} | {num(r['dm_p'], 3)} | "
                     + " | ".join(pct(r["yearly_r2"].get(y), 2) for y in yrs) + " |")
        L.append("")
    L += ["## Trading the 4-hour forecast after costs", "",
          "Decisions every 4 hours. Long/flat: buy when the forecast exceeds the 0.20% round-trip cost, hold while it stays positive. "
          "Long/short is shown for information only (no funding or borrowing costs).", "",
          "| Strategy | Annual return | Sharpe | Max drawdown | Time invested | Trades/year | Positive years | Long/short Sharpe |", "|---|---|---|---|---|---|---|---|",
          f"| buy and hold | {pct(bh.get('ann_return'))} | {num(bh.get('sharpe'))} | {pct(bh.get('max_drawdown'), 0)} | 100% | – | "
          f"{sum(v > 0 for v in bh['yearly'].values())}/{len(bh['yearly'])} | – |"]
    for m, s in strat.items():
        L.append(f"| {m} | {pct(s.get('ann_return'))} | {num(s.get('sharpe'))} | {pct(s.get('max_drawdown'), 0)} | {100*s['exposure']:.0f}% | "
                 f"{s['trades_per_year']:.0f} | {s['positive_years']}/{len(s['yearly'])} | {num(s['long_short'].get('sharpe'))} |")
    L += ["", "## Scorecard", "", "| ID | Outcome | Result | Pass |", "|---|---|---|---|"]
    for s in score:
        L.append(f"| {s['id']} | {s['outcome']} | {s['result']} | {'PASS' if s['pass'] else 'fail'} |")
    (out / "REPORT.md").write_text("\n".join(L) + "\n")
    (out / "run.log").write_text("\n".join(LOG))


if __name__ == "__main__":
    main()
