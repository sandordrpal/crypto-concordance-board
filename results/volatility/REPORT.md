# Track A: Bitcoin volatility

Walk-forward from 2021-01-01 · daily panel from hourly Binance candles · 13 news, sentiment and macro inputs · runtime 10.2 min

QLIKE is the standard loss for variance forecasts (lower is better). The ratio compares each model with HAR; below 1.00 is better. DM p tests whether the difference from HAR is more than chance.

## Next-day realized volatility

| Model | QLIKE | vs HAR | DM p | 2021 | 2022 | 2023 | 2024 | 2025 | 2026 |
|---|---|---|---|---|---|---|---|---|---|
| har | 0.4127 | **1.000×** | – | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 |
| har_ext | 0.4108 | **0.995×** | 0.616 | 1.00 | 0.98 | 1.03 | 0.98 | 0.99 | 0.97 |
| ridge | 0.3696 | **0.896×** | 0.000 | 1.01 | 0.92 | 0.88 | 0.84 | 0.91 | 0.84 |
| xgboost | 0.3563 | **0.863×** | 0.000 | 1.01 | 0.95 | 0.84 | 0.81 | 0.87 | 0.72 |
| gru | 0.3666 | **0.888×** | 0.000 | 1.14 | 1.01 | 0.83 | 0.78 | 0.87 | 0.76 |

## Next-7-day realized volatility

| Model | QLIKE | vs HAR | DM p | 2021 | 2022 | 2023 | 2024 | 2025 | 2026 |
|---|---|---|---|---|---|---|---|---|---|
| har | 0.1955 | **1.000×** | – | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 |
| har_ext | 0.1935 | **0.989×** | 0.174 | 1.00 | 1.00 | 0.99 | 0.99 | 0.99 | 0.95 |
| ridge | 0.1880 | **0.961×** | 0.351 | 1.36 | 0.94 | 0.75 | 0.91 | 0.96 | 1.00 |
| xgboost | 0.2063 | **1.055×** | 0.319 | 1.43 | 1.11 | 0.74 | 1.17 | 1.10 | 0.93 |
| gru | 0.2124 | **1.086×** | 0.091 | 1.32 | 1.15 | 0.93 | 1.06 | 1.09 | 1.01 |

## Volatility-targeted Bitcoin holding

Each day the position is set to 50% ÷ forecast annualized volatility, capped at 100% (no leverage), with 0.10% cost per unit traded.

| Forecast used | Annual return | Volatility | Sharpe | Max drawdown | Average position | Meets A3 |
|---|---|---|---|---|---|---|
| buy_and_hold | +19.7% | +57% | 0.60 | -77% | 100% | – |
| trailing_30d_vol | +15.7% | +47% | 0.55 | -74% | 88% | no |
| har | +12.1% | +44% | 0.48 | -70% | 86% | no |
| har_ext | +11.1% | +44% | 0.46 | -70% | 86% | no |
| ridge | +11.7% | +44% | 0.47 | -70% | 87% | no |
| xgboost | +10.1% | +44% | 0.44 | -72% | 87% | no |
| gru | +14.3% | +43% | 0.52 | -66% | 86% | no |

## Scorecard

| ID | Outcome | Result | Pass |
|---|---|---|---|
| A1 | Next-day realized volatility | best challenger xgboost: QLIKE 0.863× HAR, DM p 0.000; passing: ridge, xgboost, gru | PASS |
| A2 | Next-7-day realized volatility | best challenger ridge: QLIKE 0.961× HAR, DM p 0.351 | fail |
| A3 | Volatility-targeted Bitcoin (HAR forecast, primary) | Sharpe 0.48 vs 0.60 buy-and-hold; max drawdown -70% vs -77% | fail |
