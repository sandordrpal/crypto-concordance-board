"""Version 2 study: three feature tiers x two model families per track (see OUTCOMES.md, Version 2).

Tiers: F0 = the version 1 inputs, F1 = F0 + a few inputs with the strongest published evidence,
F2 = F1 + every other free input. Families: ridge (simple) and XGBoost (complex). All six cells of a
track are scored on the same out-of-sample window, 2023-01-01 to the latest data.

Usage: python research/v2.py --track vol --hf out/hf --data out/data --v2 out/v2 --out out/results/v2_volatility
       (--track xsec | intraday likewise)
"""
import argparse
import json
import time
import traceback
from pathlib import Path

import numpy as np
import pandas as pd
from scipy.stats import spearmanr

import intraday
import vol
import xsec
from common import dm, hourly_symbols, jdump, load_hourly, num, pct, perf, yearly

START = pd.Timestamp("2023-01-01")
TIERS = ("F0", "F1", "F2")
FAMILIES = ("ridge", "xgboost")
ORDER = [f"{t}-{f}" for t in TIERS for f in FAMILIES]          # simplest first
TIER_NAMES = {"F0": "current", "F1": "current + a few", "F2": "current + all free"}
LOG = []


def log(m):
    print(m, flush=True)
    LOG.append(m)


# ---------------------------------------------------------------- loading the version 2 inputs

def _csv(path):
    if not Path(path).exists():
        return None
    df = pd.read_csv(path)
    df["time"] = pd.to_datetime(df["time"], format="mixed")
    df = df.set_index("time").sort_index()
    return df[~df.index.duplicated(keep="last")]


def fut(v2, sym):
    return _csv(Path(v2) / f"fut_{sym}.csv.gz")


def metrics(v2, sym):
    return _csv(Path(v2) / f"metrics_{sym}.csv.gz")


def dvol(v2, cur):
    d = _csv(Path(v2) / f"dvol_{cur}.csv")
    return None if d is None else d["dvol"].where(d["dvol"] > 0)


def coinbase_premium(v2, btc_close):
    cb = _csv(Path(v2) / "coinbase_BTC-USD.csv")
    if cb is None:
        return None
    p = np.log(cb["close"].reindex(btc_close.index)) - np.log(btc_close)
    usdt = _csv(Path(v2) / "coinbase_USDT-USD.csv")
    if usdt is not None:                             # Binance prices are in USDT: remove USDT's own premium
        p = p - np.log(usdt["close"].reindex(btc_close.index).ffill(limit=24)).fillna(0)
    return p.clip(-0.05, 0.05)


def fomc_times(v2):
    f = Path(v2) / "fomc.csv"
    if not f.exists():
        return None
    return pd.to_datetime(pd.read_csv(f)["statement_utc"]).sort_values().values


def hourly(df, idx, cols, ffill=2):
    if df is None:
        return pd.DataFrame(index=idx, columns=cols, dtype=float)
    out = df.reindex(df.index.union(idx)).sort_index()
    for c in cols:
        if c not in out:
            out[c] = np.nan
    out = out[cols].astype(float)
    if ffill:
        out = out.ffill(limit=ffill)
    return out.reindex(idx)


def keep_available(F, cols, before, min_rows, what):
    """Drop new inputs that have too little history before the first test fold (missing source)."""
    keep, dropped = [], []
    for c in cols:
        n = int(F.loc[F.index < before, c].notna().sum())
        (keep if n >= min_rows else dropped).append(c)
    if dropped:
        log(f"{what}: dropped for missing data: {', '.join(dropped)}")
    return keep, dropped


# ---------------------------------------------------------------- tests and the decision rule

def holm(pvals):
    """Holm-adjusted p-values for a dict name -> p (NaN stays NaN)."""
    items = sorted([(p, k) for k, p in pvals.items() if p == p], key=lambda x: x[0])
    m, out, run = len(items), {k: np.nan for k in pvals}, 0.0
    for i, (p, k) in enumerate(items):
        run = max(run, min(1.0, (m - i) * p))
        out[k] = run
    return out


