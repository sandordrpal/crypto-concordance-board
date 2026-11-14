# Bitcoin model comparison: train, validate, test

Run: 2026-11-14 09:38 UTC · data collected 2026-11-14T09:09:11+00:00 · 46 of 48 series loaded · price base `btc` · runtime 21.6 min

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

Rows: train 1766, validation 365, test 1047 (2024-01-01 to 2026-11-12) · 185 features

| Model | Train R²oos | Val R²oos | Test R²oos | Test direction hit | Test DM p | Overfit gap | Half-years beating RW |
|---|---|---|---|---|---|---|---|
| zero | +0.00% | +0.00% | **+0.00%** | – | – | +0.00% | 0/6 |
| mean | +0.00% | +0.23% | **+0.02%** | 0.500 | 0.894 | +0.01% | 4/6 |
| ridge | +0.49% | -0.26% | **+0.03%** | 0.501 | 0.880 | +0.45% | 4/6 |
| poly2 | +0.08% | +0.23% | **+0.03%** | 0.500 | 0.828 | +0.09% | 4/6 |
| xgboost | +1.56% | +0.32% | **+0.11%** | 0.501 | 0.632 | +1.46% | 4/6 |
| ridge_fixed | +17.23% | -82.09% | **-120.03%** | 0.543 | 0.000 | +134.89% | 0/6 |
| poly2_fixed | +20.32% | -63.99% | **-28.50%** | 0.488 | 0.000 | +46.78% | 0/6 |
| xgb_fixed | +46.90% | -17.50% | **-2.76%** | 0.504 | 0.170 | +44.41% | 2/6 |
| gru | +2.86% | -2.75% | **-2.44%** | 0.508 | 0.037 | +6.15% | 0/6 |
| gru_fixed | +36.02% | -74.35% | **-42.89%** | 0.538 | 0.000 | +79.30% | 0/6 |

Ranking on test with overfitting flags:

- **xgboost**: test R²oos +0.11%, DM p vs random walk 0.632, vs drift 0.532 · no risk flags
- **poly2**: test R²oos +0.03%, DM p vs random walk 0.828, vs drift 0.163 · no risk flags
- **ridge**: test R²oos +0.03%, DM p vs random walk 0.880, vs drift 0.907 · no risk flags
- **gru**: test R²oos -2.44%, DM p vs random walk 0.037, vs drift 0.025 · risk: large in-sample vs test gap, loses to random walk in most half-years, no better than the constant-drift forecast

**Verdict:** no model beats both the random walk and the constant drift significantly without an overfitting flag.

Overfitting probes (fixed settings, no validation brake): ridge_fixed in-sample +14.9% → test -120.0%; poly2_fixed in-sample +18.3% → test -28.5%; xgb_fixed in-sample +41.6% → test -2.8%; gru_fixed in-sample +36.4% → test -42.9%

GRU test R²oos by seed: -4.13%, -2.06%, -2.19%, -2.84%, -3.07%

## Next 7 day return (`r7`, 7 d)

Rows: train 1760, validation 365, test 1041 (2024-01-01 to 2026-11-06) · 185 features

| Model | Train R²oos | Val R²oos | Test R²oos | Test direction hit | Test DM p | Overfit gap | Half-years beating RW |
|---|---|---|---|---|---|---|---|
| zero | +0.00% | +0.00% | **+0.00%** | – | – | +0.00% | 0/6 |
| mean | +0.03% | +1.24% | **+0.27%** | 0.515 | 0.784 | -0.06% | 4/6 |
| ridge | +2.36% | -1.07% | **+0.30%** | 0.512 | 0.816 | +2.04% | 4/6 |
| poly2 | +0.05% | +1.21% | **+0.28%** | 0.515 | 0.775 | -0.04% | 4/6 |
| xgboost | +1.57% | +1.22% | **-0.16%** | 0.515 | 0.906 | +1.73% | 3/6 |
| ridge_fixed | +56.02% | -126.64% | **-444.59%** | 0.493 | 0.000 | +494.79% | 0/6 |
| poly2_fixed | +46.85% | -69.56% | **-92.15%** | 0.458 | 0.000 | +135.05% | 0/6 |
| xgb_fixed | +80.64% | -96.07% | **-22.98%** | 0.524 | 0.000 | +98.99% | 1/6 |
| gru | +8.86% | +2.95% | **-23.77%** | 0.499 | 0.000 | +46.02% | 1/6 |
| gru_fixed | +91.32% | -235.05% | **-154.50%** | 0.503 | 0.000 | +245.69% | 0/6 |

