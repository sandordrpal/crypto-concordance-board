"""Download hourly spot candles (with taker buy volume) for the board's coins from Binance's public
bulk data site, data.binance.vision. Monthly files are cached between runs; the current month comes
from daily files. If Binance's site is unreachable, Bitcoin falls back to Coinbase hourly candles
(without taker volume).

Output: <out>/hf/<SYMBOL>.csv.gz with columns
  time, open, high, low, close, volume, quote_volume, trades, taker_buy_base, taker_buy_quote
and <out>/hf/status.json.
Usage: python research/collect_hf.py --out out --cache hf_cache
"""
import argparse
import datetime as dt
import io
import json
import re
import time
import zipfile
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

import pandas as pd
import requests

BASES = ["BTC", "ETH", "XRP", "BNB", "SOL", "DOGE", "TRX", "ADA", "LINK", "AVAX", "SUI", "XLM", "BCH", "HBAR", "LTC",
         "TON", "SHIB", "DOT", "UNI", "AAVE", "NEAR", "PEPE", "TAO", "APT", "ICP", "ETC", "ONDO", "ENA", "POL", "ARB",
         "ATOM", "ALGO", "RENDER", "FIL", "VET", "WLD", "OP", "INJ", "SEI", "FET", "TIA", "STX", "JUP", "BONK", "IMX",
         "GRT", "LDO", "CRV", "WIF", "ZEC", "QNT", "PENGU", "TRUMP", "PYTH", "FLOKI", "XTZ", "SAND", "THETA", "RUNE",
         "GALA", "MANA", "CAKE", "EGLD", "IOTA", "MATIC", "EOS", "XMR", "FTM"]
COLS = ["time", "open", "high", "low", "close", "volume", "close_time", "quote_volume", "trades",
        "taker_buy_base", "taker_buy_quote", "ignore"]
UA = {"User-Agent": "crypto-concordance-board research (https://github.com/sandordrpal/crypto-concordance-board)"}
S = requests.Session()
S.headers.update(UA)


def listing(prefix):
    """List files under a prefix of the data.binance.vision S3 bucket."""
    keys, marker = [], ""
    for _ in range(50):
        r = S.get("https://s3-ap-northeast-1.amazonaws.com/data.binance.vision",
                  params={"delimiter": "/", "prefix": prefix, "marker": marker}, timeout=60)
        r.raise_for_status()
        page = re.findall(r"<Key>([^<]+)</Key>", r.text)
        keys += page
        if "<IsTruncated>true</IsTruncated>" not in r.text or not page:
            break
        marker = page[-1]
    return keys


def fetch(url, dest):
    if dest.exists() and dest.stat().st_size > 0:
        return dest
    for i in range(4):
        try:
            r = S.get(url, timeout=60)
            if r.status_code == 404:
                return None
            r.raise_for_status()
            dest.parent.mkdir(parents=True, exist_ok=True)
            dest.write_bytes(r.content)
            return dest
        except requests.RequestException:
            time.sleep(3 * (i + 1))
    return None


def parse_zip(path):
    with zipfile.ZipFile(path) as z:
        raw = z.read(z.namelist()[0]).decode()
    first = raw.split("\n", 1)[0]
    header = 0 if not first.split(",")[0].strip().isdigit() else None
    df = pd.read_csv(io.StringIO(raw), header=header, names=None if header == 0 else COLS)
    if header == 0:
        df.columns = COLS[:len(df.columns)]
    t = pd.to_numeric(df["time"])
    unit = "us" if t.iloc[0] > 1e14 else "ms"   # Binance switched spot files to microseconds in 2025
    df["time"] = pd.to_datetime(t, unit=unit, utc=True).dt.tz_localize(None).dt.floor("h")
    return df[[c for c in COLS if c not in ("close_time", "ignore")]]


