# Bitcoin model comparison: train, validate, test

Run: 2026-10-17 07:43 UTC · data collected 2026-10-17T07:14:09+00:00 · 45 of 48 series loaded · price base `btc` · runtime 21.6 min

**How to read this.** R²oos compares each model with the random-walk forecast (tomorrow's price = today's). 0 means no better than the random walk, negative means worse. The Diebold-Mariano p-value (DM p) tests whether a model beats the random walk by more than chance. A model should also beat the constant-drift forecast (the average past return, row `mean`). The overfit gap is in-sample R²oos minus test R²oos.

## Split

| Block | Period | Used for |
|---|---|---|
| Train | 2018-03-01 to 2022-12-31 | fitting |
| Validation | 2023-01-01 to 2023-12-31 | choosing hyperparameters and early stopping |
| Test | 2024-01-01 to latest | scored once, after refitting on train + validation |

![Test R² by model and target](test_r2_by_model.png)

![30-day return: running advantage over the random walk](r30_cumulative_advantage.png)

## Next 1 day return (`r1`, 1 d)

Rows: train 1766, validation 365, test 1018 (2024-01-01 to 2026-10-14) · 181 features

| Model | Train R²oos | Val R²oos | Test R²oos | Test direction hit | Test DM p | Overfit gap | Half-years beating RW |
|---|---|---|---|---|---|---|---|
| zero | +0.00% | +0.00% | **+0.00%** | – | – | +0.00% | 0/6 |
| mean | +0.00% | +0.23% | **+0.06%** | 0.503 | 0.697 | -0.03% | 4/6 |
| ridge | +0.48% | -0.27% | **+0.06%** | 0.504 | 0.803 | +0.42% | 4/6 |
| poly2 | +0.01% | +0.22% | **+0.06%** | 0.503 | 0.691 | -0.03% | 4/6 |
| xgboost | +0.22% | +0.36% | **+0.11%** | 0.503 | 0.490 | +0.11% | 4/6 |
| ridge_fixed | +16.88% | -76.45% | **-166.27%** | 0.521 | 0.000 | +180.55% | 0/6 |
| poly2_fixed | +20.33% | -89.51% | **-27.28%** | 0.496 | 0.000 | +45.44% | 0/6 |
| xgb_fixed | +47.38% | -18.74% | **-2.02%** | 0.489 | 0.326 | +43.28% | 1/6 |
| gru | +2.45% | -2.30% | **-2.18%** | 0.502 | 0.082 | +5.97% | 0/6 |
| gru_fixed | +34.86% | -70.55% | **-48.72%** | 0.530 | 0.000 | +86.24% | 0/6 |

Ranking on test with overfitting flags:

- **xgboost**: test R²oos +0.11%, DM p vs random walk 0.490, vs drift 0.286 · no risk flags
- **poly2**: test R²oos +0.06%, DM p vs random walk 0.691, vs drift 0.253 · no risk flags
- **ridge**: test R²oos +0.06%, DM p vs random walk 0.803, vs drift 0.968 · risk: no better than the constant-drift forecast
- **gru**: test R²oos -2.18%, DM p vs random walk 0.082, vs drift 0.056 · risk: large in-sample vs test gap, loses to random walk in most half-years, no better than the constant-drift forecast

**Verdict:** no model beats both the random walk and the constant drift significantly without an overfitting flag.

Overfitting probes (fixed settings, no validation brake): ridge_fixed in-sample +14.3% → test -166.3%; poly2_fixed in-sample +18.2% → test -27.3%; xgb_fixed in-sample +41.3% → test -2.0%; gru_fixed in-sample +37.5% → test -48.7%

GRU test R²oos by seed: -3.67%, -1.45%, -3.05%, -2.72%, -2.32%

## Next 7 day return (`r7`, 7 d)

Rows: train 1760, validation 365, test 1012 (2024-01-01 to 2026-10-08) · 181 features

