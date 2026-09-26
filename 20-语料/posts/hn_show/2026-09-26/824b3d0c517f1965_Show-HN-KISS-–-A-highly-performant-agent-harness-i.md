---
type: "corpus"
item_id: "824b3d0c517f1965"
title: "Show HN: KISS – A highly performant agent harness inspired off Pi built in Rust"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49851739"
project_url: "https://github.com/racetozero/kiss"
author: "racetozero"
published_at: "2026-09-26T00:05:09Z"
captured_at: "2026-09-26T09:41:08+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-26"
pub_day: "2026-09-26"
tags:
  - 语料
  - hn_show
  - author_racetozero
  - story_49851739
  - show_hn
metrics: {"points": 2, "comments": 2, "engagement_velocity": 2}
comments_count: 2
comments_total: 2
discovered_via: "hn:show_hn:3d"
---

# Show HN: KISS – A highly performant agent harness inspired off Pi built in Rust

> [!info] 一句话导读
> I built myself a highly performant agent harness built in Rust that's quite heavily inspired by Pi with a few extra addons like optional sub-agents, dynamic wor…

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49851739>
> 指标：点赞=2 · 评论=2 · engagement_velocity=2
> 作者：racetozero　|　发布：2026-09-26T00:05:09Z
> 项目链接：<https://github.com/racetozero/kiss>
> 采集：2026-09-26T09:41:08+08:00　|　id：`824b3d0c517f1965`

## 正文

I built myself a highly performant agent harness built in Rust that's quite heavily inspired by Pi with a few extra addons like optional sub-agents, dynamic workflows, MCP, ACP, WebMCP.It also has opt-in Jev support for dynamic compaction and dynamic reasoning/effort changing mid-turn.You can also embed it in your own projects. There are SDKs for Rust, Python, TypeScript, and WASM, plus JSONL RPC and WebSocket RPC for any other language. The WASM build runs the full agent loop in the browser without needing a server.I've been daily driving this harness at work and personal day to day because I have been quite happy with Pi but unhappy with its performance so this is built on the exact same principles of Pi.Performance: https://github.com/racetozero/kiss#performancePlease feel free to provide any feedback. All feedback is appreciated!

## 评论（2/2）

> **neduma** · 2026-09-26T00:20:29.000Z　
> omp?

---

> **racetozero** · 2026-09-26T00:37:38.000Z　
> I've used omp quite a bit before. This was designed to be intentionally minimalist without tons of built-in tools and LSP and all. I personally found the output to be much better without all that. Just base Pi works better for me than omp so this is using the same philosophy of Pi's minimalism but in very performant manner.The minimalism of Pi is quite an advantage which is what KISS follows because this allows the harness to be used nicely outside of a coding domain too. One example would be in the finance domain for doing agentic orchestration without the harness being very much biased towards coding/software eng.

## 关联链接

- https://github.com/racetozero/kiss#performancePlease

## 导航

- 项目页：[[10-项目/github.com_b9b374fc]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
