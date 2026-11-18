# Live calibration of the board's typical-move ranges

Updated 2026-11-18 07:02 UTC. Rules and pass bands are fixed in [LIVE_TEST.md](https://github.com/sandordrpal/crypto-concordance-board/blob/main/research/LIVE_TEST.md) (R1-R4). Primary analysis: on-time forecasts from 2026-10-19; earlier rows are a run-in.

Coverage is the share of real moves that stayed inside the range. Confidence intervals (90%) are clustered by issue hour, because coins move together. PASS when the whole interval lies inside the band.

| Sample | Test | Horizon | Claimed | Forecasts | Issue hours | Coverage | 90% CI | Pass band | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| Primary (on time, from day 0) | R1 | next 1 h | 68% | 36600 | 726 | 69.2% | 66.6–71.7% | 63–73% | PASS |
| Primary (on time, from day 0) | R2 | next 1 h | 95% | 36600 | 726 | 95.3% | 94.2–96.5% | 92–98% | PASS |
| Primary (on time, from day 0) | R3 | next 24 h | 68% | 35450 | 703 | 71.2% | 64.8–77.6% | 63–73% | inconclusive |
| Primary (on time, from day 0) | R4 | next 24 h | 95% | 35450 | 703 | 94.1% | 91.0–97.2% | 92–98% | inconclusive |
| All rows from day 0, including back-filled | R1 | next 1 h | 68% | 38250 | 727 | 69.2% | 66.7–71.7% | 63–73% | PASS |
| All rows from day 0, including back-filled | R2 | next 1 h | 95% | 38250 | 727 | 95.3% | 94.2–96.5% | 92–98% | PASS |
| All rows from day 0, including back-filled | R3 | next 24 h | 68% | 37050 | 704 | 71.2% | 64.8–77.6% | 63–73% | inconclusive |
| All rows from day 0, including back-filled | R4 | next 24 h | 95% | 37050 | 704 | 94.1% | 91.0–97.2% | 92–98% | inconclusive |
| Run-in (before day 0) | R1 | next 1 h | 68% | 14250 | 281 | 71.0% | 67.6–74.5% | 63–73% | inconclusive |
| Run-in (before day 0) | R2 | next 1 h | 95% | 14250 | 281 | 95.2% | 93.6–96.8% | 92–98% | PASS |
| Run-in (before day 0) | R3 | next 24 h | 68% | 14250 | 281 | 72.1% | – | 63–73% | too few data yet |
| Run-in (before day 0) | R4 | next 24 h | 95% | 14250 | 281 | 97.3% | – | 92–98% | too few data yet |

Coins furthest from the 68% claim on the 24-hour range (primary sample):

| Coin | Coverage | Forecasts |
|---|---|---|
| BTC | 57% | 709 |
| ETH | 58% | 709 |
| BNB | 60% | 709 |
| TRX | 60% | 709 |
| SOL | 62% | 709 |
| TIA | 79% | 709 |
| WLD | 79% | 709 |
| DOT | 80% | 709 |
| FET | 80% | 709 |
| FIL | 81% | 709 |

Information only, not investment advice.
