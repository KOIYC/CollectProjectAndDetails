---
type: "corpus"
item_id: "afe5ac06d4299337"
title: "Show HN: Content-aware PII redaction with Jev in Postgres"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49743434"
project_url: "https://pg-redact.vercel.app/"
author: "rishi_"
published_at: "2026-09-17T16:52:18Z"
captured_at: "2026-09-20T09:36:50+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-20"
pub_day: "2026-09-17"
tags:
  - 语料
  - hn_show
  - author_rishi_
  - story_49743434
  - show_hn
metrics: {"points": 3, "comments": 0, "engagement_velocity": 3}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:90d"
---

# Show HN: Content-aware PII redaction with Jev in Postgres

> [!info] 一句话导读
> Author: Rishi Raj Jain

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49743434>
> 指标：点赞=3 · 评论=0 · engagement_velocity=3
> 作者：rishi_　|　发布：2026-09-17T16:52:18Z
> 项目链接：<https://pg-redact.vercel.app/>
> 采集：2026-09-20T09:36:50+08:00　|　id：`afe5ac06d4299337`

## 正文

Author: Rishi Raj Jain

pg_redact — Content-aware PII redaction, enforced in Postgres

# pg_redact()

Content-aware PII redaction, enforced in Postgres.

A support inbox in Postgres. Jev flags the personal data in each message, and Neon redacts or reveals it by your role. Not a blanket rule on a column: masking is content-aware, so the front office stays visible while a phone number in the same field does not.

Try obfuscated PII (“my cell is five five five, two one two, oh nine eight seven”) or a decoy (“meet at the corner of Hope and Main”).

## What people are saying

No clearance. Every detected identifier is redacted.

Clearance level 0 / 3

0 Messages

0 Identifiers

0 Redacted now

0 Visible now

PII types & sensitivity

- Name low
- Email medium
- Phone medium
- Address high
- ID / financial high

# crajah/post-graph-rag

## 导航

- 项目页：[[10-项目/pg-redact.vercel.app_4ea50a61]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
