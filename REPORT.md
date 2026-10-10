# Live calibration of the board's typical-move ranges

Updated 2026-10-10 06:59 UTC. Rules and pass bands are fixed in [LIVE_TEST.md](https://github.com/sandordrpal/crypto-concordance-board/blob/main/research/LIVE_TEST.md) (R1-R4). Primary analysis: on-time forecasts from 2026-10-19; earlier rows are a run-in.

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
| Run-in (before day 0) | R1 | next 1 h | 68% | 3550 | 71 | 68.3% | – | 63–73% | too few data yet |
| Run-in (before day 0) | R2 | next 1 h | 95% | 3550 | 71 | 95.0% | – | 92–98% | too few data yet |
| Run-in (before day 0) | R3 | next 24 h | 68% | 2400 | 48 | 60.7% | – | 63–73% | too few data yet |
| Run-in (before day 0) | R4 | next 24 h | 95% | 2400 | 48 | 93.9% | – | 92–98% | too few data yet |

Information only, not investment advice.
