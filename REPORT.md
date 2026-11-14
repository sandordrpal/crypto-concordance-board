# Live calibration of the board's typical-move ranges

Updated 2026-11-14 22:02 UTC. Rules and pass bands are fixed in [LIVE_TEST.md](https://github.com/sandordrpal/crypto-concordance-board/blob/main/research/LIVE_TEST.md) (R1-R4). Primary analysis: on-time forecasts from 2026-10-19; earlier rows are a run-in.

Coverage is the share of real moves that stayed inside the range. Confidence intervals (90%) are clustered by issue hour, because coins move together. PASS when the whole interval lies inside the band.

| Sample | Test | Horizon | Claimed | Forecasts | Issue hours | Coverage | 90% CI | Pass band | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| Primary (on time, from day 0) | R1 | next 1 h | 68% | 32550 | 645 | 70.6% | 68.0–73.2% | 63–73% | inconclusive |
| Primary (on time, from day 0) | R2 | next 1 h | 95% | 32550 | 645 | 95.7% | 94.5–96.8% | 92–98% | PASS |
| Primary (on time, from day 0) | R3 | next 24 h | 68% | 31350 | 622 | 71.5% | 65.3–77.8% | 63–73% | inconclusive |
| Primary (on time, from day 0) | R4 | next 24 h | 95% | 31350 | 622 | 94.7% | 92.2–97.3% | 92–98% | PASS |
| All rows from day 0, including back-filled | R1 | next 1 h | 68% | 34000 | 646 | 70.6% | 68.1–73.2% | 63–73% | inconclusive |
| All rows from day 0, including back-filled | R2 | next 1 h | 95% | 34000 | 646 | 95.7% | 94.5–96.8% | 92–98% | PASS |
| All rows from day 0, including back-filled | R3 | next 24 h | 68% | 32750 | 623 | 71.6% | 65.3–77.8% | 63–73% | inconclusive |
| All rows from day 0, including back-filled | R4 | next 24 h | 95% | 32750 | 623 | 94.7% | 92.2–97.3% | 92–98% | PASS |
| Run-in (before day 0) | R1 | next 1 h | 68% | 14250 | 281 | 71.0% | 67.6–74.5% | 63–73% | inconclusive |
| Run-in (before day 0) | R2 | next 1 h | 95% | 14250 | 281 | 95.2% | 93.6–96.8% | 92–98% | PASS |
| Run-in (before day 0) | R3 | next 24 h | 68% | 14250 | 281 | 72.1% | – | 63–73% | too few data yet |
| Run-in (before day 0) | R4 | next 24 h | 95% | 14250 | 281 | 97.3% | – | 92–98% | too few data yet |

Coins furthest from the 68% claim on the 24-hour range (primary sample):

| Coin | Coverage | Forecasts |
|---|---|---|
| BTC | 56% | 627 |
| ETH | 57% | 627 |
| BNB | 58% | 627 |
| XRP | 62% | 627 |
| TRX | 62% | 627 |
| WLD | 79% | 627 |
| OP | 80% | 627 |
| DOT | 81% | 627 |
| FET | 81% | 627 |
| FIL | 83% | 627 |

Information only, not investment advice.
