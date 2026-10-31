# Track A, version 2: Bitcoin volatility

Pre-registered in OUTCOMES.md (Version 2). Out of sample 2023-01-01 to 2026-10-29 (1398 days), the same for every cell. Ridge = simple family, XGBoost = complex family; F0 = version 1 inputs, F1 = F0 + a few, F2 = F0 + all free inputs.

- F1 adds 4: harq, x_dvol, xvol_eth, xvol_alt
- F2 adds 20 more: fut_funding_d, fut_premium_d, fut_flow_d, fut_spot_volume, oi_chg_1d, oi_chg_7d, top_ls_pos, ls_acct, taker_ls_d, cb_premium_d, x_dvol_eth, vrp, fomc_next_day, fomc_next_7d, cpi_next_day, etf_flow_1d, etf_flow_5d, large_share_d, large_imb_d, xl_imb_d

## Next-day volatility (primary, A1)

QLIKE relative to HAR; below 1.00 is better. Pass = lower than HAR with DM p < 0.05.

| Cell | Inputs | QLIKE vs HAR | DM p | A1 | Next-7-day vs HAR (A2) | Vol-target Sharpe (A3) | Max drawdown |
|---|---|---|---|---|---|---|---|
| F0-ridge | 23 | **0.878×** | 0.000 | PASS | 0.909× (fail) | 1.03 (fail) | -53% |
| F0-xgboost | 23 | **0.820×** | 0.000 | PASS | 0.972× (fail) | 0.98 (fail) | -51% |
| F1-ridge | 27 | **0.881×** | 0.000 | PASS | 0.919× (fail) | 1.03 (fail) | -52% |
| F1-xgboost | 27 | **0.828×** | 0.000 | PASS | 0.956× (fail) | 0.98 (fail) | -51% |
| F2-ridge | 47 | **0.898×** | 0.000 | PASS | 0.959× (fail) | 1.02 (fail) | -53% |
| F2-xgboost | 47 | **0.831×** | 0.000 | PASS | 0.999× (fail) | 1.02 (fail) | -51% |

Buy and hold over the window: Sharpe 1.10, max drawdown -53%; HAR vol-target Sharpe 0.99.

## Pre-registered comparisons

Diebold-Mariano on the primary loss, Holm-corrected over the nine tests. A positive statistic favours the challenger.

| Comparison | DM statistic | p | Holm p | Result |
|---|---|---|---|---|
| F1 vs F0 (ridge) | -0.23 | 0.8162 | 1.0000 | no significant difference |
| F2 vs F0 (ridge) | -1.34 | 0.1812 | 0.9062 | no significant difference |
| F2 vs F1 (ridge) | -1.61 | 0.1070 | 0.6421 | no significant difference |
| F1 vs F0 (xgboost) | -0.58 | 0.5590 | 1.0000 | no significant difference |
| F2 vs F0 (xgboost) | -0.84 | 0.4001 | 1.0000 | no significant difference |
| F2 vs F1 (xgboost) | -0.30 | 0.7633 | 1.0000 | no significant difference |
| xgboost vs ridge (F0) | 1.96 | 0.0499 | 0.3490 | no significant difference |
| xgboost vs ridge (F1) | 2.30 | 0.0213 | 0.1703 | no significant difference |
| xgboost vs ridge (F2) | 2.45 | 0.0142 | 0.1274 | no significant difference |

## Decision

Best cell on the primary metric: **F0-xgboost**. Live-test candidate: **F0-ridge** (simplest cell that passes the primary outcome and is not significantly worse than the best).

Information only, not investment advice.
