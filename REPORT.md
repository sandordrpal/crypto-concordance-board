# Live calibration of the board's typical-move ranges

Updated 2026-11-09 21:01 UTC. Rules and pass bands are fixed in [LIVE_TEST.md](https://github.com/sandordrpal/crypto-concordance-board/blob/main/research/LIVE_TEST.md) (R1-R4). Primary analysis: on-time forecasts from 2026-10-19; earlier rows are a run-in.

Coverage is the share of real moves that stayed inside the range. Confidence intervals (90%) are clustered by issue hour, because coins move together. PASS when the whole interval lies inside the band.

| Sample | Test | Horizon | Claimed | Forecasts | Issue hours | Coverage | 90% CI | Pass band | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| Primary (on time, from day 0) | R1 | next 1 h | 68% | 26450 | 524 | 72.2% | 69.4–75.0% | 63–73% | inconclusive |
| Primary (on time, from day 0) | R2 | next 1 h | 95% | 26450 | 524 | 96.2% | 95.0–97.3% | 92–98% | PASS |
| Primary (on time, from day 0) | R3 | next 24 h | 68% | 25300 | 501 | 73.7% | 66.6–80.9% | 63–73% | inconclusive |
| Primary (on time, from day 0) | R4 | next 24 h | 95% | 25300 | 501 | 95.6% | 93.1–98.2% | 92–98% | inconclusive |
| All rows from day 0, including back-filled | R1 | next 1 h | 68% | 27650 | 525 | 72.2% | 69.4–75.0% | 63–73% | inconclusive |
| All rows from day 0, including back-filled | R2 | next 1 h | 95% | 27650 | 525 | 96.2% | 95.0–97.3% | 92–98% | PASS |
| All rows from day 0, including back-filled | R3 | next 24 h | 68% | 26450 | 502 | 73.7% | 66.6–80.9% | 63–73% | inconclusive |
| All rows from day 0, including back-filled | R4 | next 24 h | 95% | 26450 | 502 | 95.6% | 93.1–98.2% | 92–98% | inconclusive |
| Run-in (before day 0) | R1 | next 1 h | 68% | 14250 | 281 | 71.0% | 67.6–74.5% | 63–73% | inconclusive |
| Run-in (before day 0) | R2 | next 1 h | 95% | 14250 | 281 | 95.2% | 93.6–96.8% | 92–98% | PASS |
| Run-in (before day 0) | R3 | next 24 h | 68% | 14250 | 281 | 72.1% | – | 63–73% | too few data yet |
| Run-in (before day 0) | R4 | next 24 h | 95% | 14250 | 281 | 97.3% | – | 92–98% | too few data yet |

Coins furthest from the 68% claim on the 24-hour range (primary sample):

| Coin | Coverage | Forecasts |
|---|---|---|
| TRX | 59% | 506 |
| BTC | 60% | 506 |
| ETH | 61% | 506 |
| BNB | 63% | 506 |
| BCH | 63% | 506 |
| OP | 82% | 506 |
| ICP | 82% | 506 |
| DOT | 83% | 506 |
| IMX | 83% | 506 |
| FIL | 86% | 506 |

Information only, not investment advice.
