# Track B, version 2: ranking coins

Pre-registered in OUTCOMES.md (Version 2). Out of sample 2023-01-01 to 2026-10-18 (199 weekly formations), the same for every cell. Ridge = simple family, XGBoost = complex family; F0 = version 1 inputs, F1 = F0 + a few, F2 = F0 + all free inputs.

- F1 adds 11: ma_gap_3, ma_gap_5, ma_gap_10, ma_gap_100, vol_ma_3, vol_ma_5, vol_ma_10, vol_ma_20, vol_ma_100, macd, carry_4w
- F2 adds 8 more: funding_change, premium_4w, fut_flow_4w, fut_share_4w, oi_change_4w, top_ls_pos, ls_acct, taker_ls

## Weekly rank IC (primary, B1) and the top-fifth portfolio (B2)

B1 passes when mean IC > 0 with Newey-West t > 2. B2 needs a top-fifth Sharpe above equal weight and excess return t > 2.

| Cell | Inputs | Mean IC | IC t | B1 | Top-fifth Sharpe | EW Sharpe | Excess t | B2 | Turnover/week |
|---|---|---|---|---|---|---|---|---|---|
| F0-ridge | 22 | **+0.082** | 4.12 | PASS | 0.51 | 0.53 | -0.83 | fail | 46% |
| F0-xgboost | 22 | **+0.090** | 5.79 | PASS | 0.37 | 0.53 | -1.28 | fail | 83% |
| F1-ridge | 33 | **+0.078** | 3.94 | PASS | 0.45 | 0.53 | -1.02 | fail | 62% |
| F1-xgboost | 33 | **+0.085** | 5.58 | PASS | 0.45 | 0.53 | -0.98 | fail | 82% |
| F2-ridge | 41 | **+0.085** | 4.42 | PASS | 0.41 | 0.53 | -1.16 | fail | 59% |
| F2-xgboost | 41 | **+0.086** | 5.52 | PASS | 0.46 | 0.53 | -0.94 | fail | 84% |

Reference, 4-week momentum rule: mean IC -0.027 (t -1.87).

## Pre-registered comparisons

Diebold-Mariano on the primary loss, Holm-corrected over the nine tests. A positive statistic favours the challenger.

| Comparison | DM statistic | p | Holm p | Result |
|---|---|---|---|---|
| F1 vs F0 (ridge) | -1.07 | 0.2832 | 1.0000 | no significant difference |
| F2 vs F0 (ridge) | 0.53 | 0.5950 | 1.0000 | no significant difference |
| F2 vs F1 (ridge) | 1.47 | 0.1422 | 1.0000 | no significant difference |
| F1 vs F0 (xgboost) | -0.85 | 0.3949 | 1.0000 | no significant difference |
| F2 vs F0 (xgboost) | -0.56 | 0.5772 | 1.0000 | no significant difference |
| F2 vs F1 (xgboost) | 0.13 | 0.8938 | 1.0000 | no significant difference |
| xgboost vs ridge (F0) | 0.71 | 0.4774 | 1.0000 | no significant difference |
| xgboost vs ridge (F1) | 0.73 | 0.4668 | 1.0000 | no significant difference |
| xgboost vs ridge (F2) | 0.08 | 0.9377 | 1.0000 | no significant difference |

## Decision

Best cell on the primary metric: **F0-xgboost**. Live-test candidate: **F0-ridge** (simplest cell that passes the primary outcome and is not significantly worse than the best).

Information only, not investment advice.
