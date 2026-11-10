# Live calibration of the board's typical-move ranges

Updated 2026-11-10 02:02 UTC. Rules and pass bands are fixed in [LIVE_TEST.md](https://github.com/sandordrpal/crypto-concordance-board/blob/main/research/LIVE_TEST.md) (R1-R4). Primary analysis: on-time forecasts from 2026-10-19; earlier rows are a run-in.

Coverage is the share of real moves that stayed inside the range. Confidence intervals (90%) are clustered by issue hour, because coins move together. PASS when the whole interval lies inside the band.

| Sample | Test | Horizon | Claimed | Forecasts | Issue hours | Coverage | 90% CI | Pass band | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| Primary (on time, from day 0) | R1 | next 1 h | 68% | 26700 | 529 | 72.4% | 69.6–75.2% | 63–73% | inconclusive |
| Primary (on time, from day 0) | R2 | next 1 h | 95% | 26700 | 529 | 96.2% | 95.0–97.4% | 92–98% | PASS |
| Primary (on time, from day 0) | R3 | next 24 h | 68% | 25550 | 506 | 73.8% | 66.7–80.9% | 63–73% | inconclusive |
| Primary (on time, from day 0) | R4 | next 24 h | 95% | 25550 | 506 | 95.6% | 93.1–98.2% | 92–98% | inconclusive |
| All rows from day 0, including back-filled | R1 | next 1 h | 68% | 27950 | 530 | 72.4% | 69.6–75.2% | 63–73% | inconclusive |
| All rows from day 0, including back-filled | R2 | next 1 h | 95% | 27950 | 530 | 96.2% | 95.1–97.4% | 92–98% | PASS |
| All rows from day 0, including back-filled | R3 | next 24 h | 68% | 26750 | 507 | 73.8% | 66.7–80.8% | 63–73% | inconclusive |
| All rows from day 0, including back-filled | R4 | next 24 h | 95% | 26750 | 507 | 95.6% | 93.1–98.1% | 92–98% | inconclusive |
| Run-in (before day 0) | R1 | next 1 h | 68% | 14250 | 281 | 71.0% | 67.6–74.5% | 63–73% | inconclusive |
| Run-in (before day 0) | R2 | next 1 h | 95% | 14250 | 281 | 95.2% | 93.6–96.8% | 92–98% | PASS |
| Run-in (before day 0) | R3 | next 24 h | 68% | 14250 | 281 | 72.1% | – | 63–73% | too few data yet |
| Run-in (before day 0) | R4 | next 24 h | 95% | 14250 | 281 | 97.3% | – | 92–98% | too few data yet |

Coins furthest from the 68% claim on the 24-hour range (primary sample):

| Coin | Coverage | Forecasts |
|---|---|---|
| TRX | 60% | 511 |
| BTC | 61% | 511 |
| ETH | 61% | 511 |
| BNB | 63% | 511 |
| BCH | 63% | 511 |
| FET | 82% | 511 |
| OP | 82% | 511 |
| DOT | 83% | 511 |
| IMX | 83% | 511 |
| FIL | 86% | 511 |

Information only, not investment advice.
