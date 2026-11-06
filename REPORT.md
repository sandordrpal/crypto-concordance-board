# Live calibration of the board's typical-move ranges

Updated 2026-11-06 23:02 UTC. Rules and pass bands are fixed in [LIVE_TEST.md](https://github.com/sandordrpal/crypto-concordance-board/blob/main/research/LIVE_TEST.md) (R1-R4). Primary analysis: on-time forecasts from 2026-10-19; earlier rows are a run-in.

Coverage is the share of real moves that stayed inside the range. Confidence intervals (90%) are clustered by issue hour, because coins move together. PASS when the whole interval lies inside the band.

| Sample | Test | Horizon | Claimed | Forecasts | Issue hours | Coverage | 90% CI | Pass band | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| Primary (on time, from day 0) | R1 | next 1 h | 68% | 22900 | 454 | 71.7% | 68.8–74.7% | 63–73% | inconclusive |
| Primary (on time, from day 0) | R2 | next 1 h | 95% | 22900 | 454 | 96.2% | 95.0–97.5% | 92–98% | PASS |
| Primary (on time, from day 0) | R3 | next 24 h | 68% | 21700 | 431 | 71.8% | 63.8–79.8% | 63–73% | inconclusive |
| Primary (on time, from day 0) | R4 | next 24 h | 95% | 21700 | 431 | 95.0% | 92.1–97.9% | 92–98% | PASS |
| All rows from day 0, including back-filled | R1 | next 1 h | 68% | 23950 | 455 | 71.8% | 68.9–74.7% | 63–73% | inconclusive |
| All rows from day 0, including back-filled | R2 | next 1 h | 95% | 23950 | 455 | 96.3% | 95.0–97.5% | 92–98% | PASS |
| All rows from day 0, including back-filled | R3 | next 24 h | 68% | 22700 | 432 | 71.8% | 63.8–79.8% | 63–73% | inconclusive |
| All rows from day 0, including back-filled | R4 | next 24 h | 95% | 22700 | 432 | 95.0% | 92.1–97.9% | 92–98% | PASS |
| Run-in (before day 0) | R1 | next 1 h | 68% | 14250 | 281 | 71.0% | 67.6–74.5% | 63–73% | inconclusive |
| Run-in (before day 0) | R2 | next 1 h | 95% | 14250 | 281 | 95.2% | 93.6–96.8% | 92–98% | PASS |
| Run-in (before day 0) | R3 | next 24 h | 68% | 14250 | 281 | 72.1% | – | 63–73% | too few data yet |
| Run-in (before day 0) | R4 | next 24 h | 95% | 14250 | 281 | 97.3% | – | 92–98% | too few data yet |

Coins furthest from the 68% claim on the 24-hour range (primary sample):

| Coin | Coverage | Forecasts |
|---|---|---|
| TRX | 57% | 434 |
| BTC | 58% | 434 |
| BNB | 59% | 434 |
| ETH | 60% | 434 |
| PEPE | 63% | 434 |
| ICP | 80% | 434 |
| IMX | 80% | 434 |
| OP | 80% | 434 |
| DOT | 82% | 434 |
| FIL | 86% | 434 |

Information only, not investment advice.
