---
type: "corpus"
item_id: "52e5eac9f38beecb"
title: "Show HN: Pappice live demo in browser via WASM"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49743479"
project_url: "https://pappice.eu/"
author: "lallero317"
published_at: "2026-09-17T16:55:04Z"
captured_at: "2026-09-20T09:36:49+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-20"
pub_day: "2026-09-17"
tags:
  - 语料
  - hn_show
  - author_lallero317
  - story_49743479
  - show_hn
metrics: {"points": 3, "comments": 0, "engagement_velocity": 3}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:90d"
---

# Show HN: Pappice live demo in browser via WASM

> [!info] 一句话导读
> Pappice - self-hosted support desk

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49743479>
> 指标：点赞=3 · 评论=0 · engagement_velocity=3
> 作者：lallero317　|　发布：2026-09-17T16:55:04Z
> 项目链接：<https://pappice.eu/>
> 采集：2026-09-20T09:36:49+08:00　|　id：`52e5eac9f38beecb`

## 正文

Pappice - self-hosted support desk

# The support desk you actually own.

 Pappice is a small, chat-style ticketing system for customers and staff. It runs as one lightweight Go binary with SQLite.

Release build. Used in production by a small team; not externally security audited.

### Customer portal

Customers open tickets, follow replies, and keep their support history in one place.

### Staff workflow

Staff assign tickets, set priorities, filter queues, and close requests when the support work is done.

### Chat-style replies

Public replies, internal notes, unread markers, pasted files, and inline previews fit the conversation flow.

### Admin control

Manage products, customers, staff accounts, API tokens, webhooks, audit events, and maintenance.

## AI-ready, without built-in AI.

 Pappice does not ship a bot or pick an AI provider. You create a normal account, assign the product role you want, and issue an API token. The token inherits that account's permissions, so an external agent can act only inside the boundaries you choose.

 For review-first workflows, the Internal contributor role is the narrow option: it can read tickets and add internal notes, but it cannot send public replies or edit tickets.

## One binary. One SQLite database.

 Pappice is built for small VPS deployments: run the binary, point it at a writable data directory, and put HTTPS in front. Application state lives in SQLite, attachments stay on disk, and email/webhook work is stored durably before delivery. The operational shape stays boring enough to back up and understand.

- Built with Go 1.26+
- Embedded SQLite driver
- Embedded HTML, CSS, and JavaScript
- Small instances around 20-30 MB RAM
- Role-scoped API tokens
- Stable webhook delivery IDs
- Idempotent ticket writes
- Built-in backup and restore

## Use the latest release.

The deploy guide resolves the latest release tag and covers nginx, systemd, Docker Compose, backups, restore, and upgrades. You can also try the public demo first.

# demeyer1/Autobot

## 导航

- 项目页：[[10-项目/pappice.eu_7fdbb995]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
