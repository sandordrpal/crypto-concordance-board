# Live calibration of the board's typical-move ranges

Updated 2026-11-03 03:02 UTC. Rules and pass bands are fixed in [LIVE_TEST.md](https://github.com/sandordrpal/crypto-concordance-board/blob/main/research/LIVE_TEST.md) (R1-R4). Primary analysis: on-time forecasts from 2026-10-19; earlier rows are a run-in.

Coverage is the share of real moves that stayed inside the range. Confidence intervals (90%) are clustered by issue hour, because coins move together. PASS when the whole interval lies inside the band.

| Sample | Test | Horizon | Claimed | Forecasts | Issue hours | Coverage | 90% CI | Pass band | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| Primary (on time, from day 0) | R1 | next 1 h | 68% | 18300 | 363 | 73.9% | 70.9–76.9% | 63–73% | inconclusive |
| Primary (on time, from day 0) | R2 | next 1 h | 95% | 18300 | 363 | 96.8% | 95.5–98.0% | 92–98% | inconclusive |
| Primary (on time, from day 0) | R3 | next 24 h | 68% | 17150 | 340 | 75.8% | 67.6–84.0% | 63–73% | inconclusive |
| Primary (on time, from day 0) | R4 | next 24 h | 95% | 17150 | 340 | 96.0% | 93.0–99.0% | 92–98% | inconclusive |
| All rows from day 0, including back-filled | R1 | next 1 h | 68% | 19150 | 363 | 73.9% | 70.9–76.9% | 63–73% | inconclusive |
| All rows from day 0, including back-filled | R2 | next 1 h | 95% | 19150 | 363 | 96.8% | 95.5–98.0% | 92–98% | inconclusive |
| All rows from day 0, including back-filled | R3 | next 24 h | 68% | 17950 | 340 | 75.8% | 67.6–84.0% | 63–73% | inconclusive |
| All rows from day 0, including back-filled | R4 | next 24 h | 95% | 17950 | 340 | 96.0% | 93.0–99.0% | 92–98% | inconclusive |
| Run-in (before day 0) | R1 | next 1 h | 68% | 14250 | 281 | 71.0% | 67.6–74.5% | 63–73% | inconclusive |
| Run-in (before day 0) | R2 | next 1 h | 95% | 14250 | 281 | 95.2% | 93.6–96.8% | 92–98% | PASS |
| Run-in (before day 0) | R3 | next 24 h | 68% | 14250 | 281 | 72.1% | – | 63–73% | too few data yet |
| Run-in (before day 0) | R4 | next 24 h | 95% | 14250 | 281 | 97.3% | – | 92–98% | too few data yet |

Coins furthest from the 68% claim on the 24-hour range (primary sample):

| Coin | Coverage | Forecasts |
|---|---|---|
| TRX | 59% | 343 |
| PEPE | 61% | 343 |
| AAVE | 63% | 343 |
| VET | 63% | 343 |
| BNB | 64% | 343 |
| XLM | 85% | 343 |
| QNT | 85% | 343 |
| SUI | 86% | 343 |
| ICP | 87% | 343 |
| FIL | 90% | 343 |

Information only, not investment advice.
