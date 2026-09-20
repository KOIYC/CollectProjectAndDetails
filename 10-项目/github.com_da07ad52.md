---
type: "project"
title: "Show HN: Bottle – a tiny ledger for bot memory"
project_url: "https://github.com/imron/bottle"
first_seen: "2026-09-20T09:36:53+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_imron
  - story_49739531
  - show_hn
lang: "en"
---

# Show HN: Bottle – a tiny ledger for bot memory

> [!info] 一句话导读
> A tiny ledger for autonomous bots

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://github.com/imron/bottle>
> 首次收录：2026-09-20T09:36:53+08:00
> 来源渠道：HN Show HN
> 标签：author_imron, story_49739531, show_hn
> 最新指标：点赞=2 · 评论=0 · engagement_velocity=2

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-09-20T09:23:24+08:00 | HN Show HN | 点赞=2 · 评论=0 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-09-20/51f729a9e5638f45_Show-HN-Bottle-–-a-tiny-ledger-for-bot-memory]] |
| 2026-09-20T09:36:53+08:00 | HN Show HN | 点赞=2 · 评论=0 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-09-20/51f729a9e5638f45_Show-HN-Bottle-–-a-tiny-ledger-for-bot-memory]] |

## 摘要正文

# imron/bottle  A tiny ledger for autonomous bots  - Stars: 1 - Forks: 0 - Watchers: 1 - Open issues: 0 - Default branch: master - Created: 2026-08-31T15:58:20Z  ## Languages  - Rust - Shell  ---  ## README  # Bottle  Bottle is a tiny ledger that gives autonomous bots the ability to log facts against custom schemas and query those facts using a fixed set of commands.  It provides lightweight access to structured data.  ## Why it exists  Bots are good at noticing facts but bad at keeping them. The usual method is keeping notes in markdown files, but such notes lack consistent type information and structure. You cannot sum these facts efficiently, you have no consistent way to reason about them chronologically and two bots writing about the same facts cannot safely share information without stepping on each other's toes.  Bottle corrects for these things.  Users specify a schema containing fields with simple types (text, number, enum). Bots then log facts against those schemas and query those facts back in meaningful ways.  ## Why not markdown  Markdown is prose, bottle entries are structured data. Entries have types, ids, dates, and declared numbers you can group and sum far more ef…
