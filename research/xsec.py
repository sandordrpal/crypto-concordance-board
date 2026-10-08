"""Track B: weekly cross-sectional ranking of coins (see OUTCOMES.md).

Usage: python research/xsec.py --hf out/hf --out out/results/cross_section
"""
import argparse
import time
import traceback
from pathlib import Path

import numpy as np
import pandas as pd
from scipy.stats import spearmanr
from sklearn.linear_model import Ridge

from common import COST, WF_START, hourly_symbols, jdump, load_hourly, num, nw_tstat, pct, perf, yearly

LOG = []


def log(m):
    print(m, flush=True)
    LOG.append(m)


def daily_panel(hf):
    close, qv, tbq = {}, {}, {}
    for sym in hourly_symbols(hf):
        h = load_hourly(hf, sym)
        if h is None or len(h) < 24 * 150:
            continue
        day = h.index.floor("D")
        close[sym] = h["close"].groupby(day).last()
        qv[sym] = h["quote_volume"].groupby(day).sum()
        tbq[sym] = h["taker_buy_quote"].groupby(day).sum()
    C, Q, B = pd.DataFrame(close).asfreq("D"), pd.DataFrame(qv).asfreq("D"), pd.DataFrame(tbq).asfreq("D")
    return C, Q.reindex(C.index), B.reindex(C.index)


def features(C, Q, B):
    lp = np.log(C)
    r = lp.diff()
    f = {}
    for k, nm in ((7, "mom_1w"), (14, "mom_2w"), (28, "mom_4w"), (84, "mom_12w"), (182, "mom_26w")):
        f[nm] = lp - lp.shift(k)
    f["mom_4w_skip1w"] = lp.shift(7) - lp.shift(35)
    f["rev_1d"] = r
    f["vol_4w"] = r.rolling(28, min_periods=20).std()
    f["max_ret_4w"] = r.rolling(28, min_periods=20).max()
    f["min_ret_4w"] = r.rolling(28, min_periods=20).min()
    f["illiquidity_4w"] = (r.abs() / Q.where(Q > 0)).rolling(28, min_periods=20).mean() * 1e6
    f["size_4w"] = np.log(Q.where(Q > 0).rolling(28, min_periods=20).mean())
    f["volume_trend"] = np.log(Q.where(Q > 0).rolling(7, min_periods=5).mean() / Q.where(Q > 0).rolling(28, min_periods=20).mean())
    tbs = B.rolling(28, min_periods=20).sum() / Q.rolling(28, min_periods=20).sum()
    f["buy_share_4w"] = tbs
    f["buy_share_change"] = B.rolling(7, min_periods=5).sum() / Q.rolling(7, min_periods=5).sum() - tbs
    btc = r["BTCUSDT"]
    cov = r.rolling(84, min_periods=60).cov(btc)
    var = btc.rolling(84, min_periods=60).var()
    beta = cov.div(var, axis=0)
    f["beta_btc_12w"] = beta
    f["idio_vol_12w"] = (r - beta.mul(btc, axis=0)).rolling(84, min_periods=60).std()
    f["dist_52w_high"] = lp - np.log(C.rolling(364, min_periods=120).max())
    for k in (20, 50, 200):
        f[f"ma_gap_{k}"] = lp - np.log(C.rolling(k, min_periods=int(k * 0.8)).mean())
    d = C.diff()
    up, dn = d.clip(lower=0).ewm(alpha=1 / 14).mean(), (-d.clip(upper=0)).ewm(alpha=1 / 14).mean()
    f["rsi_14"] = 100 - 100 / (1 + up / dn)
    return f


