# Track A: Bitcoin volatility

Walk-forward from 2021-01-01 · daily panel from hourly Binance candles · 13 news, sentiment and macro inputs · runtime 17.4 min

QLIKE is the standard loss for variance forecasts (lower is better). The ratio compares each model with HAR; below 1.00 is better. DM p tests whether the difference from HAR is more than chance.

## Next-day realized volatility

| Model | QLIKE | vs HAR | DM p | 2021 | 2022 | 2023 | 2024 | 2025 | 2026 |
|---|---|---|---|---|---|---|---|---|---|
| har | 0.4126 | **1.000×** | – | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 |
| har_ext | 0.4111 | **0.997×** | 0.700 | 1.00 | 0.98 | 1.03 | 0.98 | 0.99 | 0.98 |
| ridge | 0.3688 | **0.894×** | 0.000 | 0.98 | 0.93 | 0.88 | 0.84 | 0.91 | 0.85 |
| xgboost | 0.3572 | **0.866×** | 0.000 | 0.99 | 0.97 | 0.84 | 0.83 | 0.87 | 0.72 |
| gru | 0.3713 | **0.900×** | 0.001 | 1.14 | 1.09 | 0.82 | 0.77 | 0.88 | 0.78 |

## Next-7-day realized volatility

| Model | QLIKE | vs HAR | DM p | 2021 | 2022 | 2023 | 2024 | 2025 | 2026 |
|---|---|---|---|---|---|---|---|---|---|
| har | 0.1939 | **1.000×** | – | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 |
| har_ext | 0.1919 | **0.990×** | 0.178 | 1.00 | 1.00 | 0.99 | 0.99 | 0.99 | 0.95 |
| ridge | 0.1923 | **0.992×** | 0.842 | 1.38 | 1.00 | 0.76 | 0.97 | 0.98 | 1.01 |
| xgboost | 0.2069 | **1.067×** | 0.228 | 1.37 | 1.17 | 0.77 | 1.21 | 1.08 | 0.90 |
| gru | 0.2145 | **1.106×** | 0.047 | 1.45 | 1.22 | 0.82 | 1.15 | 1.11 | 0.96 |

## Volatility-targeted Bitcoin holding

Each day the position is set to 50% ÷ forecast annualized volatility, capped at 100% (no leverage), with 0.10% cost per unit traded.

| Forecast used | Annual return | Volatility | Sharpe | Max drawdown | Average position | Meets A3 |
|---|---|---|---|---|---|---|
| buy_and_hold | +17.6% | +57% | 0.57 | -77% | 100% | – |
| trailing_30d_vol | +13.8% | +47% | 0.51 | -74% | 88% | no |
| har | +10.3% | +44% | 0.44 | -70% | 86% | no |
| har_ext | +9.3% | +44% | 0.42 | -70% | 86% | no |
| ridge | +10.3% | +44% | 0.44 | -70% | 87% | no |
| xgboost | +8.4% | +44% | 0.40 | -72% | 87% | no |
| gru | +11.5% | +44% | 0.47 | -68% | 87% | no |

## Scorecard

| ID | Outcome | Result | Pass |
|---|---|---|---|
| A1 | Next-day realized volatility | best challenger xgboost: QLIKE 0.866× HAR, DM p 0.000; passing: ridge, xgboost, gru | PASS |
| A2 | Next-7-day realized volatility | best challenger har_ext: QLIKE 0.990× HAR, DM p 0.178 | fail |
| A3 | Volatility-targeted Bitcoin (HAR forecast, primary) | Sharpe 0.44 vs 0.57 buy-and-hold; max drawdown -70% vs -77% | fail |