def binance_symbol(sym, cache):
    keys = [k for k in listing(f"data/spot/monthly/klines/{sym}/1h/") if k.endswith(".zip")]
    if not keys:
        return None, "not listed on Binance spot"
    files = []
    for k in keys:
        files.append(fetch("https://data.binance.vision/" + k, cache / sym / Path(k).name))
    today = dt.datetime.now(dt.timezone.utc).date()
    last_month = max(re.search(r"(\d{4}-\d{2})\.zip$", k).group(1) for k in keys)
    d = (pd.Timestamp(last_month + "-01") + pd.offsets.MonthBegin(1)).date()
    while d < today:
        name = f"{sym}-1h-{d:%Y-%m-%d}.zip"
        # daily files of the open month are re-downloaded each run into a separate, uncached folder
        files.append(fetch(f"https://data.binance.vision/data/spot/daily/klines/{sym}/1h/{name}", cache.parent / "hf_daily" / sym / name))
        d += dt.timedelta(days=1)
    parts = [parse_zip(f) for f in files if f is not None]
    if not parts:
        return None, "no files downloaded"
    df = pd.concat(parts).drop_duplicates("time").sort_values("time")
    return df, "binance"


def coinbase_btc():
    rows, end = [], pd.Timestamp.now(tz="UTC").floor("h")
    start = pd.Timestamp("2016-01-01", tz="UTC")
    t = start
    while t < end:
        t2 = min(t + pd.Timedelta(hours=300), end)
        for i in range(4):
            r = S.get("https://api.exchange.coinbase.com/products/BTC-USD/candles",
                      params={"granularity": 3600, "start": t.isoformat(), "end": t2.isoformat()}, timeout=30)
            if r.status_code == 429:
                time.sleep(2 * (i + 1))
                continue
            r.raise_for_status()
            rows += r.json()
            break
        t = t2
        time.sleep(0.35)
    df = pd.DataFrame(rows, columns=["t", "low", "high", "open", "close", "volume"]).drop_duplicates("t")
    df["time"] = pd.to_datetime(df["t"], unit="s")
    df["quote_volume"] = df["volume"] * df["close"]
    for c in ("trades", "taker_buy_base", "taker_buy_quote"):
        df[c] = float("nan")
    return df[["time", "open", "high", "low", "close", "volume", "quote_volume", "trades", "taker_buy_base",
               "taker_buy_quote"]].sort_values("time")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default="out")
    ap.add_argument("--cache", default="hf_cache")
    a = ap.parse_args()
    out, cache = Path(a.out) / "hf", Path(a.cache)
    out.mkdir(parents=True, exist_ok=True)
    cache.mkdir(parents=True, exist_ok=True)
    status = {}

    def one(base):
        sym = base + "USDT"
        t0 = time.time()
        try:
            df, how = binance_symbol(sym, cache)
            if df is None:
                status[sym] = {"status": "missing", "reason": how}
                return
            df.to_csv(out / f"{sym}.csv.gz", index=False)
            status[sym] = {"status": "ok", "source": how, "rows": int(len(df)), "first": str(df.time.iloc[0]),
                           "last": str(df.time.iloc[-1]), "seconds": round(time.time() - t0, 1)}
            print(f"[ok] {sym} {len(df)} rows {df.time.iloc[0]} .. {df.time.iloc[-1]}", flush=True)
        except Exception as e:
            status[sym] = {"status": "error", "error": f"{type(e).__name__}: {e}"[:300]}
            print(f"[fail] {sym}: {e}", flush=True)

    with ThreadPoolExecutor(8) as ex:
        list(ex.map(one, BASES))
    if status.get("BTCUSDT", {}).get("status") != "ok":
        try:
            df = coinbase_btc()
            df.to_csv(out / "BTCUSDT.csv.gz", index=False)
            status["BTCUSDT"] = {"status": "ok", "source": "coinbase (no taker volume)", "rows": int(len(df)),
                                 "first": str(df.time.iloc[0]), "last": str(df.time.iloc[-1])}
        except Exception as e:
            status["BTCUSDT_coinbase"] = {"status": "error", "error": str(e)[:300]}
    (out / "status.json").write_text(json.dumps({"collected_utc": dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds"),
                                                 "symbols": status}, indent=1))
    ok = sum(v.get("status") == "ok" for v in status.values())
    print(f"hourly data for {ok} symbols")
    if status.get("BTCUSDT", {}).get("status") != "ok":
        raise SystemExit("No hourly Bitcoin data")


if __name__ == "__main__":
    main()
