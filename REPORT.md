# Live calibration of the board's typical-move ranges

Updated 2026-10-30 22:02 UTC. Rules and pass bands are fixed in [LIVE_TEST.md](https://github.com/sandordrpal/crypto-concordance-board/blob/main/research/LIVE_TEST.md) (R1-R4). Primary analysis: on-time forecasts from 2026-10-19; earlier rows are a run-in.

Coverage is the share of real moves that stayed inside the range. Confidence intervals (90%) are clustered by issue hour, because coins move together. PASS when the whole interval lies inside the band.

| Sample | Test | Horizon | Claimed | Forecasts | Issue hours | Coverage | 90% CI | Pass band | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| Primary (on time, from day 0) | R1 | next 1 h | 68% | 14450 | 286 | 72.5% | 69.0–76.0% | 63–73% | inconclusive |
| Primary (on time, from day 0) | R2 | next 1 h | 95% | 14450 | 286 | 96.2% | 94.6–97.8% | 92–98% | PASS |
| Primary (on time, from day 0) | R3 | next 24 h | 68% | 13300 | 263 | 73.9% | – | 63–73% | too few data yet |
| Primary (on time, from day 0) | R4 | next 24 h | 95% | 13300 | 263 | 95.6% | – | 92–98% | too few data yet |
| All rows from day 0, including back-filled | R1 | next 1 h | 68% | 15100 | 286 | 72.5% | 69.0–76.0% | 63–73% | inconclusive |
| All rows from day 0, including back-filled | R2 | next 1 h | 95% | 15100 | 286 | 96.2% | 94.6–97.8% | 92–98% | PASS |
| All rows from day 0, including back-filled | R3 | next 24 h | 68% | 13900 | 263 | 73.9% | – | 63–73% | too few data yet |
| All rows from day 0, including back-filled | R4 | next 24 h | 95% | 13900 | 263 | 95.6% | – | 92–98% | too few data yet |
| Run-in (before day 0) | R1 | next 1 h | 68% | 14250 | 281 | 71.0% | 67.6–74.5% | 63–73% | inconclusive |
| Run-in (before day 0) | R2 | next 1 h | 95% | 14250 | 281 | 95.2% | 93.6–96.8% | 92–98% | PASS |
| Run-in (before day 0) | R3 | next 24 h | 68% | 14250 | 281 | 72.1% | – | 63–73% | too few data yet |
| Run-in (before day 0) | R4 | next 24 h | 95% | 14250 | 281 | 97.3% | – | 92–98% | too few data yet |

Coins furthest from the 68% claim on the 24-hour range (primary sample):

| Coin | Coverage | Forecasts |
|---|---|---|
| PEPE | 54% | 266 |
| VET | 54% | 266 |
| ETH | 58% | 266 |
| BTC | 60% | 266 |
| BNB | 60% | 266 |
| QNT | 84% | 266 |
| SUI | 85% | 266 |
| POL | 85% | 266 |
| ICP | 86% | 266 |
| FIL | 88% | 266 |

Information only, not investment advice.
