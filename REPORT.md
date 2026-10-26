# Live calibration of the board's typical-move ranges

Updated 2026-10-26 08:02 UTC. Rules and pass bands are fixed in [LIVE_TEST.md](https://github.com/sandordrpal/crypto-concordance-board/blob/main/research/LIVE_TEST.md) (R1-R4). Primary analysis: on-time forecasts from 2026-10-19; earlier rows are a run-in.

Coverage is the share of real moves that stayed inside the range. Confidence intervals (90%) are clustered by issue hour, because coins move together. PASS when the whole interval lies inside the band.

| Sample | Test | Horizon | Claimed | Forecasts | Issue hours | Coverage | 90% CI | Pass band | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| Primary (on time, from day 0) | R1 | next 1 h | 68% | 8950 | 176 | 75.9% | 72.5–79.3% | 63–73% | inconclusive |
| Primary (on time, from day 0) | R2 | next 1 h | 95% | 8950 | 176 | 97.8% | 96.3–99.3% | 92–98% | inconclusive |
| Primary (on time, from day 0) | R3 | next 24 h | 68% | 7750 | 153 | 74.0% | – | 63–73% | too few data yet |
| Primary (on time, from day 0) | R4 | next 24 h | 95% | 7750 | 153 | 98.2% | – | 92–98% | too few data yet |
| All rows from day 0, including back-filled | R1 | next 1 h | 68% | 9400 | 176 | 75.9% | 72.5–79.3% | 63–73% | inconclusive |
| All rows from day 0, including back-filled | R2 | next 1 h | 95% | 9400 | 176 | 97.8% | 96.3–99.3% | 92–98% | inconclusive |
| All rows from day 0, including back-filled | R3 | next 24 h | 68% | 8150 | 153 | 74.0% | – | 63–73% | too few data yet |
| All rows from day 0, including back-filled | R4 | next 24 h | 95% | 8150 | 153 | 98.2% | – | 92–98% | too few data yet |
| Run-in (before day 0) | R1 | next 1 h | 68% | 14250 | 281 | 71.0% | 67.6–74.5% | 63–73% | inconclusive |
| Run-in (before day 0) | R2 | next 1 h | 95% | 14250 | 281 | 95.2% | 93.6–96.8% | 92–98% | PASS |
| Run-in (before day 0) | R3 | next 24 h | 68% | 14250 | 281 | 72.1% | – | 63–73% | too few data yet |
| Run-in (before day 0) | R4 | next 24 h | 95% | 14250 | 281 | 97.3% | – | 92–98% | too few data yet |

Coins furthest from the 68% claim on the 24-hour range (primary sample):

| Coin | Coverage | Forecasts |
|---|---|---|
| VET | 53% | 155 |
| PEPE | 54% | 155 |
| BNB | 55% | 155 |
| ETH | 56% | 155 |
| WLD | 59% | 155 |
| IMX | 88% | 155 |
| ALGO | 90% | 155 |
| QNT | 91% | 155 |
| FIL | 92% | 155 |
| TRX | 95% | 155 |

Information only, not investment advice.
