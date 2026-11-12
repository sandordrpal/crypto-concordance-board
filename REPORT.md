# Live calibration of the board's typical-move ranges

Updated 2026-11-12 08:02 UTC. Rules and pass bands are fixed in [LIVE_TEST.md](https://github.com/sandordrpal/crypto-concordance-board/blob/main/research/LIVE_TEST.md) (R1-R4). Primary analysis: on-time forecasts from 2026-10-19; earlier rows are a run-in.

Coverage is the share of real moves that stayed inside the range. Confidence intervals (90%) are clustered by issue hour, because coins move together. PASS when the whole interval lies inside the band.

| Sample | Test | Horizon | Claimed | Forecasts | Issue hours | Coverage | 90% CI | Pass band | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| Primary (on time, from day 0) | R1 | next 1 h | 68% | 29400 | 583 | 72.3% | 69.7–74.9% | 63–73% | inconclusive |
| Primary (on time, from day 0) | R2 | next 1 h | 95% | 29400 | 583 | 96.2% | 95.1–97.3% | 92–98% | PASS |
| Primary (on time, from day 0) | R3 | next 24 h | 68% | 28250 | 560 | 73.9% | 67.5–80.3% | 63–73% | inconclusive |
| Primary (on time, from day 0) | R4 | next 24 h | 95% | 28250 | 560 | 95.8% | 93.5–98.0% | 92–98% | inconclusive |
| All rows from day 0, including back-filled | R1 | next 1 h | 68% | 30750 | 584 | 72.3% | 69.7–74.9% | 63–73% | inconclusive |
| All rows from day 0, including back-filled | R2 | next 1 h | 95% | 30750 | 584 | 96.2% | 95.1–97.3% | 92–98% | PASS |
| All rows from day 0, including back-filled | R3 | next 24 h | 68% | 29550 | 561 | 73.9% | 67.5–80.3% | 63–73% | inconclusive |
| All rows from day 0, including back-filled | R4 | next 24 h | 95% | 29550 | 561 | 95.8% | 93.5–98.0% | 92–98% | inconclusive |
| Run-in (before day 0) | R1 | next 1 h | 68% | 14250 | 281 | 71.0% | 67.6–74.5% | 63–73% | inconclusive |
| Run-in (before day 0) | R2 | next 1 h | 95% | 14250 | 281 | 95.2% | 93.6–96.8% | 92–98% | PASS |
| Run-in (before day 0) | R3 | next 24 h | 68% | 14250 | 281 | 72.1% | – | 63–73% | too few data yet |
| Run-in (before day 0) | R4 | next 24 h | 95% | 14250 | 281 | 97.3% | – | 92–98% | too few data yet |

Coins furthest from the 68% claim on the 24-hour range (primary sample):

| Coin | Coverage | Forecasts |
|---|---|---|
| ETH | 60% | 565 |
| BTC | 61% | 565 |
| XRP | 63% | 565 |
| TRX | 63% | 565 |
| BNB | 64% | 565 |
| FET | 82% | 565 |
| TIA | 83% | 565 |
| DOT | 83% | 565 |
| OP | 84% | 565 |
| FIL | 87% | 565 |

Information only, not investment advice.
