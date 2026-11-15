# Live calibration of the board's typical-move ranges

Updated 2026-11-15 04:02 UTC. Rules and pass bands are fixed in [LIVE_TEST.md](https://github.com/sandordrpal/crypto-concordance-board/blob/main/research/LIVE_TEST.md) (R1-R4). Primary analysis: on-time forecasts from 2026-10-19; earlier rows are a run-in.

Coverage is the share of real moves that stayed inside the range. Confidence intervals (90%) are clustered by issue hour, because coins move together. PASS when the whole interval lies inside the band.

| Sample | Test | Horizon | Claimed | Forecasts | Issue hours | Coverage | 90% CI | Pass band | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| Primary (on time, from day 0) | R1 | next 1 h | 68% | 32850 | 651 | 70.1% | 67.5–72.8% | 63–73% | PASS |
| Primary (on time, from day 0) | R2 | next 1 h | 95% | 32850 | 651 | 95.3% | 94.1–96.6% | 92–98% | PASS |
| Primary (on time, from day 0) | R3 | next 24 h | 68% | 31700 | 628 | 70.9% | 64.3–77.4% | 63–73% | inconclusive |
| Primary (on time, from day 0) | R4 | next 24 h | 95% | 31700 | 628 | 94.1% | 90.9–97.2% | 92–98% | inconclusive |
| All rows from day 0, including back-filled | R1 | next 1 h | 68% | 34350 | 652 | 70.2% | 67.5–72.8% | 63–73% | PASS |
| All rows from day 0, including back-filled | R2 | next 1 h | 95% | 34350 | 652 | 95.3% | 94.1–96.6% | 92–98% | PASS |
| All rows from day 0, including back-filled | R3 | next 24 h | 68% | 33150 | 629 | 70.9% | 64.4–77.4% | 63–73% | inconclusive |
| All rows from day 0, including back-filled | R4 | next 24 h | 95% | 33150 | 629 | 94.1% | 90.9–97.2% | 92–98% | inconclusive |
| Run-in (before day 0) | R1 | next 1 h | 68% | 14250 | 281 | 71.0% | 67.6–74.5% | 63–73% | inconclusive |
| Run-in (before day 0) | R2 | next 1 h | 95% | 14250 | 281 | 95.2% | 93.6–96.8% | 92–98% | PASS |
| Run-in (before day 0) | R3 | next 24 h | 68% | 14250 | 281 | 72.1% | – | 63–73% | too few data yet |
| Run-in (before day 0) | R4 | next 24 h | 95% | 14250 | 281 | 97.3% | – | 92–98% | too few data yet |

Coins furthest from the 68% claim on the 24-hour range (primary sample):

| Coin | Coverage | Forecasts |
|---|---|---|
| BTC | 56% | 634 |
| ETH | 56% | 634 |
| BNB | 57% | 634 |
| XRP | 61% | 634 |
| TRX | 62% | 634 |
| WLD | 79% | 634 |
| OP | 79% | 634 |
| DOT | 80% | 634 |
| FET | 80% | 634 |
| FIL | 82% | 634 |

Information only, not investment advice.
