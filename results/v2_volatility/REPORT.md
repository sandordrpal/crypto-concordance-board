# Track A, version 2: Bitcoin volatility

Pre-registered in OUTCOMES.md (Version 2). Out of sample 2023-01-01 to 2026-10-08 (1377 days), the same for every cell. Ridge = simple family, XGBoost = complex family; F0 = version 1 inputs, F1 = F0 + a few, F2 = F0 + all free inputs.

- F1 adds 4: harq, x_dvol, xvol_eth, xvol_alt
- F2 adds 18 more: fut_funding_d, fut_premium_d, fut_flow_d, fut_spot_volume, oi_chg_1d, oi_chg_7d, top_ls_pos, ls_acct, taker_ls_d, cb_premium_d, x_dvol_eth, vrp, fomc_next_day, fomc_next_7d, cpi_next_day, large_share_d, large_imb_d, xl_imb_d

## Next-day volatility (primary, A1)

QLIKE relative to HAR; below 1.00 is better. Pass = lower than HAR with DM p < 0.05.

| Cell | Inputs | QLIKE vs HAR | DM p | A1 | Next-7-day vs HAR (A2) | Vol-target Sharpe (A3) | Max drawdown |
|---|---|---|---|---|---|---|---|
| F0-ridge | 23 | **0.873×** | 0.000 | PASS | 0.890× (PASS) | 1.08 (fail) | -53% |
| F0-xgboost | 23 | **0.829×** | 0.000 | PASS | 0.960× (fail) | 1.05 (fail) | -51% |
| F1-ridge | 27 | **0.876×** | 0.000 | PASS | 0.907× (fail) | 1.08 (fail) | -52% |
| F1-xgboost | 27 | **0.825×** | 0.000 | PASS | 0.964× (fail) | 1.03 (fail) | -51% |
| F2-ridge | 45 | **0.891×** | 0.000 | PASS | 0.959× (fail) | 1.07 (fail) | -53% |
| F2-xgboost | 45 | **0.834×** | 0.000 | PASS | 1.023× (fail) | 1.05 (fail) | -51% |

Buy and hold over the window: Sharpe 1.15, max drawdown -53%; HAR vol-target Sharpe 1.04.

## Pre-registered comparisons

Diebold-Mariano on the primary loss, Holm-corrected over the nine tests. A positive statistic favours the challenger.

| Comparison | DM statistic | p | Holm p | Result |
|---|---|---|---|---|
| F1 vs F0 (ridge) | -0.23 | 0.8218 | 1.0000 | no significant difference |
| F2 vs F0 (ridge) | -1.14 | 0.2547 | 1.0000 | no significant difference |
| F2 vs F1 (ridge) | -1.45 | 0.1464 | 0.8784 | no significant difference |
| F1 vs F0 (xgboost) | 0.34 | 0.7319 | 1.0000 | no significant difference |
| F2 vs F0 (xgboost) | -0.29 | 0.7715 | 1.0000 | no significant difference |
| F2 vs F1 (xgboost) | -0.62 | 0.5345 | 1.0000 | no significant difference |
| xgboost vs ridge (F0) | 1.55 | 0.1208 | 0.8456 | no significant difference |
| xgboost vs ridge (F1) | 2.34 | 0.0192 | 0.1727 | no significant difference |
| xgboost vs ridge (F2) | 2.26 | 0.0237 | 0.1896 | no significant difference |

## Decision

Best cell on the primary metric: **F1-xgboost**. Live-test candidate: **F0-ridge** (simplest cell that passes the primary outcome and is not significantly worse than the best).

Information only, not investment advice.
