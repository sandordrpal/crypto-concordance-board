# Live calibration of the board's typical-move ranges

Updated 2026-11-03 08:02 UTC. Rules and pass bands are fixed in [LIVE_TEST.md](https://github.com/sandordrpal/crypto-concordance-board/blob/main/research/LIVE_TEST.md) (R1-R4). Primary analysis: on-time forecasts from 2026-10-19; earlier rows are a run-in.

Coverage is the share of real moves that stayed inside the range. Confidence intervals (90%) are clustered by issue hour, because coins move together. PASS when the whole interval lies inside the band.

| Sample | Test | Horizon | Claimed | Forecasts | Issue hours | Coverage | 90% CI | Pass band | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| Primary (on time, from day 0) | R1 | next 1 h | 68% | 18550 | 368 | 74.0% | 71.0–77.0% | 63–73% | inconclusive |
| Primary (on time, from day 0) | R2 | next 1 h | 95% | 18550 | 368 | 96.8% | 95.6–98.0% | 92–98% | inconclusive |
| Primary (on time, from day 0) | R3 | next 24 h | 68% | 17400 | 345 | 75.4% | 67.3–83.5% | 63–73% | inconclusive |
| Primary (on time, from day 0) | R4 | next 24 h | 95% | 17400 | 345 | 96.1% | 93.1–99.0% | 92–98% | inconclusive |
| All rows from day 0, including back-filled | R1 | next 1 h | 68% | 19400 | 368 | 74.0% | 71.0–77.0% | 63–73% | inconclusive |
| All rows from day 0, including back-filled | R2 | next 1 h | 95% | 19400 | 368 | 96.8% | 95.6–98.0% | 92–98% | inconclusive |
| All rows from day 0, including back-filled | R3 | next 24 h | 68% | 18200 | 345 | 75.4% | 67.3–83.5% | 63–73% | inconclusive |
| All rows from day 0, including back-filled | R4 | next 24 h | 95% | 18200 | 345 | 96.1% | 93.1–99.0% | 92–98% | inconclusive |
| Run-in (before day 0) | R1 | next 1 h | 68% | 14250 | 281 | 71.0% | 67.6–74.5% | 63–73% | inconclusive |
| Run-in (before day 0) | R2 | next 1 h | 95% | 14250 | 281 | 95.2% | 93.6–96.8% | 92–98% | PASS |
| Run-in (before day 0) | R3 | next 24 h | 68% | 14250 | 281 | 72.1% | – | 63–73% | too few data yet |
| Run-in (before day 0) | R4 | next 24 h | 95% | 14250 | 281 | 97.3% | – | 92–98% | too few data yet |

Coins furthest from the 68% claim on the 24-hour range (primary sample):

| Coin | Coverage | Forecasts |
|---|---|---|
| TRX | 59% | 348 |
| PEPE | 61% | 348 |
| AAVE | 62% | 348 |
| BNB | 63% | 348 |
| VET | 64% | 348 |
| QNT | 85% | 348 |
| ALGO | 85% | 348 |
| SUI | 86% | 348 |
| ICP | 86% | 348 |
| FIL | 90% | 348 |

Information only, not investment advice.
