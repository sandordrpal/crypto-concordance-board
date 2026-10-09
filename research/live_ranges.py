"""Live calibration test of the board's "typical size of the next move" ranges (see LIVE_TEST.md, R1-R4).

Every run (hourly on GitHub Actions):
1. issue: for each of the 50 frozen coins, compute the board's ranges from the last 720 closed hourly
   candles and append them to ranges_issued.csv with the issue time, before the outcome is known;
   hours that a delayed or skipped run missed are back-filled and flagged late=1;
2. score: once the next 1 and 24 hours have closed, append the realised move to ranges_outcomes.csv;
3. report: rebuild REPORT.md with coverage, confidence intervals and the pre-registered verdicts.

The rule is copied exactly from index.html (histCoin): ranges are the 68th and 95th percentiles of the
absolute 1-hour and overlapping 24-hour log returns over the last 720 closed hours, with linear
interpolation between order statistics. Files are only ever appended to; nothing is rewritten.

Usage: python research/live_ranges.py --log live-log
"""
import argparse
import datetime as dt
import json
import time
from pathlib import Path

import numpy as np
import pandas as pd
import requests

# board candidate list, in the board's order (index.html CANDIDATES); the first 50 Binance lists are frozen
CANDIDATES = ["BTC", "ETH", "XRP", "BNB", "SOL", "DOGE", "TRX", "ADA", "LINK", "AVAX", "SUI", "XLM", "BCH", "HBAR", "LTC",
              "TON", "SHIB", "DOT", "UNI", "AAVE", "NEAR", "PEPE", "TAO", "APT", "ICP", "ETC", "ONDO", "ENA", "POL", "ARB",
              "ATOM", "ALGO", "RENDER", "FIL", "VET", "WLD", "OP", "INJ", "SEI", "FET", "TIA", "STX", "JUP", "BONK", "IMX",
              "GRT", "LDO", "CRV", "WIF", "ZEC", "QNT", "PENGU", "TRUMP", "PYTH", "FLOKI", "XTZ", "SAND", "THETA", "RUNE",
              "GALA", "MANA", "CAKE", "EGLD", "IOTA"]
N_COINS, WINDOW, MIN_OBS = 50, 720, 100
DAY0 = pd.Timestamp("2026-10-19 00:00")          # primary analysis starts here; earlier rows are a run-in
HOSTS = ["https://data-api.binance.vision", "https://api.binance.com", "https://api-gcp.binance.com", "https://api1.binance.com"]
S = requests.Session()
S.headers.update({"User-Agent": "crypto-concordance-board live calibration (github.com/sandordrpal/crypto-concordance-board)"})
ISSUED_COLS = ["issued_utc", "as_of_utc", "coin", "base_close", "h1_68", "h1_95", "h24_68", "h24_95", "n1", "n24", "source", "late"]
OUT_COLS = ["as_of_utc", "coin", "horizon_h", "realized_abs_logret", "range_68", "range_95", "in_68", "in_95", "late", "scored_utc"]


def quantile(a, q):
    a = np.sort(np.asarray(a, float))
    pos = (len(a) - 1) * q
    lo, hi = int(np.floor(pos)), int(np.ceil(pos))
    return float(a[lo] + (a[hi] - a[lo]) * (pos - lo))


def ranges_at(closes):
    """Board rule on a series of closed hourly closes ending at the as-of hour."""
    c = np.asarray(closes, float)
    lr = np.diff(np.log(c))
    a1 = np.abs(lr[-WINDOW:])
    a24 = np.abs(np.log(c[24:] / c[:-24]))[-WINDOW:]
    a1, a24 = a1[np.isfinite(a1)], a24[np.isfinite(a24)]
    if len(a1) < MIN_OBS or len(a24) < MIN_OBS:
        return None
    return {"h1_68": quantile(a1, 0.68), "h1_95": quantile(a1, 0.95), "h24_68": quantile(a24, 0.68),
            "h24_95": quantile(a24, 0.95), "n1": len(a1), "n24": len(a24)}


def fetch(sym, hosts):
    """Last 1000 closed hourly candles as a Series of closes indexed by close time (UTC, naive)."""
    last = None
    for h in hosts:
        for i in range(3):
            try:
                r = S.get(f"{h}/api/v3/klines", params={"symbol": sym, "interval": "1h", "limit": 1000}, timeout=20)
                if r.status_code in (418, 429):
                    time.sleep(5 * (i + 1))
                    continue
                if r.status_code in (403, 451):
                    last = f"{h} HTTP {r.status_code}"
                    break
                r.raise_for_status()
                rows = r.json()
                now_ms = time.time() * 1000
                rows = [x for x in rows if x[6] < now_ms]          # closed candles only
                close_t = pd.to_datetime([x[6] + 1 for x in rows], unit="ms")
                return pd.Series([float(x[4]) for x in rows], index=close_t), h
            except Exception as e:
                last = f"{h} {type(e).__name__}"
                time.sleep(1)
    raise RuntimeError(last or "no host answered")


