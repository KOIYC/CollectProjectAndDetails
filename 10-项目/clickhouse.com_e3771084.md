---
type: "project"
title: "Show HN: Pg_chdb, fast imports from object storage to Postgres using COPY"
project_url: "https://clickhouse.com/blog/introducing-chdb-postgres"
first_seen: "2026-09-20T09:48:16+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_saisrirampur
  - story_49768601
  - show_hn
lang: "en"
---

# Show HN: Pg_chdb, fast imports from object storage to Postgres using COPY

> [!info] 一句话导读
> Collapse the terminal

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://clickhouse.com/blog/introducing-chdb-postgres>
> 首次收录：2026-09-20T09:48:16+08:00
> 来源渠道：HN Show HN
> 标签：author_saisrirampur, story_49768601, show_hn
> 最新指标：点赞=3 · 评论=0 · engagement_velocity=3

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-09-20T02:35:34+08:00 | HN Show HN | 点赞=2 · 评论=0 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-09-20/8ba66cf38a6fe6bc_Show-HN-Pg_chdb,-fast-imports-from-object-storage]] |
| 2026-09-20T02:46:51+08:00 | HN Show HN | 点赞=3 · 评论=0 · engagement_velocity=3 | [[20-语料/posts/hn_show/2026-09-20/8ba66cf38a6fe6bc_Show-HN-Pg_chdb,-fast-imports-from-object-storage]] |
| 2026-09-20T02:55:58+08:00 | HN Show HN | 点赞=3 · 评论=0 · engagement_velocity=3 | [[20-语料/posts/hn_show/2026-09-20/8ba66cf38a6fe6bc_Show-HN-Pg_chdb,-fast-imports-from-object-storage]] |
| 2026-09-20T03:04:29+08:00 | HN Show HN | 点赞=3 · 评论=0 · engagement_velocity=3 | [[20-语料/posts/hn_show/2026-09-20/8ba66cf38a6fe6bc_Show-HN-Pg_chdb,-fast-imports-from-object-storage]] |
| 2026-09-20T03:16:53+08:00 | HN Show HN | 点赞=3 · 评论=0 · engagement_velocity=3 | [[20-语料/posts/hn_show/2026-09-20/8ba66cf38a6fe6bc_Show-HN-Pg_chdb,-fast-imports-from-object-storage]] |
| 2026-09-20T03:29:12+08:00 | HN Show HN | 点赞=3 · 评论=0 · engagement_velocity=3 | [[20-语料/posts/hn_show/2026-09-20/8ba66cf38a6fe6bc_Show-HN-Pg_chdb,-fast-imports-from-object-storage]] |
| 2026-09-20T03:38:50+08:00 | HN Show HN | 点赞=3 · 评论=0 · engagement_velocity=3 | [[20-语料/posts/hn_show/2026-09-20/8ba66cf38a6fe6bc_Show-HN-Pg_chdb,-fast-imports-from-object-storage]] |
| 2026-09-20T09:20:19+08:00 | HN Show HN | 点赞=3 · 评论=0 · engagement_velocity=3 | [[20-语料/posts/hn_show/2026-09-20/8ba66cf38a6fe6bc_Show-HN-Pg_chdb,-fast-imports-from-object-storage]] |
| 2026-09-20T09:23:24+08:00 | HN Show HN | 点赞=3 · 评论=0 · engagement_velocity=3 | [[20-语料/posts/hn_show/2026-09-20/8ba66cf38a6fe6bc_Show-HN-Pg_chdb,-fast-imports-from-object-storage]] |
| 2026-09-20T09:48:16+08:00 | HN Show HN | 点赞=3 · 评论=0 · engagement_velocity=3 | [[20-语料/posts/hn_show/2026-09-20/8ba66cf38a6fe6bc_Show-HN-Pg_chdb,-fast-imports-from-object-storage]] |

## 摘要正文

Skip to content  Collapse the terminal  ->Scroll to top  <-Back  - Blog - / - Product  Copy pageCopied!More actions  - View as Markdown Open this page in Markdown - Open in ChatGPT Ask questions about this page - Open in Claude Ask questions about this page - Open in v0 Ask questions about this page  # Introducing chdb Postgres extension: High-performance imports from cloud storage  David Wheeler  Sep 8, 2026 · 11 minutes read  We're happy to announce a new Postgres extension: chdb. This extension expands Postgres import and export features via the chDB library, an in-process ClickHouse engine, providing efficient, flexible conversion to and from a wide array of data formats living on your favorite cloud storage systems.  ## Benchmark  And boy howdy do we mean efficient! We compared chdb's performance importing the NYC Taxi dataset (1m rows, wide table) in a number of data formats to three other Postgres extensions, all reading from a regionally-colocated AWS S3 bucket. To the chart!  > In order to minimize differences and to optimize for measurement of extension performance rather than infrastructure, the chdb, pg_lake, and pg_duckdb benchmarks ran on `r8id.xlarge` ClickHouse Mana…
