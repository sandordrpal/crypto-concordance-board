# Live calibration of the board's typical-move ranges

Updated 2026-10-28 11:02 UTC. Rules and pass bands are fixed in [LIVE_TEST.md](https://github.com/sandordrpal/crypto-concordance-board/blob/main/research/LIVE_TEST.md) (R1-R4). Primary analysis: on-time forecasts from 2026-10-19; earlier rows are a run-in.

Coverage is the share of real moves that stayed inside the range. Confidence intervals (90%) are clustered by issue hour, because coins move together. PASS when the whole interval lies inside the band.

| Sample | Test | Horizon | Claimed | Forecasts | Issue hours | Coverage | 90% CI | Pass band | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| Primary (on time, from day 0) | R1 | next 1 h | 68% | 11500 | 227 | 76.7% | 73.6–79.9% | 63–73% | FAIL |
| Primary (on time, from day 0) | R2 | next 1 h | 95% | 11500 | 227 | 97.9% | 96.7–99.1% | 92–98% | inconclusive |
| Primary (on time, from day 0) | R3 | next 24 h | 68% | 10350 | 204 | 78.4% | – | 63–73% | too few data yet |
| Primary (on time, from day 0) | R4 | next 24 h | 95% | 10350 | 204 | 98.5% | – | 92–98% | too few data yet |
| All rows from day 0, including back-filled | R1 | next 1 h | 68% | 12050 | 227 | 76.7% | 73.6–79.9% | 63–73% | FAIL |
| All rows from day 0, including back-filled | R2 | next 1 h | 95% | 12050 | 227 | 97.9% | 96.7–99.1% | 92–98% | inconclusive |
| All rows from day 0, including back-filled | R3 | next 24 h | 68% | 10850 | 204 | 78.4% | – | 63–73% | too few data yet |
| All rows from day 0, including back-filled | R4 | next 24 h | 95% | 10850 | 204 | 98.5% | – | 92–98% | too few data yet |
| Run-in (before day 0) | R1 | next 1 h | 68% | 14250 | 281 | 71.0% | 67.6–74.5% | 63–73% | inconclusive |
| Run-in (before day 0) | R2 | next 1 h | 95% | 14250 | 281 | 95.2% | 93.6–96.8% | 92–98% | PASS |
| Run-in (before day 0) | R3 | next 24 h | 68% | 14250 | 281 | 72.1% | – | 63–73% | too few data yet |
| Run-in (before day 0) | R4 | next 24 h | 95% | 14250 | 281 | 97.3% | – | 92–98% | too few data yet |

Coins furthest from the 68% claim on the 24-hour range (primary sample):

| Coin | Coverage | Forecasts |
|---|---|---|
| PEPE | 58% | 207 |
| VET | 58% | 207 |
| ETH | 61% | 207 |
| BCH | 61% | 207 |
| ZEC | 65% | 207 |
| TIA | 89% | 207 |
| AVAX | 89% | 207 |
| IMX | 91% | 207 |
| ALGO | 92% | 207 |
| FIL | 94% | 207 |

Information only, not investment advice.
