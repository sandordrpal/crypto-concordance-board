# Bitcoin model comparison: train, validate, test

Run: 2026-10-31 09:10 UTC · data collected 2026-10-31T08:38:56+00:00 · 47 of 48 series loaded · price base `btc` · runtime 22.8 min

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

Rows: train 1766, validation 365, test 1033 (2024-01-01 to 2026-10-29) · 189 features

| Model | Train R²oos | Val R²oos | Test R²oos | Test direction hit | Test DM p | Overfit gap | Half-years beating RW |
|---|---|---|---|---|---|---|---|
| zero | +0.00% | +0.00% | **+0.00%** | – | – | +0.00% | 0/6 |
| mean | +0.00% | +0.23% | **+0.05%** | 0.500 | 0.763 | -0.02% | 4/6 |
| ridge | +0.49% | -0.25% | **+0.05%** | 0.503 | 0.841 | +0.45% | 4/6 |
| poly2 | +4.85% | +0.69% | **+0.21%** | 0.488 | 0.747 | +4.56% | 3/6 |
| xgboost | +1.98% | +0.33% | **+0.16%** | 0.494 | 0.484 | +1.83% | 4/6 |
| ridge_fixed | +17.51% | -75.98% | **-131.51%** | 0.527 | 0.000 | +146.60% | 0/6 |
| poly2_fixed | +19.70% | -80.18% | **-29.72%** | 0.489 | 0.000 | +47.59% | 0/6 |
| xgb_fixed | +46.73% | -16.94% | **-2.69%** | 0.500 | 0.181 | +44.66% | 1/6 |
| gru | +2.44% | -1.45% | **-1.70%** | 0.508 | 0.104 | +5.31% | 0/6 |
| gru_fixed | +33.54% | -66.25% | **-47.37%** | 0.521 | 0.000 | +82.78% | 0/6 |

Ranking on test with overfitting flags:

- **poly2**: test R²oos +0.21%, DM p vs random walk 0.747, vs drift 0.794 · no risk flags
- **xgboost**: test R²oos +0.16%, DM p vs random walk 0.484, vs drift 0.401 · no risk flags
- **ridge**: test R²oos +0.05%, DM p vs random walk 0.841, vs drift 0.989 · risk: no better than the constant-drift forecast
- **gru**: test R²oos -1.70%, DM p vs random walk 0.104, vs drift 0.074 · risk: large in-sample vs test gap, loses to random walk in most half-years, no better than the constant-drift forecast

**Verdict:** no model beats both the random walk and the constant drift significantly without an overfitting flag.

Overfitting probes (fixed settings, no validation brake): ridge_fixed in-sample +15.1% → test -131.5%; poly2_fixed in-sample +17.9% → test -29.7%; xgb_fixed in-sample +42.0% → test -2.7%; gru_fixed in-sample +35.4% → test -47.4%

GRU test R²oos by seed: -2.57%, -1.95%, -1.41%, -2.64%, -1.92%

## Next 7 day return (`r7`, 7 d)

Rows: train 1760, validation 365, test 1027 (2024-01-01 to 2026-10-23) · 189 features

| Model | Train R²oos | Val R²oos | Test R²oos | Test direction hit | Test DM p | Overfit gap | Half-years beating RW |
|---|---|---|---|---|---|---|---|
| zero | +0.00% | +0.00% | **+0.00%** | – | – | +0.00% | 0/6 |
| mean | +0.03% | +1.24% | **+0.41%** | 0.522 | 0.679 | -0.20% | 4/6 |
| ridge | +2.39% | -1.03% | **+0.42%** | 0.520 | 0.742 | +1.95% | 4/6 |
| poly2 | +0.31% | +1.23% | **+0.38%** | 0.522 | 0.697 | +0.12% | 4/6 |
| xgboost | +0.80% | +1.57% | **+0.53%** | 0.522 | 0.606 | +0.32% | 4/6 |
| ridge_fixed | +56.67% | -120.88% | **-503.34%** | 0.518 | 0.000 | +554.55% | 0/6 |
| poly2_fixed | +47.58% | -53.22% | **-95.52%** | 0.433 | 0.000 | +138.50% | 0/6 |
| xgb_fixed | +81.20% | -95.84% | **-19.71%** | 0.506 | 0.000 | +95.87% | 1/6 |
| gru | +10.30% | +2.18% | **-21.63%** | 0.501 | 0.000 | +45.01% | 0/6 |
| gru_fixed | +90.97% | -266.44% | **-145.74%** | 0.471 | 0.000 | +236.95% | 0/6 |

