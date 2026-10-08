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

## Known biases stated in advance

- Survivorship: the coin list is today's large coins, which inflates historical altcoin returns in Track B.
- Spot fees only: no slippage, funding or borrowing costs, so short positions are not tested as tradable.
- Binance data only: other venues may differ.
