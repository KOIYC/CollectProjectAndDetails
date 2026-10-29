---
type: "project"
title: "Show HN: OpenTaxRate – open-source US sales tax rates by street address"
project_url: "https://github.com/equated-org/opentaxrate"
first_seen: "2026-10-29T20:41:52+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_winxton
  - story_50277662
  - show_hn
lang: "en"
---

# Show HN: OpenTaxRate – open-source US sales tax rates by street address

> [!info] 一句话导读
> I built this because I tried many sales tax APIs and the problems were:

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://github.com/equated-org/opentaxrate>
> 首次收录：2026-10-29T20:41:52+08:00
> 来源渠道：HN Show HN
> 标签：author_winxton, story_50277662, show_hn
> 最新指标：点赞=4 · 评论=0 · engagement_velocity=4

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-10-29T20:41:52+08:00 | HN Show HN | 点赞=4 · 评论=0 · engagement_velocity=4 | [[20-语料/posts/hn_show/2026-10-29/d202f0da024133f5_Show-HN-OpenTaxRate-–-open-source-US-sales-tax-rat]] |

## 摘要正文

I built this because I tried many sales tax APIs and the problems were: a) the rates were a black box with no source attached b) lookups resolved by ZIP code.ZIP codes are postal routes, not tax jurisdictions. Stripe's Tax team wrote a good post on this [1]: two houses in Drexel, MO share a city, a ZIP, and nearly a house number, but sit in different counties with different rates. If your lookup key is the ZIP, you are wrong on those addresses, even when the rate table is accurate.OpenTaxRate resolves the street address instead: - SST member states (24): the quarterly rate + boundary files, street ranges and ZIP+4, not just the rate tables - Non-SST states: a custom adapter for each state, using its DOR's own published tables and boundary files (TX Comptroller, FL DR-15DSS, ALDOR, IDOR, NY Pub 718, California via CDTFA's lookup, etc) - Census TIGER for geometryI tried with multiple open source geocoders you can self-host: Nominatim, Photon and Pelias, as well as proprietary ones (HERE, Geocodio, Mapbox, Google). Proprietary ones have higher accuracy, ~99.3% correct vs. 97.1% with just open source.For comparison: Avalara AvaTax 99.6%, TaxJar 98.2%. Public benchmark set are in the re…
