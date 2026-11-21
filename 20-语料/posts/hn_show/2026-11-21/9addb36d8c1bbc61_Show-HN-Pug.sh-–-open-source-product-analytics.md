---
type: "corpus"
item_id: "9addb36d8c1bbc61"
title: "Show HN: Pug.sh – open-source product analytics"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50576620"
project_url: "https://github.com/pug-sh/pug"
author: "BajajScooter"
published_at: "2026-11-20T15:54:56Z"
captured_at: "2026-11-21T14:45:01+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-11-21"
pub_day: "2026-11-20"
tags:
  - 语料
  - hn_show
  - author_BajajScooter
  - story_50576620
  - show_hn
metrics: {"points": 5, "comments": 0, "engagement_velocity": 5}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:3d"
---

# Show HN: Pug.sh – open-source product analytics

> [!info] 一句话导读
> Open-source product analytics

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50576620>
> 指标：点赞=5 · 评论=0 · engagement_velocity=5
> 作者：BajajScooter　|　发布：2026-11-20T15:54:56Z
> 项目链接：<https://github.com/pug-sh/pug>
> 采集：2026-11-21T14:45:01+08:00　|　id：`9addb36d8c1bbc61`

## 正文

# pug-sh/pug

Open-source product analytics

- Stars: 72
- Forks: 8
- Watchers: 72
- Open issues: 2
- License: Other
- Homepage: https://pug.sh
- Default branch: main
- Created: 2026-06-04T13:10:04Z

## Languages

- Dockerfile
- Go
- Makefile
- PLpgSQL
- templ

## Topics

- ai
- analytics
- assistant
- clickhouse
- connectrpc
- dpdp
- flutter
- flutter-analytics
- gdpr
- google-analytics
- mcp
- mixpanel
- nats
- posthog
- productanalytics
- self-hosted
- selfhosted
- web-analytics
- webanalytics

## Top Contributors

- poluruprvn (1098 contributions)
- nullorm (560 contributions)
- dependabot[bot] (51 contributions)
- boramuyar (5 contributions)

---

## README

# Pug

CI
codecov
Discord

Pug is an open-source product analytics platform. Capture events, identify the
people behind them, and explore behavior through funnels, retention, trends,
segmentation, and user-flow analysis — all surfaced on customizable dashboards.

Built in Go on PostgreSQL, ClickHouse, and NATS.

## Features

- **Event ingestion** — a NATS-backed capture pipeline with automatic geo,
 user-agent, bot-detection, and web-attribution enrichment.
- **Web analytics** — an overview auto-built from your events: visitors,
 sessions, pageviews, bounce rate, and traffic sources, with no tile to wire up.
- **Live view** — every visitor on a real-time world map, down to the person and
 the event they just fired.
- **Profiles** — identify and alias the users behind events, with a
 ClickHouse-backed profile and activity API.
- **Insights** — trends, funnels, retention, segmentation, user flow (Sankey),
 and top-K breakdowns, with filtering, breakdowns, and period-over-period
 comparison.
- **Dashboards** — compose insight and markdown tiles on a grid with a
 board-level time window, accelerated by a pre-aggregated rollup fast path.
- **Privacy & compliance** — GDPR/DPDP data-subject erasure of a person's
 events and profile.

 Overview — a web-analytics view auto-built from your events, with the previous period alongside.

 Breakdowns — pageviews by country, plus locations, devices, and events; click any value to filter the whole view.

 Live view — every visitor on a live world map; click one to fly to them and see the page, device, and profile behind it.

 Dashboards — compose insight and markdown tiles on a time-windowed grid.

 Insights — trends, filters, and breakdowns; here product views split by country.

 Profiles — the person behind the events, with traits, sessions, and activity.

## Tech stack

- **Go** — backend services and workers, exposed over Connect RPC (HTTP/2)
- **PostgreSQL** — relational store (orgs, projects, dashboards, auth)
- **ClickHouse** — analytical store for events, insights, and profiles
- **NATS** — messaging backbone for the ingestion and worker pipelines

## Quick start

```bash
# Build the binary -> bin/pug
make build

# Start dev infrastructure (PostgreSQL, NATS, ClickHouse)
make infra

# Run migrations
./bin/pug postgres migrate
./bin/pug nats migrate
./bin/pug clickhouse migrate

# Seed the demo project with events, profiles, and dashboards
# (resets the local Postgres and ClickHouse databases — see "Demo data" below)
./bin/pug seed

# Start the dev server + workers together
./bin/pug dev
```

Environment variables are documented in `.env.example`.
Google and generic OIDC sign-in are documented in
`docs/authentication.md`, with a ready-to-copy
`config.example.json`.

### Demo data

`./bin/pug seed` fills a "Pug & Pals" demo project with ~4 months of history, so
dashboards, insights, and profiles have something to show. Profiles are seeded
only for users that produced events, so the data is internally consistent.

> **Local databases only.** By default `seed` migrates Postgres and ClickHouse
> all the way down and back up, dropping every table — not just the demo rows.
> There is no confirmation prompt and no environment check: it connects to
> whatever `DATABASE_URL` and `CLICKHOUSE_URL` resolve to, and an already
> exported variable beats `.env`. Point it at a disposable local or demo
> database.

Pass `--no-reset` to keep the schema; it then deletes the demo project's own
events and profiles before re-seeding them, leaving other projects untouched.
Volume is tunable with `--count` (default 500,000 events) and `--batch` (default
10,000 events per insert). Run it from the repo root; it reads the same `.env`
as the rest of the CLI.

Two accounts are seeded:

- `woof@pug.sh` — org admin, password `goodboy`
- `snoop@pug.sh` — read-only viewer, no password; open `/demo` with
 `PUG_DEMO_ENABLED=true` to sign in as it

For a live stream of traffic instead of a one-shot backfill, set
`PUG_DEMO_ENABLED=true`: `./bin/pug dev` then also runs the demo worker. It
backfills an **empty** project once, so after `pug seed` it skips straight to
playing new sessions out in real time. If you seed with a smaller `--count`,
lower `PUG_DEMO_SEED_COUNT` to match — the worker reads a project holding fewer
events than that as an interrupted backfill and warns rather than topping it up.

## Development

```bash
make test    # run tests (race detector enabled)
make cover   # run tests and write coverage.out
make lint    # lint Go code
make sqlc    # regenerate sqlc queries after editing SQL
make rpc     # regenerate protobuf code after editing .proto files
make templ   # regenerate templ email templates
```

## Architecture

Per-subsystem documentation lives in `docs/architecture/`
(insights, ClickHouse, profiles, ingestion, email, telemetry). Contributor
guidance and conventions are in `CLAUDE.md`.

## License

Pug is licensed under the GNU AGPL v3.0. Contributors sign a
CLA before their first pull request is merged — see
CONTRIBUTING.md.

Error fetching https://spa-mvc-pages.duckdns.org/wordmap/: CRAWL_EMPTY_CONTENT

## 关联链接

- https://pug.sh
- https://spa-mvc-pages.duckdns.org/wordmap/:

## 导航

- 项目页：[[10-项目/github.com_815749f6]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
