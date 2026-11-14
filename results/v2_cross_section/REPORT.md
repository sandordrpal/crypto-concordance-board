# Track B, version 2: ranking coins

Pre-registered in OUTCOMES.md (Version 2). Out of sample 2023-01-01 to 2026-11-01 (201 weekly formations), the same for every cell. Ridge = simple family, XGBoost = complex family; F0 = version 1 inputs, F1 = F0 + a few, F2 = F0 + all free inputs.

- F1 adds 11: ma_gap_3, ma_gap_5, ma_gap_10, ma_gap_100, vol_ma_3, vol_ma_5, vol_ma_10, vol_ma_20, vol_ma_100, macd, carry_4w
- F2 adds 8 more: funding_change, premium_4w, fut_flow_4w, fut_share_4w, oi_change_4w, top_ls_pos, ls_acct, taker_ls

## Weekly rank IC (primary, B1) and the top-fifth portfolio (B2)

B1 passes when mean IC > 0 with Newey-West t > 2. B2 needs a top-fifth Sharpe above equal weight and excess return t > 2.

| Cell | Inputs | Mean IC | IC t | B1 | Top-fifth Sharpe | EW Sharpe | Excess t | B2 | Turnover/week |
|---|---|---|---|---|---|---|---|---|---|
| F0-ridge | 22 | **+0.084** | 4.20 | PASS | 0.46 | 0.49 | -0.76 | fail | 46% |
| F0-xgboost | 22 | **+0.087** | 5.73 | PASS | 0.37 | 0.49 | -1.06 | fail | 84% |
| F1-ridge | 33 | **+0.079** | 4.02 | PASS | 0.40 | 0.49 | -0.95 | fail | 61% |
| F1-xgboost | 33 | **+0.092** | 6.40 | PASS | 0.42 | 0.49 | -0.86 | fail | 84% |
| F2-ridge | 41 | **+0.086** | 4.51 | PASS | 0.36 | 0.49 | -1.12 | fail | 60% |
| F2-xgboost | 41 | **+0.082** | 5.32 | PASS | 0.43 | 0.49 | -0.75 | fail | 83% |

Reference, 4-week momentum rule: mean IC -0.027 (t -1.85).

## Pre-registered comparisons

Diebold-Mariano on the primary loss, Holm-corrected over the nine tests. A positive statistic favours the challenger.

| Comparison | DM statistic | p | Holm p | Result |
|---|---|---|---|---|
| F1 vs F0 (ridge) | -1.03 | 0.3024 | 1.0000 | no significant difference |
| F2 vs F0 (ridge) | 0.48 | 0.6294 | 1.0000 | no significant difference |
| F2 vs F1 (ridge) | 1.35 | 0.1766 | 1.0000 | no significant difference |
| F1 vs F0 (xgboost) | 1.02 | 0.3066 | 1.0000 | no significant difference |
| F2 vs F0 (xgboost) | -0.73 | 0.4667 | 1.0000 | no significant difference |
| F2 vs F1 (xgboost) | -1.89 | 0.0586 | 0.5271 | no significant difference |
| xgboost vs ridge (F0) | 0.31 | 0.7573 | 1.0000 | no significant difference |
| xgboost vs ridge (F1) | 1.28 | 0.1997 | 1.0000 | no significant difference |
| xgboost vs ridge (F2) | -0.44 | 0.6598 | 1.0000 | no significant difference |

## Decision

Best cell on the primary metric: **F1-xgboost**. Live-test candidate: **F0-ridge** (simplest cell that passes the primary outcome and is not significantly worse than the best).

Information only, not investment advice.
