# Live calibration of the board's typical-move ranges

Updated 2026-11-21 22:02 UTC. Rules and pass bands are fixed in [LIVE_TEST.md](https://github.com/sandordrpal/crypto-concordance-board/blob/main/research/LIVE_TEST.md) (R1-R4). Primary analysis: on-time forecasts from 2026-10-19; earlier rows are a run-in.

Coverage is the share of real moves that stayed inside the range. Confidence intervals (90%) are clustered by issue hour, because coins move together. PASS when the whole interval lies inside the band.

| Sample | Test | Horizon | Claimed | Forecasts | Issue hours | Coverage | 90% CI | Pass band | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| Primary (on time, from day 0) | R1 | next 1 h | 68% | 41000 | 813 | 67.9% | 65.5–70.4% | 63–73% | PASS |
| Primary (on time, from day 0) | R2 | next 1 h | 95% | 41000 | 813 | 94.8% | 93.7–96.0% | 92–98% | PASS |
| Primary (on time, from day 0) | R3 | next 24 h | 68% | 39850 | 790 | 69.3% | 62.5–76.0% | 63–73% | inconclusive |
| Primary (on time, from day 0) | R4 | next 24 h | 95% | 39850 | 790 | 93.3% | 90.0–96.5% | 92–98% | inconclusive |
| All rows from day 0, including back-filled | R1 | next 1 h | 68% | 42800 | 814 | 68.0% | 65.6–70.4% | 63–73% | PASS |
| All rows from day 0, including back-filled | R2 | next 1 h | 95% | 42800 | 814 | 94.8% | 93.7–96.0% | 92–98% | PASS |
| All rows from day 0, including back-filled | R3 | next 24 h | 68% | 41600 | 791 | 69.3% | 62.6–76.0% | 63–73% | inconclusive |
| All rows from day 0, including back-filled | R4 | next 24 h | 95% | 41600 | 791 | 93.3% | 90.0–96.5% | 92–98% | inconclusive |
| Run-in (before day 0) | R1 | next 1 h | 68% | 14250 | 281 | 71.0% | 67.6–74.5% | 63–73% | inconclusive |
| Run-in (before day 0) | R2 | next 1 h | 95% | 14250 | 281 | 95.2% | 93.6–96.8% | 92–98% | PASS |
| Run-in (before day 0) | R3 | next 24 h | 68% | 14250 | 281 | 72.1% | – | 63–73% | too few data yet |
| Run-in (before day 0) | R4 | next 24 h | 95% | 14250 | 281 | 97.3% | – | 92–98% | too few data yet |

Coins furthest from the 68% claim on the 24-hour range (primary sample):

| Coin | Coverage | Forecasts |
|---|---|---|
| BTC | 55% | 797 |
| ETH | 57% | 797 |
| TRX | 58% | 797 |
| BNB | 58% | 797 |
| SOL | 61% | 797 |
| OP | 76% | 797 |
| FET | 76% | 797 |
| TIA | 77% | 797 |
| DOT | 77% | 797 |
| FIL | 78% | 797 |

Information only, not investment advice.
