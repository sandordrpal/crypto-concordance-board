# Live calibration of the board's typical-move ranges

Updated 2026-10-29 01:02 UTC. Rules and pass bands are fixed in [LIVE_TEST.md](https://github.com/sandordrpal/crypto-concordance-board/blob/main/research/LIVE_TEST.md) (R1-R4). Primary analysis: on-time forecasts from 2026-10-19; earlier rows are a run-in.

Coverage is the share of real moves that stayed inside the range. Confidence intervals (90%) are clustered by issue hour, because coins move together. PASS when the whole interval lies inside the band.

| Sample | Test | Horizon | Claimed | Forecasts | Issue hours | Coverage | 90% CI | Pass band | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| Primary (on time, from day 0) | R1 | next 1 h | 68% | 12200 | 241 | 76.2% | 73.1–79.2% | 63–73% | FAIL |
| Primary (on time, from day 0) | R2 | next 1 h | 95% | 12200 | 241 | 97.7% | 96.6–98.9% | 92–98% | inconclusive |
| Primary (on time, from day 0) | R3 | next 24 h | 68% | 11050 | 218 | 79.2% | – | 63–73% | too few data yet |
| Primary (on time, from day 0) | R4 | next 24 h | 95% | 11050 | 218 | 98.5% | – | 92–98% | too few data yet |
| All rows from day 0, including back-filled | R1 | next 1 h | 68% | 12800 | 241 | 76.2% | 73.1–79.2% | 63–73% | FAIL |
| All rows from day 0, including back-filled | R2 | next 1 h | 95% | 12800 | 241 | 97.7% | 96.6–98.9% | 92–98% | inconclusive |
| All rows from day 0, including back-filled | R3 | next 24 h | 68% | 11600 | 218 | 79.2% | – | 63–73% | too few data yet |
| All rows from day 0, including back-filled | R4 | next 24 h | 95% | 11600 | 218 | 98.5% | – | 92–98% | too few data yet |
| Run-in (before day 0) | R1 | next 1 h | 68% | 14250 | 281 | 71.0% | 67.6–74.5% | 63–73% | inconclusive |
| Run-in (before day 0) | R2 | next 1 h | 95% | 14250 | 281 | 95.2% | 93.6–96.8% | 92–98% | PASS |
| Run-in (before day 0) | R3 | next 24 h | 68% | 14250 | 281 | 72.1% | – | 63–73% | too few data yet |
| Run-in (before day 0) | R4 | next 24 h | 95% | 14250 | 281 | 97.3% | – | 92–98% | too few data yet |

Coins furthest from the 68% claim on the 24-hour range (primary sample):

| Coin | Coverage | Forecasts |
|---|---|---|
| PEPE | 54% | 221 |
| VET | 61% | 221 |
| BCH | 62% | 221 |
| ETH | 63% | 221 |
| BNB | 65% | 221 |
| TIA | 90% | 221 |
| AVAX | 90% | 221 |
| IMX | 92% | 221 |
| ALGO | 93% | 221 |
| FIL | 94% | 221 |

Information only, not investment advice.
