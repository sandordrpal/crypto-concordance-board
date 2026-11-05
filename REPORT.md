# Live calibration of the board's typical-move ranges

Updated 2026-11-05 12:02 UTC. Rules and pass bands are fixed in [LIVE_TEST.md](https://github.com/sandordrpal/crypto-concordance-board/blob/main/research/LIVE_TEST.md) (R1-R4). Primary analysis: on-time forecasts from 2026-10-19; earlier rows are a run-in.

Coverage is the share of real moves that stayed inside the range. Confidence intervals (90%) are clustered by issue hour, because coins move together. PASS when the whole interval lies inside the band.

| Sample | Test | Horizon | Claimed | Forecasts | Issue hours | Coverage | 90% CI | Pass band | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| Primary (on time, from day 0) | R1 | next 1 h | 68% | 21100 | 419 | 72.5% | 69.6–75.4% | 63–73% | inconclusive |
| Primary (on time, from day 0) | R2 | next 1 h | 95% | 21100 | 419 | 96.6% | 95.5–97.8% | 92–98% | PASS |
| Primary (on time, from day 0) | R3 | next 24 h | 68% | 19950 | 396 | 74.6% | 67.2–82.0% | 63–73% | inconclusive |
| Primary (on time, from day 0) | R4 | next 24 h | 95% | 19950 | 396 | 96.1% | 93.5–98.7% | 92–98% | inconclusive |
| All rows from day 0, including back-filled | R1 | next 1 h | 68% | 22100 | 420 | 72.5% | 69.6–75.5% | 63–73% | inconclusive |
| All rows from day 0, including back-filled | R2 | next 1 h | 95% | 22100 | 420 | 96.6% | 95.5–97.8% | 92–98% | PASS |
| All rows from day 0, including back-filled | R3 | next 24 h | 68% | 20900 | 397 | 74.6% | 67.2–82.0% | 63–73% | inconclusive |
| All rows from day 0, including back-filled | R4 | next 24 h | 95% | 20900 | 397 | 96.1% | 93.5–98.7% | 92–98% | inconclusive |
| Run-in (before day 0) | R1 | next 1 h | 68% | 14250 | 281 | 71.0% | 67.6–74.5% | 63–73% | inconclusive |
| Run-in (before day 0) | R2 | next 1 h | 95% | 14250 | 281 | 95.2% | 93.6–96.8% | 92–98% | PASS |
| Run-in (before day 0) | R3 | next 24 h | 68% | 14250 | 281 | 72.1% | – | 63–73% | too few data yet |
| Run-in (before day 0) | R4 | next 24 h | 95% | 14250 | 281 | 97.3% | – | 92–98% | too few data yet |

Coins furthest from the 68% claim on the 24-hour range (primary sample):

| Coin | Coverage | Forecasts |
|---|---|---|
| TRX | 55% | 399 |
| BTC | 61% | 399 |
| BNB | 62% | 399 |
| ETH | 63% | 399 |
| PEPE | 63% | 399 |
| SUI | 84% | 399 |
| IMX | 84% | 399 |
| FET | 84% | 399 |
| ICP | 84% | 399 |
| FIL | 91% | 399 |

Information only, not investment advice.
