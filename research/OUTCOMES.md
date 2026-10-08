# Pre-registered outcomes

Written and committed before any of these tests were run, so the thresholds cannot be tuned to the results.
Every outcome is scored out of sample in a walk-forward design starting 2021-01-01: models are refit
on past data only and evaluated on the following period, over and over, up to the latest data.

Costs: 10 basis points (0.10%) per side on every change of position, a typical spot taker fee.
Risk-free rate: 0. Data: Binance hourly candles with taker buy volume, plus the daily research variables.

## Track A: Bitcoin volatility (risk forecasting)

Why: published work finds volatility far more predictable than direction. The benchmark is HAR
(daily, weekly and monthly realized volatility), re-estimated every day on a rolling 3-year window.

| ID | Outcome | Pass when |
|---|---|---|
| A1 | Forecast of next-day realized volatility (from 24 hourly returns) | A challenger model has lower QLIKE loss than HAR, Diebold-Mariano p < 0.05 |
| A2 | Forecast of next-7-day realized volatility | Same rule as A1 |
| A3 | Volatility-targeted Bitcoin holding (daily weight = 50% ÷ forecast annualized volatility, capped at 100%, costs included) | Sharpe ratio above buy-and-hold **and** maximum drawdown at least 25% smaller than buy-and-hold |

Challengers: HAR with semivariances and jumps, ridge with the news, sentiment and macro variables, XGBoost, GRU.

## Track B: ranking coins against each other (weekly)

Why: published work finds relative returns across coins predictable from size, momentum, illiquidity
and trend signals. Universe: up to 50 large coins on Binance with at least 120 days of history.
Rebalanced every Monday 00:00 UTC.

| ID | Outcome | Pass when |
|---|---|---|
| B1 | Rank correlation between predicted and next-week coin returns (information coefficient) | Mean weekly IC > 0 with Newey-West t-statistic > 2 |
| B2 | Long-only portfolio of the top fifth of coins, equal weight, after costs | Net Sharpe above the equal-weight universe **and** mean weekly excess return over it with t > 2 |

Models: 4-week momentum rule, ridge on 20 rank-normalized coin characteristics, XGBoost, and a small neural network (MLP).

## Track C: Bitcoin intraday order flow (1 to 12 hours)

Why: buy/sell imbalance has been reported to predict returns a few hours ahead, and hourly data gives
roughly 70,000 observations instead of 2,500.

| ID | Outcome | Pass when |
|---|---|---|
| C1 | Next-4-hour Bitcoin return | Out-of-sample R² vs the random walk > 0 with Diebold-Mariano p < 0.05, **and** direction hit rate > 51% |
| C2 | Cost-aware long/flat strategy on the 4-hour forecast (enter only when the forecast clears the round-trip cost) | Net Sharpe above buy-and-hold over the same period **and** positive net return in at least 4 of the 6 test years |

Models: ridge, XGBoost, GRU on 24-hour sequences. Next-1-hour and next-12-hour returns are reported for context only.

## What does not count

- In-sample fit, validation-year results or any single lucky year.
- Results before costs.
- A model that passes only after its settings were changed in response to these results; such a change
  starts a new pre-registered test on data that arrives afterwards.

## Version 2: does more free data help? (registered 2026-10-08, before any v2 run)

Version 1 above is frozen. Version 2 asks one question per track: do new free inputs improve the
forecasts, and is a complex model needed to use them? It crosses three feature tiers with two model
families, so every track has six cells.

**Feature tiers.** Each tier contains the one before it. New inputs were chosen from published
evidence, not from our results.

| Tier | Track A: volatility | Track B: ranking | Track C: intraday |
|---|---|---|---|
| F0 current | The v1 inputs | The v1 inputs | The v1 inputs |
| F1 current + a few | + Deribit DVOL (options-implied volatility), realized quarticity (HARQ), Ether and altcoin realized volatility | + multi-horizon trend set (CTREND: 3/5/10/100-day price averages, volume averages), funding-rate carry | + futures premium over spot, latest funding rate, Coinbase premium |
| F2 current + all free | + futures open interest, long/short ratios, futures order flow and volume share, premium, Coinbase premium, Ether DVOL, the gap between implied and realized volatility, FOMC days | + futures premium, open-interest change, long/short ratios, futures order flow and volume share, funding change | + open-interest changes, long/short ratios, futures order flow and volume share, DVOL level and changes, average trade size, hours to the next scheduled FOMC statement |

All new inputs are free and keyless: Binance public bulk files (data.binance.vision), the Deribit
public API, Coinbase Exchange public candles, and the Federal Reserve's published schedule
(scheduled meetings only, since only those are known in advance). Excluded and why:
tick-level large-trade imbalance (tens of GB per coin, beyond free compute), spot ETF flows (no free
licensed source), CPI dates (no free machine-readable source reachable from the pipeline).
If a source cannot be downloaded, its inputs are dropped from the tier and the report says so;
no replacement is chosen after seeing results.

**Model families.** Simple: ridge regression (penalized linear). Complex: XGBoost (gradient-boosted
trees). Tuning, refit schedule, costs and targets are the same as in v1. The v1 HAR benchmark stays the
yardstick for A1 to A3.

**Evaluation window.** All six cells per track are scored on the same out-of-sample period,
2023-01-01 to the latest data, so that the new inputs (most start in 2021) have at least a year of
training history. Before an input starts, its missing values are filled with the training median.

**Primary metric per track:** A, QLIKE of next-day volatility; B, weekly rank IC; C, squared error of the
next-4-hour return.

**Pairwise tests.** Per track, nine comparisons: F1 vs F0, F2 vs F0 and F2 vs F1 within each family (six),
and XGBoost vs ridge within each tier (three). The tests are Diebold-Mariano on loss differences
(A and C) and a Newey-West t-test on weekly IC differences (B). P-values are Holm-corrected within
the track; a difference counts at corrected p < 0.05.

**Absolute outcomes.** Each cell is also scored on the v1 rules A1 to A3, B1 to B2 and C1 to C2 within
the window. Because the window has four calendar years (2023 to 2026, 2026 partial), C2 requires
positive net return in at least 3 of the 4 years.

**Decision rule.** Order the cells from simplest to most complex: F0-ridge, F0-XGBoost, F1-ridge,
F1-XGBoost, F2-ridge, F2-XGBoost. A track's candidate is the simplest cell that passes the track's
primary absolute outcome (A1, B1 or C1) and is not significantly worse than the best cell on the
primary metric (Holm-corrected tests of the best cell against each other cell). The strategy outcomes
(A3, B2, C2) are reported per cell; a strategy feature needs its own pass. Without
such a cell the track has no candidate. A candidate joins the live test as a challenger to the frozen
v1 model; the live test decides.

**Stated in advance.** The 2023 to 2026 window was already used, as part of the v1 test, so v2
results are evidence, not proof. Only data arriving after the v2 code is committed is a clean test.

## Known biases stated in advance

- Survivorship: the coin list is today's large coins, which inflates historical altcoin returns in Track B.
- Spot fees only: no slippage, funding or borrowing costs, so short positions are not tested as tradable.
- Binance data only: other venues may differ.
