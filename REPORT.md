# Live calibration of the board's typical-move ranges

Updated 2026-11-05 04:02 UTC. Rules and pass bands are fixed in [LIVE_TEST.md](https://github.com/sandordrpal/crypto-concordance-board/blob/main/research/LIVE_TEST.md) (R1-R4). Primary analysis: on-time forecasts from 2026-10-19; earlier rows are a run-in.

Coverage is the share of real moves that stayed inside the range. Confidence intervals (90%) are clustered by issue hour, because coins move together. PASS when the whole interval lies inside the band.

| Sample | Test | Horizon | Claimed | Forecasts | Issue hours | Coverage | 90% CI | Pass band | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| Primary (on time, from day 0) | R1 | next 1 h | 68% | 20700 | 411 | 72.6% | 69.7–75.6% | 63–73% | inconclusive |
| Primary (on time, from day 0) | R2 | next 1 h | 95% | 20700 | 411 | 96.6% | 95.4–97.8% | 92–98% | PASS |
| Primary (on time, from day 0) | R3 | next 24 h | 68% | 19600 | 389 | 74.9% | 67.4–82.3% | 63–73% | inconclusive |
| Primary (on time, from day 0) | R4 | next 24 h | 95% | 19600 | 389 | 96.1% | 93.4–98.7% | 92–98% | inconclusive |
| All rows from day 0, including back-filled | R1 | next 1 h | 68% | 21700 | 412 | 72.7% | 69.7–75.6% | 63–73% | inconclusive |
| All rows from day 0, including back-filled | R2 | next 1 h | 95% | 21700 | 412 | 96.6% | 95.4–97.8% | 92–98% | PASS |
| All rows from day 0, including back-filled | R3 | next 24 h | 68% | 20500 | 389 | 74.9% | 67.4–82.3% | 63–73% | inconclusive |
| All rows from day 0, including back-filled | R4 | next 24 h | 95% | 20500 | 389 | 96.1% | 93.4–98.7% | 92–98% | inconclusive |
| Run-in (before day 0) | R1 | next 1 h | 68% | 14250 | 281 | 71.0% | 67.6–74.5% | 63–73% | inconclusive |
| Run-in (before day 0) | R2 | next 1 h | 95% | 14250 | 281 | 95.2% | 93.6–96.8% | 92–98% | PASS |
| Run-in (before day 0) | R3 | next 24 h | 68% | 14250 | 281 | 72.1% | – | 63–73% | too few data yet |
| Run-in (before day 0) | R4 | next 24 h | 95% | 14250 | 281 | 97.3% | – | 92–98% | too few data yet |

Coins furthest from the 68% claim on the 24-hour range (primary sample):

| Coin | Coverage | Forecasts |
|---|---|---|
| TRX | 55% | 392 |
| BTC | 62% | 392 |
| PEPE | 62% | 392 |
| BNB | 63% | 392 |
| ETH | 64% | 392 |
| IMX | 84% | 392 |
| FET | 84% | 392 |
| ADA | 84% | 392 |
| ICP | 85% | 392 |
| FIL | 91% | 392 |

Information only, not investment advice.
