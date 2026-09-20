---
type: "corpus"
item_id: "21d69f842ccdd184"
title: "Show HN: pg_raw_parse - parse PgSQL in Rust"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49755552"
project_url: "https://github.com/pgdogdev/pg_raw_parse"
author: "levkk"
published_at: "2026-09-18T15:13:18Z"
captured_at: "2026-09-20T09:36:38+08:00"
lang: "en"
kind: "post"
topic: "开发者工具"
shard: "2026-09-20"
pub_day: "2026-09-18"
tags:
  - 语料
  - hn_show
  - author_levkk
  - story_49755552
  - show_hn
metrics: {"points": 2, "comments": 0, "engagement_velocity": 2}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:90d"
---

# Show HN: pg_raw_parse - parse PgSQL in Rust

> [!info] 一句话导读
> pgdogdev/pg_raw_parse

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49755552>
> 指标：点赞=2 · 评论=0 · engagement_velocity=2
> 作者：levkk　|　发布：2026-09-18T15:13:18Z
> 项目链接：<https://github.com/pgdogdev/pg_raw_parse>
> 采集：2026-09-20T09:36:38+08:00　|　id：`21d69f842ccdd184`

## 正文

# pgdogdev/pg_raw_parse

The SQL parser powering pgdog.dev

- Stars: 2
- Forks: 0
- Watchers: 2
- Open issues: 1
- License: Apache License 2.0
- Homepage: https://pgdog.dev/
- Default branch: main
- Created: 2026-06-16T20:02:45Z

## Languages

- C
- Rust

## Top Contributors

- sgrif (101 contributions)
- levkk (4 contributions)

---

## README

# PG Raw Parse
## Safe bindings to libpg_query

PG Raw Parse provides a low level wrapper around the PostgreSQL backend parser.
These bindings, as well as some additional functionality are provided by
libpg\_query.

In addition to parsing, we provide mechanisms to [traverse an AST], [construct
new ASTs], and [transform ASTs]. See the API docs for more details.

[traverse an AST]: https://docs.rs/pg_raw_parse/latest/pg_raw_parse/walk/index.html
[construct new ASTs]: https://docs.rs/pg_raw_parse/latest/pg_raw_parse/make/index.html
[transform ASTs]: https://docs.rs/pg_raw_parse/latest/pg_raw_parse/transform/index.html

This library's API surface is primarily driven by the needs of
PgDog. It is not intended to be a complete,
one-size-fits-all solution to PostgreSQL ASTs. Contributions are welcome, but
pull requests adding large and complex features are unlikely to be accepted
unless they align with PgDog's needs. For a more general purpose library,
consider pg\_query.rs.

## License

Licensed under either of these:

 * Apache License, Version 2.0, (LICENSE-APACHE or
 https://www.apache.org/licenses/LICENSE-2.0)
 * MIT license (LICENSE-MIT or
 https://opensource.org/licenses/MIT)

## 关联链接

- https://docs.rs/pg_raw_parse/latest/pg_raw_parse/make/index.html
- https://docs.rs/pg_raw_parse/latest/pg_raw_parse/transform/index.html
- https://docs.rs/pg_raw_parse/latest/pg_raw_parse/walk/index.html
- https://opensource.org/licenses/MIT
- https://pgdog.dev/
- https://www.apache.org/licenses/LICENSE-2.0

## 导航

- 项目页：[[10-项目/github.com_bc611ce9]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`开发者工具`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
