# Live calibration of the board's typical-move ranges

Updated 2026-10-28 12:02 UTC. Rules and pass bands are fixed in [LIVE_TEST.md](https://github.com/sandordrpal/crypto-concordance-board/blob/main/research/LIVE_TEST.md) (R1-R4). Primary analysis: on-time forecasts from 2026-10-19; earlier rows are a run-in.

Coverage is the share of real moves that stayed inside the range. Confidence intervals (90%) are clustered by issue hour, because coins move together. PASS when the whole interval lies inside the band.

| Sample | Test | Horizon | Claimed | Forecasts | Issue hours | Coverage | 90% CI | Pass band | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| Primary (on time, from day 0) | R1 | next 1 h | 68% | 11550 | 228 | 76.8% | 73.7–80.0% | 63–73% | FAIL |
| Primary (on time, from day 0) | R2 | next 1 h | 95% | 11550 | 228 | 97.9% | 96.8–99.1% | 92–98% | inconclusive |
| Primary (on time, from day 0) | R3 | next 24 h | 68% | 10400 | 205 | 78.4% | – | 63–73% | too few data yet |
| Primary (on time, from day 0) | R4 | next 24 h | 95% | 10400 | 205 | 98.5% | – | 92–98% | too few data yet |
| All rows from day 0, including back-filled | R1 | next 1 h | 68% | 12100 | 228 | 76.8% | 73.7–80.0% | 63–73% | FAIL |
| All rows from day 0, including back-filled | R2 | next 1 h | 95% | 12100 | 228 | 97.9% | 96.8–99.1% | 92–98% | inconclusive |
| All rows from day 0, including back-filled | R3 | next 24 h | 68% | 10900 | 205 | 78.4% | – | 63–73% | too few data yet |
| All rows from day 0, including back-filled | R4 | next 24 h | 95% | 10900 | 205 | 98.5% | – | 92–98% | too few data yet |
| Run-in (before day 0) | R1 | next 1 h | 68% | 14250 | 281 | 71.0% | 67.6–74.5% | 63–73% | inconclusive |
| Run-in (before day 0) | R2 | next 1 h | 95% | 14250 | 281 | 95.2% | 93.6–96.8% | 92–98% | PASS |
| Run-in (before day 0) | R3 | next 24 h | 68% | 14250 | 281 | 72.1% | – | 63–73% | too few data yet |
| Run-in (before day 0) | R4 | next 24 h | 95% | 14250 | 281 | 97.3% | – | 92–98% | too few data yet |

Coins furthest from the 68% claim on the 24-hour range (primary sample):

| Coin | Coverage | Forecasts |
|---|---|---|
| PEPE | 58% | 208 |
| VET | 59% | 208 |
| ETH | 61% | 208 |
| BCH | 61% | 208 |
| ZEC | 65% | 208 |
| TIA | 89% | 208 |
| AVAX | 89% | 208 |
| IMX | 91% | 208 |
| ALGO | 92% | 208 |
| FIL | 94% | 208 |

Information only, not investment advice.