Ranking on test with overfitting flags:

- **ridge**: test R²oos +0.30%, DM p vs random walk 0.816, vs drift 0.958 · no risk flags
- **poly2**: test R²oos +0.28%, DM p vs random walk 0.775, vs drift 0.097 · no risk flags
- **xgboost**: test R²oos -0.16%, DM p vs random walk 0.906, vs drift 0.352 · risk: no better than the constant-drift forecast
- **gru**: test R²oos -23.77%, DM p vs random walk 0.000, vs drift 0.000 · risk: large in-sample vs test gap, validation result did not hold on test, loses to random walk in most half-years, no better than the constant-drift forecast

**Verdict:** no model beats both the random walk and the constant drift significantly without an overfitting flag.

Overfitting probes (fixed settings, no validation brake): ridge_fixed in-sample +50.2% → test -444.6%; poly2_fixed in-sample +42.9% → test -92.1%; xgb_fixed in-sample +76.0% → test -23.0%; gru_fixed in-sample +91.2% → test -154.5%

GRU test R²oos by seed: -24.95%, -27.99%, -24.50%, -24.67%, -24.21%

## Next 30 day return (`r30`, 30 d)

Rows: train 1737, validation 365, test 1018 (2024-01-01 to 2026-10-14) · 185 features

| Model | Train R²oos | Val R²oos | Test R²oos | Test direction hit | Test DM p | Overfit gap | Half-years beating RW |
|---|---|---|---|---|---|---|---|
| zero | +0.00% | +0.00% | **+0.00%** | – | – | +0.00% | 0/6 |
| mean | +0.24% | +6.66% | **+1.54%** | 0.552 | 0.740 | -0.42% | 4/6 |
| ridge | +7.27% | -2.56% | **+0.47%** | 0.552 | 0.931 | +6.69% | 4/6 |
| poly2 | +0.65% | +6.65% | **+1.53%** | 0.552 | 0.741 | +0.02% | 4/6 |
| xgboost | +2.32% | +7.76% | **+1.10%** | 0.552 | 0.826 | +1.98% | 4/6 |
| ridge_fixed | +85.99% | -1423.59% | **-543.63%** | 0.520 | 0.000 | +624.78% | 0/6 |
| poly2_fixed | +69.13% | -145.24% | **-69.02%** | 0.448 | 0.000 | +131.39% | 0/6 |
| xgb_fixed | +95.68% | -137.39% | **-34.31%** | 0.585 | 0.029 | +128.57% | 1/6 |
| gru | +26.38% | +7.20% | **-62.32%** | 0.537 | 0.009 | +137.74% | 0/6 |
| gru_fixed | +97.41% | -83.58% | **-94.29%** | 0.522 | 0.000 | +191.75% | 0/6 |

Ranking on test with overfitting flags:

- **poly2**: test R²oos +1.53%, DM p vs random walk 0.741, vs drift 0.850 · risk: validation result did not hold on test, no better than the constant-drift forecast
- **xgboost**: test R²oos +1.10%, DM p vs random walk 0.826, vs drift 0.332 · risk: validation result did not hold on test, no better than the constant-drift forecast
- **ridge**: test R²oos +0.47%, DM p vs random walk 0.931, vs drift 0.389 · risk: large in-sample vs test gap, no better than the constant-drift forecast
- **gru**: test R²oos -62.32%, DM p vs random walk 0.009, vs drift 0.008 · risk: large in-sample vs test gap, validation result did not hold on test, loses to random walk in most half-years, unstable across seeds, no better than the constant-drift forecast

**Verdict:** no model beats both the random walk and the constant drift significantly without an overfitting flag.

