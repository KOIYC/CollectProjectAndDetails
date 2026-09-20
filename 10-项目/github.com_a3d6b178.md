---
type: "project"
title: "Show HN: A chess analyzer that runs in the browser"
project_url: "https://github.com/huytd/whyblunder"
first_seen: "2026-09-20T14:05:47+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_huydotnet
  - story_49720669
  - show_hn
lang: "en"
---

# Show HN: A chess analyzer that runs in the browser

> [!info] 一句话导读
> Analyze chess games from PGN, identify blunders, mistakes,...

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://github.com/huytd/whyblunder>
> 首次收录：2026-09-20T14:05:47+08:00
> 来源渠道：HN Show HN
> 标签：author_huydotnet, story_49720669, show_hn
> 最新指标：点赞=3 · 评论=2 · engagement_velocity=3

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-09-20T09:23:24+08:00 | HN Show HN | 点赞=3 · 评论=2 · engagement_velocity=3 | [[20-语料/posts/hn_show/2026-09-20/d341dc24e90b56ac_Show-HN-A-chess-analyzer-that-runs-in-the-browser]] |
| 2026-09-20T09:37:08+08:00 | HN Show HN | 点赞=3 · 评论=2 · engagement_velocity=3 | [[20-语料/posts/hn_show/2026-09-20/d341dc24e90b56ac_Show-HN-A-chess-analyzer-that-runs-in-the-browser]] |
| 2026-09-20T14:05:47+08:00 | HN Show HN | 点赞=3 · 评论=2 · engagement_velocity=3 | [[20-语料/posts/hn_show/2026-09-20/d341dc24e90b56ac_Show-HN-A-chess-analyzer-that-runs-in-the-browser]] |

## 摘要正文

# huytd/whyblunder  Analyze chess games from PGN, identify blunders, mistakes,...  - Stars: 9 - Forks: 0 - Watchers: 9 - Open issues: 1 - Homepage: https://whyblunder.vercel.app - Default branch: main - Created: 2025-03-10T07:17:25Z  ## Languages  - CSS - HTML - JavaScript  ## Topics  - analyze - blunder - chess - stockfish  ## Top Contributors  - huytd (52 contributions)  ---  ## README  # WhyBlunder  WhyBlunder is an in-browser, zero-backend chess game analyzer. It runs a parallelized pool of WebAssembly-compiled Stockfish engine workers directly on the client to classify move quality, detect tactical patterns, and generate human-readable explanations without server infrastructure.  Traditional chess analysis platforms route game evaluations to centralized server queues, introducing network latency, rate limits, infrastructure operating costs, and subscription walls. WhyBlunder offloads the entire computational pipeline (UCI engine evaluation, win-probability modeling, tactical pattern recognition, and variation tree parsing) to client Web Workers.  ---  ## Architecture & Data Flow  WhyBlunder executes an asynchronous, client-side analysis pipeline:  ```mermaid flowchart TD     A…
