"""Collect every daily variable the research models use, from free public sources.

Each series is saved as <out>/raw/<name>.csv with columns date,value and described in
<out>/status.json (source, kind, publication lag, coverage, success or the error).
A failing source never stops the run; it is recorded and the models work without it.

Usage: python research/collect.py --out out/data
"""
import argparse
import datetime as dt
import io
import json
import time
import traceback
from pathlib import Path

import pandas as pd
import requests

UA = {"User-Agent": "crypto-concordance-board research (https://github.com/sandordrpal/crypto-concordance-board)"}
TODAY = dt.datetime.now(dt.timezone.utc).date()
START = "2013-01-01"

# kind decides the feature transforms: price = traded price, count = growing quantity,
# level = bounded or mean-reverting level. lag = days after the stamped date when the
# value is safely public (prevents look-ahead).
CATALOG = {}
STATUS = {}


def save(out, name, s, source, kind, lag, desc):
    s = pd.Series(s).dropna()
    s.index = pd.to_datetime(s.index).tz_localize(None).normalize()
    s = s[~s.index.duplicated(keep="last")].sort_index()
    s = s[s.index >= "2010-01-01"]
    if len(s) < 30:
        raise ValueError(f"only {len(s)} rows")
    df = pd.DataFrame({"date": s.index.strftime("%Y-%m-%d"), "value": s.values})
    df.to_csv(out / "raw" / f"{name}.csv", index=False)
    STATUS[name] = {"status": "ok", "source": source, "kind": kind, "lag_days": lag, "description": desc,
                    "rows": int(len(s)), "first": df.date.iloc[0], "last": df.date.iloc[-1]}


def attempt(name, source, fn):
    t0 = time.time()
    try:
        fn()
    except Exception as e:  # record and move on
        STATUS[name] = {"status": "error", "source": source, "error": f"{type(e).__name__}: {e}"[:400]}
        print(f"[fail] {name}: {e}")
        traceback.print_exc()
    else:
        print(f"[ok]   {name} ({time.time() - t0:.1f}s)")


def get(url, **kw):
    for i in range(3):
        try:
            r = requests.get(url, headers=UA, timeout=60, **kw)
            if r.status_code == 429:
                time.sleep(10 * (i + 1))
                continue
            r.raise_for_status()
            return r
        except requests.RequestException:
            if i == 2:
                raise
            time.sleep(5 * (i + 1))
    raise RuntimeError("rate limited")


# ---------------------------------------------------------------- sources
def yahoo(out):
    import yfinance as yf
    tickers = {
        "BTC-USD": ("btc", "price", "Bitcoin price, USD (Yahoo, daily close 00:00 UTC)"),
        "ETH-USD": ("eth", "price", "Ether price, USD"),
        "^GSPC": ("sp500", "price", "S&P 500 index"),
        "^IXIC": ("nasdaq", "price", "Nasdaq Composite index"),
        "^VIX": ("vix", "level", "CBOE VIX equity volatility index"),
        "^MOVE": ("move", "level", "ICE BofA MOVE bond volatility index"),
        "DX-Y.NYB": ("dxy", "price", "US dollar index"),
        "GC=F": ("gold", "price", "Gold futures"),
        "CL=F": ("oil", "price", "WTI crude oil futures"),
        "^TNX": ("ust10y_yahoo", "level", "US 10-year Treasury yield (Yahoo)"),
        "MSTR": ("mstr", "price", "MicroStrategy / Strategy share price"),
        "COIN": ("coin", "price", "Coinbase share price"),
    }
    for tk, (name, kind, desc) in tickers.items():
        def one(tk=tk, name=name, kind=kind, desc=desc):
            df = None
            for i in range(3):
                df = yf.download(tk, start=START, interval="1d", auto_adjust=True, progress=False, threads=False)
                if df is not None and len(df):
                    break
                time.sleep(5 * (i + 1))
            if df is None or not len(df):
                raise ValueError("no rows from Yahoo")
            if isinstance(df.columns, pd.MultiIndex):
                df.columns = df.columns.get_level_values(0)
            save(out, name, df["Close"], "Yahoo Finance", kind, 0, desc)
            if name == "btc" and "Volume" in df:
                save(out, "btc_volume", df["Volume"].replace(0, pd.NA), "Yahoo Finance", "count", 0, "Bitcoin traded volume, USD")
        attempt(name, "Yahoo Finance", one)
        time.sleep(1.5)


