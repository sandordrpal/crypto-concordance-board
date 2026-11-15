# Live calibration of the board's typical-move ranges

Updated 2026-11-15 02:02 UTC. Rules and pass bands are fixed in [LIVE_TEST.md](https://github.com/sandordrpal/crypto-concordance-board/blob/main/research/LIVE_TEST.md) (R1-R4). Primary analysis: on-time forecasts from 2026-10-19; earlier rows are a run-in.

Coverage is the share of real moves that stayed inside the range. Confidence intervals (90%) are clustered by issue hour, because coins move together. PASS when the whole interval lies inside the band.

| Sample | Test | Horizon | Claimed | Forecasts | Issue hours | Coverage | 90% CI | Pass band | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| Primary (on time, from day 0) | R1 | next 1 h | 68% | 32750 | 649 | 70.2% | 67.6–72.9% | 63–73% | PASS |
| Primary (on time, from day 0) | R2 | next 1 h | 95% | 32750 | 649 | 95.5% | 94.3–96.7% | 92–98% | PASS |
| Primary (on time, from day 0) | R3 | next 24 h | 68% | 31600 | 626 | 71.1% | 64.6–77.6% | 63–73% | inconclusive |
| Primary (on time, from day 0) | R4 | next 24 h | 95% | 31600 | 626 | 94.2% | 91.2–97.2% | 92–98% | inconclusive |
| All rows from day 0, including back-filled | R1 | next 1 h | 68% | 34250 | 650 | 70.3% | 67.6–72.9% | 63–73% | PASS |
| All rows from day 0, including back-filled | R2 | next 1 h | 95% | 34250 | 650 | 95.5% | 94.3–96.7% | 92–98% | PASS |
| All rows from day 0, including back-filled | R3 | next 24 h | 68% | 33050 | 627 | 71.1% | 64.7–77.5% | 63–73% | inconclusive |
| All rows from day 0, including back-filled | R4 | next 24 h | 95% | 33050 | 627 | 94.2% | 91.2–97.2% | 92–98% | inconclusive |
| Run-in (before day 0) | R1 | next 1 h | 68% | 14250 | 281 | 71.0% | 67.6–74.5% | 63–73% | inconclusive |
| Run-in (before day 0) | R2 | next 1 h | 95% | 14250 | 281 | 95.2% | 93.6–96.8% | 92–98% | PASS |
| Run-in (before day 0) | R3 | next 24 h | 68% | 14250 | 281 | 72.1% | – | 63–73% | too few data yet |
| Run-in (before day 0) | R4 | next 24 h | 95% | 14250 | 281 | 97.3% | – | 92–98% | too few data yet |

Coins furthest from the 68% claim on the 24-hour range (primary sample):

| Coin | Coverage | Forecasts |
|---|---|---|
| BTC | 56% | 632 |
| ETH | 56% | 632 |
| BNB | 57% | 632 |
| XRP | 61% | 632 |
| TRX | 62% | 632 |
| WLD | 79% | 632 |
| OP | 79% | 632 |
| DOT | 80% | 632 |
| FET | 80% | 632 |
| FIL | 83% | 632 |

Information only, not investment advice.
