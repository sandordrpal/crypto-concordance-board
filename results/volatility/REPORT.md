# Track A: Bitcoin volatility

Walk-forward from 2021-01-01 · daily panel from hourly Binance candles · 11 news, sentiment and macro inputs · runtime 18.2 min

QLIKE is the standard loss for variance forecasts (lower is better). The ratio compares each model with HAR; below 1.00 is better. DM p tests whether the difference from HAR is more than chance.

## Next-day realized volatility

| Model | QLIKE | vs HAR | DM p | 2021 | 2022 | 2023 | 2024 | 2025 | 2026 |
|---|---|---|---|---|---|---|---|---|---|
| har | 0.4127 | **1.000×** | – | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 |
| har_ext | 0.4107 | **0.995×** | 0.603 | 1.00 | 0.98 | 1.03 | 0.98 | 0.99 | 0.97 |
| ridge | 0.3663 | **0.888×** | 0.000 | 0.95 | 0.91 | 0.88 | 0.86 | 0.89 | 0.84 |
| xgboost | 0.3552 | **0.861×** | 0.000 | 1.00 | 0.94 | 0.83 | 0.82 | 0.87 | 0.73 |
| gru | 0.3584 | **0.869×** | 0.000 | 1.01 | 1.02 | 0.85 | 0.79 | 0.82 | 0.73 |

## Next-7-day realized volatility

| Model | QLIKE | vs HAR | DM p | 2021 | 2022 | 2023 | 2024 | 2025 | 2026 |
|---|---|---|---|---|---|---|---|---|---|
| har | 0.1950 | **1.000×** | – | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 |
| har_ext | 0.1930 | **0.990×** | 0.177 | 1.00 | 1.00 | 0.99 | 0.99 | 0.99 | 0.95 |
| ridge | 0.1970 | **1.010×** | 0.839 | 1.41 | 1.06 | 0.71 | 1.05 | 0.97 | 1.02 |
| xgboost | 0.2050 | **1.051×** | 0.363 | 1.38 | 1.10 | 0.74 | 1.21 | 1.12 | 0.92 |
| gru | 0.2031 | **1.041×** | 0.371 | 1.37 | 1.16 | 0.73 | 1.02 | 1.03 | 1.01 |

## Volatility-targeted Bitcoin holding

Each day the position is set to 50% ÷ forecast annualized volatility, capped at 100% (no leverage), with 0.10% cost per unit traded.

| Forecast used | Annual return | Volatility | Sharpe | Max drawdown | Average position | Meets A3 |
|---|---|---|---|---|---|---|
| buy_and_hold | +19.3% | +57% | 0.59 | -77% | 100% | – |
| trailing_30d_vol | +15.4% | +47% | 0.54 | -74% | 88% | no |
| har | +11.8% | +44% | 0.47 | -70% | 86% | no |
| har_ext | +10.8% | +44% | 0.45 | -70% | 86% | no |
| ridge | +12.2% | +44% | 0.48 | -70% | 88% | no |
| xgboost | +10.2% | +44% | 0.44 | -71% | 87% | no |
| gru | +12.8% | +44% | 0.49 | -68% | 87% | no |

## Scorecard

| ID | Outcome | Result | Pass |
|---|---|---|---|
| A1 | Next-day realized volatility | best challenger xgboost: QLIKE 0.861× HAR, DM p 0.000; passing: ridge, xgboost, gru | PASS |
| A2 | Next-7-day realized volatility | best challenger har_ext: QLIKE 0.990× HAR, DM p 0.177 | fail |
| A3 | Volatility-targeted Bitcoin (HAR forecast, primary) | Sharpe 0.47 vs 0.59 buy-and-hold; max drawdown -70% vs -77% | fail |
