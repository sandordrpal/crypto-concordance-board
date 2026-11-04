# Live calibration of the board's typical-move ranges

Updated 2026-11-04 15:02 UTC. Rules and pass bands are fixed in [LIVE_TEST.md](https://github.com/sandordrpal/crypto-concordance-board/blob/main/research/LIVE_TEST.md) (R1-R4). Primary analysis: on-time forecasts from 2026-10-19; earlier rows are a run-in.

Coverage is the share of real moves that stayed inside the range. Confidence intervals (90%) are clustered by issue hour, because coins move together. PASS when the whole interval lies inside the band.

| Sample | Test | Horizon | Claimed | Forecasts | Issue hours | Coverage | 90% CI | Pass band | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| Primary (on time, from day 0) | R1 | next 1 h | 68% | 20050 | 398 | 73.1% | 70.2–76.1% | 63–73% | inconclusive |
| Primary (on time, from day 0) | R2 | next 1 h | 95% | 20050 | 398 | 96.6% | 95.4–97.8% | 92–98% | PASS |
| Primary (on time, from day 0) | R3 | next 24 h | 68% | 18950 | 376 | 76.2% | 68.8–83.7% | 63–73% | inconclusive |
| Primary (on time, from day 0) | R4 | next 24 h | 95% | 18950 | 376 | 96.3% | 93.5–99.0% | 92–98% | inconclusive |
| All rows from day 0, including back-filled | R1 | next 1 h | 68% | 21000 | 399 | 73.2% | 70.2–76.1% | 63–73% | inconclusive |
| All rows from day 0, including back-filled | R2 | next 1 h | 95% | 21000 | 399 | 96.6% | 95.4–97.8% | 92–98% | PASS |
| All rows from day 0, including back-filled | R3 | next 24 h | 68% | 19800 | 376 | 76.2% | 68.8–83.7% | 63–73% | inconclusive |
| All rows from day 0, including back-filled | R4 | next 24 h | 95% | 19800 | 376 | 96.3% | 93.5–99.0% | 92–98% | inconclusive |
| Run-in (before day 0) | R1 | next 1 h | 68% | 14250 | 281 | 71.0% | 67.6–74.5% | 63–73% | inconclusive |
| Run-in (before day 0) | R2 | next 1 h | 95% | 14250 | 281 | 95.2% | 93.6–96.8% | 92–98% | PASS |
| Run-in (before day 0) | R3 | next 24 h | 68% | 14250 | 281 | 72.1% | – | 63–73% | too few data yet |
| Run-in (before day 0) | R4 | next 24 h | 95% | 14250 | 281 | 97.3% | – | 92–98% | too few data yet |

Coins furthest from the 68% claim on the 24-hour range (primary sample):

| Coin | Coverage | Forecasts |
|---|---|---|
| TRX | 56% | 379 |
| PEPE | 62% | 379 |
| BTC | 64% | 379 |
| AAVE | 64% | 379 |
| BNB | 65% | 379 |
| SUI | 86% | 379 |
| ADA | 86% | 379 |
| QNT | 86% | 379 |
| ICP | 88% | 379 |
| FIL | 91% | 379 |

Information only, not investment advice.
