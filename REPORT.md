# Live calibration of the board's typical-move ranges

Updated 2026-11-07 07:02 UTC. Rules and pass bands are fixed in [LIVE_TEST.md](https://github.com/sandordrpal/crypto-concordance-board/blob/main/research/LIVE_TEST.md) (R1-R4). Primary analysis: on-time forecasts from 2026-10-19; earlier rows are a run-in.

Coverage is the share of real moves that stayed inside the range. Confidence intervals (90%) are clustered by issue hour, because coins move together. PASS when the whole interval lies inside the band.

| Sample | Test | Horizon | Claimed | Forecasts | Issue hours | Coverage | 90% CI | Pass band | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| Primary (on time, from day 0) | R1 | next 1 h | 68% | 23350 | 462 | 72.0% | 69.1–74.9% | 63–73% | inconclusive |
| Primary (on time, from day 0) | R2 | next 1 h | 95% | 23350 | 462 | 96.3% | 95.1–97.5% | 92–98% | PASS |
| Primary (on time, from day 0) | R3 | next 24 h | 68% | 22150 | 439 | 72.2% | 64.3–80.1% | 63–73% | inconclusive |
| Primary (on time, from day 0) | R4 | next 24 h | 95% | 22150 | 439 | 95.1% | 92.2–97.9% | 92–98% | PASS |
| All rows from day 0, including back-filled | R1 | next 1 h | 68% | 24450 | 463 | 72.1% | 69.2–75.0% | 63–73% | inconclusive |
| All rows from day 0, including back-filled | R2 | next 1 h | 95% | 24450 | 463 | 96.3% | 95.1–97.5% | 92–98% | PASS |
| All rows from day 0, including back-filled | R3 | next 24 h | 68% | 23200 | 440 | 72.2% | 64.4–80.0% | 63–73% | inconclusive |
| All rows from day 0, including back-filled | R4 | next 24 h | 95% | 23200 | 440 | 95.1% | 92.3–97.9% | 92–98% | PASS |
| Run-in (before day 0) | R1 | next 1 h | 68% | 14250 | 281 | 71.0% | 67.6–74.5% | 63–73% | inconclusive |
| Run-in (before day 0) | R2 | next 1 h | 95% | 14250 | 281 | 95.2% | 93.6–96.8% | 92–98% | PASS |
| Run-in (before day 0) | R3 | next 24 h | 68% | 14250 | 281 | 72.1% | – | 63–73% | too few data yet |
| Run-in (before day 0) | R4 | next 24 h | 95% | 14250 | 281 | 97.3% | – | 92–98% | too few data yet |

Coins furthest from the 68% claim on the 24-hour range (primary sample):

| Coin | Coverage | Forecasts |
|---|---|---|
| TRX | 58% | 443 |
| BTC | 59% | 443 |
| BNB | 60% | 443 |
| ETH | 60% | 443 |
| XRP | 63% | 443 |
| FET | 80% | 443 |
| ICP | 81% | 443 |
| OP | 81% | 443 |
| DOT | 82% | 443 |
| FIL | 86% | 443 |

Information only, not investment advice.
