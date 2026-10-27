---
type: "project"
title: "Show HN: Markdown is 40× more token-efficient with SQLite"
project_url: "https://withnative.ai/research-and-posts/markdown-context-benchmark"
first_seen: "2026-10-27T23:46:32+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_richardcrng
  - story_50258875
  - show_hn
lang: "en"
---

# Show HN: Markdown is 40× more token-efficient with SQLite

> [!info] 一句话导读
> Hi HN, I'm Richard, founder of Native. I'm working on open-source context ownership, to stop AI centralisation: https://github.com/withnative/nativeMy first foc…

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://withnative.ai/research-and-posts/markdown-context-benchmark>
> 首次收录：2026-10-27T23:46:32+08:00
> 来源渠道：HN Show HN
> 标签：author_richardcrng, story_50258875, show_hn
> 最新指标：点赞=5 · 评论=0 · engagement_velocity=5

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-10-27T23:46:32+08:00 | HN Show HN | 点赞=5 · 评论=0 · engagement_velocity=5 | [[20-语料/posts/hn_show/2026-10-27/83fa85b46147b343_Show-HN-Markdown-is-40×-more-token-efficient-with]] |

## 摘要正文

Hi HN, I'm Richard, founder of Native. I'm working on open-source context ownership, to stop AI centralisation: https://github.com/withnative/nativeMy first focus has been making Markdown vaults powerful enough so that teams can self-host all of their context (messaging, docs and projects), without it being externally fragmented or rate-limited.I'm sharing some early results: Markdown vaults can be 40× more efficient with SQLite!https://www.withnative.ai/research-and-posts/markdown-contex...Here's some of the main ideas:- SQLite or Markdown folders, you pick. You can project the same authoritative event log into either form; more projection formats will follow (e.g. maybe neo4j; we do use a graph structure).- Empirically: SQLite is better for agents! On a 120 trial evaluation for 11,000 records, agents use 40× fewer tokens with SQLite vs Markdown, per correct answer.- Everything is a file or SQLite row. Messages, documents and projects: all can be modelled in your vault. You get local-first collaboration with teammates, synced to a cloud of your choice.- You can render your vault with arbitrary UI. Your WhatsApp-like UI speaks to your teammate's Slack-like UI; both are just views o…
