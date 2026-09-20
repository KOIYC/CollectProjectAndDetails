---
type: "project"
title: "Show HN: MigraDiff v1.3.0 – PostgreSQL schema diff with AI migration explanation"
project_url: "https://github.com/migradiff/migra/releases/tag/v1.3.0"
first_seen: "2026-09-21T02:52:52+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_lateos-ai
  - story_48338061
  - show_hn
lang: "en"
---

# Show HN: MigraDiff v1.3.0 – PostgreSQL schema diff with AI migration explanation

> [!info] 一句话导读
> v1.3.0 — AI-Powered Migration Explanation & Migrations Folder Support

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://github.com/migradiff/migra/releases/tag/v1.3.0>
> 首次收录：2026-09-21T02:52:52+08:00
> 来源渠道：HN Show HN
> 标签：author_lateos-ai, story_48338061, show_hn
> 最新指标：点赞=3 · 评论=0 · engagement_velocity=3

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-09-21T01:27:24+08:00 | HN Show HN | 点赞=3 · 评论=0 · engagement_velocity=3 | [[20-语料/posts/hn_show/2026-09-21/f1593a42319f97cd_Show-HN-MigraDiff-v1.3.0-–-PostgreSQL-schema-diff]] |
| 2026-09-21T02:52:52+08:00 | HN Show HN | 点赞=3 · 评论=0 · engagement_velocity=3 | [[20-语料/posts/hn_show/2026-09-21/f1593a42319f97cd_Show-HN-MigraDiff-v1.3.0-–-PostgreSQL-schema-diff]] |

## 摘要正文

# v1.3.0 — AI-Powered Migration Explanation & Migrations Folder Support  - Tag: v1.3.0 - Repository: postgresql-tools/migra - Published: 2026-05-30T15:28:38Z - Author: leochong  ---  ## Install   pip install --upgrade migradiff  ## What's New  ### AI-Powered Migration Explanation (--explain)  MigraDiff can now explain any migration in plain English — what each change does, what risks it carries, and safer alternatives for destructive operations.   pip install migradiff[ai]  migra --setup-ai  migra --explain postgres://db_a postgres://db_b  Powered by Claude Haiku (Anthropic). Bring your own API key — no data is sent to MigraDiff servers. Works with --output json, --from-file, --from-migrations-dir, and all existing flags.  ### Migrations Folder Input Mode (--from-migrations-dir)  Diff a directory of numbered migration files against a base schema without requiring a live branch database.   migra --from-migrations-dir ./supabase/migrations \  postgres://db_production  Supports Supabase timestamp format, Flyway versioned format, and standard numeric prefixes. Files applied in correct numeric sort order (9 before 10, not lexicographic).  ### Also in this release - Naming clarification …
