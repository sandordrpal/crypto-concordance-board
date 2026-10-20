# Live calibration of the board's typical-move ranges

Updated 2026-10-20 13:02 UTC. Rules and pass bands are fixed in [LIVE_TEST.md](https://github.com/sandordrpal/crypto-concordance-board/blob/main/research/LIVE_TEST.md) (R1-R4). Primary analysis: on-time forecasts from 2026-10-19; earlier rows are a run-in.

Coverage is the share of real moves that stayed inside the range. Confidence intervals (90%) are clustered by issue hour, because coins move together. PASS when the whole interval lies inside the band.

| Sample | Test | Horizon | Claimed | Forecasts | Issue hours | Coverage | 90% CI | Pass band | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| Primary (on time, from day 0) | R1 | next 1 h | 68% | 1950 | 37 | 83.5% | – | 63–73% | too few data yet |
| Primary (on time, from day 0) | R2 | next 1 h | 95% | 1950 | 37 | 99.7% | – | 92–98% | too few data yet |
| Primary (on time, from day 0) | R3 | next 24 h | 68% | 750 | 14 | 95.7% | – | 63–73% | too few data yet |
| Primary (on time, from day 0) | R4 | next 24 h | 95% | 750 | 14 | 100.0% | – | 92–98% | too few data yet |
| All rows from day 0, including back-filled | R1 | next 1 h | 68% | 2050 | 37 | 83.5% | – | 63–73% | too few data yet |
| All rows from day 0, including back-filled | R2 | next 1 h | 95% | 2050 | 37 | 99.7% | – | 92–98% | too few data yet |
| All rows from day 0, including back-filled | R3 | next 24 h | 68% | 800 | 14 | 95.7% | – | 63–73% | too few data yet |
| All rows from day 0, including back-filled | R4 | next 24 h | 95% | 800 | 14 | 100.0% | – | 92–98% | too few data yet |
| Run-in (before day 0) | R1 | next 1 h | 68% | 14250 | 281 | 71.0% | 67.6–74.5% | 63–73% | inconclusive |
| Run-in (before day 0) | R2 | next 1 h | 95% | 14250 | 281 | 95.2% | 93.6–96.8% | 92–98% | PASS |
| Run-in (before day 0) | R3 | next 24 h | 68% | 14250 | 281 | 72.1% | – | 63–73% | too few data yet |
| Run-in (before day 0) | R4 | next 24 h | 95% | 14250 | 281 | 97.3% | – | 92–98% | too few data yet |

Coins furthest from the 68% claim on the 24-hour range (primary sample):

| Coin | Coverage | Forecasts |
|---|---|---|
| WLD | 20% | 15 |
| BTC | 67% | 15 |
| STX | 73% | 15 |
| CRV | 73% | 15 |
| ARB | 80% | 15 |
| VET | 100% | 15 |
| WIF | 100% | 15 |
| XLM | 100% | 15 |
| XRP | 100% | 15 |
| ZEC | 100% | 15 |

Information only, not investment advice.
