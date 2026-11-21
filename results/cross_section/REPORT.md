# Track B: ranking coins against each other

68 coins with hourly Binance data · 52 eligible coins in a typical week (min 33, max 64) · weekly rebalancing from 2021-01-01 · models refit every 13 weeks · 0.10% cost per side · runtime 0.5 min

IC is the rank correlation between a model's scores and the next week's returns across coins (0 = no information). The top-fifth portfolio holds the highest-scored coins in equal weights; equal weight (EW) holds every eligible coin.

| Model | Mean IC | IC t-stat | Weeks IC > 0 | Top-fifth Sharpe | EW Sharpe | Excess t-stat | Top-fifth annual | EW annual | Long-short Sharpe | Turnover/week |
|---|---|---|---|---|---|---|---|---|---|---|
| momentum_4w | -0.028 | -2.29 | 47% | 0.67 | 0.65 | 0.21 | +23% | +21% | 0.18 | 72% |
| ridge | +0.075 | 4.88 | 61% | 0.60 | 0.65 | -0.92 | +19% | +21% | -0.47 | 50% |
| xgboost | +0.079 | 6.54 | 61% | 0.62 | 0.65 | -0.74 | +20% | +21% | -0.55 | 90% |
| mlp | +0.076 | 7.07 | 62% | 0.64 | 0.65 | -0.48 | +22% | +21% | -0.08 | 98% |

Mean IC by year:

| Model | 2021 | 2022 | 2023 | 2024 | 2025 | 2026 |
|---|---|---|---|---|---|---|
| momentum_4w | -0.068 | +0.010 | -0.010 | -0.036 | +0.010 | -0.080 |
| ridge | -0.020 | +0.128 | +0.042 | +0.070 | +0.119 | +0.116 |
| xgboost | +0.018 | +0.116 | +0.067 | +0.080 | +0.097 | +0.098 |
| mlp | +0.020 | +0.125 | +0.058 | +0.066 | +0.093 | +0.097 |

Caveat stated in advance: the coin list is today's large coins, so past altcoin returns are flattered (survivorship bias).

## Scorecard

| ID | Outcome | Result | Pass |
|---|---|---|---|
| B1 | Weekly rank IC of coin forecasts | best mlp: mean IC +0.076, t 7.07; momentum_4w -0.028, ridge +0.075, xgboost +0.079, mlp +0.076 | PASS |
| B2 | Top-fifth long-only vs equal weight, after costs | best momentum_4w: Sharpe 0.67 vs 0.65 EW, excess t 0.21 | fail |
