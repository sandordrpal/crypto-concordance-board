# Live calibration of the board's typical-move ranges

Updated 2026-11-10 09:02 UTC. Rules and pass bands are fixed in [LIVE_TEST.md](https://github.com/sandordrpal/crypto-concordance-board/blob/main/research/LIVE_TEST.md) (R1-R4). Primary analysis: on-time forecasts from 2026-10-19; earlier rows are a run-in.

Coverage is the share of real moves that stayed inside the range. Confidence intervals (90%) are clustered by issue hour, because coins move together. PASS when the whole interval lies inside the band.

| Sample | Test | Horizon | Claimed | Forecasts | Issue hours | Coverage | 90% CI | Pass band | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| Primary (on time, from day 0) | R1 | next 1 h | 68% | 27050 | 536 | 72.5% | 69.8–75.3% | 63–73% | inconclusive |
| Primary (on time, from day 0) | R2 | next 1 h | 95% | 27050 | 536 | 96.2% | 95.1–97.4% | 92–98% | PASS |
| Primary (on time, from day 0) | R3 | next 24 h | 68% | 25900 | 513 | 73.8% | 66.8–80.8% | 63–73% | inconclusive |
| Primary (on time, from day 0) | R4 | next 24 h | 95% | 25900 | 513 | 95.7% | 93.2–98.2% | 92–98% | inconclusive |
| All rows from day 0, including back-filled | R1 | next 1 h | 68% | 28300 | 537 | 72.5% | 69.8–75.3% | 63–73% | inconclusive |
| All rows from day 0, including back-filled | R2 | next 1 h | 95% | 28300 | 537 | 96.3% | 95.1–97.4% | 92–98% | PASS |
| All rows from day 0, including back-filled | R3 | next 24 h | 68% | 27100 | 514 | 73.8% | 66.9–80.8% | 63–73% | inconclusive |
| All rows from day 0, including back-filled | R4 | next 24 h | 95% | 27100 | 514 | 95.7% | 93.2–98.2% | 92–98% | inconclusive |
| Run-in (before day 0) | R1 | next 1 h | 68% | 14250 | 281 | 71.0% | 67.6–74.5% | 63–73% | inconclusive |
| Run-in (before day 0) | R2 | next 1 h | 95% | 14250 | 281 | 95.2% | 93.6–96.8% | 92–98% | PASS |
| Run-in (before day 0) | R3 | next 24 h | 68% | 14250 | 281 | 72.1% | – | 63–73% | too few data yet |
| Run-in (before day 0) | R4 | next 24 h | 95% | 14250 | 281 | 97.3% | – | 92–98% | too few data yet |

Coins furthest from the 68% claim on the 24-hour range (primary sample):

| Coin | Coverage | Forecasts |
|---|---|---|
| TRX | 60% | 518 |
| BTC | 61% | 518 |
| ETH | 62% | 518 |
| BNB | 63% | 518 |
| BCH | 64% | 518 |
| FET | 82% | 518 |
| IMX | 82% | 518 |
| OP | 83% | 518 |
| DOT | 83% | 518 |
| FIL | 86% | 518 |

Information only, not investment advice.
