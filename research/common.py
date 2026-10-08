"""Shared helpers for the research tracks: data loading, tests and performance statistics."""
import json
from pathlib import Path

import numpy as np
import pandas as pd
from scipy.stats import norm

COST = 0.001          # 10 bp per side
WF_START = pd.Timestamp("2021-01-01")


def load_hourly(hf_dir, sym):
    f = Path(hf_dir) / f"{sym}.csv.gz"
    if not f.exists():
        return None
    df = pd.read_csv(f)
    df["time"] = pd.to_datetime(df["time"], format="mixed").dt.floor("h")   # files mix second and microsecond formats
    df = df.set_index("time").sort_index()
    df = df[~df.index.duplicated(keep="last")]
    today = pd.Timestamp.now(tz="UTC").floor("h").tz_localize(None)
    df = df[df.index < today]                       # drop the hour that is still forming
    full = pd.date_range(df.index.min(), df.index.max(), freq="h")
    df = df.reindex(full)
    df["close"] = df["close"].ffill(limit=6)
    for c in ("open", "high", "low"):
        df[c] = df[c].fillna(df["close"])
    for c in ("volume", "quote_volume", "trades", "taker_buy_base", "taker_buy_quote"):
        df[c] = df[c].fillna(0.0)
    return df


def hourly_symbols(hf_dir):
    st = json.loads((Path(hf_dir) / "status.json").read_text())["symbols"]
    return [s for s, v in st.items() if v.get("status") == "ok" and (Path(hf_dir) / f"{s}.csv.gz").exists()]


def load_daily_research(data_dir):
    """Daily research variables from collect.py as {name: (series, meta)}."""
    p = Path(data_dir)
    if not (p / "status.json").exists():
        return {}
    st = json.loads((p / "status.json").read_text())["series"]
    out = {}
    for name, meta in st.items():
        f = p / "raw" / f"{name}.csv"
        if meta.get("status") == "ok" and f.exists():
            df = pd.read_csv(f)
            s = pd.Series(pd.to_numeric(df["value"], errors="coerce").values, index=pd.to_datetime(df["date"])).dropna()
            out[name] = (s[~s.index.duplicated(keep="last")].sort_index(), meta)
    return out


def daily_aligned(s, index, lag):
    """Reindex a daily (or slower) series to `index` days, forward fill, and hold back `lag` days."""
    gaps = np.diff(s.index.values).astype("timedelta64[D]").astype(float)
    spacing = float(np.median(gaps)) if len(gaps) else 1.0
    limit = 5 if spacing <= 1.5 else 10 if spacing <= 8 else 40
    return s.reindex(index.union(s.index)).sort_index().ffill(limit=limit).reindex(index).shift(lag)


def nw_var(x, lags):
    x = np.asarray(x, float) - np.mean(x)
    n = len(x)
    v = x @ x / n
    for k in range(1, lags + 1):
        v += 2 * (1 - k / (lags + 1)) * (x[k:] @ x[:-k]) / n
    return v


def nw_tstat(x, lags=None):
    x = np.asarray(x, float)
    x = x[~np.isnan(x)]
    n = len(x)
    if n < 10:
        return np.nan
    lags = lags if lags is not None else int(np.floor(4 * (n / 100) ** (2 / 9)))
    v = nw_var(x, lags)
    return float(np.mean(x) / np.sqrt(v / n)) if v > 0 else np.nan


def dm(loss_base, loss_model, lags):
    """Diebold-Mariano on loss differences; stat > 0 means the model has lower loss. Returns (stat, p)."""
    d = np.asarray(loss_base, float) - np.asarray(loss_model, float)
    d = d[~np.isnan(d)]
    if len(d) < 30 or np.allclose(d, 0):
        return np.nan, np.nan
    v = nw_var(d, max(int(lags), 1))
    if v <= 0:
        return np.nan, np.nan
    s = d.mean() / np.sqrt(v / len(d))
    return float(s), float(2 * (1 - norm.cdf(abs(s))))


def perf(returns, periods_per_year):
    """Annualized return, volatility, Sharpe, max drawdown for a series of simple period returns."""
    r = pd.Series(returns).dropna()
    if len(r) < 10:
        return {}
    eq = (1 + r).cumprod()
    dd = (eq / eq.cummax() - 1).min()
    years = len(r) / periods_per_year
    ann_ret = eq.iloc[-1] ** (1 / years) - 1 if eq.iloc[-1] > 0 else -1.0
    vol = r.std() * np.sqrt(periods_per_year)
    return {"ann_return": float(ann_ret), "ann_vol": float(vol),
            "sharpe": float(r.mean() / r.std() * np.sqrt(periods_per_year)) if r.std() > 0 else np.nan,
            "max_drawdown": float(dd), "total_return": float(eq.iloc[-1] - 1), "periods": int(len(r))}


def yearly(returns, index):
    s = pd.Series(np.asarray(returns, float), index=index).dropna()
    return {int(y): float((1 + g).prod() - 1) for y, g in s.groupby(s.index.year)}


def jdump(obj, path):
    Path(path).write_text(json.dumps(clean(obj), indent=1, default=str))


def clean(o):
    if isinstance(o, dict):
        return {str(k): clean(v) for k, v in o.items()}
    if isinstance(o, (list, tuple)):
        return [clean(v) for v in o]
    if isinstance(o, (float, np.floating)):
        return None if np.isnan(o) else float(o)
    if isinstance(o, np.integer):
        return int(o)
    return o


def pct(x, d=1):
    return "–" if x is None or (isinstance(x, float) and np.isnan(x)) else f"{100 * x:+.{d}f}%"


def num(x, d=2):
    return "–" if x is None or (isinstance(x, float) and np.isnan(x)) else f"{x:.{d}f}"