def coinmetrics(out):
    metrics = {
        "PriceUSD": ("cm_price", "price", "Bitcoin reference price, USD (Coin Metrics)"),
        "CapMVRVCur": ("cm_mvrv", "level", "Market value to realized value"),
        "AdrActCnt": ("cm_active_addresses", "count", "Active addresses"),
        "TxCnt": ("cm_tx_count", "count", "Transactions"),
        "HashRate": ("cm_hashrate", "count", "Hash rate"),
        "IssTotUSD": ("cm_issuance", "count", "Miner issuance, USD"),
        "FlowInExUSD": ("cm_exchange_inflow", "count", "Exchange inflow, USD"),
        "FlowOutExUSD": ("cm_exchange_outflow", "count", "Exchange outflow, USD"),
        "SplyExNtv": ("cm_exchange_supply", "count", "BTC held on exchanges"),
    }
    for m, (name, kind, desc) in metrics.items():
        def one(m=m, name=name, kind=kind, desc=desc):
            url = "https://community-api.coinmetrics.io/v4/timeseries/asset-metrics"
            params = {"assets": "btc", "metrics": m, "frequency": "1d", "start_time": START, "page_size": 10000}
            rows = []
            r = get(url, params=params).json()
            rows += r.get("data", [])
            while r.get("next_page_url"):
                time.sleep(0.8)
                r = get(r["next_page_url"]).json()
                rows += r.get("data", [])
            if not rows:
                raise ValueError("no data (metric may not be in the free tier)")
            s = pd.Series({x["time"][:10]: float(x[m]) for x in rows if x.get(m) not in (None, "")})
            save(out, name, s, "Coin Metrics community API", kind, 1, desc)
        attempt(name, "Coin Metrics", one)
        time.sleep(0.8)


def fred(out):
    series = {
        "DFF": ("fed_funds", "level", 1, "Effective federal funds rate"),
        "DGS2": ("ust2y", "level", 1, "US 2-year Treasury yield"),
        "DGS10": ("ust10y", "level", 1, "US 10-year Treasury yield"),
        "T10Y2Y": ("curve_10y2y", "level", 1, "10-year minus 2-year Treasury spread"),
        "T5YIE": ("breakeven5y", "level", 1, "5-year breakeven inflation"),
        "BAMLH0A0HYM2": ("hy_spread", "level", 1, "US high-yield credit spread"),
        "DTWEXBGS": ("usd_broad", "price", 1, "Broad trade-weighted US dollar"),
        "RRPONTSYD": ("reverse_repo", "count", 1, "Fed overnight reverse repo"),
        "WALCL": ("fed_balance_sheet", "count", 2, "Fed total assets (weekly)"),
        "WTREGEN": ("treasury_account", "count", 2, "US Treasury General Account (weekly)"),
        "M2SL": ("m2", "count", 60, "US M2 money supply (monthly)"),
        "USEPUINDXD": ("epu_us", "level", 1, "US Economic Policy Uncertainty, news-based (daily)"),
        "WLEMUINDXD": ("emu_us", "level", 1, "Equity market uncertainty, news-based (daily)"),
        "NFCI": ("fin_conditions", "level", 7, "Chicago Fed financial conditions (weekly)"),
    }
    for sid, (name, kind, lag, desc) in series.items():
        def one(sid=sid, name=name, kind=kind, lag=lag, desc=desc):
            r = get("https://fred.stlouisfed.org/graph/fredgraph.csv", params={"id": sid})
            df = pd.read_csv(io.StringIO(r.text))
            dcol = df.columns[0]
            s = pd.to_numeric(df[sid], errors="coerce")
            s.index = pd.to_datetime(df[dcol])
            save(out, name, s, "FRED (St. Louis Fed)", kind, lag, desc)
        attempt(name, "FRED", one)
        time.sleep(0.5)


