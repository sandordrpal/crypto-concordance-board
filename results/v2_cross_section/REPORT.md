# Track B, version 2: ranking coins

Pre-registered in OUTCOMES.md (Version 2). Out of sample 2023-01-01 to 2026-11-15 (203 weekly formations), the same for every cell. Ridge = simple family, XGBoost = complex family; F0 = version 1 inputs, F1 = F0 + a few, F2 = F0 + all free inputs.

- F1 adds 11: ma_gap_3, ma_gap_5, ma_gap_10, ma_gap_100, vol_ma_3, vol_ma_5, vol_ma_10, vol_ma_20, vol_ma_100, macd, carry_4w
- F2 adds 8 more: funding_change, premium_4w, fut_flow_4w, fut_share_4w, oi_change_4w, top_ls_pos, ls_acct, taker_ls

## Weekly rank IC (primary, B1) and the top-fifth portfolio (B2)

B1 passes when mean IC > 0 with Newey-West t > 2. B2 needs a top-fifth Sharpe above equal weight and excess return t > 2.

| Cell | Inputs | Mean IC | IC t | B1 | Top-fifth Sharpe | EW Sharpe | Excess t | B2 | Turnover/week |
|---|---|---|---|---|---|---|---|---|---|
| F0-ridge | 22 | **+0.087** | 4.30 | PASS | 0.39 | 0.41 | -0.66 | fail | 46% |
| F0-xgboost | 22 | **+0.089** | 5.99 | PASS | 0.32 | 0.41 | -0.90 | fail | 84% |
| F1-ridge | 33 | **+0.082** | 4.12 | PASS | 0.31 | 0.41 | -1.01 | fail | 61% |
| F1-xgboost | 33 | **+0.090** | 6.16 | PASS | 0.36 | 0.41 | -0.79 | fail | 87% |
| F2-ridge | 41 | **+0.091** | 4.60 | PASS | 0.29 | 0.41 | -0.99 | fail | 60% |
| F2-xgboost | 41 | **+0.083** | 5.41 | PASS | 0.47 | 0.41 | -0.14 | fail | 83% |

Reference, 4-week momentum rule: mean IC -0.026 (t -1.81).

## Pre-registered comparisons

Diebold-Mariano on the primary loss, Holm-corrected over the nine tests. A positive statistic favours the challenger.

| Comparison | DM statistic | p | Holm p | Result |
|---|---|---|---|---|
| F1 vs F0 (ridge) | -1.11 | 0.2661 | 1.0000 | no significant difference |
| F2 vs F0 (ridge) | 0.63 | 0.5278 | 1.0000 | no significant difference |
| F2 vs F1 (ridge) | 1.55 | 0.1214 | 1.0000 | no significant difference |
| F1 vs F0 (xgboost) | 0.06 | 0.9493 | 1.0000 | no significant difference |
| F2 vs F0 (xgboost) | -1.01 | 0.3144 | 1.0000 | no significant difference |
| F2 vs F1 (xgboost) | -1.06 | 0.2888 | 1.0000 | no significant difference |
| xgboost vs ridge (F0) | 0.19 | 0.8486 | 1.0000 | no significant difference |
| xgboost vs ridge (F1) | 0.68 | 0.4970 | 1.0000 | no significant difference |
| xgboost vs ridge (F2) | -0.81 | 0.4202 | 1.0000 | no significant difference |

## Decision

Best cell on the primary metric: **F2-ridge**. Live-test candidate: **F0-ridge** (simplest cell that passes the primary outcome and is not significantly worse than the best).

Information only, not investment advice.
