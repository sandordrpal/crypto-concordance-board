"""Combine the track reports into one README with the pre-registered scorecard on top.

Usage: python research/summarize.py --results out/results --out out/README.md
"""
import argparse
import json
from pathlib import Path

TRACKS = [("volatility", "Track A: Bitcoin volatility"), ("cross_section", "Track B: ranking coins"),
          ("intraday", "Track C: intraday order flow")]


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
    L += ["", "## Track reports", ""]
    for key, title in TRACKS:
        if (R / key / "REPORT.md").exists():
            L.append(f"- [{title}](results/{key}/REPORT.md)")
    if (R / "direction" / "REPORT.md").exists():
        L.append("- [Earlier study: daily direction of Bitcoin returns](results/direction/REPORT.md)")
    L += ["", "Data: `data/` (daily variables), hourly candles are rebuilt each run from Binance's public bulk data and not stored here. "
          "Logs: `logs/`.", "", "Information only, not investment advice."]
    Path(a.out).write_text("\n".join(L) + "\n")


if __name__ == "__main__":
    main()