def pairwise(losses, lags, label):
    """The nine pre-registered comparisons. losses: cell -> Series (lower is better), aligned."""
    tests = []
    for fam in FAMILIES:
        for a, b in (("F0", "F1"), ("F0", "F2"), ("F1", "F2")):
            tests.append((f"{b} vs {a} ({fam})", f"{a}-{fam}", f"{b}-{fam}"))
    for t in TIERS:
        tests.append((f"xgboost vs ridge ({t})", f"{t}-ridge", f"{t}-xgboost"))
    rows, raw = [], {}
    for name, base, chal in tests:
        if base not in losses or chal not in losses:
            continue
        s, p = dm(losses[base].values, losses[chal].values, lags)
        raw[name] = p
        rows.append({"test": name, "base": base, "challenger": chal, "dm_stat": s, "p": p,
                     "mean_base": float(losses[base].mean()), "mean_challenger": float(losses[chal].mean())})
    adj = holm(raw)
    for r in rows:
        r["p_holm"] = adj[r["test"]]
        r["significant"] = bool(r["p_holm"] == r["p_holm"] and r["p_holm"] < 0.05)
        r["better"] = "challenger" if r["dm_stat"] == r["dm_stat"] and r["dm_stat"] > 0 else "base"
        log(f"[{label}] {r['test']:28s} DM {num(r['dm_stat'])} p {num(r['p'], 4)} Holm {num(r['p_holm'], 4)}")
    return rows


def decide(losses, lags, passes):
    """Simplest cell that passes the primary absolute outcome and is not significantly worse than the best."""
    avail = [c for c in ORDER if c in losses]
    if not avail:
        return {"candidate": None, "reason": "no cell ran"}
    best = min(avail, key=lambda c: losses[c].mean())
    raw = {}
    for c in avail:
        if c != best:
            raw[c] = dm(losses[c].values, losses[best].values, lags)[1]
    adj = holm(raw)
    worse = {c: bool(adj[c] == adj[c] and adj[c] < 0.05) for c in raw}
    cand = next((c for c in avail if passes.get(c) and (c == best or not worse[c])), None)
    return {"best_cell": best, "candidate": cand, "worse_than_best_holm_p": adj, "significantly_worse": worse,
            "reason": "simplest cell that passes the primary outcome and is not significantly worse than the best"
            if cand else "no cell passes the primary outcome"}


# ---------------------------------------------------------------- Track A: volatility

def vol_inputs(hf, data, v2):
    F, Y, HAR, EXT, ALL, ret, exog = vol.build(hf, data)
    days = F.index
    h = load_hourly(hf, "BTCUSDT")
    lr = np.log(h["close"]).diff()
    day = lr.index.floor("D")
    rv2 = (lr ** 2).groupby(day).sum().clip(lower=1e-10)
    n = lr.groupby(day).count()
    rq = n / 3 * (lr ** 4).groupby(day).sum()
    X = pd.DataFrame(index=days)
    X["harq"] = F["lv_d"] * (np.sqrt(rq) / rv2).reindex(days)
    dv = dvol(v2, "BTC")
    if dv is not None:
        dvd = dv.groupby(dv.index.floor("D")).last().reindex(days)
        X["x_dvol"] = np.log(dvd / 100 / np.sqrt(365))
    syms = hourly_symbols(hf)
    alt = []
    for s in syms:
        if s == "BTCUSDT":
            continue
        a = load_hourly(hf, s)
        if a is None:
            continue
        ar = np.log(a["close"]).diff()
        lv = 0.5 * np.log((ar ** 2).groupby(ar.index.floor("D")).sum().clip(lower=1e-10))
        cnt = ar.groupby(ar.index.floor("D")).count()
        lv = lv.where(cnt >= 20).reindex(days)
        if s == "ETHUSDT":
            X["xvol_eth"] = lv
        else:
            alt.append(lv)
    if alt:
        A = pd.concat(alt, axis=1)
        X["xvol_alt"] = A.mean(1).where(A.notna().sum(1) >= 5)
    F1_new = [c for c in ("harq", "x_dvol", "xvol_eth", "xvol_alt") if c in X]
    # F2: futures, positioning, Coinbase premium, Ether DVOL, implied minus realized, FOMC
    fb = hourly(fut(v2, "BTCUSDT"), h.index, ["fut_qv", "fut_tbq", "premium", "funding"], ffill=0)
    g = fb.groupby(day)
    X["fut_funding_d"] = g["funding"].mean().reindex(days)
    X["fut_premium_d"] = g["premium"].mean().reindex(days)
    fq, ft = g["fut_qv"].sum(min_count=12).reindex(days), g["fut_tbq"].sum(min_count=12).reindex(days)
    X["fut_flow_d"] = (2 * ft - fq) / fq.where(fq > 0)
    sq = h["quote_volume"].groupby(day).sum().reindex(days)
    X["fut_spot_volume"] = np.log(fq.where(fq > 0) / sq.where(sq > 0))
    m = metrics(v2, "BTCUSDT")
    if m is not None:
        md = m.groupby(m.index.floor("D")).last().reindex(days)
        if "oi_value" in md:
            loi = np.log(md["oi_value"].where(md["oi_value"] > 0))
            X["oi_chg_1d"], X["oi_chg_7d"] = loi.diff(1), loi.diff(7)
        for c in ("top_ls_pos", "ls_acct"):
            if c in md:
                X[c] = np.log(md[c].where(md[c] > 0))
        if "taker_ls" in m:
            X["taker_ls_d"] = np.log(m["taker_ls"].where(m["taker_ls"] > 0)).groupby(m.index.floor("D")).mean().reindex(days)
    cbp = coinbase_premium(v2, h["close"])
    if cbp is not None:
        X["cb_premium_d"] = cbp.groupby(day).mean().reindex(days)
    de = dvol(v2, "ETH")
    if de is not None:
        X["x_dvol_eth"] = np.log(de.groupby(de.index.floor("D")).last().reindex(days) / 100 / np.sqrt(365))
    if "x_dvol" in X:
        X["vrp"] = 2 * X["x_dvol"] - 2 * F["lv_w"]
    ft_ = fomc_times(v2)
    if ft_ is not None:
        sd = pd.DatetimeIndex(ft_).floor("D")
        X["fomc_next_day"] = days.map(lambda d: float((d + pd.Timedelta(days=1)) in sd)).astype(float)
        X["fomc_next_7d"] = days.map(lambda d: float(((sd > d) & (sd <= d + pd.Timedelta(days=7))).sum())).astype(float)
    F2_new = [c for c in X.columns if c not in F1_new]
    F = pd.concat([F, X.replace([np.inf, -np.inf], np.nan)], axis=1)
    # an input needs 200 days of history before the window; each refit then uses it once it has 100 training days
    F1_new, d1 = keep_available(F, F1_new, START, 200, "volatility F1")
    F2_new, d2 = keep_available(F, F2_new, START, 200, "volatility F2")
    tiers = {"F0": list(ALL), "F1": list(ALL) + F1_new, "F2": list(ALL) + F1_new + F2_new}
    return F, Y, HAR, EXT, tiers, ret, d1 + d2


