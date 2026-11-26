# Live calibration of the board's typical-move ranges

Updated 2026-11-26 10:02 UTC. Rules and pass bands are fixed in [LIVE_TEST.md](https://github.com/sandordrpal/crypto-concordance-board/blob/main/research/LIVE_TEST.md) (R1-R4). Primary analysis: on-time forecasts from 2026-10-19; earlier rows are a run-in.

Coverage is the share of real moves that stayed inside the range. Confidence intervals (90%) are clustered by issue hour, because coins move together. PASS when the whole interval lies inside the band.

| Sample | Test | Horizon | Claimed | Forecasts | Issue hours | Coverage | 90% CI | Pass band | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| Primary (on time, from day 0) | R1 | next 1 h | 68% | 46450 | 920 | 67.8% | 65.5–70.0% | 63–73% | PASS |
| Primary (on time, from day 0) | R2 | next 1 h | 95% | 46450 | 920 | 94.9% | 93.8–95.9% | 92–98% | PASS |
| Primary (on time, from day 0) | R3 | next 24 h | 68% | 45350 | 898 | 68.2% | 62.1–74.2% | 63–73% | inconclusive |
| Primary (on time, from day 0) | R4 | next 24 h | 95% | 45350 | 898 | 93.7% | 90.9–96.6% | 92–98% | inconclusive |
| All rows from day 0, including back-filled | R1 | next 1 h | 68% | 48550 | 922 | 67.7% | 65.5–70.0% | 63–73% | PASS |
| All rows from day 0, including back-filled | R2 | next 1 h | 95% | 48550 | 922 | 94.9% | 93.8–96.0% | 92–98% | PASS |
| All rows from day 0, including back-filled | R3 | next 24 h | 68% | 47350 | 899 | 68.2% | 62.1–74.2% | 63–73% | inconclusive |
| All rows from day 0, including back-filled | R4 | next 24 h | 95% | 47350 | 899 | 93.8% | 90.9–96.6% | 92–98% | inconclusive |
| Run-in (before day 0) | R1 | next 1 h | 68% | 14250 | 281 | 71.0% | 67.6–74.5% | 63–73% | inconclusive |
| Run-in (before day 0) | R2 | next 1 h | 95% | 14250 | 281 | 95.2% | 93.6–96.8% | 92–98% | PASS |
| Run-in (before day 0) | R3 | next 24 h | 68% | 14250 | 281 | 72.1% | – | 63–73% | too few data yet |
| Run-in (before day 0) | R4 | next 24 h | 95% | 14250 | 281 | 97.3% | – | 92–98% | too few data yet |

Coins furthest from the 68% claim on the 24-hour range (primary sample):

| Coin | Coverage | Forecasts |
|---|---|---|
| BTC | 54% | 907 |
| TRX | 57% | 907 |
| BNB | 58% | 907 |
| ETH | 58% | 907 |
| SOL | 60% | 907 |
| DOT | 75% | 907 |
| WLD | 75% | 907 |
| TIA | 75% | 907 |
| FET | 76% | 907 |
| OP | 77% | 907 |

Information only, not investment advice.
