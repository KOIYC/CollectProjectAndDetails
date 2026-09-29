---
type: "corpus"
item_id: "0e31ed07be5805d0"
title: "Show HN: iCli – Postgres health reporter and index optimizer"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49882674"
project_url: "https://github.com/abhiraj-ku/iCli"
author: "abhirajabhi312"
published_at: "2026-09-28T18:51:27Z"
captured_at: "2026-09-29T09:42:55+08:00"
lang: "en"
kind: "post"
topic: "开发者工具"
shard: "2026-09-29"
pub_day: "2026-09-28"
tags:
  - 语料
  - hn_show
  - author_abhirajabhi312
  - story_49882674
  - show_hn
metrics: {"points": 2, "comments": 0, "engagement_velocity": 2}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:3d"
---

# Show HN: iCli – Postgres health reporter and index optimizer

> [!info] 一句话导读
> Suggest the indexing strategy for your database

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49882674>
> 指标：点赞=2 · 评论=0 · engagement_velocity=2
> 作者：abhirajabhi312　|　发布：2026-09-28T18:51:27Z
> 项目链接：<https://github.com/abhiraj-ku/iCli>
> 采集：2026-09-29T09:42:55+08:00　|　id：`0e31ed07be5805d0`

## 正文

# abhiraj-ku/iCli

Suggest the indexing strategy for your database

- Stars: 1
- Forks: 0
- Watchers: 1
- Open issues: 0
- License: MIT License
- Default branch: main
- Created: 2026-09-18T17:03:45Z

## Languages

- Go

## Topics

- cli
- cli-tool
- golang
- golang-application
- golang-cli
- postgres
- postgresql

## Top Contributors

- abhiraj-ku (33 contributions)

---

## README

# iCli - PostgreSQL query and index advisor

`iCli` is a Go CLI that reads PostgreSQL query statistics, explains the most expensive queries, identifies execution-plan bottlenecks, detects missing foreign key indexes, and reports unused indexes.

> [!NOTE]
> 🔒 **Read-Only Guarantee**: `iCli` only executes read-only SQL queries (`SELECT` metadata and `EXPLAIN` plan analysis). It never mutates, inserts, or deletes any data in your database.

## Demo

iCli example output

## Features

- **Expensive Query Analysis**: Identifies slow and resource-heavy queries using `pg_stat_statements`.
- **Execution Plan Profiling**: Runs `EXPLAIN (FORMAT JSON)` and detects plan bottlenecks (e.g., sequential scans, disk sort spillage, inefficient joins).
- **Missing Foreign Key Index Detection**: Finds foreign key constraints on child tables without a covering index, preventing severe sequential scan table locks on parent `UPDATE` or `DELETE` operations.
- **Unused Index Scanner**: Identifies non-primary, non-unique indexes with zero recorded scans that degrade `INSERT`/`UPDATE` performance.
- **Database Health Reports**: Displays real-time database connection metrics, cache hit ratios, and server metadata via `icli report`.
- **Modern Terminal UI**: Formats findings into container cards, severity badges, rounded tables, and ready-to-run SQL remediation snippets powered by Lipgloss.

## Requirements

- Go 1.25 or later.
- PostgreSQL with `pg_stat_statements` enabled.

Enable the extension at the server level, then restart PostgreSQL:

```sql
ALTER SYSTEM SET shared_preload_libraries = 'pg_stat_statements';
```

After restarting PostgreSQL, enable it in the target database:

```sql
CREATE EXTENSION IF NOT EXISTS pg_stat_statements;
```

On a Homebrew PostgreSQL installation, restart with:

```bash
brew services restart postgresql@18
```

## Quick Start

### Install via `go install`

If you have Go installed, you can install `icli` directly:

```bash
go install github.com/abhiraj-ku/pg_adv/cmd/icli@latest
```

### Run Locally / From Source

Clone the repository and run the CLI with a PostgreSQL connection string.

DSN resolution order:

1. `-d` / `--dsn`
2. `PGDSN` environment variable

Examples:

