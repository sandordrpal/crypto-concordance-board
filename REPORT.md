# Live calibration of the board's typical-move ranges

Updated 2026-11-20 05:02 UTC. Rules and pass bands are fixed in [LIVE_TEST.md](https://github.com/sandordrpal/crypto-concordance-board/blob/main/research/LIVE_TEST.md) (R1-R4). Primary analysis: on-time forecasts from 2026-10-19; earlier rows are a run-in.

Coverage is the share of real moves that stayed inside the range. Confidence intervals (90%) are clustered by issue hour, because coins move together. PASS when the whole interval lies inside the band.

| Sample | Test | Horizon | Claimed | Forecasts | Issue hours | Coverage | 90% CI | Pass band | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| Primary (on time, from day 0) | R1 | next 1 h | 68% | 38950 | 772 | 68.6% | 66.2–71.1% | 63–73% | PASS |
| Primary (on time, from day 0) | R2 | next 1 h | 95% | 38950 | 772 | 95.3% | 94.2–96.4% | 92–98% | PASS |
| Primary (on time, from day 0) | R3 | next 24 h | 68% | 37750 | 749 | 71.9% | 65.8–78.1% | 63–73% | inconclusive |
| Primary (on time, from day 0) | R4 | next 24 h | 95% | 37750 | 749 | 94.4% | 91.5–97.4% | 92–98% | inconclusive |
| All rows from day 0, including back-filled | R1 | next 1 h | 68% | 40700 | 773 | 68.6% | 66.2–71.1% | 63–73% | PASS |
| All rows from day 0, including back-filled | R2 | next 1 h | 95% | 40700 | 773 | 95.3% | 94.2–96.4% | 92–98% | PASS |
| All rows from day 0, including back-filled | R3 | next 24 h | 68% | 39450 | 750 | 72.0% | 65.8–78.1% | 63–73% | inconclusive |
| All rows from day 0, including back-filled | R4 | next 24 h | 95% | 39450 | 750 | 94.4% | 91.5–97.4% | 92–98% | inconclusive |
| Run-in (before day 0) | R1 | next 1 h | 68% | 14250 | 281 | 71.0% | 67.6–74.5% | 63–73% | inconclusive |
| Run-in (before day 0) | R2 | next 1 h | 95% | 14250 | 281 | 95.2% | 93.6–96.8% | 92–98% | PASS |
| Run-in (before day 0) | R3 | next 24 h | 68% | 14250 | 281 | 72.1% | – | 63–73% | too few data yet |
| Run-in (before day 0) | R4 | next 24 h | 95% | 14250 | 281 | 97.3% | – | 92–98% | too few data yet |

Coins furthest from the 68% claim on the 24-hour range (primary sample):

| Coin | Coverage | Forecasts |
|---|---|---|
| BTC | 57% | 755 |
| ETH | 60% | 755 |
| TRX | 60% | 755 |
| BNB | 61% | 755 |
| SOL | 63% | 755 |
| WLD | 79% | 755 |
| TIA | 79% | 755 |
| DOT | 80% | 755 |
| FET | 80% | 755 |
| FIL | 80% | 755 |

Information only, not investment advice.
