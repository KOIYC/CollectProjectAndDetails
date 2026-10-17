---
type: "project"
title: "Show HN: RDST – A local agent that watches Postgres/MySQL for query regressions"
project_url: "https://github.com/readysettech/rdst"
first_seen: "2026-10-16T09:35:18+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_gvsg
  - story_50107729
  - show_hn
lang: "en"
---

# Show HN: RDST – A local agent that watches Postgres/MySQL for query regressions

> [!info] 一句话导读
> Default branch: main

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://github.com/readysettech/rdst>
> 首次收录：2026-10-16T09:35:18+08:00
> 来源渠道：HN Show HN
> 标签：author_gvsg, story_50107729, show_hn
> 最新指标：点赞=6 · 评论=1 · engagement_velocity=6

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-10-16T09:35:18+08:00 | HN Show HN | 点赞=6 · 评论=1 · engagement_velocity=6 | [[20-语料/posts/hn_show/2026-10-16/5c4a8a9e521dae42_Show-HN-RDST-–-A-local-agent-that-watches-Postgres]] |

## 摘要正文

# readysettech/rdst  - Stars: 0 - Forks: 0 - Watchers: 0 - Open issues: 0 - License: Other - Default branch: main - Created: 2026-04-28T16:46:40Z  ## Languages  - Python - Shell - TypeScript  ## Top Contributors  - gvsg-rs (42 contributions) - seanreadyset (32 contributions) - mvreadyset (30 contributions) - ofarukaydin (21 contributions) - davisjc (1 contributions)  ---  ## README  # RDST - Readyset Data and SQL Toolkit  A command-line tool for database diagnostics, query analysis, performance tuning, and caching optimization with Readyset.  ## What is RDST?  RDST helps you: - Analyze SQL queries for caching opportunities - Identify slow queries in real-time - Get optimization suggestions - Evaluate query compatibility with Readyset cache - Manage database connection profiles  ## Installation  ### Using uvx (recommended - no installation required)  Run RDST directly without installing:  ```bash uvx rdst --help uvx rdst analyze "SELECT * FROM users WHERE id = 1" ```  ### Using pipx (persistent installation)  Install globally:  ```bash # Install pipx install rdst  # Run rdst --help  # Upgrade to latest version pipx upgrade rdst ```  ### Using pip  ```bash pip install rdst ```  > **A…
