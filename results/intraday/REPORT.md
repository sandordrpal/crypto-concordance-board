# Track C: Bitcoin intraday order flow

Hourly Binance candles 2017-08-17 to 2026-10-30 · 35 features (taker buy/sell imbalance for Bitcoin, Ether and a 66-coin altcoin basket, returns, volume, volatility, time of day) · yearly walk-forward 2021–2026 · runtime 2.4 min

R²oos compares each forecast with the random walk (0 = equal). Hit is the share of hours where the forecast had the right sign.

## Next 1 hour

| Model | R²oos | Hit rate | DM p | 2021 | 2022 | 2023 | 2024 | 2025 | 2026 |
|---|---|---|---|---|---|---|---|---|---|
| zero | **+0.000%** | – | – | +0.00% | +0.00% | +0.00% | +0.00% | +0.00% | +0.00% |
| ridge | **-0.045%** | 51.5% | 0.325 | -0.12% | -0.02% | -0.00% | +0.02% | -0.01% | +0.02% |
| xgboost | **-0.066%** | 50.1% | 0.687 | -0.08% | -0.14% | +0.02% | +0.21% | -0.31% | -0.10% |

## Next 4 hours

| Model | R²oos | Hit rate | DM p | 2021 | 2022 | 2023 | 2024 | 2025 | 2026 |
|---|---|---|---|---|---|---|---|---|---|
| zero | **+0.000%** | – | – | +0.00% | +0.00% | +0.00% | +0.00% | +0.00% | +0.00% |
| ridge | **-0.002%** | 50.7% | 0.915 | +0.00% | -0.06% | +0.01% | +0.07% | -0.03% | +0.03% |
| xgboost | **+0.042%** | 49.9% | 0.764 | +0.27% | -0.05% | +0.10% | -0.18% | -0.40% | +0.07% |
| gru | **-0.078%** | 50.8% | 0.600 | +0.23% | -0.26% | -0.45% | -0.07% | -0.41% | -0.24% |

## Next 12 hours

| Model | R²oos | Hit rate | DM p | 2021 | 2022 | 2023 | 2024 | 2025 | 2026 |
|---|---|---|---|---|---|---|---|---|---|
| zero | **+0.000%** | – | – | +0.00% | +0.00% | +0.00% | +0.00% | +0.00% | +0.00% |
| ridge | **+0.214%** | 50.4% | 0.279 | +0.46% | +0.04% | +0.11% | +0.16% | -0.03% | +0.05% |
| xgboost | **-0.513%** | 50.6% | 0.177 | +0.92% | -3.08% | +0.16% | -1.11% | -0.32% | -0.27% |

## Trading the 4-hour forecast after costs

Decisions every 4 hours. Long/flat: buy when the forecast exceeds the 0.20% round-trip cost, hold while it stays positive. Long/short is shown for information only (no funding or borrowing costs).

| Strategy | Annual return | Sharpe | Max drawdown | Time invested | Trades/year | Positive years | Long/short Sharpe |
|---|---|---|---|---|---|---|---|
| buy and hold | +18.2% | 0.58 | -77% | 100% | – | 3/6 | – |
| ridge | +0.0% | – | +0% | 0% | 0 | 0/6 | – |
| xgboost | +4.8% | 0.46 | -24% | 1% | 12 | 4/6 | -0.14 |
| gru | +5.8% | 0.42 | -33% | 6% | 70 | 4/6 | 0.04 |

## Scorecard

| ID | Outcome | Result | Pass |
|---|---|---|---|
| C1 | Next-4-hour Bitcoin return | best xgboost: R²oos +0.04%, hit 49.9%, DM p 0.764 | fail |
| C2 | Cost-aware long/flat on the 4-hour forecast | best xgboost: net Sharpe 0.46 vs 0.58 buy-and-hold, positive in 4 of 6 years | fail |
