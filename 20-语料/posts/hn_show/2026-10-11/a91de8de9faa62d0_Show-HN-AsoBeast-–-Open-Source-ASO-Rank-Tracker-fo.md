---
type: "corpus"
item_id: "a91de8de9faa62d0"
title: "Show HN: AsoBeast – Open-Source ASO Rank Tracker for App Store and Google Play"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50032812"
project_url: "https://github.com/AsoBeast/asobeast"
author: "subisoft77"
published_at: "2026-10-10T13:34:34Z"
captured_at: "2026-10-11T09:43:53+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-10-11"
pub_day: "2026-10-10"
tags:
  - 语料
  - hn_show
  - author_subisoft77
  - story_50032812
  - show_hn
metrics: {"points": 7, "comments": 0, "engagement_velocity": 7}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:3d"
---

# Show HN: AsoBeast – Open-Source ASO Rank Tracker for App Store and Google Play

> [!info] 一句话导读
> Open source, self-hosted App Store Optimization toolkit for the Apple App Store and Google Play.

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50032812>
> 指标：点赞=7 · 评论=0 · engagement_velocity=7
> 作者：subisoft77　|　发布：2026-10-10T13:34:34Z
> 项目链接：<https://github.com/AsoBeast/asobeast>
> 采集：2026-10-11T09:43:53+08:00　|　id：`a91de8de9faa62d0`

## 正文

# AsoBeast/asobeast

Open source, self-hosted App Store Optimization toolkit for the Apple App Store and Google Play.

- Stars: 30
- Forks: 4
- Watchers: 30
- Open issues: 3
- License: GNU Affero General Public License v3.0
- Homepage: https://asobeast.com
- Default branch: main
- Created: 2026-08-24T12:44:40Z

## Languages

- CSS
- Dockerfile
- JavaScript
- PLpgSQL
- Shell
- TypeScript

## Topics

- app-store
- app-store-optimization
- aso
- google-play
- keyword-tracking
- mcp
- nestjs
- nextjs
- self-hosted
- typescript

## Top Contributors

- MrAdex77 (701 contributions)
- claude (13 contributions)
- dependabot[bot] (12 contributions)
- github-actions[bot] (9 contributions)

---

## README

 AsoBeast
 AsoBeast is an App Store Optimization (ASO) tool and keyword rank tracker for the Apple App Store and Google Play.
 Use the hosted service at asobeast.com, or self-host the open source edition on your own server.

 Website ·
 Quickstart ·
 Self-host ·
 MCP server ·
 API ·
 Changelog

## What is AsoBeast?

AsoBeast is an App Store Optimization (ASO) tool and keyword rank tracker for the Apple App Store and Google Play. It imports a listing, tracks keyword rankings daily to a depth of 200, watches competitors, reviews and metadata, and turns that history into a prioritized queue of ASO work. This repository is the free, open source edition that you run on your own server, and the hosted service at asobeast.com runs the same code.

Every store request runs on the machine hosting AsoBeast as an ordinary public search or page request, so Apple and Google see each tracked phrase the way they see any search. There is no ASO vendor to sign up with, no API key to buy, and no ASO vendor that learns which keywords you target. Beyond those store requests, your data stays in your deployment unless you explicitly enable an outbound integration such as webhook alerts, email, OpenAI assistance, Apple Ads search popularity or store status updates.

## Why AsoBeast?

- **No accounts, no vendor API keys.** AsoBeast collects from the public store endpoints at a deliberately modest rate. You need Docker and nothing else.
- **Your keyword list is your strategy.** It lives in your database and is never sent to an ASO vendor, so no competitor intelligence product is quietly assembling it. The stores only ever see one search at a time.
- **Both stores as one tracking entity.** One app row tracks keywords across many storefronts, so `us` and `de` are markets on the same listing rather than two subscriptions.
- **Every score shows its evidence.** Popularity and difficulty carry their source, calculation version, capture date and confidence, so you can argue with a number instead of trusting it.
- **Deterministic recommendations.** Fifteen rules turn stored history into an explainable work queue. AI is optional garnish that can summarize an action, never invent or reorder one.
- **AGPL-3.0, no open core.** Every feature the hosted service runs is in this repository.

## Features

