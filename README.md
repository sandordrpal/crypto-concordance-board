# Crypto research results

Latest run 2026-10-17 (run 39011908025). Outcomes and pass thresholds were fixed in advance in [OUTCOMES.md](https://github.com/sandordrpal/crypto-concordance-board/blob/main/research/OUTCOMES.md). Everything below is out of sample, walk-forward from 2021, after 0.10% costs per side.

## Scorecard

| ID | Outcome | Result | Pass |
|---|---|---|---|
| A1 | Next-day realized volatility | best challenger xgboost: QLIKE 0.861× HAR, DM p 0.000; passing: ridge, xgboost, gru | **PASS** |
| A2 | Next-7-day realized volatility | best challenger har_ext: QLIKE 0.990× HAR, DM p 0.177 | fail |
| A3 | Volatility-targeted Bitcoin (HAR forecast, primary) | Sharpe 0.47 vs 0.59 buy-and-hold; max drawdown -70% vs -77% | fail |
| B1 | Weekly rank IC of coin forecasts | best xgboost: mean IC +0.080, t 6.60; momentum_4w -0.025, ridge +0.070, xgboost +0.080, mlp +0.074 | **PASS** |
| B2 | Top-fifth long-only vs equal weight, after costs | best momentum_4w: Sharpe 0.77 vs 0.74 EW, excess t 0.30 | fail |
| C1 | Next-4-hour Bitcoin return | best xgboost: R²oos +0.04%, hit 49.9%, DM p 0.761 | fail |
| C2 | Cost-aware long/flat on the 4-hour forecast | best xgboost: net Sharpe 0.46 vs 0.60 buy-and-hold, positive in 4 of 6 years | fail |

## Version 2: three feature tiers × two model families

Out of sample from 2023-01-01. F0 = version 1 inputs, F1 = + a few, F2 = + all free inputs. Candidate = simplest cell that passes and is not significantly worse than the best (see OUTCOMES.md).

| Track | F0-ridge | F0-xgboost | F1-ridge | F1-xgboost | F2-ridge | F2-xgboost | Candidate |
|---|---|---|---|---|---|---|---|
| Track A: Bitcoin volatility (QLIKE vs HAR, ✓ = A1 pass) | 0.880× ✓ | 0.829× ✓ | 0.881× ✓ | 0.823× ✓ | 0.907× ✓ | 0.837× ✓ | F0-ridge |
| Track B: ranking coins (Mean IC, ✓ = B1 pass) | +0.079 ✓ | +0.086 ✓ | +0.074 ✓ | +0.081 ✓ | +0.082 ✓ | +0.081 ✓ | F0-ridge |
| Track C: intraday order flow (R²oos, ✓ = C1 pass) | +0.025% | -0.123% | +0.030% | -0.084% | +0.163% | -0.098% | none |

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
