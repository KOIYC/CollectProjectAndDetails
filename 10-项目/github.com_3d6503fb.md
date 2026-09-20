---
type: "project"
title: "Show HN: Pg_column_Tetris – a pg extension for optimal column alignment"
project_url: "https://github.com/rogerwelin/pg_column_tetris"
first_seen: "2026-09-21T02:52:29+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_rogerw
  - story_47959459
  - show_hn
lang: "en"
---

# Show HN: Pg_column_Tetris – a pg extension for optimal column alignment

> [!info] 一句话导读
> rogerwelin/pg_column_tetris

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://github.com/rogerwelin/pg_column_tetris>
> 首次收录：2026-09-21T02:52:29+08:00
> 来源渠道：HN Show HN
> 标签：author_rogerw, story_47959459, show_hn
> 最新指标：点赞=2 · 评论=0 · engagement_velocity=2

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-09-21T01:09:14+08:00 | HN Show HN | 点赞=2 · 评论=0 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-09-21/3952842f4a6b44fd_Show-HN-Pg_column_Tetris-–-a-pg-extension-for-opti]] |
| 2026-09-21T01:13:42+08:00 | HN Show HN | 点赞=2 · 评论=0 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-09-21/3952842f4a6b44fd_Show-HN-Pg_column_Tetris-–-a-pg-extension-for-opti]] |
| 2026-09-21T02:52:29+08:00 | HN Show HN | 点赞=2 · 评论=0 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-09-21/3952842f4a6b44fd_Show-HN-Pg_column_Tetris-–-a-pg-extension-for-opti]] |

## 摘要正文

# rogerwelin/pg_column_tetris  A PostgreSQL extension that can enforce optimal column alignment to minimize row padding waste.  - Stars: 98 - Forks: 2 - Watchers: 98 - Open issues: 0 - License: MIT License - Default branch: main - Created: 2026-04-23T14:13:05Z  ## Languages  - Makefile - PLpgSQL  ## Top Contributors  - rogerwelin (30 contributions)  ---  ## README  # pg_column_tetris  PostgreSQL GitHub Actions Workflow Status License  A PostgreSQL extension that enforces optimal column alignment to minimize row padding waste.  - Warns on suboptimal `CREATE TABLE` statements during development - Enforces strict alignment in CI/CD pipelines - Audits existing tables and generates optimized migration scripts  ## Table of Contents  - Why Column Order Matters  - Alignment Groups - Requirements - Installation  - Self-hosted PostgreSQL  - Managed services (RDS, Cloud SQL, Supabase, Neon, etc.) - Usage  - Warn mode (default)  - Strict mode  - As an analysis tool  - Other configuration  - What gets checked - License  ## Why Column Order Matters  PostgreSQL stores each row as a sequence of bytes on disk. Column types have different sizes: a `bigint` takes 8 bytes, an `integer` takes 4, a `boo…
