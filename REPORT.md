# Live calibration of the board's typical-move ranges

Updated 2026-11-17 04:02 UTC. Rules and pass bands are fixed in [LIVE_TEST.md](https://github.com/sandordrpal/crypto-concordance-board/blob/main/research/LIVE_TEST.md) (R1-R4). Primary analysis: on-time forecasts from 2026-10-19; earlier rows are a run-in.

Coverage is the share of real moves that stayed inside the range. Confidence intervals (90%) are clustered by issue hour, because coins move together. PASS when the whole interval lies inside the band.

| Sample | Test | Horizon | Claimed | Forecasts | Issue hours | Coverage | 90% CI | Pass band | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| Primary (on time, from day 0) | R1 | next 1 h | 68% | 35250 | 699 | 69.4% | 66.8–72.0% | 63–73% | PASS |
| Primary (on time, from day 0) | R2 | next 1 h | 95% | 35250 | 699 | 95.4% | 94.2–96.6% | 92–98% | PASS |
| Primary (on time, from day 0) | R3 | next 24 h | 68% | 34100 | 676 | 70.6% | 64.0–77.2% | 63–73% | inconclusive |
| Primary (on time, from day 0) | R4 | next 24 h | 95% | 34100 | 676 | 93.9% | 90.7–97.2% | 92–98% | inconclusive |
| All rows from day 0, including back-filled | R1 | next 1 h | 68% | 36850 | 700 | 69.4% | 66.9–72.0% | 63–73% | PASS |
| All rows from day 0, including back-filled | R2 | next 1 h | 95% | 36850 | 700 | 95.4% | 94.2–96.6% | 92–98% | PASS |
| All rows from day 0, including back-filled | R3 | next 24 h | 68% | 35650 | 677 | 70.6% | 64.0–77.1% | 63–73% | inconclusive |
| All rows from day 0, including back-filled | R4 | next 24 h | 95% | 35650 | 677 | 93.9% | 90.7–97.2% | 92–98% | inconclusive |
| Run-in (before day 0) | R1 | next 1 h | 68% | 14250 | 281 | 71.0% | 67.6–74.5% | 63–73% | inconclusive |
| Run-in (before day 0) | R2 | next 1 h | 95% | 14250 | 281 | 95.2% | 93.6–96.8% | 92–98% | PASS |
| Run-in (before day 0) | R3 | next 24 h | 68% | 14250 | 281 | 72.1% | – | 63–73% | too few data yet |
| Run-in (before day 0) | R4 | next 24 h | 95% | 14250 | 281 | 97.3% | – | 92–98% | too few data yet |

Coins furthest from the 68% claim on the 24-hour range (primary sample):

| Coin | Coverage | Forecasts |
|---|---|---|
| BTC | 56% | 682 |
| ETH | 57% | 682 |
| BNB | 58% | 682 |
| TRX | 60% | 682 |
| XRP | 62% | 682 |
| WLD | 78% | 682 |
| OP | 78% | 682 |
| DOT | 79% | 682 |
| FET | 79% | 682 |
| FIL | 81% | 682 |

Information only, not investment advice.