| Feature | What it does |
| -------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Two live stores | Import an Apple App Store or Google Play URL, snapshot the metadata, refresh on demand and diff every field |
| Keyword tracking | Track any validated storefront, see daily positions and history, bulk edit, and keep the private 100 byte iOS keyword field by hand |
| Rank checks to depth 200 | One search per keyword and market serves your app and all of its competitors, so competitor tracking costs no extra requests |
| Transparent scoring | Popularity and difficulty with provenance and confidence, plus opportunity derived on read |
| SERP and category intelligence | Retained SERP snapshots, volatility, entrants and movers, and free, paid and grossing category charts |
| Competitor discovery | Find competitors from live search results, compare listings and find keyword gaps |
| Reviews and change detection | Sync reviews and rating history, mine review language for keyword ideas, and detect owned and competitor metadata changes |
| ASO audit and metadata workbench | A deterministic audit rubric with history, store metadata lints and strategic keyword buckets |
| ASO Action Center | Fifteen deterministic rules produce recommendations with a priority, an estimated impact, the evidence behind them, a deep link, a full lifecycle and a verified outcome |
| Portfolio analysis | Group linked listings across stores and countries, compare group visibility and generate weekly digests |
| Alerts | Signed webhooks or SMTP email for rank, SERP, metadata, review and new action events, with resumable batched delivery |
| MCP server | 27 read tools, plus 5 opt-in tools that change keywords, competitors and actions, over stdio or a remote endpoint, so Claude Code and Claude Desktop can work with your instance directly |

A guide for each of these lives in the documentation.

## Quick start

### One-click deploy

Deploy on Railway

Runs the published images on Railway with PostgreSQL and Redis, and generates every secret for you. See deploy on Railway.

### Docker Compose

You need Docker with Compose, roughly 2 GB of memory and 5 GB of disk.

```bash
git clone https://github.com/AsoBeast/asobeast.git
cd asobeast
printf 'POSTGRES_PASSWORD=%s\nAUTH_SECRET=%s\n' "$(openssl rand -hex 32)" "$(openssl rand -hex 32)" > .env
chmod 600 .env
docker compose up --build -d --wait
```

Open http://localhost:3001 and create the owner account. Registration closes automatically once it exists. Safari does not keep the session cookie over plain HTTP, so use Chrome or Firefox for a local evaluation, or see signing in returns to the sign in form. Import a store URL and keyword tracking starts immediately.

Prefer published images to a build? `docker-compose.pull.yml` runs the same stack from GHCR without a clone:

```bash
curl -fsSLO https://raw.githubusercontent.com/AsoBeast/asobeast/main/docker-compose.pull.yml
printf 'POSTGRES_PASSWORD=%s\nAUTH_SECRET=%s\n' "$(openssl rand -hex 32)" "$(openssl rand -hex 32)" > .env
chmod 600 .env
docker compose -f docker-compose.pull.yml up -d --wait
```

Full walkthrough: quickstart. Image tags, pinning and upgrades: run a published release.

## How AsoBeast compares

| | AsoBeast (self-hosted) | Subscription ASO platforms |
| -------------------------- | --------------------------------- | -------------------------------- |
| Where store requests run | Your machine | Their infrastructure |
| Who sees your keyword list | You | The vendor |
| Cost model | Your hosting bill | Per seat, per app or per keyword |
| Keyword history | Yours, retained on your terms | Ends when the subscription does |
| Score methodology | Published, versioned, inspectable | Usually proprietary |
| Extending it | Fork it, it is AGPL-3.0 | File a feature request |

A hosted AsoBeast is a separate product built from this same repository. Self-hosted installations get every feature.

## Tech stack

pnpm and Turborepo, TypeScript strict throughout, NestJS, Prisma, PostgreSQL 18, BullMQ, Redis 8, Next.js with Tailwind, Docker Compose.

Contributor setup, architecture and the module map: local development and how AsoBeast works.

## Configuration

Every environment variable, with defaults and what each one changes, is documented in the configuration reference. `apps/api/.env.example` and `apps/web/.env.example` are the authoritative lists in the repository.

A default installation needs two variables, `POSTGRES_PASSWORD` and `AUTH_SECRET`. Everything else has a working default.

## FAQ

### What is App Store Optimization?

