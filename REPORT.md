# Live calibration of the board's typical-move ranges

Updated 2026-11-20 22:02 UTC. Rules and pass bands are fixed in [LIVE_TEST.md](https://github.com/sandordrpal/crypto-concordance-board/blob/main/research/LIVE_TEST.md) (R1-R4). Primary analysis: on-time forecasts from 2026-10-19; earlier rows are a run-in.

Coverage is the share of real moves that stayed inside the range. Confidence intervals (90%) are clustered by issue hour, because coins move together. PASS when the whole interval lies inside the band.

| Sample | Test | Horizon | Claimed | Forecasts | Issue hours | Coverage | 90% CI | Pass band | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| Primary (on time, from day 0) | R1 | next 1 h | 68% | 39800 | 789 | 68.3% | 65.9–70.7% | 63–73% | PASS |
| Primary (on time, from day 0) | R2 | next 1 h | 95% | 39800 | 789 | 95.1% | 94.0–96.2% | 92–98% | PASS |
| Primary (on time, from day 0) | R3 | next 24 h | 68% | 38600 | 766 | 70.6% | 64.2–76.9% | 63–73% | inconclusive |
| Primary (on time, from day 0) | R4 | next 24 h | 95% | 38600 | 766 | 93.9% | 91.0–96.9% | 92–98% | inconclusive |
| All rows from day 0, including back-filled | R1 | next 1 h | 68% | 41550 | 790 | 68.4% | 66.0–70.8% | 63–73% | PASS |
| All rows from day 0, including back-filled | R2 | next 1 h | 95% | 41550 | 790 | 95.2% | 94.1–96.3% | 92–98% | PASS |
| All rows from day 0, including back-filled | R3 | next 24 h | 68% | 40300 | 767 | 70.6% | 64.2–76.9% | 63–73% | inconclusive |
| All rows from day 0, including back-filled | R4 | next 24 h | 95% | 40300 | 767 | 94.0% | 91.0–96.9% | 92–98% | inconclusive |
| Run-in (before day 0) | R1 | next 1 h | 68% | 14250 | 281 | 71.0% | 67.6–74.5% | 63–73% | inconclusive |
| Run-in (before day 0) | R2 | next 1 h | 95% | 14250 | 281 | 95.2% | 93.6–96.8% | 92–98% | PASS |
| Run-in (before day 0) | R3 | next 24 h | 68% | 14250 | 281 | 72.1% | – | 63–73% | too few data yet |
| Run-in (before day 0) | R4 | next 24 h | 95% | 14250 | 281 | 97.3% | – | 92–98% | too few data yet |

Coins furthest from the 68% claim on the 24-hour range (primary sample):

| Coin | Coverage | Forecasts |
|---|---|---|
| BTC | 56% | 772 |
| ETH | 59% | 772 |
| TRX | 59% | 772 |
| BNB | 60% | 772 |
| SOL | 62% | 772 |
| WLD | 78% | 772 |
| TIA | 78% | 772 |
| FET | 78% | 772 |
| DOT | 79% | 772 |
| FIL | 79% | 772 |

Information only, not investment advice.
