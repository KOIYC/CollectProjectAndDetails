---
type: "corpus"
item_id: "8fb7ec42f7c105e0"
title: "Show HN: Shop via CLI; for agents and software engineers"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50264240"
project_url: "https://storerouter.ai/playground"
author: "marram"
published_at: "2026-10-27T19:12:20Z"
captured_at: "2026-10-28T09:39:16+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-10-28"
pub_day: "2026-10-27"
tags:
  - 语料
  - hn_show
  - author_marram
  - story_50264240
  - show_hn
metrics: {"points": 5, "comments": 0, "engagement_velocity": 5}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:3d"
---

# Show HN: Shop via CLI; for agents and software engineers

> [!info] 一句话导读
> Hello HN!We're building a single search/browse API interface to thousands of ecommerce stores (hopefully, eventually, all of them). Inspired by Shopify's https:…

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50264240>
> 指标：点赞=5 · 评论=0 · engagement_velocity=5
> 作者：marram　|　发布：2026-10-27T19:12:20Z
> 项目链接：<https://storerouter.ai/playground>
> 采集：2026-10-28T09:39:16+08:00　|　id：`8fb7ec42f7c105e0`

## 正文

Hello HN!We're building a single search/browse API interface to thousands of ecommerce stores (hopefully, eventually, all of them). Inspired by Shopify's https://shop.dev, we embedded a WASM bridge of our CLI in our website.The idea is to provide an efficient commerce interface for agents; personal assistants (Instinct et al) or otherwise. The alternatives are to build a crawling system / Firecrawl, use an LLM search api (Exa, Parallel etc) or use embedded headless browsers. Collective action by brands/retailers to implement agentic-protocols (UCP, ACP etc) is unlikely; so we're doing it for them.Surprisingly, despite our coverage list being smaller than Shopify's and the search endpoint being slower (~3k ms for p90; because there is JEV and/or LLM to convert free form search to facets) the search results are often subjectively better:```
storerouter search 'gold frame pink tint sunglasses' --facet category_path.depth_3=sunglasses --facet temple_color=gold --facet lens_color=pink --facet eyewear_frame_material=metal
```vs Shop.dev's:
```
shop search 'gold frame pink tint sunglasses' --category gid://shopify/TaxonomyCategory/aa-2-27
# dropped facet temple_color=temple_color__gold (no Shopify filter)
# dropped facet lens_color=lens_color__pink (no Shopify filter)
# dropped facet eyewear_frame_material=eyewear_frame_material__metal (no Shopify filter)
# category 'sunglasses' → Apparel & Accessories > Clothing Accessories > Sunglasses
```

## 关联链接

- https://shop.dev,

## 导航

- 项目页：[[10-项目/storerouter.ai_d54712eb]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
