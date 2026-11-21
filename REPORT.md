# Live calibration of the board's typical-move ranges

Updated 2026-11-21 06:02 UTC. Rules and pass bands are fixed in [LIVE_TEST.md](https://github.com/sandordrpal/crypto-concordance-board/blob/main/research/LIVE_TEST.md) (R1-R4). Primary analysis: on-time forecasts from 2026-10-19; earlier rows are a run-in.

Coverage is the share of real moves that stayed inside the range. Confidence intervals (90%) are clustered by issue hour, because coins move together. PASS when the whole interval lies inside the band.

| Sample | Test | Horizon | Claimed | Forecasts | Issue hours | Coverage | 90% CI | Pass band | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| Primary (on time, from day 0) | R1 | next 1 h | 68% | 40200 | 797 | 68.2% | 65.8–70.6% | 63–73% | PASS |
| Primary (on time, from day 0) | R2 | next 1 h | 95% | 40200 | 797 | 95.0% | 93.9–96.1% | 92–98% | PASS |
| Primary (on time, from day 0) | R3 | next 24 h | 68% | 39050 | 774 | 69.9% | 63.3–76.4% | 63–73% | inconclusive |
| Primary (on time, from day 0) | R4 | next 24 h | 95% | 39050 | 774 | 93.6% | 90.4–96.7% | 92–98% | inconclusive |
| All rows from day 0, including back-filled | R1 | next 1 h | 68% | 42000 | 798 | 68.2% | 65.8–70.6% | 63–73% | PASS |
| All rows from day 0, including back-filled | R2 | next 1 h | 95% | 42000 | 798 | 95.0% | 93.9–96.1% | 92–98% | PASS |
| All rows from day 0, including back-filled | R3 | next 24 h | 68% | 40800 | 775 | 69.9% | 63.3–76.4% | 63–73% | inconclusive |
| All rows from day 0, including back-filled | R4 | next 24 h | 95% | 40800 | 775 | 93.6% | 90.5–96.7% | 92–98% | inconclusive |
| Run-in (before day 0) | R1 | next 1 h | 68% | 14250 | 281 | 71.0% | 67.6–74.5% | 63–73% | inconclusive |
| Run-in (before day 0) | R2 | next 1 h | 95% | 14250 | 281 | 95.2% | 93.6–96.8% | 92–98% | PASS |
| Run-in (before day 0) | R3 | next 24 h | 68% | 14250 | 281 | 72.1% | – | 63–73% | too few data yet |
| Run-in (before day 0) | R4 | next 24 h | 95% | 14250 | 281 | 97.3% | – | 92–98% | too few data yet |

Coins furthest from the 68% claim on the 24-hour range (primary sample):

| Coin | Coverage | Forecasts |
|---|---|---|
| BTC | 56% | 781 |
| ETH | 58% | 781 |
| TRX | 59% | 781 |
| BNB | 59% | 781 |
| SOL | 61% | 781 |
| WLD | 77% | 781 |
| FET | 77% | 781 |
| TIA | 77% | 781 |
| DOT | 78% | 781 |
| FIL | 78% | 781 |

Information only, not investment advice.
