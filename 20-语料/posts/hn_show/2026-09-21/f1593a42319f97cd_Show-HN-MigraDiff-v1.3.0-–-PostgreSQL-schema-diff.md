---
type: "corpus"
item_id: "f1593a42319f97cd"
title: "Show HN: MigraDiff v1.3.0 – PostgreSQL schema diff with AI migration explanation"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=48338061"
project_url: "https://github.com/migradiff/migra/releases/tag/v1.3.0"
author: "lateos-ai"
published_at: "2026-05-30T16:34:22Z"
captured_at: "2026-09-21T02:52:52+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-21"
pub_day: "2026-05-30"
tags:
  - 语料
  - hn_show
  - author_lateos-ai
  - story_48338061
  - show_hn
metrics: {"points": 3, "comments": 0, "engagement_velocity": 3}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:144d"
---

# Show HN: MigraDiff v1.3.0 – PostgreSQL schema diff with AI migration explanation

> [!info] 一句话导读
> v1.3.0 — AI-Powered Migration Explanation & Migrations Folder Support

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=48338061>
> 指标：点赞=3 · 评论=0 · engagement_velocity=3
> 作者：lateos-ai　|　发布：2026-05-30T16:34:22Z
> 项目链接：<https://github.com/migradiff/migra/releases/tag/v1.3.0>
> 采集：2026-09-21T02:52:52+08:00　|　id：`f1593a42319f97cd`

## 正文

# v1.3.0 — AI-Powered Migration Explanation & Migrations Folder Support

- Tag: v1.3.0
- Repository: postgresql-tools/migra
- Published: 2026-05-30T15:28:38Z
- Author: leochong

---

## Install

 pip install --upgrade migradiff

## What's New

### AI-Powered Migration Explanation (--explain)

MigraDiff can now explain any migration in plain English — what
each change does, what risks it carries, and safer alternatives
for destructive operations.

 pip install migradiff[ai]
 migra --setup-ai
 migra --explain postgres://db_a postgres://db_b

Powered by Claude Haiku (Anthropic). Bring your own API key —
no data is sent to MigraDiff servers. Works with --output json,
--from-file, --from-migrations-dir, and all existing flags.

### Migrations Folder Input Mode (--from-migrations-dir)

Diff a directory of numbered migration files against a base
schema without requiring a live branch database.

 migra --from-migrations-dir ./supabase/migrations \
 postgres://db_production

Supports Supabase timestamp format, Flyway versioned format,
and standard numeric prefixes. Files applied in correct numeric
sort order (9 before 10, not lexicographic).

### Also in this release
- Naming clarification in README — CLI stays `migra` for backward
 compatibility, package is `migradiff`

Full changelog: https://github.com/migradiff/migra/blob/main/CHANGELOG.md

## Upgrading

 pip install --upgrade migradiff

# HumanForScale

## 关联链接

- https://github.com/migradiff/migra/blob/main/CHANGELOG.md

## 导航

- 项目页：[[10-项目/github.com_35b44a7b]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
