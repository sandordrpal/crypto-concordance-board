# Track B: ranking coins against each other

68 coins with hourly Binance data · 52 eligible coins in a typical week (min 33, max 64) · weekly rebalancing from 2021-01-01 · models refit every 13 weeks · 0.10% cost per side · runtime 0.6 min

IC is the rank correlation between a model's scores and the next week's returns across coins (0 = no information). The top-fifth portfolio holds the highest-scored coins in equal weights; equal weight (EW) holds every eligible coin.

| Model | Mean IC | IC t-stat | Weeks IC > 0 | Top-fifth Sharpe | EW Sharpe | Excess t-stat | Top-fifth annual | EW annual | Long-short Sharpe | Turnover/week |
|---|---|---|---|---|---|---|---|---|---|---|
| momentum_4w | -0.027 | -2.24 | 48% | 0.70 | 0.68 | 0.25 | +26% | +24% | 0.20 | 72% |
| ridge | +0.074 | 4.84 | 61% | 0.63 | 0.68 | -0.94 | +21% | +24% | -0.49 | 50% |
| xgboost | +0.082 | 6.77 | 63% | 0.65 | 0.68 | -0.56 | +24% | +24% | -0.56 | 91% |
| mlp | +0.077 | 6.89 | 64% | 0.66 | 0.68 | -0.33 | +24% | +24% | -0.05 | 99% |

Mean IC by year:

| Model | 2021 | 2022 | 2023 | 2024 | 2025 | 2026 |
|---|---|---|---|---|---|---|
| momentum_4w | -0.068 | +0.010 | -0.010 | -0.036 | +0.010 | -0.078 |
| ridge | -0.020 | +0.128 | +0.042 | +0.070 | +0.119 | +0.110 |
| xgboost | +0.018 | +0.125 | +0.070 | +0.080 | +0.099 | +0.102 |
| mlp | +0.025 | +0.120 | +0.058 | +0.072 | +0.094 | +0.097 |

Caveat stated in advance: the coin list is today's large coins, so past altcoin returns are flattered (survivorship bias).

## Scorecard

| ID | Outcome | Result | Pass |
|---|---|---|---|
| B1 | Weekly rank IC of coin forecasts | best mlp: mean IC +0.077, t 6.89; momentum_4w -0.027, ridge +0.074, xgboost +0.082, mlp +0.077 | PASS |
| B2 | Top-fifth long-only vs equal weight, after costs | best momentum_4w: Sharpe 0.70 vs 0.68 EW, excess t 0.25 | fail |
