# Live test protocol

Registered 2026-10-09, before any live forecast was logged. Forecasts are written to the
[`live-log`](../../tree/live-log) branch before their outcome is known. That branch is only ever
appended to: no row is changed or deleted. The commit history is the audit trail.

Day 0 of the primary analysis is **2026-10-19 00:00 UTC**. Rows logged before day 0 are a run-in,
used to check the pipeline, and are reported separately.

## Part R: the board's typical-move ranges (registered 2026-10-09)

**What is tested.** The board's claim, in each coin's detail panel: "two in three moves of that length
stayed inside these ranges over the last 30 days", and one in twenty went beyond the outer figure.
The live test asks whether the ranges also hold for the *next* move.

**Frozen rule** (copied from `histCoin` in `index.html`, implemented in `live_ranges.py`). At the close of
each hour, for each coin, from the last 720 closed hourly Binance spot candles:

- 1-hour range: the 68th and 95th percentiles of the 720 absolute 1-hour log returns;
- 24-hour range: the 68th and 95th percentiles of the 720 overlapping absolute 24-hour log returns;
- percentiles by linear interpolation between order statistics; at least 100 values required.

**Coins.** The first 50 of the board's candidate list that are trading on Binance spot at the first logged run,
written to `universe.json`.

- A coin counts as trading only if it has a closed hourly candle in the last 3 hours.
- Before day 0, a coin that stops trading is replaced by the next candidate, and the change is recorded in `universe.json`.
- From day 0 the list is fixed: a coin that stops trading simply stops being scored.

*Amendment, 2026-10-09, during the run-in and before day 0:* the first run included TON. Its Binance USDT
market has had no trades since June 2026, and the board itself does not show it. The not-trading rule above
was added, and TON was replaced by the next candidate. Run-in rows for TON stay in the log but are excluded
from every analysis.

**Outcome.** A forecast issued at hour t is a hit when |log(close at t+h) − log(close at t)| is at or below the
range, for h = 1 and h = 24 hours.

| ID | Claim tested | Pass band for coverage |
|---|---|---|
| R1 | Next-1-hour move inside the 68% range | 63%–73% |
| R2 | Next-1-hour move inside the 95% range | 92%–98% |
| R3 | Next-24-hour move inside the 68% range | 63%–73% |
| R4 | Next-24-hour move inside the 95% range | 92%–98% |

**Statistics: an equivalence test, as in bioequivalence.** Coverage is computed per issue hour (the share of
coins inside their range), then averaged over hours. The 90% confidence interval uses Newey-West
variance with 6 lags (1-hour tests) or 24 lags (24-hour tests, because consecutive 24-hour windows overlap).
Clustering by hour accounts for coins moving together.

- **PASS:** the whole 90% interval lies inside the pass band (two one-sided tests at 5%).
- **FAIL:** the whole interval lies outside the band.
- **Inconclusive:** anything else.

No verdict is given before 7 days (R1, R2) or 14 days (R3, R4) of issue hours.

**Primary sample:** forecasts issued on time, within 59 minutes of the hour's close and before any part of the
outcome was known, from day 0. Hours missed by a delayed or skipped run are back-filled from past data
only, flagged `late`, and reported as a secondary sample. The rule uses only past prices, so back-filled rows
are valid but carry no timestamp proof.

**Readouts:** 1 month (2026-11-19) and 3 months (2027-01-19, final). Secondary, reported but not judged:

