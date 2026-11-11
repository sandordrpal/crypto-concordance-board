# Live calibration of the board's typical-move ranges

Updated 2026-11-11 05:02 UTC. Rules and pass bands are fixed in [LIVE_TEST.md](https://github.com/sandordrpal/crypto-concordance-board/blob/main/research/LIVE_TEST.md) (R1-R4). Primary analysis: on-time forecasts from 2026-10-19; earlier rows are a run-in.

Coverage is the share of real moves that stayed inside the range. Confidence intervals (90%) are clustered by issue hour, because coins move together. PASS when the whole interval lies inside the band.

| Sample | Test | Horizon | Claimed | Forecasts | Issue hours | Coverage | 90% CI | Pass band | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| Primary (on time, from day 0) | R1 | next 1 h | 68% | 28050 | 556 | 72.3% | 69.6–75.0% | 63–73% | inconclusive |
| Primary (on time, from day 0) | R2 | next 1 h | 95% | 28050 | 556 | 96.2% | 95.0–97.3% | 92–98% | PASS |
| Primary (on time, from day 0) | R3 | next 24 h | 68% | 26900 | 533 | 73.6% | 66.9–80.4% | 63–73% | inconclusive |
| Primary (on time, from day 0) | R4 | next 24 h | 95% | 26900 | 533 | 95.7% | 93.3–98.1% | 92–98% | inconclusive |
| All rows from day 0, including back-filled | R1 | next 1 h | 68% | 29350 | 557 | 72.4% | 69.7–75.1% | 63–73% | inconclusive |
| All rows from day 0, including back-filled | R2 | next 1 h | 95% | 29350 | 557 | 96.2% | 95.0–97.3% | 92–98% | PASS |
| All rows from day 0, including back-filled | R3 | next 24 h | 68% | 28150 | 534 | 73.6% | 66.9–80.3% | 63–73% | inconclusive |
| All rows from day 0, including back-filled | R4 | next 24 h | 95% | 28150 | 534 | 95.7% | 93.3–98.1% | 92–98% | inconclusive |
| Run-in (before day 0) | R1 | next 1 h | 68% | 14250 | 281 | 71.0% | 67.6–74.5% | 63–73% | inconclusive |
| Run-in (before day 0) | R2 | next 1 h | 95% | 14250 | 281 | 95.2% | 93.6–96.8% | 92–98% | PASS |
| Run-in (before day 0) | R3 | next 24 h | 68% | 14250 | 281 | 72.1% | – | 63–73% | too few data yet |
| Run-in (before day 0) | R4 | next 24 h | 95% | 14250 | 281 | 97.3% | – | 92–98% | too few data yet |

Coins furthest from the 68% claim on the 24-hour range (primary sample):

| Coin | Coverage | Forecasts |
|---|---|---|
| ETH | 60% | 538 |
| BTC | 60% | 538 |
| TRX | 61% | 538 |
| XRP | 62% | 538 |
| BNB | 63% | 538 |
| TIA | 82% | 538 |
| FET | 83% | 538 |
| DOT | 83% | 538 |
| OP | 83% | 538 |
| FIL | 86% | 538 |

Information only, not investment advice.
