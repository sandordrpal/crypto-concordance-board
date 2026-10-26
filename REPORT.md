# Live calibration of the board's typical-move ranges

Updated 2026-10-26 13:02 UTC. Rules and pass bands are fixed in [LIVE_TEST.md](https://github.com/sandordrpal/crypto-concordance-board/blob/main/research/LIVE_TEST.md) (R1-R4). Primary analysis: on-time forecasts from 2026-10-19; earlier rows are a run-in.

Coverage is the share of real moves that stayed inside the range. Confidence intervals (90%) are clustered by issue hour, because coins move together. PASS when the whole interval lies inside the band.

| Sample | Test | Horizon | Claimed | Forecasts | Issue hours | Coverage | 90% CI | Pass band | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| Primary (on time, from day 0) | R1 | next 1 h | 68% | 9200 | 181 | 75.8% | 72.5–79.2% | 63–73% | inconclusive |
| Primary (on time, from day 0) | R2 | next 1 h | 95% | 9200 | 181 | 97.8% | 96.4–99.3% | 92–98% | inconclusive |
| Primary (on time, from day 0) | R3 | next 24 h | 68% | 8000 | 158 | 74.6% | – | 63–73% | too few data yet |
| Primary (on time, from day 0) | R4 | next 24 h | 95% | 8000 | 158 | 98.3% | – | 92–98% | too few data yet |
| All rows from day 0, including back-filled | R1 | next 1 h | 68% | 9650 | 181 | 75.8% | 72.5–79.2% | 63–73% | inconclusive |
| All rows from day 0, including back-filled | R2 | next 1 h | 95% | 9650 | 181 | 97.8% | 96.4–99.3% | 92–98% | inconclusive |
| All rows from day 0, including back-filled | R3 | next 24 h | 68% | 8400 | 158 | 74.6% | – | 63–73% | too few data yet |
| All rows from day 0, including back-filled | R4 | next 24 h | 95% | 8400 | 158 | 98.3% | – | 92–98% | too few data yet |
| Run-in (before day 0) | R1 | next 1 h | 68% | 14250 | 281 | 71.0% | 67.6–74.5% | 63–73% | inconclusive |
| Run-in (before day 0) | R2 | next 1 h | 95% | 14250 | 281 | 95.2% | 93.6–96.8% | 92–98% | PASS |
| Run-in (before day 0) | R3 | next 24 h | 68% | 14250 | 281 | 72.1% | – | 63–73% | too few data yet |
| Run-in (before day 0) | R4 | next 24 h | 95% | 14250 | 281 | 97.3% | – | 92–98% | too few data yet |

Coins furthest from the 68% claim on the 24-hour range (primary sample):

| Coin | Coverage | Forecasts |
|---|---|---|
| VET | 54% | 160 |
| PEPE | 56% | 160 |
| BNB | 57% | 160 |
| ETH | 57% | 160 |
| WLD | 60% | 160 |
| QNT | 88% | 160 |
| IMX | 89% | 160 |
| ALGO | 90% | 160 |
| FIL | 92% | 160 |
| TRX | 93% | 160 |

Information only, not investment advice.
