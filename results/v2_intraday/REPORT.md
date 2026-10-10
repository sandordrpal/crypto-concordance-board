# Track C, version 2: Bitcoin intraday

Pre-registered in OUTCOMES.md (Version 2). Out of sample 2023-01-01 to 2026-10-09 (33068 hours), the same for every cell. Ridge = simple family, XGBoost = complex family; F0 = version 1 inputs, F1 = F0 + a few, F2 = F0 + all free inputs.

- F1 adds 5: premium_1h, premium_chg_4h, funding_last, cb_premium, cb_premium_chg_4h
- F2 adds 22 more: oi_chg_1h, oi_chg_4h, oi_chg_24h, top_ls_pos, ls_acct, taker_ls, fut_flow_1h, fut_flow_4h, fut_spot_24h, dvol_level, dvol_chg_1h, dvol_chg_24h, eth_premium_1h, trade_size_z, fomc_soon, fomc_after, cpi_soon, cpi_after, large_imb_1h, large_imb_4h, large_share_4h, xl_imb_4h

## Next-4-hour return (primary, C1) and the long/flat strategy (C2)

C1 passes when R²oos > 0 with DM p < 0.05 and hit rate > 51%. C2 needs a net Sharpe above buy-and-hold and positive net return in at least 3 of the 4 years.

| Cell | Inputs | R²oos | DM p | Hit rate | C1 | Strategy Sharpe | Positive years | Time invested | C2 |
|---|---|---|---|---|---|---|---|---|---|
| F0-ridge | 36 | **+0.025%** | 0.255 | 50.9% | fail | – | 0/4 | 0% | fail |
| F0-xgboost | 36 | **-0.196%** | 0.159 | 49.8% | fail | 1.16 | 2/4 | 1% | fail |
| F1-ridge | 41 | **+0.030%** | 0.435 | 50.4% | fail | – | 0/4 | 0% | fail |
| F1-xgboost | 41 | **-0.200%** | 0.259 | 49.8% | fail | 1.00 | 2/4 | 1% | fail |
| F2-ridge | 63 | **+0.164%** | 0.008 | 50.8% | fail | – | 0/4 | 0% | fail |
| F2-xgboost | 63 | **-0.121%** | 0.372 | 50.1% | fail | 1.31 | 2/4 | 1% | fail |

Buy and hold over the window: Sharpe 1.15, max drawdown -53%.

## Pre-registered comparisons

Diebold-Mariano on the primary loss, Holm-corrected over the nine tests. A positive statistic favours the challenger.

| Comparison | DM statistic | p | Holm p | Result |
|---|---|---|---|---|
| F1 vs F0 (ridge) | 0.24 | 0.8130 | 1.0000 | no significant difference |
| F2 vs F0 (ridge) | 2.49 | 0.0129 | 0.1036 | no significant difference |
| F2 vs F1 (ridge) | 2.58 | 0.0099 | 0.0887 | no significant difference |
| F1 vs F0 (xgboost) | -0.05 | 0.9578 | 1.0000 | no significant difference |
| F2 vs F0 (xgboost) | 1.00 | 0.3182 | 1.0000 | no significant difference |
| F2 vs F1 (xgboost) | 0.86 | 0.3892 | 1.0000 | no significant difference |
| xgboost vs ridge (F0) | -1.59 | 0.1113 | 0.6675 | no significant difference |
| xgboost vs ridge (F1) | -1.30 | 0.1939 | 0.9693 | no significant difference |
| xgboost vs ridge (F2) | -2.16 | 0.0306 | 0.2142 | no significant difference |

## Decision

Best cell on the primary metric: **F2-ridge**. Live-test candidate: **none** (no cell passes the primary outcome).

Information only, not investment advice.
