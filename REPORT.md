# Live calibration of the board's typical-move ranges

Updated 2026-11-19 01:02 UTC. Rules and pass bands are fixed in [LIVE_TEST.md](https://github.com/sandordrpal/crypto-concordance-board/blob/main/research/LIVE_TEST.md) (R1-R4). Primary analysis: on-time forecasts from 2026-10-19; earlier rows are a run-in.

Coverage is the share of real moves that stayed inside the range. Confidence intervals (90%) are clustered by issue hour, because coins move together. PASS when the whole interval lies inside the band.

| Sample | Test | Horizon | Claimed | Forecasts | Issue hours | Coverage | 90% CI | Pass band | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| Primary (on time, from day 0) | R1 | next 1 h | 68% | 37500 | 744 | 69.0% | 66.5–71.5% | 63–73% | PASS |
| Primary (on time, from day 0) | R2 | next 1 h | 95% | 37500 | 744 | 95.4% | 94.2–96.5% | 92–98% | PASS |
| Primary (on time, from day 0) | R3 | next 24 h | 68% | 36350 | 721 | 71.5% | 65.2–77.8% | 63–73% | inconclusive |
| Primary (on time, from day 0) | R4 | next 24 h | 95% | 36350 | 721 | 94.2% | 91.2–97.3% | 92–98% | inconclusive |
| All rows from day 0, including back-filled | R1 | next 1 h | 68% | 39200 | 745 | 69.0% | 66.6–71.5% | 63–73% | PASS |
| All rows from day 0, including back-filled | R2 | next 1 h | 95% | 39200 | 745 | 95.4% | 94.2–96.5% | 92–98% | PASS |
| All rows from day 0, including back-filled | R3 | next 24 h | 68% | 38000 | 722 | 71.5% | 65.2–77.8% | 63–73% | inconclusive |
| All rows from day 0, including back-filled | R4 | next 24 h | 95% | 38000 | 722 | 94.2% | 91.2–97.3% | 92–98% | inconclusive |
| Run-in (before day 0) | R1 | next 1 h | 68% | 14250 | 281 | 71.0% | 67.6–74.5% | 63–73% | inconclusive |
| Run-in (before day 0) | R2 | next 1 h | 95% | 14250 | 281 | 95.2% | 93.6–96.8% | 92–98% | PASS |
| Run-in (before day 0) | R3 | next 24 h | 68% | 14250 | 281 | 72.1% | – | 63–73% | too few data yet |
| Run-in (before day 0) | R4 | next 24 h | 95% | 14250 | 281 | 97.3% | – | 92–98% | too few data yet |

Coins furthest from the 68% claim on the 24-hour range (primary sample):

| Coin | Coverage | Forecasts |
|---|---|---|
| BTC | 57% | 727 |
| ETH | 59% | 727 |
| BNB | 60% | 727 |
| TRX | 60% | 727 |
| SOL | 62% | 727 |
| TIA | 79% | 727 |
| WLD | 79% | 727 |
| DOT | 80% | 727 |
| FET | 80% | 727 |
| FIL | 81% | 727 |

Information only, not investment advice.
