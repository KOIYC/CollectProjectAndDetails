---
type: "project"
title: "Show HN: pg_raw_parse - parse PgSQL in Rust"
project_url: "https://github.com/pgdogdev/pg_raw_parse"
first_seen: "2026-09-20T09:36:38+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_levkk
  - story_49755552
  - show_hn
lang: "en"
---

# Show HN: pg_raw_parse - parse PgSQL in Rust

> [!info] 一句话导读
> pgdogdev/pg_raw_parse

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://github.com/pgdogdev/pg_raw_parse>
> 首次收录：2026-09-20T09:36:38+08:00
> 来源渠道：HN Show HN
> 标签：author_levkk, story_49755552, show_hn
> 最新指标：点赞=2 · 评论=0 · engagement_velocity=2

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-09-20T09:23:24+08:00 | HN Show HN | 点赞=2 · 评论=0 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-09-20/21d69f842ccdd184_Show-HN-pg_raw_parse-parse-PgSQL-in-Rust]] |
| 2026-09-20T09:36:38+08:00 | HN Show HN | 点赞=2 · 评论=0 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-09-20/21d69f842ccdd184_Show-HN-pg_raw_parse-parse-PgSQL-in-Rust]] |

## 摘要正文

# pgdogdev/pg_raw_parse  The SQL parser powering pgdog.dev  - Stars: 2 - Forks: 0 - Watchers: 2 - Open issues: 1 - License: Apache License 2.0 - Homepage: https://pgdog.dev/ - Default branch: main - Created: 2026-06-16T20:02:45Z  ## Languages  - C - Rust  ## Top Contributors  - sgrif (101 contributions) - levkk (4 contributions)  ---  ## README  # PG Raw Parse ## Safe bindings to libpg_query  PG Raw Parse provides a low level wrapper around the PostgreSQL backend parser. These bindings, as well as some additional functionality are provided by libpg\_query.  In addition to parsing, we provide mechanisms to [traverse an AST], [construct new ASTs], and [transform ASTs]. See the API docs for more details.  [traverse an AST]: https://docs.rs/pg_raw_parse/latest/pg_raw_parse/walk/index.html [construct new ASTs]: https://docs.rs/pg_raw_parse/latest/pg_raw_parse/make/index.html [transform ASTs]: https://docs.rs/pg_raw_parse/latest/pg_raw_parse/transform/index.html  This library's API surface is primarily driven by the needs of PgDog. It is not intended to be a complete, one-size-fits-all solution to PostgreSQL ASTs. Contributions are welcome, but pull requests adding large and complex feat…
