# Live calibration of the board's typical-move ranges

Updated 2026-10-26 07:02 UTC. Rules and pass bands are fixed in [LIVE_TEST.md](https://github.com/sandordrpal/crypto-concordance-board/blob/main/research/LIVE_TEST.md) (R1-R4). Primary analysis: on-time forecasts from 2026-10-19; earlier rows are a run-in.

Coverage is the share of real moves that stayed inside the range. Confidence intervals (90%) are clustered by issue hour, because coins move together. PASS when the whole interval lies inside the band.

| Sample | Test | Horizon | Claimed | Forecasts | Issue hours | Coverage | 90% CI | Pass band | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| Primary (on time, from day 0) | R1 | next 1 h | 68% | 8900 | 175 | 75.8% | 72.4–79.3% | 63–73% | inconclusive |
| Primary (on time, from day 0) | R2 | next 1 h | 95% | 8900 | 175 | 97.8% | 96.3–99.3% | 92–98% | inconclusive |
| Primary (on time, from day 0) | R3 | next 24 h | 68% | 7700 | 152 | 73.8% | – | 63–73% | too few data yet |
| Primary (on time, from day 0) | R4 | next 24 h | 95% | 7700 | 152 | 98.2% | – | 92–98% | too few data yet |
| All rows from day 0, including back-filled | R1 | next 1 h | 68% | 9350 | 175 | 75.8% | 72.4–79.3% | 63–73% | inconclusive |
| All rows from day 0, including back-filled | R2 | next 1 h | 95% | 9350 | 175 | 97.8% | 96.3–99.3% | 92–98% | inconclusive |
| All rows from day 0, including back-filled | R3 | next 24 h | 68% | 8100 | 152 | 73.8% | – | 63–73% | too few data yet |
| All rows from day 0, including back-filled | R4 | next 24 h | 95% | 8100 | 152 | 98.2% | – | 92–98% | too few data yet |
| Run-in (before day 0) | R1 | next 1 h | 68% | 14250 | 281 | 71.0% | 67.6–74.5% | 63–73% | inconclusive |
| Run-in (before day 0) | R2 | next 1 h | 95% | 14250 | 281 | 95.2% | 93.6–96.8% | 92–98% | PASS |
| Run-in (before day 0) | R3 | next 24 h | 68% | 14250 | 281 | 72.1% | – | 63–73% | too few data yet |
| Run-in (before day 0) | R4 | next 24 h | 95% | 14250 | 281 | 97.3% | – | 92–98% | too few data yet |

Coins furthest from the 68% claim on the 24-hour range (primary sample):

| Coin | Coverage | Forecasts |
|---|---|---|
| VET | 53% | 154 |
| PEPE | 54% | 154 |
| BNB | 55% | 154 |
| ETH | 56% | 154 |
| WLD | 58% | 154 |
| IMX | 88% | 154 |
| ALGO | 90% | 154 |
| QNT | 91% | 154 |
| FIL | 92% | 154 |
| TRX | 95% | 154 |

Information only, not investment advice.
