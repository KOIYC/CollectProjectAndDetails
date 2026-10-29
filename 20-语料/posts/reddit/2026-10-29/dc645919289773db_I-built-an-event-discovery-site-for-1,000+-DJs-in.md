---
type: "corpus"
item_id: "dc645919289773db"
title: "I built an event-discovery site for 1,000+ DJs in pure PHP and vanilla JS — zero dependencies, zero frameworks. Here are the parts I'm weirdly proud of."
source: "reddit"
source_name: "Reddit 独立开发版块"
url: "https://www.reddit.com/r/SideProject/comments/1x9viuo/i_built_an_eventdiscovery_site_for_1000_djs_in/"
project_url: "https://thedjcalendar.com/"
author: "EmergencyIsland4574"
published_at: "2026-10-19T20:26:35+08:00"
captured_at: "2026-10-29T20:43:48+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-10-29"
pub_day: "2026-10-19"
tags:
  - 语料
  - reddit
  - r/SideProject
metrics: {"score": 3, "comments": 2, "upvote_ratio": 1}
comments_count: 2
comments_total: 2
discovered_via: "reddit:14d+settle10"
---

# I built an event-discovery site for 1,000+ DJs in pure PHP and vanilla JS — zero dependencies, zero frameworks. Here are the parts I'm weirdly proud of.

> [!info] 一句话导读
> Launched this week: [thedjcalendar.com](http://thedjcalendar.com) — tracks tour dates for the world's biggest DJs. Around 1,000 pages (artists, venues, cities, …

> [!meta]- 语料信息（点开展开）
> 来源：Reddit 独立开发版块（post）
> 原帖：<https://www.reddit.com/r/SideProject/comments/1x9viuo/i_built_an_eventdiscovery_site_for_1000_djs_in/>
> 指标：得分=3 · 评论=2 · 赞踩比=1
> 作者：EmergencyIsland4574　|　发布：2026-10-19T20:26:35+08:00
> 项目链接：<https://thedjcalendar.com/>
> 采集：2026-10-29T20:43:48+08:00　|　id：`dc645919289773db`

## 正文

Launched this week: [thedjcalendar.com](http://thedjcalendar.com) — tracks tour dates for the world's biggest DJs. Around 1,000 pages (artists, venues, cities, genres), and the whole thing is PHP + vanilla JS. No build step, no npm, no framework. I know that's a controversial lifestyle choice, so let me show the parts where it paid off.

**1. The search index is a prebuilt JSON file, not a server round-trip.**
Every artist name, alias and genre gets compiled into a static JSON index at deploy time. Client-side matching scores candidates and returns results in a keyboard-navigable combobox. Search feels instant because there's no network involved at all. On a shared host with no Node, this was the difference between "search box" and "search feature."

**2. The equalizer bars aren't animated — they're a readout.**
Hovering an artist card previews one of their tracks, and an 8-bar EQ reacts to the actual audio via Web Audio's AnalyserNode. Every animation frame the analyser hands me 32 frequency bins (0-255); bar N IS bin N. No easing, no random jitter to fake liveliness. When the preview stops, the bars flatline. It's an instrument readout, not a decoration — and it took real work to make the visuals match the production math exactly.

**3. SEO at 1,000 pages without a framework meant building the pipeline myself.**
Segmented sitemap generator that respects crawl budget, JSON-LD (MusicGroup + event schema) with strict visible-text parity checks, llms.txt, an answer-engine JSON endpoint for AI crawlers. None of it came from a library — it's all hand-rolled PHP, which also means I know exactly where every byte goes.

**4. Caching almost gaslit me.**
LiteSpeed page-caches HTML with a 5-minute TTL, so every deploy served stale pages for five minutes and I "verified" broken fixes more than once. Cache-busters on every live check now.

Happy to go deeper on any of these — the Web Audio EQ and the search index are the two I'd write full posts about (and probably will). Brutal feedback welcome, especially on the schema/SEO layer.

## 评论（2/2）

> **Minimum_Hour519**（1 分） · 2026-10-19T20:28:04+08:00　
> https://built.indie.pit.world/i/zjFWdPkY

---

> **EmergencyIsland4574**（1 分） · 2026-10-19T20:30:01+08:00　
> Since people always ask: stack is PHP 8 + vanilla JS, hosted on shared cPanel hosting, Cloudflare in front. The EQ preview system is the thing I'd most like a code review on — Web Audio + canvas, \~200 lines.

## 关联链接

- http://thedjcalendar.com

## 导航

- 项目页：[[10-项目/thedjcalendar.com_a47ceb9e]]
- 渠道页：[[50-渠道/reddit]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
