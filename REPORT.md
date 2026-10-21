# Live calibration of the board's typical-move ranges

Updated 2026-10-21 20:02 UTC. Rules and pass bands are fixed in [LIVE_TEST.md](https://github.com/sandordrpal/crypto-concordance-board/blob/main/research/LIVE_TEST.md) (R1-R4). Primary analysis: on-time forecasts from 2026-10-19; earlier rows are a run-in.

Coverage is the share of real moves that stayed inside the range. Confidence intervals (90%) are clustered by issue hour, because coins move together. PASS when the whole interval lies inside the band.

| Sample | Test | Horizon | Claimed | Forecasts | Issue hours | Coverage | 90% CI | Pass band | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| Primary (on time, from day 0) | R1 | next 1 h | 68% | 3500 | 68 | 78.2% | – | 63–73% | too few data yet |
| Primary (on time, from day 0) | R2 | next 1 h | 95% | 3500 | 68 | 97.2% | – | 92–98% | too few data yet |
| Primary (on time, from day 0) | R3 | next 24 h | 68% | 2350 | 45 | 78.6% | – | 63–73% | too few data yet |
| Primary (on time, from day 0) | R4 | next 24 h | 95% | 2350 | 45 | 99.0% | – | 92–98% | too few data yet |
| All rows from day 0, including back-filled | R1 | next 1 h | 68% | 3700 | 68 | 78.2% | – | 63–73% | too few data yet |
| All rows from day 0, including back-filled | R2 | next 1 h | 95% | 3700 | 68 | 97.2% | – | 92–98% | too few data yet |
| All rows from day 0, including back-filled | R3 | next 24 h | 68% | 2450 | 45 | 78.6% | – | 63–73% | too few data yet |
| All rows from day 0, including back-filled | R4 | next 24 h | 95% | 2450 | 45 | 99.0% | – | 92–98% | too few data yet |
| Run-in (before day 0) | R1 | next 1 h | 68% | 14250 | 281 | 71.0% | 67.6–74.5% | 63–73% | inconclusive |
| Run-in (before day 0) | R2 | next 1 h | 95% | 14250 | 281 | 95.2% | 93.6–96.8% | 92–98% | PASS |
| Run-in (before day 0) | R3 | next 24 h | 68% | 14250 | 281 | 72.1% | – | 63–73% | too few data yet |
| Run-in (before day 0) | R4 | next 24 h | 95% | 14250 | 281 | 97.3% | – | 92–98% | too few data yet |

Coins furthest from the 68% claim on the 24-hour range (primary sample):

| Coin | Coverage | Forecasts |
|---|---|---|
| WLD | 26% | 47 |
| ZEC | 34% | 47 |
| VET | 36% | 47 |
| ETH | 38% | 47 |
| JUP | 43% | 47 |
| SEI | 100% | 47 |
| SUI | 100% | 47 |
| QNT | 100% | 47 |
| TAO | 100% | 47 |
| TRX | 100% | 47 |

Information only, not investment advice.