Overfitting probes (fixed settings, no validation brake): ridge_fixed in-sample +81.1% → test -543.6%; poly2_fixed in-sample +62.4% → test -69.0%; xgb_fixed in-sample +94.3% → test -34.3%; gru_fixed in-sample +97.5% → test -94.3%

GRU test R²oos by seed: -81.75%, -77.49%, -87.11%, -83.54%, -63.07%

## Mean price over next 30 days (drives 50/100/200-day MA forecasts) (`m30`, 30 d)

Rows: train 1737, validation 365, test 1018 (2024-01-01 to 2026-10-14) · 185 features

| Model | Train R²oos | Val R²oos | Test R²oos | Test direction hit | Test DM p | Overfit gap | Half-years beating RW |
|---|---|---|---|---|---|---|---|
| zero | +0.00% | +0.00% | **+0.00%** | – | – | +0.00% | 0/6 |
| mean | +0.47% | +8.10% | **+1.56%** | 0.538 | 0.741 | -0.21% | 4/6 |
| ridge | +6.14% | +2.08% | **+0.68%** | 0.538 | 0.899 | +5.67% | 4/6 |
| poly2 | +0.86% | +8.03% | **+1.54%** | 0.538 | 0.744 | +0.21% | 4/6 |
| xgboost | +11.20% | +10.12% | **+2.00%** | 0.553 | 0.757 | +9.03% | 4/6 |
| ridge_fixed | +85.36% | -856.24% | **-306.21%** | 0.539 | 0.000 | +386.70% | 0/6 |
| poly2_fixed | +66.45% | -89.96% | **-84.78%** | 0.442 | 0.000 | +144.57% | 0/6 |
| xgb_fixed | +95.29% | -117.63% | **-47.47%** | 0.558 | 0.025 | +140.81% | 2/6 |
| gru | +23.82% | +11.96% | **-69.68%** | 0.502 | 0.002 | +136.67% | 1/6 |
| gru_fixed | +98.71% | -207.57% | **-167.32%** | 0.515 | 0.000 | +266.12% | 0/6 |

Ranking on test with overfitting flags:

- **xgboost**: test R²oos +2.00%, DM p vs random walk 0.757, vs drift 0.843 · risk: large in-sample vs test gap, validation result did not hold on test
- **poly2**: test R²oos +1.54%, DM p vs random walk 0.744, vs drift 0.532 · risk: validation result did not hold on test, no better than the constant-drift forecast
- **ridge**: test R²oos +0.68%, DM p vs random walk 0.899, vs drift 0.435 · risk: large in-sample vs test gap, no better than the constant-drift forecast
- **gru**: test R²oos -69.68%, DM p vs random walk 0.002, vs drift 0.001 · risk: large in-sample vs test gap, validation result did not hold on test, loses to random walk in most half-years, unstable across seeds, no better than the constant-drift forecast

**Verdict:** no model beats both the random walk and the constant drift significantly without an overfitting flag.

Overfitting probes (fixed settings, no validation brake): ridge_fixed in-sample +80.5% → test -306.2%; poly2_fixed in-sample +59.8% → test -84.8%; xgb_fixed in-sample +93.3% → test -47.5%; gru_fixed in-sample +98.8% → test -167.3%

GRU test R²oos by seed: -66.48%, -94.28%, -87.74%, -94.85%, -71.70%

## Walk-forward check (refit every 91 days, 2020 onwards)

Each quarter the models are re-tuned on the trailing year and refit on all earlier data, then forecast the next quarter. This tests the same models over about 25 different periods instead of one.

**Next 1 day return** · 25 folds, 2020-09-30 to 2026-11-12

| Model | R²oos | DM p vs random walk | DM p vs drift | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 | 2026 |
|---|---|---|---|---|---|---|---|---|---|---|
| zero | **+0.00%** | – | – | +0.0% | +0.0% | +0.0% | +0.0% | +0.0% | +0.0% | +0.0% |
| mean | **-0.09%** | 0.451 | – | +0.0% | -0.0% | -0.5% | +0.3% | +0.3% | -0.2% | -0.3% |
| ridge | **-1.17%** | 0.032 | 0.043 | +0.2% | -2.0% | -1.7% | -1.5% | +0.3% | -0.6% | -0.4% |
| poly2 | **-0.34%** | 0.658 | 0.733 | +0.2% | +0.4% | -1.5% | -1.2% | +0.0% | +0.1% | -0.7% |
| xgboost | **-0.25%** | 0.624 | 0.747 | +1.6% | -0.4% | -0.5% | -0.7% | -0.4% | +0.6% | -0.3% |