def run_vol(a, out):
    F, Y, HAR, EXT, tiers, ret, dropped = vol_inputs(a.hf, a.data, a.v2)
    log(f"volatility: {len(tiers['F0'])} / {len(tiers['F1'])} / {len(tiers['F2'])} inputs in F0 / F1 / F2")
    res, fc_all = {}, {}
    for tgt, hz in (("v1", 1), ("v7", 7)):
        base, _ = vol.forecast_all(F, Y, HAR, EXT, HAR, tgt, hz, START, models=(), linear=("har",))
        fc = pd.DataFrame({"har": base["har"]})
        for t in TIERS:
            f, _ = vol.forecast_all(F, Y, HAR, EXT, tiers[t], tgt, hz, START, models=FAMILIES, linear=(), min_cov=0.0)
            for fam in FAMILIES:
                if fam in f:
                    fc[f"{t}-{fam}"] = f[fam].values
        var = Y[tgt].reindex(fc.index)
        ok = fc.notna().all(axis=1) & var.notna()
        fc, var = fc[ok], var[ok]
        fc_all[tgt] = fc
        L = {c: vol.qlike(var, fc[c]) for c in fc.columns}
        rows = {}
        for c in [c for c in ORDER if c in fc]:
            s, p = dm(L["har"].values, L[c].values, hz)
            rows[c] = {"qlike": float(L[c].mean()), "qlike_vs_har": float(L[c].mean() / L["har"].mean()), "dm_vs_har": s, "p_vs_har": p,
                       "passes": bool(L[c].mean() < L["har"].mean() and p == p and p < 0.05), "n": int(len(var)),
                       "yearly_ratio": {int(y): float(L[c][L[c].index.year == y].mean() / L["har"][L["har"].index.year == y].mean())
                                        for y in sorted(set(var.index.year))}}
            log(f"[{tgt}] {c:12s} QLIKE {rows[c]['qlike']:.4f} = {rows[c]['qlike_vs_har']:.3f}x HAR, p {num(p, 4)}")
        res[tgt] = {"cells": rows, "har_qlike": float(L["har"].mean()), "days": int(len(var)),
                    "window": [str(var.index.min().date()), str(var.index.max().date())]}
        if tgt == "v1":
            losses = {c: L[c] for c in ORDER if c in L}
            tests = pairwise(losses, hz, "volatility")
            decision = decide(losses, hz, {c: rows[c]["passes"] for c in rows})
    fc1 = fc_all["v1"]
    bh = ret[(ret.index > fc1.index.min()) & (ret.index <= fc1.index.max() + pd.Timedelta(days=1))].dropna()
    bhp = perf(bh, 365)
    strat = {"buy_and_hold": bhp}
    for c in ["har"] + [c for c in ORDER if c in fc1]:
        _, p = vol.vol_target(fc1[c], ret, c)
        p["passes_A3"] = bool(p.get("sharpe", -9) > bhp["sharpe"] and abs(p.get("max_drawdown", -1)) <= 0.75 * abs(bhp["max_drawdown"]))
        strat[c] = p
    cells = {c: {"primary": res["v1"]["cells"][c]["qlike_vs_har"], "passes_primary": res["v1"]["cells"][c]["passes"],
                 "A2": res["v7"]["cells"].get(c, {}).get("passes"), "A3": strat.get(c, {}).get("passes_A3")}
             for c in res["v1"]["cells"]}
    summary = {"track": "volatility", "primary": "next-day QLIKE relative to HAR (lower is better)", "cells": cells,
               "detail": res, "vol_target": strat, "tests": tests, "decision": decision, "tiers": tiers, "dropped_inputs": dropped}
    jdump(summary, out / "metrics.json")
    L_ = header("Track A, version 2: Bitcoin volatility", res["v1"]["window"], res["v1"]["days"], "days", tiers, dropped)
    L_ += ["## Next-day volatility (primary, A1)", "", "QLIKE relative to HAR; below 1.00 is better. Pass = lower than HAR with DM p < 0.05.", "",
           "| Cell | Inputs | QLIKE vs HAR | DM p | A1 | Next-7-day vs HAR (A2) | Vol-target Sharpe (A3) | Max drawdown |", "|---|---|---|---|---|---|---|---|"]
    for c in [c for c in ORDER if c in res["v1"]["cells"]]:
        r1, r7, s = res["v1"]["cells"][c], res["v7"]["cells"].get(c, {}), strat.get(c, {})
        L_.append(f"| {c} | {len(tiers[c.split('-')[0]])} | **{r1['qlike_vs_har']:.3f}×** | {num(r1['p_vs_har'], 3)} | {'PASS' if r1['passes'] else 'fail'} | "
                  f"{num(r7.get('qlike_vs_har'), 3)}× ({'PASS' if r7.get('passes') else 'fail'}) | {num(s.get('sharpe'))} ({'PASS' if s.get('passes_A3') else 'fail'}) | {pct(s.get('max_drawdown'), 0)} |")
    L_ += ["", f"Buy and hold over the window: Sharpe {num(bhp.get('sharpe'))}, max drawdown {pct(bhp.get('max_drawdown'), 0)}; "
           f"HAR vol-target Sharpe {num(strat['har'].get('sharpe'))}.", ""]
    L_ += footer(tests, decision)
    (out / "REPORT.md").write_text("\n".join(L_) + "\n")


