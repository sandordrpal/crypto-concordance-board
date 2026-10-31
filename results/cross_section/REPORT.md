# Track B: ranking coins against each other

68 coins with hourly Binance data · 52 eligible coins in a typical week (min 33, max 64) · weekly rebalancing from 2021-01-01 · models refit every 13 weeks · 0.10% cost per side · runtime 1.2 min

IC is the rank correlation between a model's scores and the next week's returns across coins (0 = no information). The top-fifth portfolio holds the highest-scored coins in equal weights; equal weight (EW) holds every eligible coin.

| Model | Mean IC | IC t-stat | Weeks IC > 0 | Top-fifth Sharpe | EW Sharpe | Excess t-stat | Top-fifth annual | EW annual | Long-short Sharpe | Turnover/week |
|---|---|---|---|---|---|---|---|---|---|---|
| momentum_4w | -0.028 | -2.26 | 48% | 0.72 | 0.71 | 0.21 | +29% | +27% | 0.19 | 72% |
| ridge | +0.073 | 4.77 | 61% | 0.66 | 0.71 | -0.99 | +24% | +27% | -0.50 | 50% |
| xgboost | +0.084 | 6.90 | 62% | 0.81 | 0.71 | 0.16 | +39% | +27% | -0.60 | 91% |
| mlp | +0.074 | 6.80 | 62% | 0.71 | 0.71 | -0.52 | +28% | +27% | -0.33 | 96% |

Mean IC by year:

| Model | 2021 | 2022 | 2023 | 2024 | 2025 | 2026 |
|---|---|---|---|---|---|---|
| momentum_4w | -0.068 | +0.010 | -0.010 | -0.036 | +0.010 | -0.084 |
| ridge | -0.020 | +0.128 | +0.042 | +0.070 | +0.119 | +0.104 |
| xgboost | +0.020 | +0.125 | +0.078 | +0.082 | +0.111 | +0.087 |
| mlp | +0.016 | +0.122 | +0.058 | +0.072 | +0.095 | +0.086 |

Caveat stated in advance: the coin list is today's large coins, so past altcoin returns are flattered (survivorship bias).

## Scorecard

| ID | Outcome | Result | Pass |
|---|---|---|---|
| B1 | Weekly rank IC of coin forecasts | best xgboost: mean IC +0.084, t 6.90; momentum_4w -0.028, ridge +0.073, xgboost +0.084, mlp +0.074 | PASS |
| B2 | Top-fifth long-only vs equal weight, after costs | best momentum_4w: Sharpe 0.72 vs 0.71 EW, excess t 0.21 | fail |