- coverage per coin;
- coverage in calm versus turbulent weeks (Bitcoin's 7-day realised volatility in thirds);
- up moves versus down moves.

**What a result changes.** If any R test FAILS at a readout, the board's wording is corrected to the measured
coverage ("in the live test, x in y moves stayed inside") within a week. If all four PASS at 3 months, the board
may say the ranges are live-tested. This is gate G2 in the plan, replacing the earlier placeholder of an
80% range.

## Part L: frozen forecasting models (registered 2026-10-11)

**Principle: nothing changes.** The two live candidates from version 2 (cell F0-ridge in both tracks) go
into the live test exactly as backtested, with the same inputs, model, refit schedule, tuning and training
window. What is frozen is the *recipe*, not the coefficients: models are refitted on schedule with new data,
exactly as in the walk-forward backtest that passed. Each refit is logged with its date, tuned penalty and
coefficients.

- **Frozen code:** commit `ae49efe` (2026-10-08) of `research/vol.py`, `research/xsec.py`, `research/v2.py`, `research/common.py`, `research/collect.py` and `research/collect_hf.py`.
- **Allowed later:** changes that only move these functions into a daily logger, without changing any calculation.
- **Not allowed:** any other change to inputs, model, schedule or tuning. That would start a new, separately registered challenger.

### L1: next-day Bitcoin volatility

| Item | Frozen setting |
|---|---|
| Target | Next UTC day's realized variance: sum of the 24 squared hourly log returns of Binance BTCUSDT spot |
| Inputs | The version 1 input set (tier F0, `vol.build`): HAR terms, downside and jump shares, absolute and negative return, weekend flag, volume z-score, taker flow imbalance, and the version 1 news, macro and sentiment series, each with its publication lag |
| Model | Ridge regression on standardized inputs (median fill, clipped at ±6), log-volatility target, smearing correction from validation residuals |
| Training window | All days from 2018-03-01 up to the refit date |
| Tuning | Penalty from the grid 10^−2 … 10^4 (13 values), chosen on the most recent 365 days before the refit, then refitted on all training days |
| Input availability | An input enters a refit if it has at least 100 training days (version 2 rule) |
| Refit schedule | Every 30 days, starting on day 0 (2026-10-19, 2026-11-18, …) |
| Forecast issued | Daily, after the UTC day closes, for the next UTC day, logged before that day's first hour closes |
| Benchmark | HAR (daily, weekly and monthly log volatility), ordinary least squares, re-estimated every day on a rolling 3-year window |
| Primary metric | QLIKE loss relative to HAR |
| Test | Diebold–Mariano on daily QLIKE differences (Newey–West, 1 lag), two-sided |
| Interim analyses | At 3, 6 and 9 months (2027-01-19, 2027-04-19, 2027-07-19). Success may be declared only at p < 0.001 (Haybittle–Peto boundary) |
| Final analysis | At 12 months (2026-10-19 to 2027-10-18): PASS if QLIKE is lower than HAR's with p < 0.05 |

### L2: weekly coin ranking

| Item | Frozen setting |
|---|---|
| Universe | Coins from the research list (`collect_hf.py`) with at least 120 days of hourly history and a 30-day median daily volume of at least $1 million at formation |
| Target | Rank of next-week (7-day) log return across eligible coins |
| Inputs | The 22 version 1 characteristics (`xsec.features`), rank-normalized across coins each week |
| Model | Ridge regression; penalty chosen from {1, 10, 100, 1,000, 10,000} on the most recent 26 weeks, then refitted on all earlier weeks |
| Refit schedule | Every 13 weeks, starting with the first live formation |
| Formation | Sunday close (00:00 UTC Monday). The first live formation is Sunday 2026-10-18, issued at day 0 |
| Primary metric | Weekly Spearman rank correlation (IC) between scores and next-week returns |
| Test | Mean IC > 0 with Newey–West t-statistic (4 lags) |
| Interim analysis | At 26 weeks (April 2027). Success may be declared only at p < 0.001 |
| Final analysis | After 48 weekly formations (around 2027-09-19): PASS if mean IC > 0 with t > 2 |
| Reported, not judged | Top-fifth portfolio against equal weight, after 0.10% cost per side |

### Stop rule (both models)

The rule is checked monthly:

- L1 is withdrawn if its rolling 90-day QLIKE ratio to HAR is above 1.00 at two consecutive monthly checks.
- L2 is withdrawn if its rolling 13-week mean IC is below 0 at two consecutive monthly checks.

A withdrawn model is removed from the board. Its forecasts continue to be logged and scored until the
final analysis, so the result is reported in full, as in an intention-to-treat analysis.

### What the results change

- **Interim success or a final pass:** the board may call the forecast *validated* (gates G4 and G5).
- **A final fail:** the claim is withdrawn and the failure is published.
