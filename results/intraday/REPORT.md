# Track C: Bitcoin intraday order flow

Hourly Binance candles 2017-08-17 to 2026-10-09 · 36 features (taker buy/sell imbalance for Bitcoin, Ether and a 65-coin altcoin basket, returns, volume, volatility, time of day) · yearly walk-forward 2021–2026 · runtime 1.8 min

R²oos compares each forecast with the random walk (0 = equal). Hit is the share of hours where the forecast had the right sign.

## Next 1 hour

| Model | R²oos | Hit rate | DM p | 2021 | 2022 | 2023 | 2024 | 2025 | 2026 |
|---|---|---|---|---|---|---|---|---|---|
| zero | **+0.000%** | – | – | +0.00% | +0.00% | +0.00% | +0.00% | +0.00% | +0.00% |
| ridge | **-0.045%** | 51.5% | 0.329 | -0.12% | -0.02% | +0.01% | +0.02% | -0.01% | +0.02% |
| xgboost | **+0.038%** | 49.9% | 0.756 | +0.10% | -0.02% | +0.03% | +0.17% | -0.23% | +0.01% |

## Next 4 hours

| Model | R²oos | Hit rate | DM p | 2021 | 2022 | 2023 | 2024 | 2025 | 2026 |
|---|---|---|---|---|---|---|---|---|---|
| zero | **+0.000%** | – | – | +0.00% | +0.00% | +0.00% | +0.00% | +0.00% | +0.00% |
| ridge | **-0.001%** | 50.8% | 0.950 | +0.00% | -0.06% | +0.01% | +0.06% | -0.03% | +0.04% |
| xgboost | **+0.077%** | 50.1% | 0.719 | +0.45% | -0.07% | +0.11% | -0.31% | -0.53% | +0.11% |
| gru | **+0.007%** | 50.7% | 0.963 | +0.07% | -0.04% | +0.41% | -0.27% | -0.06% | -0.09% |

## Next 12 hours

| Model | R²oos | Hit rate | DM p | 2021 | 2022 | 2023 | 2024 | 2025 | 2026 |
|---|---|---|---|---|---|---|---|---|---|
| zero | **+0.000%** | – | – | +0.00% | +0.00% | +0.00% | +0.00% | +0.00% | +0.00% |
| ridge | **+0.101%** | 50.3% | 0.693 | +0.17% | +0.03% | +0.12% | +0.12% | -0.03% | +0.09% |
| xgboost | **-0.849%** | 50.5% | 0.101 | +0.76% | -4.58% | +0.02% | -1.01% | -0.04% | -0.08% |

## Trading the 4-hour forecast after costs

Decisions every 4 hours. Long/flat: buy when the forecast exceeds the 0.20% round-trip cost, hold while it stays positive. Long/short is shown for information only (no funding or borrowing costs).

| Strategy | Annual return | Sharpe | Max drawdown | Time invested | Trades/year | Positive years | Long/short Sharpe |
|---|---|---|---|---|---|---|---|
| buy and hold | +19.9% | 0.60 | -77% | 100% | – | 3/6 | – |
| ridge | +0.0% | – | +0% | 0% | 0 | 0/6 | – |
| xgboost | +27.5% | 1.24 | -24% | 6% | 32 | 3/6 | 1.08 |
| gru | +4.6% | 0.33 | -32% | 6% | 70 | 3/6 | 0.14 |

## Scorecard

| ID | Outcome | Result | Pass |
|---|---|---|---|
| C1 | Next-4-hour Bitcoin return | best xgboost: R²oos +0.08%, hit 50.1%, DM p 0.719 | fail |
| C2 | Cost-aware long/flat on the 4-hour forecast | best xgboost: net Sharpe 1.24 vs 0.60 buy-and-hold, positive in 3 of 6 years | fail |
