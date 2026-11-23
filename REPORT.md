# Live calibration of the board's typical-move ranges

Updated 2026-11-23 03:02 UTC. Rules and pass bands are fixed in [LIVE_TEST.md](https://github.com/sandordrpal/crypto-concordance-board/blob/main/research/LIVE_TEST.md) (R1-R4). Primary analysis: on-time forecasts from 2026-10-19; earlier rows are a run-in.

Coverage is the share of real moves that stayed inside the range. Confidence intervals (90%) are clustered by issue hour, because coins move together. PASS when the whole interval lies inside the band.

| Sample | Test | Horizon | Claimed | Forecasts | Issue hours | Coverage | 90% CI | Pass band | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| Primary (on time, from day 0) | R1 | next 1 h | 68% | 42500 | 842 | 68.3% | 65.9–70.7% | 63–73% | PASS |
| Primary (on time, from day 0) | R2 | next 1 h | 95% | 42500 | 842 | 94.9% | 93.8–96.1% | 92–98% | PASS |
| Primary (on time, from day 0) | R3 | next 24 h | 68% | 41300 | 819 | 69.5% | 63.0–76.0% | 63–73% | inconclusive |
| Primary (on time, from day 0) | R4 | next 24 h | 95% | 41300 | 819 | 93.5% | 90.4–96.6% | 92–98% | inconclusive |
| All rows from day 0, including back-filled | R1 | next 1 h | 68% | 44400 | 843 | 68.3% | 66.0–70.7% | 63–73% | PASS |
| All rows from day 0, including back-filled | R2 | next 1 h | 95% | 44400 | 843 | 94.9% | 93.8–96.1% | 92–98% | PASS |
| All rows from day 0, including back-filled | R3 | next 24 h | 68% | 43150 | 820 | 69.5% | 63.0–76.0% | 63–73% | inconclusive |
| All rows from day 0, including back-filled | R4 | next 24 h | 95% | 43150 | 820 | 93.5% | 90.4–96.6% | 92–98% | inconclusive |
| Run-in (before day 0) | R1 | next 1 h | 68% | 14250 | 281 | 71.0% | 67.6–74.5% | 63–73% | inconclusive |
| Run-in (before day 0) | R2 | next 1 h | 95% | 14250 | 281 | 95.2% | 93.6–96.8% | 92–98% | PASS |
| Run-in (before day 0) | R3 | next 24 h | 68% | 14250 | 281 | 72.1% | – | 63–73% | too few data yet |
| Run-in (before day 0) | R4 | next 24 h | 95% | 14250 | 281 | 97.3% | – | 92–98% | too few data yet |

Coins furthest from the 68% claim on the 24-hour range (primary sample):

| Coin | Coverage | Forecasts |
|---|---|---|
| BTC | 55% | 826 |
| ETH | 57% | 826 |
| BNB | 58% | 826 |
| TRX | 58% | 826 |
| UNI | 61% | 826 |
| OP | 76% | 826 |
| FET | 77% | 826 |
| TIA | 77% | 826 |
| FIL | 78% | 826 |
| DOT | 78% | 826 |

Information only, not investment advice.
