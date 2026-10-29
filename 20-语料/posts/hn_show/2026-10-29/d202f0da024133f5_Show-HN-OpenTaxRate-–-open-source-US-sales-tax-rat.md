---
type: "corpus"
item_id: "d202f0da024133f5"
title: "Show HN: OpenTaxRate – open-source US sales tax rates by street address"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50277662"
project_url: "https://github.com/equated-org/opentaxrate"
author: "winxton"
published_at: "2026-10-28T17:40:49Z"
captured_at: "2026-10-29T20:41:52+08:00"
lang: "en"
kind: "post"
topic: "开发者工具"
shard: "2026-10-29"
pub_day: "2026-10-28"
tags:
  - 语料
  - hn_show
  - author_winxton
  - story_50277662
  - show_hn
metrics: {"points": 4, "comments": 0, "engagement_velocity": 4}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:3d"
---

# Show HN: OpenTaxRate – open-source US sales tax rates by street address

> [!info] 一句话导读
> I built this because I tried many sales tax APIs and the problems were:

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50277662>
> 指标：点赞=4 · 评论=0 · engagement_velocity=4
> 作者：winxton　|　发布：2026-10-28T17:40:49Z
> 项目链接：<https://github.com/equated-org/opentaxrate>
> 采集：2026-10-29T20:41:52+08:00　|　id：`d202f0da024133f5`

## 正文

I built this because I tried many sales tax APIs and the problems were:
a) the rates were a black box with no source attached
b) lookups resolved by ZIP code.ZIP codes are postal routes, not tax jurisdictions. Stripe's Tax team wrote a good post on this [1]: two houses in Drexel, MO share a city, a ZIP, and nearly a house number, but sit in different counties with different rates. If your lookup key is the ZIP, you are wrong on those addresses, even when the rate table is accurate.OpenTaxRate resolves the street address instead:
- SST member states (24): the quarterly rate + boundary files, street ranges and ZIP+4, not just the rate tables
- Non-SST states: a custom adapter for each state, using its DOR's own published tables and boundary files (TX Comptroller, FL DR-15DSS, ALDOR, IDOR, NY Pub 718, California via CDTFA's lookup, etc)
- Census TIGER for geometryI tried with multiple open source geocoders you can self-host: Nominatim, Photon and Pelias, as well as proprietary ones (HERE, Geocodio, Mapbox, Google). Proprietary ones have higher accuracy, ~99.3% correct vs. 97.1% with just open source.For comparison: Avalara AvaTax 99.6%, TaxJar 98.2%. Public benchmark set are in the repo and at opentaxrate.com/benchmarks.Rates are just one part of sales tax, but also there's a ton of work in maintaining it as rules change. It doesn't handle exemptions, holidays, and caps.It returns the rate, plus the state's own location and jurisdiction codes for the address, resolved to the address, with its official source attached. MIT licensed, you can self-host with Postgres + PostGIS.[1]: https://stripe.dev/blog/how-we-built-it-jurisdiction-resolut...

## 关联链接

- https://stripe.dev/blog/how-we-built-it-jurisdiction-resolut...

## 导航

- 项目页：[[10-项目/github.com_03a4b834]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`开发者工具`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
