# Live calibration of the board's typical-move ranges

Updated 2026-11-07 22:02 UTC. Rules and pass bands are fixed in [LIVE_TEST.md](https://github.com/sandordrpal/crypto-concordance-board/blob/main/research/LIVE_TEST.md) (R1-R4). Primary analysis: on-time forecasts from 2026-10-19; earlier rows are a run-in.

Coverage is the share of real moves that stayed inside the range. Confidence intervals (90%) are clustered by issue hour, because coins move together. PASS when the whole interval lies inside the band.

| Sample | Test | Horizon | Claimed | Forecasts | Issue hours | Coverage | 90% CI | Pass band | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| Primary (on time, from day 0) | R1 | next 1 h | 68% | 24100 | 477 | 72.5% | 69.6–75.4% | 63–73% | inconclusive |
| Primary (on time, from day 0) | R2 | next 1 h | 95% | 24100 | 477 | 96.4% | 95.2–97.6% | 92–98% | PASS |
| Primary (on time, from day 0) | R3 | next 24 h | 68% | 22900 | 454 | 72.9% | 65.1–80.6% | 63–73% | inconclusive |
| Primary (on time, from day 0) | R4 | next 24 h | 95% | 22900 | 454 | 95.2% | 92.5–98.0% | 92–98% | inconclusive |
| All rows from day 0, including back-filled | R1 | next 1 h | 68% | 25200 | 478 | 72.5% | 69.7–75.4% | 63–73% | inconclusive |
| All rows from day 0, including back-filled | R2 | next 1 h | 95% | 25200 | 478 | 96.4% | 95.2–97.6% | 92–98% | PASS |
| All rows from day 0, including back-filled | R3 | next 24 h | 68% | 23950 | 455 | 72.9% | 65.2–80.5% | 63–73% | inconclusive |
| All rows from day 0, including back-filled | R4 | next 24 h | 95% | 23950 | 455 | 95.3% | 92.5–98.0% | 92–98% | PASS |
| Run-in (before day 0) | R1 | next 1 h | 68% | 14250 | 281 | 71.0% | 67.6–74.5% | 63–73% | inconclusive |
| Run-in (before day 0) | R2 | next 1 h | 95% | 14250 | 281 | 95.2% | 93.6–96.8% | 92–98% | PASS |
| Run-in (before day 0) | R3 | next 24 h | 68% | 14250 | 281 | 72.1% | – | 63–73% | too few data yet |
| Run-in (before day 0) | R4 | next 24 h | 95% | 14250 | 281 | 97.3% | – | 92–98% | too few data yet |

Coins furthest from the 68% claim on the 24-hour range (primary sample):

| Coin | Coverage | Forecasts |
|---|---|---|
| TRX | 60% | 458 |
| BTC | 60% | 458 |
| BNB | 62% | 458 |
| ETH | 62% | 458 |
| XRP | 64% | 458 |
| FET | 81% | 458 |
| IMX | 81% | 458 |
| ICP | 81% | 458 |
| DOT | 82% | 458 |
| FIL | 86% | 458 |

Information only, not investment advice.
