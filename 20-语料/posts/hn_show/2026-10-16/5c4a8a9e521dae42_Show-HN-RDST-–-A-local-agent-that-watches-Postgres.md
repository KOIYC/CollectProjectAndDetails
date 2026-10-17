---
type: "corpus"
item_id: "5c4a8a9e521dae42"
title: "Show HN: RDST – A local agent that watches Postgres/MySQL for query regressions"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50107729"
project_url: "https://github.com/readysettech/rdst"
author: "gvsg"
published_at: "2026-10-15T18:09:01Z"
captured_at: "2026-10-16T09:35:18+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-10-16"
pub_day: "2026-10-15"
tags:
  - 语料
  - hn_show
  - author_gvsg
  - story_50107729
  - show_hn
metrics: {"points": 6, "comments": 1, "engagement_velocity": 6}
comments_count: 1
comments_total: 1
discovered_via: "hn:show_hn:3d"
---

# Show HN: RDST – A local agent that watches Postgres/MySQL for query regressions

> [!info] 一句话导读
> Default branch: main

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50107729>
> 指标：点赞=6 · 评论=1 · engagement_velocity=6
> 作者：gvsg　|　发布：2026-10-15T18:09:01Z
> 项目链接：<https://github.com/readysettech/rdst>
> 采集：2026-10-16T09:35:18+08:00　|　id：`5c4a8a9e521dae42`

## 正文

# readysettech/rdst

- Stars: 0
- Forks: 0
- Watchers: 0
- Open issues: 0
- License: Other
- Default branch: main
- Created: 2026-04-28T16:46:40Z

## Languages

- Python
- Shell
- TypeScript

## Top Contributors

- gvsg-rs (42 contributions)
- seanreadyset (32 contributions)
- mvreadyset (30 contributions)
- ofarukaydin (21 contributions)
- davisjc (1 contributions)

---

## README

# RDST - Readyset Data and SQL Toolkit

A command-line tool for database diagnostics, query analysis, performance tuning, and caching optimization with Readyset.

## What is RDST?

RDST helps you:
- Analyze SQL queries for caching opportunities
- Identify slow queries in real-time
- Get optimization suggestions
- Evaluate query compatibility with Readyset cache
- Manage database connection profiles

## Installation

### Using uvx (recommended - no installation required)

Run RDST directly without installing:

```bash
uvx rdst --help
uvx rdst analyze "SELECT * FROM users WHERE id = 1"
```

### Using pipx (persistent installation)

Install globally:

```bash
# Install
pipx install rdst

# Run
rdst --help

# Upgrade to latest version
pipx upgrade rdst
```

### Using pip

```bash
pip install rdst
```

> **After installing**, run `rdst init` to configure your first database connection.

## Quick Start

1. **Initialize RDST:**
   ```bash
   rdst init
   # Or with uvx (no installation needed):
   uvx rdst init
   ```

2. **Configure database connection:**
   ```bash
   rdst configure add-target mydb \
     --host localhost \
     --port 5432 \
     --database myapp \
     --user postgres
   ```

3. **Analyze queries:**
   ```bash
   # Analyze a specific query
   rdst analyze "SELECT * FROM users WHERE active = true"

   # With uvx:
   uvx rdst analyze "SELECT * FROM users WHERE active = true"

   # Analyze with Readyset cache evaluation
   rdst analyze --readyset-cache "SELECT * FROM products ORDER BY created_at"
   ```

4. **Monitor slow queries:**
   ```bash
   rdst top
   # Or: uvx rdst top
   ```

5. **Audit your fleet:**
   ```bash
   # Snapshot all ReadySet clusters and audit their health
   rdst fleet audit --target prod

   # Import clusters from your infrastructure
   rdst fleet import --target prod
   ```

 Fleet audit checks cache utilization, query support, and configuration
 across your ReadySet deployments. See the
 fleet audit docs
 for more.

## Commands

All commands can be run with `rdst` (if installed) or `uvx rdst` (no installation):

- `rdst analyze` - Analyze SQL queries and evaluate caching opportunities
- `rdst top` - Live view of slow queries
- `rdst ask` - Natural language to SQL queries
- `rdst scan` - Scan codebases for ORM queries and analyze performance
- `rdst fleet audit` - Audit ReadySet cluster health and cache utilization
- `rdst fleet import` - Import ReadySet clusters from your infrastructure
- `rdst schema` - Manage the semantic layer for better query generation
- `rdst query` - Manage query registry
- `rdst configure` - Manage database targets and connection profiles
- `rdst init` - First-time setup wizard
- `rdst version` - Show version information

**Example with uvx:**
```bash
uvx rdst analyze "SELECT * FROM orders WHERE status = 'pending'"
```

## Requirements

- Python 3.11 or higher
- PostgreSQL or MySQL database access

## About Readyset

Readyset is a SQL caching engine that sits between your application and database, automatically caching query results to improve performance. Learn more at readyset.io.

## Documentation

- Readyset Documentation
- GitHub Repository
- Report Issues

## License

MIT License - see LICENSE file for details

# IshekKhal/bitrun

## 评论（1/1）

> **Frone125** · 2026-10-15T18:38:26.000Z　
> This is really interesting. I'm almost at the point where I'd be fully ready to let the agent just apply the indexes and database fixes for me. I'd say i don't fully trust AI on that level yet, but I could see that being an awesome feature for this tool. Regardless, I love the suggestions that it gives. Even if i don't create every single index it suggests im glad that it looks at ones you should drop too.

## 导航

- 项目页：[[10-项目/github.com_b0dfc6e7]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