App Store Optimization is the practice of improving how an app ranks and converts in App Store and Google Play search. It covers keyword targeting in indexed metadata fields, competitor positioning, ratings and reviews, and category performance.

### Does AsoBeast need an App Store Connect or Google Play Console account?

No. AsoBeast reads public store data, so you can track any app including your competitors. It never asks for store credentials or an ASO vendor API key.

### Which app stores does AsoBeast support?

Both the Apple App Store and Google Play. Apple indexes a title, a subtitle and a private 100 byte keyword field. Google Play indexes a title, an 80 character short description and a long description, so subtitle and keyword field stay Apple only concepts. See stores.

### How often does it check rankings?

Once a day by default, on a UTC cron you control. Rank checks capture position to a depth of 200, and a position of `null` means checked and not found within that depth rather than zero. See positions.

### Can I track more than one country?

Yes. An app is imported once, and keyword tracking carries its own storefront, so one listing can track keywords in many markets at once. Each added market multiplies daily store requests, and the settings page shows a budget card that estimates the fan-out. See countries and markets.

### Is any of my data sent anywhere?

Only the store requests themselves, which send each tracked phrase to the App Store or Google Play as an ordinary search, from your own address or through a proxy provider if you configure one. Beyond those, webhook alerts, SMTP email, OpenAI assistance, Apple Ads search popularity and the store status poll are the only outbound integrations, and each is off until configured. There is no telemetry. See what leaves your deployment.

### Can I connect AsoBeast to Claude or another AI agent?

Yes. AsoBeast ships a Model Context Protocol server with 27 read tools, available as a local stdio process or as a remote endpoint on your instance. Every connection needs a personal API token and reads by default. Five more tools that change keywords, competitors and actions are listed only to a token you give the write scope. See MCP.

### Is AsoBeast really free?

The software is, entirely. It is AGPL-3.0 with no open core and no feature held back for a commercial edition, so a self-hosted installation has everything. A hosted service built from this same repository is charged for the hosting it uses, never for features. If you run a modified version as a network service, the AGPL asks you to offer that modified source to its users.

## Documentation

| Topic | Link |
| --------------------------------------- | ---------------------------------------------------------------------------- |
| Quickstart and first import | docs.asobeast.com/quickstart |
| Self-hosting with Docker Compose | install/docker-compose |
| Configuration reference | configuration/reference |
| Concepts: scoring, positions, countries | concepts |
| Guides: keywords, competitors, alerts | guides |
| Operations: backups, restore, upgrades | operations |
| API reference and OpenAPI | api-reference |
| MCP tools | mcp/tools |

## Limitations

Worth knowing before you rely on it:

- **Scores are store-specific estimates.** Popularity and difficulty come from different public evidence on each store, so the numbers are not comparable across stores and are not a substitute for first-party acquisition data.
- **Scrapers can break.** AsoBeast reads public endpoints. When a store changes one, a parser can fail. Failures fail the job, which BullMQ retries with backoff, and never take down request handling.
- **Store rate limits bind first, not hardware.** The public endpoints tolerate only modest request rates per address, which is what caps how many keyword markets one instance can track. See capacity and limits.
- **Operations are yours.** Backups, TLS, secret rotation, monitoring and upgrades are the operator's responsibility. Verify a restore before you rely on a backup.

## Roadmap

The `1.x` line is current, and the changelog names the latest release. What remains open:

- A per-user permission model finer than owner and member, and one account in several workspaces.
- Better popularity calibration using licensed or first-party acquisition data.
- Per-market reviews, category ranks and ratings history. Listings and their screenshot captions are already captured and switched per market.
- More MCP write tools behind the same opt-in, one reversible change at a time.

Release policy and the `1.x` compatibility promise: upgrade and roll back.

## Contributing

Pull requests are welcome. Read CONTRIBUTING.md first for the commit conventions, the compatibility promise and how the test suites are run. Security reports go through SECURITY.md, never a public issue.

## License

This repository's source code is available under the AGPL-3.0 license.

# aindeev/agent-chrome-relay

## 关联链接

- http://localhost:3001
- https://asobeast.com
- https://github.com/AsoBeast/asobeast.git
- https://raw.githubusercontent.com/AsoBeast/asobeast/main/docker-compose.pull.yml

## 导航

- 项目页：[[10-项目/github.com_e5318f73]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
