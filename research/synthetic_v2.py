"""Simulated version 2 inputs in collect_v2.py's format, built from simulated hourly candles, for offline
tests only (not market data). DVOL is planted as a noisy, forward-looking view of volatility so a working
pipeline has something to find.
Usage: python research/synthetic_v2.py --hf /tmp/sim/hf --out /tmp/sim
"""
import argparse
import json
from pathlib import Path

import numpy as np
import pandas as pd

from collect_v2 import cpi_frame, fomc_frame
from common import hourly_symbols, load_hourly


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--hf", required=True)
    ap.add_argument("--out", required=True)
    a = ap.parse_args()
    out = Path(a.out) / "v2"
    out.mkdir(parents=True, exist_ok=True)
    rng = np.random.default_rng(7)
    status = {}
    for j, sym in enumerate(hourly_symbols(a.hf)):
        h = load_hourly(a.hf, sym)
        if j % 5 == 4:                               # some coins have no futures
            status[sym] = {"status": "missing", "reason": "simulated: no perpetual"}
            continue
        start = max(h.index.min(), pd.Timestamp("2019-09-08"))
        h = h[h.index >= start]
        n = len(h)
        f = pd.DataFrame(index=h.index)
        f["fut_close"] = h["close"] * (1 + 0.0005 * rng.standard_normal(n))
        f["fut_qv"] = h["quote_volume"] * rng.uniform(1.5, 3, n)
        f["fut_tbq"] = f["fut_qv"] * np.clip(0.5 + 0.04 * rng.standard_normal(n), 0.2, 0.8)
        prem = np.zeros(n)
        for t in range(1, n):
            prem[t] = 0.98 * prem[t - 1] + 0.00005 * rng.standard_normal()
        f["premium"] = prem
        fund = pd.Series(np.nan, index=h.index)
        settle = h.index.hour % 8 == 0
        fund[settle] = 0.0001 + pd.Series(prem, index=h.index)[settle] * 0.3
        f["funding"] = fund
        f.index.name = "time"
        f.to_csv(out / f"fut_{sym}.csv.gz")
        mstart = pd.Timestamp("2021-12-01")
        mi = h.index[h.index >= mstart]
        if sym not in ("BTCUSDT", "ETHUSDT"):
            mi = mi[(mi.dayofweek == 6)]
        oi = np.exp(np.cumsum(0.002 * rng.standard_normal(len(mi)))) * 1e9
        m = pd.DataFrame({"oi_value": oi, "top_ls_pos": np.exp(0.1 * rng.standard_normal(len(mi))),
                          "top_ls_acct": np.exp(0.1 * rng.standard_normal(len(mi))), "ls_acct": np.exp(0.1 * rng.standard_normal(len(mi))),
                          "taker_ls": np.exp(0.2 * rng.standard_normal(len(mi)))}, index=mi)
        m.index.name = "time"
        m.to_csv(out / f"metrics_{sym}.csv.gz")
        status[sym] = {"status": "ok", "rows": n}
    btc = load_hourly(a.hf, "BTCUSDT")
    r = np.log(btc["close"]).diff()
    fwd = (r ** 2)[::-1].rolling(24 * 7, min_periods=24).mean()[::-1].shift(-1)
    for cur, base in (("BTC", fwd), ("ETH", fwd * 1.3)):
        d = 100 * np.sqrt(base * 24 * 365) * np.exp(0.15 * rng.standard_normal(len(base)))
        d = d[d.index >= pd.Timestamp("2021-03-24")].dropna()
        pd.DataFrame({"time": d.index, "dvol": d.values}).to_csv(out / f"dvol_{cur}.csv", index=False)
        status[f"dvol_{cur}"] = {"status": "ok", "rows": int(len(d))}
    cb = btc["close"] * (1 + 0.0008 * rng.standard_normal(len(btc)))
    pd.DataFrame({"time": cb.index, "close": cb.values}).to_csv(out / "coinbase_BTC-USD.csv", index=False)
    ui = btc.index[btc.index >= pd.Timestamp("2021-01-01")]
    pd.DataFrame({"time": ui, "close": 1 + 0.0003 * rng.standard_normal(len(ui))}).to_csv(out / "coinbase_USDT-USD.csv", index=False)
    fomc_frame().to_csv(out / "fomc.csv", index=False)
    cpi_frame().to_csv(out / "cpi.csv", index=False)
    ed = pd.bdate_range("2024-01-11", btc.index.max())
    pd.DataFrame({"date": ed, "total": 200 * rng.standard_normal(len(ed))}).to_csv(out / "etf_flows.csv", index=False)
    tr = Path(a.out) / "trades"
    tr.mkdir(exist_ok=True)
    ti = btc.index[btc.index >= pd.Timestamp("2021-01-01")]
    q = btc["quote_volume"].reindex(ti).values * 3
    share = np.clip(0.5 + 0.03 * rng.standard_normal(len(ti)), 0.3, 0.7)
    T = pd.DataFrame({"buy_q": q * share, "sell_q": q * (1 - share)}, index=ti)
    T["large_buy_q"], T["large_sell_q"] = T["buy_q"] * 0.2, T["sell_q"] * 0.2
    T["xl_buy_q"], T["xl_sell_q"], T["n_large"] = T["buy_q"] * 0.05, T["sell_q"] * 0.05, 100
    T.index.name = "time"
    for y, g in T.groupby(T.index.year):
        g.to_csv(tr / f"BTCUSDT-{y}.csv.gz")
    status.update({"coinbase_BTC-USD": {"status": "ok"}, "coinbase_USDT-USD": {"status": "ok"}, "fomc": {"status": "ok"}})
    (out / "status.json").write_text(json.dumps({"collected_utc": "simulated", "sources": status}, indent=1))
    print(f"simulated version 2 inputs in {out}")


if __name__ == "__main__":
    main()
