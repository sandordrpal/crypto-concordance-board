# Live calibration of the board's typical-move ranges

Updated 2026-11-06 14:02 UTC. Rules and pass bands are fixed in [LIVE_TEST.md](https://github.com/sandordrpal/crypto-concordance-board/blob/main/research/LIVE_TEST.md) (R1-R4). Primary analysis: on-time forecasts from 2026-10-19; earlier rows are a run-in.

Coverage is the share of real moves that stayed inside the range. Confidence intervals (90%) are clustered by issue hour, because coins move together. PASS when the whole interval lies inside the band.

| Sample | Test | Horizon | Claimed | Forecasts | Issue hours | Coverage | 90% CI | Pass band | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| Primary (on time, from day 0) | R1 | next 1 h | 68% | 22450 | 445 | 71.7% | 68.8–74.7% | 63–73% | inconclusive |
| Primary (on time, from day 0) | R2 | next 1 h | 95% | 22450 | 445 | 96.2% | 94.9–97.5% | 92–98% | PASS |
| Primary (on time, from day 0) | R3 | next 24 h | 68% | 21250 | 422 | 71.6% | 63.4–79.8% | 63–73% | inconclusive |
| Primary (on time, from day 0) | R4 | next 24 h | 95% | 21250 | 422 | 94.9% | 91.9–97.9% | 92–98% | inconclusive |
| All rows from day 0, including back-filled | R1 | next 1 h | 68% | 23500 | 446 | 71.8% | 68.8–74.7% | 63–73% | inconclusive |
| All rows from day 0, including back-filled | R2 | next 1 h | 95% | 23500 | 446 | 96.2% | 94.9–97.5% | 92–98% | PASS |
| All rows from day 0, including back-filled | R3 | next 24 h | 68% | 22250 | 423 | 71.6% | 63.4–79.8% | 63–73% | inconclusive |
| All rows from day 0, including back-filled | R4 | next 24 h | 95% | 22250 | 423 | 94.9% | 92.0–97.9% | 92–98% | inconclusive |
| Run-in (before day 0) | R1 | next 1 h | 68% | 14250 | 281 | 71.0% | 67.6–74.5% | 63–73% | inconclusive |
| Run-in (before day 0) | R2 | next 1 h | 95% | 14250 | 281 | 95.2% | 93.6–96.8% | 92–98% | PASS |
| Run-in (before day 0) | R3 | next 24 h | 68% | 14250 | 281 | 72.1% | – | 63–73% | too few data yet |
| Run-in (before day 0) | R4 | next 24 h | 95% | 14250 | 281 | 97.3% | – | 92–98% | too few data yet |

Coins furthest from the 68% claim on the 24-hour range (primary sample):

| Coin | Coverage | Forecasts |
|---|---|---|
| TRX | 57% | 425 |
| BTC | 57% | 425 |
| BNB | 59% | 425 |
| ETH | 59% | 425 |
| VET | 64% | 425 |
| OP | 80% | 425 |
| IMX | 81% | 425 |
| ARB | 81% | 425 |
| DOT | 82% | 425 |
| FIL | 86% | 425 |

Information only, not investment advice.