| Model | Train R²oos | Val R²oos | Test R²oos | Test direction hit | Test DM p | Overfit gap | Half-years beating RW |
|---|---|---|---|---|---|---|---|
| zero | +0.00% | +0.00% | **+0.00%** | – | – | +0.00% | 0/6 |
| mean | +0.03% | +1.24% | **+0.47%** | 0.528 | 0.634 | -0.26% | 4/6 |
| ridge | +2.34% | -1.22% | **+0.46%** | 0.524 | 0.720 | +1.83% | 4/6 |
| poly2 | +0.31% | +1.22% | **+0.44%** | 0.528 | 0.653 | +0.05% | 4/6 |
| xgboost | +0.35% | +1.15% | **+0.49%** | 0.528 | 0.625 | -0.00% | 4/6 |
| ridge_fixed | +55.21% | -93.33% | **-503.07%** | 0.510 | 0.000 | +552.87% | 0/6 |
| poly2_fixed | +46.53% | -79.76% | **-81.81%** | 0.432 | 0.000 | +124.17% | 0/6 |
| xgb_fixed | +80.42% | -97.80% | **-21.50%** | 0.502 | 0.000 | +97.09% | 1/6 |
| gru | +10.11% | -1.63% | **-27.23%** | 0.517 | 0.000 | +50.85% | 0/6 |
| gru_fixed | +91.27% | -176.46% | **-163.88%** | 0.496 | 0.000 | +254.94% | 0/6 |

Ranking on test with overfitting flags:

- **xgboost**: test R²oos +0.49%, DM p vs random walk 0.625, vs drift 0.821 · no risk flags
- **ridge**: test R²oos +0.46%, DM p vs random walk 0.720, vs drift 0.987 · risk: no better than the constant-drift forecast
- **poly2**: test R²oos +0.44%, DM p vs random walk 0.653, vs drift 0.200 · risk: no better than the constant-drift forecast
- **gru**: test R²oos -27.23%, DM p vs random walk 0.000, vs drift 0.000 · risk: large in-sample vs test gap, validation result did not hold on test, loses to random walk in most half-years, unstable across seeds, no better than the constant-drift forecast

**Verdict:** no model beats both the random walk and the constant drift significantly without an overfitting flag.

Overfitting probes (fixed settings, no validation brake): ridge_fixed in-sample +49.8% → test -503.1%; poly2_fixed in-sample +42.4% → test -81.8%; xgb_fixed in-sample +75.6% → test -21.5%; gru_fixed in-sample +91.1% → test -163.9%

GRU test R²oos by seed: -30.33%, -26.42%, -34.25%, -23.39%, -30.42%

## Next 30 day return (`r30`, 30 d)

Rows: train 1737, validation 365, test 989 (2024-01-01 to 2026-09-15) · 181 features

| Model | Train R²oos | Val R²oos | Test R²oos | Test direction hit | Test DM p | Overfit gap | Half-years beating RW |
|---|---|---|---|---|---|---|---|
| zero | +0.00% | +0.00% | **+0.00%** | – | – | +0.00% | 0/6 |
| mean | +0.24% | +6.66% | **+2.04%** | 0.563 | 0.661 | -0.93% | 4/6 |
| ridge | +7.17% | -3.02% | **+0.72%** | 0.563 | 0.895 | +6.31% | 4/6 |
| poly2 | +22.30% | +7.06% | **-3.17%** | 0.544 | 0.578 | +25.89% | 4/6 |
| xgboost | +2.44% | +7.29% | **+1.59%** | 0.563 | 0.749 | +1.38% | 4/6 |
| ridge_fixed | +85.87% | -1374.30% | **-612.84%** | 0.506 | 0.000 | +693.88% | 0/6 |
| poly2_fixed | +69.22% | -149.84% | **-72.05%** | 0.442 | 0.000 | +134.36% | 0/6 |
| xgb_fixed | +95.48% | -139.87% | **-42.72%** | 0.585 | 0.033 | +136.97% | 2/6 |
| gru | +29.75% | -4.57% | **-75.97%** | 0.543 | 0.007 | +151.47% | 0/6 |
| gru_fixed | +97.50% | -93.91% | **-124.94%** | 0.532 | 0.000 | +222.40% | 0/6 |

Ranking on test with overfitting flags:

