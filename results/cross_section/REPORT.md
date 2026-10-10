# Track B: ranking coins against each other

67 coins with hourly Binance data · 51 eligible coins in a typical week (min 32, max 63) · weekly rebalancing from 2021-01-01 · models refit every 13 weeks · 0.10% cost per side · runtime 1.2 min

IC is the rank correlation between a model's scores and the next week's returns across coins (0 = no information). The top-fifth portfolio holds the highest-scored coins in equal weights; equal weight (EW) holds every eligible coin.

| Model | Mean IC | IC t-stat | Weeks IC > 0 | Top-fifth Sharpe | EW Sharpe | Excess t-stat | Top-fifth annual | EW annual | Long-short Sharpe | Turnover/week |
|---|---|---|---|---|---|---|---|---|---|---|
| momentum_4w | -0.026 | -2.10 | 48% | 0.79 | 0.76 | 0.33 | +37% | +32% | 0.19 | 71% |
| ridge | +0.070 | 4.62 | 60% | 0.71 | 0.76 | -0.95 | +29% | +32% | -0.51 | 50% |
| xgboost | +0.079 | 6.48 | 66% | 0.82 | 0.76 | 0.14 | +41% | +32% | -0.25 | 90% |
| mlp | +0.072 | 6.70 | 64% | 0.78 | 0.76 | -0.17 | +36% | +32% | -0.20 | 96% |

Mean IC by year:

| Model | 2021 | 2022 | 2023 | 2024 | 2025 | 2026 |
|---|---|---|---|---|---|---|
| momentum_4w | -0.066 | +0.011 | -0.014 | -0.035 | +0.012 | -0.074 |
| ridge | -0.018 | +0.125 | +0.039 | +0.072 | +0.116 | +0.093 |
| xgboost | +0.021 | +0.101 | +0.079 | +0.094 | +0.096 | +0.087 |
| mlp | +0.027 | +0.114 | +0.066 | +0.071 | +0.079 | +0.081 |

Caveat stated in advance: the coin list is today's large coins, so past altcoin returns are flattered (survivorship bias).

## Scorecard

| ID | Outcome | Result | Pass |
|---|---|---|---|
| B1 | Weekly rank IC of coin forecasts | best mlp: mean IC +0.072, t 6.70; momentum_4w -0.026, ridge +0.070, xgboost +0.079, mlp +0.072 | PASS |
| B2 | Top-fifth long-only vs equal weight, after costs | best momentum_4w: Sharpe 0.79 vs 0.76 EW, excess t 0.33 | fail |
