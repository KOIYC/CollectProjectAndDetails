---
type: "corpus"
item_id: "83d9742ac7011b3c"
title: "Show HN: Snitchmd – Cloudflare-protected URLs into clean Markdown via Docker"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=47949500"
project_url: "https://github.com/syabro/snitchmd"
author: "syabro"
published_at: "2026-04-29T15:07:51Z"
captured_at: "2026-09-21T01:41:49+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-21"
pub_day: "2026-04-29"
tags:
  - 语料
  - hn_show
  - author_syabro
  - story_47949500
  - show_hn
metrics: {"points": 8, "comments": 1, "engagement_velocity": 8}
comments_count: 1
comments_total: 1
discovered_via: "hn:show_hn:174d"
---

# Show HN: Snitchmd – Cloudflare-protected URLs into clean Markdown via Docker

> [!info] 一句话导读
> Shmauthor here. Built this for myself, putting it out in case it's useful.Needed any URL as clean Markdown for LLM context — including Cloudflare/anti-bot sites…

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=47949500>
> 指标：点赞=8 · 评论=1 · engagement_velocity=8
> 作者：syabro　|　发布：2026-04-29T15:07:51Z
> 项目链接：<https://github.com/syabro/snitchmd>
> 采集：2026-09-21T01:41:49+08:00　|　id：`83d9742ac7011b3c`

## 正文

Shmauthor here. Built this for myself, putting it out in case it's useful.Needed any URL as clean Markdown for LLM context — including Cloudflare/anti-bot sites. curl gets HTTP 403 on those, raw HTML is 80%+ nav noise eating context, paid SaaS (Firecrawl, Jina) wasn't an option for me.It's a Docker wrapper around two existing OSS tools — CloakBrowser (stealth Chromium that passes Cloudflare) and rs-trafilatura (HTML → Markdown). No new scraper, just glue. Runs locally, my URLs stay on my boxToken reduction (raw curl HTML vs snitchmd, tiktoken cl100k_base):- cloudflare.com/learning/bots — curl: HTTP 403 → snitchmd: 0.8k- docs.docker.com/engine/install — 187k → 0.9k- en.wikipedia.org/wiki/LLM — 222.7k → 29.7kHeads up: passes Cloudflare, can't solve "click traffic lights" captchas (reCAPTCHA v2, hCaptcha)MIT. Happy to answer questions

## 评论（1/1）

> **sc0rp10** · 2026-04-29T15:26:36.000Z　
> What's the difference with playwright?

## 导航

- 项目页：[[10-项目/github.com_75460815]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