Ranking on test with overfitting flags:

- **xgboost**: test R²oos +0.53%, DM p vs random walk 0.606, vs drift 0.301 · no risk flags
- **ridge**: test R²oos +0.42%, DM p vs random walk 0.742, vs drift 0.975 · no risk flags
- **poly2**: test R²oos +0.38%, DM p vs random walk 0.697, vs drift 0.233 · risk: no better than the constant-drift forecast
- **gru**: test R²oos -21.63%, DM p vs random walk 0.000, vs drift 0.000 · risk: large in-sample vs test gap, validation result did not hold on test, loses to random walk in most half-years, unstable across seeds, no better than the constant-drift forecast

**Verdict:** no model beats both the random walk and the constant drift significantly without an overfitting flag.

Overfitting probes (fixed settings, no validation brake): ridge_fixed in-sample +51.2% → test -503.3%; poly2_fixed in-sample +43.0% → test -95.5%; xgb_fixed in-sample +76.2% → test -19.7%; gru_fixed in-sample +91.2% → test -145.7%

GRU test R²oos by seed: -23.67%, -24.96%, -19.48%, -25.17%, -21.80%

## Next 30 day return (`r30`, 30 d)

Rows: train 1737, validation 365, test 1004 (2024-01-01 to 2026-09-30) · 189 features

| Model | Train R²oos | Val R²oos | Test R²oos | Test direction hit | Test DM p | Overfit gap | Half-years beating RW |
|---|---|---|---|---|---|---|---|
| zero | +0.00% | +0.00% | **+0.00%** | – | – | +0.00% | 0/6 |
| mean | +0.24% | +6.66% | **+1.93%** | 0.560 | 0.678 | -0.81% | 4/6 |
| ridge | +7.37% | -2.63% | **+0.91%** | 0.560 | 0.867 | +6.32% | 4/6 |
| poly2 | +0.68% | +6.61% | **+1.91%** | 0.560 | 0.682 | -0.34% | 4/6 |
| xgboost | +17.20% | +9.85% | **-0.50%** | 0.558 | 0.914 | +17.70% | 3/6 |
| ridge_fixed | +86.10% | -1416.20% | **-516.26%** | 0.506 | 0.000 | +597.71% | 0/6 |
| poly2_fixed | +69.33% | -148.77% | **-75.64%** | 0.425 | 0.000 | +138.88% | 0/6 |
| xgb_fixed | +95.58% | -72.85% | **-36.36%** | 0.582 | 0.039 | +130.55% | 1/6 |
| gru | +23.17% | +9.77% | **-69.63%** | 0.604 | 0.015 | +147.32% | 0/6 |
| gru_fixed | +97.51% | -95.04% | **-109.44%** | 0.585 | 0.001 | +206.78% | 0/6 |

Ranking on test with overfitting flags:

- **poly2**: test R²oos +1.91%, DM p vs random walk 0.682, vs drift 0.657 · risk: no better than the constant-drift forecast
- **ridge**: test R²oos +0.91%, DM p vs random walk 0.867, vs drift 0.424 · risk: large in-sample vs test gap, no better than the constant-drift forecast
- **xgboost**: test R²oos -0.50%, DM p vs random walk 0.914, vs drift 0.065 · risk: large in-sample vs test gap, validation result did not hold on test, no better than the constant-drift forecast
- **gru**: test R²oos -69.63%, DM p vs random walk 0.015, vs drift 0.013 · risk: large in-sample vs test gap, validation result did not hold on test, loses to random walk in most half-years, unstable across seeds, no better than the constant-drift forecast

**Verdict:** no model beats both the random walk and the constant drift significantly without an overfitting flag.