- **xgboost**: test R²oos +1.59%, DM p vs random walk 0.749, vs drift 0.208 · risk: validation result did not hold on test, no better than the constant-drift forecast
- **ridge**: test R²oos +0.72%, DM p vs random walk 0.895, vs drift 0.278 · risk: large in-sample vs test gap, no better than the constant-drift forecast
- **poly2**: test R²oos -3.17%, DM p vs random walk 0.578, vs drift 0.016 · risk: large in-sample vs test gap, validation result did not hold on test, no better than the constant-drift forecast
- **gru**: test R²oos -75.97%, DM p vs random walk 0.007, vs drift 0.004 · risk: large in-sample vs test gap, validation result did not hold on test, loses to random walk in most half-years, unstable across seeds, no better than the constant-drift forecast

**Verdict:** no model beats both the random walk and the constant drift significantly without an overfitting flag.

Overfitting probes (fixed settings, no validation brake): ridge_fixed in-sample +81.0% → test -612.8%; poly2_fixed in-sample +62.3% → test -72.0%; xgb_fixed in-sample +94.3% → test -42.7%; gru_fixed in-sample +97.5% → test -124.9%

GRU test R²oos by seed: -89.71%, -84.38%, -84.50%, -101.82%, -75.00%

## Mean price over next 30 days (drives 50/100/200-day MA forecasts) (`m30`, 30 d)

Rows: train 1737, validation 365, test 989 (2024-01-01 to 2026-09-15) · 181 features

| Model | Train R²oos | Val R²oos | Test R²oos | Test direction hit | Test DM p | Overfit gap | Half-years beating RW |
|---|---|---|---|---|---|---|---|
| zero | +0.00% | +0.00% | **+0.00%** | – | – | +0.00% | 0/6 |
| mean | +0.47% | +8.10% | **+1.88%** | 0.549 | 0.693 | -0.53% | 4/6 |
| ridge | +6.06% | +1.66% | **+0.88%** | 0.549 | 0.870 | +5.34% | 4/6 |
| poly2 | +0.85% | +8.06% | **+1.85%** | 0.549 | 0.697 | -0.10% | 4/6 |
| xgboost | +4.26% | +10.58% | **+2.20%** | 0.549 | 0.681 | +2.82% | 4/6 |
| ridge_fixed | +85.17% | -807.72% | **-331.49%** | 0.540 | 0.000 | +411.89% | 0/6 |
| poly2_fixed | +66.70% | -77.31% | **-83.79%** | 0.428 | 0.000 | +144.18% | 0/6 |
| xgb_fixed | +95.19% | -147.81% | **-57.30%** | 0.555 | 0.019 | +150.80% | 2/6 |
| gru | +25.83% | +0.30% | **-75.25%** | 0.530 | 0.002 | +141.59% | 0/6 |
| gru_fixed | +98.78% | -188.44% | **-188.53%** | 0.490 | 0.000 | +287.34% | 0/6 |

Ranking on test with overfitting flags:

- **xgboost**: test R²oos +2.20%, DM p vs random walk 0.681, vs drift 0.708 · risk: validation result did not hold on test
- **poly2**: test R²oos +1.85%, DM p vs random walk 0.697, vs drift 0.324 · risk: validation result did not hold on test, no better than the constant-drift forecast
- **ridge**: test R²oos +0.88%, DM p vs random walk 0.870, vs drift 0.377 · risk: large in-sample vs test gap, no better than the constant-drift forecast
- **gru**: test R²oos -75.25%, DM p vs random walk 0.002, vs drift 0.001 · risk: large in-sample vs test gap, validation result did not hold on test, loses to random walk in most half-years, unstable across seeds, no better than the constant-drift forecast

**Verdict:** no model beats both the random walk and the constant drift significantly without an overfitting flag.

Overfitting probes (fixed settings, no validation brake): ridge_fixed in-sample +80.4% → test -331.5%; poly2_fixed in-sample +60.4% → test -83.8%; xgb_fixed in-sample +93.5% → test -57.3%; gru_fixed in-sample +98.8% → test -188.5%

GRU test R²oos by seed: -79.52%, -83.65%, -99.18%, -95.31%, -64.03%

## Walk-forward check (refit every 91 days, 2020 onwards)

Each quarter the models are re-tuned on the trailing year and refit on all earlier data, then forecast the next quarter. This tests the same models over about 25 different periods instead of one.