def fear_greed(out):
    def one():
        j = get("https://api.alternative.me/fng/", params={"limit": 0, "format": "json"}).json()
        s = pd.Series({dt.datetime.fromtimestamp(int(d["timestamp"]), dt.timezone.utc).date(): float(d["value"]) for d in j["data"]})
        save(out, "fear_greed", s, "alternative.me", "level", 0, "Crypto Fear & Greed Index")
    attempt("fear_greed", "alternative.me", one)


def gpr(out):
    def one():
        r = get("https://www.matteoiacoviello.com/gpr_files/data_gpr_daily_recent.xls")
        df = pd.read_excel(io.BytesIO(r.content))
        cols = {c.lower(): c for c in df.columns}
        if "date" in cols:
            d = pd.to_datetime(df[cols["date"]], errors="coerce")
        else:
            d = pd.to_datetime(df[cols["day"]].astype(str), format="%Y%m%d", errors="coerce")
        for key, name, desc in [("gprd", "gpr", "Geopolitical risk index, news-based (daily)"),
                                ("gprd_act", "gpr_acts", "Geopolitical acts index (daily)"),
                                ("gprd_threat", "gpr_threats", "Geopolitical threats index (daily)")]:
            if key in cols:
                s = pd.to_numeric(df[cols[key]], errors="coerce")
                s.index = d
                save(out, name, s, "Caldara & Iacoviello GPR", "level", 1, desc)
        if "gpr" not in STATUS:
            raise ValueError(f"GPRD column not found in {list(df.columns)[:12]}")
    attempt("gpr", "Caldara & Iacoviello", one)


def wikipedia(out):
    for article, name in [("Bitcoin", "wiki_bitcoin"), ("Cryptocurrency", "wiki_crypto")]:
        def one(article=article, name=name):
            url = (f"https://wikimedia.org/api/rest_v1/metrics/pageviews/per-article/en.wikipedia/all-access/user/"
                   f"{article}/daily/20150701/{TODAY:%Y%m%d}")
            items = get(url).json()["items"]
            s = pd.Series({pd.to_datetime(x["timestamp"][:8]): float(x["views"]) for x in items})
            save(out, name, s, "Wikimedia pageviews", "count", 1, f"English Wikipedia views of '{article}'")
        attempt(name, "Wikimedia", one)


def stablecoins(out):
    def one():
        j = get("https://stablecoins.llama.fi/stablecoincharts/all").json()
        s = pd.Series({dt.datetime.fromtimestamp(int(x["date"]), dt.timezone.utc).date():
                       float((x.get("totalCirculatingUSD") or {}).get("peggedUSD") or 0) or None for x in j})
        save(out, "stablecoin_supply", s, "DefiLlama", "count", 1, "Total USD stablecoin supply")
    attempt("stablecoin_supply", "DefiLlama", one)


def gdelt(out):
    queries = {"news_tone_bitcoin": ("bitcoin", "timelinetone", "Average tone of world news mentioning bitcoin"),
               "news_volume_bitcoin": ("bitcoin", "timelinevolraw", "Number of world news articles mentioning bitcoin"),
               "news_tone_macro": ('(inflation OR recession OR "interest rates" OR tariffs)', "timelinetone",
                                   "Average tone of world news on inflation, recession, rates and tariffs"),
               "news_tone_conflict": ("(war OR sanctions OR missile)", "timelinetone", "Average tone of world news on war and sanctions")}
    for name, (q, mode, desc) in queries.items():
        def one(name=name, q=q, mode=mode, desc=desc):
            params = {"query": q, "mode": mode, "format": "csv", "startdatetime": "20170101000000",
                      "enddatetime": f"{TODAY:%Y%m%d}235959"}
            r = None
            for i in range(5):
                r = requests.get("https://api.gdeltproject.org/api/v2/doc/doc", params=params, headers=UA, timeout=90)
                if r.status_code == 429 or "limit requests" in r.text[:300].lower():
                    time.sleep(20 * (i + 1))
                    continue
                r.raise_for_status()
                break
            else:
                raise RuntimeError("GDELT rate limit persisted")
            df = pd.read_csv(io.StringIO(r.text))
            df.columns = [c.strip().lower() for c in df.columns]
            vcol = "value" if "value" in df else df.columns[-1]
            d = pd.to_datetime(df["date"], errors="coerce").dt.normalize()
            if "series" in df and mode == "timelinevolraw":
                df = df[df["series"].astype(str).str.contains("Article Count|Volume", case=False, regex=True)] if df["series"].nunique() > 1 else df
                d = pd.to_datetime(df["date"], errors="coerce").dt.normalize()
            s = pd.to_numeric(df[vcol], errors="coerce").groupby(d).mean()
            kind = "count" if mode == "timelinevolraw" else "level"
            save(out, name, s, "GDELT 2.0 DOC API", kind, 1, desc)
        attempt(name, "GDELT", one)
        time.sleep(12)


