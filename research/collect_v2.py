"""Free inputs for the version 2 study (see OUTCOMES.md, Version 2). Every source is keyless and public.

- Binance USD-M futures bulk files (data.binance.vision): hourly futures candles with taker buy volume,
  hourly premium index (futures over spot), funding settlements, and the metrics files (open interest and
  long/short ratios, 5-minute snapshots; every day for BTC and ETH, Sundays only for other coins).
- Deribit DVOL, the 30-day implied volatility index from options, hourly, for BTC and ETH.
- Coinbase Exchange hourly candles for BTC-USD and USDT-USD (for the Coinbase premium).
- Scheduled FOMC statement times, from the Federal Reserve's published calendar (typed below).

Every source fails on its own; status.json says what arrived. Output in <out>/v2/.
Usage: python research/collect_v2.py --out out --cache v2_cache
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
from zoneinfo import ZoneInfo

import numpy as np
import pandas as pd

from collect_hf import BASES, S, fetch, listing

BV = "https://data.binance.vision/"
KCOLS = ["time", "open", "high", "low", "close", "volume", "close_time", "quote_volume", "trades",
         "taker_buy_base", "taker_buy_quote", "ignore"]
FULL_METRICS = ("BTCUSDT", "ETHUSDT")
METRICS_START = pd.Timestamp("2021-06-01")
STATUS = {}

# Scheduled FOMC meetings, last day (statement day), from federalreserve.gov/monetarypolicy/fomccalendars.htm
# and the historical pages for 2017-2020. Unscheduled meetings and notation votes are left out because they
# were not known in advance.
FOMC = """2017-09-20 2017-11-01 2017-12-13
2018-01-31 2018-03-21 2018-05-02 2018-06-13 2018-08-01 2018-09-26 2018-11-08 2018-12-19
2019-01-30 2019-03-20 2019-05-01 2019-06-19 2019-07-31 2019-09-18 2019-10-30 2019-12-11
2020-01-29 2020-04-29 2020-06-10 2020-07-29 2020-09-16 2020-11-05 2020-12-16
2021-01-27 2021-03-17 2021-04-28 2021-06-16 2021-07-28 2021-09-22 2021-11-03 2021-12-15
2022-01-26 2022-03-16 2022-05-04 2022-06-15 2022-07-27 2022-09-21 2022-11-02 2022-12-14
2023-02-01 2023-03-22 2023-05-03 2023-06-14 2023-07-26 2023-09-20 2023-11-01 2023-12-13
2024-01-31 2024-03-20 2024-05-01 2024-06-12 2024-07-31 2024-09-18 2024-11-07 2024-12-18
2025-01-29 2025-03-19 2025-05-07 2025-06-18 2025-07-30 2025-09-17 2025-10-29 2025-12-10
2026-01-28 2026-03-18 2026-04-29 2026-06-17 2026-07-29 2026-09-16 2026-10-28 2026-12-09
2027-01-27 2027-03-17 2027-04-28 2027-06-09 2027-07-28 2027-09-15 2027-10-27 2027-12-08"""


def read_zip(path):
    with zipfile.ZipFile(path) as z:
        raw = z.read(z.namelist()[0]).decode()
    first = raw.split("\n", 1)[0].split(",")[0].strip()
    header = not re.fullmatch(r"-?[\d.]+", first)
    return pd.read_csv(io.StringIO(raw), header=0 if header else None)


def to_time(x):
    """Milliseconds or microseconds since the epoch, or a date string, to naive UTC timestamps."""
    if np.issubdtype(np.asarray(x).dtype, np.number):
        t = pd.to_numeric(x)
        unit = "us" if t.iloc[0] > 1e14 else "ms"
        return pd.to_datetime(t, unit=unit)
    return pd.to_datetime(x, format="mixed")


def monthly_and_daily(kind, sym, cache, interval="1h"):
    """Monthly zips plus daily zips for the month that has no monthly file yet."""
    sub = f"{sym}/{interval}/" if interval else f"{sym}/"
    keys = [k for k in listing(f"data/futures/um/monthly/{kind}/{sub}") if k.endswith(".zip")]
    if not keys:
        return []
    files = [fetch(BV + k, cache / kind / sym / Path(k).name) for k in keys]
    if interval:
        last = max(re.search(r"(\d{4}-\d{2})\.zip$", k).group(1) for k in keys)
        d = (pd.Timestamp(last + "-01") + pd.offsets.MonthBegin(1)).date()
        today = dt.datetime.now(dt.timezone.utc).date()
        while d < today:
            name = f"{sym}-{interval}-{d:%Y-%m-%d}.zip"
            files.append(fetch(f"{BV}data/futures/um/daily/{kind}/{sym}/{interval}/{name}", cache / kind / sym / name))
            d += dt.timedelta(days=1)
    return [f for f in files if f is not None]


def klines(files):
    parts = []
    for f in files:
        df = read_zip(f)
        df = df.iloc[:, :len(KCOLS)]
        df.columns = KCOLS[:df.shape[1]]
        df["time"] = to_time(df["time"]).dt.floor("h")
        parts.append(df)
    if not parts:
        return None
    return pd.concat(parts).drop_duplicates("time", keep="last").set_index("time").sort_index()


def futures_symbol(base):
    for sym in (base + "USDT", "1000" + base + "USDT"):
        if listing(f"data/futures/um/monthly/klines/{sym}/1h/"):
            return sym
    return None


def one_coin(base, cache, out):
    t0 = time.time()
    spot = base + "USDT"
    st = {}
    try:
        sym = futures_symbol(base)
        if sym is None:
            STATUS[spot] = {"status": "missing", "reason": "no USD-M perpetual on Binance"}
            return
        st["futures_symbol"] = sym
        k = klines(monthly_and_daily("klines", sym, cache))
        frame = pd.DataFrame(index=k.index)
        frame["fut_close"] = k["close"].astype(float)
        frame["fut_qv"] = k["quote_volume"].astype(float)
        frame["fut_tbq"] = k["taker_buy_quote"].astype(float)
        try:
            p = klines(monthly_and_daily("premiumIndexKlines", sym, cache))
            frame = frame.join(p["close"].astype(float).rename("premium"), how="outer")
            st["premium"] = "ok"
        except Exception as e:
            st["premium"] = f"error: {e}"[:200]
        try:
            parts = [read_zip(f) for f in monthly_and_daily("fundingRate", sym, cache, interval=None)]
            fr = pd.concat(parts)
            tcol = [c for c in fr.columns if "time" in str(c).lower()]
            rcol = [c for c in fr.columns if "rate" in str(c).lower()]
            if not tcol or not rcol:                 # files without a header: calc_time, interval, rate
                tcol, rcol = [fr.columns[0]], [fr.columns[-1]]
            s = pd.Series(pd.to_numeric(fr[rcol[0]], errors="coerce").values, index=to_time(fr[tcol[0]]).dt.floor("h"))
            frame = frame.join(s.groupby(level=0).last().rename("funding"), how="outer")
            st["funding"] = "ok"
        except Exception as e:
            st["funding"] = f"error: {e}"[:200]
        frame.index.name = "time"
        frame.to_csv(out / f"fut_{spot}.csv.gz")
        try:
            m = metrics(sym, cache, full=spot in FULL_METRICS)
            if m is not None:
                m.to_csv(out / f"metrics_{spot}.csv.gz")
                st["metrics_rows"] = int(len(m))
        except Exception as e:
            st["metrics"] = f"error: {e}"[:200]
        st.update(status="ok", rows=int(len(frame)), first=str(frame.index.min()), last=str(frame.index.max()),
                  seconds=round(time.time() - t0, 1))
        STATUS[spot] = st
        print(f"[ok] {spot} via {sym}: {len(frame)} hours, metrics {st.get('metrics_rows', st.get('metrics'))}", flush=True)
    except Exception as e:
        STATUS[spot] = {"status": "error", "error": f"{type(e).__name__}: {e}"[:300], **st}
        print(f"[fail] {spot}: {e}", flush=True)


MCOLS = {"sum_open_interest_value": "oi_value", "sum_toptrader_long_short_ratio": "top_ls_pos",
         "count_toptrader_long_short_ratio": "top_ls_acct", "count_long_short_ratio": "ls_acct",
         "sum_taker_long_short_vol_ratio": "taker_ls"}


def metrics(sym, cache, full):
    keys = [k for k in listing(f"data/futures/um/daily/metrics/{sym}/") if k.endswith(".zip")]
    rows = []
    for k in keys:
        day = pd.Timestamp(re.search(r"(\d{4}-\d{2}-\d{2})\.zip$", k).group(1))
        if day < METRICS_START or (not full and day.dayofweek != 6):
            continue
        f = fetch(BV + k, cache / "metrics" / sym / Path(k).name)
        if f is None:
            continue
        df = read_zip(f)
        if "create_time" not in df.columns:
            continue
        t = to_time(df["create_time"])
        # a snapshot taken at hh:mm belongs to the hour whose candle closes at or after it
        df.index = (t - pd.Timedelta(microseconds=1)).dt.floor("h")
        keep = {c: n for c, n in MCOLS.items() if c in df.columns}
        rows.append(df[list(keep)].rename(columns=keep).apply(pd.to_numeric, errors="coerce").groupby(level=0).last())
    if not rows:
        return None
    m = pd.concat(rows).sort_index()
    m = m[~m.index.duplicated(keep="last")]
    m.index.name = "time"
    return m


def deribit_dvol(cur):
    end = int(pd.Timestamp.now(tz="UTC").timestamp() * 1000)
    start = int(pd.Timestamp("2021-03-01", tz="UTC").timestamp() * 1000)
    rows = []
    for _ in range(400):
        r = S.get("https://www.deribit.com/api/v2/public/get_volatility_index_data",
                  params={"currency": cur, "start_timestamp": start, "end_timestamp": end, "resolution": "3600"}, timeout=30)
        r.raise_for_status()
        res = r.json()["result"]
        data = res.get("data") or []
        rows += data
        cont = res.get("continuation")
        if not data or cont is None or cont <= start:
            break
        end = int(cont)
        time.sleep(0.2)
    df = pd.DataFrame(rows, columns=["t", "open", "high", "low", "close"]).drop_duplicates("t")
    # candles are stamped at their start; the close is treated as known one hour after the stamp of the next
    # candle (a conservative extra hour in case the stamp is the candle end)
    df["time"] = pd.to_datetime(df["t"], unit="ms").dt.floor("h") + pd.Timedelta(hours=1)
    return df.set_index("time").sort_index()[["close"]].rename(columns={"close": "dvol"})


def coinbase(product, start):
    rows, end = [], pd.Timestamp.now(tz="UTC").floor("h")
    t = pd.Timestamp(start, tz="UTC")
    while t < end:
        t2 = min(t + pd.Timedelta(hours=300), end)
        for i in range(5):
            r = S.get(f"https://api.exchange.coinbase.com/products/{product}/candles",
                      params={"granularity": 3600, "start": t.isoformat(), "end": t2.isoformat()}, timeout=30)
            if r.status_code == 429:
                time.sleep(2 * (i + 1))
                continue
            r.raise_for_status()
            rows += r.json()
            break
        t = t2
        time.sleep(0.34)
    df = pd.DataFrame(rows, columns=["t", "low", "high", "open", "close", "volume"]).drop_duplicates("t")
    df["time"] = pd.to_datetime(df["t"], unit="s")
    return df.set_index("time").sort_index()[["close"]]


def fomc_frame():
    ny = ZoneInfo("America/New_York")
    times = [pd.Timestamp(dt.datetime.fromisoformat(d + "T14:00").replace(tzinfo=ny)).tz_convert("UTC").tz_localize(None)
             for d in FOMC.split()]
    return pd.DataFrame({"statement_utc": times})


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default="out")
    ap.add_argument("--cache", default="v2_cache")
    ap.add_argument("--coins", type=int, default=0, help="limit the number of coins (testing)")
    a = ap.parse_args()
    out, cache = Path(a.out) / "v2", Path(a.cache)
    out.mkdir(parents=True, exist_ok=True)
    cache.mkdir(parents=True, exist_ok=True)
    fomc_frame().to_csv(out / "fomc.csv", index=False)
    STATUS["fomc"] = {"status": "ok", "rows": len(FOMC.split())}
    for cur in ("BTC", "ETH"):
        try:
            d = deribit_dvol(cur)
            d.to_csv(out / f"dvol_{cur}.csv")
            STATUS[f"dvol_{cur}"] = {"status": "ok", "rows": int(len(d)), "first": str(d.index.min()), "last": str(d.index.max())}
            print(f"[ok] DVOL {cur}: {len(d)} hours from {d.index.min()}", flush=True)
        except Exception as e:
            STATUS[f"dvol_{cur}"] = {"status": "error", "error": f"{type(e).__name__}: {e}"[:300]}
            print(f"[fail] DVOL {cur}: {e}", flush=True)
    for product, start in (("BTC-USD", "2017-08-01"), ("USDT-USD", "2021-01-01")):
        try:
            c = coinbase(product, start)
            c.to_csv(out / f"coinbase_{product}.csv")
            STATUS[f"coinbase_{product}"] = {"status": "ok", "rows": int(len(c)), "first": str(c.index.min()), "last": str(c.index.max())}
            print(f"[ok] Coinbase {product}: {len(c)} hours", flush=True)
        except Exception as e:
            STATUS[f"coinbase_{product}"] = {"status": "error", "error": f"{type(e).__name__}: {e}"[:300]}
            print(f"[fail] Coinbase {product}: {e}", flush=True)
    bases = BASES[:a.coins] if a.coins else BASES
    with ThreadPoolExecutor(12) as ex:
        list(ex.map(lambda b: one_coin(b, cache, out), bases))
    (out / "status.json").write_text(json.dumps({"collected_utc": dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds"),
                                                 "sources": STATUS}, indent=1))
    ok = sum(v.get("status") == "ok" for v in STATUS.values())
    print(f"version 2 inputs: {ok} of {len(STATUS)} sources ok")


if __name__ == "__main__":
    main()
