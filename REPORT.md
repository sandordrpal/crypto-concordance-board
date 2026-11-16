# Live calibration of the board's typical-move ranges

Updated 2026-11-16 22:02 UTC. Rules and pass bands are fixed in [LIVE_TEST.md](https://github.com/sandordrpal/crypto-concordance-board/blob/main/research/LIVE_TEST.md) (R1-R4). Primary analysis: on-time forecasts from 2026-10-19; earlier rows are a run-in.

Coverage is the share of real moves that stayed inside the range. Confidence intervals (90%) are clustered by issue hour, because coins move together. PASS when the whole interval lies inside the band.

| Sample | Test | Horizon | Claimed | Forecasts | Issue hours | Coverage | 90% CI | Pass band | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| Primary (on time, from day 0) | R1 | next 1 h | 68% | 34950 | 693 | 69.4% | 66.8–72.0% | 63–73% | PASS |
| Primary (on time, from day 0) | R2 | next 1 h | 95% | 34950 | 693 | 95.4% | 94.2–96.6% | 92–98% | PASS |
| Primary (on time, from day 0) | R3 | next 24 h | 68% | 33800 | 670 | 70.4% | 63.7–77.0% | 63–73% | inconclusive |
| Primary (on time, from day 0) | R4 | next 24 h | 95% | 33800 | 670 | 93.9% | 90.6–97.1% | 92–98% | inconclusive |
| All rows from day 0, including back-filled | R1 | next 1 h | 68% | 36500 | 694 | 69.5% | 66.9–72.0% | 63–73% | PASS |
| All rows from day 0, including back-filled | R2 | next 1 h | 95% | 36500 | 694 | 95.4% | 94.2–96.6% | 92–98% | PASS |
| All rows from day 0, including back-filled | R3 | next 24 h | 68% | 35300 | 671 | 70.4% | 63.8–77.0% | 63–73% | inconclusive |
| All rows from day 0, including back-filled | R4 | next 24 h | 95% | 35300 | 671 | 93.9% | 90.6–97.1% | 92–98% | inconclusive |
| Run-in (before day 0) | R1 | next 1 h | 68% | 14250 | 281 | 71.0% | 67.6–74.5% | 63–73% | inconclusive |
| Run-in (before day 0) | R2 | next 1 h | 95% | 14250 | 281 | 95.2% | 93.6–96.8% | 92–98% | PASS |
| Run-in (before day 0) | R3 | next 24 h | 68% | 14250 | 281 | 72.1% | – | 63–73% | too few data yet |
| Run-in (before day 0) | R4 | next 24 h | 95% | 14250 | 281 | 97.3% | – | 92–98% | too few data yet |

Coins furthest from the 68% claim on the 24-hour range (primary sample):

| Coin | Coverage | Forecasts |
|---|---|---|
| BTC | 55% | 676 |
| ETH | 56% | 676 |
| BNB | 58% | 676 |
| TRX | 59% | 676 |
| XRP | 61% | 676 |
| WLD | 78% | 676 |
| OP | 78% | 676 |
| DOT | 79% | 676 |
| FET | 79% | 676 |
| FIL | 80% | 676 |

Information only, not investment advice.
