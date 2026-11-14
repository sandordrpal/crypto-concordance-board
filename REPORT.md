# Live calibration of the board's typical-move ranges

Updated 2026-11-14 10:02 UTC. Rules and pass bands are fixed in [LIVE_TEST.md](https://github.com/sandordrpal/crypto-concordance-board/blob/main/research/LIVE_TEST.md) (R1-R4). Primary analysis: on-time forecasts from 2026-10-19; earlier rows are a run-in.

Coverage is the share of real moves that stayed inside the range. Confidence intervals (90%) are clustered by issue hour, because coins move together. PASS when the whole interval lies inside the band.

| Sample | Test | Horizon | Claimed | Forecasts | Issue hours | Coverage | 90% CI | Pass band | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| Primary (on time, from day 0) | R1 | next 1 h | 68% | 31950 | 633 | 71.1% | 68.6–73.7% | 63–73% | inconclusive |
| Primary (on time, from day 0) | R2 | next 1 h | 95% | 31950 | 633 | 96.0% | 94.9–97.1% | 92–98% | PASS |
| Primary (on time, from day 0) | R3 | next 24 h | 68% | 30750 | 610 | 72.8% | 66.8–78.8% | 63–73% | inconclusive |
| Primary (on time, from day 0) | R4 | next 24 h | 95% | 30750 | 610 | 95.7% | 93.6–97.8% | 92–98% | PASS |
| All rows from day 0, including back-filled | R1 | next 1 h | 68% | 33400 | 634 | 71.1% | 68.6–73.7% | 63–73% | inconclusive |
| All rows from day 0, including back-filled | R2 | next 1 h | 95% | 33400 | 634 | 96.0% | 94.9–97.1% | 92–98% | PASS |
| All rows from day 0, including back-filled | R3 | next 24 h | 68% | 32150 | 611 | 72.8% | 66.8–78.8% | 63–73% | inconclusive |
| All rows from day 0, including back-filled | R4 | next 24 h | 95% | 32150 | 611 | 95.7% | 93.6–97.8% | 92–98% | PASS |
| Run-in (before day 0) | R1 | next 1 h | 68% | 14250 | 281 | 71.0% | 67.6–74.5% | 63–73% | inconclusive |
| Run-in (before day 0) | R2 | next 1 h | 95% | 14250 | 281 | 95.2% | 93.6–96.8% | 92–98% | PASS |
| Run-in (before day 0) | R3 | next 24 h | 68% | 14250 | 281 | 72.1% | – | 63–73% | too few data yet |
| Run-in (before day 0) | R4 | next 24 h | 95% | 14250 | 281 | 97.3% | – | 92–98% | too few data yet |

Coins furthest from the 68% claim on the 24-hour range (primary sample):

| Coin | Coverage | Forecasts |
|---|---|---|
| BTC | 57% | 615 |
| ETH | 58% | 615 |
| BNB | 59% | 615 |
| TRX | 63% | 615 |
| XRP | 63% | 615 |
| WLD | 81% | 615 |
| OP | 81% | 615 |
| DOT | 82% | 615 |
| FET | 83% | 615 |
| FIL | 85% | 615 |

Information only, not investment advice.
