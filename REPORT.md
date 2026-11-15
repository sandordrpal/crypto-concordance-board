# Live calibration of the board's typical-move ranges

Updated 2026-11-15 11:02 UTC. Rules and pass bands are fixed in [LIVE_TEST.md](https://github.com/sandordrpal/crypto-concordance-board/blob/main/research/LIVE_TEST.md) (R1-R4). Primary analysis: on-time forecasts from 2026-10-19; earlier rows are a run-in.

Coverage is the share of real moves that stayed inside the range. Confidence intervals (90%) are clustered by issue hour, because coins move together. PASS when the whole interval lies inside the band.

| Sample | Test | Horizon | Claimed | Forecasts | Issue hours | Coverage | 90% CI | Pass band | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| Primary (on time, from day 0) | R1 | next 1 h | 68% | 33200 | 658 | 70.0% | 67.4–72.7% | 63–73% | PASS |
| Primary (on time, from day 0) | R2 | next 1 h | 95% | 33200 | 658 | 95.4% | 94.1–96.6% | 92–98% | PASS |
| Primary (on time, from day 0) | R3 | next 24 h | 68% | 32050 | 635 | 70.2% | 63.4–77.1% | 63–73% | inconclusive |
| Primary (on time, from day 0) | R4 | next 24 h | 95% | 32050 | 635 | 93.7% | 90.3–97.1% | 92–98% | inconclusive |
| All rows from day 0, including back-filled | R1 | next 1 h | 68% | 34700 | 659 | 70.1% | 67.4–72.7% | 63–73% | PASS |
| All rows from day 0, including back-filled | R2 | next 1 h | 95% | 34700 | 659 | 95.4% | 94.1–96.6% | 92–98% | PASS |
| All rows from day 0, including back-filled | R3 | next 24 h | 68% | 33500 | 636 | 70.2% | 63.5–77.0% | 63–73% | inconclusive |
| All rows from day 0, including back-filled | R4 | next 24 h | 95% | 33500 | 636 | 93.7% | 90.3–97.1% | 92–98% | inconclusive |
| Run-in (before day 0) | R1 | next 1 h | 68% | 14250 | 281 | 71.0% | 67.6–74.5% | 63–73% | inconclusive |
| Run-in (before day 0) | R2 | next 1 h | 95% | 14250 | 281 | 95.2% | 93.6–96.8% | 92–98% | PASS |
| Run-in (before day 0) | R3 | next 24 h | 68% | 14250 | 281 | 72.1% | – | 63–73% | too few data yet |
| Run-in (before day 0) | R4 | next 24 h | 95% | 14250 | 281 | 97.3% | – | 92–98% | too few data yet |

Coins furthest from the 68% claim on the 24-hour range (primary sample):

| Coin | Coverage | Forecasts |
|---|---|---|
| BTC | 55% | 641 |
| ETH | 55% | 641 |
| BNB | 57% | 641 |
| XRP | 61% | 641 |
| TRX | 61% | 641 |
| WLD | 78% | 641 |
| OP | 78% | 641 |
| DOT | 79% | 641 |
| FET | 79% | 641 |
| FIL | 81% | 641 |

Information only, not investment advice.
