# Track A: Bitcoin volatility

Walk-forward from 2021-01-01 · daily panel from hourly Binance candles · 13 news, sentiment and macro inputs · runtime 18.1 min

QLIKE is the standard loss for variance forecasts (lower is better). The ratio compares each model with HAR; below 1.00 is better. DM p tests whether the difference from HAR is more than chance.

## Next-day realized volatility

| Model | QLIKE | vs HAR | DM p | 2021 | 2022 | 2023 | 2024 | 2025 | 2026 |
|---|---|---|---|---|---|---|---|---|---|
| har | 0.4122 | **1.000×** | – | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 |
| har_ext | 0.4101 | **0.995×** | 0.584 | 1.00 | 0.98 | 1.03 | 0.98 | 0.99 | 0.97 |
| ridge | 0.3690 | **0.895×** | 0.000 | 0.98 | 0.93 | 0.88 | 0.84 | 0.91 | 0.86 |
| xgboost | 0.3589 | **0.871×** | 0.000 | 0.99 | 0.97 | 0.84 | 0.83 | 0.87 | 0.77 |
| gru | 0.3719 | **0.902×** | 0.001 | 1.14 | 1.09 | 0.82 | 0.77 | 0.88 | 0.81 |

## Next-7-day realized volatility

| Model | QLIKE | vs HAR | DM p | 2021 | 2022 | 2023 | 2024 | 2025 | 2026 |
|---|---|---|---|---|---|---|---|---|---|
| har | 0.1936 | **1.000×** | – | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 |
| har_ext | 0.1915 | **0.989×** | 0.168 | 1.00 | 1.00 | 0.99 | 0.99 | 0.99 | 0.95 |
| ridge | 0.1925 | **0.994×** | 0.885 | 1.38 | 1.00 | 0.76 | 0.97 | 0.98 | 1.03 |
| xgboost | 0.2069 | **1.069×** | 0.211 | 1.37 | 1.17 | 0.77 | 1.21 | 1.08 | 0.92 |
| gru | 0.2144 | **1.107×** | 0.044 | 1.45 | 1.22 | 0.82 | 1.15 | 1.11 | 0.97 |

## Volatility-targeted Bitcoin holding

Each day the position is set to 50% ÷ forecast annualized volatility, capped at 100% (no leverage), with 0.10% cost per unit traded.

| Forecast used | Annual return | Volatility | Sharpe | Max drawdown | Average position | Meets A3 |
|---|---|---|---|---|---|---|
| buy_and_hold | +12.6% | +57% | 0.49 | -77% | 100% | – |
| trailing_30d_vol | +8.9% | +47% | 0.42 | -74% | 88% | no |
| har | +5.8% | +44% | 0.35 | -70% | 86% | no |
| har_ext | +4.9% | +44% | 0.33 | -70% | 86% | no |
| ridge | +5.9% | +44% | 0.35 | -70% | 87% | no |
| xgboost | +4.0% | +44% | 0.31 | -72% | 87% | no |
| gru | +6.7% | +44% | 0.37 | -68% | 87% | no |

## Scorecard

| ID | Outcome | Result | Pass |
|---|---|---|---|
| A1 | Next-day realized volatility | best challenger xgboost: QLIKE 0.871× HAR, DM p 0.000; passing: ridge, xgboost, gru | PASS |
| A2 | Next-7-day realized volatility | best challenger har_ext: QLIKE 0.989× HAR, DM p 0.168 | fail |
| A3 | Volatility-targeted Bitcoin (HAR forecast, primary) | Sharpe 0.35 vs 0.49 buy-and-hold; max drawdown -70% vs -77% | fail |
