# Track A: Bitcoin volatility

Walk-forward from 2021-01-01 · daily panel from hourly Binance candles · 10 news, sentiment and macro inputs · runtime 19.4 min

QLIKE is the standard loss for variance forecasts (lower is better). The ratio compares each model with HAR; below 1.00 is better. DM p tests whether the difference from HAR is more than chance.

## Next-day realized volatility

| Model | QLIKE | vs HAR | DM p | 2021 | 2022 | 2023 | 2024 | 2025 | 2026 |
|---|---|---|---|---|---|---|---|---|---|
| har | 0.4121 | **1.000×** | – | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 |
| har_ext | 0.4099 | **0.995×** | 0.552 | 1.00 | 0.98 | 1.03 | 0.98 | 0.99 | 0.97 |
| ridge | 0.3650 | **0.886×** | 0.000 | 0.97 | 0.90 | 0.87 | 0.85 | 0.89 | 0.87 |
| xgboost | 0.3563 | **0.864×** | 0.000 | 1.02 | 0.93 | 0.83 | 0.80 | 0.87 | 0.78 |
| gru | 0.3576 | **0.868×** | 0.000 | 1.05 | 0.94 | 0.81 | 0.82 | 0.84 | 0.82 |

## Next-7-day realized volatility

| Model | QLIKE | vs HAR | DM p | 2021 | 2022 | 2023 | 2024 | 2025 | 2026 |
|---|---|---|---|---|---|---|---|---|---|
| har | 0.1942 | **1.000×** | – | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 |
| har_ext | 0.1921 | **0.989×** | 0.159 | 1.00 | 1.00 | 0.99 | 0.99 | 0.99 | 0.95 |
| ridge | 0.1925 | **0.991×** | 0.845 | 1.44 | 0.96 | 0.73 | 1.05 | 0.95 | 1.03 |
| xgboost | 0.1992 | **1.026×** | 0.635 | 1.34 | 1.02 | 0.75 | 1.19 | 1.08 | 0.96 |
| gru | 0.2098 | **1.080×** | 0.180 | 1.23 | 1.06 | 0.74 | 1.68 | 1.08 | 0.98 |

## Volatility-targeted Bitcoin holding

Each day the position is set to 50% ÷ forecast annualized volatility, capped at 100% (no leverage), with 0.10% cost per unit traded.

| Forecast used | Annual return | Volatility | Sharpe | Max drawdown | Average position | Meets A3 |
|---|---|---|---|---|---|---|
| buy_and_hold | +12.9% | +57% | 0.50 | -77% | 100% | – |
| trailing_30d_vol | +9.2% | +47% | 0.42 | -74% | 88% | no |
| har | +5.9% | +44% | 0.35 | -70% | 86% | no |
| har_ext | +5.0% | +44% | 0.33 | -70% | 86% | no |
| ridge | +6.2% | +44% | 0.36 | -70% | 88% | no |
| xgboost | +4.4% | +44% | 0.32 | -71% | 87% | no |
| gru | +7.7% | +44% | 0.39 | -67% | 87% | no |

## Scorecard

| ID | Outcome | Result | Pass |
|---|---|---|---|
| A1 | Next-day realized volatility | best challenger xgboost: QLIKE 0.864× HAR, DM p 0.000; passing: ridge, xgboost, gru | PASS |
| A2 | Next-7-day realized volatility | best challenger har_ext: QLIKE 0.989× HAR, DM p 0.159 | fail |
| A3 | Volatility-targeted Bitcoin (HAR forecast, primary) | Sharpe 0.35 vs 0.50 buy-and-hold; max drawdown -70% vs -77% | fail |
