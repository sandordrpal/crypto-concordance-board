# Track A: Bitcoin volatility

Walk-forward from 2021-01-01 · daily panel from hourly Binance candles · 12 news, sentiment and macro inputs · runtime 17.2 min

QLIKE is the standard loss for variance forecasts (lower is better). The ratio compares each model with HAR; below 1.00 is better. DM p tests whether the difference from HAR is more than chance.

## Next-day realized volatility

| Model | QLIKE | vs HAR | DM p | 2021 | 2022 | 2023 | 2024 | 2025 | 2026 |
|---|---|---|---|---|---|---|---|---|---|
| har | 0.4121 | **1.000×** | – | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 |
| har_ext | 0.4101 | **0.995×** | 0.604 | 1.00 | 0.98 | 1.03 | 0.98 | 0.99 | 0.97 |
| ridge | 0.3659 | **0.888×** | 0.000 | 0.95 | 0.91 | 0.88 | 0.86 | 0.90 | 0.84 |
| xgboost | 0.3583 | **0.870×** | 0.000 | 1.02 | 0.96 | 0.84 | 0.82 | 0.88 | 0.73 |
| gru | 0.3705 | **0.899×** | 0.002 | 1.07 | 1.05 | 0.83 | 0.83 | 0.89 | 0.76 |

## Next-7-day realized volatility

| Model | QLIKE | vs HAR | DM p | 2021 | 2022 | 2023 | 2024 | 2025 | 2026 |
|---|---|---|---|---|---|---|---|---|---|
| har | 0.1947 | **1.000×** | – | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 |
| har_ext | 0.1927 | **0.990×** | 0.176 | 1.00 | 1.00 | 0.99 | 0.99 | 0.99 | 0.95 |
| ridge | 0.1955 | **1.004×** | 0.928 | 1.39 | 1.05 | 0.71 | 1.04 | 0.97 | 1.02 |
| xgboost | 0.2051 | **1.053×** | 0.352 | 1.34 | 1.11 | 0.75 | 1.21 | 1.12 | 0.93 |
| gru | 0.2174 | **1.117×** | 0.037 | 1.49 | 1.29 | 0.73 | 1.09 | 1.20 | 0.99 |

## Volatility-targeted Bitcoin holding

Each day the position is set to 50% ÷ forecast annualized volatility, capped at 100% (no leverage), with 0.10% cost per unit traded.

| Forecast used | Annual return | Volatility | Sharpe | Max drawdown | Average position | Meets A3 |
|---|---|---|---|---|---|---|
| buy_and_hold | +19.1% | +57% | 0.59 | -77% | 100% | – |
| trailing_30d_vol | +15.2% | +47% | 0.54 | -74% | 88% | no |
| har | +11.7% | +44% | 0.47 | -70% | 86% | no |
| har_ext | +10.7% | +44% | 0.45 | -70% | 86% | no |
| ridge | +11.8% | +44% | 0.47 | -70% | 88% | no |
| xgboost | +9.9% | +44% | 0.44 | -71% | 87% | no |
| gru | +14.6% | +44% | 0.53 | -65% | 86% | no |

## Scorecard

| ID | Outcome | Result | Pass |
|---|---|---|---|
| A1 | Next-day realized volatility | best challenger xgboost: QLIKE 0.870× HAR, DM p 0.000; passing: ridge, xgboost, gru | PASS |
| A2 | Next-7-day realized volatility | best challenger har_ext: QLIKE 0.990× HAR, DM p 0.176 | fail |
| A3 | Volatility-targeted Bitcoin (HAR forecast, primary) | Sharpe 0.47 vs 0.59 buy-and-hold; max drawdown -70% vs -77% | fail |