**Next 1 day return** · 25 folds, 2020-09-30 to 2026-10-14

| Model | R²oos | DM p vs random walk | DM p vs drift | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 | 2026 |
|---|---|---|---|---|---|---|---|---|---|---|
| zero | **+0.00%** | – | – | +0.0% | +0.0% | +0.0% | +0.0% | +0.0% | +0.0% | +0.0% |
| mean | **-0.08%** | 0.517 | – | +0.0% | -0.0% | -0.5% | +0.3% | +0.3% | -0.2% | -0.2% |
| ridge | **-1.15%** | 0.039 | 0.050 | +1.0% | -2.0% | -1.8% | -1.4% | +0.3% | -0.6% | -0.3% |
| poly2 | **-1.10%** | 0.095 | 0.106 | -0.3% | +0.7% | -2.4% | -6.5% | -0.5% | -0.4% | -0.8% |
| xgboost | **-1.34%** | 0.073 | 0.083 | +3.2% | -0.7% | -4.5% | -0.6% | -0.6% | -1.4% | -0.5% |

**Next 7 day return** · 25 folds, 2020-09-30 to 2026-10-08

| Model | R²oos | DM p vs random walk | DM p vs drift | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 | 2026 |
|---|---|---|---|---|---|---|---|---|---|---|
| zero | **+0.00%** | – | – | +0.0% | +0.0% | +0.0% | +0.0% | +0.0% | +0.0% | +0.0% |
| mean | **-0.60%** | 0.390 | – | +0.2% | -0.7% | -3.1% | +1.6% | +2.2% | -2.1% | -1.4% |
| ridge | **-2.91%** | 0.064 | 0.142 | +2.0% | -4.9% | -2.7% | -8.6% | +2.7% | -3.6% | -2.2% |
| poly2 | **-4.90%** | 0.032 | 0.053 | +8.3% | +0.0% | -10.0% | -20.3% | -5.9% | -2.0% | -2.6% |
| xgboost | **-7.01%** | 0.030 | 0.040 | +1.9% | -2.0% | -11.5% | -32.0% | +2.5% | -8.4% | -1.8% |

**Next 30 day return** · 24 folds, 2020-09-30 to 2026-09-15

| Model | R²oos | DM p vs random walk | DM p vs drift | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 | 2026 |
|---|---|---|---|---|---|---|---|---|---|---|
| zero | **+0.00%** | – | – | +0.0% | +0.0% | +0.0% | +0.0% | +0.0% | +0.0% | +0.0% |
| mean | **-2.16%** | 0.479 | – | +2.7% | -5.2% | -13.7% | +7.8% | +9.6% | -12.2% | -5.2% |
| ridge | **-16.62%** | 0.023 | 0.039 | +3.7% | -19.1% | -13.0% | -98.2% | +10.5% | -25.9% | -6.2% |
| poly2 | **-18.11%** | 0.014 | 0.017 | +2.8% | -7.6% | -76.4% | -27.7% | +6.3% | -13.2% | -16.6% |
| xgboost | **-20.17%** | 0.013 | 0.007 | +0.0% | -58.1% | -8.4% | -10.7% | +8.3% | -52.0% | -5.4% |

**Mean price over next 30 days (drives 50/100/200-day MA forecasts)** · 24 folds, 2020-09-30 to 2026-09-15

| Model | R²oos | DM p vs random walk | DM p vs drift | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 | 2026 |
|---|---|---|---|---|---|---|---|---|---|---|
| zero | **+0.00%** | – | – | +0.0% | +0.0% | +0.0% | +0.0% | +0.0% | +0.0% | +0.0% |
| mean | **-1.18%** | 0.681 | – | +4.6% | -3.4% | -14.1% | +8.7% | +8.8% | -10.5% | -5.1% |
| ridge | **-8.14%** | 0.105 | 0.094 | +6.0% | -18.7% | -2.5% | -31.0% | +9.2% | -22.0% | -5.6% |
| poly2 | **-14.79%** | 0.018 | 0.010 | +5.2% | -20.3% | -42.0% | -23.6% | +3.7% | -10.8% | -10.1% |
| xgboost | **-23.93%** | 0.015 | 0.010 | -0.3% | -49.5% | -10.2% | -61.9% | +9.0% | -52.1% | -5.1% |

