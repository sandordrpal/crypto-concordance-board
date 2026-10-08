"""Write simulated raw data in the collector's format, for testing the pipeline offline.

The simulated Bitcoin return has a small, known dependence on two lagged inputs, so a working
pipeline should find a little skill and an over-fitted one should not. Not market data.
Usage: python research/synthetic.py --out /tmp/simdata
"""
import argparse
import json
from pathlib import Path

import numpy as np
import pandas as pd


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", required=True)
    out = Path(ap.parse_args().out)
    (out / "raw").mkdir(parents=True, exist_ok=True)
    rng = np.random.default_rng(7)
    d = pd.date_range("2014-09-17", "2026-10-07", freq="D")
    n = len(d)
    fg = np.clip(50 + np.cumsum(rng.normal(0, 3, n)) * 0.3 + rng.normal(0, 8, n), 1, 99)
    epu = np.exp(rng.normal(4.8, 0.4, n))
    r = 0.0004 + 0.03 * rng.standard_t(4, n) / np.sqrt(2)
    r[1:] += -0.0006 * (fg[:-1] - 50) / 10            # weak contrarian sentiment effect
    r[1:] += 0.03 * np.tanh(np.r_[0, np.diff(np.log(epu))][:-1])  # tiny news effect
    btc = 400 * np.exp(np.cumsum(r))
    sp = 2000 * np.exp(np.cumsum(0.0003 + 0.011 * rng.normal(size=n)))
    status = {}

    def put(name, idx, vals, kind, lag, src="simulated"):
        pd.DataFrame({"date": idx.strftime("%Y-%m-%d"), "value": vals}).to_csv(out / "raw" / f"{name}.csv", index=False)
        status[name] = {"status": "ok", "source": src, "kind": kind, "lag_days": lag, "rows": len(idx),
                        "first": str(idx[0].date()), "last": str(idx[-1].date()), "description": name}

    put("btc", d, btc, "price", 0)
    put("btc_volume", d, np.exp(rng.normal(23, 0.5, n)), "count", 0)
    wk = d.dayofweek < 5
    put("sp500", d[wk], sp[wk], "price", 0)
    put("vix", d[wk], np.exp(rng.normal(2.9, 0.3, wk.sum())), "level", 0)
    m = d >= "2018-02-01"
    put("fear_greed", d[m], fg[m], "level", 0)
    put("epu_us", d, epu, "level", 1)
    put("gpr", d, np.exp(rng.normal(4.6, 0.5, n)), "level", 1)
    ms = d[d.is_month_start]
    put("m2", ms, np.linspace(11e3, 22e3, len(ms)), "count", 60)
    s = d >= "2017-11-01"
    put("stablecoin_supply", d[s], np.linspace(2e9, 3e11, s.sum()), "count", 1)
    f = d >= "2019-09-10"
    put("funding_rate", d[f], 0.0001 + 0.0002 * rng.normal(size=f.sum()), "level", 0)
    g = d >= "2026-07-01"
    put("news_tone_bitcoin", d[g], rng.normal(-1, 1, g.sum()), "level", 1)
    status["cm_exchange_inflow"] = {"status": "error", "source": "simulated", "error": "HTTP 403 (not in free tier)"}
    (out / "status.json").write_text(json.dumps({"collected_utc": "simulated", "series": status}, indent=1))
    print(f"wrote {len(status)} simulated series to {out}")


if __name__ == "__main__":
    main()
