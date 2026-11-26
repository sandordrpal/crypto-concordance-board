# Live calibration of the board's typical-move ranges

Updated 2026-11-26 13:02 UTC. Rules and pass bands are fixed in [LIVE_TEST.md](https://github.com/sandordrpal/crypto-concordance-board/blob/main/research/LIVE_TEST.md) (R1-R4). Primary analysis: on-time forecasts from 2026-10-19; earlier rows are a run-in.

Coverage is the share of real moves that stayed inside the range. Confidence intervals (90%) are clustered by issue hour, because coins move together. PASS when the whole interval lies inside the band.

| Sample | Test | Horizon | Claimed | Forecasts | Issue hours | Coverage | 90% CI | Pass band | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| Primary (on time, from day 0) | R1 | next 1 h | 68% | 46600 | 923 | 67.8% | 65.5–70.0% | 63–73% | PASS |
| Primary (on time, from day 0) | R2 | next 1 h | 95% | 46600 | 923 | 94.9% | 93.9–96.0% | 92–98% | PASS |
| Primary (on time, from day 0) | R3 | next 24 h | 68% | 45500 | 901 | 68.0% | 61.9–74.0% | 63–73% | inconclusive |
| Primary (on time, from day 0) | R4 | next 24 h | 95% | 45500 | 901 | 93.7% | 90.9–96.6% | 92–98% | inconclusive |
| All rows from day 0, including back-filled | R1 | next 1 h | 68% | 48700 | 925 | 67.8% | 65.5–70.0% | 63–73% | PASS |
| All rows from day 0, including back-filled | R2 | next 1 h | 95% | 48700 | 925 | 94.9% | 93.9–96.0% | 92–98% | PASS |
| All rows from day 0, including back-filled | R3 | next 24 h | 68% | 47500 | 902 | 68.0% | 62.0–74.0% | 63–73% | inconclusive |
| All rows from day 0, including back-filled | R4 | next 24 h | 95% | 47500 | 902 | 93.7% | 90.9–96.6% | 92–98% | inconclusive |
| Run-in (before day 0) | R1 | next 1 h | 68% | 14250 | 281 | 71.0% | 67.6–74.5% | 63–73% | inconclusive |
| Run-in (before day 0) | R2 | next 1 h | 95% | 14250 | 281 | 95.2% | 93.6–96.8% | 92–98% | PASS |
| Run-in (before day 0) | R3 | next 24 h | 68% | 14250 | 281 | 72.1% | – | 63–73% | too few data yet |
| Run-in (before day 0) | R4 | next 24 h | 95% | 14250 | 281 | 97.3% | – | 92–98% | too few data yet |

Coins furthest from the 68% claim on the 24-hour range (primary sample):

| Coin | Coverage | Forecasts |
|---|---|---|
| BTC | 54% | 910 |
| TRX | 57% | 910 |
| BNB | 58% | 910 |
| ETH | 58% | 910 |
| SOL | 60% | 910 |
| DOT | 75% | 910 |
| WLD | 75% | 910 |
| TIA | 75% | 910 |
| FET | 76% | 910 |
| OP | 76% | 910 |

Information only, not investment advice.
