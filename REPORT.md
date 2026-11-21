# Live calibration of the board's typical-move ranges

Updated 2026-11-21 00:02 UTC. Rules and pass bands are fixed in [LIVE_TEST.md](https://github.com/sandordrpal/crypto-concordance-board/blob/main/research/LIVE_TEST.md) (R1-R4). Primary analysis: on-time forecasts from 2026-10-19; earlier rows are a run-in.

Coverage is the share of real moves that stayed inside the range. Confidence intervals (90%) are clustered by issue hour, because coins move together. PASS when the whole interval lies inside the band.

| Sample | Test | Horizon | Claimed | Forecasts | Issue hours | Coverage | 90% CI | Pass band | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| Primary (on time, from day 0) | R1 | next 1 h | 68% | 39900 | 791 | 68.3% | 65.9–70.7% | 63–73% | PASS |
| Primary (on time, from day 0) | R2 | next 1 h | 95% | 39900 | 791 | 95.2% | 94.1–96.3% | 92–98% | PASS |
| Primary (on time, from day 0) | R3 | next 24 h | 68% | 38750 | 768 | 70.4% | 64.0–76.8% | 63–73% | inconclusive |
| Primary (on time, from day 0) | R4 | next 24 h | 95% | 38750 | 768 | 93.9% | 90.9–96.9% | 92–98% | inconclusive |
| All rows from day 0, including back-filled | R1 | next 1 h | 68% | 41650 | 792 | 68.3% | 65.9–70.7% | 63–73% | PASS |
| All rows from day 0, including back-filled | R2 | next 1 h | 95% | 41650 | 792 | 95.2% | 94.1–96.3% | 92–98% | PASS |
| All rows from day 0, including back-filled | R3 | next 24 h | 68% | 40500 | 769 | 70.4% | 64.0–76.8% | 63–73% | inconclusive |
| All rows from day 0, including back-filled | R4 | next 24 h | 95% | 40500 | 769 | 93.9% | 90.9–96.9% | 92–98% | inconclusive |
| Run-in (before day 0) | R1 | next 1 h | 68% | 14250 | 281 | 71.0% | 67.6–74.5% | 63–73% | inconclusive |
| Run-in (before day 0) | R2 | next 1 h | 95% | 14250 | 281 | 95.2% | 93.6–96.8% | 92–98% | PASS |
| Run-in (before day 0) | R3 | next 24 h | 68% | 14250 | 281 | 72.1% | – | 63–73% | too few data yet |
| Run-in (before day 0) | R4 | next 24 h | 95% | 14250 | 281 | 97.3% | – | 92–98% | too few data yet |

Coins furthest from the 68% claim on the 24-hour range (primary sample):

| Coin | Coverage | Forecasts |
|---|---|---|
| BTC | 56% | 775 |
| ETH | 58% | 775 |
| TRX | 59% | 775 |
| BNB | 59% | 775 |
| SOL | 62% | 775 |
| WLD | 77% | 775 |
| TIA | 78% | 775 |
| FET | 78% | 775 |
| DOT | 79% | 775 |
| FIL | 79% | 775 |

Information only, not investment advice.
