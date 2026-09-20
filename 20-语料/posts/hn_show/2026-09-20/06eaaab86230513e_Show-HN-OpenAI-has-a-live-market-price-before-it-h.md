---
type: "corpus"
item_id: "06eaaab86230513e"
title: "Show HN: OpenAI has a live market price before it has a stock ticker"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49747379"
project_url: "https://tickerlayer.com/symbols/openaiusdt-perp"
author: "tickerlayer"
published_at: "2026-09-17T22:12:19Z"
captured_at: "2026-09-20T14:02:47+08:00"
lang: "en"
kind: "post"
topic: "开发者工具"
shard: "2026-09-20"
pub_day: "2026-09-17"
tags:
  - 语料
  - hn_show
  - author_tickerlayer
  - story_49747379
  - show_hn
metrics: {"points": 2, "comments": 2, "engagement_velocity": 2}
comments_count: 2
comments_total: 2
discovered_via: "hn:show_hn:90d"
---

# Show HN: OpenAI has a live market price before it has a stock ticker

> [!info] 一句话导读
> OpenAI (OPENAIUSDT) Perpetual Price & Data API

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49747379>
> 指标：点赞=2 · 评论=2 · engagement_velocity=2
> 作者：tickerlayer　|　发布：2026-09-17T22:12:19Z
> 项目链接：<https://tickerlayer.com/symbols/openaiusdt-perp>
> 采集：2026-09-20T14:02:47+08:00　|　id：`06eaaab86230513e`

## 正文

Author: TickerLayer

OpenAI (OPENAIUSDT) Perpetual Price & Data API | TickerLayer

# OpenAI perpetual OPENAIUSDT

1,484.01 USDT+9.26 (+0.63%)

- Delayed 15 min
- Composite, indicative
- Trades around the clock
- As of Sep 17, 22:15 UTC

OPENAIUSDT is a perpetual futures contract on OpenAI, a private company with no listed share, priced in USDT around the clock. One composite bid, ask and mark from several independent markets. Delayed 15 minutes here, real time on the API.

REST

`GET /perpetuals/snapshot/OPENAIUSDT`

WebSocket

`perpetuals.quotes · OPENAIUSDT`

Bars

`1m · 5m · 15m · 1h · 4h · 1d`

Symbol discovery on every key. Prices on the Perpetuals plan.

## OPENAIUSDT price chart

Aug 18 to Sep 17 UTC

Previous close

1,474.75

Day range

1,463.68 1,504.49

52-week range

–

Volume

11.31K

Avg volume (30d)

7.90K

## OPENAIUSDT over time

- 1W−0.62%
- 1M+19.06%
- 3M+8.84%
- 6M–
- YTD–
- 1Y–

## OPENAIUSDT in your app, in real time

The page above is the delayed view. These are the calls that return OPENAIUSDT live: one snapshot for the headline numbers, one aggregate call for the chart, one WebSocket subscription for every tick after that. Same symbol, same field names, on every asset class.

GET Snapshot

```
curl "https://api.tickerlayer.com/perpetuals/snapshot/OPENAIUSDT" \
  -H "x-api-key: YOUR_API_KEY"
```

GET Daily bars, one year

```
curl "https://api.tickerlayer.com/perpetuals/agg/OPENAIUSDT/1/day/2025-09-17/2026-09-17" \
  -H "x-api-key: YOUR_API_KEY"
```

WS Subscribe on stream.tickerlayer.com

```
{
  "action": "subscribe",
  "channels": ["perpetuals.quotes", "perpetuals.marks"],
  "symbols": ["OPENAIUSDT"]
}
```

200 Snapshot shape, delayed values

```
{
  "symbol": "OPENAIUSDT",
  "last_price": 1484.01,
  "prev_close": 1474.75,
  "change": 9.26,
  "change_percent": 0.63,
  "last_timestamp": 1789683300000
}
```

## Frequently asked questions

Is the OPENAIUSDT price on this page real-time?

No. The price, the ranges, and the chart are delayed by at least 15 minutes and refresh periodically. Real-time OPENAIUSDT quotes, mark prices and trades are delivered through the REST endpoints and the WebSocket channels on an API key with the Perpetuals plan.

What is OPENAIUSDT?

OPENAIUSDT is a perpetual futures contract on OpenAI, a private company with no listed share. A perpetual has no expiry and trades 24 hours a day, 7 days a week, so it keeps printing a price when the underlying market is closed. It is a derivative: it is not the underlying itself, carries no ownership or shareholder rights, and its price can differ from the underlying, most of all outside the underlying's own trading hours.

Where does the OPENAIUSDT data come from?

TickerLayer consolidates top-of-book quotes and mark prices from several independent perpetual futures markets into one composite per contract: the median of the live bids and the median of the live asks, with source_count on every message. It is a calculated reference, not an executable quote, and it is not the price of the underlying on its primary market. TickerLayer is a data provider: it does not list, offer or trade this contract.

How do I get OPENAIUSDT market data through the API?

Call GET /perpetuals/snapshot/OPENAIUSDT for bid, ask, mark price, previous close and change in one response, GET /perpetuals/quote/OPENAIUSDT and GET /perpetuals/mark/OPENAIUSDT for each on its own, and GET /perpetuals/agg/OPENAIUSDT/1/day/{from}/{to} for OHLCV bars. Subscribe to perpetuals.quotes, perpetuals.marks or perpetuals.trades on the WebSocket to stream updates as they happen.

Which bar intervals are available for OPENAIUSDT?

One, five, and fifteen minute bars, one and four hour bars, and daily bars, each with a documented maximum window per request. Bars are built from traded prices on the contract's primary market source, and history starts when the contract was first listed, which for many perpetuals is recent.

Which plan includes OPENAIUSDT?

Symbol discovery is open to every API key. Prices need the Perpetuals plan: Individual covers REST, Business adds WebSocket streaming and commercial use. Redistributing the raw feed or displaying it as a standalone data product needs a separate agreement.

## 评论（2/2）

> **tickerlayer** · 2026-09-17T22:13:49.000Z　
> We recently added these perpetual markets to TickerLayer. The interesting part for us is seeing price discovery continue when the underlying exchange is closed, and in OpenAI’s case before there’s even a public stock. These aren’t shares, they’re perpetual markets referencing the underlying. Curious what people here think of this kind of data.

---

> **andsoitis** · 2026-09-17T22:17:32.000Z　
> This makes no sense.

## 关联链接

- https://api.tickerlayer.com/perpetuals/agg/OPENAIUSDT/1/day/2025-09-17/2026-09-17
- https://api.tickerlayer.com/perpetuals/snapshot/OPENAIUSDT

## 导航

- 项目页：[[10-项目/tickerlayer.com_73ee7860]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`开发者工具`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