def funding(out):
    def binance():
        rows, start = [], int(dt.datetime(2019, 9, 1, tzinfo=dt.timezone.utc).timestamp() * 1000)
        while True:
            r = requests.get("https://fapi.binance.com/fapi/v1/fundingRate", headers=UA, timeout=30,
                             params={"symbol": "BTCUSDT", "startTime": start, "limit": 1000})
            if r.status_code != 200:
                raise RuntimeError(f"Binance HTTP {r.status_code}")
            batch = r.json()
            if not batch:
                break
            rows += batch
            start = batch[-1]["fundingTime"] + 1
            if len(batch) < 1000:
                break
            time.sleep(0.3)
        return pd.Series({pd.to_datetime(x["fundingTime"], unit="ms"): float(x["fundingRate"]) for x in rows}), "Binance"

    def bitmex():
        rows, since = [], "2016-05-01T00:00:00.000Z"
        for _ in range(200):
            r = requests.get("https://www.bitmex.com/api/v1/funding", headers=UA, timeout=30,
                             params={"symbol": "XBTUSD", "count": 500, "startTime": since, "reverse": "false"})
            if r.status_code == 429:
                time.sleep(30)
                continue
            if r.status_code != 200:
                raise RuntimeError(f"BitMEX HTTP {r.status_code}")
            batch = r.json()
            if not batch:
                break
            rows += batch
            nxt = (pd.Timestamp(batch[-1]["timestamp"]) + pd.Timedelta(seconds=1)).strftime("%Y-%m-%dT%H:%M:%S.000Z")
            if len(batch) < 500 or nxt == since:
                break
            since = nxt
            time.sleep(2.2)
        return pd.Series({pd.to_datetime(x["timestamp"]): float(x["fundingRate"]) for x in rows}), "BitMEX"

    def one():
        errs = []
        for fn in (binance, bitmex):
            try:
                s, src = fn()
                if len(s) > 300:
                    s.index = pd.to_datetime(s.index).tz_localize(None) if getattr(s.index, "tz", None) else s.index
                    daily = s.groupby(pd.to_datetime(s.index).normalize()).mean()
                    save(out, "funding_rate", daily, src, "level", 0, f"BTC perpetual funding rate, daily mean ({src})")
                    return
                errs.append(f"{fn.__name__}: only {len(s)} rows")
            except Exception as e:
                errs.append(f"{fn.__name__}: {e}")
        raise RuntimeError("; ".join(errs))
    attempt("funding_rate", "Binance or BitMEX", one)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default="out/data")
    a = ap.parse_args()
    out = Path(a.out)
    (out / "raw").mkdir(parents=True, exist_ok=True)
    for fn in (yahoo, coinmetrics, fred, fear_greed, gpr, wikipedia, stablecoins, gdelt, funding):
        print(f"== {fn.__name__}")
        try:
            fn(out)
        except Exception as e:
            STATUS[fn.__name__] = {"status": "error", "source": fn.__name__, "error": str(e)[:400]}
    meta = {"collected_utc": dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds"), "series": STATUS}
    (out / "status.json").write_text(json.dumps(meta, indent=1))
    ok = sum(1 for v in STATUS.values() if v["status"] == "ok")
    print(f"collected {ok} of {len(STATUS)} series")
    if "btc" not in STATUS or STATUS["btc"]["status"] != "ok":
        if STATUS.get("cm_price", {}).get("status") != "ok":
            raise SystemExit("No Bitcoin price series; cannot continue")


if __name__ == "__main__":
    main()
