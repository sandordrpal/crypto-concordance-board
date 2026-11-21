# Live calibration of the board's typical-move ranges

Updated 2026-11-21 16:02 UTC. Rules and pass bands are fixed in [LIVE_TEST.md](https://github.com/sandordrpal/crypto-concordance-board/blob/main/research/LIVE_TEST.md) (R1-R4). Primary analysis: on-time forecasts from 2026-10-19; earlier rows are a run-in.

Coverage is the share of real moves that stayed inside the range. Confidence intervals (90%) are clustered by issue hour, because coins move together. PASS when the whole interval lies inside the band.

| Sample | Test | Horizon | Claimed | Forecasts | Issue hours | Coverage | 90% CI | Pass band | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| Primary (on time, from day 0) | R1 | next 1 h | 68% | 40700 | 807 | 67.8% | 65.4–70.2% | 63–73% | PASS |
| Primary (on time, from day 0) | R2 | next 1 h | 95% | 40700 | 807 | 94.8% | 93.6–95.9% | 92–98% | PASS |
| Primary (on time, from day 0) | R3 | next 24 h | 68% | 39550 | 784 | 69.2% | 62.5–76.0% | 63–73% | inconclusive |
| Primary (on time, from day 0) | R4 | next 24 h | 95% | 39550 | 784 | 93.2% | 89.9–96.5% | 92–98% | inconclusive |
| All rows from day 0, including back-filled | R1 | next 1 h | 68% | 42500 | 808 | 67.8% | 65.4–70.2% | 63–73% | PASS |
| All rows from day 0, including back-filled | R2 | next 1 h | 95% | 42500 | 808 | 94.8% | 93.6–95.9% | 92–98% | PASS |
| All rows from day 0, including back-filled | R3 | next 24 h | 68% | 41300 | 785 | 69.3% | 62.5–76.0% | 63–73% | inconclusive |
| All rows from day 0, including back-filled | R4 | next 24 h | 95% | 41300 | 785 | 93.2% | 89.9–96.5% | 92–98% | inconclusive |
| Run-in (before day 0) | R1 | next 1 h | 68% | 14250 | 281 | 71.0% | 67.6–74.5% | 63–73% | inconclusive |
| Run-in (before day 0) | R2 | next 1 h | 95% | 14250 | 281 | 95.2% | 93.6–96.8% | 92–98% | PASS |
| Run-in (before day 0) | R3 | next 24 h | 68% | 14250 | 281 | 72.1% | – | 63–73% | too few data yet |
| Run-in (before day 0) | R4 | next 24 h | 95% | 14250 | 281 | 97.3% | – | 92–98% | too few data yet |

Coins furthest from the 68% claim on the 24-hour range (primary sample):

| Coin | Coverage | Forecasts |
|---|---|---|
| BTC | 55% | 791 |
| ETH | 57% | 791 |
| TRX | 58% | 791 |
| BNB | 58% | 791 |
| SOL | 61% | 791 |
| OP | 76% | 791 |
| FET | 77% | 791 |
| TIA | 77% | 791 |
| DOT | 77% | 791 |
| FIL | 78% | 791 |

Information only, not investment advice.
