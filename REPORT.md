# Live calibration of the board's typical-move ranges

Updated 2026-10-30 09:02 UTC. Rules and pass bands are fixed in [LIVE_TEST.md](https://github.com/sandordrpal/crypto-concordance-board/blob/main/research/LIVE_TEST.md) (R1-R4). Primary analysis: on-time forecasts from 2026-10-19; earlier rows are a run-in.

Coverage is the share of real moves that stayed inside the range. Confidence intervals (90%) are clustered by issue hour, because coins move together. PASS when the whole interval lies inside the band.

| Sample | Test | Horizon | Claimed | Forecasts | Issue hours | Coverage | 90% CI | Pass band | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| Primary (on time, from day 0) | R1 | next 1 h | 68% | 13800 | 273 | 73.1% | 69.5–76.7% | 63–73% | inconclusive |
| Primary (on time, from day 0) | R2 | next 1 h | 95% | 13800 | 273 | 96.3% | 94.7–97.9% | 92–98% | PASS |
| Primary (on time, from day 0) | R3 | next 24 h | 68% | 12650 | 250 | 76.1% | – | 63–73% | too few data yet |
| Primary (on time, from day 0) | R4 | next 24 h | 95% | 12650 | 250 | 96.6% | – | 92–98% | too few data yet |
| All rows from day 0, including back-filled | R1 | next 1 h | 68% | 14450 | 273 | 73.1% | 69.5–76.7% | 63–73% | inconclusive |
| All rows from day 0, including back-filled | R2 | next 1 h | 95% | 14450 | 273 | 96.3% | 94.7–97.9% | 92–98% | PASS |
| All rows from day 0, including back-filled | R3 | next 24 h | 68% | 13250 | 250 | 76.1% | – | 63–73% | too few data yet |
| All rows from day 0, including back-filled | R4 | next 24 h | 95% | 13250 | 250 | 96.6% | – | 92–98% | too few data yet |
| Run-in (before day 0) | R1 | next 1 h | 68% | 14250 | 281 | 71.0% | 67.6–74.5% | 63–73% | inconclusive |
| Run-in (before day 0) | R2 | next 1 h | 95% | 14250 | 281 | 95.2% | 93.6–96.8% | 92–98% | PASS |
| Run-in (before day 0) | R3 | next 24 h | 68% | 14250 | 281 | 72.1% | – | 63–73% | too few data yet |
| Run-in (before day 0) | R4 | next 24 h | 95% | 14250 | 281 | 97.3% | – | 92–98% | too few data yet |

Coins furthest from the 68% claim on the 24-hour range (primary sample):

| Coin | Coverage | Forecasts |
|---|---|---|
| PEPE | 55% | 253 |
| VET | 56% | 253 |
| BCH | 59% | 253 |
| ETH | 60% | 253 |
| BNB | 63% | 253 |
| TIA | 86% | 253 |
| ICP | 87% | 253 |
| SUI | 87% | 253 |
| IMX | 88% | 253 |
| FIL | 91% | 253 |

Information only, not investment advice.
