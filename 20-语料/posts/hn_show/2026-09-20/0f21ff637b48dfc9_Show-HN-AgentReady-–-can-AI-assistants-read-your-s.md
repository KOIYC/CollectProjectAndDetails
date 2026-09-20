---
type: "corpus"
item_id: "0f21ff637b48dfc9"
title: "Show HN: AgentReady – can AI assistants read your site?"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49720850"
project_url: "https://shop.lumnika.com/lab/agentready?src=hackernews-showhn"
author: "deusautoai725"
published_at: "2026-09-16T00:50:37Z"
captured_at: "2026-09-20T09:37:07+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-20"
pub_day: "2026-09-16"
tags:
  - 语料
  - hn_show
  - author_deusautoai725
  - story_49720850
  - show_hn
metrics: {"points": 2, "comments": 0, "engagement_velocity": 2}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:90d"
---

# Show HN: AgentReady – can AI assistants read your site?

> [!info] 一句话导读
> AgentReady — can AI assistants actually read your site?

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49720850>
> 指标：点赞=2 · 评论=0 · engagement_velocity=2
> 作者：deusautoai725　|　发布：2026-09-16T00:50:37Z
> 项目链接：<https://shop.lumnika.com/lab/agentready?src=hackernews-showhn>
> 采集：2026-09-20T09:37:07+08:00　|　id：`0f21ff637b48dfc9`

## 正文

AgentReady — can AI assistants actually read your site?

# Can ChatGPT, Claude and Perplexity actually read your site?

Most site owners have never checked. We ask your page six times — once as a normal browser, then once as each of the crawlers that feed the assistants people now ask instead of Google — and show you what each one really got back. Everything below is a live request made when you press the button; nothing is cached, guessed or scored from a list.

### What each assistant's crawler got back

One real GET request per crawler, with that crawler's own published user-agent, made seconds ago. Served means it received substantially the same page a browser receives. Anything else means the assistant is answering questions about you from somewhere other than your site.

### The seven checks

Weighted by how much each one actually decides whether an assistant can use your page. Click a card for the raw evidence.

### Fix these first

Ordered by points recoverable, not by how easy they are to say.

### Put the result on your site

Self-contained SVG — no script, no tracker, no request to us. It states the grade and the date it was measured, and links back to this exact report so anyone can re-run it.

What this audit is, exactly. Six HTTP requests to the URL you gave, plus `/robots.txt`, `/llms.txt`, `/llms-full.txt`, `/sitemap.xml` and `/.well-known/security.txt`, all made from our server at the moment you pressed the button, with a 12-second timeout each.

One page, not your whole site. The URL you typed is the only page fetched. A site can be excellent on the homepage and unreadable on product pages — audit those too.

We do not run your JavaScript. That is the point: most crawlers do not either. If your text only appears after hydration, this audit sees what they see.

Being crawlable is a choice, not a virtue. A publisher blocking AI crawlers on purpose is not failing — it is trading reach for control. The score measures reachability; whether you want it is your call, and we say so rather than scoring your strategy.

A snapshot, not a monitor. Bot-defence rules change hourly and edge networks answer differently from different places. A single 403 can be your CDN having a bad minute — re-run it before you rebuild anything.

# alex-zaporozhan/leo

## 导航

- 项目页：[[10-项目/shop.lumnika.com_1cf9301c]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
