# Track B: ranking coins against each other

68 coins with hourly Binance data · 52 eligible coins in a typical week (min 33, max 64) · weekly rebalancing from 2021-01-01 · models refit every 13 weeks · 0.10% cost per side · runtime 0.7 min

IC is the rank correlation between a model's scores and the next week's returns across coins (0 = no information). The top-fifth portfolio holds the highest-scored coins in equal weights; equal weight (EW) holds every eligible coin.

| Model | Mean IC | IC t-stat | Weeks IC > 0 | Top-fifth Sharpe | EW Sharpe | Excess t-stat | Top-fifth annual | EW annual | Long-short Sharpe | Turnover/week |
|---|---|---|---|---|---|---|---|---|---|---|
| momentum_4w | -0.027 | -2.22 | 48% | 0.65 | 0.63 | 0.21 | +21% | +19% | 0.19 | 72% |
| ridge | +0.076 | 4.92 | 61% | 0.59 | 0.63 | -0.87 | +18% | +19% | -0.45 | 50% |
| xgboost | +0.081 | 6.62 | 63% | 0.69 | 0.63 | -0.18 | +27% | +19% | -0.43 | 89% |
| mlp | +0.076 | 6.49 | 63% | 0.53 | 0.63 | -0.95 | +12% | +19% | -0.09 | 96% |

Mean IC by year:

| Model | 2021 | 2022 | 2023 | 2024 | 2025 | 2026 |
|---|---|---|---|---|---|---|
| momentum_4w | -0.068 | +0.010 | -0.010 | -0.036 | +0.010 | -0.073 |
| ridge | -0.020 | +0.128 | +0.042 | +0.070 | +0.119 | +0.124 |
| xgboost | +0.011 | +0.117 | +0.067 | +0.076 | +0.110 | +0.107 |
| mlp | +0.013 | +0.126 | +0.059 | +0.064 | +0.088 | +0.110 |

Caveat stated in advance: the coin list is today's large coins, so past altcoin returns are flattered (survivorship bias).

## Scorecard

| ID | Outcome | Result | Pass |
|---|---|---|---|
| B1 | Weekly rank IC of coin forecasts | best xgboost: mean IC +0.081, t 6.62; momentum_4w -0.027, ridge +0.076, xgboost +0.081, mlp +0.076 | PASS |
| B2 | Top-fifth long-only vs equal weight, after costs | best momentum_4w: Sharpe 0.65 vs 0.63 EW, excess t 0.21 | fail |
