---
type: "project"
title: "Show HN: Warp – Run DeepSeek v4.1 Flash with 5 GB of RAM at 3.77 tok/s"
project_url: "https://github.com/sqliteai/warp"
first_seen: "2026-09-21T21:59:54+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_marcobambini
  - story_49714036
  - show_hn
lang: "en"
---

# Show HN: Warp – Run DeepSeek v4.1 Flash with 5 GB of RAM at 3.77 tok/s

> [!info] 一句话导读
> Run the full 2.78-trillion-parameter Kimi K3 model beyond available RAM by streaming activated weights directly from NVMe. A dependency-free, embeddable C infer…

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://github.com/sqliteai/warp>
> 首次收录：2026-09-21T21:59:54+08:00
> 来源渠道：HN Show HN
> 标签：author_marcobambini, story_49714036, show_hn
> 最新指标：点赞=13 · 评论=4 · engagement_velocity=13

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-09-20T09:23:24+08:00 | HN Show HN | 点赞=13 · 评论=4 · engagement_velocity=13 | [[20-语料/posts/hn_show/2026-09-20/50f24fcca5d4d7f6_Show-HN-Warp-–-Run-DeepSeek-v4.1-Flash-with-5-GB-o]] |
| 2026-09-20T14:06:09+08:00 | HN Show HN | 点赞=13 · 评论=4 · engagement_velocity=13 | [[20-语料/posts/hn_show/2026-09-20/50f24fcca5d4d7f6_Show-HN-Warp-–-Run-DeepSeek-v4.1-Flash-with-5-GB-o]] |
| 2026-09-21T21:59:54+08:00 | HN Show HN | 点赞=13 · 评论=4 · engagement_velocity=13 | [[20-语料/posts/hn_show/2026-09-20/50f24fcca5d4d7f6_Show-HN-Warp-–-Run-DeepSeek-v4.1-Flash-with-5-GB-o]] |

## 摘要正文

# sqliteai/warp  Run the full 2.78-trillion-parameter Kimi K3 model beyond available RAM by streaming activated weights directly from NVMe. A dependency-free, embeddable C inference engine.  - Stars: 2086 - Forks: 151 - Watchers: 2086 - Open issues: 10 - License: Apache License 2.0 - Homepage: https://sqlite.ai - Default branch: main - Created: 2026-07-28T20:56:00Z  ## Languages  - C - Makefile - Objective-C - Python - Shell  ## Top Contributors  - marcobambini (177 contributions) - isenbek (3 contributions) - pierre-x (2 contributions)  ---  ## README  # WARP — Weight-Aware Runtime and Paging (formerly WASTE)  WARP is an embeddable inference engine written in C, with no third-party runtime dependencies. It keeps the model trunk in memory, streams selected experts directly from disk, and uses the remaining RAM as a bounded expert cache.  The project is driven by humans: the ideas, hypotheses, priorities, tests, and decisions are human. The code is written by LLMs. At this scale, that is the only way to iterate on new algorithms and test hypotheses fast enough.  The goal is to run huge frontier models such as Kimi K3 on consumer hardware. Today, the complete 2.78-trillion-parameter …
