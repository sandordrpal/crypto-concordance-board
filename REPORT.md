# Live calibration of the board's typical-move ranges

Updated 2026-11-15 01:02 UTC. Rules and pass bands are fixed in [LIVE_TEST.md](https://github.com/sandordrpal/crypto-concordance-board/blob/main/research/LIVE_TEST.md) (R1-R4). Primary analysis: on-time forecasts from 2026-10-19; earlier rows are a run-in.

Coverage is the share of real moves that stayed inside the range. Confidence intervals (90%) are clustered by issue hour, because coins move together. PASS when the whole interval lies inside the band.

| Sample | Test | Horizon | Claimed | Forecasts | Issue hours | Coverage | 90% CI | Pass band | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| Primary (on time, from day 0) | R1 | next 1 h | 68% | 32700 | 648 | 70.3% | 67.7–73.0% | 63–73% | PASS |
| Primary (on time, from day 0) | R2 | next 1 h | 95% | 32700 | 648 | 95.5% | 94.3–96.7% | 92–98% | PASS |
| Primary (on time, from day 0) | R3 | next 24 h | 68% | 31550 | 625 | 71.2% | 64.8–77.6% | 63–73% | inconclusive |
| Primary (on time, from day 0) | R4 | next 24 h | 95% | 31550 | 625 | 94.3% | 91.4–97.2% | 92–98% | inconclusive |
| All rows from day 0, including back-filled | R1 | next 1 h | 68% | 34200 | 649 | 70.4% | 67.7–73.0% | 63–73% | PASS |
| All rows from day 0, including back-filled | R2 | next 1 h | 95% | 34200 | 649 | 95.5% | 94.3–96.7% | 92–98% | PASS |
| All rows from day 0, including back-filled | R3 | next 24 h | 68% | 33000 | 626 | 71.2% | 64.8–77.6% | 63–73% | inconclusive |
| All rows from day 0, including back-filled | R4 | next 24 h | 95% | 33000 | 626 | 94.3% | 91.4–97.2% | 92–98% | inconclusive |
| Run-in (before day 0) | R1 | next 1 h | 68% | 14250 | 281 | 71.0% | 67.6–74.5% | 63–73% | inconclusive |
| Run-in (before day 0) | R2 | next 1 h | 95% | 14250 | 281 | 95.2% | 93.6–96.8% | 92–98% | PASS |
| Run-in (before day 0) | R3 | next 24 h | 68% | 14250 | 281 | 72.1% | – | 63–73% | too few data yet |
| Run-in (before day 0) | R4 | next 24 h | 95% | 14250 | 281 | 97.3% | – | 92–98% | too few data yet |

Coins furthest from the 68% claim on the 24-hour range (primary sample):

| Coin | Coverage | Forecasts |
|---|---|---|
| BTC | 56% | 631 |
| ETH | 56% | 631 |
| BNB | 58% | 631 |
| XRP | 61% | 631 |
| TRX | 62% | 631 |
| WLD | 79% | 631 |
| OP | 79% | 631 |
| DOT | 80% | 631 |
| FET | 81% | 631 |
| FIL | 83% | 631 |

Information only, not investment advice.