Overfitting probes (fixed settings, no validation brake): ridge_fixed in-sample +81.5% → test -516.3%; poly2_fixed in-sample +63.2% → test -75.6%; xgb_fixed in-sample +94.2% → test -36.4%; gru_fixed in-sample +97.3% → test -109.4%

GRU test R²oos by seed: -87.59%, -69.94%, -104.95%, -91.33%, -83.89%

## Mean price over next 30 days (drives 50/100/200-day MA forecasts) (`m30`, 30 d)

Rows: train 1737, validation 365, test 1004 (2024-01-01 to 2026-09-30) · 189 features

| Model | Train R²oos | Val R²oos | Test R²oos | Test direction hit | Test DM p | Overfit gap | Half-years beating RW |
|---|---|---|---|---|---|---|---|
| zero | +0.00% | +0.00% | **+0.00%** | – | – | +0.00% | 0/6 |
| mean | +0.47% | +8.10% | **+1.86%** | 0.546 | 0.694 | -0.51% | 4/6 |
| ridge | +6.24% | +2.11% | **+1.04%** | 0.546 | 0.847 | +5.40% | 4/6 |
| poly2 | +0.60% | +8.03% | **+1.88%** | 0.546 | 0.691 | -0.39% | 4/6 |
| xgboost | +2.45% | +8.63% | **+2.45%** | 0.546 | 0.616 | +0.58% | 4/6 |
| ridge_fixed | +85.62% | -807.17% | **-341.63%** | 0.536 | 0.000 | +422.43% | 0/6 |
| poly2_fixed | +66.32% | -67.74% | **-95.50%** | 0.412 | 0.000 | +155.83% | 0/6 |
| xgb_fixed | +95.42% | -134.73% | **-44.71%** | 0.552 | 0.036 | +138.29% | 2/6 |
| gru | +18.73% | +12.96% | **-73.88%** | 0.519 | 0.003 | +144.94% | 1/6 |
| gru_fixed | +98.79% | -212.89% | **-162.23%** | 0.525 | 0.000 | +260.99% | 0/6 |

Ranking on test with overfitting flags:

- **xgboost**: test R²oos +2.45%, DM p vs random walk 0.616, vs drift 0.176 · risk: validation result did not hold on test
- **poly2**: test R²oos +1.88%, DM p vs random walk 0.691, vs drift 0.386 · risk: validation result did not hold on test
- **ridge**: test R²oos +1.04%, DM p vs random walk 0.847, vs drift 0.476 · risk: large in-sample vs test gap, no better than the constant-drift forecast
- **gru**: test R²oos -73.88%, DM p vs random walk 0.003, vs drift 0.003 · risk: large in-sample vs test gap, validation result did not hold on test, loses to random walk in most half-years, unstable across seeds, no better than the constant-drift forecast

**Verdict:** no model beats both the random walk and the constant drift significantly without an overfitting flag.

Overfitting probes (fixed settings, no validation brake): ridge_fixed in-sample +80.8% → test -341.6%; poly2_fixed in-sample +60.3% → test -95.5%; xgb_fixed in-sample +93.6% → test -44.7%; gru_fixed in-sample +98.8% → test -162.2%

GRU test R²oos by seed: -91.46%, -72.86%, -102.42%, -104.35%, -75.08%

## Walk-forward check (refit every 91 days, 2020 onwards)

Each quarter the models are re-tuned on the trailing year and refit on all earlier data, then forecast the next quarter. This tests the same models over about 25 different periods instead of one.

**Next 1 day return** · 25 folds, 2020-09-30 to 2026-10-29

| Model | R²oos | DM p vs random walk | DM p vs drift | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 | 2026 |
|---|---|---|---|---|---|---|---|---|---|---|
| zero | **+0.00%** | – | – | +0.0% | +0.0% | +0.0% | +0.0% | +0.0% | +0.0% | +0.0% |
| mean | **-0.08%** | 0.494 | – | +0.0% | -0.0% | -0.5% | +0.3% | +0.3% | -0.2% | -0.2% |
| ridge | **-0.59%** | 0.183 | 0.224 | -0.2% | -0.8% | -0.8% | -1.4% | +0.3% | -0.6% | -0.3% |
| poly2 | **-0.58%** | 0.326 | 0.364 | +0.1% | +0.4% | -2.1% | -1.7% | -0.1% | -0.0% | -1.0% |
| xgboost | **-0.61%** | 0.326 | 0.388 | -1.8% | +0.1% | -0.7% | -0.8% | -0.5% | -1.6% | -1.4% |

