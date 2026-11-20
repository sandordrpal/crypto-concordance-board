# Live calibration of the board's typical-move ranges

Updated 2026-11-20 00:02 UTC. Rules and pass bands are fixed in [LIVE_TEST.md](https://github.com/sandordrpal/crypto-concordance-board/blob/main/research/LIVE_TEST.md) (R1-R4). Primary analysis: on-time forecasts from 2026-10-19; earlier rows are a run-in.

Coverage is the share of real moves that stayed inside the range. Confidence intervals (90%) are clustered by issue hour, because coins move together. PASS when the whole interval lies inside the band.

| Sample | Test | Horizon | Claimed | Forecasts | Issue hours | Coverage | 90% CI | Pass band | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| Primary (on time, from day 0) | R1 | next 1 h | 68% | 38650 | 767 | 68.8% | 66.4–71.2% | 63–73% | PASS |
| Primary (on time, from day 0) | R2 | next 1 h | 95% | 38650 | 767 | 95.4% | 94.3–96.5% | 92–98% | PASS |
| Primary (on time, from day 0) | R3 | next 24 h | 68% | 37500 | 744 | 72.1% | 65.9–78.3% | 63–73% | inconclusive |
| Primary (on time, from day 0) | R4 | next 24 h | 95% | 37500 | 744 | 94.4% | 91.4–97.4% | 92–98% | inconclusive |
| All rows from day 0, including back-filled | R1 | next 1 h | 68% | 40350 | 768 | 68.8% | 66.4–71.2% | 63–73% | PASS |
| All rows from day 0, including back-filled | R2 | next 1 h | 95% | 40350 | 768 | 95.4% | 94.3–96.5% | 92–98% | PASS |
| All rows from day 0, including back-filled | R3 | next 24 h | 68% | 39200 | 745 | 72.1% | 66.0–78.3% | 63–73% | inconclusive |
| All rows from day 0, including back-filled | R4 | next 24 h | 95% | 39200 | 745 | 94.4% | 91.4–97.4% | 92–98% | inconclusive |
| Run-in (before day 0) | R1 | next 1 h | 68% | 14250 | 281 | 71.0% | 67.6–74.5% | 63–73% | inconclusive |
| Run-in (before day 0) | R2 | next 1 h | 95% | 14250 | 281 | 95.2% | 93.6–96.8% | 92–98% | PASS |
| Run-in (before day 0) | R3 | next 24 h | 68% | 14250 | 281 | 72.1% | – | 63–73% | too few data yet |
| Run-in (before day 0) | R4 | next 24 h | 95% | 14250 | 281 | 97.3% | – | 92–98% | too few data yet |

Coins furthest from the 68% claim on the 24-hour range (primary sample):

| Coin | Coverage | Forecasts |
|---|---|---|
| BTC | 57% | 750 |
| ETH | 60% | 750 |
| TRX | 60% | 750 |
| BNB | 61% | 750 |
| SOL | 63% | 750 |
| TIA | 80% | 750 |
| WLD | 80% | 750 |
| DOT | 80% | 750 |
| FIL | 80% | 750 |
| FET | 80% | 750 |

Information only, not investment advice.
