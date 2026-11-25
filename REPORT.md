# Live calibration of the board's typical-move ranges

Updated 2026-11-25 13:02 UTC. Rules and pass bands are fixed in [LIVE_TEST.md](https://github.com/sandordrpal/crypto-concordance-board/blob/main/research/LIVE_TEST.md) (R1-R4). Primary analysis: on-time forecasts from 2026-10-19; earlier rows are a run-in.

Coverage is the share of real moves that stayed inside the range. Confidence intervals (90%) are clustered by issue hour, because coins move together. PASS when the whole interval lies inside the band.

| Sample | Test | Horizon | Claimed | Forecasts | Issue hours | Coverage | 90% CI | Pass band | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| Primary (on time, from day 0) | R1 | next 1 h | 68% | 45450 | 900 | 67.9% | 65.6–70.1% | 63–73% | PASS |
| Primary (on time, from day 0) | R2 | next 1 h | 95% | 45450 | 900 | 94.9% | 93.8–96.0% | 92–98% | PASS |
| Primary (on time, from day 0) | R3 | next 24 h | 68% | 44250 | 877 | 68.4% | 62.2–74.6% | 63–73% | inconclusive |
| Primary (on time, from day 0) | R4 | next 24 h | 95% | 44250 | 877 | 93.6% | 90.7–96.6% | 92–98% | inconclusive |
| All rows from day 0, including back-filled | R1 | next 1 h | 68% | 47450 | 901 | 67.9% | 65.6–70.2% | 63–73% | PASS |
| All rows from day 0, including back-filled | R2 | next 1 h | 95% | 47450 | 901 | 94.9% | 93.8–96.0% | 92–98% | PASS |
| All rows from day 0, including back-filled | R3 | next 24 h | 68% | 46200 | 878 | 68.4% | 62.2–74.6% | 63–73% | inconclusive |
| All rows from day 0, including back-filled | R4 | next 24 h | 95% | 46200 | 878 | 93.6% | 90.7–96.6% | 92–98% | inconclusive |
| Run-in (before day 0) | R1 | next 1 h | 68% | 14250 | 281 | 71.0% | 67.6–74.5% | 63–73% | inconclusive |
| Run-in (before day 0) | R2 | next 1 h | 95% | 14250 | 281 | 95.2% | 93.6–96.8% | 92–98% | PASS |
| Run-in (before day 0) | R3 | next 24 h | 68% | 14250 | 281 | 72.1% | – | 63–73% | too few data yet |
| Run-in (before day 0) | R4 | next 24 h | 95% | 14250 | 281 | 97.3% | – | 92–98% | too few data yet |

Coins furthest from the 68% claim on the 24-hour range (primary sample):

| Coin | Coverage | Forecasts |
|---|---|---|
| BTC | 55% | 885 |
| ETH | 58% | 885 |
| BNB | 58% | 885 |
| TRX | 59% | 885 |
| SOL | 60% | 885 |
| DOT | 75% | 885 |
| WLD | 76% | 885 |
| OP | 76% | 885 |
| TIA | 76% | 885 |
| FET | 77% | 885 |

Information only, not investment advice.