def build(C, Q, B):
    f = features(C, Q, B)
    fwd = np.log(C.shift(-7) / C)                   # next-week log return, formation at Sunday close
    hist = C.notna().cumsum()
    liq = Q.rolling(30, min_periods=20).median()
    sundays = C.index[C.index.dayofweek == 6]
    rows = []
    for d in sundays:
        elig = (hist.loc[d] >= 120) & (liq.loc[d] >= 1e6) & C.loc[d].notna()
        coins = elig[elig].index
        if len(coins) < 10:
            continue
        row = pd.DataFrame({k: v.loc[d, coins] for k, v in f.items()})
        ranked = row.rank(pct=True) - 0.5          # cross-sectional rank normalization
        ranked = ranked.fillna(0.0)
        ranked["date"], ranked["coin"] = d, coins
        ranked["ret"] = fwd.loc[d, coins].values
        ranked["ret_simple"] = (C.shift(-7) / C - 1).loc[d, coins].values
        rows.append(ranked)
    P = pd.concat(rows, ignore_index=True)
    P["target"] = P.groupby("date")["ret"].rank(pct=True) - 0.5
    return P, list(f)


def walk_forward(P, feats):
    dates = sorted(P["date"].unique())
    test_dates = [d for d in dates if d >= WF_START]
    preds = {m: pd.Series(np.nan, index=P.index) for m in ("momentum_4w", "ridge", "xgboost", "mlp")}
    preds["momentum_4w"] = P["mom_4w"].astype(float)
    for k in range(0, len(test_dates), 13):
        block = test_dates[k:k + 13]
        start = block[0]
        trn = (P["date"] <= start - pd.Timedelta(days=7)) & P["target"].notna()   # targets realized before formation
        val = trn & (P["date"] > start - pd.Timedelta(days=7 + 26 * 7))
        itr = trn & ~val & (P["date"] <= start - pd.Timedelta(days=7 + 26 * 7 + 7))
        tst = P["date"].isin(block)
        if trn.sum() < 300:
            log(f"block from {pd.Timestamp(start).date()}: only {int(trn.sum())} training rows, skipped")
            continue
        X, y = P[feats].values, P["target"].values
        best = None
        for a in (1, 10, 100, 1000, 10000):
            if itr.sum() < 200 or val.sum() < 50:
                best = (0, 100)
                break
            m = Ridge(alpha=a).fit(X[itr], y[itr])
            e = np.mean((m.predict(X[val]) - y[val]) ** 2)
            if best is None or e < best[0]:
                best = (e, a)
        preds["ridge"][tst] = Ridge(alpha=best[1]).fit(X[trn], y[trn]).predict(X[tst])
        try:
            import xgboost as xgb
            m = xgb.XGBRegressor(n_estimators=300, learning_rate=0.03, max_depth=3, min_child_weight=50, subsample=0.7,
                                 colsample_bytree=0.7, reg_lambda=5, n_jobs=4, random_state=0)
            preds["xgboost"][tst] = m.fit(X[trn], y[trn]).predict(X[tst])
        except ImportError:
            from sklearn.ensemble import HistGradientBoostingRegressor as HGB
            preds["xgboost"][tst] = HGB(max_depth=3, learning_rate=0.03, max_iter=300, min_samples_leaf=50).fit(X[trn], y[trn]).predict(X[tst])
        try:
            from sklearn.neural_network import MLPRegressor
            ps = []
            for seed in (1, 2, 3):
                m = MLPRegressor(hidden_layer_sizes=(32, 16), alpha=1e-2, learning_rate_init=1e-3, max_iter=200,
                                 early_stopping=True, validation_fraction=0.15, n_iter_no_change=10, random_state=seed)
                ps.append(m.fit(X[trn], y[trn]).predict(X[tst]))
            preds["mlp"][tst] = np.mean(ps, 0)
        except Exception:
            log(traceback.format_exc())
    return preds, test_dates


