---
type: "project"
title: "Show HN: Arneb – A Trino-compatible distributed SQL engine in Rust"
project_url: "https://arneb.io/"
first_seen: "2026-10-16T09:35:18+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_jackypan1989
  - story_50103445
  - show_hn
lang: "en"
---

# Show HN: Arneb – A Trino-compatible distributed SQL engine in Rust

> [!info] 一句话导读
> Skip to content Arneb

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://arneb.io/>
> 首次收录：2026-10-16T09:35:18+08:00
> 来源渠道：HN Show HN
> 标签：author_jackypan1989, story_50103445, show_hn
> 最新指标：点赞=2 · 评论=0 · engagement_velocity=2

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-10-16T09:35:18+08:00 | HN Show HN | 点赞=2 · 评论=0 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-10-16/cc6f61bb231422ae_Show-HN-Arneb-–-A-Trino-compatible-distributed-SQL]] |

## 摘要正文

Skip to content Arneb Search K Main Navigation Guide SQL Reference Connectors Architecture Performance v0.1.2 Release notes  Changelog  Contributing Appearance Arneb Distributed SQL Query Engine  A Trino alternative built in Rust. Federated queries across heterogeneous data sources, served over the PostgreSQL wire protocol and Trino's client protocol.  Get Started  GitHub  Release notes Faster and Leaner than Trino  On all 22 TPC-H queries at SF10, cell-identical results, 2.3× faster warm and about a seventh of Trino's peak memory; faster on all 22 at SF30 too.  See the numbers Arrow-Native  All intermediate data in Apache Arrow columnar format. No row-by-row processing. PostgreSQL Compatible  Full Simple and Extended Query protocol. Works with psql, DBeaver, JDBC, and psycopg2 out of the box. Trino Client Compatible  Trino's REST protocol, so the trino CLI, Trino JDBC, Superset, Metabase and dbt-trino connect unchanged. Federated Queries  Query CSV and Parquet files, S3/GCS/Azure object stores, and Hive Metastore catalogs (Parquet, ORC, partitioned and Iceberg tables) from a single SQL interface. Distributed Execution  Coordinator-worker architecture with Apache Arrow Flight RPC f…
