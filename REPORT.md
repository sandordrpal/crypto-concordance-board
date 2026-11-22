# Live calibration of the board's typical-move ranges

Updated 2026-11-22 17:02 UTC. Rules and pass bands are fixed in [LIVE_TEST.md](https://github.com/sandordrpal/crypto-concordance-board/blob/main/research/LIVE_TEST.md) (R1-R4). Primary analysis: on-time forecasts from 2026-10-19; earlier rows are a run-in.

Coverage is the share of real moves that stayed inside the range. Confidence intervals (90%) are clustered by issue hour, because coins move together. PASS when the whole interval lies inside the band.

| Sample | Test | Horizon | Claimed | Forecasts | Issue hours | Coverage | 90% CI | Pass band | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| Primary (on time, from day 0) | R1 | next 1 h | 68% | 41950 | 832 | 68.1% | 65.7–70.5% | 63–73% | PASS |
| Primary (on time, from day 0) | R2 | next 1 h | 95% | 41950 | 832 | 94.9% | 93.8–96.0% | 92–98% | PASS |
| Primary (on time, from day 0) | R3 | next 24 h | 68% | 40800 | 809 | 69.1% | 62.6–75.7% | 63–73% | inconclusive |
| Primary (on time, from day 0) | R4 | next 24 h | 95% | 40800 | 809 | 93.4% | 90.2–96.6% | 92–98% | inconclusive |
| All rows from day 0, including back-filled | R1 | next 1 h | 68% | 43800 | 833 | 68.1% | 65.8–70.5% | 63–73% | PASS |
| All rows from day 0, including back-filled | R2 | next 1 h | 95% | 43800 | 833 | 94.9% | 93.8–96.0% | 92–98% | PASS |
| All rows from day 0, including back-filled | R3 | next 24 h | 68% | 42600 | 810 | 69.1% | 62.6–75.7% | 63–73% | inconclusive |
| All rows from day 0, including back-filled | R4 | next 24 h | 95% | 42600 | 810 | 93.4% | 90.3–96.6% | 92–98% | inconclusive |
| Run-in (before day 0) | R1 | next 1 h | 68% | 14250 | 281 | 71.0% | 67.6–74.5% | 63–73% | inconclusive |
| Run-in (before day 0) | R2 | next 1 h | 95% | 14250 | 281 | 95.2% | 93.6–96.8% | 92–98% | PASS |
| Run-in (before day 0) | R3 | next 24 h | 68% | 14250 | 281 | 72.1% | – | 63–73% | too few data yet |
| Run-in (before day 0) | R4 | next 24 h | 95% | 14250 | 281 | 97.3% | – | 92–98% | too few data yet |

Coins furthest from the 68% claim on the 24-hour range (primary sample):

| Coin | Coverage | Forecasts |
|---|---|---|
| BTC | 54% | 816 |
| ETH | 56% | 816 |
| BNB | 58% | 816 |
| TRX | 58% | 816 |
| UNI | 60% | 816 |
| WLD | 76% | 816 |
| FET | 76% | 816 |
| TIA | 77% | 816 |
| FIL | 78% | 816 |
| DOT | 78% | 816 |

Information only, not investment advice.
