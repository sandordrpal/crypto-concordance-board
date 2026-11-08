# Live calibration of the board's typical-move ranges

Updated 2026-11-08 13:02 UTC. Rules and pass bands are fixed in [LIVE_TEST.md](https://github.com/sandordrpal/crypto-concordance-board/blob/main/research/LIVE_TEST.md) (R1-R4). Primary analysis: on-time forecasts from 2026-10-19; earlier rows are a run-in.

Coverage is the share of real moves that stayed inside the range. Confidence intervals (90%) are clustered by issue hour, because coins move together. PASS when the whole interval lies inside the band.

| Sample | Test | Horizon | Claimed | Forecasts | Issue hours | Coverage | 90% CI | Pass band | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| Primary (on time, from day 0) | R1 | next 1 h | 68% | 24850 | 492 | 73.0% | 70.2–75.8% | 63–73% | inconclusive |
| Primary (on time, from day 0) | R2 | next 1 h | 95% | 24850 | 492 | 96.5% | 95.4–97.7% | 92–98% | PASS |
| Primary (on time, from day 0) | R3 | next 24 h | 68% | 23700 | 469 | 73.6% | 65.9–81.2% | 63–73% | inconclusive |
| Primary (on time, from day 0) | R4 | next 24 h | 95% | 23700 | 469 | 95.4% | 92.7–98.1% | 92–98% | inconclusive |
| All rows from day 0, including back-filled | R1 | next 1 h | 68% | 26000 | 493 | 73.0% | 70.2–75.8% | 63–73% | inconclusive |
| All rows from day 0, including back-filled | R2 | next 1 h | 95% | 26000 | 493 | 96.5% | 95.4–97.7% | 92–98% | PASS |
| All rows from day 0, including back-filled | R3 | next 24 h | 68% | 24800 | 470 | 73.6% | 66.0–81.1% | 63–73% | inconclusive |
| All rows from day 0, including back-filled | R4 | next 24 h | 95% | 24800 | 470 | 95.4% | 92.7–98.1% | 92–98% | inconclusive |
| Run-in (before day 0) | R1 | next 1 h | 68% | 14250 | 281 | 71.0% | 67.6–74.5% | 63–73% | inconclusive |
| Run-in (before day 0) | R2 | next 1 h | 95% | 14250 | 281 | 95.2% | 93.6–96.8% | 92–98% | PASS |
| Run-in (before day 0) | R3 | next 24 h | 68% | 14250 | 281 | 72.1% | – | 63–73% | too few data yet |
| Run-in (before day 0) | R4 | next 24 h | 95% | 14250 | 281 | 97.3% | – | 92–98% | too few data yet |

Coins furthest from the 68% claim on the 24-hour range (primary sample):

| Coin | Coverage | Forecasts |
|---|---|---|
| TRX | 60% | 474 |
| BTC | 62% | 474 |
| BCH | 62% | 474 |
| BNB | 63% | 474 |
| ETH | 63% | 474 |
| FET | 82% | 474 |
| IMX | 82% | 474 |
| ICP | 82% | 474 |
| DOT | 83% | 474 |
| FIL | 87% | 474 |

Information only, not investment advice.
