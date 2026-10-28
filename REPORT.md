# Live calibration of the board's typical-move ranges

Updated 2026-10-28 22:02 UTC. Rules and pass bands are fixed in [LIVE_TEST.md](https://github.com/sandordrpal/crypto-concordance-board/blob/main/research/LIVE_TEST.md) (R1-R4). Primary analysis: on-time forecasts from 2026-10-19; earlier rows are a run-in.

Coverage is the share of real moves that stayed inside the range. Confidence intervals (90%) are clustered by issue hour, because coins move together. PASS when the whole interval lies inside the band.

| Sample | Test | Horizon | Claimed | Forecasts | Issue hours | Coverage | 90% CI | Pass band | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| Primary (on time, from day 0) | R1 | next 1 h | 68% | 12050 | 238 | 76.2% | 73.1–79.3% | 63–73% | FAIL |
| Primary (on time, from day 0) | R2 | next 1 h | 95% | 12050 | 238 | 97.7% | 96.5–98.9% | 92–98% | inconclusive |
| Primary (on time, from day 0) | R3 | next 24 h | 68% | 10900 | 215 | 79.0% | – | 63–73% | too few data yet |
| Primary (on time, from day 0) | R4 | next 24 h | 95% | 10900 | 215 | 98.5% | – | 92–98% | too few data yet |
| All rows from day 0, including back-filled | R1 | next 1 h | 68% | 12600 | 238 | 76.2% | 73.1–79.3% | 63–73% | FAIL |
| All rows from day 0, including back-filled | R2 | next 1 h | 95% | 12600 | 238 | 97.7% | 96.5–98.9% | 92–98% | inconclusive |
| All rows from day 0, including back-filled | R3 | next 24 h | 68% | 11400 | 215 | 79.0% | – | 63–73% | too few data yet |
| All rows from day 0, including back-filled | R4 | next 24 h | 95% | 11400 | 215 | 98.5% | – | 92–98% | too few data yet |
| Run-in (before day 0) | R1 | next 1 h | 68% | 14250 | 281 | 71.0% | 67.6–74.5% | 63–73% | inconclusive |
| Run-in (before day 0) | R2 | next 1 h | 95% | 14250 | 281 | 95.2% | 93.6–96.8% | 92–98% | PASS |
| Run-in (before day 0) | R3 | next 24 h | 68% | 14250 | 281 | 72.1% | – | 63–73% | too few data yet |
| Run-in (before day 0) | R4 | next 24 h | 95% | 14250 | 281 | 97.3% | – | 92–98% | too few data yet |

Coins furthest from the 68% claim on the 24-hour range (primary sample):

| Coin | Coverage | Forecasts |
|---|---|---|
| PEPE | 55% | 218 |
| VET | 61% | 218 |
| BCH | 62% | 218 |
| ETH | 63% | 218 |
| BNB | 66% | 218 |
| TIA | 90% | 218 |
| AVAX | 90% | 218 |
| IMX | 92% | 218 |
| ALGO | 93% | 218 |
| FIL | 94% | 218 |

Information only, not investment advice.
