"""Large-trade order flow for Bitcoin from Binance USD-M futures aggregate trades (data.binance.vision).

Each monthly file is several GB of ticks, so files are streamed one at a time, reduced to hourly totals and
deleted; only the hourly totals are cached. One year per call, so the years can run as parallel jobs.

Hourly columns: buy_q and sell_q (taker buy and sell notional, USDT), large_buy_q / large_sell_q (trades of at
least $100,000), xl_buy_q / xl_sell_q (at least $1,000,000), n_large.
Output: <out>/trades/BTCUSDT-<year>.csv.gz
Usage: python research/collect_trades.py --year 2024 --out out --cache trades_cache
"""
import argparse
import datetime as dt
import io
import json
import re
import time
import zipfile
from pathlib import Path

import numpy as np
import pandas as pd

from collect_hf import S, listing

SYM = "BTCUSDT"
LARGE, XL = 1e5, 1e6
BV = "https://data.binance.vision/"


def download(url, dest):
    for i in range(4):
        try:
            with S.get(url, stream=True, timeout=120) as r:
                if r.status_code == 404:
                    return None
                r.raise_for_status()
                with open(dest, "wb") as f:
                    for chunk in r.iter_content(1 << 22):
                        f.write(chunk)
            return dest
        except Exception as e:
            print(f"retry {url}: {e}", flush=True)
            time.sleep(5 * (i + 1))
    return None


def reduce_zip(path):
    with zipfile.ZipFile(path) as z:
        name = z.namelist()[0]
        with z.open(name) as fh:
            first = fh.readline().decode().strip()
        header = not re.fullmatch(r"\d+", first.split(",")[0])
        parts = []
        with z.open(name) as fh:
            reader = pd.read_csv(fh, header=0 if header else None, usecols=[1, 2, 5, 6], chunksize=8_000_000,
                                 names=None if header else ["id", "price", "qty", "f", "l", "t", "ibm"])
            for ch in reader:
                ch.columns = ["price", "qty", "t", "ibm"]
                t = pd.to_numeric(ch["t"])
                unit = "us" if t.iloc[0] > 1e14 else "ms"
                hour = pd.to_datetime(t, unit=unit).dt.floor("h")
                q = ch["price"].values * ch["qty"].values
                sell = ch["ibm"].astype(str).str.lower().isin(("true", "1")).values   # buyer is maker: the taker sold
                df = pd.DataFrame({"hour": hour.values, "buy_q": np.where(sell, 0, q), "sell_q": np.where(sell, q, 0)})
                big, xl = q >= LARGE, q >= XL
                df["large_buy_q"] = np.where(big & ~sell, q, 0)
                df["large_sell_q"] = np.where(big & sell, q, 0)
                df["xl_buy_q"] = np.where(xl & ~sell, q, 0)
                df["xl_sell_q"] = np.where(xl & sell, q, 0)
                df["n_large"] = big.astype(int)
                parts.append(df.groupby("hour").sum())
    return pd.concat(parts).groupby(level=0).sum()


def one(url, cache_file, tmp):
    if cache_file.exists():
        return pd.read_csv(cache_file, index_col=0, parse_dates=True)
    t0 = time.time()
    z = download(url, tmp)
    if z is None:
        return None
    try:
        h = reduce_zip(z)
    finally:
        tmp.unlink(missing_ok=True)
    cache_file.parent.mkdir(parents=True, exist_ok=True)
    h.to_csv(cache_file)
    print(f"[ok] {Path(url).name}: {len(h)} hours in {time.time() - t0:.0f}s", flush=True)
    return h


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--year", type=int, required=True)
    ap.add_argument("--out", default="out")
    ap.add_argument("--cache", default="trades_cache")
    a = ap.parse_args()
    out, cache = Path(a.out) / "trades", Path(a.cache)
    out.mkdir(parents=True, exist_ok=True)
    cache.mkdir(parents=True, exist_ok=True)
    tmp = cache / "_download.zip"
    keys = [k for k in listing(f"data/futures/um/monthly/aggTrades/{SYM}/") if k.endswith(".zip") and f"-{a.year}-" in k]
    months = {re.search(r"(\d{4}-\d{2})\.zip$", k).group(1): k for k in keys}
    parts, status = [], {"year": a.year, "months": sorted(months), "errors": []}
    for m, k in sorted(months.items()):
        try:
            h = one(BV + k, cache / f"{SYM}-{m}.csv", tmp)
            if h is not None:
                parts.append(h)
        except Exception as e:
            status["errors"].append(f"{m}: {type(e).__name__}: {e}"[:200])
            print(f"[fail] {m}: {e}", flush=True)
    # days of months that have no monthly file yet
    today = dt.datetime.now(dt.timezone.utc).date()
    d = dt.date(a.year, 1, 1)
    while d < min(today, dt.date(a.year + 1, 1, 1)):
        if f"{d:%Y-%m}" not in months:
            name = f"{SYM}-aggTrades-{d:%Y-%m-%d}.zip"
            try:
                h = one(f"{BV}data/futures/um/daily/aggTrades/{SYM}/{name}", cache / "daily" / f"{SYM}-{d}.csv", tmp)
                if h is not None:
                    parts.append(h)
            except Exception as e:
                status["errors"].append(f"{d}: {type(e).__name__}: {e}"[:200])
        d += dt.timedelta(days=1)
    if parts:
        H = pd.concat(parts).groupby(level=0).sum().sort_index()
        H.index.name = "time"
        H.to_csv(out / f"{SYM}-{a.year}.csv.gz")
        status.update(rows=int(len(H)), first=str(H.index.min()), last=str(H.index.max()))
    (out / f"status-{a.year}.json").write_text(json.dumps(status, indent=1))
    print(f"{a.year}: {status.get('rows', 0)} hours, {len(status['errors'])} errors")


if __name__ == "__main__":
    main()
