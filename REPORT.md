# Live calibration of the board's typical-move ranges

Updated 2026-11-08 20:02 UTC. Rules and pass bands are fixed in [LIVE_TEST.md](https://github.com/sandordrpal/crypto-concordance-board/blob/main/research/LIVE_TEST.md) (R1-R4). Primary analysis: on-time forecasts from 2026-10-19; earlier rows are a run-in.

Coverage is the share of real moves that stayed inside the range. Confidence intervals (90%) are clustered by issue hour, because coins move together. PASS when the whole interval lies inside the band.

| Sample | Test | Horizon | Claimed | Forecasts | Issue hours | Coverage | 90% CI | Pass band | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| Primary (on time, from day 0) | R1 | next 1 h | 68% | 25200 | 499 | 73.0% | 70.2–75.8% | 63–73% | inconclusive |
| Primary (on time, from day 0) | R2 | next 1 h | 95% | 25200 | 499 | 96.6% | 95.4–97.7% | 92–98% | PASS |
| Primary (on time, from day 0) | R3 | next 24 h | 68% | 24050 | 476 | 73.9% | 66.3–81.5% | 63–73% | inconclusive |
| Primary (on time, from day 0) | R4 | next 24 h | 95% | 24050 | 476 | 95.5% | 92.8–98.1% | 92–98% | inconclusive |
| All rows from day 0, including back-filled | R1 | next 1 h | 68% | 26350 | 500 | 73.1% | 70.3–75.8% | 63–73% | inconclusive |
| All rows from day 0, including back-filled | R2 | next 1 h | 95% | 26350 | 500 | 96.6% | 95.4–97.7% | 92–98% | PASS |
| All rows from day 0, including back-filled | R3 | next 24 h | 68% | 25150 | 477 | 73.9% | 66.4–81.4% | 63–73% | inconclusive |
| All rows from day 0, including back-filled | R4 | next 24 h | 95% | 25150 | 477 | 95.5% | 92.8–98.1% | 92–98% | inconclusive |
| Run-in (before day 0) | R1 | next 1 h | 68% | 14250 | 281 | 71.0% | 67.6–74.5% | 63–73% | inconclusive |
| Run-in (before day 0) | R2 | next 1 h | 95% | 14250 | 281 | 95.2% | 93.6–96.8% | 92–98% | PASS |
| Run-in (before day 0) | R3 | next 24 h | 68% | 14250 | 281 | 72.1% | – | 63–73% | too few data yet |
| Run-in (before day 0) | R4 | next 24 h | 95% | 14250 | 281 | 97.3% | – | 92–98% | too few data yet |

Coins furthest from the 68% claim on the 24-hour range (primary sample):

| Coin | Coverage | Forecasts |
|---|---|---|
| TRX | 60% | 481 |
| BCH | 62% | 481 |
| BTC | 62% | 481 |
| BNB | 63% | 481 |
| ETH | 64% | 481 |
| FET | 82% | 481 |
| IMX | 82% | 481 |
| ICP | 82% | 481 |
| DOT | 83% | 481 |
| FIL | 86% | 481 |

Information only, not investment advice.
