# Crypto Concordance Board: functions, tests and roadmap

*Last updated 9 October 2026. Information only, not investment advice.*

The Crypto Concordance Board is a free, live dashboard for 50 cryptocurrencies, with a public research
programme behind it. This page explains:

1. what the board does today;
2. which tests stand behind it, and how they work;
3. what was found so far;
4. which tests are running or planned, with their dates, expected results and pass/fail rules;
5. the roadmap for the next 12 months.

Every rule on this page was published *before* the test it governs, so it cannot be bent to fit the
results. If a test fails, we publish that too.

**Contents:** [1. What the board does](#1-what-the-board-does-today) ·
[2. How we test](#2-how-we-test-the-basis-of-every-test) ·
[3. Completed tests](#3-completed-tests-and-their-results) ·
[4. Live tests](#4-live-tests-running-and-planned) ·
[5. Calendar](#5-calendar-of-readouts) · [6. Roadmap](#6-roadmap) ·
[7. Stop rules](#7-what-would-change-the-plan) · [8. Links](#8-links)

---

## 1. What the board does today

Open the board at **[sandordrpal.github.io/crypto-concordance-board](https://sandordrpal.github.io/crypto-concordance-board/)**.
It runs entirely in your browser on free public data. Nothing is installed and nothing about you is stored.

| Function | What you see | How it works |
|---|---|---|
| **Coin list** | 50 coins, refreshed every 20 seconds | The board's candidate list of well-known coins, keeping the first 50 that trade on Binance spot. Gaps are filled by 24-hour trading volume |
| **Six signal votes per coin** | Up, down or neutral for trend, stretch, order flow, positioning, market tide and sentiment | Fixed rules, listed in the table below |
| **Net score** | −100 to +100 | Balance of up and down votes |
| **Discord score** | 0 (agreement) to 100 (even split) | How strongly the signals disagree |
| **State** | Aligned up, Leaning up, Split, Quiet, Leaning down, Aligned down | Combines the net and discord scores |
| **Typical size of the next move** | A ± range for the next hour and the next 24 hours, plus an outer range | From the coin's last 30 days: two in three past moves stayed inside the first range (68%), one in twenty went beyond the outer one (95%). Size only, not direction. Now under live test (section 4.1) |
| **Exchange cross-check** | Price gap between Binance, OKX and Bybit, in basis points (1 bp = 0.01%) | Flags unusual gaps between venues |
| **History test** | What each state was followed by over the past 30 days | Rebuilt without look-ahead, for context only |
| **Source status** | Which data feeds are live | Each source fails on its own; rate limits pause only that source |
| **Demo mode** | The full layout with simulated data | Add `#demo` to the address |
| **Support** | Buy Me a Coffee button and a Bitcoin address with a copy button and QR code | Donations only; nothing is unlocked by donating |

### The six signal votes

| Family | Votes up when | Votes down when |
|---|---|---|
| Trend | At least two more of four checks point up than down (24 h, 3 d and 7 d return; price against its 7-day average) | The same checks point down |
| Stretch | Price is at least 2 standard deviations below its 7-day average | At least 2 standard deviations above |
| Order flow | Buyers' share of 24-hour volume is in the top fifth of the last 20 days | In the bottom fifth |
| Positioning | Futures funding ≤ −0.01% | Funding ≥ +0.05% |
| Market tide | At least 65% of tracked coins are above their 7-day average | 35% or fewer are |
| Sentiment | Fear & Greed Index ≤ 25 | Fear & Greed Index ≥ 75 |

Stretch, positioning and sentiment are read as contrarian, by convention. **The voting rules are
heuristics and have not been validated.** The tested parts of the project are the ones in sections 3 and 4.

### Data sources

The board uses only free, keyless sources:

- **Binance:** spot prices, hourly candles and taker volume, plus futures funding and basis.
- **OKX and Bybit:** price cross-checks.
- **alternative.me:** the Crypto Fear & Greed Index.

The research pipeline adds free daily and hourly data:

- **Markets and macro:** FRED, US market indices, Coin Metrics community data.
- **News, attention and risk indices:** GDELT news tone, Wikipedia attention, policy-uncertainty and geopolitical-risk indices.
- **Derivatives and flows:** Binance futures bulk files, Deribit's DVOL volatility index, Coinbase prices.
- **Event calendars:** Federal Reserve meeting dates and CPI release dates.

---

## 2. How we test: the basis of every test

The approach borrows from clinical trials.

| Principle | What it means here |
|---|---|
| **Pre-registration** | The rule, the metric, the pass threshold and the comparison are committed to this repository before the test runs. The commit time is public proof. Files: [`research/OUTCOMES.md`](research/OUTCOMES.md) (history tests) and [`research/LIVE_TEST.md`](research/LIVE_TEST.md) (live tests) |
| **Out of sample only** | Models learn only from the past and are scored on data they never saw (walk-forward: refit, forecast the next period, move on) |
| **Costs included** | 0.10% per side on every trade, a typical exchange fee |
| **A fair benchmark** | Every forecast must beat a simple, well-known alternative: HAR for volatility, the random walk for returns, buy-and-hold for strategies |
| **Correct statistics** | Diebold–Mariano tests for forecast accuracy; Newey–West errors for overlapping data; Holm correction when many comparisons are made; equivalence tests for calibration |
| **Logged before the outcome** | Live forecasts are written, with a timestamp, to the append-only [`live-log`](../../tree/live-log) branch before the outcome is known. No row is ever changed |
| **Interim looks are strict** | Early readouts need p < 0.001, so looking early cannot manufacture a result |
| **Everything is published** | Passes and failures alike, on the [`research-results`](../../tree/research-results) and `live-log` branches |
| **Robust to one lucky week** | Crypto returns have very fat tails (Grobys et al., 2025). Strategy results must survive removing the single best and the single worst week |

**Key terms.**

- **HAR:** the textbook volatility model. It forecasts tomorrow's volatility from yesterday's, last week's and last month's.
- **QLIKE:** the standard error score for volatility forecasts (lower is better).
- **IC (information coefficient):** the weekly rank correlation between a ranking and what coins actually did next.
- **Sharpe ratio:** return per unit of risk.
- **Drawdown:** the fall from a peak to a later low.

---

## 3. Completed tests and their results

### 3.1 Daily direction of Bitcoin (2018–2026)

We asked whether models can predict Bitcoin's 1-, 7- and 30-day returns from about 47 daily variables:
macro, on-chain, news and sentiment. The models compared were ridge regression, polynomial regression,
XGBoost and a GRU neural network, with a 2024–2026 test period. **No model beat both the random walk and a
constant-drift forecast.** This is why the board shows risk and relative strength, not price predictions.

### 3.2 Version 1: three tracks on hourly data (walk-forward from 2021, after costs)

| ID | Goal | Pass rule (fixed in advance) | Result | Verdict |
|---|---|---|---|---|
| A1 | Forecast next-day Bitcoin volatility | Lower QLIKE than HAR, p < 0.05 | 12.4% lower than HAR (p < 0.001) | **Pass** |
| A2 | Forecast next-7-day volatility | Same as A1 | 2% lower, p = 0.63 | Fail |
| A3 | Hold less Bitcoin when risk is high | Sharpe above buy-and-hold **and** drawdown ≥ 25% smaller | Sharpe 0.48 vs 0.60; drawdown −70% vs −77% | Fail |
| B1 | Rank coins for the next week | Mean IC > 0 with t > 2 | IC +0.07 to +0.08, t 4.7–6.4 | **Pass** |
| B2 | Hold the top-ranked fifth | Beats equal weight after costs, t > 2 | t = 0.30 (costs of high turnover) | Fail |
| C1 | Forecast the next 4 hours | Better than random walk, p < 0.05, hit rate > 51% | R² +0.08%, p = 0.73 | Fail |
| C2 | Trade the 4-hour forecast | Beats buy-and-hold, positive in ≥ 4 of 6 years | Positive in 2 of 6 years | Fail |

### 3.3 Version 2: does more free data help? (2023–2026, after costs)

Three input sets were each tested with a simple model (ridge) and a complex one (XGBoost):

- **current inputs;**
- **current plus a few new inputs:** options-implied volatility, cross-coin volatility, trend and carry features;
- **current plus every other free input:** futures, positioning, the Coinbase premium, large trades, Fed and CPI days.

| Track | Range across the 6 combinations | Did more data help significantly? | Model chosen for the live test |
|---|---|---|---|
| Volatility | 0.82× to 0.91× HAR's loss, all pass A1 | No | Ridge on current inputs (0.873× HAR; also passes A2) |
| Coin ranking | IC +0.075 to +0.086, all pass B1 | No | Ridge on current inputs (IC +0.080) |
| Intraday | Best R² +0.17%, none pass C1 | No | None; track closed |

**Takeaway:** two things are forecastable, next-day volatility and relative strength across coins. Neither has
yet produced a trading strategy that beats simply holding after costs. More data did not change that, so the
simplest model goes forward.

Full reports: [scorecard](../../blob/research-results/README.md) · [version 2 volatility](../../blob/research-results/results/v2_volatility/REPORT.md) ·
[version 2 ranking](../../blob/research-results/results/v2_cross_section/REPORT.md).

---

## 4. Live tests: running and planned

Day 0 of the live programme is **19 October 2026, 00:00 UTC**. Anything logged before that is a run-in
period that checks the pipeline. It is reported separately and never counts.

### 4.1 Part R: are the board's typical-move ranges honest? (running since 9 October 2026)

Every hour, for 50 frozen coins, the board's exact range rule is logged *before* the next hour and day happen,
then scored once they have.

| ID | Claim tested | Pass if the 90% confidence interval of coverage lies within | Fail if it lies entirely outside | First verdict | Final verdict |
|---|---|---|---|---|---|
| R1 | Next-hour move inside the 68% range | 63%–73% | 63%–73% | 19 Nov 2026 | 19 Jan 2027 |
| R2 | Next-hour move inside the 95% range | 92%–98% | 92%–98% | 19 Nov 2026 | 19 Jan 2027 |
| R3 | Next-24-hour move inside the 68% range | 63%–73% | 63%–73% | 19 Nov 2026 | 19 Jan 2027 |
| R4 | Next-24-hour move inside the 95% range | 92%–98% | 92%–98% | 19 Nov 2026 | 19 Jan 2027 |

Coverage means the share of real moves that stayed inside the range. Any other outcome is *inconclusive*.

- **Before a verdict:** at least 7 days of data are needed for R1 and R2, and 14 days for R3 and R4.
- **Why an equivalence test:** it is the same logic as bioequivalence. The range passes only if it is shown to be close to its claim, not merely "not proven wrong".
- **Expected result:** the 1-hour ranges should land close to their claims. The 24-hour ranges may hold fewer moves than claimed when markets turn more volatile, because they are built from the past 30 days.
- **What happens next:** if a test fails, the board's wording changes within a week to the measured figure ("in the live test, x in 100 moves stayed inside"). If all four pass, the board may say the ranges are live-tested.
- **Live results:** [live-log/REPORT.md](../../blob/live-log/REPORT.md), updated hourly.

### 4.2 Part L: frozen forecasting models (to be registered before 19 October 2026)

| ID | What is tested | Benchmark | Pass rule | Interim checks | Expected verdict |
|---|---|---|---|---|---|
| L1 | Next-day Bitcoin volatility forecast (ridge, frozen) | HAR | Lower QLIKE than HAR: p < 0.001 at an interim check, or p < 0.05 at full length | 3 months (Jan 2027), 6 months (Apr 2027), 9 months (Jul 2027) | A first significant result is likely after 6–9 months; full statistical power takes about 14 months (Dec 2027) |
| L2 | Weekly coin ranking (ridge, frozen, 30 largest coins) | No information (IC = 0) | Mean IC > 0 with t > 2 over at least 40 weeks | 3, 6 and 9 months | Around weeks 47–49 (September 2027) |

- **Expected result:** the backtests point to about 12% better than HAR (L1) and an IC near +0.08 (L2). Live results are often weaker than backtests; we will report whatever happens.
- **Stop rule:** a model that does worse than its benchmark over a rolling 90 days, two months in a row, is withdrawn from the board until a new pre-registered test passes.

### 4.3 Part S: can the findings become a strategy that beats holding? (planned, version 3)

The backtests will be pre-registered in October 2026, and any survivor is paper-traded from day 0.
Paper trading means the trades are simulated and logged, with no real money. The benchmark is
buy-and-hold Bitcoin, plus an equal-weight basket of the 30 largest coins for the ranking strategies.

| ID | Strategy | Signal used | Pass rule (backtest and live) |
|---|---|---|---|
| S1 | Sell volatility (options) only when the market's expected volatility is well above our forecast | Volatility forecast vs DVOL | Higher Sharpe than always selling, with a smaller worst month; positive in most quarters |
| S2 | Hold Bitcoin; halve the position only when forecast risk is high *and* the trend is down | Volatility + trend | Sharpe above buy-and-hold **and** maximum drawdown at most 75% of buy-and-hold's |
| S3 | Risk-targeted holding, allowing up to 1.5× exposure in calm periods, including funding costs | Volatility forecast | Same as S2 |
| S4 | Hold the top third of the 30 largest coins; rebalance monthly; cap each coin at 10% | Ranking | Beats the equal-weight top-30 basket after costs with t > 2; turnover below 25% a month |
| S6 | S4 scaled by our volatility forecast, never more than 100% invested | Ranking + volatility | Sharpe above S4 and buy-and-hold; drawdown at most 75% of buy-and-hold's |

S5, long-short ranking, was dropped: published evidence shows single-coin spikes can wipe out the short side.

**Robustness rules for every strategy:**

- the result must hold after removing the single best week, and separately the single worst week;
- report bootstrap confidence intervals;
- the worst month must be no worse than buy-and-hold's;
- positive in at least 3 of 4 backtest years.

**Expected verdicts:** a 6-month live readout in April 2027 and a 12-month verdict in October 2027. A strategy
that passes is published as research only. This project does not sell trading signals.

---

## 5. Calendar of readouts

| Date | What happens |
|---|---|
| 9 Oct 2026 | Part R live logging starts (run-in) |
| by 19 Oct 2026 | Parts L and S registered; models frozen |
| **19 Oct 2026** | **Day 0**: primary analysis starts |
| early Nov 2026 | Board shows the frozen volatility gauge and the top-10 ranking, each with its live track record |
| 19 Nov 2026 | First Part R verdicts (R1–R4) |
| 19 Jan 2027 | Final Part R verdicts; 3-month interim check of L1 and L2 (stop rule) |
| 19 Apr 2027 | 6-month interim: L1 can be declared validated at p < 0.001; first strategy readout |
| 19 Jul 2027 | 9-month readout |
| Sep 2027 | L2 ranking verdict (weeks 47–49) |
| Oct 2027 | 12-month report: L1, L2 and strategy verdicts; version 1.0 decision |

---

## 6. Roadmap

| Phase | When | What is delivered | Gate before the next phase |
|---|---|---|---|
| 1 Freeze and run-in | 9–31 Oct 2026 | Live range test (done); frozen models; daily forecast log; strategy pre-registration | **G0** models frozen and registered before day 0 · **G1** board live with logged forecasts |
| 2 Public beta | Nov–mid Dec 2026 | Risk gauge and top-10 relative strength on the board, with live track records; feedback from early users | **G2** Part R first verdicts published |
| 3 Groundwork for a paid tier | mid Dec 2026–Jan 2027 | Alerts (Telegram and email), position-size calculator, weekly risk report; data sources licensed for commercial use; legal review | **G3** 3-month checks: no stop rule triggered, Part R final verdicts, legal review complete |
| 4 Pro tier (if G3 passes) | from late Jan 2027 | Optional paid tier for information and tools, clearly labelled "live track record in progress". The free board stays free | Paid features show their live record and are withdrawn under the stop rule |
| 5 Validate | Apr–Jul 2027 | Volatility verdict; per-coin volatility forecasts pre-registered | **G4** L1 validated, or the claim withdrawn |
| 6 Confirm and decide | Jul–Oct 2027 | Ranking verdict; 12-month report; write-up for publication | **G5** L2 verdict · **G6** version 1.0 decision |

**What will not be built:**

- no trading signals or "buy/sell" calls;
- no managed money;
- no price predictions.

These would need regulatory licences (EU MiCA), and the evidence does not support them.

---

## 7. What would change the plan

| Event | Response |
|---|---|
| A Part R test fails | The board's wording is corrected to the measured coverage |
| L1 or L2 triggers the stop rule | That forecast is removed from the board and the failure is published |
| L1 or L2 fails at full length | The claim is withdrawn; the free board continues without it |
| A strategy passes only because of one week | It fails under the robustness rules |
| A data source becomes unavailable | It is dropped and reported; no replacement is chosen after seeing results |

---

## 8. Links

| | |
|---|---|
| Live board | [sandordrpal.github.io/crypto-concordance-board](https://sandordrpal.github.io/crypto-concordance-board/) |
| History-test rules | [`research/OUTCOMES.md`](research/OUTCOMES.md) |
| Live-test rules | [`research/LIVE_TEST.md`](research/LIVE_TEST.md) |
| History-test results | [`research-results` branch](../../tree/research-results) |
| Live log and report | [`live-log` branch](../../tree/live-log) · [REPORT.md](../../blob/live-log/REPORT.md) |
| Support the project | [buymeacoffee.com/palsandormd](https://buymeacoffee.com/palsandormd) · Bitcoin `3Mw3zMyh7wsQ3qaQNjWtmA4zeFoJNnRENf` |

**References:**

- Corsi (2009), HAR volatility model.
- Grobys, Kolari, Sandretto, Shahzad & Äijö (2025), *Cryptocurrency momentum has (not) its moments*, Financial Markets and Portfolio Management.
- Fieberg et al. (2025), *A trend factor for the cross section of cryptocurrency returns*, JFQA.
- Moreira & Muir (2017), *Volatility-managed portfolios*, Journal of Finance.
- BIS Working Paper 1087, *Crypto carry*.
