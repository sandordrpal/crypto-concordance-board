# Track B: ranking coins against each other

68 coins with hourly Binance data · 52 eligible coins in a typical week (min 33, max 64) · weekly rebalancing from 2021-01-01 · models refit every 13 weeks · 0.10% cost per side · runtime 1.1 min

IC is the rank correlation between a model's scores and the next week's returns across coins (0 = no information). The top-fifth portfolio holds the highest-scored coins in equal weights; equal weight (EW) holds every eligible coin.

| Model | Mean IC | IC t-stat | Weeks IC > 0 | Top-fifth Sharpe | EW Sharpe | Excess t-stat | Top-fifth annual | EW annual | Long-short Sharpe | Turnover/week |
|---|---|---|---|---|---|---|---|---|---|---|
| momentum_4w | -0.027 | -2.19 | 48% | 0.74 | 0.72 | 0.26 | +31% | +29% | 0.21 | 71% |
| ridge | +0.071 | 4.71 | 61% | 0.66 | 0.72 | -1.03 | +24% | +29% | -0.51 | 50% |
| xgboost | +0.079 | 6.69 | 66% | 0.72 | 0.72 | -0.52 | +30% | +29% | -0.44 | 89% |
| mlp | +0.075 | 6.79 | 62% | 0.78 | 0.72 | 0.11 | +37% | +29% | -0.26 | 97% |

Mean IC by year:

| Model | 2021 | 2022 | 2023 | 2024 | 2025 | 2026 |
|---|---|---|---|---|---|---|
| momentum_4w | -0.068 | +0.010 | -0.010 | -0.036 | +0.010 | -0.076 |
| ridge | -0.020 | +0.128 | +0.042 | +0.070 | +0.119 | +0.097 |
| xgboost | +0.019 | +0.112 | +0.072 | +0.085 | +0.107 | +0.079 |
| mlp | +0.020 | +0.135 | +0.064 | +0.069 | +0.087 | +0.074 |

Caveat stated in advance: the coin list is today's large coins, so past altcoin returns are flattered (survivorship bias).

## Scorecard

| ID | Outcome | Result | Pass |
|---|---|---|---|
| B1 | Weekly rank IC of coin forecasts | best mlp: mean IC +0.075, t 6.79; momentum_4w -0.027, ridge +0.071, xgboost +0.079, mlp +0.075 | PASS |
| B2 | Top-fifth long-only vs equal weight, after costs | best momentum_4w: Sharpe 0.74 vs 0.72 EW, excess t 0.26 | fail |