**Next 7 day return** · 25 folds, 2020-09-30 to 2026-10-23

| Model | R²oos | DM p vs random walk | DM p vs drift | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 | 2026 |
|---|---|---|---|---|---|---|---|---|---|---|
| zero | **+0.00%** | – | – | +0.0% | +0.0% | +0.0% | +0.0% | +0.0% | +0.0% | +0.0% |
| mean | **-0.61%** | 0.377 | – | +0.2% | -0.7% | -3.1% | +1.6% | +2.2% | -2.1% | -1.7% |
| ridge | **-2.21%** | 0.102 | 0.232 | +1.8% | -4.7% | -2.3% | -4.3% | +2.6% | -2.7% | -2.1% |
| poly2 | **-3.00%** | 0.266 | 0.343 | +2.6% | +1.9% | -5.9% | -19.1% | +0.8% | -1.9% | -3.3% |
| xgboost | **-8.81%** | 0.011 | 0.016 | +4.2% | -4.4% | -14.0% | -39.4% | +2.3% | -6.3% | -1.8% |

**Next 30 day return** · 25 folds, 2020-09-30 to 2026-09-30

| Model | R²oos | DM p vs random walk | DM p vs drift | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 | 2026 |
|---|---|---|---|---|---|---|---|---|---|---|
| zero | **+0.00%** | – | – | +0.0% | +0.0% | +0.0% | +0.0% | +0.0% | +0.0% | +0.0% |
| mean | **-2.18%** | 0.473 | – | +2.7% | -5.2% | -13.7% | +7.8% | +9.6% | -12.2% | -5.5% |
| ridge | **-15.47%** | 0.038 | 0.063 | +3.6% | -20.2% | -2.8% | -104.2% | +10.2% | -19.6% | -5.7% |
| poly2 | **-14.38%** | 0.029 | 0.032 | +2.7% | -6.1% | -57.9% | -26.6% | +7.0% | -15.5% | -14.4% |
| xgboost | **-22.78%** | 0.011 | 0.006 | -3.9% | -61.2% | -14.6% | -5.3% | +5.2% | -52.5% | -6.4% |

**Mean price over next 30 days (drives 50/100/200-day MA forecasts)** · 25 folds, 2020-09-30 to 2026-09-30

| Model | R²oos | DM p vs random walk | DM p vs drift | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 | 2026 |
|---|---|---|---|---|---|---|---|---|---|---|
| zero | **+0.00%** | – | – | +0.0% | +0.0% | +0.0% | +0.0% | +0.0% | +0.0% | +0.0% |
| mean | **-1.19%** | 0.681 | – | +4.6% | -3.4% | -14.1% | +8.7% | +8.8% | -10.5% | -5.1% |
| ridge | **-6.71%** | 0.200 | 0.219 | +5.9% | -16.8% | -0.5% | -28.8% | +8.9% | -15.4% | -5.0% |
| poly2 | **-8.94%** | 0.051 | 0.038 | +5.1% | -6.1% | -34.0% | -21.3% | +5.4% | -9.8% | -7.8% |
| xgboost | **-17.33%** | 0.032 | 0.023 | +2.2% | -34.6% | -8.6% | -47.9% | +9.0% | -46.5% | -5.5% |

## 50/100/200-day moving averages, 30 days ahead

Forecast = known part of the average + 30 predicted days (from the `m30` model). The naive forecast fills the 30 unknown days with today's price.

