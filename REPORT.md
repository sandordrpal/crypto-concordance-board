# Live calibration of the board's typical-move ranges

Updated 2026-11-20 09:02 UTC. Rules and pass bands are fixed in [LIVE_TEST.md](https://github.com/sandordrpal/crypto-concordance-board/blob/main/research/LIVE_TEST.md) (R1-R4). Primary analysis: on-time forecasts from 2026-10-19; earlier rows are a run-in.

Coverage is the share of real moves that stayed inside the range. Confidence intervals (90%) are clustered by issue hour, because coins move together. PASS when the whole interval lies inside the band.

| Sample | Test | Horizon | Claimed | Forecasts | Issue hours | Coverage | 90% CI | Pass band | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| Primary (on time, from day 0) | R1 | next 1 h | 68% | 39150 | 776 | 68.6% | 66.2–71.0% | 63–73% | PASS |
| Primary (on time, from day 0) | R2 | next 1 h | 95% | 39150 | 776 | 95.3% | 94.2–96.4% | 92–98% | PASS |
| Primary (on time, from day 0) | R3 | next 24 h | 68% | 37950 | 753 | 71.7% | 65.6–77.8% | 63–73% | inconclusive |
| Primary (on time, from day 0) | R4 | next 24 h | 95% | 37950 | 753 | 94.4% | 91.5–97.4% | 92–98% | inconclusive |
| All rows from day 0, including back-filled | R1 | next 1 h | 68% | 40900 | 777 | 68.6% | 66.2–71.0% | 63–73% | PASS |
| All rows from day 0, including back-filled | R2 | next 1 h | 95% | 40900 | 777 | 95.3% | 94.2–96.4% | 92–98% | PASS |
| All rows from day 0, including back-filled | R3 | next 24 h | 68% | 39650 | 754 | 71.7% | 65.6–77.8% | 63–73% | inconclusive |
| All rows from day 0, including back-filled | R4 | next 24 h | 95% | 39650 | 754 | 94.4% | 91.5–97.4% | 92–98% | inconclusive |
| Run-in (before day 0) | R1 | next 1 h | 68% | 14250 | 281 | 71.0% | 67.6–74.5% | 63–73% | inconclusive |
| Run-in (before day 0) | R2 | next 1 h | 95% | 14250 | 281 | 95.2% | 93.6–96.8% | 92–98% | PASS |
| Run-in (before day 0) | R3 | next 24 h | 68% | 14250 | 281 | 72.1% | – | 63–73% | too few data yet |
| Run-in (before day 0) | R4 | next 24 h | 95% | 14250 | 281 | 97.3% | – | 92–98% | too few data yet |

Coins furthest from the 68% claim on the 24-hour range (primary sample):

| Coin | Coverage | Forecasts |
|---|---|---|
| BTC | 57% | 759 |
| ETH | 60% | 759 |
| TRX | 60% | 759 |
| BNB | 61% | 759 |
| SOL | 63% | 759 |
| WLD | 79% | 759 |
| TIA | 79% | 759 |
| FET | 80% | 759 |
| DOT | 80% | 759 |
| FIL | 81% | 759 |

Information only, not investment advice.