# ---------------------------------------------------------------- Track B: ranking coins

def daily_from_hourly(v2, cols_C, idx, col, how):
    frames = {}
    for sym in cols_C:
        f = fut(v2, sym)
        if f is None or col not in f:
            continue
        g = f[col].groupby(f.index.floor("D"))
        frames[sym] = (g.mean() if how == "mean" else g.sum(min_count=12)).reindex(idx)
    return pd.DataFrame(frames, index=idx).reindex(columns=cols_C)


def xsec_inputs(hf, v2):
    C, Q, B = xsec.daily_panel(hf)
    lp = np.log(C)
    e1, e2 = {}, {}
    for k in (3, 5, 10, 100):
        e1[f"ma_gap_{k}"] = lp - np.log(C.rolling(k, min_periods=max(2, int(k * 0.8))).mean())
    lq = Q.where(Q > 0)
    base50 = lq.rolling(50, min_periods=40).mean()
    for k in (3, 5, 10, 20, 100):
        e1[f"vol_ma_{k}"] = np.log(lq.rolling(k, min_periods=max(2, int(k * 0.8))).mean() / base50)
    e1["macd"] = (C.ewm(span=12, min_periods=20).mean() - C.ewm(span=26, min_periods=40).mean()) / C
    fund = daily_from_hourly(v2, C.columns, C.index, "funding", "mean")
    if fund.notna().any().any():
        e1["carry_4w"] = fund.rolling(28, min_periods=14).mean()
        e2["funding_change"] = fund.rolling(7, min_periods=4).mean() - e1["carry_4w"]
    prem = daily_from_hourly(v2, C.columns, C.index, "premium", "mean")
    if prem.notna().any().any():
        e2["premium_4w"] = prem.rolling(28, min_periods=14).mean()
    fq = daily_from_hourly(v2, C.columns, C.index, "fut_qv", "sum")
    ft = daily_from_hourly(v2, C.columns, C.index, "fut_tbq", "sum")
    if fq.notna().any().any():
        f28, t28 = fq.rolling(28, min_periods=20).sum(), ft.rolling(28, min_periods=20).sum()
        e2["fut_flow_4w"] = (2 * t28 - f28) / f28.where(f28 > 0)
        e2["fut_share_4w"] = np.log(f28.where(f28 > 0) / Q.rolling(28, min_periods=20).sum().where(Q > 0))
    mets = {c: {} for c in ("oi_value", "top_ls_pos", "ls_acct", "taker_ls")}
    for sym in C.columns:
        m = metrics(v2, sym)
        if m is None:
            continue
        md = m.groupby(m.index.floor("D")).last().reindex(C.index)     # Sunday rows for most coins
        for c in mets:
            if c in md:
                mets[c][sym] = md[c]
    if mets["oi_value"]:
        oi = pd.DataFrame(mets["oi_value"], index=C.index).reindex(columns=C.columns)
        e2["oi_change_4w"] = np.log(oi.where(oi > 0)).diff(28)
    for c in ("top_ls_pos", "ls_acct", "taker_ls"):
        if mets[c]:
            v = pd.DataFrame(mets[c], index=C.index).reindex(columns=C.columns)
            e2[c] = np.log(v.where(v > 0))
    e1 = {k: v.replace([np.inf, -np.inf], np.nan) for k, v in e1.items()}
    e2 = {k: v.replace([np.inf, -np.inf], np.nan) for k, v in e2.items()}
    return C, Q, B, e1, e2


