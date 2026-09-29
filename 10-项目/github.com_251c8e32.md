---
type: "project"
title: "Show HN: iCli – Postgres health reporter and index optimizer"
project_url: "https://github.com/abhiraj-ku/iCli"
first_seen: "2026-09-29T09:42:55+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_abhirajabhi312
  - story_49882674
  - show_hn
lang: "en"
---

# Show HN: iCli – Postgres health reporter and index optimizer

> [!info] 一句话导读
> Suggest the indexing strategy for your database

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://github.com/abhiraj-ku/iCli>
> 首次收录：2026-09-29T09:42:55+08:00
> 来源渠道：HN Show HN
> 标签：author_abhirajabhi312, story_49882674, show_hn
> 最新指标：点赞=2 · 评论=0 · engagement_velocity=2

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-09-29T09:42:55+08:00 | HN Show HN | 点赞=2 · 评论=0 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-09-29/0e31ed07be5805d0_Show-HN-iCli-–-Postgres-health-reporter-and-index]] |

## 摘要正文

# abhiraj-ku/iCli  Suggest the indexing strategy for your database  - Stars: 1 - Forks: 0 - Watchers: 1 - Open issues: 0 - License: MIT License - Default branch: main - Created: 2026-09-18T17:03:45Z  ## Languages  - Go  ## Topics  - cli - cli-tool - golang - golang-application - golang-cli - postgres - postgresql  ## Top Contributors  - abhiraj-ku (33 contributions)  ---  ## README  # iCli - PostgreSQL query and index advisor  `iCli` is a Go CLI that reads PostgreSQL query statistics, explains the most expensive queries, identifies execution-plan bottlenecks, detects missing foreign key indexes, and reports unused indexes.  > [!NOTE] > 🔒 **Read-Only Guarantee**: `iCli` only executes read-only SQL queries (`SELECT` metadata and `EXPLAIN` plan analysis). It never mutates, inserts, or deletes any data in your database.  ## Demo  iCli example output  ## Features  - **Expensive Query Analysis**: Identifies slow and resource-heavy queries using `pg_stat_statements`. - **Execution Plan Profiling**: Runs `EXPLAIN (FORMAT JSON)` and detects plan bottlenecks (e.g., sequential scans, disk sort spillage, inefficient joins). - **Missing Foreign Key Index Detection**: Finds foreign key constrain…
