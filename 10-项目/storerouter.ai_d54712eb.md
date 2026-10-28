---
type: "project"
title: "Show HN: Shop via CLI; for agents and software engineers"
project_url: "https://storerouter.ai/playground"
first_seen: "2026-10-28T09:39:16+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_marram
  - story_50264240
  - show_hn
lang: "en"
---

# Show HN: Shop via CLI; for agents and software engineers

> [!info] 一句话导读
> Hello HN!We're building a single search/browse API interface to thousands of ecommerce stores (hopefully, eventually, all of them). Inspired by Shopify's https:…

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://storerouter.ai/playground>
> 首次收录：2026-10-28T09:39:16+08:00
> 来源渠道：HN Show HN
> 标签：author_marram, story_50264240, show_hn
> 最新指标：点赞=5 · 评论=0 · engagement_velocity=5

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-10-28T09:39:16+08:00 | HN Show HN | 点赞=5 · 评论=0 · engagement_velocity=5 | [[20-语料/posts/hn_show/2026-10-28/8fb7ec42f7c105e0_Show-HN-Shop-via-CLI;-for-agents-and-software-engi]] |

## 摘要正文

Hello HN!We're building a single search/browse API interface to thousands of ecommerce stores (hopefully, eventually, all of them). Inspired by Shopify's https://shop.dev, we embedded a WASM bridge of our CLI in our website.The idea is to provide an efficient commerce interface for agents; personal assistants (Instinct et al) or otherwise. The alternatives are to build a crawling system / Firecrawl, use an LLM search api (Exa, Parallel etc) or use embedded headless browsers. Collective action by brands/retailers to implement agentic-protocols (UCP, ACP etc) is unlikely; so we're doing it for them.Surprisingly, despite our coverage list being smaller than Shopify's and the search endpoint being slower (~3k ms for p90; because there is JEV and/or LLM to convert free form search to facets) the search results are often subjectively better:``` storerouter search 'gold frame pink tint sunglasses' --facet category_path.depth_3=sunglasses --facet temple_color=gold --facet lens_color=pink --facet eyewear_frame_material=metal ```vs Shop.dev's: ``` shop search 'gold frame pink tint sunglasses' --category gid://shopify/TaxonomyCategory/aa-2-27 # dropped facet temple_color=temple_color__gold (n…
