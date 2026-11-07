# Track B: ranking coins against each other

67 coins with hourly Binance data · 52 eligible coins in a typical week (min 32, max 63) · weekly rebalancing from 2021-01-01 · models refit every 13 weeks · 0.10% cost per side · runtime 1.1 min

IC is the rank correlation between a model's scores and the next week's returns across coins (0 = no information). The top-fifth portfolio holds the highest-scored coins in equal weights; equal weight (EW) holds every eligible coin.

| Model | Mean IC | IC t-stat | Weeks IC > 0 | Top-fifth Sharpe | EW Sharpe | Excess t-stat | Top-fifth annual | EW annual | Long-short Sharpe | Turnover/week |
|---|---|---|---|---|---|---|---|---|---|---|
| momentum_4w | -0.028 | -2.25 | 48% | 0.75 | 0.71 | 0.38 | +32% | +27% | 0.24 | 71% |
| ridge | +0.073 | 4.81 | 62% | 0.69 | 0.71 | -0.71 | +27% | +27% | -0.42 | 49% |
| xgboost | +0.080 | 6.53 | 62% | 0.79 | 0.71 | 0.25 | +38% | +27% | -0.18 | 87% |
| mlp | +0.079 | 6.80 | 63% | 0.71 | 0.71 | -0.30 | +30% | +27% | -0.39 | 98% |

Mean IC by year:

| Model | 2021 | 2022 | 2023 | 2024 | 2025 | 2026 |
|---|---|---|---|---|---|---|
| momentum_4w | -0.066 | +0.010 | -0.009 | -0.034 | +0.009 | -0.087 |
| ridge | -0.020 | +0.131 | +0.040 | +0.069 | +0.115 | +0.107 |
| xgboost | +0.007 | +0.117 | +0.071 | +0.093 | +0.094 | +0.104 |
| mlp | +0.012 | +0.123 | +0.071 | +0.083 | +0.102 | +0.084 |

Caveat stated in advance: the coin list is today's large coins, so past altcoin returns are flattered (survivorship bias).

## Scorecard

| ID | Outcome | Result | Pass |
|---|---|---|---|
| B1 | Weekly rank IC of coin forecasts | best mlp: mean IC +0.079, t 6.80; momentum_4w -0.028, ridge +0.073, xgboost +0.080, mlp +0.079 | PASS |
| B2 | Top-fifth long-only vs equal weight, after costs | best momentum_4w: Sharpe 0.75 vs 0.71 EW, excess t 0.38 | fail |