```bash
git clone https://github.com/abhiraj-ku/iCli.git
cd iCli
export PGDSN="postgres://postgres@localhost:5432/postgres?sslmode=disable"

# Display interactive CLI commands menu & guide
go run ./cmd/icli

# Analyze top slow queries & execution plans
go run ./cmd/icli analyze -n 5

# Scan for unused indexes and missing foreign key indexes
go run ./cmd/icli index
go run ./cmd/icli index unused
go run ./cmd/icli index missing-fk

# Generate an instant database health summary report
go run ./cmd/icli report
```

Or pass the DSN explicitly:

```bash
go run ./cmd/icli analyze -d="postgres://postgres@localhost:5432/postgres?sslmode=disable"
```

The long-form flag is also supported:

```bash
go run ./cmd/icli analyze --dsn="postgres://postgres@localhost:5432/postgres?sslmode=disable"
```

Build a binary with:

```bash
go build -o icli ./cmd/icli
export PGDSN="postgres://postgres@localhost:5432/postgres?sslmode=disable"
./icli analyze
```

## Developer Setup

### Prerequisites

- Go 1.25 or later
- PostgreSQL instance running locally or remotely
- `pg_stat_statements` enabled in the target database
- A valid DSN available through either `-d/--dsn` or `PGDSN`

### Local database setup

Create a local PostgreSQL database and enable the extension:

```sql
CREATE EXTENSION IF NOT EXISTS pg_stat_statements;
```

Then export the connection string for local development:

```bash
export PGDSN="postgres://postgres@localhost:5432/postgres?sslmode=disable"
```

### Repo layout

- `cmd/icli` — CLI entrypoint and subcommand routing (`analyze`, `index`, `report`, `update`)
- `internals/analyzer` — execution-plan issue detection rules
- `internals/db` — PostgreSQL queries (`pg_stat_statements`, unused indexes, missing foreign key indexes)
- `internals/health` — database health stats collection (cache hit ratio, active connections)
- `internals/report` — modern Lipgloss terminal TUI rendering

### Common dev commands

```bash
go test ./...
go run ./cmd/icli
go run ./cmd/icli report
GOFLAGS=-mod=mod go run ./cmd/icli
```

### Troubleshooting

- If you see `connection refused`, confirm PostgreSQL is running and the host/port are correct.
- If the slow query report is empty, ensure `pg_stat_statements` is enabled and queries have been executed.
- If the DSN is missing, pass `-d` / `--dsn` or export `PGDSN`.
- If formatting looks odd in a narrow terminal, run it in a wider terminal or resize the window.

## Releases

Prebuilt releases are available for these platforms on the GitHub Releases page:

| Platform | Architecture | Archive name pattern |
| --- | --- | --- |
| Linux | x86_64 | `icli_Linux_x86_64.tar.gz` |
| macOS (Apple Silicon, M-series) | ARM 64-bit | `icli_Darwin_arm64.tar.gz` |

Download the archive for your platform from the Releases page, extract it, and run `icli`:

```bash
tar -xzf icli_Darwin_arm64.tar.gz
./icli -dsn="postgres://user:password@localhost:5432/database?sslmode=disable"
```

Windows and Intel macOS binaries are not included in releases.

## How It Works

1. Reads the PostgreSQL server version to select the correct execution-time column (`total_time` vs `total_exec_time`).
2. Queries `pg_stat_statements` and excludes `iCli`'s internal telemetry queries.
3. Sanitizes parameter placeholders before requesting an `EXPLAIN (FORMAT JSON)` plan.
4. Walks execution plans and reports bottlenecks like sequential scans, disk sort spillage, and inefficient nested loops.
5. Queries `pg_stat_user_indexes` and `pg_index` to find non-primary, non-unique indexes with 0 recorded scans.
6. Inspects `pg_constraint`, `pg_attribute`, and `pg_index` to detect unindexed foreign keys on child tables.

# ankurCES/Mahout

## 关联链接

- https://github.com/abhiraj-ku/iCli.git

## 导航

- 项目页：[[10-项目/github.com_251c8e32]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`开发者工具`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
