"""Simulated hourly candles in collect_hf.py's format, for offline tests only (not market data).

Volatility clusters (GARCH-like), a weak order-flow effect on the next hours and a weak cross-coin
momentum effect are planted so that a working pipeline has something to find.
Usage: python research/synthetic_hf.py --out /tmp/sim
"""
import argparse
import json
from pathlib import Path

import numpy as np
import pandas as pd


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", required=True)
    ap.add_argument("--coins", type=int, default=14)
    a = ap.parse_args()
    out = Path(a.out) / "hf"
    out.mkdir(parents=True, exist_ok=True)
    rng = np.random.default_rng(3)
    idx = pd.date_range("2017-09-01", "2026-10-07 23:00", freq="h")
    n = len(idx)
    # market factor with GARCH(1,1) volatility
    h, mk = np.empty(n), np.empty(n)
    h[0] = 1e-5
    e = rng.standard_normal(n)
    for t in range(n):
        if t:
            h[t] = 2e-7 + 0.08 * mk[t - 1] ** 2 + 0.9 * h[t - 1]
        mk[t] = np.sqrt(h[t]) * e[t]
    status = {}
    names = ["BTC", "ETH"] + [f"C{i:02d}" for i in range(a.coins - 2)]
    drift = rng.normal(0, 2e-5, len(names))
    for j, b in enumerate(names):
        start = 0 if j < 4 else int(rng.integers(0, n // 2))
        beta = 1.0 if j == 0 else rng.uniform(0.8, 1.6)
        idio = np.sqrt(h) * rng.uniform(0.3, 1.0) * rng.standard_normal(n)
        flow = np.clip(0.5 + 0.05 * rng.standard_normal(n), 0.2, 0.8)
        r = beta * mk + idio + drift[j]
        r[1:] += 0.002 * (flow[:-1] - 0.5)                         # planted order-flow effect
        mom = pd.Series(r).rolling(24 * 28, min_periods=1).sum().shift(1).fillna(0).values
        r += 2e-6 * np.tanh(mom * 5)                                # planted momentum effect
        close = 100 * np.exp(np.cumsum(r))
        vol = np.exp(rng.normal(8, 0.4, n)) * (1 + 50 * np.abs(r))
        df = pd.DataFrame({"time": idx, "open": np.r_[close[0], close[:-1]], "close": close,
                           "volume": vol, "trades": (vol / 3).round(), "taker_buy_base": vol * flow})
        df["high"] = np.maximum(df.open, df.close) * 1.001
        df["low"] = np.minimum(df.open, df.close) * 0.999
        df["quote_volume"] = df.volume * df.close * (1e4 if j < 2 else 50)
        df["taker_buy_quote"] = df.taker_buy_base * df.close * (1e4 if j < 2 else 50)
        df = df.iloc[start:]
        cols = ["time", "open", "high", "low", "close", "volume", "quote_volume", "trades", "taker_buy_base", "taker_buy_quote"]
        df[cols].to_csv(out / f"{b}USDT.csv.gz", index=False)
        status[f"{b}USDT"] = {"status": "ok", "source": "simulated", "rows": len(df)}
    (out / "status.json").write_text(json.dumps({"collected_utc": "simulated", "symbols": status}))
    print(f"wrote {len(names)} simulated hourly series")


if __name__ == "__main__":
    main()
