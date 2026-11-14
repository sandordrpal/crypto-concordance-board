# Track A, version 2: Bitcoin volatility

Pre-registered in OUTCOMES.md (Version 2). Out of sample 2023-01-01 to 2026-11-12 (1412 days), the same for every cell. Ridge = simple family, XGBoost = complex family; F0 = version 1 inputs, F1 = F0 + a few, F2 = F0 + all free inputs.

- F1 adds 4: harq, x_dvol, xvol_eth, xvol_alt
- F2 adds 20 more: fut_funding_d, fut_premium_d, fut_flow_d, fut_spot_volume, oi_chg_1d, oi_chg_7d, top_ls_pos, ls_acct, taker_ls_d, cb_premium_d, x_dvol_eth, vrp, fomc_next_day, fomc_next_7d, cpi_next_day, etf_flow_1d, etf_flow_5d, large_share_d, large_imb_d, xl_imb_d

## Next-day volatility (primary, A1)

QLIKE relative to HAR; below 1.00 is better. Pass = lower than HAR with DM p < 0.05.

| Cell | Inputs | QLIKE vs HAR | DM p | A1 | Next-7-day vs HAR (A2) | Vol-target Sharpe (A3) | Max drawdown |
|---|---|---|---|---|---|---|---|
| F0-ridge | 22 | **0.881×** | 0.000 | PASS | 0.919× (fail) | 0.94 (fail) | -53% |
| F0-xgboost | 22 | **0.827×** | 0.000 | PASS | 0.968× (fail) | 0.93 (fail) | -51% |
| F1-ridge | 26 | **0.881×** | 0.000 | PASS | 0.931× (fail) | 0.95 (fail) | -52% |
| F1-xgboost | 26 | **0.831×** | 0.000 | PASS | 0.972× (fail) | 0.90 (fail) | -50% |
| F2-ridge | 46 | **0.910×** | 0.004 | PASS | 0.969× (fail) | 0.93 (fail) | -53% |
| F2-xgboost | 46 | **0.828×** | 0.000 | PASS | 0.992× (fail) | 0.93 (fail) | -50% |

Buy and hold over the window: Sharpe 1.02, max drawdown -53%; HAR vol-target Sharpe 0.90.

## Pre-registered comparisons

Diebold-Mariano on the primary loss, Holm-corrected over the nine tests. A positive statistic favours the challenger.

| Comparison | DM statistic | p | Holm p | Result |
|---|---|---|---|---|
| F1 vs F0 (ridge) | 0.04 | 0.9646 | 1.0000 | no significant difference |
| F2 vs F0 (ridge) | -1.86 | 0.0626 | 0.3727 | no significant difference |
| F2 vs F1 (ridge) | -2.85 | 0.0044 | 0.0353 | F1-ridge better |
| F1 vs F0 (xgboost) | -0.31 | 0.7564 | 1.0000 | no significant difference |
| F2 vs F0 (xgboost) | -0.10 | 0.9167 | 1.0000 | no significant difference |
| F2 vs F1 (xgboost) | 0.23 | 0.8192 | 1.0000 | no significant difference |
| xgboost vs ridge (F0) | 2.26 | 0.0236 | 0.1650 | no significant difference |
| xgboost vs ridge (F1) | 1.87 | 0.0621 | 0.3727 | no significant difference |
| xgboost vs ridge (F2) | 3.34 | 0.0008 | 0.0076 | F2-xgboost better |

## Decision

Best cell on the primary metric: **F0-xgboost**. Live-test candidate: **F0-ridge** (simplest cell that passes the primary outcome and is not significantly worse than the best).

Information only, not investment advice.
