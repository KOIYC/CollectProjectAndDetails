---
type: "corpus"
item_id: "3952842f4a6b44fd"
title: "Show HN: Pg_column_Tetris – a pg extension for optimal column alignment"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=47959459"
project_url: "https://github.com/rogerwelin/pg_column_tetris"
author: "rogerw"
published_at: "2026-04-30T07:43:31Z"
captured_at: "2026-09-21T02:52:29+08:00"
lang: "en"
kind: "post"
topic: "开发者工具"
shard: "2026-09-21"
pub_day: "2026-04-30"
tags:
  - 语料
  - hn_show
  - author_rogerw
  - story_47959459
  - show_hn
metrics: {"points": 2, "comments": 0, "engagement_velocity": 2}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:174d"
---

# Show HN: Pg_column_Tetris – a pg extension for optimal column alignment

> [!info] 一句话导读
> rogerwelin/pg_column_tetris

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=47959459>
> 指标：点赞=2 · 评论=0 · engagement_velocity=2
> 作者：rogerw　|　发布：2026-04-30T07:43:31Z
> 项目链接：<https://github.com/rogerwelin/pg_column_tetris>
> 采集：2026-09-21T02:52:29+08:00　|　id：`3952842f4a6b44fd`

## 正文

# rogerwelin/pg_column_tetris

A PostgreSQL extension that can enforce optimal column alignment to minimize row padding waste.

- Stars: 98
- Forks: 2
- Watchers: 98
- Open issues: 0
- License: MIT License
- Default branch: main
- Created: 2026-04-23T14:13:05Z

## Languages

- Makefile
- PLpgSQL

## Top Contributors

- rogerwelin (30 contributions)

---

## README

# pg_column_tetris

PostgreSQL
GitHub Actions Workflow Status
License

A PostgreSQL extension that enforces optimal column alignment to minimize row padding waste.

- Warns on suboptimal `CREATE TABLE` statements during development
- Enforces strict alignment in CI/CD pipelines
- Audits existing tables and generates optimized migration scripts

## Table of Contents

- Why Column Order Matters
 - Alignment Groups
- Requirements
- Installation
 - Self-hosted PostgreSQL
 - Managed services (RDS, Cloud SQL, Supabase, Neon, etc.)
- Usage
 - Warn mode (default)
 - Strict mode
 - As an analysis tool
 - Other configuration
 - What gets checked
- License

## Why Column Order Matters

PostgreSQL stores each row as a sequence of bytes on disk. Column types have different sizes: a `bigint` takes 8 bytes, an `integer` takes 4, a `boolean` takes just 1. So far so simple.

The problem is that PostgreSQL can't just pack them back to back. The CPU reads memory most efficiently when values are naturally aligned; an 8-byte value should start at a position divisible by 8, a 4-byte value at a position divisible by 4, and so on. To guarantee this, PostgreSQL inserts invisible **padding bytes** between columns whenever needed.

Here's an example. Say you create a table like this:

```sql
CREATE TABLE bad_order (
    active    boolean,   -- 1 byte
    user_id   bigint,    -- 8 bytes
    age       integer    -- 4 bytes
);
```

In memory, each row looks like:

```
[active: 1B] [7B padding] [user_id: 8B] [age: 4B]  →  20 bytes of column data
```

`user_id` needs to start at an 8-byte boundary, so PostgreSQL pads 7 bytes after `active` to get there. That's 7 wasted bytes **per row**.

Now reorder the columns largest-first:

```sql
CREATE TABLE good_order (
    user_id   bigint,    -- 8 bytes
    age       integer,   -- 4 bytes
    active    boolean    -- 1 byte
);
```

```
[user_id: 8B] [age: 4B] [active: 1B]  →  13 bytes of column data
```

Zero padding. Same data, 35% smaller rows. Multiply that across millions of rows and dozens of columns and it will adds up fast. Optimal column order is free performance: zero runtime cost, just a smarter `CREATE TABLE`.

### Alignment Groups

The extension sorts columns into these groups, largest alignment first:

1. **8-byte aligned** (`d`): `bigint`, `timestamptz`, `float8`, `interval`
2. **4-byte aligned** (`i`): `integer`, `float4`, `date`, `oid`
3. **2-byte aligned** (`s`): `smallint`
4. **1-byte aligned** (`c`): `boolean`, `char(1)`
5. **Variable-length** (varlena): `text`, `varchar`, `numeric`, `jsonb`, `bytea` - always last

Within each group, `NOT NULL` columns come first (minor CPU optimization for tuple deforming).

## Requirements

