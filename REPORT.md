# Live calibration of the board's typical-move ranges

Updated 2026-11-15 16:02 UTC. Rules and pass bands are fixed in [LIVE_TEST.md](https://github.com/sandordrpal/crypto-concordance-board/blob/main/research/LIVE_TEST.md) (R1-R4). Primary analysis: on-time forecasts from 2026-10-19; earlier rows are a run-in.

Coverage is the share of real moves that stayed inside the range. Confidence intervals (90%) are clustered by issue hour, because coins move together. PASS when the whole interval lies inside the band.

| Sample | Test | Horizon | Claimed | Forecasts | Issue hours | Coverage | 90% CI | Pass band | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| Primary (on time, from day 0) | R1 | next 1 h | 68% | 33450 | 663 | 69.9% | 67.3–72.6% | 63–73% | PASS |
| Primary (on time, from day 0) | R2 | next 1 h | 95% | 33450 | 663 | 95.4% | 94.1–96.6% | 92–98% | PASS |
| Primary (on time, from day 0) | R3 | next 24 h | 68% | 32300 | 640 | 70.0% | 63.2–76.9% | 63–73% | inconclusive |
| Primary (on time, from day 0) | R4 | next 24 h | 95% | 32300 | 640 | 93.7% | 90.3–97.1% | 92–98% | inconclusive |
| All rows from day 0, including back-filled | R1 | next 1 h | 68% | 34950 | 664 | 70.0% | 67.3–72.6% | 63–73% | PASS |
| All rows from day 0, including back-filled | R2 | next 1 h | 95% | 34950 | 664 | 95.4% | 94.1–96.6% | 92–98% | PASS |
| All rows from day 0, including back-filled | R3 | next 24 h | 68% | 33750 | 641 | 70.0% | 63.2–76.9% | 63–73% | inconclusive |
| All rows from day 0, including back-filled | R4 | next 24 h | 95% | 33750 | 641 | 93.7% | 90.3–97.1% | 92–98% | inconclusive |
| Run-in (before day 0) | R1 | next 1 h | 68% | 14250 | 281 | 71.0% | 67.6–74.5% | 63–73% | inconclusive |
| Run-in (before day 0) | R2 | next 1 h | 95% | 14250 | 281 | 95.2% | 93.6–96.8% | 92–98% | PASS |
| Run-in (before day 0) | R3 | next 24 h | 68% | 14250 | 281 | 72.1% | – | 63–73% | too few data yet |
| Run-in (before day 0) | R4 | next 24 h | 95% | 14250 | 281 | 97.3% | – | 92–98% | too few data yet |

Coins furthest from the 68% claim on the 24-hour range (primary sample):

| Coin | Coverage | Forecasts |
|---|---|---|
| BTC | 54% | 646 |
| ETH | 55% | 646 |
| BNB | 57% | 646 |
| TRX | 60% | 646 |
| XRP | 60% | 646 |
| WLD | 78% | 646 |
| OP | 78% | 646 |
| DOT | 78% | 646 |
| FET | 79% | 646 |
| FIL | 81% | 646 |

Information only, not investment advice.
