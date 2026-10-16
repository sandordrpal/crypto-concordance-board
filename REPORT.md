# Live calibration of the board's typical-move ranges

Updated 2026-10-16 16:02 UTC. Rules and pass bands are fixed in [LIVE_TEST.md](https://github.com/sandordrpal/crypto-concordance-board/blob/main/research/LIVE_TEST.md) (R1-R4). Primary analysis: on-time forecasts from 2026-10-19; earlier rows are a run-in.

Coverage is the share of real moves that stayed inside the range. Confidence intervals (90%) are clustered by issue hour, because coins move together. PASS when the whole interval lies inside the band.

| Sample | Test | Horizon | Claimed | Forecasts | Issue hours | Coverage | 90% CI | Pass band | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| Primary (on time, from day 0) | R1 | next 1 h | 68% | 0 | 0 | – | – | 63–73% | too few data yet |
| Primary (on time, from day 0) | R2 | next 1 h | 95% | 0 | 0 | – | – | 92–98% | too few data yet |
| Primary (on time, from day 0) | R3 | next 24 h | 68% | 0 | 0 | – | – | 63–73% | too few data yet |
| Primary (on time, from day 0) | R4 | next 24 h | 95% | 0 | 0 | – | – | 92–98% | too few data yet |
| All rows from day 0, including back-filled | R1 | next 1 h | 68% | 0 | 0 | – | – | 63–73% | too few data yet |
| All rows from day 0, including back-filled | R2 | next 1 h | 95% | 0 | 0 | – | – | 92–98% | too few data yet |
| All rows from day 0, including back-filled | R3 | next 24 h | 68% | 0 | 0 | – | – | 63–73% | too few data yet |
| All rows from day 0, including back-filled | R4 | next 24 h | 95% | 0 | 0 | – | – | 92–98% | too few data yet |
| Run-in (before day 0) | R1 | next 1 h | 68% | 11350 | 225 | 69.8% | 65.9–73.6% | 63–73% | inconclusive |
| Run-in (before day 0) | R2 | next 1 h | 95% | 11350 | 225 | 95.0% | 93.1–96.9% | 92–98% | PASS |
| Run-in (before day 0) | R3 | next 24 h | 68% | 10100 | 202 | 65.3% | – | 63–73% | too few data yet |
| Run-in (before day 0) | R4 | next 24 h | 95% | 10100 | 202 | 96.4% | – | 92–98% | too few data yet |

Information only, not investment advice.
