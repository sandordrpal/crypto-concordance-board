# Track B, version 2: ranking coins

Pre-registered in OUTCOMES.md (Version 2). Out of sample 2023-01-01 to 2026-10-25 (200 weekly formations), the same for every cell. Ridge = simple family, XGBoost = complex family; F0 = version 1 inputs, F1 = F0 + a few, F2 = F0 + all free inputs.

- F1 adds 11: ma_gap_3, ma_gap_5, ma_gap_10, ma_gap_100, vol_ma_3, vol_ma_5, vol_ma_10, vol_ma_20, vol_ma_100, macd, carry_4w
- F2 adds 8 more: funding_change, premium_4w, fut_flow_4w, fut_share_4w, oi_change_4w, top_ls_pos, ls_acct, taker_ls

## Weekly rank IC (primary, B1) and the top-fifth portfolio (B2)

B1 passes when mean IC > 0 with Newey-West t > 2. B2 needs a top-fifth Sharpe above equal weight and excess return t > 2.

| Cell | Inputs | Mean IC | IC t | B1 | Top-fifth Sharpe | EW Sharpe | Excess t | B2 | Turnover/week |
|---|---|---|---|---|---|---|---|---|---|
| F0-ridge | 22 | **+0.082** | 4.12 | PASS | 0.55 | 0.52 | -0.53 | fail | 44% |
| F0-xgboost | 22 | **+0.090** | 5.89 | PASS | 0.42 | 0.52 | -1.08 | fail | 81% |
| F1-ridge | 33 | **+0.077** | 3.89 | PASS | 0.38 | 0.52 | -1.34 | fail | 60% |
| F1-xgboost | 33 | **+0.084** | 5.68 | PASS | 0.38 | 0.52 | -1.32 | fail | 85% |
| F2-ridge | 41 | **+0.084** | 4.42 | PASS | 0.38 | 0.52 | -1.23 | fail | 59% |
| F2-xgboost | 41 | **+0.081** | 5.27 | PASS | 0.48 | 0.52 | -0.69 | fail | 84% |

Reference, 4-week momentum rule: mean IC -0.028 (t -1.87).

## Pre-registered comparisons

Diebold-Mariano on the primary loss, Holm-corrected over the nine tests. A positive statistic favours the challenger.

| Comparison | DM statistic | p | Holm p | Result |
|---|---|---|---|---|
| F1 vs F0 (ridge) | -0.96 | 0.3384 | 1.0000 | no significant difference |
| F2 vs F0 (ridge) | 0.43 | 0.6655 | 1.0000 | no significant difference |
| F2 vs F1 (ridge) | 1.31 | 0.1901 | 1.0000 | no significant difference |
| F1 vs F0 (xgboost) | -1.28 | 0.1993 | 1.0000 | no significant difference |
| F2 vs F0 (xgboost) | -1.49 | 0.1358 | 1.0000 | no significant difference |
| F2 vs F1 (xgboost) | -0.59 | 0.5557 | 1.0000 | no significant difference |
| xgboost vs ridge (F0) | 0.77 | 0.4390 | 1.0000 | no significant difference |
| xgboost vs ridge (F1) | 0.67 | 0.5058 | 1.0000 | no significant difference |
| xgboost vs ridge (F2) | -0.35 | 0.7227 | 1.0000 | no significant difference |

## Decision

Best cell on the primary metric: **F0-xgboost**. Live-test candidate: **F0-ridge** (simplest cell that passes the primary outcome and is not significantly worse than the best).

Information only, not investment advice.
