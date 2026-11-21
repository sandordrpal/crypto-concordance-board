# Track C, version 2: Bitcoin intraday

Pre-registered in OUTCOMES.md (Version 2). Out of sample 2023-01-01 to 2026-11-20 (34076 hours), the same for every cell. Ridge = simple family, XGBoost = complex family; F0 = version 1 inputs, F1 = F0 + a few, F2 = F0 + all free inputs.

- F1 adds 5: premium_1h, premium_chg_4h, funding_last, cb_premium, cb_premium_chg_4h
- F2 adds 23 more: oi_chg_1h, oi_chg_4h, oi_chg_24h, top_ls_pos, ls_acct, taker_ls, fut_flow_1h, fut_flow_4h, fut_spot_24h, dvol_level, dvol_chg_1h, dvol_chg_24h, eth_premium_1h, trade_size_z, fomc_soon, fomc_after, cpi_soon, cpi_after, etf_flow_1d, large_imb_1h, large_imb_4h, large_share_4h, xl_imb_4h

## Next-4-hour return (primary, C1) and the long/flat strategy (C2)

C1 passes when R²oos > 0 with DM p < 0.05 and hit rate > 51%. C2 needs a net Sharpe above buy-and-hold and positive net return in at least 3 of the 4 years.

| Cell | Inputs | R²oos | DM p | Hit rate | C1 | Strategy Sharpe | Positive years | Time invested | C2 |
|---|---|---|---|---|---|---|---|---|---|
| F0-ridge | 35 | **+0.016%** | 0.472 | 50.7% | fail | – | 0/4 | 0% | fail |
| F0-xgboost | 35 | **-0.130%** | 0.301 | 49.7% | fail | 0.85 | 2/4 | 0% | fail |
| F1-ridge | 40 | **+0.020%** | 0.599 | 50.3% | fail | – | 0/4 | 0% | fail |
| F1-xgboost | 40 | **-0.091%** | 0.516 | 49.9% | fail | 0.66 | 1/4 | 1% | fail |
| F2-ridge | 63 | **+0.177%** | 0.004 | 50.9% | fail | – | 0/4 | 0% | fail |
| F2-xgboost | 63 | **-0.113%** | 0.422 | 49.6% | fail | 1.08 | 2/4 | 4% | fail |

Buy and hold over the window: Sharpe 0.94, max drawdown -53%.

## Pre-registered comparisons

Diebold-Mariano on the primary loss, Holm-corrected over the nine tests. A positive statistic favours the challenger.

| Comparison | DM statistic | p | Holm p | Result |
|---|---|---|---|---|
| F1 vs F0 (ridge) | 0.20 | 0.8383 | 1.0000 | no significant difference |
| F2 vs F0 (ridge) | 2.85 | 0.0044 | 0.0355 | F2-ridge better |
| F2 vs F1 (ridge) | 2.94 | 0.0032 | 0.0291 | F2-ridge better |
| F1 vs F0 (xgboost) | 0.63 | 0.5255 | 1.0000 | no significant difference |
| F2 vs F0 (xgboost) | 0.24 | 0.8139 | 1.0000 | no significant difference |
| F2 vs F1 (xgboost) | -0.28 | 0.7819 | 1.0000 | no significant difference |
| xgboost vs ridge (F0) | -1.17 | 0.2419 | 1.0000 | no significant difference |
| xgboost vs ridge (F1) | -0.79 | 0.4274 | 1.0000 | no significant difference |
| xgboost vs ridge (F2) | -2.13 | 0.0334 | 0.2338 | no significant difference |

## Decision

Best cell on the primary metric: **F2-ridge**. Live-test candidate: **none** (no cell passes the primary outcome).

Information only, not investment advice.