| Model | MA50 error | MA100 error | MA200 error | MA50 vs naive | MA100 vs naive | MA200 vs naive |
|---|---|---|---|---|---|---|
| gru | 4.92% | 2.51% | 1.30% | 1.350× | 1.342× | 1.331× |
| gru_fixed | 6.01% | 3.09% | 1.61% | 1.648× | 1.652× | 1.651× |
| mean | 3.68% | 1.88% | 0.98% | 1.008× | 1.005× | 1.006× |
| poly2 | 3.68% | 1.88% | 0.98% | 1.008× | 1.005× | 1.006× |
| poly2_fixed | 5.38% | 2.73% | 1.41% | 1.474× | 1.461× | 1.448× |
| ridge | 3.72% | 1.90% | 0.99% | 1.021× | 1.017× | 1.019× |
| ridge_fixed | 8.21% | 4.18% | 2.17% | 2.250× | 2.235× | 2.220× |
| xgb_fixed | 4.90% | 2.48% | 1.29% | 1.343× | 1.324× | 1.326× |
| xgboost | 3.67% | 1.88% | 0.98% | 1.007× | 1.003× | 1.004× |
| zero | 3.65% | 1.87% | 0.98% | 1.000× | 1.000× | 1.000× |

The naive forecast alone already explains MA50 96.2%, MA100 99.1%, MA200 99.8% of the variation in moving-average levels on test, so high R² on moving averages says nothing about skill.

## XGBoost: most used features (gain, final refit)

- `r1`: btc_ma_gap_20, fed_funds_chg_7, news_tone_conflict_lvl, btc_ma_gap_100, cm_exchange_supply_chg_7, ust10y_z365, ust10y_chg_30, gpr_acts_lvl, move_z365, ust10y_yahoo_z365, m2_chg_90, btc_rsi_14
- `r7`: fin_conditions_z365, btc_mom_90, btc_mom_365, epu_us_lvl, fin_conditions_lvl, fed_funds_z365
- `r30`: fin_conditions_z365, ust10y_lvl, ust10y_yahoo_lvl, fed_funds_lvl, move_z365, curve_10y2y_z365, btc_ma_gap_100, breakeven5y_z365, gold_ret_30, usd_broad_gap_200, stablecoin_supply_chg_90, fed_balance_sheet_chg_90
- `m30`: ust10y_yahoo_lvl, fin_conditions_z365, fed_funds_lvl, fed_funds_z365, m2_z365, epu_us_lvl

## Data sources