**Next 7 day return** · 25 folds, 2020-09-30 to 2026-11-06

| Model | R²oos | DM p vs random walk | DM p vs drift | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 | 2026 |
|---|---|---|---|---|---|---|---|---|---|---|
| zero | **+0.00%** | – | – | +0.0% | +0.0% | +0.0% | +0.0% | +0.0% | +0.0% | +0.0% |
| mean | **-0.65%** | 0.347 | – | +0.2% | -0.7% | -3.1% | +1.6% | +2.2% | -2.1% | -2.1% |
| ridge | **-2.19%** | 0.101 | 0.247 | +1.8% | -4.4% | -2.4% | -4.7% | +2.6% | -2.1% | -2.4% |
| poly2 | **-3.26%** | 0.125 | 0.193 | +5.3% | +1.1% | -5.4% | -17.1% | -3.8% | -1.6% | -3.3% |
| xgboost | **-4.61%** | 0.037 | 0.053 | +0.6% | -2.1% | -11.7% | -12.2% | +3.9% | -7.4% | -2.2% |

**Next 30 day return** · 25 folds, 2020-09-30 to 2026-10-14

| Model | R²oos | DM p vs random walk | DM p vs drift | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 | 2026 |
|---|---|---|---|---|---|---|---|---|---|---|
| zero | **+0.00%** | – | – | +0.0% | +0.0% | +0.0% | +0.0% | +0.0% | +0.0% | +0.0% |
| mean | **-2.28%** | 0.454 | – | +2.7% | -5.2% | -13.7% | +7.8% | +9.6% | -12.2% | -6.5% |
| ridge | **-15.71%** | 0.032 | 0.055 | +3.7% | -16.8% | -12.9% | -98.1% | +10.2% | -19.5% | -7.0% |
| poly2 | **-17.41%** | 0.022 | 0.019 | +2.4% | -15.2% | -58.3% | -29.3% | +5.9% | -16.7% | -14.2% |
| xgboost | **-25.39%** | 0.009 | 0.007 | -3.1% | -67.4% | -10.9% | -20.1% | +6.4% | -61.7% | -6.2% |

**Mean price over next 30 days (drives 50/100/200-day MA forecasts)** · 25 folds, 2020-09-30 to 2026-10-14

| Model | R²oos | DM p vs random walk | DM p vs drift | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 | 2026 |
|---|---|---|---|---|---|---|---|---|---|---|
| zero | **+0.00%** | – | – | +0.0% | +0.0% | +0.0% | +0.0% | +0.0% | +0.0% | +0.0% |
| mean | **-1.26%** | 0.662 | – | +4.6% | -3.4% | -14.1% | +8.7% | +8.8% | -10.5% | -5.9% |
| ridge | **-6.46%** | 0.181 | 0.165 | +5.8% | -14.6% | -2.4% | -28.4% | +8.9% | -15.3% | -6.1% |
| poly2 | **-11.06%** | 0.058 | 0.031 | +4.9% | -14.7% | -30.6% | -22.7% | +2.5% | -10.2% | -4.8% |
| xgboost | **-17.68%** | 0.043 | 0.032 | +2.0% | -34.8% | -9.2% | -55.0% | +8.4% | -33.3% | -5.8% |

## 50/100/200-day moving averages, 30 days ahead

Forecast = known part of the average + 30 predicted days (from the `m30` model). The naive forecast fills the 30 unknown days with today's price.

