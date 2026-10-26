---
type: "project"
title: "Building a financial data SaaS solo: what I’ve learned turning an internal tool into a paid beta"
project_url: "https://stonkhub.net/"
first_seen: "2026-10-26T09:43:50+08:00"
sources:
  - reddit
tags:
  - 项目
  - reddit
  - r/SaaS
lang: "en"
---

# Building a financial data SaaS solo: what I’ve learned turning an internal tool into a paid beta

> [!info] 一句话导读
> I'm the solo developer behind StonkHub, a market research platform that aggregates public government and market data (congressional stock trades, lobbying, fede…

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://stonkhub.net/>
> 首次收录：2026-10-26T09:43:50+08:00
> 来源渠道：Reddit 独立开发版块
> 标签：r/SaaS
> 最新指标：得分=4 · 评论=13 · 赞踩比=1

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-10-26T09:43:50+08:00 | Reddit 独立开发版块 | 得分=4 · 评论=13 · 赞踩比=1 | [[20-语料/posts/reddit/2026-10-26/383d802841c808e6_Building-a-financial-data-SaaS-solo-what-I’ve-lear]] |

## 摘要正文

Howdy all,  I'm the solo developer behind StonkHub, a market research platform that aggregates public government and market data (congressional stock trades, lobbying, federal contracts, SEC filings, options positioning) into one dashboard.  It started as a tool I built for my own research. Friends wanted access, then their friends did, and at some point I had to decide whether this was a side project or a product. I went with product, and wanted to share some of the decisions along the way:  * Free tier vs paid: The free account includes all government data and social features. The $25/month beta unlocks the full feature set (GEX, technical screener, full watchlists, full premarket emails). My reasoning was that the government data is the hook and the easiest thing to understand, while the analytics and scanners are what active traders will actually pay for. * Pricing: I landed on $25/month by working backward from two things. First, cost: every paid user adds load across the data pipeline, Redis cache, MongoDB, and AI summaries, so I needed a price that stays profitable as usage grows. Second, the market: most tools covering just one of these data sets (congressional trades, GEX,…