| Series | Source | Kind | Lag (days) | From | To | Status |
|---|---|---|---|---|---|---|
| breakeven5y | FRED (St. Louis Fed) | level | 1 | 2010-01-04 | 2026-10-30 | ok |
| btc | Yahoo Finance | price | 0 | 2014-09-17 | 2026-10-31 | ok |
| btc_volume | Yahoo Finance | count | 0 | 2014-09-17 | 2026-10-31 | ok |
| cm_active_addresses | Coin Metrics community API | count | 1 | 2013-01-01 | 2026-10-30 | ok |
| cm_exchange_inflow | Coin Metrics community API | count | 1 | 2013-01-01 | 2026-10-30 | ok |
| cm_exchange_outflow | Coin Metrics community API | count | 1 | 2013-01-01 | 2026-10-30 | ok |
| cm_exchange_supply | Coin Metrics community API | count | 1 | 2013-01-01 | 2026-10-30 | ok |
| cm_hashrate | Coin Metrics community API | count | 1 | 2013-01-01 | 2026-10-30 | ok |
| cm_issuance | Coin Metrics community API | count | 1 | 2013-01-01 | 2026-10-30 | ok |
| cm_mvrv | Coin Metrics community API | level | 1 | 2013-01-01 | 2026-10-30 | ok |
| cm_price | Coin Metrics community API | price | 1 | 2013-01-01 | 2026-10-30 | ok |
| cm_tx_count | Coin Metrics community API | count | 1 | 2013-01-01 | 2026-10-30 | ok |
| coin | Yahoo Finance | price | 0 | 2021-04-14 | 2026-10-30 | ok |
| curve_10y2y | FRED (St. Louis Fed) | level | 1 | 2010-01-04 | 2026-10-30 | ok |
| dxy | Yahoo Finance | price | 0 | 2013-01-02 | 2026-10-30 | ok |
| emu_us | FRED (St. Louis Fed) | level | 1 | 2010-01-01 | 2026-10-29 | ok |
| epu_us | FRED (St. Louis Fed) | level | 1 | 2010-01-01 | 2026-10-29 | ok |
| eth | Yahoo Finance | price | 0 | 2017-11-09 | 2026-10-31 | ok |
| fear_greed | alternative.me | level | 0 | 2018-02-01 | 2026-10-31 | ok |
| fed_balance_sheet | FRED (St. Louis Fed) | count | 2 | 2010-01-06 | 2026-10-28 | ok |
| fed_funds | FRED (St. Louis Fed) | level | 1 | 2010-01-01 | 2026-10-29 | ok |
| fin_conditions | FRED (St. Louis Fed) | level | 7 | 2010-01-01 | 2026-10-23 | ok |
| funding_rate | Binance or BitMEX | | | | | failed: RuntimeError: binance: Binance HTTP 451; bitmex: BitMEX HTTP 403 |
| gold | Yahoo Finance | price | 0 | 2013-01-02 | 2026-10-30 | ok |
| gpr | Caldara & Iacoviello GPR | level | 1 | 2010-01-01 | 2026-10-26 | ok |
| gpr_acts | Caldara & Iacoviello GPR | level | 1 | 2010-01-01 | 2026-10-26 | ok |
| gpr_threats | Caldara & Iacoviello GPR | level | 1 | 2010-01-01 | 2026-10-26 | ok |
| hy_spread | FRED (St. Louis Fed) | level | 1 | 2023-10-31 | 2026-10-29 | ok |
| m2 | FRED (St. Louis Fed) | count | 60 | 2010-01-01 | 2026-09-01 | ok |
| move | Yahoo Finance | level | 0 | 2013-01-02 | 2026-10-30 | ok |
| mstr | Yahoo Finance | price | 0 | 2013-01-02 | 2026-10-30 | ok |
| nasdaq | Yahoo Finance | price | 0 | 2013-01-02 | 2026-10-30 | ok |
| news_tone_bitcoin | GDELT 2.0 DOC API | level | 1 | 2017-01-01 | 2026-10-27 | ok |
| news_tone_conflict | GDELT 2.0 DOC API | level | 1 | 2017-01-01 | 2026-10-27 | ok |
| news_tone_macro | GDELT 2.0 DOC API | level | 1 | 2017-01-01 | 2026-10-27 | ok |
| news_volume_bitcoin | GDELT 2.0 DOC API | count | 1 | 2017-01-01 | 2026-10-27 | ok |
| oil | Yahoo Finance | price | 0 | 2013-01-02 | 2026-10-30 | ok |
| reverse_repo | FRED (St. Louis Fed) | count | 1 | 2010-08-12 | 2026-10-30 | ok |
| sp500 | Yahoo Finance | price | 0 | 2013-01-02 | 2026-10-30 | ok |
| stablecoin_supply | DefiLlama | count | 1 | 2017-11-29 | 2026-10-31 | ok |
| treasury_account | FRED (St. Louis Fed) | count | 2 | 2010-01-06 | 2026-10-28 | ok |
| usd_broad | FRED (St. Louis Fed) | price | 1 | 2010-01-04 | 2026-10-23 | ok |
| ust10y | FRED (St. Louis Fed) | level | 1 | 2010-01-04 | 2026-10-29 | ok |
| ust10y_yahoo | Yahoo Finance | level | 0 | 2013-01-02 | 2026-10-30 | ok |
| ust2y | FRED (St. Louis Fed) | level | 1 | 2010-01-04 | 2026-10-29 | ok |
| vix | Yahoo Finance | level | 0 | 2013-01-02 | 2026-10-30 | ok |
| wiki_bitcoin | Wikimedia pageviews | count | 1 | 2015-07-01 | 2026-10-30 | ok |
| wiki_crypto | Wikimedia pageviews | count | 1 | 2015-07-01 | 2026-10-30 | ok |

Lag is the number of days a value is held back before the model may use it, so that only data that was public at the time enters each prediction.
