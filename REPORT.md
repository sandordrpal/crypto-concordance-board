# Live calibration of the board's typical-move ranges

Updated 2026-11-05 23:02 UTC. Rules and pass bands are fixed in [LIVE_TEST.md](https://github.com/sandordrpal/crypto-concordance-board/blob/main/research/LIVE_TEST.md) (R1-R4). Primary analysis: on-time forecasts from 2026-10-19; earlier rows are a run-in.

Coverage is the share of real moves that stayed inside the range. Confidence intervals (90%) are clustered by issue hour, because coins move together. PASS when the whole interval lies inside the band.

| Sample | Test | Horizon | Claimed | Forecasts | Issue hours | Coverage | 90% CI | Pass band | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| Primary (on time, from day 0) | R1 | next 1 h | 68% | 21650 | 430 | 71.6% | 68.5–74.6% | 63–73% | inconclusive |
| Primary (on time, from day 0) | R2 | next 1 h | 95% | 21650 | 430 | 96.2% | 94.9–97.5% | 92–98% | PASS |
| Primary (on time, from day 0) | R3 | next 24 h | 68% | 20500 | 407 | 73.4% | 65.8–81.0% | 63–73% | inconclusive |
| Primary (on time, from day 0) | R4 | next 24 h | 95% | 20500 | 407 | 95.5% | 92.8–98.3% | 92–98% | inconclusive |
| All rows from day 0, including back-filled | R1 | next 1 h | 68% | 22650 | 431 | 71.6% | 68.6–74.7% | 63–73% | inconclusive |
| All rows from day 0, including back-filled | R2 | next 1 h | 95% | 22650 | 431 | 96.2% | 94.9–97.5% | 92–98% | PASS |
| All rows from day 0, including back-filled | R3 | next 24 h | 68% | 21450 | 408 | 73.4% | 65.8–81.0% | 63–73% | inconclusive |
| All rows from day 0, including back-filled | R4 | next 24 h | 95% | 21450 | 408 | 95.5% | 92.8–98.3% | 92–98% | inconclusive |
| Run-in (before day 0) | R1 | next 1 h | 68% | 14250 | 281 | 71.0% | 67.6–74.5% | 63–73% | inconclusive |
| Run-in (before day 0) | R2 | next 1 h | 95% | 14250 | 281 | 95.2% | 93.6–96.8% | 92–98% | PASS |
| Run-in (before day 0) | R3 | next 24 h | 68% | 14250 | 281 | 72.1% | – | 63–73% | too few data yet |
| Run-in (before day 0) | R4 | next 24 h | 95% | 14250 | 281 | 97.3% | – | 92–98% | too few data yet |

Coins furthest from the 68% claim on the 24-hour range (primary sample):

| Coin | Coverage | Forecasts |
|---|---|---|
| TRX | 55% | 410 |
| BTC | 60% | 410 |
| BNB | 61% | 410 |
| ETH | 61% | 410 |
| PEPE | 63% | 410 |
| OP | 82% | 410 |
| IMX | 82% | 410 |
| FET | 82% | 410 |
| ICP | 83% | 410 |
| FIL | 89% | 410 |

Information only, not investment advice.
