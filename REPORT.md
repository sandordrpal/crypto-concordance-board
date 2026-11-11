# Live calibration of the board's typical-move ranges

Updated 2026-11-11 01:02 UTC. Rules and pass bands are fixed in [LIVE_TEST.md](https://github.com/sandordrpal/crypto-concordance-board/blob/main/research/LIVE_TEST.md) (R1-R4). Primary analysis: on-time forecasts from 2026-10-19; earlier rows are a run-in.

Coverage is the share of real moves that stayed inside the range. Confidence intervals (90%) are clustered by issue hour, because coins move together. PASS when the whole interval lies inside the band.

| Sample | Test | Horizon | Claimed | Forecasts | Issue hours | Coverage | 90% CI | Pass band | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| Primary (on time, from day 0) | R1 | next 1 h | 68% | 27850 | 552 | 72.3% | 69.5–75.0% | 63–73% | inconclusive |
| Primary (on time, from day 0) | R2 | next 1 h | 95% | 27850 | 552 | 96.1% | 95.0–97.3% | 92–98% | PASS |
| Primary (on time, from day 0) | R3 | next 24 h | 68% | 26700 | 529 | 73.6% | 66.8–80.4% | 63–73% | inconclusive |
| Primary (on time, from day 0) | R4 | next 24 h | 95% | 26700 | 529 | 95.7% | 93.3–98.1% | 92–98% | inconclusive |
| All rows from day 0, including back-filled | R1 | next 1 h | 68% | 29150 | 553 | 72.3% | 69.6–75.0% | 63–73% | inconclusive |
| All rows from day 0, including back-filled | R2 | next 1 h | 95% | 29150 | 553 | 96.1% | 95.0–97.3% | 92–98% | PASS |
| All rows from day 0, including back-filled | R3 | next 24 h | 68% | 27950 | 530 | 73.6% | 66.8–80.3% | 63–73% | inconclusive |
| All rows from day 0, including back-filled | R4 | next 24 h | 95% | 27950 | 530 | 95.7% | 93.3–98.1% | 92–98% | inconclusive |
| Run-in (before day 0) | R1 | next 1 h | 68% | 14250 | 281 | 71.0% | 67.6–74.5% | 63–73% | inconclusive |
| Run-in (before day 0) | R2 | next 1 h | 95% | 14250 | 281 | 95.2% | 93.6–96.8% | 92–98% | PASS |
| Run-in (before day 0) | R3 | next 24 h | 68% | 14250 | 281 | 72.1% | – | 63–73% | too few data yet |
| Run-in (before day 0) | R4 | next 24 h | 95% | 14250 | 281 | 97.3% | – | 92–98% | too few data yet |

Coins furthest from the 68% claim on the 24-hour range (primary sample):

| Coin | Coverage | Forecasts |
|---|---|---|
| BTC | 60% | 534 |
| ETH | 60% | 534 |
| TRX | 61% | 534 |
| BNB | 63% | 534 |
| XRP | 63% | 534 |
| TIA | 82% | 534 |
| FET | 83% | 534 |
| DOT | 83% | 534 |
| OP | 83% | 534 |
| FIL | 86% | 534 |

Information only, not investment advice.
