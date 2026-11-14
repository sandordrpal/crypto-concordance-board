# Track A: Bitcoin volatility

Walk-forward from 2021-01-01 · daily panel from hourly Binance candles · 12 news, sentiment and macro inputs · runtime 9.4 min

QLIKE is the standard loss for variance forecasts (lower is better). The ratio compares each model with HAR; below 1.00 is better. DM p tests whether the difference from HAR is more than chance.

## Next-day realized volatility

| Model | QLIKE | vs HAR | DM p | 2021 | 2022 | 2023 | 2024 | 2025 | 2026 |
|---|---|---|---|---|---|---|---|---|---|
| har | 0.4126 | **1.000×** | – | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 |
| har_ext | 0.4111 | **0.996×** | 0.681 | 1.00 | 0.98 | 1.03 | 0.98 | 0.99 | 0.98 |
| ridge | 0.3667 | **0.889×** | 0.000 | 0.95 | 0.91 | 0.88 | 0.86 | 0.90 | 0.85 |
| xgboost | 0.3593 | **0.871×** | 0.000 | 1.02 | 0.96 | 0.84 | 0.82 | 0.88 | 0.75 |
| gru | 0.3713 | **0.900×** | 0.002 | 1.07 | 1.05 | 0.83 | 0.83 | 0.89 | 0.78 |

## Next-7-day realized volatility

| Model | QLIKE | vs HAR | DM p | 2021 | 2022 | 2023 | 2024 | 2025 | 2026 |
|---|---|---|---|---|---|---|---|---|---|
| har | 0.1934 | **1.000×** | – | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 |
| har_ext | 0.1914 | **0.990×** | 0.195 | 1.00 | 1.00 | 0.99 | 0.99 | 0.99 | 0.95 |
| ridge | 0.1944 | **1.005×** | 0.914 | 1.39 | 1.05 | 0.71 | 1.04 | 0.97 | 1.02 |
| xgboost | 0.2037 | **1.054×** | 0.348 | 1.34 | 1.11 | 0.75 | 1.21 | 1.12 | 0.94 |
| gru | 0.2160 | **1.117×** | 0.037 | 1.49 | 1.29 | 0.73 | 1.09 | 1.20 | 0.99 |

## Volatility-targeted Bitcoin holding

Each day the position is set to 50% ÷ forecast annualized volatility, capped at 100% (no leverage), with 0.10% cost per unit traded.

| Forecast used | Annual return | Volatility | Sharpe | Max drawdown | Average position | Meets A3 |
|---|---|---|---|---|---|---|
| buy_and_hold | +15.5% | +57% | 0.54 | -77% | 100% | – |
| trailing_30d_vol | +11.7% | +47% | 0.47 | -74% | 88% | no |
| har | +8.3% | +44% | 0.40 | -70% | 86% | no |
| har_ext | +7.4% | +44% | 0.38 | -70% | 86% | no |
| ridge | +8.4% | +44% | 0.40 | -70% | 88% | no |
| xgboost | +6.7% | +44% | 0.37 | -71% | 87% | no |
| gru | +11.1% | +44% | 0.46 | -65% | 87% | no |

## Scorecard

| ID | Outcome | Result | Pass |
|---|---|---|---|
| A1 | Next-day realized volatility | best challenger xgboost: QLIKE 0.871× HAR, DM p 0.000; passing: ridge, xgboost, gru | PASS |
| A2 | Next-7-day realized volatility | best challenger har_ext: QLIKE 0.990× HAR, DM p 0.195 | fail |
| A3 | Volatility-targeted Bitcoin (HAR forecast, primary) | Sharpe 0.40 vs 0.54 buy-and-hold; max drawdown -70% vs -77% | fail |