- PostgreSQL 14+
- Superuser or event trigger privileges (`rds_superuser` on RDS, `cloudsqlsuperuser` on Cloud SQL)

## Installation

Pure SQL/PL/pgSQL - no C, no compilation.

### Self-hosted PostgreSQL

```bash
make install
```

```sql
CREATE EXTENSION pg_column_tetris;
```

### Managed services (RDS, Cloud SQL, Supabase, Neon, etc.)

Since there's no C code, the extension runs anywhere PostgreSQL does:

```bash
psql -d your_database -f pg_column_tetris--0.1.0.sql
```

## Usage

The extension has three modes (`warn`, `strict`, `off`) that cover different workflows.

### Warn mode (default) - catch bad ordering during development

The extension installs in `warn` mode. Any `CREATE TABLE` with suboptimal column order emits a NOTICE but still succeeds:

```sql
CREATE TABLE orders (
    is_shipped boolean,
    order_total numeric,
    user_id bigint,
    item_ct smallint,
    order_dt timestamptz,
    status smallint,
    ship_dt timestamptz
);
```

```
NOTICE: pg_column_tetris: suboptimal column alignment — 19 bytes of fixed-width padding wasted per row
```

Good for development — you see the problem without breaking anything.

### Strict mode — enforce alignment in CI/migrations

In strict mode, `CREATE TABLE` with suboptimal column order is **blocked** and rolled back. The error message includes the optimal column order so you can fix it immediately:

```sql
SELECT column_tetris.set_mode('strict');

CREATE TABLE orders ( ... );
-- ERROR:  suboptimal column alignment — 19 bytes of fixed-width padding wasted per row
-- HINT:  Suggested order:
--     CREATE TABLE orders (
--         user_id bigint,          -- 8-byte aligned
--         order_dt timestamptz,    -- 8-byte aligned
--         ship_dt timestamptz,     -- 8-byte aligned
--         item_ct smallint,        -- 2-byte aligned
--         status smallint,         -- 2-byte aligned
--         is_shipped boolean,      -- 1-byte aligned
--         order_total numeric      -- varlena (last)
--     );
```

Use this in staging/production databases or CI pipelines to guarantee every new table has optimal alignment.

### As an analysis tool - audit existing tables

Use `padding_wasted()` to quickly check how many bytes a table wastes per row:

```sql
SELECT column_tetris.padding_wasted('orders');
-- Returns: 7  (bytes of avoidable padding per row)
```

Pass `'total'` to see the total waste across all rows in the table. Wrap with `pg_size_pretty()` for human-readable output:

```sql
SELECT pg_size_pretty(column_tetris.padding_wasted('orders', 'total'));
-- Returns: '458 MB'
```

Find all tables with padding waste:

```sql
SELECT schemaname, tablename,
       column_tetris.padding_wasted(schemaname || '.' || tablename) AS bytes_per_row
  FROM pg_tables
 WHERE schemaname = 'public'
   AND column_tetris.padding_wasted(schemaname || '.' || tablename) > 0;
```

Use `check()` for a detailed column-by-column layout report:

```sql
SELECT * FROM column_tetris.check('orders');
```

Use `suggest_rewrite()` to generate a migration script that reorders the columns optimally. **Caution** - it renames the original table, creates a new one, and copies all data. This means exclusive locks, downtime for that table, and lost foreign keys/indexes/triggers/defaults that aren't part of the generated DDL. Always review the output and test on a copy first:

```sql
SELECT column_tetris.suggest_rewrite('orders');
```

```sql
-- Generated output:
BEGIN;
ALTER TABLE public.orders RENAME TO orders_old;
CREATE TABLE public.orders ( ...optimal order... );
INSERT INTO public.orders SELECT ... FROM public.orders_old;
DROP TABLE public.orders_old;
COMMIT;
```

You can use `off` mode if you want to disable the event trigger entirely and just use the analysis functions.

### Other configuration

```sql
-- Check current mode
SELECT column_tetris.mode();

-- Exclude a table from validation (e.g., matching an external schema)
SELECT column_tetris.exclude('legacy_imports');

-- View excluded table-/s
SELECT * FROM column_tetris.exclusions;
```

### What gets checked

- **CREATE TABLE** statements are validated by the event trigger
- **ALTER TABLE** is deliberately skipped - you can't reorder existing columns, so warning would be noise
- **Temp tables** and **system schemas** (`pg_catalog`, `information_schema`) are skipped
- Tables in the `exclusions` list are skipped

## License

MIT

## 导航

- 项目页：[[10-项目/github.com_3d6503fb]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`开发者工具`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