def portfolios(P, score, test_dates, name):
    """Weekly top-quintile long-only and top-minus-bottom portfolios, with costs on weight changes."""
    ic, top_net, ew_net, ls_net, dates, turn = [], [], [], [], [], []
    w_prev_top, w_prev_ew, w_prev_ls = pd.Series(dtype=float), pd.Series(dtype=float), pd.Series(dtype=float)
    for d in test_dates:
        g = P[P["date"] == d]
        s = score[g.index]
        ok = s.notna() & g["ret"].notna()
        g, s = g[ok], s[ok]
        if len(g) < 10:
            continue
        ic.append(spearmanr(s, g["ret"]).statistic)
        q = pd.qcut(s.rank(method="first"), 5, labels=False)
        top, bot = g[q == 4], g[q == 0]
        w_top = pd.Series(1 / len(top), index=top["coin"])
        w_ew = pd.Series(1 / len(g), index=g["coin"])
        w_ls = pd.concat([w_top, -pd.Series(1 / len(bot), index=bot["coin"])])

        def tc(w, wp):
            u = w.index.union(wp.index)
            return float((w.reindex(u, fill_value=0) - wp.reindex(u, fill_value=0)).abs().sum())
        rs = g.set_index("coin")["ret_simple"]
        t1, t2, t3 = tc(w_top, w_prev_top), tc(w_ew, w_prev_ew), tc(w_ls, w_prev_ls)
        top_net.append(float((w_top * rs.reindex(w_top.index)).sum()) - COST * t1)
        ew_net.append(float((w_ew * rs.reindex(w_ew.index)).sum()) - COST * t2)
        ls_net.append(float((w_ls * rs.reindex(w_ls.index)).sum()) - COST * t3)
        turn.append(t1)
        w_prev_top, w_prev_ew, w_prev_ls = w_top, w_ew, w_ls
        dates.append(d)
    idx = pd.DatetimeIndex(dates)
    ex = np.array(top_net) - np.array(ew_net)
    out = {"ic_mean": float(np.nanmean(ic)), "ic_t": nw_tstat(ic, 4), "ic_positive_share": float(np.mean(np.array(ic) > 0)),
           "weeks": len(ic), "top_quintile": perf(pd.Series(top_net, index=idx), 52), "equal_weight": perf(pd.Series(ew_net, index=idx), 52),
           "long_short": perf(pd.Series(ls_net, index=idx), 52), "excess_mean_weekly": float(ex.mean()), "excess_t": nw_tstat(ex, 4),
           "avg_turnover": float(np.mean(turn)), "yearly_top": yearly(top_net, idx), "yearly_ew": yearly(ew_net, idx),
           "yearly_ic": {int(y): float(np.nanmean(np.array(ic)[idx.year == y])) for y in sorted(set(idx.year))}}
    out["passes_B1"] = bool(out["ic_mean"] > 0 and out["ic_t"] == out["ic_t"] and out["ic_t"] > 2)
    out["passes_B2"] = bool(out["top_quintile"].get("sharpe", -9) > out["equal_weight"].get("sharpe", 9) and out["excess_t"] == out["excess_t"] and out["excess_t"] > 2)
    log(f"{name:12s} IC {out['ic_mean']:+.4f} (t {out['ic_t']:.2f}) top Sharpe {out['top_quintile'].get('sharpe', np.nan):.2f} "
        f"EW Sharpe {out['equal_weight'].get('sharpe', np.nan):.2f} excess t {out['excess_t']:.2f}")
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--hf", default="out/hf")
    ap.add_argument("--out", default="out/results/cross_section")
    a = ap.parse_args()
    out = Path(a.out)
    out.mkdir(parents=True, exist_ok=True)
    t0 = time.time()
    C, Q, B = daily_panel(a.hf)
    P, feats = build(C, Q, B)
    log(f"{C.shape[1]} coins · {P['date'].nunique()} weekly formations · {len(P)} coin-weeks · {len(feats)} characteristics")
    preds, test_dates = walk_forward(P, feats)
    res = {m: portfolios(P, s, test_dates, m) for m, s in preds.items() if s.notna().any()}
    coins_per_week = P[P["date"] >= WF_START].groupby("date").size()
    best_b1 = max(res, key=lambda m: res[m]["ic_t"] if res[m]["ic_t"] == res[m]["ic_t"] else -9)
    best_b2 = max(res, key=lambda m: res[m]["excess_t"] if res[m]["excess_t"] == res[m]["excess_t"] else -9)
    score = [{"id": "B1", "outcome": "Weekly rank IC of coin forecasts", "pass": any(r["passes_B1"] for r in res.values()),
              "result": f"best {best_b1}: mean IC {res[best_b1]['ic_mean']:+.3f}, t {num(res[best_b1]['ic_t'])}; "
                        + ", ".join(f"{m} {r['ic_mean']:+.3f}" for m, r in res.items())},
             {"id": "B2", "outcome": "Top-fifth long-only vs equal weight, after costs", "pass": any(r["passes_B2"] for r in res.values()),
              "result": f"best {best_b2}: Sharpe {num(res[best_b2]['top_quintile'].get('sharpe'))} vs {num(res[best_b2]['equal_weight'].get('sharpe'))} EW, "
                        f"excess t {num(res[best_b2]['excess_t'])}"}]
    jdump({"models": res, "scorecard": score, "coins": list(C.columns), "features": feats,
           "coins_per_week": {"min": int(coins_per_week.min()), "median": float(coins_per_week.median()), "max": int(coins_per_week.max())}},
          out / "metrics.json")
    L = ["# Track B: ranking coins against each other", "",
         f"{C.shape[1]} coins with hourly Binance data · {coins_per_week.median():.0f} eligible coins in a typical week "
         f"(min {coins_per_week.min()}, max {coins_per_week.max()}) · weekly rebalancing from {WF_START.date()} · "
         f"models refit every 13 weeks · 0.10% cost per side · runtime {(time.time()-t0)/60:.1f} min", "",
         "IC is the rank correlation between a model's scores and the next week's returns across coins (0 = no information). "
         "The top-fifth portfolio holds the highest-scored coins in equal weights; equal weight (EW) holds every eligible coin.", "",
         "| Model | Mean IC | IC t-stat | Weeks IC > 0 | Top-fifth Sharpe | EW Sharpe | Excess t-stat | Top-fifth annual | EW annual | Long-short Sharpe | Turnover/week |",
         "|---|---|---|---|---|---|---|---|---|---|---|"]
    for m, r in res.items():
        L.append(f"| {m} | {r['ic_mean']:+.3f} | {num(r['ic_t'])} | {100*r['ic_positive_share']:.0f}% | {num(r['top_quintile'].get('sharpe'))} | "
                 f"{num(r['equal_weight'].get('sharpe'))} | {num(r['excess_t'])} | {pct(r['top_quintile'].get('ann_return'), 0)} | "
                 f"{pct(r['equal_weight'].get('ann_return'), 0)} | {num(r['long_short'].get('sharpe'))} | {100*r['avg_turnover']:.0f}% |")
    yrs = sorted({y for r in res.values() for y in r["yearly_ic"]})
    L += ["", "Mean IC by year:", "", "| Model | " + " | ".join(map(str, yrs)) + " |", "|---|" + "---|" * len(yrs)]
    for m, r in res.items():
        L.append(f"| {m} | " + " | ".join(f"{r['yearly_ic'].get(y, np.nan):+.3f}" for y in yrs) + " |")
    L += ["", "Caveat stated in advance: the coin list is today's large coins, so past altcoin returns are flattered (survivorship bias).", "",
          "## Scorecard", "", "| ID | Outcome | Result | Pass |", "|---|---|---|---|"]
    for s in score:
        L.append(f"| {s['id']} | {s['outcome']} | {s['result']} | {'PASS' if s['pass'] else 'fail'} |")
    (out / "REPORT.md").write_text("\n".join(L) + "\n")
    (out / "run.log").write_text("\n".join(LOG))


if __name__ == "__main__":
    main()
