---
type: "project"
title: "Built a micro SaaS for a niche nobody was serving: table reservations for Shopify restaurants"
project_url: "https://apselo.com/reservics"
first_seen: "2026-09-26T09:42:53+08:00"
sources:
  - reddit
tags:
  - 项目
  - reddit
  - r/microsaas
lang: "en"
---

# Built a micro SaaS for a niche nobody was serving: table reservations for Shopify restaurants

> [!info] 一句话导读
> The niche is narrow on purpose. Restaurants that already run their site on Shopify and want to take table bookings there instead of paying for a separate bookin…

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://apselo.com/reservics>
> 首次收录：2026-09-26T09:42:53+08:00
> 来源渠道：Reddit 独立开发版块
> 标签：r/microsaas
> 最新指标：得分=4 · 评论=19 · 赞踩比=1

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-09-26T09:42:53+08:00 | Reddit 独立开发版块 | 得分=4 · 评论=19 · 赞踩比=1 | [[20-语料/posts/reddit/2026-09-26/7a35eb76285f6e0b_Built-a-micro-SaaS-for-a-niche-nobody-was-serving]] |

## 摘要正文

The niche is narrow on purpose. Restaurants that already run their site on Shopify and want to take table bookings there instead of paying for a separate booking platform. Shopify covers gift cards and online ordering, but reservations are a gap.  Reservics: [https://www.apselo.com/reservics/](https://www.apselo.com/reservics/)  Five months of nights and weekends to build. Currently 42 active users.  Technically the hardest part was not the app, it was the availability engine. Timezone handling plus overlapping slot logic plus per table capacity produced my first real production bug, a double booking on a Friday night. Shopify's embedded app layer with App Bridge, session tokens and the billing API ate roughly a month on its own.  Two things worth passing on for micro SaaS specifically. A narrow niche means your first ten users tell you exactly what to build, but you cannot rely on passive discovery, so almost all 42 came from me reaching out directly. And building on a platform like Shopify gives you billing and checkout for free, which sounds small until you realise you never have to touch card data.  Where I would like input: free to paid conversion. Deposits, floor plan and wai…
