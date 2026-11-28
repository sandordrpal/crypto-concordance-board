# Live calibration of the board's typical-move ranges

Updated 2026-11-28 08:02 UTC. Rules and pass bands are fixed in [LIVE_TEST.md](https://github.com/sandordrpal/crypto-concordance-board/blob/main/research/LIVE_TEST.md) (R1-R4). Primary analysis: on-time forecasts from 2026-10-19; earlier rows are a run-in.

Coverage is the share of real moves that stayed inside the range. Confidence intervals (90%) are clustered by issue hour, because coins move together. PASS when the whole interval lies inside the band.

| Sample | Test | Horizon | Claimed | Forecasts | Issue hours | Coverage | 90% CI | Pass band | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| Primary (on time, from day 0) | R1 | next 1 h | 68% | 48750 | 966 | 68.2% | 66.0–70.4% | 63–73% | PASS |
| Primary (on time, from day 0) | R2 | next 1 h | 95% | 48750 | 966 | 95.0% | 94.0–96.0% | 92–98% | PASS |
| Primary (on time, from day 0) | R3 | next 24 h | 68% | 47600 | 943 | 68.5% | 62.6–74.3% | 63–73% | inconclusive |
| Primary (on time, from day 0) | R4 | next 24 h | 95% | 47600 | 943 | 93.9% | 91.2–96.7% | 92–98% | inconclusive |
| All rows from day 0, including back-filled | R1 | next 1 h | 68% | 50950 | 968 | 68.2% | 66.0–70.3% | 63–73% | PASS |
| All rows from day 0, including back-filled | R2 | next 1 h | 95% | 50950 | 968 | 95.0% | 94.0–96.0% | 92–98% | PASS |
| All rows from day 0, including back-filled | R3 | next 24 h | 68% | 49750 | 945 | 68.4% | 62.6–74.3% | 63–73% | inconclusive |
| All rows from day 0, including back-filled | R4 | next 24 h | 95% | 49750 | 945 | 93.9% | 91.2–96.7% | 92–98% | inconclusive |
| Run-in (before day 0) | R1 | next 1 h | 68% | 14250 | 281 | 71.0% | 67.6–74.5% | 63–73% | inconclusive |
| Run-in (before day 0) | R2 | next 1 h | 95% | 14250 | 281 | 95.2% | 93.6–96.8% | 92–98% | PASS |
| Run-in (before day 0) | R3 | next 24 h | 68% | 14250 | 281 | 72.1% | – | 63–73% | too few data yet |
| Run-in (before day 0) | R4 | next 24 h | 95% | 14250 | 281 | 97.3% | – | 92–98% | too few data yet |

Coins furthest from the 68% claim on the 24-hour range (primary sample):

| Coin | Coverage | Forecasts |
|---|---|---|
| BTC | 55% | 952 |
| TRX | 58% | 952 |
| BNB | 59% | 952 |
| ETH | 59% | 952 |
| SOL | 61% | 952 |
| FIL | 74% | 952 |
| DOT | 74% | 952 |
| WLD | 75% | 952 |
| TIA | 76% | 952 |
| OP | 76% | 952 |

Information only, not investment advice.
