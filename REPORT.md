# Live calibration of the board's typical-move ranges

Updated 2026-11-06 02:02 UTC. Rules and pass bands are fixed in [LIVE_TEST.md](https://github.com/sandordrpal/crypto-concordance-board/blob/main/research/LIVE_TEST.md) (R1-R4). Primary analysis: on-time forecasts from 2026-10-19; earlier rows are a run-in.

Coverage is the share of real moves that stayed inside the range. Confidence intervals (90%) are clustered by issue hour, because coins move together. PASS when the whole interval lies inside the band.

| Sample | Test | Horizon | Claimed | Forecasts | Issue hours | Coverage | 90% CI | Pass band | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| Primary (on time, from day 0) | R1 | next 1 h | 68% | 21850 | 433 | 71.5% | 68.4–74.5% | 63–73% | inconclusive |
| Primary (on time, from day 0) | R2 | next 1 h | 95% | 21850 | 433 | 96.1% | 94.8–97.4% | 92–98% | PASS |
| Primary (on time, from day 0) | R3 | next 24 h | 68% | 20650 | 410 | 73.0% | 65.3–80.8% | 63–73% | inconclusive |
| Primary (on time, from day 0) | R4 | next 24 h | 95% | 20650 | 410 | 95.4% | 92.6–98.2% | 92–98% | inconclusive |
| All rows from day 0, including back-filled | R1 | next 1 h | 68% | 22900 | 434 | 71.5% | 68.4–74.5% | 63–73% | inconclusive |
| All rows from day 0, including back-filled | R2 | next 1 h | 95% | 22900 | 434 | 96.1% | 94.8–97.4% | 92–98% | PASS |
| All rows from day 0, including back-filled | R3 | next 24 h | 68% | 21650 | 411 | 73.0% | 65.3–80.7% | 63–73% | inconclusive |
| All rows from day 0, including back-filled | R4 | next 24 h | 95% | 21650 | 411 | 95.4% | 92.6–98.1% | 92–98% | inconclusive |
| Run-in (before day 0) | R1 | next 1 h | 68% | 14250 | 281 | 71.0% | 67.6–74.5% | 63–73% | inconclusive |
| Run-in (before day 0) | R2 | next 1 h | 95% | 14250 | 281 | 95.2% | 93.6–96.8% | 92–98% | PASS |
| Run-in (before day 0) | R3 | next 24 h | 68% | 14250 | 281 | 72.1% | – | 63–73% | too few data yet |
| Run-in (before day 0) | R4 | next 24 h | 95% | 14250 | 281 | 97.3% | – | 92–98% | too few data yet |

Coins furthest from the 68% claim on the 24-hour range (primary sample):

| Coin | Coverage | Forecasts |
|---|---|---|
| TRX | 55% | 413 |
| BTC | 59% | 413 |
| BNB | 60% | 413 |
| ETH | 61% | 413 |
| PEPE | 63% | 413 |
| DOT | 82% | 413 |
| IMX | 82% | 413 |
| FET | 82% | 413 |
| ICP | 82% | 413 |
| FIL | 88% | 413 |

Information only, not investment advice.