def weekly_ic(P, score, dates):
    out = {}
    for d in dates:
        g = P[P["date"] == d]
        s = score[g.index]
        ok = s.notna() & g["ret"].notna()
        if ok.sum() >= 10:
            out[d] = spearmanr(s[ok], g["ret"][ok]).statistic
    return pd.Series(out)


def run_xsec(a, out):
    C, Q, B, e1, e2 = xsec_inputs(a.hf, a.v2)
    dropped = []
    for k in list(e2):                               # an input with no data before the window is dropped
        if e2[k][e2[k].index < START - pd.Timedelta(days=180)].notna().sum().sum() < 200:
            dropped.append(k)
            e2.pop(k)
    if dropped:
        log(f"ranking F2: dropped for missing data: {', '.join(dropped)}")
    panels = {"F0": xsec.build(C, Q, B), "F1": xsec.build(C, Q, B, e1), "F2": xsec.build(C, Q, B, {**e1, **e2})}
    tiers = {t: feats for t, (_, feats) in panels.items()}
    log(f"ranking: {len(tiers['F0'])} / {len(tiers['F1'])} / {len(tiers['F2'])} characteristics in F0 / F1 / F2")
    port, ics, ref = {}, {}, None
    for t, (P, feats) in panels.items():
        preds, test_dates = xsec.walk_forward(P, feats, models=FAMILIES, start=START)
        for fam in FAMILIES:
            if preds[fam].notna().any():
                c = f"{t}-{fam}"
                port[c] = xsec.portfolios(P, preds[fam], test_dates, c)
                ics[c] = weekly_ic(P, preds[fam], test_dates)
        if t == "F0":
            ref = xsec.portfolios(P, preds["momentum_4w"], test_dates, "momentum_4w")
    common = sorted(set.intersection(*[set(s.dropna().index) for s in ics.values()]))
    losses = {c: -ics[c].reindex(common) for c in ics}
    tests = pairwise(losses, 4, "ranking")
    passes = {c: port[c]["passes_B1"] for c in port}
    decision = decide(losses, 4, passes)
    cells = {c: {"primary": port[c]["ic_mean"], "ic_t": port[c]["ic_t"], "passes_primary": port[c]["passes_B1"], "B2": port[c]["passes_B2"]}
             for c in [c for c in ORDER if c in port]}
    jdump({"track": "cross_section", "primary": "weekly rank IC (higher is better)", "cells": cells, "portfolios": port,
           "momentum_reference": ref, "tests": tests, "decision": decision, "tiers": tiers, "dropped_inputs": dropped,
           "weeks": len(common)}, out / "metrics.json")
    window = [str(pd.Timestamp(common[0]).date()), str(pd.Timestamp(common[-1]).date())] if common else ["–", "–"]
    L = header("Track B, version 2: ranking coins", window, len(common), "weekly formations", tiers, dropped)
    L += ["## Weekly rank IC (primary, B1) and the top-fifth portfolio (B2)", "",
          "B1 passes when mean IC > 0 with Newey-West t > 2. B2 needs a top-fifth Sharpe above equal weight and excess return t > 2.", "",
          "| Cell | Inputs | Mean IC | IC t | B1 | Top-fifth Sharpe | EW Sharpe | Excess t | B2 | Turnover/week |", "|---|---|---|---|---|---|---|---|---|---|"]
    for c in [c for c in ORDER if c in port]:
        r = port[c]
        L.append(f"| {c} | {len(tiers[c.split('-')[0]])} | **{r['ic_mean']:+.3f}** | {num(r['ic_t'])} | {'PASS' if r['passes_B1'] else 'fail'} | "
                 f"{num(r['top_quintile'].get('sharpe'))} | {num(r['equal_weight'].get('sharpe'))} | {num(r['excess_t'])} | "
                 f"{'PASS' if r['passes_B2'] else 'fail'} | {100 * r['avg_turnover']:.0f}% |")
    if ref:
        L += ["", f"Reference, 4-week momentum rule: mean IC {ref['ic_mean']:+.3f} (t {num(ref['ic_t'])}).", ""]
    L += footer(tests, decision, higher_better=True)
    (out / "REPORT.md").write_text("\n".join(L) + "\n")


