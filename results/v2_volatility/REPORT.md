# Track A, version 2: Bitcoin volatility

Pre-registered in OUTCOMES.md (Version 2). Out of sample 2023-01-01 to 2026-11-26 (1426 days), the same for every cell. Ridge = simple family, XGBoost = complex family; F0 = version 1 inputs, F1 = F0 + a few, F2 = F0 + all free inputs.

- F1 adds 4: harq, x_dvol, xvol_eth, xvol_alt
- F2 adds 20 more: fut_funding_d, fut_premium_d, fut_flow_d, fut_spot_volume, oi_chg_1d, oi_chg_7d, top_ls_pos, ls_acct, taker_ls_d, cb_premium_d, x_dvol_eth, vrp, fomc_next_day, fomc_next_7d, cpi_next_day, etf_flow_1d, etf_flow_5d, large_share_d, large_imb_d, xl_imb_d

## Next-day volatility (primary, A1)

QLIKE relative to HAR; below 1.00 is better. Pass = lower than HAR with DM p < 0.05.

| Cell | Inputs | QLIKE vs HAR | DM p | A1 | Next-7-day vs HAR (A2) | Vol-target Sharpe (A3) | Max drawdown |
|---|---|---|---|---|---|---|---|
| F0-ridge | 20 | **0.875×** | 0.000 | PASS | 0.905× (fail) | 0.87 (fail) | -53% |
| F0-xgboost | 20 | **0.835×** | 0.000 | PASS | 0.975× (fail) | 0.85 (fail) | -51% |
| F1-ridge | 24 | **0.875×** | 0.000 | PASS | 0.927× (fail) | 0.87 (fail) | -53% |
| F1-xgboost | 24 | **0.833×** | 0.000 | PASS | 0.991× (fail) | 0.82 (fail) | -51% |
| F2-ridge | 44 | **0.912×** | 0.006 | PASS | 0.967× (fail) | 0.85 (fail) | -53% |
| F2-xgboost | 44 | **0.846×** | 0.000 | PASS | 1.006× (fail) | 0.85 (fail) | -51% |

Buy and hold over the window: Sharpe 0.94, max drawdown -53%; HAR vol-target Sharpe 0.82.

## Pre-registered comparisons

Diebold-Mariano on the primary loss, Holm-corrected over the nine tests. A positive statistic favours the challenger.

| Comparison | DM statistic | p | Holm p | Result |
|---|---|---|---|---|
| F1 vs F0 (ridge) | 0.02 | 0.9803 | 1.0000 | no significant difference |
| F2 vs F0 (ridge) | -2.29 | 0.0223 | 0.1560 | no significant difference |
| F2 vs F1 (ridge) | -3.57 | 0.0004 | 0.0032 | F1-ridge better |
| F1 vs F0 (xgboost) | 0.20 | 0.8437 | 1.0000 | no significant difference |
| F2 vs F0 (xgboost) | -0.81 | 0.4179 | 1.0000 | no significant difference |
| F2 vs F1 (xgboost) | -1.09 | 0.2772 | 1.0000 | no significant difference |
| xgboost vs ridge (F0) | 1.61 | 0.1063 | 0.5316 | no significant difference |
| xgboost vs ridge (F1) | 1.71 | 0.0870 | 0.5219 | no significant difference |
| xgboost vs ridge (F2) | 2.69 | 0.0071 | 0.0567 | no significant difference |

## Decision

Best cell on the primary metric: **F1-xgboost**. Live-test candidate: **F0-ridge** (simplest cell that passes the primary outcome and is not significantly worse than the best).

Information only, not investment advice.
