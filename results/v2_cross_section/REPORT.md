# Track B, version 2: ranking coins

Pre-registered in OUTCOMES.md (Version 2). Out of sample 2023-01-01 to 2026-10-11 (198 weekly formations), the same for every cell. Ridge = simple family, XGBoost = complex family; F0 = version 1 inputs, F1 = F0 + a few, F2 = F0 + all free inputs.

- F1 adds 11: ma_gap_3, ma_gap_5, ma_gap_10, ma_gap_100, vol_ma_3, vol_ma_5, vol_ma_10, vol_ma_20, vol_ma_100, macd, carry_4w
- F2 adds 8 more: funding_change, premium_4w, fut_flow_4w, fut_share_4w, oi_change_4w, top_ls_pos, ls_acct, taker_ls

## Weekly rank IC (primary, B1) and the top-fifth portfolio (B2)

B1 passes when mean IC > 0 with Newey-West t > 2. B2 needs a top-fifth Sharpe above equal weight and excess return t > 2.

| Cell | Inputs | Mean IC | IC t | B1 | Top-fifth Sharpe | EW Sharpe | Excess t | B2 | Turnover/week |
|---|---|---|---|---|---|---|---|---|---|
| F0-ridge | 22 | **+0.081** | 4.05 | PASS | 0.52 | 0.55 | -0.88 | fail | 46% |
| F0-xgboost | 22 | **+0.086** | 5.73 | PASS | 0.42 | 0.55 | -1.17 | fail | 83% |
| F1-ridge | 33 | **+0.076** | 3.87 | PASS | 0.46 | 0.55 | -1.07 | fail | 62% |
| F1-xgboost | 33 | **+0.086** | 5.70 | PASS | 0.45 | 0.55 | -1.12 | fail | 85% |
| F2-ridge | 41 | **+0.083** | 4.35 | PASS | 0.42 | 0.55 | -1.20 | fail | 59% |
| F2-xgboost | 41 | **+0.084** | 5.35 | PASS | 0.46 | 0.55 | -1.01 | fail | 81% |

Reference, 4-week momentum rule: mean IC -0.025 (t -1.78).

## Pre-registered comparisons

Diebold-Mariano on the primary loss, Holm-corrected over the nine tests. A positive statistic favours the challenger.

| Comparison | DM statistic | p | Holm p | Result |
|---|---|---|---|---|
| F1 vs F0 (ridge) | -1.09 | 0.2757 | 1.0000 | no significant difference |
| F2 vs F0 (ridge) | 0.53 | 0.5961 | 1.0000 | no significant difference |
| F2 vs F1 (ridge) | 1.48 | 0.1386 | 1.0000 | no significant difference |
| F1 vs F0 (xgboost) | -0.02 | 0.9870 | 1.0000 | no significant difference |
| F2 vs F0 (xgboost) | -0.31 | 0.7562 | 1.0000 | no significant difference |
| F2 vs F1 (xgboost) | -0.35 | 0.7243 | 1.0000 | no significant difference |
| xgboost vs ridge (F0) | 0.53 | 0.5989 | 1.0000 | no significant difference |
| xgboost vs ridge (F1) | 0.98 | 0.3257 | 1.0000 | no significant difference |
| xgboost vs ridge (F2) | 0.07 | 0.9469 | 1.0000 | no significant difference |

## Decision

Best cell on the primary metric: **F0-xgboost**. Live-test candidate: **F0-ridge** (simplest cell that passes the primary outcome and is not significantly worse than the best).

Information only, not investment advice.
