# Live calibration of the board's typical-move ranges

Updated 2026-10-27 18:02 UTC. Rules and pass bands are fixed in [LIVE_TEST.md](https://github.com/sandordrpal/crypto-concordance-board/blob/main/research/LIVE_TEST.md) (R1-R4). Primary analysis: on-time forecasts from 2026-10-19; earlier rows are a run-in.

Coverage is the share of real moves that stayed inside the range. Confidence intervals (90%) are clustered by issue hour, because coins move together. PASS when the whole interval lies inside the band.

| Sample | Test | Horizon | Claimed | Forecasts | Issue hours | Coverage | 90% CI | Pass band | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| Primary (on time, from day 0) | R1 | next 1 h | 68% | 10650 | 210 | 75.6% | 72.4–78.7% | 63–73% | inconclusive |
| Primary (on time, from day 0) | R2 | next 1 h | 95% | 10650 | 210 | 97.8% | 96.5–99.1% | 92–98% | inconclusive |
| Primary (on time, from day 0) | R3 | next 24 h | 68% | 9500 | 187 | 77.9% | – | 63–73% | too few data yet |
| Primary (on time, from day 0) | R4 | next 24 h | 95% | 9500 | 187 | 98.5% | – | 92–98% | too few data yet |
| All rows from day 0, including back-filled | R1 | next 1 h | 68% | 11150 | 210 | 75.6% | 72.4–78.7% | 63–73% | inconclusive |
| All rows from day 0, including back-filled | R2 | next 1 h | 95% | 11150 | 210 | 97.8% | 96.5–99.1% | 92–98% | inconclusive |
| All rows from day 0, including back-filled | R3 | next 24 h | 68% | 9950 | 187 | 77.9% | – | 63–73% | too few data yet |
| All rows from day 0, including back-filled | R4 | next 24 h | 95% | 9950 | 187 | 98.5% | – | 92–98% | too few data yet |
| Run-in (before day 0) | R1 | next 1 h | 68% | 14250 | 281 | 71.0% | 67.6–74.5% | 63–73% | inconclusive |
| Run-in (before day 0) | R2 | next 1 h | 95% | 14250 | 281 | 95.2% | 93.6–96.8% | 92–98% | PASS |
| Run-in (before day 0) | R3 | next 24 h | 68% | 14250 | 281 | 72.1% | – | 63–73% | too few data yet |
| Run-in (before day 0) | R4 | next 24 h | 95% | 14250 | 281 | 97.3% | – | 92–98% | too few data yet |

Coins furthest from the 68% claim on the 24-hour range (primary sample):

| Coin | Coverage | Forecasts |
|---|---|---|
| VET | 55% | 190 |
| PEPE | 63% | 190 |
| ETH | 63% | 190 |
| BNB | 64% | 190 |
| WLD | 66% | 190 |
| TIA | 88% | 190 |
| AVAX | 89% | 190 |
| IMX | 91% | 190 |
| ALGO | 92% | 190 |
| FIL | 93% | 190 |

Information only, not investment advice.
