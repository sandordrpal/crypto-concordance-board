# Live calibration of the board's typical-move ranges

Updated 2026-11-06 01:02 UTC. Rules and pass bands are fixed in [LIVE_TEST.md](https://github.com/sandordrpal/crypto-concordance-board/blob/main/research/LIVE_TEST.md) (R1-R4). Primary analysis: on-time forecasts from 2026-10-19; earlier rows are a run-in.

Coverage is the share of real moves that stayed inside the range. Confidence intervals (90%) are clustered by issue hour, because coins move together. PASS when the whole interval lies inside the band.

| Sample | Test | Horizon | Claimed | Forecasts | Issue hours | Coverage | 90% CI | Pass band | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| Primary (on time, from day 0) | R1 | next 1 h | 68% | 21800 | 432 | 71.4% | 68.4–74.5% | 63–73% | inconclusive |
| Primary (on time, from day 0) | R2 | next 1 h | 95% | 21800 | 432 | 96.1% | 94.8–97.4% | 92–98% | PASS |
| Primary (on time, from day 0) | R3 | next 24 h | 68% | 20600 | 409 | 73.1% | 65.4–80.9% | 63–73% | inconclusive |
| Primary (on time, from day 0) | R4 | next 24 h | 95% | 20600 | 409 | 95.4% | 92.6–98.2% | 92–98% | inconclusive |
| All rows from day 0, including back-filled | R1 | next 1 h | 68% | 22850 | 433 | 71.5% | 68.4–74.5% | 63–73% | inconclusive |
| All rows from day 0, including back-filled | R2 | next 1 h | 95% | 22850 | 433 | 96.1% | 94.8–97.4% | 92–98% | PASS |
| All rows from day 0, including back-filled | R3 | next 24 h | 68% | 21600 | 410 | 73.1% | 65.5–80.8% | 63–73% | inconclusive |
| All rows from day 0, including back-filled | R4 | next 24 h | 95% | 21600 | 410 | 95.4% | 92.6–98.2% | 92–98% | inconclusive |
| Run-in (before day 0) | R1 | next 1 h | 68% | 14250 | 281 | 71.0% | 67.6–74.5% | 63–73% | inconclusive |
| Run-in (before day 0) | R2 | next 1 h | 95% | 14250 | 281 | 95.2% | 93.6–96.8% | 92–98% | PASS |
| Run-in (before day 0) | R3 | next 24 h | 68% | 14250 | 281 | 72.1% | – | 63–73% | too few data yet |
| Run-in (before day 0) | R4 | next 24 h | 95% | 14250 | 281 | 97.3% | – | 92–98% | too few data yet |

Coins furthest from the 68% claim on the 24-hour range (primary sample):

| Coin | Coverage | Forecasts |
|---|---|---|
| TRX | 55% | 412 |
| BTC | 59% | 412 |
| BNB | 60% | 412 |
| ETH | 61% | 412 |
| PEPE | 63% | 412 |
| OP | 82% | 412 |
| IMX | 82% | 412 |
| FET | 82% | 412 |
| ICP | 83% | 412 |
| FIL | 89% | 412 |

Information only, not investment advice.
