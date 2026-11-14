# Live calibration of the board's typical-move ranges

Updated 2026-11-14 17:02 UTC. Rules and pass bands are fixed in [LIVE_TEST.md](https://github.com/sandordrpal/crypto-concordance-board/blob/main/research/LIVE_TEST.md) (R1-R4). Primary analysis: on-time forecasts from 2026-10-19; earlier rows are a run-in.

Coverage is the share of real moves that stayed inside the range. Confidence intervals (90%) are clustered by issue hour, because coins move together. PASS when the whole interval lies inside the band.

| Sample | Test | Horizon | Claimed | Forecasts | Issue hours | Coverage | 90% CI | Pass band | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| Primary (on time, from day 0) | R1 | next 1 h | 68% | 32300 | 640 | 70.8% | 68.3–73.4% | 63–73% | inconclusive |
| Primary (on time, from day 0) | R2 | next 1 h | 95% | 32300 | 640 | 95.8% | 94.7–96.9% | 92–98% | PASS |
| Primary (on time, from day 0) | R3 | next 24 h | 68% | 31100 | 617 | 72.1% | 66.0–78.2% | 63–73% | inconclusive |
| Primary (on time, from day 0) | R4 | next 24 h | 95% | 31100 | 617 | 95.4% | 93.2–97.5% | 92–98% | PASS |
| All rows from day 0, including back-filled | R1 | next 1 h | 68% | 33750 | 641 | 70.8% | 68.3–73.4% | 63–73% | inconclusive |
| All rows from day 0, including back-filled | R2 | next 1 h | 95% | 33750 | 641 | 95.8% | 94.7–96.9% | 92–98% | PASS |
| All rows from day 0, including back-filled | R3 | next 24 h | 68% | 32500 | 618 | 72.1% | 66.0–78.2% | 63–73% | inconclusive |
| All rows from day 0, including back-filled | R4 | next 24 h | 95% | 32500 | 618 | 95.4% | 93.3–97.5% | 92–98% | PASS |
| Run-in (before day 0) | R1 | next 1 h | 68% | 14250 | 281 | 71.0% | 67.6–74.5% | 63–73% | inconclusive |
| Run-in (before day 0) | R2 | next 1 h | 95% | 14250 | 281 | 95.2% | 93.6–96.8% | 92–98% | PASS |
| Run-in (before day 0) | R3 | next 24 h | 68% | 14250 | 281 | 72.1% | – | 63–73% | too few data yet |
| Run-in (before day 0) | R4 | next 24 h | 95% | 14250 | 281 | 97.3% | – | 92–98% | too few data yet |

Coins furthest from the 68% claim on the 24-hour range (primary sample):

| Coin | Coverage | Forecasts |
|---|---|---|
| BTC | 57% | 622 |
| ETH | 57% | 622 |
| BNB | 58% | 622 |
| XRP | 62% | 622 |
| TRX | 63% | 622 |
| WLD | 80% | 622 |
| OP | 81% | 622 |
| DOT | 82% | 622 |
| FET | 82% | 622 |
| FIL | 84% | 622 |

Information only, not investment advice.
