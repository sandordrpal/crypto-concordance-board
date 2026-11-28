# Crypto research results

Latest run 2026-11-28 (run 46135391370). Outcomes and pass thresholds were fixed in advance in [OUTCOMES.md](https://github.com/sandordrpal/crypto-concordance-board/blob/main/research/OUTCOMES.md). Everything below is out of sample, walk-forward from 2021, after 0.10% costs per side.

## Scorecard

| ID | Outcome | Result | Pass |
|---|---|---|---|
| A1 | Next-day realized volatility | best challenger xgboost: QLIKE 0.864× HAR, DM p 0.000; passing: ridge, xgboost, gru | **PASS** |
| A2 | Next-7-day realized volatility | best challenger har_ext: QLIKE 0.989× HAR, DM p 0.159 | fail |
| A3 | Volatility-targeted Bitcoin (HAR forecast, primary) | Sharpe 0.35 vs 0.50 buy-and-hold; max drawdown -70% vs -77% | fail |
| B1 | Weekly rank IC of coin forecasts | best xgboost: mean IC +0.081, t 6.62; momentum_4w -0.027, ridge +0.076, xgboost +0.081, mlp +0.076 | **PASS** |
| B2 | Top-fifth long-only vs equal weight, after costs | best momentum_4w: Sharpe 0.65 vs 0.63 EW, excess t 0.21 | fail |
| C1 | Next-4-hour Bitcoin return | best xgboost: R²oos +0.04%, hit 49.8%, DM p 0.788 | fail |
| C2 | Cost-aware long/flat on the 4-hour forecast | best xgboost: net Sharpe 0.46 vs 0.50 buy-and-hold, positive in 4 of 6 years | fail |

## Version 2: three feature tiers × two model families

Out of sample from 2023-01-01. F0 = version 1 inputs, F1 = + a few, F2 = + all free inputs. Candidate = simplest cell that passes and is not significantly worse than the best (see OUTCOMES.md).

| Track | F0-ridge | F0-xgboost | F1-ridge | F1-xgboost | F2-ridge | F2-xgboost | Candidate |
|---|---|---|---|---|---|---|---|
| Track A: Bitcoin volatility (QLIKE vs HAR, ✓ = A1 pass) | 0.875× ✓ | 0.835× ✓ | 0.875× ✓ | 0.833× ✓ | 0.912× ✓ | 0.846× ✓ | F0-ridge |
| Track B: ranking coins (Mean IC, ✓ = B1 pass) | +0.087 ✓ | +0.089 ✓ | +0.082 ✓ | +0.090 ✓ | +0.091 ✓ | +0.083 ✓ | F0-ridge |
| Track C: intraday order flow (R²oos, ✓ = C1 pass) | +0.018% | -0.131% | +0.022% | -0.121% | +0.188% | -0.196% | none |

## Track reports

- [Track A: Bitcoin volatility](results/volatility/REPORT.md)
- [Track B: ranking coins](results/cross_section/REPORT.md)
- [Track C: intraday order flow](results/intraday/REPORT.md)
- [Track A: Bitcoin volatility, version 2](results/v2_volatility/REPORT.md)
- [Track B: ranking coins, version 2](results/v2_cross_section/REPORT.md)
- [Track C: intraday order flow, version 2](results/v2_intraday/REPORT.md)
- [Earlier study: daily direction of Bitcoin returns](results/direction/REPORT.md)

Data: `data/` (daily variables), hourly candles are rebuilt each run from Binance's public bulk data and not stored here. Logs: `logs/`.

Information only, not investment advice.
