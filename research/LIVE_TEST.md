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

**Coins.** The first 50 of the board's candidate list that Binance lists at the first logged run, written to
`universe.json` and never changed.

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

## Part L: frozen forecasting models (to be registered before day 0)

The volatility model (ridge on the version 1 inputs, live candidate from version 2) and the coin-ranking model
(same) will be frozen here with their commit hash, metrics, interim thresholds and the stop rule, before
2026-10-19.
