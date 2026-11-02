# Live calibration of the board's typical-move ranges

Updated 2026-11-02 16:02 UTC. Rules and pass bands are fixed in [LIVE_TEST.md](https://github.com/sandordrpal/crypto-concordance-board/blob/main/research/LIVE_TEST.md) (R1-R4). Primary analysis: on-time forecasts from 2026-10-19; earlier rows are a run-in.

Coverage is the share of real moves that stayed inside the range. Confidence intervals (90%) are clustered by issue hour, because coins move together. PASS when the whole interval lies inside the band.

| Sample | Test | Horizon | Claimed | Forecasts | Issue hours | Coverage | 90% CI | Pass band | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| Primary (on time, from day 0) | R1 | next 1 h | 68% | 17750 | 352 | 74.0% | 70.9–77.1% | 63–73% | inconclusive |
| Primary (on time, from day 0) | R2 | next 1 h | 95% | 17750 | 352 | 96.7% | 95.4–98.0% | 92–98% | PASS |
| Primary (on time, from day 0) | R3 | next 24 h | 68% | 16600 | 329 | 76.2% | – | 63–73% | too few data yet |
| Primary (on time, from day 0) | R4 | next 24 h | 95% | 16600 | 329 | 95.9% | – | 92–98% | too few data yet |
| All rows from day 0, including back-filled | R1 | next 1 h | 68% | 18550 | 352 | 74.0% | 70.9–77.1% | 63–73% | inconclusive |
| All rows from day 0, including back-filled | R2 | next 1 h | 95% | 18550 | 352 | 96.7% | 95.4–98.0% | 92–98% | PASS |
| All rows from day 0, including back-filled | R3 | next 24 h | 68% | 17350 | 329 | 76.2% | – | 63–73% | too few data yet |
| All rows from day 0, including back-filled | R4 | next 24 h | 95% | 17350 | 329 | 95.9% | – | 92–98% | too few data yet |
| Run-in (before day 0) | R1 | next 1 h | 68% | 14250 | 281 | 71.0% | 67.6–74.5% | 63–73% | inconclusive |
| Run-in (before day 0) | R2 | next 1 h | 95% | 14250 | 281 | 95.2% | 93.6–96.8% | 92–98% | PASS |
| Run-in (before day 0) | R3 | next 24 h | 68% | 14250 | 281 | 72.1% | – | 63–73% | too few data yet |
| Run-in (before day 0) | R4 | next 24 h | 95% | 14250 | 281 | 97.3% | – | 92–98% | too few data yet |

Coins furthest from the 68% claim on the 24-hour range (primary sample):

| Coin | Coverage | Forecasts |
|---|---|---|
| PEPE | 61% | 332 |
| TRX | 61% | 332 |
| VET | 62% | 332 |
| AAVE | 65% | 332 |
| BNB | 65% | 332 |
| QNT | 85% | 332 |
| XLM | 86% | 332 |
| SUI | 86% | 332 |
| ICP | 87% | 332 |
| FIL | 89% | 332 |

Information only, not investment advice.
