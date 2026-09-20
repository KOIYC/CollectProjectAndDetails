---
type: "corpus"
item_id: "014672a483749bf5"
title: "Show HN: Forexfin – Trading calculators, alerts and a journal in one place"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49770525"
project_url: "https://forexfin.tech/"
author: "howtobatman101"
published_at: "2026-09-19T22:12:18Z"
captured_at: "2026-09-20T09:48:16+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-20"
pub_day: "2026-09-19"
tags:
  - 语料
  - hn_show
  - author_howtobatman101
  - story_49770525
  - show_hn
metrics: {"points": 2, "comments": 0, "engagement_velocity": 2}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:3d"
---

# Show HN: Forexfin – Trading calculators, alerts and a journal in one place

> [!info] 一句话导读
> Some many years ago I started trading here and there and whenever I was doing it, I was bouncing between different platforms for position sizing, pip value, spr…

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49770525>
> 指标：点赞=2 · 评论=0 · engagement_velocity=2
> 作者：howtobatman101　|　发布：2026-09-19T22:12:18Z
> 项目链接：<https://forexfin.tech/>
> 采集：2026-09-20T09:48:16+08:00　|　id：`014672a483749bf5`

## 正文

Some many years ago I started trading here and there and whenever I was doing it, I was bouncing between different platforms for position sizing, pip value, spread cost etc. Each of them was more or less expensive, I've also met some nice free tools along the way. But. Long story short, I built my own stuff, because first of all, I wanted them in a single place, under my control and by building them, I would be learning something along the way.I'm inviting you to check ForexFin.techFor all my projects I used initially ChatGPT (static stuff), Codex, GitHub's Copilot. Since February I've been relying on Claude an my own research and learnings along the way.It is not a financial advice tool.There's still work to be done and I've got a semi-clear roadmap, but it is just this much you can do as solo dev and this week I'm just going to stop here and present it to the public. If you're having a spin, I would like to kindly ask you to use the "report a bug" button, if your time allows. Suggestions are also welecomed. I usually do follow ups to the reports, but you can write out if you don't want an update.What's in itCalculators: position size, pip value, spread cost, trade plan builder (shareable via URL hash), trade architect with a candle chartLive forex market hours / session overlap, DST- and weekend-awareCurrency strength meter (8-currency basket) and a pair correlation matrix with a 14/30/60/90d windowEmail price alerts across FX, crypto, metals, stocks and ETFsA trading journal that imports broker CSVs (or a screenshot) and reports behavioural stats rather than just P&LStack (boring, from what I've been told)Node 20 + Express 4, server-rendered HTMLSQLite via better-sqlite3, single file, migrations inline and idempotentFrontend is static HTML + one main.css + two small JS files. No framework, no bundler, no build step. FCP budget is under 1s on 4G and it's been easy to holdPM2 + nginx on a single small VPS, Let's EncryptMarket data from Twelve Data, with ECB reference rates as an automatic fallback so a vendor outage degrades instead of breakingPostmark for magic-link sign-in and alert emails. No trackers beyond consent-gated GA4

## 导航

- 项目页：[[10-项目/forexfin.tech_135907f4]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
