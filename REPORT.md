# Live calibration of the board's typical-move ranges

Updated 2026-11-14 15:02 UTC. Rules and pass bands are fixed in [LIVE_TEST.md](https://github.com/sandordrpal/crypto-concordance-board/blob/main/research/LIVE_TEST.md) (R1-R4). Primary analysis: on-time forecasts from 2026-10-19; earlier rows are a run-in.

Coverage is the share of real moves that stayed inside the range. Confidence intervals (90%) are clustered by issue hour, because coins move together. PASS when the whole interval lies inside the band.

| Sample | Test | Horizon | Claimed | Forecasts | Issue hours | Coverage | 90% CI | Pass band | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| Primary (on time, from day 0) | R1 | next 1 h | 68% | 32200 | 638 | 70.9% | 68.4–73.5% | 63–73% | inconclusive |
| Primary (on time, from day 0) | R2 | next 1 h | 95% | 32200 | 638 | 95.9% | 94.9–97.0% | 92–98% | PASS |
| Primary (on time, from day 0) | R3 | next 24 h | 68% | 31000 | 615 | 72.3% | 66.3–78.4% | 63–73% | inconclusive |
| Primary (on time, from day 0) | R4 | next 24 h | 95% | 31000 | 615 | 95.6% | 93.5–97.6% | 92–98% | PASS |
| All rows from day 0, including back-filled | R1 | next 1 h | 68% | 33650 | 639 | 70.9% | 68.4–73.5% | 63–73% | inconclusive |
| All rows from day 0, including back-filled | R2 | next 1 h | 95% | 33650 | 639 | 95.9% | 94.9–97.0% | 92–98% | PASS |
| All rows from day 0, including back-filled | R3 | next 24 h | 68% | 32400 | 616 | 72.3% | 66.3–78.4% | 63–73% | inconclusive |
| All rows from day 0, including back-filled | R4 | next 24 h | 95% | 32400 | 616 | 95.6% | 93.5–97.6% | 92–98% | PASS |
| Run-in (before day 0) | R1 | next 1 h | 68% | 14250 | 281 | 71.0% | 67.6–74.5% | 63–73% | inconclusive |
| Run-in (before day 0) | R2 | next 1 h | 95% | 14250 | 281 | 95.2% | 93.6–96.8% | 92–98% | PASS |
| Run-in (before day 0) | R3 | next 24 h | 68% | 14250 | 281 | 72.1% | – | 63–73% | too few data yet |
| Run-in (before day 0) | R4 | next 24 h | 95% | 14250 | 281 | 97.3% | – | 92–98% | too few data yet |

Coins furthest from the 68% claim on the 24-hour range (primary sample):

| Coin | Coverage | Forecasts |
|---|---|---|
| BTC | 57% | 620 |
| ETH | 57% | 620 |
| BNB | 59% | 620 |
| XRP | 62% | 620 |
| TRX | 63% | 620 |
| WLD | 80% | 620 |
| OP | 81% | 620 |
| DOT | 82% | 620 |
| FET | 82% | 620 |
| FIL | 84% | 620 |

Information only, not investment advice.
