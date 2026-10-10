# Track B, version 2: ranking coins

Pre-registered in OUTCOMES.md (Version 2). Out of sample 2023-01-01 to 2026-09-27 (196 weekly formations), the same for every cell. Ridge = simple family, XGBoost = complex family; F0 = version 1 inputs, F1 = F0 + a few, F2 = F0 + all free inputs.

- F1 adds 11: ma_gap_3, ma_gap_5, ma_gap_10, ma_gap_100, vol_ma_3, vol_ma_5, vol_ma_10, vol_ma_20, vol_ma_100, macd, carry_4w
- F2 adds 8 more: funding_change, premium_4w, fut_flow_4w, fut_share_4w, oi_change_4w, top_ls_pos, ls_acct, taker_ls

## Weekly rank IC (primary, B1) and the top-fifth portfolio (B2)

B1 passes when mean IC > 0 with Newey-West t > 2. B2 needs a top-fifth Sharpe above equal weight and excess return t > 2.

| Cell | Inputs | Mean IC | IC t | B1 | Top-fifth Sharpe | EW Sharpe | Excess t | B2 | Turnover/week |
|---|---|---|---|---|---|---|---|---|---|
| F0-ridge | 22 | **+0.079** | 3.95 | PASS | 0.57 | 0.60 | -0.94 | fail | 46% |
| F0-xgboost | 22 | **+0.089** | 5.71 | PASS | 0.54 | 0.60 | -0.99 | fail | 83% |
| F1-ridge | 33 | **+0.075** | 3.78 | PASS | 0.51 | 0.60 | -1.12 | fail | 57% |
| F1-xgboost | 33 | **+0.088** | 6.12 | PASS | 0.57 | 0.60 | -0.87 | fail | 86% |
| F2-ridge | 41 | **+0.081** | 4.16 | PASS | 0.51 | 0.60 | -1.08 | fail | 60% |
| F2-xgboost | 41 | **+0.082** | 5.72 | PASS | 0.61 | 0.60 | -0.52 | fail | 83% |

Reference, 4-week momentum rule: mean IC -0.024 (t -1.70).

## Pre-registered comparisons

Diebold-Mariano on the primary loss, Holm-corrected over the nine tests. A positive statistic favours the challenger.

| Comparison | DM statistic | p | Holm p | Result |
|---|---|---|---|---|
| F1 vs F0 (ridge) | -0.98 | 0.3293 | 1.0000 | no significant difference |
| F2 vs F0 (ridge) | 0.37 | 0.7081 | 1.0000 | no significant difference |
| F2 vs F1 (ridge) | 1.18 | 0.2360 | 1.0000 | no significant difference |
| F1 vs F0 (xgboost) | -0.28 | 0.7802 | 1.0000 | no significant difference |
| F2 vs F0 (xgboost) | -1.03 | 0.3030 | 1.0000 | no significant difference |
| F2 vs F1 (xgboost) | -1.08 | 0.2820 | 1.0000 | no significant difference |
| xgboost vs ridge (F0) | 0.94 | 0.3484 | 1.0000 | no significant difference |
| xgboost vs ridge (F1) | 1.13 | 0.2600 | 1.0000 | no significant difference |
| xgboost vs ridge (F2) | 0.10 | 0.9181 | 1.0000 | no significant difference |

## Decision

Best cell on the primary metric: **F0-xgboost**. Live-test candidate: **F0-ridge** (simplest cell that passes the primary outcome and is not significantly worse than the best).

Information only, not investment advice.
