# Live calibration of the board's typical-move ranges

Updated 2026-11-14 21:02 UTC. Rules and pass bands are fixed in [LIVE_TEST.md](https://github.com/sandordrpal/crypto-concordance-board/blob/main/research/LIVE_TEST.md) (R1-R4). Primary analysis: on-time forecasts from 2026-10-19; earlier rows are a run-in.

Coverage is the share of real moves that stayed inside the range. Confidence intervals (90%) are clustered by issue hour, because coins move together. PASS when the whole interval lies inside the band.

| Sample | Test | Horizon | Claimed | Forecasts | Issue hours | Coverage | 90% CI | Pass band | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| Primary (on time, from day 0) | R1 | next 1 h | 68% | 32500 | 644 | 70.6% | 68.0–73.2% | 63–73% | inconclusive |
| Primary (on time, from day 0) | R2 | next 1 h | 95% | 32500 | 644 | 95.7% | 94.5–96.8% | 92–98% | PASS |
| Primary (on time, from day 0) | R3 | next 24 h | 68% | 31300 | 621 | 71.7% | 65.4–77.9% | 63–73% | inconclusive |
| Primary (on time, from day 0) | R4 | next 24 h | 95% | 31300 | 621 | 94.9% | 92.5–97.3% | 92–98% | PASS |
| All rows from day 0, including back-filled | R1 | next 1 h | 68% | 33950 | 645 | 70.6% | 68.1–73.2% | 63–73% | inconclusive |
| All rows from day 0, including back-filled | R2 | next 1 h | 95% | 33950 | 645 | 95.7% | 94.5–96.8% | 92–98% | PASS |
| All rows from day 0, including back-filled | R3 | next 24 h | 68% | 32700 | 622 | 71.7% | 65.5–77.9% | 63–73% | inconclusive |
| All rows from day 0, including back-filled | R4 | next 24 h | 95% | 32700 | 622 | 94.9% | 92.5–97.3% | 92–98% | PASS |
| Run-in (before day 0) | R1 | next 1 h | 68% | 14250 | 281 | 71.0% | 67.6–74.5% | 63–73% | inconclusive |
| Run-in (before day 0) | R2 | next 1 h | 95% | 14250 | 281 | 95.2% | 93.6–96.8% | 92–98% | PASS |
| Run-in (before day 0) | R3 | next 24 h | 68% | 14250 | 281 | 72.1% | – | 63–73% | too few data yet |
| Run-in (before day 0) | R4 | next 24 h | 95% | 14250 | 281 | 97.3% | – | 92–98% | too few data yet |

Coins furthest from the 68% claim on the 24-hour range (primary sample):

| Coin | Coverage | Forecasts |
|---|---|---|
| BTC | 56% | 626 |
| ETH | 57% | 626 |
| BNB | 58% | 626 |
| XRP | 62% | 626 |
| TRX | 62% | 626 |
| WLD | 80% | 626 |
| OP | 80% | 626 |
| DOT | 81% | 626 |
| FET | 81% | 626 |
| FIL | 83% | 626 |

Information only, not investment advice.
