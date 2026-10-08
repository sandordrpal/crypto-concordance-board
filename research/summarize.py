"""Combine the track reports into one README with the pre-registered scorecard on top.

Usage: python research/summarize.py --results out/results --out out/README.md
"""
import argparse
import json
from pathlib import Path

TRACKS = [("volatility", "Track A: Bitcoin volatility"), ("cross_section", "Track B: ranking coins"),
          ("intraday", "Track C: intraday order flow")]


V2 = [("v2_volatility", "Track A: Bitcoin volatility"), ("v2_cross_section", "Track B: ranking coins"),
      ("v2_intraday", "Track C: intraday order flow")]
V2_METRIC = {"v2_volatility": ("QLIKE vs HAR", "{:.3f}×", "A1"), "v2_cross_section": ("Mean IC", "{:+.3f}", "B1"),
             "v2_intraday": ("R²oos", "{:+.3%}", "C1")}
ORDER = ["F0-ridge", "F0-xgboost", "F1-ridge", "F1-xgboost", "F2-ridge", "F2-xgboost"]


def v2_section(R):
    rows = []
    for key, title in V2:
        f = R / key / "metrics.json"
        if not f.exists():
            continue
        m = json.loads(f.read_text())
        lab, fmt, oid = V2_METRIC[key]
        cells = m.get("cells", {})
        vals = []
        for c in ORDER:
            v = cells.get(c)
            vals.append("–" if not v or v.get("primary") is None else fmt.format(v["primary"]) + (" ✓" if v.get("passes_primary") else ""))
        d = m.get("decision", {})
        rows.append(f"| {title} ({lab}, ✓ = {oid} pass) | " + " | ".join(vals) + f" | {d.get('candidate') or 'none'} |")
    if not rows:
        return []
    return ["", "## Version 2: three feature tiers × two model families", "",
            "Out of sample from 2023-01-01. F0 = version 1 inputs, F1 = + a few, F2 = + all free inputs. "
            "Candidate = simplest cell that passes and is not significantly worse than the best (see OUTCOMES.md).", "",
            "| Track | " + " | ".join(ORDER) + " | Candidate |", "|---|" + "---|" * (len(ORDER) + 1)] + rows


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--results", default="out/results")
    ap.add_argument("--out", default="out/README.md")
    ap.add_argument("--run", default="")
    a = ap.parse_args()
    R = Path(a.results)
    L = ["# Crypto research results", "",
         f"Latest run {a.run}. Outcomes and pass thresholds were fixed in advance in "
         "[OUTCOMES.md](https://github.com/sandordrpal/crypto-concordance-board/blob/main/research/OUTCOMES.md). "
         "Everything below is out of sample, walk-forward from 2021, after 0.10% costs per side.", "",
         "## Scorecard", "", "| ID | Outcome | Result | Pass |", "|---|---|---|---|"]
    missing = []
    for key, title in TRACKS:
        f = R / key / "metrics.json"
        if not f.exists():
            missing.append(title)
            continue
        for s in json.loads(f.read_text()).get("scorecard", []):
            L.append(f"| {s['id']} | {s['outcome']} | {s['result']} | {'**PASS**' if s['pass'] else 'fail'} |")
    if missing:
        L += ["", "Did not finish: " + ", ".join(missing) + " (see logs/)."]
    L += v2_section(R)
    L += ["", "## Track reports", ""]
    for key, title in TRACKS:
        if (R / key / "REPORT.md").exists():
            L.append(f"- [{title}](results/{key}/REPORT.md)")
    for key, title in V2:
        if (R / key / "REPORT.md").exists():
            L.append(f"- [{title}, version 2](results/{key}/REPORT.md)")
    if (R / "direction" / "REPORT.md").exists():
        L.append("- [Earlier study: daily direction of Bitcoin returns](results/direction/REPORT.md)")
    L += ["", "Data: `data/` (daily variables), hourly candles are rebuilt each run from Binance's public bulk data and not stored here. "
          "Logs: `logs/`.", "", "Information only, not investment advice."]
    Path(a.out).write_text("\n".join(L) + "\n")


if __name__ == "__main__":
    main()
