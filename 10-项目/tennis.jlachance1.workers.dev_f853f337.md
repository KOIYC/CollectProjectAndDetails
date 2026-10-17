---
type: "project"
title: "Show HN: Tennis, a local/offline context store"
project_url: "https://tennis.jlachance1.workers.dev/"
first_seen: "2026-10-17T13:35:15+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_pizzuh
  - story_50119473
  - show_hn
lang: "en"
---

# Show HN: Tennis, a local/offline context store

> [!info] 一句话导读
> Hi everyone! I'm Joe, and I built Tennis: a CLI that indexes and searches your context offline. You can index any files, your Chat & Claude sessions, Codex hist…

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://tennis.jlachance1.workers.dev/>
> 首次收录：2026-10-17T13:35:15+08:00
> 来源渠道：HN Show HN
> 标签：author_pizzuh, story_50119473, show_hn
> 最新指标：点赞=2 · 评论=0 · engagement_velocity=2

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-10-17T13:35:15+08:00 | HN Show HN | 点赞=2 · 评论=0 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-10-17/b2a1ab84cb8e27f4_Show-HN-Tennis,-a-local-offline-context-store]] |

## 摘要正文

Hi everyone! I'm Joe, and I built Tennis: a CLI that indexes and searches your context offline. You can index any files, your Chat & Claude sessions, Codex history, etc. All local and offline.I've always hated having chats siloed in Claude and not having an easy way to connect that context in other apps. Anything that exists today has a subscription and is stored on their servers, and really wanted something fast, local, and offline.How Tennis works: * SQLite/FTS5 (keyword) + vec0 (vector) * model2vec / potion-retrieval-32M (512-dim, 123MB). This is a flat vector table, and what helps make this work well local/offline. * RRF (k=60) fuses BM25 keyword rank + cosine semantic rank into one scoreTennis also creates markdown files called 'cards' at indexing time. This gives you an easy, summarized, human readable format to see what Tennis has. You can edit these files (but won't change the embeddings in SQLite).You can use Tennis via API and MCP. It's incredibly fast, and the MCP works great as a connector to different applications (ChatGPT, Claude, Opencode, etc).You can install and use it today: https://tennis.jlachance1.workers.dev/Thanks for checking this out! I would love any feedb…
