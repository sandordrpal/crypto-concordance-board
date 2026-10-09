# Crypto Concordance Board

A single-page dashboard that shows how far six signal families agree on each of 50 cryptocurrencies, and how far three exchanges disagree on price. It runs entirely in the visitor's browser on free, keyless public market data and refreshes prices every 20 seconds.

It does not predict prices and nothing on it is investment advice.

**[Roadmap.md](Roadmap.md)** explains every function, every test with its pass and fail rules, the expected dates and results, and the 12-month roadmap.

## Run it

Open `index.html` in a normal browser tab. No build step and no server are needed.

To host it for free, enable GitHub Pages for this repository (Settings → Pages → deploy from the `main` branch, root folder). The page is then served at `https://<user>.github.io/<repo>/`.

If live data does not load, the page explains why and offers a simulated-data mode so the layout can still be inspected. Add `#demo` to the address to start in that mode.

## What it shows

| Family | Votes up when | Votes down when |
|---|---|---|
| Trend | At least two more of four checks point up than down (24 h, 3 d and 7 d return; price against its 7-day average) | The same checks point down |
| Stretch | Price is ≥ 2 standard deviations below its 7-day average | Price is ≥ 2 standard deviations above it |
| Order flow | Buyers' share of 24 h volume is in the top fifth of the last 20 days | It is in the bottom fifth |
| Positioning | Futures funding ≤ −0.01% | Funding ≥ +0.05% |
| Market tide | ≥ 65% of tracked coins are above their 7-day average | ≤ 35% are |
| Sentiment | Fear & Greed Index ≤ 25 | Fear & Greed Index ≥ 75 |

Each coin gets a **net score** (−100 to +100), a **discord score** (0 = no disagreement, 100 = even split) and a state: Aligned up, Leaning up, Split, Quiet, Leaning down or Aligned down.

The page also shows:

- the typical size of the next 1-hour and 24-hour move, from the last 30 days of hourly returns;
- the price gap between Binance, OKX and Bybit, in basis points;
- a history test that rebuilds each state for the past 30 days without look-ahead and reports what the price did next.

## Data sources

| Source | Used for | Refresh |
|---|---|---|
| Binance spot (`data-api.binance.vision`) | Prices, hourly candles, taker buy volume | Prices every 20 s; candles rotate through all coins every ~200 s |
| Binance USDⓈ-M futures (`fapi.binance.com`) | Funding rate, basis | 60 s |
| OKX, Bybit public tickers | Price cross-check | 120 s |
| alternative.me Crypto Fear & Greed Index | Sentiment | 30 min |

Each source fails independently; its status is shown at the top of the page. Rate-limit responses (HTTP 429/418) pause that source for the time the exchange asks.

## Settings

Edit the `CONFIG` block at the top of the script in `index.html`:

- `refreshSeconds`, `universeSize` and the refresh intervals of each source;
- `donation.buyMeACoffee`, the Buy Me a Coffee page shown as a button in the support panel (set to `''` to hide it);
- `donation.bitcoinAddress` and `donation.lightningAddress`. Paste a **receiving** address only, never a seed phrase or private key. Each option appears only once it is set.

## Known limits

- Live connections have not yet been verified from a browser; development testing used simulated data.
- The coin list starts from 64 well-known tickers and keeps the first 50 that Binance lists, filling gaps by 24 h trading volume. Rank is by volume, not market cap.
- The voting rules are unvalidated heuristics. Stretch, positioning and sentiment are read as contrarian by convention.
- Market tide and sentiment give every coin the same vote, and the families are not independent.
- The history test covers a few weeks of overlapping, correlated data and excludes positioning.
- No on-chain, ETF-flow or macro data. No server, so no alerts and no long-term stored track record.
- Visitors in countries where Binance blocks access will not get live data.

## Research pipeline

`research/` holds a model comparison that runs on GitHub Actions (`.github/workflows/research.yml`): on demand, whenever the research code changes, and once a day.

1. `research/collect.py` downloads about 50 daily variables from free public sources: Bitcoin and Ether prices, US equities, VIX and MOVE volatility, the dollar, gold, oil, Treasury yields and spreads, Fed balance sheet and money supply, Coin Metrics on-chain data, Fear & Greed, news-based policy uncertainty (EPU) and geopolitical risk (GPR), GDELT news tone, Wikipedia attention, stablecoin supply and futures funding. Each value is held back by its publication lag so models only see what was public at the time.
2. `research/model.py` builds leak-safe daily features and compares a random walk, a constant drift, ridge regression, polynomial ridge, XGBoost and a GRU neural network on 1-, 7- and 30-day returns and on the 30-day-ahead 50/100/200-day moving averages. Train 2018–2022, validate 2023, test 2024 onwards, with purged boundaries.

3. Three further tracks use hourly Binance candles with taker buy volume for the board's coins, with success thresholds fixed in advance in [`research/OUTCOMES.md`](research/OUTCOMES.md): Bitcoin volatility against the HAR benchmark plus a volatility-targeted holding (`vol.py`), weekly ranking of coins (`xsec.py`), and intraday order flow 1–12 hours ahead with a cost-aware strategy (`intraday.py`). `collect_hf.py` downloads the candles; `summarize.py` builds the scorecard.

4. `research/live_ranges.py` runs every hour (`.github/workflows/live.yml`). It logs the board's typical-move ranges for the next hour and day for 50 coins before the outcome is known, then scores them, on the append-only [`live-log`](../../tree/live-log) branch. The pass rules are fixed in [`research/LIVE_TEST.md`](research/LIVE_TEST.md).

Results, the collected data and run logs are published to the [`research-results`](../../tree/research-results) branch, whose README is the latest report. `research/synthetic.py` creates simulated inputs for testing the pipeline offline.

## Support

If the board is useful to you, you can support it at [buymeacoffee.com/palsandormd](https://buymeacoffee.com/palsandormd) or in Bitcoin at `3Mw3zMyh7wsQ3qaQNjWtmA4zeFoJNnRENf`.

## Attribution

Market data from the public APIs of Binance, OKX and Bybit. Sentiment from the Crypto Fear & Greed Index by alternative.me.
