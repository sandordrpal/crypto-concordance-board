# Track A, version 2: Bitcoin volatility

Pre-registered in OUTCOMES.md (Version 2). Out of sample 2023-01-01 to 2026-10-15 (1384 days), the same for every cell. Ridge = simple family, XGBoost = complex family; F0 = version 1 inputs, F1 = F0 + a few, F2 = F0 + all free inputs.

- F1 adds 4: harq, x_dvol, xvol_eth, xvol_alt
- F2 adds 18 more: fut_funding_d, fut_premium_d, fut_flow_d, fut_spot_volume, oi_chg_1d, oi_chg_7d, top_ls_pos, ls_acct, taker_ls_d, cb_premium_d, x_dvol_eth, vrp, fomc_next_day, fomc_next_7d, cpi_next_day, large_share_d, large_imb_d, xl_imb_d

## Next-day volatility (primary, A1)

QLIKE relative to HAR; below 1.00 is better. Pass = lower than HAR with DM p < 0.05.

| Cell | Inputs | QLIKE vs HAR | DM p | A1 | Next-7-day vs HAR (A2) | Vol-target Sharpe (A3) | Max drawdown |
|---|---|---|---|---|---|---|---|
| F0-ridge | 21 | **0.880×** | 0.000 | PASS | 0.922× (fail) | 1.07 (fail) | -53% |
| F0-xgboost | 21 | **0.829×** | 0.000 | PASS | 0.985× (fail) | 1.05 (fail) | -51% |
| F1-ridge | 25 | **0.881×** | 0.000 | PASS | 0.932× (fail) | 1.07 (fail) | -53% |
| F1-xgboost | 25 | **0.823×** | 0.000 | PASS | 0.971× (fail) | 1.03 (fail) | -51% |
| F2-ridge | 43 | **0.907×** | 0.003 | PASS | 0.974× (fail) | 1.06 (fail) | -53% |
| F2-xgboost | 43 | **0.837×** | 0.000 | PASS | 1.009× (fail) | 1.06 (fail) | -51% |

Buy and hold over the window: Sharpe 1.14, max drawdown -53%; HAR vol-target Sharpe 1.03.

## Pre-registered comparisons

Diebold-Mariano on the primary loss, Holm-corrected over the nine tests. A positive statistic favours the challenger.

| Comparison | DM statistic | p | Holm p | Result |
|---|---|---|---|---|
| F1 vs F0 (ridge) | -0.09 | 0.9270 | 1.0000 | no significant difference |
| F2 vs F0 (ridge) | -1.71 | 0.0870 | 0.4349 | no significant difference |
| F2 vs F1 (ridge) | -2.44 | 0.0148 | 0.1187 | no significant difference |
| F1 vs F0 (xgboost) | 0.51 | 0.6127 | 1.0000 | no significant difference |
| F2 vs F0 (xgboost) | -0.51 | 0.6130 | 1.0000 | no significant difference |
| F2 vs F1 (xgboost) | -1.15 | 0.2482 | 0.9928 | no significant difference |
| xgboost vs ridge (F0) | 1.97 | 0.0488 | 0.2930 | no significant difference |
| xgboost vs ridge (F1) | 2.34 | 0.0191 | 0.1340 | no significant difference |
| xgboost vs ridge (F2) | 2.72 | 0.0065 | 0.0583 | no significant difference |

## Decision

Best cell on the primary metric: **F1-xgboost**. Live-test candidate: **F0-ridge** (simplest cell that passes the primary outcome and is not significantly worse than the best).

Information only, not investment advice.
