# Track C, version 2: Bitcoin intraday

Pre-registered in OUTCOMES.md (Version 2). Out of sample 2023-01-01 to 2026-11-27 (34244 hours), the same for every cell. Ridge = simple family, XGBoost = complex family; F0 = version 1 inputs, F1 = F0 + a few, F2 = F0 + all free inputs.

- F1 adds 5: premium_1h, premium_chg_4h, funding_last, cb_premium, cb_premium_chg_4h
- F2 adds 23 more: oi_chg_1h, oi_chg_4h, oi_chg_24h, top_ls_pos, ls_acct, taker_ls, fut_flow_1h, fut_flow_4h, fut_spot_24h, dvol_level, dvol_chg_1h, dvol_chg_24h, eth_premium_1h, trade_size_z, fomc_soon, fomc_after, cpi_soon, cpi_after, etf_flow_1d, large_imb_1h, large_imb_4h, large_share_4h, xl_imb_4h

## Next-4-hour return (primary, C1) and the long/flat strategy (C2)

C1 passes when R²oos > 0 with DM p < 0.05 and hit rate > 51%. C2 needs a net Sharpe above buy-and-hold and positive net return in at least 3 of the 4 years.

| Cell | Inputs | R²oos | DM p | Hit rate | C1 | Strategy Sharpe | Positive years | Time invested | C2 |
|---|---|---|---|---|---|---|---|---|---|
| F0-ridge | 35 | **+0.018%** | 0.426 | 50.7% | fail | – | 0/4 | 0% | fail |
| F0-xgboost | 35 | **-0.131%** | 0.295 | 49.7% | fail | 0.85 | 2/4 | 0% | fail |
| F1-ridge | 40 | **+0.022%** | 0.564 | 50.3% | fail | – | 0/4 | 0% | fail |
| F1-xgboost | 40 | **-0.121%** | 0.392 | 49.8% | fail | 0.82 | 1/4 | 1% | fail |
| F2-ridge | 63 | **+0.188%** | 0.002 | 51.0% | fail | – | 0/4 | 0% | fail |
| F2-xgboost | 63 | **-0.196%** | 0.181 | 49.6% | fail | 0.92 | 2/4 | 1% | fail |

Buy and hold over the window: Sharpe 0.94, max drawdown -55%.

## Pre-registered comparisons

Diebold-Mariano on the primary loss, Holm-corrected over the nine tests. A positive statistic favours the challenger.

| Comparison | DM statistic | p | Holm p | Result |
|---|---|---|---|---|
| F1 vs F0 (ridge) | 0.22 | 0.8285 | 1.0000 | no significant difference |
| F2 vs F0 (ridge) | 3.00 | 0.0027 | 0.0213 | F2-ridge better |
| F2 vs F1 (ridge) | 3.10 | 0.0019 | 0.0173 | F2-ridge better |
| F1 vs F0 (xgboost) | 0.15 | 0.8777 | 1.0000 | no significant difference |
| F2 vs F0 (xgboost) | -0.75 | 0.4506 | 1.0000 | no significant difference |
| F2 vs F1 (xgboost) | -0.99 | 0.3206 | 1.0000 | no significant difference |
| xgboost vs ridge (F0) | -1.20 | 0.2310 | 1.0000 | no significant difference |
| xgboost vs ridge (F1) | -1.01 | 0.3104 | 1.0000 | no significant difference |
| xgboost vs ridge (F2) | -2.78 | 0.0055 | 0.0384 | F2-ridge better |

## Decision

Best cell on the primary metric: **F2-ridge**. Live-test candidate: **none** (no cell passes the primary outcome).

Information only, not investment advice.