| Model | MA50 error | MA100 error | MA200 error | MA50 vs naive | MA100 vs naive | MA200 vs naive |
|---|---|---|---|---|---|---|
| gru | 4.88% | 2.51% | 1.31% | 1.343× | 1.344× | 1.348× |
| gru_fixed | 6.19% | 3.21% | 1.69% | 1.704× | 1.719× | 1.736× |
| mean | 3.67% | 1.88% | 0.98% | 1.012× | 1.008× | 1.009× |
| poly2 | 3.67% | 1.88% | 0.98% | 1.012× | 1.008× | 1.009× |
| poly2_fixed | 5.22% | 2.65% | 1.37% | 1.436× | 1.423× | 1.413× |
| ridge | 3.72% | 1.90% | 0.99% | 1.023× | 1.020× | 1.022× |
| ridge_fixed | 7.91% | 4.03% | 2.09% | 2.177× | 2.161× | 2.147× |
| xgb_fixed | 4.91% | 2.48% | 1.30% | 1.351× | 1.332× | 1.333× |
| xgboost | 3.70% | 1.89% | 0.99% | 1.019× | 1.015× | 1.016× |
| zero | 3.63% | 1.86% | 0.97% | 1.000× | 1.000× | 1.000× |

The naive forecast alone already explains MA50 96.2%, MA100 99.1%, MA200 99.8% of the variation in moving-average levels on test, so high R² on moving averages says nothing about skill.

## XGBoost: most used features (gain, final refit)

- `r1`: dxy_gap_200, cm_exchange_supply_z365, cm_exchange_supply_chg_7, fin_conditions_chg_7, reverse_repo_chg_30, cm_tx_count_z365, oil_gap_200, wiki_crypto_z365, btc_ma_gap_50, cm_issuance_chg_90, news_tone_bitcoin_chg_30, btc_mom_60
- `r7`: fin_conditions_z365, btc_mom_90, fin_conditions_lvl, reverse_repo_z365, epu_us_chg_30, epu_us_lvl
- `r30`: ust10y_yahoo_lvl, fed_funds_lvl, btc_vol_90, mstr_gap_200, btc_mom_60, btc_ma_gap_200, btc_mom_180, fin_conditions_z365, dxy_gap_200, fed_funds_z365, cm_mvrv_lvl, stablecoin_supply_chg_90
- `m30`: fin_conditions_z365, fed_balance_sheet_chg_90, btc_ma_gap_100, breakeven5y_lvl, fed_funds_z365, btc_vol_90, ust10y_yahoo_lvl, curve_10y2y_z365, fed_funds_lvl, fin_conditions_lvl, reverse_repo_z365, breakeven5y_z365

## Data sources

