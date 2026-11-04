# Live calibration of the board's typical-move ranges

Updated 2026-11-04 12:02 UTC. Rules and pass bands are fixed in [LIVE_TEST.md](https://github.com/sandordrpal/crypto-concordance-board/blob/main/research/LIVE_TEST.md) (R1-R4). Primary analysis: on-time forecasts from 2026-10-19; earlier rows are a run-in.

Coverage is the share of real moves that stayed inside the range. Confidence intervals (90%) are clustered by issue hour, because coins move together. PASS when the whole interval lies inside the band.

| Sample | Test | Horizon | Claimed | Forecasts | Issue hours | Coverage | 90% CI | Pass band | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| Primary (on time, from day 0) | R1 | next 1 h | 68% | 19900 | 395 | 73.4% | 70.5–76.4% | 63–73% | inconclusive |
| Primary (on time, from day 0) | R2 | next 1 h | 95% | 19900 | 395 | 96.8% | 95.6–98.0% | 92–98% | PASS |
| Primary (on time, from day 0) | R3 | next 24 h | 68% | 18800 | 373 | 76.2% | 68.7–83.7% | 63–73% | inconclusive |
| Primary (on time, from day 0) | R4 | next 24 h | 95% | 18800 | 373 | 96.3% | 93.5–99.0% | 92–98% | inconclusive |
| All rows from day 0, including back-filled | R1 | next 1 h | 68% | 20850 | 396 | 73.5% | 70.5–76.4% | 63–73% | inconclusive |
| All rows from day 0, including back-filled | R2 | next 1 h | 95% | 20850 | 396 | 96.8% | 95.6–98.0% | 92–98% | PASS |
| All rows from day 0, including back-filled | R3 | next 24 h | 68% | 19650 | 373 | 76.2% | 68.7–83.7% | 63–73% | inconclusive |
| All rows from day 0, including back-filled | R4 | next 24 h | 95% | 19650 | 373 | 96.3% | 93.5–99.0% | 92–98% | inconclusive |
| Run-in (before day 0) | R1 | next 1 h | 68% | 14250 | 281 | 71.0% | 67.6–74.5% | 63–73% | inconclusive |
| Run-in (before day 0) | R2 | next 1 h | 95% | 14250 | 281 | 95.2% | 93.6–96.8% | 92–98% | PASS |
| Run-in (before day 0) | R3 | next 24 h | 68% | 14250 | 281 | 72.1% | – | 63–73% | too few data yet |
| Run-in (before day 0) | R4 | next 24 h | 95% | 14250 | 281 | 97.3% | – | 92–98% | too few data yet |

Coins furthest from the 68% claim on the 24-hour range (primary sample):

| Coin | Coverage | Forecasts |
|---|---|---|
| TRX | 57% | 376 |
| PEPE | 62% | 376 |
| BTC | 64% | 376 |
| AAVE | 64% | 376 |
| BNB | 65% | 376 |
| ADA | 86% | 376 |
| SUI | 86% | 376 |
| QNT | 86% | 376 |
| ICP | 88% | 376 |
| FIL | 90% | 376 |

Information only, not investment advice.
