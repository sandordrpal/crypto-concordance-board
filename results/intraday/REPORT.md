# Track C: Bitcoin intraday order flow

Hourly Binance candles 2017-08-17 to 2026-11-06 · 35 features (taker buy/sell imbalance for Bitcoin, Ether and a 65-coin altcoin basket, returns, volume, volatility, time of day) · yearly walk-forward 2021–2026 · runtime 2.5 min

R²oos compares each forecast with the random walk (0 = equal). Hit is the share of hours where the forecast had the right sign.

## Next 1 hour

| Model | R²oos | Hit rate | DM p | 2021 | 2022 | 2023 | 2024 | 2025 | 2026 |
|---|---|---|---|---|---|---|---|---|---|
| zero | **+0.000%** | – | – | +0.00% | +0.00% | +0.00% | +0.00% | +0.00% | +0.00% |
| ridge | **-0.050%** | 51.3% | 0.275 | -0.12% | -0.02% | -0.05% | +0.02% | -0.01% | +0.01% |
| xgboost | **-0.037%** | 50.2% | 0.822 | -0.06% | -0.13% | +0.02% | +0.21% | -0.14% | -0.07% |

## Next 4 hours

| Model | R²oos | Hit rate | DM p | 2021 | 2022 | 2023 | 2024 | 2025 | 2026 |
|---|---|---|---|---|---|---|---|---|---|
| zero | **+0.000%** | – | – | +0.00% | +0.00% | +0.00% | +0.00% | +0.00% | +0.00% |
| ridge | **-0.002%** | 50.7% | 0.914 | +0.00% | -0.06% | +0.01% | +0.07% | -0.03% | +0.03% |
| xgboost | **-0.022%** | 50.3% | 0.920 | +0.27% | -0.32% | +0.09% | -0.20% | -0.43% | +0.09% |
| gru | **-0.075%** | 50.8% | 0.618 | +0.23% | -0.26% | -0.45% | -0.06% | -0.41% | -0.18% |

## Next 12 hours

| Model | R²oos | Hit rate | DM p | 2021 | 2022 | 2023 | 2024 | 2025 | 2026 |
|---|---|---|---|---|---|---|---|---|---|
| zero | **+0.000%** | – | – | +0.00% | +0.00% | +0.00% | +0.00% | +0.00% | +0.00% |
| ridge | **+0.211%** | 50.4% | 0.286 | +0.45% | +0.04% | +0.11% | +0.16% | -0.03% | +0.07% |
| xgboost | **-0.433%** | 50.6% | 0.178 | +0.69% | -2.07% | +0.16% | -1.62% | -0.15% | -0.24% |

## Trading the 4-hour forecast after costs

Decisions every 4 hours. Long/flat: buy when the forecast exceeds the 0.20% round-trip cost, hold while it stays positive. Long/short is shown for information only (no funding or borrowing costs).

| Strategy | Annual return | Sharpe | Max drawdown | Time invested | Trades/year | Positive years | Long/short Sharpe |
|---|---|---|---|---|---|---|---|
| buy and hold | +17.9% | 0.57 | -77% | 100% | – | 3/6 | – |
| ridge | +0.0% | – | +0% | 0% | 0 | 0/6 | – |
| xgboost | +23.8% | 1.08 | -24% | 7% | 33 | 3/6 | 0.90 |
| gru | +5.7% | 0.41 | -33% | 6% | 71 | 4/6 | -0.02 |

## Scorecard

| ID | Outcome | Result | Pass |
|---|---|---|---|
| C1 | Next-4-hour Bitcoin return | best ridge: R²oos -0.00%, hit 50.7%, DM p 0.914 | fail |
| C2 | Cost-aware long/flat on the 4-hour forecast | best xgboost: net Sharpe 1.08 vs 0.57 buy-and-hold, positive in 3 of 6 years | fail |
