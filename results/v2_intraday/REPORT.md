# Track C, version 2: Bitcoin intraday

Pre-registered in OUTCOMES.md (Version 2). Out of sample 2023-01-01 to 2026-11-06 (33740 hours), the same for every cell. Ridge = simple family, XGBoost = complex family; F0 = version 1 inputs, F1 = F0 + a few, F2 = F0 + all free inputs.

- F1 adds 5: premium_1h, premium_chg_4h, funding_last, cb_premium, cb_premium_chg_4h
- F2 adds 23 more: oi_chg_1h, oi_chg_4h, oi_chg_24h, top_ls_pos, ls_acct, taker_ls, fut_flow_1h, fut_flow_4h, fut_spot_24h, dvol_level, dvol_chg_1h, dvol_chg_24h, eth_premium_1h, trade_size_z, fomc_soon, fomc_after, cpi_soon, cpi_after, etf_flow_1d, large_imb_1h, large_imb_4h, large_share_4h, xl_imb_4h

## Next-4-hour return (primary, C1) and the long/flat strategy (C2)

C1 passes when R²oos > 0 with DM p < 0.05 and hit rate > 51%. C2 needs a net Sharpe above buy-and-hold and positive net return in at least 3 of the 4 years.

| Cell | Inputs | R²oos | DM p | Hit rate | C1 | Strategy Sharpe | Positive years | Time invested | C2 |
|---|---|---|---|---|---|---|---|---|---|
| F0-ridge | 35 | **+0.022%** | 0.329 | 50.8% | fail | – | 0/4 | 0% | fail |
| F0-xgboost | 35 | **-0.137%** | 0.293 | 50.0% | fail | 1.41 | 2/4 | 1% | fail |
| F1-ridge | 40 | **+0.027%** | 0.487 | 50.4% | fail | – | 0/4 | 0% | fail |
| F1-xgboost | 40 | **-0.089%** | 0.552 | 50.0% | fail | 0.75 | 1/4 | 1% | fail |
| F2-ridge | 63 | **+0.159%** | 0.010 | 50.8% | fail | – | 0/4 | 0% | fail |
| F2-xgboost | 63 | **-0.117%** | 0.423 | 49.8% | fail | 1.04 | 2/4 | 4% | fail |

Buy and hold over the window: Sharpe 1.09, max drawdown -53%.

## Pre-registered comparisons

Diebold-Mariano on the primary loss, Holm-corrected over the nine tests. A positive statistic favours the challenger.

| Comparison | DM statistic | p | Holm p | Result |
|---|---|---|---|---|
| F1 vs F0 (ridge) | 0.24 | 0.8067 | 1.0000 | no significant difference |
| F2 vs F0 (ridge) | 2.44 | 0.0149 | 0.1188 | no significant difference |
| F2 vs F1 (ridge) | 2.50 | 0.0123 | 0.1106 | no significant difference |
| F1 vs F0 (xgboost) | 0.69 | 0.4907 | 1.0000 | no significant difference |
| F2 vs F0 (xgboost) | 0.24 | 0.8071 | 1.0000 | no significant difference |
| F2 vs F1 (xgboost) | -0.36 | 0.7202 | 1.0000 | no significant difference |
| xgboost vs ridge (F0) | -1.23 | 0.2190 | 1.0000 | no significant difference |
| xgboost vs ridge (F1) | -0.77 | 0.4405 | 1.0000 | no significant difference |
| xgboost vs ridge (F2) | -1.95 | 0.0513 | 0.3589 | no significant difference |

## Decision

Best cell on the primary metric: **F2-ridge**. Live-test candidate: **none** (no cell passes the primary outcome).

Information only, not investment advice.