# ---------------------------------------------------------------- Track C: intraday

def intraday_inputs(hf, data, v2):
    F, Y, has_flow, n_alts = intraday.build(hf, data)
    idx = F.index
    btc = load_hourly(hf, "BTCUSDT").reindex(idx)
    X = pd.DataFrame(index=idx)
    fb = fut(v2, "BTCUSDT")
    px = hourly(fb, idx, ["premium"], ffill=2)["premium"]
    X["premium_1h"] = px
    X["premium_chg_4h"] = px - px.shift(4)
    X["funding_last"] = hourly(fb, idx, ["funding"], ffill=9)["funding"]
    cbp = coinbase_premium(v2, btc["close"])
    if cbp is not None:
        cbp = cbp.reindex(idx).ffill(limit=2)
        X["cb_premium"] = cbp
        X["cb_premium_chg_4h"] = cbp - cbp.shift(4)
    F1_new = list(X.columns)
    m = hourly(metrics(v2, "BTCUSDT"), idx, ["oi_value", "top_ls_pos", "ls_acct", "taker_ls"], ffill=2)
    loi = np.log(m["oi_value"].where(m["oi_value"] > 0))
    for k in (1, 4, 24):
        X[f"oi_chg_{k}h"] = loi.diff(k)
    for c in ("top_ls_pos", "ls_acct", "taker_ls"):
        X[c] = np.log(m[c].where(m[c] > 0))
    fv = hourly(fb, idx, ["fut_qv", "fut_tbq"], ffill=0)
    for k in (1, 4):
        q, b = fv["fut_qv"].rolling(k).sum(), fv["fut_tbq"].rolling(k).sum()
        X[f"fut_flow_{k}h"] = (2 * b - q) / q.where(q > 0)
    X["fut_spot_24h"] = np.log(fv["fut_qv"].rolling(24).sum().where(lambda s: s > 0) / btc["quote_volume"].rolling(24).sum().where(lambda s: s > 0))
    dv = dvol(v2, "BTC")
    if dv is not None:
        ld = np.log(dv.reindex(dv.index.union(idx)).sort_index().ffill(limit=2).reindex(idx))
        X["dvol_level"], X["dvol_chg_1h"], X["dvol_chg_24h"] = ld, ld.diff(1), ld.diff(24)
    ef = fut(v2, "ETHUSDT")
    if ef is not None:
        X["eth_premium_1h"] = hourly(ef, idx, ["premium"], ffill=2)["premium"]
    if btc["trades"].abs().sum() > 0:
        ts = np.log(btc["quote_volume"].where(btc["quote_volume"] > 0) / btc["trades"].where(btc["trades"] > 0))
        X["trade_size_z"] = (ts - ts.rolling(168, min_periods=48).mean()) / ts.rolling(168, min_periods=48).std()
    ft_ = fomc_times(v2)
    if ft_ is not None:
        now = (idx + pd.Timedelta(hours=1)).values               # decisions are made at the close of each hour
        nxt = np.searchsorted(ft_, now, side="left")
        hrs_to = np.array([(ft_[i] - t) / np.timedelta64(1, "h") if i < len(ft_) else np.inf for i, t in zip(nxt, now)])
        prv = nxt - 1
        hrs_since = np.array([(t - ft_[i]) / np.timedelta64(1, "h") if i >= 0 else np.inf for i, t in zip(prv, now)])
        X["fomc_soon"] = np.where((hrs_to >= 0) & (hrs_to <= 24), (24 - hrs_to) / 24, 0.0)
        X["fomc_after"] = ((hrs_since >= 0) & (hrs_since < 6)).astype(float)
    F2_new = [c for c in X.columns if c not in F1_new]
    F = pd.concat([F, X.replace([np.inf, -np.inf], np.nan)], axis=1)
    cut = START - pd.Timedelta(days=200)
    F1_new, d1 = keep_available(F, F1_new, cut, 1000, "intraday F1")
    F2_new, d2 = keep_available(F, F2_new, cut, 1000, "intraday F2")
    F0 = [c for c in F.columns if c not in X.columns]
    return F, Y, {"F0": F0, "F1": F0 + F1_new, "F2": F0 + F1_new + F2_new}, d1 + d2


