# Live calibration of the board's typical-move ranges

Updated 2026-11-12 13:02 UTC. Rules and pass bands are fixed in [LIVE_TEST.md](https://github.com/sandordrpal/crypto-concordance-board/blob/main/research/LIVE_TEST.md) (R1-R4). Primary analysis: on-time forecasts from 2026-10-19; earlier rows are a run-in.

Coverage is the share of real moves that stayed inside the range. Confidence intervals (90%) are clustered by issue hour, because coins move together. PASS when the whole interval lies inside the band.

| Sample | Test | Horizon | Claimed | Forecasts | Issue hours | Coverage | 90% CI | Pass band | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| Primary (on time, from day 0) | R1 | next 1 h | 68% | 29650 | 588 | 72.2% | 69.6–74.8% | 63–73% | inconclusive |
| Primary (on time, from day 0) | R2 | next 1 h | 95% | 29650 | 588 | 96.2% | 95.2–97.3% | 92–98% | PASS |
| Primary (on time, from day 0) | R3 | next 24 h | 68% | 28500 | 565 | 73.8% | 67.4–80.1% | 63–73% | inconclusive |
| Primary (on time, from day 0) | R4 | next 24 h | 95% | 28500 | 565 | 95.8% | 93.5–98.0% | 92–98% | inconclusive |
| All rows from day 0, including back-filled | R1 | next 1 h | 68% | 31000 | 589 | 72.2% | 69.7–74.8% | 63–73% | inconclusive |
| All rows from day 0, including back-filled | R2 | next 1 h | 95% | 31000 | 589 | 96.2% | 95.2–97.3% | 92–98% | PASS |
| All rows from day 0, including back-filled | R3 | next 24 h | 68% | 29800 | 566 | 73.8% | 67.4–80.1% | 63–73% | inconclusive |
| All rows from day 0, including back-filled | R4 | next 24 h | 95% | 29800 | 566 | 95.8% | 93.5–98.0% | 92–98% | inconclusive |
| Run-in (before day 0) | R1 | next 1 h | 68% | 14250 | 281 | 71.0% | 67.6–74.5% | 63–73% | inconclusive |
| Run-in (before day 0) | R2 | next 1 h | 95% | 14250 | 281 | 95.2% | 93.6–96.8% | 92–98% | PASS |
| Run-in (before day 0) | R3 | next 24 h | 68% | 14250 | 281 | 72.1% | – | 63–73% | too few data yet |
| Run-in (before day 0) | R4 | next 24 h | 95% | 14250 | 281 | 97.3% | – | 92–98% | too few data yet |

Coins furthest from the 68% claim on the 24-hour range (primary sample):

| Coin | Coverage | Forecasts |
|---|---|---|
| ETH | 61% | 570 |
| BTC | 62% | 570 |
| XRP | 63% | 570 |
| TRX | 63% | 570 |
| BNB | 64% | 570 |
| TIA | 82% | 570 |
| FET | 83% | 570 |
| OP | 83% | 570 |
| DOT | 84% | 570 |
| FIL | 87% | 570 |

Information only, not investment advice.
