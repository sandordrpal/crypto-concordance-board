# Track B, version 2: ranking coins

Pre-registered in OUTCOMES.md (Version 2). Out of sample 2023-01-01 to 2026-10-04 (197 weekly formations), the same for every cell. Ridge = simple family, XGBoost = complex family; F0 = version 1 inputs, F1 = F0 + a few, F2 = F0 + all free inputs.

- F1 adds 11: ma_gap_3, ma_gap_5, ma_gap_10, ma_gap_100, vol_ma_3, vol_ma_5, vol_ma_10, vol_ma_20, vol_ma_100, macd, carry_4w
- F2 adds 8 more: funding_change, premium_4w, fut_flow_4w, fut_share_4w, oi_change_4w, top_ls_pos, ls_acct, taker_ls

## Weekly rank IC (primary, B1) and the top-fifth portfolio (B2)

B1 passes when mean IC > 0 with Newey-West t > 2. B2 needs a top-fifth Sharpe above equal weight and excess return t > 2.

| Cell | Inputs | Mean IC | IC t | B1 | Top-fifth Sharpe | EW Sharpe | Excess t | B2 | Turnover/week |
|---|---|---|---|---|---|---|---|---|---|
| F0-ridge | 22 | **+0.079** | 3.94 | PASS | 0.55 | 0.59 | -0.95 | fail | 46% |
| F0-xgboost | 22 | **+0.086** | 5.70 | PASS | 0.46 | 0.59 | -1.33 | fail | 84% |
| F1-ridge | 33 | **+0.074** | 3.76 | PASS | 0.49 | 0.59 | -1.14 | fail | 62% |
| F1-xgboost | 33 | **+0.081** | 5.38 | PASS | 0.54 | 0.59 | -0.84 | fail | 85% |
| F2-ridge | 41 | **+0.082** | 4.23 | PASS | 0.45 | 0.59 | -1.26 | fail | 59% |
| F2-xgboost | 41 | **+0.081** | 5.46 | PASS | 0.61 | 0.59 | -0.55 | fail | 85% |

Reference, 4-week momentum rule: mean IC -0.023 (t -1.67).

## Pre-registered comparisons

Diebold-Mariano on the primary loss, Holm-corrected over the nine tests. A positive statistic favours the challenger.

| Comparison | DM statistic | p | Holm p | Result |
|---|---|---|---|---|
| F1 vs F0 (ridge) | -1.11 | 0.2655 | 1.0000 | no significant difference |
| F2 vs F0 (ridge) | 0.51 | 0.6081 | 1.0000 | no significant difference |
| F2 vs F1 (ridge) | 1.48 | 0.1380 | 1.0000 | no significant difference |
| F1 vs F0 (xgboost) | -1.04 | 0.2975 | 1.0000 | no significant difference |
| F2 vs F0 (xgboost) | -0.66 | 0.5076 | 1.0000 | no significant difference |
| F2 vs F1 (xgboost) | 0.13 | 0.8967 | 1.0000 | no significant difference |
| xgboost vs ridge (F0) | 0.69 | 0.4922 | 1.0000 | no significant difference |
| xgboost vs ridge (F1) | 0.63 | 0.5272 | 1.0000 | no significant difference |
| xgboost vs ridge (F2) | -0.01 | 0.9903 | 1.0000 | no significant difference |

## Decision

Best cell on the primary metric: **F0-xgboost**. Live-test candidate: **F0-ridge** (simplest cell that passes the primary outcome and is not significantly worse than the best).

Information only, not investment advice.