## 50/100/200-day moving averages, 30 days ahead

Forecast = known part of the average + 30 predicted days (from the `m30` model). The naive forecast fills the 30 unknown days with today's price.

| Model | MA50 error | MA100 error | MA200 error | MA50 vs naive | MA100 vs naive | MA200 vs naive |
|---|---|---|---|---|---|---|
| gru | 5.05% | 2.59% | 1.36% | 1.375× | 1.372× | 1.379× |
| gru_fixed | 6.53% | 3.36% | 1.76% | 1.777× | 1.780× | 1.793× |
| mean | 3.70% | 1.89% | 0.99% | 1.007× | 1.003× | 1.004× |
| poly2 | 3.70% | 1.89% | 0.99% | 1.007× | 1.004× | 1.005× |
| poly2_fixed | 5.22% | 2.66% | 1.38% | 1.422× | 1.410× | 1.407× |
| ridge | 3.75% | 1.91% | 1.00% | 1.019× | 1.015× | 1.017× |
| ridge_fixed | 8.09% | 4.11% | 2.13% | 2.200× | 2.181× | 2.163× |
| xgb_fixed | 5.21% | 2.63% | 1.38% | 1.418× | 1.396× | 1.399× |
| xgboost | 3.71% | 1.90% | 0.99% | 1.010× | 1.006× | 1.007× |
| zero | 3.68% | 1.89% | 0.98% | 1.000× | 1.000× | 1.000× |

The naive forecast alone already explains MA50 96.2%, MA100 99.1%, MA200 99.8% of the variation in moving-average levels on test, so high R² on moving averages says nothing about skill.

## XGBoost: most used features (gain, final refit)

- `r1`: cm_exchange_supply_chg_7, epu_us_chg_30, curve_10y2y_z365, cm_exchange_inflow_chg_30, btc_ma_gap_20, epu_us_lvl
- `r7`: btc_ma_gap_100, btc_mom_180, btc_ma_gap_200
- `r30`: ust10y_yahoo_lvl, fed_funds_lvl, move_z365, btc_ma_gap_100, stablecoin_supply_chg_30, ust2y_z365
- `m30`: curve_10y2y_z365, fin_conditions_z365, ust10y_yahoo_lvl, fed_funds_lvl, fed_funds_z365, fed_balance_sheet_chg_90, cm_exchange_supply_chg_90, cm_issuance_z365, gold_gap_200, treasury_account_z365, vix_z365, cm_mvrv_lvl

## Data sources

