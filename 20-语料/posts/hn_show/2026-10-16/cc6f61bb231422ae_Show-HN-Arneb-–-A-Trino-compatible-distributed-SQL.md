---
type: "corpus"
item_id: "cc6f61bb231422ae"
title: "Show HN: Arneb – A Trino-compatible distributed SQL engine in Rust"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50103445"
project_url: "https://arneb.io/"
author: "jackypan1989"
published_at: "2026-10-15T13:32:14Z"
captured_at: "2026-10-16T09:35:18+08:00"
lang: "en"
kind: "post"
topic: "开发者工具"
shard: "2026-10-16"
pub_day: "2026-10-15"
tags:
  - 语料
  - hn_show
  - author_jackypan1989
  - story_50103445
  - show_hn
metrics: {"points": 2, "comments": 0, "engagement_velocity": 2}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:3d"
---

# Show HN: Arneb – A Trino-compatible distributed SQL engine in Rust

> [!info] 一句话导读
> Skip to content Arneb

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50103445>
> 指标：点赞=2 · 评论=0 · engagement_velocity=2
> 作者：jackypan1989　|　发布：2026-10-15T13:32:14Z
> 项目链接：<https://arneb.io/>
> 采集：2026-10-16T09:35:18+08:00　|　id：`cc6f61bb231422ae`

## 正文

Skip to content Arneb
Search K
Main Navigation Guide SQL Reference Connectors Architecture Performance v0.1.2 Release notes
 Changelog
 Contributing
Appearance
Arneb Distributed SQL Query Engine
 A Trino alternative built in Rust. Federated queries across heterogeneous data sources, served over the PostgreSQL wire protocol and Trino's client protocol.
 Get Started
 GitHub
 Release notes
Faster and Leaner than Trino
 On all 22 TPC-H queries at SF10, cell-identical results, 2.3× faster warm and about a seventh of Trino's peak memory; faster on all 22 at SF30 too.
 See the numbers
Arrow-Native
 All intermediate data in Apache Arrow columnar format. No row-by-row processing.
PostgreSQL Compatible
 Full Simple and Extended Query protocol. Works with psql, DBeaver, JDBC, and psycopg2 out of the box.
Trino Client Compatible
 Trino's REST protocol, so the trino CLI, Trino JDBC, Superset, Metabase and dbt-trino connect unchanged.
Federated Queries
 Query CSV and Parquet files, S3/GCS/Azure object stores, and Hive Metastore catalogs (Parquet, ORC, partitioned and Iceberg tables) from a single SQL interface.
Distributed Execution
 Coordinator-worker architecture with Apache Arrow Flight RPC for high-throughput data exchange.

## 导航

- 项目页：[[10-项目/arneb.io_5a317069]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`开发者工具`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
