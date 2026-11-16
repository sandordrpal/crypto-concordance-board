# Live calibration of the board's typical-move ranges

Updated 2026-11-16 05:02 UTC. Rules and pass bands are fixed in [LIVE_TEST.md](https://github.com/sandordrpal/crypto-concordance-board/blob/main/research/LIVE_TEST.md) (R1-R4). Primary analysis: on-time forecasts from 2026-10-19; earlier rows are a run-in.

Coverage is the share of real moves that stayed inside the range. Confidence intervals (90%) are clustered by issue hour, because coins move together. PASS when the whole interval lies inside the band.

| Sample | Test | Horizon | Claimed | Forecasts | Issue hours | Coverage | 90% CI | Pass band | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| Primary (on time, from day 0) | R1 | next 1 h | 68% | 34100 | 676 | 69.8% | 67.2–72.4% | 63–73% | PASS |
| Primary (on time, from day 0) | R2 | next 1 h | 95% | 34100 | 676 | 95.4% | 94.1–96.6% | 92–98% | PASS |
| Primary (on time, from day 0) | R3 | next 24 h | 68% | 32950 | 653 | 69.8% | 63.0–76.6% | 63–73% | inconclusive |
| Primary (on time, from day 0) | R4 | next 24 h | 95% | 32950 | 653 | 93.7% | 90.4–97.1% | 92–98% | inconclusive |
| All rows from day 0, including back-filled | R1 | next 1 h | 68% | 35650 | 677 | 69.8% | 67.2–72.4% | 63–73% | PASS |
| All rows from day 0, including back-filled | R2 | next 1 h | 95% | 35650 | 677 | 95.4% | 94.1–96.6% | 92–98% | PASS |
| All rows from day 0, including back-filled | R3 | next 24 h | 68% | 34450 | 654 | 69.8% | 63.1–76.6% | 63–73% | inconclusive |
| All rows from day 0, including back-filled | R4 | next 24 h | 95% | 34450 | 654 | 93.8% | 90.4–97.1% | 92–98% | inconclusive |
| Run-in (before day 0) | R1 | next 1 h | 68% | 14250 | 281 | 71.0% | 67.6–74.5% | 63–73% | inconclusive |
| Run-in (before day 0) | R2 | next 1 h | 95% | 14250 | 281 | 95.2% | 93.6–96.8% | 92–98% | PASS |
| Run-in (before day 0) | R3 | next 24 h | 68% | 14250 | 281 | 72.1% | – | 63–73% | too few data yet |
| Run-in (before day 0) | R4 | next 24 h | 95% | 14250 | 281 | 97.3% | – | 92–98% | too few data yet |

Coins furthest from the 68% claim on the 24-hour range (primary sample):

| Coin | Coverage | Forecasts |
|---|---|---|
| BTC | 55% | 659 |
| ETH | 55% | 659 |
| BNB | 56% | 659 |
| TRX | 60% | 659 |
| XRP | 60% | 659 |
| WLD | 77% | 659 |
| OP | 77% | 659 |
| DOT | 78% | 659 |
| FET | 79% | 659 |
| FIL | 81% | 659 |

Information only, not investment advice.