| Series | Source | Kind | Lag (days) | From | To | Status |
|---|---|---|---|---|---|---|
| breakeven5y | FRED (St. Louis Fed) | level | 1 | 2010-01-04 | 2026-10-16 | ok |
| btc | Yahoo Finance | price | 0 | 2014-09-17 | 2026-10-17 | ok |
| btc_volume | Yahoo Finance | count | 0 | 2014-09-17 | 2026-10-17 | ok |
| cm_active_addresses | Coin Metrics community API | count | 1 | 2013-01-01 | 2026-10-16 | ok |
| cm_exchange_inflow | Coin Metrics community API | count | 1 | 2013-01-01 | 2026-10-16 | ok |
| cm_exchange_outflow | Coin Metrics community API | count | 1 | 2013-01-01 | 2026-10-16 | ok |
| cm_exchange_supply | Coin Metrics community API | count | 1 | 2013-01-01 | 2026-10-16 | ok |
| cm_hashrate | Coin Metrics community API | count | 1 | 2013-01-01 | 2026-10-16 | ok |
| cm_issuance | Coin Metrics community API | count | 1 | 2013-01-01 | 2026-10-16 | ok |
| cm_mvrv | Coin Metrics community API | level | 1 | 2013-01-01 | 2026-10-16 | ok |
| cm_price | Coin Metrics community API | price | 1 | 2013-01-01 | 2026-10-16 | ok |
| cm_tx_count | Coin Metrics community API | count | 1 | 2013-01-01 | 2026-10-16 | ok |
| coin | Yahoo Finance | price | 0 | 2021-04-14 | 2026-10-16 | ok |
| curve_10y2y | FRED (St. Louis Fed) | level | 1 | 2010-01-04 | 2026-10-16 | ok |
| dxy | Yahoo Finance | price | 0 | 2013-01-02 | 2026-10-16 | ok |
| emu_us | FRED (St. Louis Fed) | level | 1 | 2010-01-01 | 2026-10-15 | ok |
| epu_us | FRED (St. Louis Fed) | level | 1 | 2010-01-01 | 2026-10-15 | ok |
| eth | Yahoo Finance | price | 0 | 2017-11-09 | 2026-10-17 | ok |
| fear_greed | alternative.me | level | 0 | 2018-02-01 | 2026-10-17 | ok |
| fed_balance_sheet | FRED (St. Louis Fed) | count | 2 | 2010-01-06 | 2026-10-14 | ok |
| fed_funds | FRED (St. Louis Fed) | level | 1 | 2010-01-01 | 2026-10-15 | ok |
| fin_conditions | FRED (St. Louis Fed) | level | 7 | 2010-01-01 | 2026-10-09 | ok |
| funding_rate | Binance or BitMEX | | | | | failed: RuntimeError: binance: Binance HTTP 451; bitmex: BitMEX HTTP 403 |
| gold | Yahoo Finance | price | 0 | 2013-01-02 | 2026-10-16 | ok |
| gpr | Caldara & Iacoviello GPR | level | 1 | 2010-01-01 | 2026-10-13 | ok |
| gpr_acts | Caldara & Iacoviello GPR | level | 1 | 2010-01-01 | 2026-10-13 | ok |
| gpr_threats | Caldara & Iacoviello GPR | level | 1 | 2010-01-01 | 2026-10-13 | ok |
| hy_spread | FRED (St. Louis Fed) | level | 1 | 2023-10-17 | 2026-10-15 | ok |
| m2 | FRED (St. Louis Fed) | count | 60 | 2010-01-01 | 2026-08-01 | ok |
| move | Yahoo Finance | level | 0 | 2013-01-02 | 2026-10-16 | ok |
| mstr | Yahoo Finance | price | 0 | 2013-01-02 | 2026-10-16 | ok |
| nasdaq | Yahoo Finance | price | 0 | 2013-01-02 | 2026-10-16 | ok |
| news_tone_bitcoin | GDELT 2.0 DOC API | level | 1 | 2017-01-01 | 2026-10-17 | ok |
| news_tone_conflict | GDELT | | | | | failed: RuntimeError: GDELT rate limit persisted |
| news_tone_macro | GDELT 2.0 DOC API | level | 1 | 2017-01-01 | 2026-10-17 | ok |
| news_volume_bitcoin | GDELT | | | | | failed: RuntimeError: GDELT rate limit persisted |
| oil | Yahoo Finance | price | 0 | 2013-01-02 | 2026-10-16 | ok |
| reverse_repo | FRED (St. Louis Fed) | count | 1 | 2010-08-12 | 2026-10-16 | ok |
| sp500 | Yahoo Finance | price | 0 | 2013-01-02 | 2026-10-16 | ok |
| stablecoin_supply | DefiLlama | count | 1 | 2017-11-29 | 2026-10-17 | ok |
| treasury_account | FRED (St. Louis Fed) | count | 2 | 2010-01-06 | 2026-10-14 | ok |
| usd_broad | FRED (St. Louis Fed) | price | 1 | 2010-01-04 | 2026-10-09 | ok |
| ust10y | FRED (St. Louis Fed) | level | 1 | 2010-01-04 | 2026-10-15 | ok |
| ust10y_yahoo | Yahoo Finance | level | 0 | 2013-01-02 | 2026-10-16 | ok |
| ust2y | FRED (St. Louis Fed) | level | 1 | 2010-01-04 | 2026-10-15 | ok |
| vix | Yahoo Finance | level | 0 | 2013-01-02 | 2026-10-16 | ok |
| wiki_bitcoin | Wikimedia pageviews | count | 1 | 2015-07-01 | 2026-10-15 | ok |
| wiki_crypto | Wikimedia pageviews | count | 1 | 2015-07-01 | 2026-10-15 | ok |

Lag is the number of days a value is held back before the model may use it, so that only data that was public at the time enters each prediction.
