# Track B: ranking coins against each other

68 coins with hourly Binance data · 52 eligible coins in a typical week (min 33, max 64) · weekly rebalancing from 2021-01-01 · models refit every 13 weeks · 0.10% cost per side · runtime 1.1 min

IC is the rank correlation between a model's scores and the next week's returns across coins (0 = no information). The top-fifth portfolio holds the highest-scored coins in equal weights; equal weight (EW) holds every eligible coin.

| Model | Mean IC | IC t-stat | Weeks IC > 0 | Top-fifth Sharpe | EW Sharpe | Excess t-stat | Top-fifth annual | EW annual | Long-short Sharpe | Turnover/week |
|---|---|---|---|---|---|---|---|---|---|---|
| momentum_4w | -0.025 | -2.10 | 48% | 0.77 | 0.74 | 0.30 | +34% | +31% | 0.23 | 71% |
| ridge | +0.070 | 4.62 | 60% | 0.68 | 0.74 | -1.08 | +26% | +31% | -0.53 | 50% |
| xgboost | +0.080 | 6.60 | 62% | 0.66 | 0.74 | -1.25 | +24% | +31% | -0.66 | 91% |
| mlp | +0.074 | 6.56 | 62% | 0.76 | 0.74 | -0.15 | +35% | +31% | 0.00 | 98% |

Mean IC by year:

| Model | 2021 | 2022 | 2023 | 2024 | 2025 | 2026 |
|---|---|---|---|---|---|---|
| momentum_4w | -0.068 | +0.010 | -0.010 | -0.036 | +0.010 | -0.067 |
| ridge | -0.020 | +0.128 | +0.042 | +0.070 | +0.119 | +0.088 |
| xgboost | +0.019 | +0.115 | +0.083 | +0.091 | +0.099 | +0.069 |
| mlp | +0.018 | +0.132 | +0.064 | +0.074 | +0.080 | +0.074 |

Caveat stated in advance: the coin list is today's large coins, so past altcoin returns are flattered (survivorship bias).

## Scorecard

| ID | Outcome | Result | Pass |
|---|---|---|---|
| B1 | Weekly rank IC of coin forecasts | best xgboost: mean IC +0.080, t 6.60; momentum_4w -0.025, ridge +0.070, xgboost +0.080, mlp +0.074 | PASS |
| B2 | Top-fifth long-only vs equal weight, after costs | best momentum_4w: Sharpe 0.77 vs 0.74 EW, excess t 0.30 | fail |
