# Live calibration of the board's typical-move ranges

Updated 2026-11-28 09:02 UTC. Rules and pass bands are fixed in [LIVE_TEST.md](https://github.com/sandordrpal/crypto-concordance-board/blob/main/research/LIVE_TEST.md) (R1-R4). Primary analysis: on-time forecasts from 2026-10-19; earlier rows are a run-in.

Coverage is the share of real moves that stayed inside the range. Confidence intervals (90%) are clustered by issue hour, because coins move together. PASS when the whole interval lies inside the band.

| Sample | Test | Horizon | Claimed | Forecasts | Issue hours | Coverage | 90% CI | Pass band | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| Primary (on time, from day 0) | R1 | next 1 h | 68% | 48800 | 967 | 68.2% | 66.0–70.4% | 63–73% | PASS |
| Primary (on time, from day 0) | R2 | next 1 h | 95% | 48800 | 967 | 95.0% | 94.0–96.0% | 92–98% | PASS |
| Primary (on time, from day 0) | R3 | next 24 h | 68% | 47650 | 944 | 68.5% | 62.6–74.3% | 63–73% | inconclusive |
| Primary (on time, from day 0) | R4 | next 24 h | 95% | 47650 | 944 | 93.9% | 91.2–96.7% | 92–98% | inconclusive |
| All rows from day 0, including back-filled | R1 | next 1 h | 68% | 51000 | 969 | 68.2% | 66.0–70.4% | 63–73% | PASS |
| All rows from day 0, including back-filled | R2 | next 1 h | 95% | 51000 | 969 | 95.0% | 94.0–96.0% | 92–98% | PASS |
| All rows from day 0, including back-filled | R3 | next 24 h | 68% | 49800 | 946 | 68.4% | 62.6–74.2% | 63–73% | inconclusive |
| All rows from day 0, including back-filled | R4 | next 24 h | 95% | 49800 | 946 | 93.9% | 91.2–96.7% | 92–98% | inconclusive |
| Run-in (before day 0) | R1 | next 1 h | 68% | 14250 | 281 | 71.0% | 67.6–74.5% | 63–73% | inconclusive |
| Run-in (before day 0) | R2 | next 1 h | 95% | 14250 | 281 | 95.2% | 93.6–96.8% | 92–98% | PASS |
| Run-in (before day 0) | R3 | next 24 h | 68% | 14250 | 281 | 72.1% | – | 63–73% | too few data yet |
| Run-in (before day 0) | R4 | next 24 h | 95% | 14250 | 281 | 97.3% | – | 92–98% | too few data yet |

Coins furthest from the 68% claim on the 24-hour range (primary sample):

| Coin | Coverage | Forecasts |
|---|---|---|
| BTC | 55% | 953 |
| TRX | 58% | 953 |
| BNB | 59% | 953 |
| ETH | 59% | 953 |
| SOL | 61% | 953 |
| FIL | 74% | 953 |
| DOT | 74% | 953 |
| WLD | 75% | 953 |
| TIA | 76% | 953 |
| OP | 76% | 953 |

Information only, not investment advice.
