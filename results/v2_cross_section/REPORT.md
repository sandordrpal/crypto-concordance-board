# Track B, version 2: ranking coins

Pre-registered in OUTCOMES.md (Version 2). Out of sample 2023-01-01 to 2026-11-08 (202 weekly formations), the same for every cell. Ridge = simple family, XGBoost = complex family; F0 = version 1 inputs, F1 = F0 + a few, F2 = F0 + all free inputs.

- F1 adds 11: ma_gap_3, ma_gap_5, ma_gap_10, ma_gap_100, vol_ma_3, vol_ma_5, vol_ma_10, vol_ma_20, vol_ma_100, macd, carry_4w
- F2 adds 8 more: funding_change, premium_4w, fut_flow_4w, fut_share_4w, oi_change_4w, top_ls_pos, ls_acct, taker_ls

## Weekly rank IC (primary, B1) and the top-fifth portfolio (B2)

B1 passes when mean IC > 0 with Newey-West t > 2. B2 needs a top-fifth Sharpe above equal weight and excess return t > 2.

| Cell | Inputs | Mean IC | IC t | B1 | Top-fifth Sharpe | EW Sharpe | Excess t | B2 | Turnover/week |
|---|---|---|---|---|---|---|---|---|---|
| F0-ridge | 22 | **+0.085** | 4.25 | PASS | 0.41 | 0.44 | -0.73 | fail | 46% |
| F0-xgboost | 22 | **+0.085** | 5.66 | PASS | 0.25 | 0.44 | -1.40 | fail | 83% |
| F1-ridge | 33 | **+0.081** | 4.07 | PASS | 0.36 | 0.44 | -0.90 | fail | 61% |
| F1-xgboost | 33 | **+0.083** | 5.73 | PASS | 0.42 | 0.44 | -0.66 | fail | 85% |
| F2-ridge | 41 | **+0.088** | 4.55 | PASS | 0.31 | 0.44 | -1.09 | fail | 59% |
| F2-xgboost | 41 | **+0.086** | 5.63 | PASS | 0.45 | 0.44 | -0.38 | fail | 86% |

Reference, 4-week momentum rule: mean IC -0.027 (t -1.90).

## Pre-registered comparisons

Diebold-Mariano on the primary loss, Holm-corrected over the nine tests. A positive statistic favours the challenger.

| Comparison | DM statistic | p | Holm p | Result |
|---|---|---|---|---|
| F1 vs F0 (ridge) | -1.05 | 0.2941 | 1.0000 | no significant difference |
| F2 vs F0 (ridge) | 0.52 | 0.6054 | 1.0000 | no significant difference |
| F2 vs F1 (ridge) | 1.41 | 0.1580 | 1.0000 | no significant difference |
| F1 vs F0 (xgboost) | -0.48 | 0.6287 | 1.0000 | no significant difference |
| F2 vs F0 (xgboost) | 0.15 | 0.8787 | 1.0000 | no significant difference |
| F2 vs F1 (xgboost) | 0.50 | 0.6177 | 1.0000 | no significant difference |
| xgboost vs ridge (F0) | -0.04 | 0.9704 | 1.0000 | no significant difference |
| xgboost vs ridge (F1) | 0.19 | 0.8480 | 1.0000 | no significant difference |
| xgboost vs ridge (F2) | -0.24 | 0.8115 | 1.0000 | no significant difference |

## Decision

Best cell on the primary metric: **F2-ridge**. Live-test candidate: **F0-ridge** (simplest cell that passes the primary outcome and is not significantly worse than the best).

Information only, not investment advice.