| Series | Source | Kind | Lag (days) | From | To | Status |
|---|---|---|---|---|---|---|
| breakeven5y | FRED (St. Louis Fed) | level | 1 | 2010-01-04 | 2026-11-13 | ok |
| btc | Yahoo Finance | price | 0 | 2014-09-17 | 2026-11-14 | ok |
| btc_volume | Yahoo Finance | count | 0 | 2014-09-17 | 2026-11-14 | ok |
| cm_active_addresses | Coin Metrics community API | count | 1 | 2013-01-01 | 2026-11-13 | ok |
| cm_exchange_inflow | Coin Metrics community API | count | 1 | 2013-01-01 | 2026-11-13 | ok |
| cm_exchange_outflow | Coin Metrics community API | count | 1 | 2013-01-01 | 2026-11-13 | ok |
| cm_exchange_supply | Coin Metrics community API | count | 1 | 2013-01-01 | 2026-11-13 | ok |
| cm_hashrate | Coin Metrics community API | count | 1 | 2013-01-01 | 2026-11-13 | ok |
| cm_issuance | Coin Metrics community API | count | 1 | 2013-01-01 | 2026-11-13 | ok |
| cm_mvrv | Coin Metrics community API | level | 1 | 2013-01-01 | 2026-11-13 | ok |
| cm_price | Coin Metrics community API | price | 1 | 2013-01-01 | 2026-11-13 | ok |
| cm_tx_count | Coin Metrics community API | count | 1 | 2013-01-01 | 2026-11-13 | ok |
| coin | Yahoo Finance | price | 0 | 2021-04-14 | 2026-11-13 | ok |
| curve_10y2y | FRED (St. Louis Fed) | level | 1 | 2010-01-04 | 2026-11-13 | ok |
| dxy | Yahoo Finance | price | 0 | 2013-01-02 | 2026-11-13 | ok |
| emu_us | FRED (St. Louis Fed) | level | 1 | 2010-01-01 | 2026-11-12 | ok |
| epu_us | FRED (St. Louis Fed) | level | 1 | 2010-01-01 | 2026-11-12 | ok |
| eth | Yahoo Finance | price | 0 | 2017-11-09 | 2026-11-14 | ok |
| fear_greed | alternative.me | level | 0 | 2018-02-01 | 2026-11-14 | ok |
| fed_balance_sheet | FRED (St. Louis Fed) | count | 2 | 2010-01-06 | 2026-11-11 | ok |
| fed_funds | FRED (St. Louis Fed) | level | 1 | 2010-01-01 | 2026-11-12 | ok |
| fin_conditions | FRED (St. Louis Fed) | level | 7 | 2010-01-01 | 2026-11-06 | ok |
| funding_rate | Binance or BitMEX | | | | | failed: RuntimeError: binance: Binance HTTP 451; bitmex: BitMEX HTTP 403 |
| gold | Yahoo Finance | price | 0 | 2013-01-02 | 2026-11-13 | ok |
| gpr | Caldara & Iacoviello GPR | level | 1 | 2010-01-01 | 2026-11-02 | ok |
| gpr_acts | Caldara & Iacoviello GPR | level | 1 | 2010-01-01 | 2026-11-02 | ok |
| gpr_threats | Caldara & Iacoviello GPR | level | 1 | 2010-01-01 | 2026-11-02 | ok |
| hy_spread | FRED (St. Louis Fed) | level | 1 | 2023-11-14 | 2026-11-12 | ok |
| m2 | FRED (St. Louis Fed) | count | 60 | 2010-01-01 | 2026-09-01 | ok |
| move | Yahoo Finance | level | 0 | 2013-01-02 | 2026-11-13 | ok |
| mstr | Yahoo Finance | price | 0 | 2013-01-02 | 2026-11-13 | ok |
| nasdaq | Yahoo Finance | price | 0 | 2013-01-02 | 2026-11-13 | ok |
| news_tone_bitcoin | GDELT 2.0 DOC API | level | 1 | 2017-01-01 | 2026-11-12 | ok |
| news_tone_conflict | GDELT 2.0 DOC API | level | 1 | 2017-01-01 | 2026-11-12 | ok |
| news_tone_macro | GDELT 2.0 DOC API | level | 1 | 2017-01-01 | 2026-11-12 | ok |
| news_volume_bitcoin | GDELT | | | | | failed: RuntimeError: GDELT rate limit persisted |
| oil | Yahoo Finance | price | 0 | 2013-01-02 | 2026-11-13 | ok |
| reverse_repo | FRED (St. Louis Fed) | count | 1 | 2010-08-12 | 2026-11-13 | ok |
| sp500 | Yahoo Finance | price | 0 | 2013-01-02 | 2026-11-13 | ok |
| stablecoin_supply | DefiLlama | count | 1 | 2017-11-29 | 2026-11-14 | ok |
| treasury_account | FRED (St. Louis Fed) | count | 2 | 2010-01-06 | 2026-11-11 | ok |
| usd_broad | FRED (St. Louis Fed) | price | 1 | 2010-01-04 | 2026-11-06 | ok |
| ust10y | FRED (St. Louis Fed) | level | 1 | 2010-01-04 | 2026-11-12 | ok |
| ust10y_yahoo | Yahoo Finance | level | 0 | 2013-01-02 | 2026-11-13 | ok |
| ust2y | FRED (St. Louis Fed) | level | 1 | 2010-01-04 | 2026-11-12 | ok |
| vix | Yahoo Finance | level | 0 | 2013-01-02 | 2026-11-13 | ok |
| wiki_bitcoin | Wikimedia pageviews | count | 1 | 2015-07-01 | 2026-11-13 | ok |
| wiki_crypto | Wikimedia pageviews | count | 1 | 2015-07-01 | 2026-11-13 | ok |

Lag is the number of days a value is held back before the model may use it, so that only data that was public at the time enters each prediction.
