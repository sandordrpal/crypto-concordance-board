# Track A, version 2: Bitcoin volatility

Pre-registered in OUTCOMES.md (Version 2). Out of sample 2023-01-01 to 2026-10-22 (1391 days), the same for every cell. Ridge = simple family, XGBoost = complex family; F0 = version 1 inputs, F1 = F0 + a few, F2 = F0 + all free inputs.

- F1 adds 4: harq, x_dvol, xvol_eth, xvol_alt
- F2 adds 18 more: fut_funding_d, fut_premium_d, fut_flow_d, fut_spot_volume, oi_chg_1d, oi_chg_7d, top_ls_pos, ls_acct, taker_ls_d, cb_premium_d, x_dvol_eth, vrp, fomc_next_day, fomc_next_7d, cpi_next_day, large_share_d, large_imb_d, xl_imb_d

## Next-day volatility (primary, A1)

QLIKE relative to HAR; below 1.00 is better. Pass = lower than HAR with DM p < 0.05.

| Cell | Inputs | QLIKE vs HAR | DM p | A1 | Next-7-day vs HAR (A2) | Vol-target Sharpe (A3) | Max drawdown |
|---|---|---|---|---|---|---|---|
| F0-ridge | 22 | **0.880×** | 0.000 | PASS | 0.918× (fail) | 1.06 (fail) | -53% |
| F0-xgboost | 22 | **0.825×** | 0.000 | PASS | 0.968× (fail) | 1.05 (fail) | -51% |
| F1-ridge | 26 | **0.881×** | 0.000 | PASS | 0.929× (fail) | 1.06 (fail) | -52% |
| F1-xgboost | 26 | **0.831×** | 0.000 | PASS | 0.972× (fail) | 1.03 (fail) | -50% |
| F2-ridge | 44 | **0.908×** | 0.004 | PASS | 0.972× (fail) | 1.06 (fail) | -53% |
| F2-xgboost | 44 | **0.837×** | 0.000 | PASS | 0.998× (fail) | 1.04 (fail) | -51% |

Buy and hold over the window: Sharpe 1.13, max drawdown -53%; HAR vol-target Sharpe 1.02.

## Pre-registered comparisons

Diebold-Mariano on the primary loss, Holm-corrected over the nine tests. A positive statistic favours the challenger.

| Comparison | DM statistic | p | Holm p | Result |
|---|---|---|---|---|
| F1 vs F0 (ridge) | -0.04 | 0.9641 | 1.0000 | no significant difference |
| F2 vs F0 (ridge) | -1.78 | 0.0757 | 0.4039 | no significant difference |
| F2 vs F1 (ridge) | -2.61 | 0.0090 | 0.0810 | no significant difference |
| F1 vs F0 (xgboost) | -0.46 | 0.6486 | 1.0000 | no significant difference |
| F2 vs F0 (xgboost) | -0.98 | 0.3251 | 1.0000 | no significant difference |
| F2 vs F1 (xgboost) | -0.51 | 0.6119 | 1.0000 | no significant difference |
| xgboost vs ridge (F0) | 2.27 | 0.0235 | 0.1643 | no significant difference |
| xgboost vs ridge (F1) | 1.83 | 0.0673 | 0.4039 | no significant difference |
| xgboost vs ridge (F2) | 2.56 | 0.0104 | 0.0829 | no significant difference |

## Decision

Best cell on the primary metric: **F0-xgboost**. Live-test candidate: **F0-ridge** (simplest cell that passes the primary outcome and is not significantly worse than the best).

Information only, not investment advice.
