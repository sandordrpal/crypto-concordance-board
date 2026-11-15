# Live calibration of the board's typical-move ranges

Updated 2026-11-15 00:02 UTC. Rules and pass bands are fixed in [LIVE_TEST.md](https://github.com/sandordrpal/crypto-concordance-board/blob/main/research/LIVE_TEST.md) (R1-R4). Primary analysis: on-time forecasts from 2026-10-19; earlier rows are a run-in.

Coverage is the share of real moves that stayed inside the range. Confidence intervals (90%) are clustered by issue hour, because coins move together. PASS when the whole interval lies inside the band.

| Sample | Test | Horizon | Claimed | Forecasts | Issue hours | Coverage | 90% CI | Pass band | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| Primary (on time, from day 0) | R1 | next 1 h | 68% | 32650 | 647 | 70.4% | 67.8–73.0% | 63–73% | inconclusive |
| Primary (on time, from day 0) | R2 | next 1 h | 95% | 32650 | 647 | 95.5% | 94.4–96.7% | 92–98% | PASS |
| Primary (on time, from day 0) | R3 | next 24 h | 68% | 31500 | 624 | 71.3% | 64.9–77.7% | 63–73% | inconclusive |
| Primary (on time, from day 0) | R4 | next 24 h | 95% | 31500 | 624 | 94.5% | 91.7–97.2% | 92–98% | inconclusive |
| All rows from day 0, including back-filled | R1 | next 1 h | 68% | 34100 | 648 | 70.4% | 67.8–73.0% | 63–73% | inconclusive |
| All rows from day 0, including back-filled | R2 | next 1 h | 95% | 34100 | 648 | 95.5% | 94.4–96.7% | 92–98% | PASS |
| All rows from day 0, including back-filled | R3 | next 24 h | 68% | 32950 | 625 | 71.3% | 65.0–77.7% | 63–73% | inconclusive |
| All rows from day 0, including back-filled | R4 | next 24 h | 95% | 32950 | 625 | 94.5% | 91.7–97.2% | 92–98% | inconclusive |
| Run-in (before day 0) | R1 | next 1 h | 68% | 14250 | 281 | 71.0% | 67.6–74.5% | 63–73% | inconclusive |
| Run-in (before day 0) | R2 | next 1 h | 95% | 14250 | 281 | 95.2% | 93.6–96.8% | 92–98% | PASS |
| Run-in (before day 0) | R3 | next 24 h | 68% | 14250 | 281 | 72.1% | – | 63–73% | too few data yet |
| Run-in (before day 0) | R4 | next 24 h | 95% | 14250 | 281 | 97.3% | – | 92–98% | too few data yet |

Coins furthest from the 68% claim on the 24-hour range (primary sample):

| Coin | Coverage | Forecasts |
|---|---|---|
| BTC | 56% | 630 |
| ETH | 56% | 630 |
| BNB | 58% | 630 |
| XRP | 61% | 630 |
| TRX | 62% | 630 |
| WLD | 79% | 630 |
| OP | 80% | 630 |
| DOT | 80% | 630 |
| FET | 81% | 630 |
| FIL | 83% | 630 |

Information only, not investment advice.