def run_intraday(a, out):
    F, Y, tiers, dropped = intraday_inputs(a.hf, a.data, a.v2)
    log(f"intraday: {len(tiers['F0'])} / {len(tiers['F1'])} / {len(tiers['F2'])} inputs in F0 / F1 / F2")
    years = tuple(range(START.year, pd.Timestamp.now().year + 1))
    preds = {}
    for t in TIERS:
        P = intraday.walk_forward(F[tiers[t]], Y, 4, use_gru=False, years=years)
        for fam in FAMILIES:
            if fam in P and not np.isnan(P[fam]).all():
                preds[f"{t}-{fam}"] = P[fam]
    y = Y["y4"].values
    idx = F.index
    mask = (idx >= START) & ~np.isnan(y)
    for p in preds.values():
        mask &= ~np.isnan(p)
    yy = pd.Series(y[mask], index=idx[mask])
    rows, losses, strat, bh = {}, {}, {}, None
    for c in [c for c in ORDER if c in preds]:
        pm = pd.Series(preds[c][mask], index=idx[mask])
        r2 = 1 - ((yy - pm) ** 2).sum() / (yy ** 2).sum()
        s, p = dm((yy ** 2).values, ((yy - pm) ** 2).values, 4)
        nz = (yy != 0) & (pm != 0)
        hit = float(np.mean(np.sign(yy[nz]) == np.sign(pm[nz])))
        rows[c] = {"r2_oos": float(r2), "dm_p": p, "hit_rate": hit, "n": int(mask.sum()),
                   "passes": bool(r2 > 0 and p == p and p < 0.05 and hit > 0.51),
                   "yearly_r2": {int(t): float(1 - ((yy[yy.index.year == t] - pm[pm.index.year == t]) ** 2).sum() / (yy[yy.index.year == t] ** 2).sum())
                                 for t in sorted(set(yy.index.year))}}
        losses[c] = (yy - pm) ** 2
        full = np.where(mask, preds[c], np.nan)
        try:
            st, bh = intraday.strategy(full, y, idx)
            st["positive_years"] = int(sum(v > 0 for v in st["yearly"].values()))
            st["passes_C2"] = bool(st.get("sharpe", -9) == st.get("sharpe", -9) and st.get("sharpe", -9) > bh.get("sharpe", 9)
                                   and st["positive_years"] >= 3)
            strat[c] = st
        except Exception:
            log(f"strategy {c} failed:\n{traceback.format_exc()}")
        log(f"[y4] {c:12s} R2oos {r2:+.5f} hit {hit:.4f} DM p {num(p, 4)}")
    tests = pairwise(losses, 4, "intraday")
    decision = decide(losses, 4, {c: rows[c]["passes"] for c in rows})
    cells = {c: {"primary": rows[c]["r2_oos"], "passes_primary": rows[c]["passes"], "C2": strat.get(c, {}).get("passes_C2")} for c in rows}
    jdump({"track": "intraday", "primary": "next-4-hour squared error (R2oos vs random walk)", "cells": cells, "detail": rows,
           "strategy": strat, "buy_and_hold": bh, "tests": tests, "decision": decision, "tiers": tiers, "dropped_inputs": dropped},
          out / "metrics.json")
    window = [str(yy.index.min().date()), str(yy.index.max().date())]
    L = header("Track C, version 2: Bitcoin intraday", window, int(mask.sum()), "hours", tiers, dropped)
    L += ["## Next-4-hour return (primary, C1) and the long/flat strategy (C2)", "",
          "C1 passes when R²oos > 0 with DM p < 0.05 and hit rate > 51%. C2 needs a net Sharpe above buy-and-hold and positive net return in at least 3 of the 4 years.", "",
          "| Cell | Inputs | R²oos | DM p | Hit rate | C1 | Strategy Sharpe | Positive years | Time invested | C2 |", "|---|---|---|---|---|---|---|---|---|---|"]
    for c in rows:
        r, s = rows[c], strat.get(c, {})
        L.append(f"| {c} | {len(tiers[c.split('-')[0]])} | **{pct(r['r2_oos'], 3)}** | {num(r['dm_p'], 3)} | {100 * r['hit_rate']:.1f}% | {'PASS' if r['passes'] else 'fail'} | "
                 f"{num(s.get('sharpe'))} | {s.get('positive_years', '–')}/{len(s.get('yearly', {}))} | {100 * s.get('exposure', 0):.0f}% | {'PASS' if s.get('passes_C2') else 'fail'} |")
    if bh:
        L += ["", f"Buy and hold over the window: Sharpe {num(bh.get('sharpe'))}, max drawdown {pct(bh.get('max_drawdown'), 0)}.", ""]
    L += footer(tests, decision)
    (out / "REPORT.md").write_text("\n".join(L) + "\n")