def append(path, df, cols):
    df = df[cols]
    df.to_csv(path, mode="a", header=not path.exists(), index=False)


def nw_ci(x, lags, level=0.90):
    x = np.asarray(x, float)
    x = x[np.isfinite(x)]
    n = len(x)
    if n < 10:
        return np.nan, np.nan, np.nan, n
    m = x.mean()
    d = x - m
    v = d @ d / n
    for k in range(1, min(lags, n - 1) + 1):
        v += 2 * (1 - k / (lags + 1)) * (d[k:] @ d[:-k]) / n
    z = {0.90: 1.6449, 0.95: 1.96}[level]
    se = np.sqrt(max(v, 0) / n)
    return m, m - z * se, m + z * se, n


BANDS = {"68": (0.63, 0.73), "95": (0.92, 0.98)}
MIN_HOURS = {1: 7 * 24, 24: 14 * 24}


def verdict(lo, hi, band):
    if not np.isfinite(lo):
        return "too few data yet"
    if band[0] <= lo and hi <= band[1]:
        return "PASS"
    if hi < band[0] or lo > band[1]:
        return "FAIL"
    return "inconclusive"


def report(log):
    o = pd.read_csv(log / "ranges_outcomes.csv", parse_dates=["as_of_utc"]) if (log / "ranges_outcomes.csv").exists() else pd.DataFrame(columns=OUT_COLS)
    L = ["# Live calibration of the board's typical-move ranges", "",
         f"Updated {dt.datetime.now(dt.timezone.utc):%Y-%m-%d %H:%M} UTC. Rules and pass bands are fixed in "
         "[LIVE_TEST.md](https://github.com/sandordrpal/crypto-concordance-board/blob/main/research/LIVE_TEST.md) (R1-R4). "
         f"Primary analysis: on-time forecasts from {DAY0:%Y-%m-%d}; earlier rows are a run-in.", "",
         "Coverage is the share of real moves that stayed inside the range. Confidence intervals (90%) are clustered by "
         "issue hour, because coins move together. PASS when the whole interval lies inside the band.", ""]
    rows = []
    for label, sub in (("Primary (on time, from day 0)", o[(o["late"] == 0) & (o["as_of_utc"] >= DAY0)]),
                       ("All rows from day 0, including back-filled", o[o["as_of_utc"] >= DAY0]),
                       ("Run-in (before day 0)", o[o["as_of_utc"] < DAY0])):
        for hz in (1, 24):
            s = sub[sub["horizon_h"] == hz]
            for lev in ("68", "95"):
                per_hour = s.groupby("as_of_utc")[f"in_{lev}"].mean().sort_index()
                m, lo, hi, n = nw_ci(per_hour.values, 24 if hz == 24 else 6)
                if n < MIN_HOURS[hz]:                  # no verdict on fewer than 7 (1 h) or 14 (24 h) days of issue hours
                    lo = hi = np.nan
                rid = {("1", "68"): "R1", ("1", "95"): "R2", ("24", "68"): "R3", ("24", "95"): "R4"}[(str(hz), lev)]
                rows.append([label, rid, f"next {hz} h", f"{lev}%", len(s), n,
                             "–" if not np.isfinite(m) else f"{100 * m:.1f}%",
                             "–" if not np.isfinite(lo) else f"{100 * lo:.1f}–{100 * hi:.1f}%",
                             f"{100 * BANDS[lev][0]:.0f}–{100 * BANDS[lev][1]:.0f}%", verdict(lo, hi, BANDS[lev])])
    L += ["| Sample | Test | Horizon | Claimed | Forecasts | Issue hours | Coverage | 90% CI | Pass band | Verdict |",
          "|---|---|---|---|---|---|---|---|---|---|"]
    L += ["| " + " | ".join(map(str, r)) + " |" for r in rows]
    prim = o[(o["late"] == 0) & (o["as_of_utc"] >= DAY0)]
    if len(prim):
        by = prim[prim["horizon_h"] == 24].groupby("coin")["in_68"].agg(["mean", "count"]).sort_values("mean")
        if len(by):
            L += ["", "Coins furthest from the 68% claim on the 24-hour range (primary sample):", "",
                  "| Coin | Coverage | Forecasts |", "|---|---|---|"]
            for c, r in pd.concat([by.head(5), by.tail(5)]).iterrows():
                L.append(f"| {c} | {100 * r['mean']:.0f}% | {int(r['count'])} |")
    L += ["", "Information only, not investment advice."]
    (log / "REPORT.md").write_text("\n".join(L) + "\n")
    return rows


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--log", default="live-log")
    a = ap.parse_args()
    log = Path(a.log)
    log.mkdir(parents=True, exist_ok=True)
    now = pd.Timestamp.now(tz="UTC").tz_localize(None)
    status = {"run_utc": str(now), "errors": {}}
    # frozen universe: written on the first run, never changed afterwards
    uf = log / "universe.json"
    data, sources, hosts = {}, {}, list(HOSTS)
    if uf.exists():
        universe = json.loads(uf.read_text())["coins"]
    else:
        universe = []
        for b in CANDIDATES:
            if len(universe) >= N_COINS:
                break
            try:
                data[b], sources[b] = fetch(b + "USDT", hosts)
                universe.append(b)
            except Exception as e:
                status["errors"][b] = str(e)[:200]
        if len(universe) < 10:
            raise SystemExit(f"Could not reach Binance for enough coins: {status['errors']}")
        uf.write_text(json.dumps({"frozen_utc": str(now), "rule": "first 50 board candidates listed on Binance spot",
                                  "coins": universe}, indent=1))
    for b in universe:
        if b in data:
            continue
        try:
            data[b], sources[b] = fetch(b + "USDT", hosts)
        except Exception as e:
            status["errors"][b] = str(e)[:200]
    if not data:
        (log / "last_run.json").write_text(json.dumps(status, indent=1))
        raise SystemExit("No price data this run")
    issued_p, out_p = log / "ranges_issued.csv", log / "ranges_outcomes.csv"
    issued = pd.read_csv(issued_p, parse_dates=["as_of_utc"]) if issued_p.exists() else pd.DataFrame(columns=ISSUED_COLS)
    done = set(zip(issued["as_of_utc"].astype(str), issued["coin"]))
    new_rows = []
    for b, s in data.items():
        s = s[~s.index.duplicated(keep="last")].sort_index()
        latest = s.index[-1]
        # the current hour is on time; up to 48 earlier hours missed by skipped runs are back-filled as late
        for t in s.index[-49:]:
            if (str(t), b) in done:
                continue
            hist = s[s.index <= t]
            r = ranges_at(hist.values[-(WINDOW + 25):])
            if r is None:
                continue
            late = int(not (t == latest and (now - t) <= pd.Timedelta(minutes=59)))
            new_rows.append({"issued_utc": str(now), "as_of_utc": t, "coin": b, "base_close": float(hist.iloc[-1]),
                             **r, "source": sources[b], "late": late})
    if new_rows:
        append(issued_p, pd.DataFrame(new_rows), ISSUED_COLS)
        issued = pd.concat([issued, pd.DataFrame(new_rows)], ignore_index=True)
    # score every issued forecast whose horizon has closed and that is not yet scored
    outs = pd.read_csv(out_p, parse_dates=["as_of_utc"]) if out_p.exists() else pd.DataFrame(columns=OUT_COLS)
    scored = set(zip(outs["as_of_utc"].astype(str), outs["coin"], outs["horizon_h"].astype(int)))
    o_rows = []
    for _, r in issued.iterrows():
        s = data.get(r["coin"])
        if s is None:
            continue
        t0 = pd.Timestamp(r["as_of_utc"])
        for hz, k68, k95 in ((1, "h1_68", "h1_95"), (24, "h24_68", "h24_95")):
            if (str(t0), r["coin"], hz) in scored:
                continue
            t1 = t0 + pd.Timedelta(hours=hz)
            if t1 not in s.index or t0 not in s.index:
                continue
            mv = abs(float(np.log(s[t1] / s[t0])))
            o_rows.append({"as_of_utc": t0, "coin": r["coin"], "horizon_h": hz, "realized_abs_logret": mv,
                           "range_68": r[k68], "range_95": r[k95], "in_68": int(mv <= r[k68]), "in_95": int(mv <= r[k95]),
                           "late": int(r["late"]), "scored_utc": str(now)})
    if o_rows:
        append(out_p, pd.DataFrame(o_rows), OUT_COLS)
    report(log)
    status.update(issued=len(new_rows), scored=len(o_rows), coins_with_data=len(data), sources=sorted(set(sources.values())))
    (log / "last_run.json").write_text(json.dumps(status, indent=1))
    print(json.dumps(status))


if __name__ == "__main__":
    main()