# ---------------------------------------------------------------- report helpers

def header(title, window, n, unit, tiers, dropped):
    L = [f"# {title}", "",
         f"Pre-registered in OUTCOMES.md (Version 2). Out of sample {window[0]} to {window[1]} ({n} {unit}), the same for every cell. "
         "Ridge = simple family, XGBoost = complex family; F0 = version 1 inputs, F1 = F0 + a few, F2 = F0 + all free inputs.", ""]
    new1 = [c for c in tiers["F1"] if c not in tiers["F0"]]
    new2 = [c for c in tiers["F2"] if c not in tiers["F1"]]
    L += [f"- F1 adds {len(new1)}: {', '.join(new1) or 'none'}", f"- F2 adds {len(new2)} more: {', '.join(new2) or 'none'}"]
    if dropped:
        L.append(f"- Dropped because the source had too little data: {', '.join(dropped)}")
    return L + [""]


def footer(tests, decision, higher_better=False):
    L = ["## Pre-registered comparisons", "",
         "Diebold-Mariano on the primary loss, Holm-corrected over the nine tests. A positive statistic favours the challenger.", "",
         "| Comparison | DM statistic | p | Holm p | Result |", "|---|---|---|---|---|"]
    for r in tests:
        res = (f"{r['challenger'] if r['better'] == 'challenger' else r['base']} better" if r["significant"] else "no significant difference")
        L.append(f"| {r['test']} | {num(r['dm_stat'])} | {num(r['p'], 4)} | {num(r['p_holm'], 4)} | {res} |")
    L += ["", "## Decision", "",
          f"Best cell on the primary metric: **{decision.get('best_cell')}**. "
          f"Live-test candidate: **{decision.get('candidate') or 'none'}** ({decision.get('reason')}).", ""]
    L += ["Information only, not investment advice."]
    return L


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--track", required=True, choices=("vol", "xsec", "intraday"))
    ap.add_argument("--hf", default="out/hf")
    ap.add_argument("--data", default="out/data")
    ap.add_argument("--v2", default="out/v2")
    ap.add_argument("--out", required=True)
    a = ap.parse_args()
    out = Path(a.out)
    out.mkdir(parents=True, exist_ok=True)
    t0 = time.time()
    st = Path(a.v2) / "status.json"
    if st.exists():
        srcs = json.loads(st.read_text()).get("sources", {})
        log(f"version 2 inputs: {sum(v.get('status') == 'ok' for v in srcs.values())} of {len(srcs)} sources ok")
    else:
        log("version 2 inputs missing: only F0 can be informative")
    try:
        {"vol": run_vol, "xsec": run_xsec, "intraday": run_intraday}[a.track](a, out)
    finally:
        log(f"runtime {(time.time() - t0) / 60:.1f} min")
        (out / "run.log").write_text("\n".join(LOG))


if __name__ == "__main__":
    main()
