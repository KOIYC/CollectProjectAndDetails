---
type: "corpus"
item_id: "6e5b5974f269d728"
title: "Show HN: Dribble – an open-source AI IDE for databases"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=48727039"
project_url: "https://github.com/azhakhan/dribble"
author: "ayazhan"
published_at: "2026-06-30T00:16:39Z"
captured_at: "2026-09-21T03:11:00+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-21"
pub_day: "2026-06-30"
tags:
  - 语料
  - hn_show
  - author_ayazhan
  - story_48727039
  - show_hn
metrics: {"points": 5, "comments": 0, "engagement_velocity": 5}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:113d"
---

# Show HN: Dribble – an open-source AI IDE for databases

> [!info] 一句话导读
> AI-powered, open source IDE for Databases

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=48727039>
> 指标：点赞=5 · 评论=0 · engagement_velocity=5
> 作者：ayazhan　|　发布：2026-06-30T00:16:39Z
> 项目链接：<https://github.com/azhakhan/dribble>
> 采集：2026-09-21T03:11:00+08:00　|　id：`6e5b5974f269d728`

## 正文

# azhakhan/dribble

AI-powered, open source IDE for Databases

- Stars: 17
- Forks: 0
- Watchers: 17
- Open issues: 0
- License: MIT License
- Homepage: https://dribblesql.com
- Default branch: main
- Created: 2025-05-19T16:32:33Z

## Languages

- CSS
- JavaScript
- TypeScript

## Topics

- ai
- assistant
- database
- mysql
- postger
- redshift
- snowflake
- sql

## Top Contributors

- azhakhan (47 contributions)

---

## README

# Dribble

**An AI-powered, open-source SQL IDE for your databases.**

Dribble

Dribble is a web-based SQL IDE with a built-in AI data analyst. Connect to a
Postgres database, browse its schema, run queries in a notebook, explore tables
with sort/filter/pagination, and ask an AI agent questions about your data — all
in one tabbed workspace that remembers where you left off.

---

## Features

- **AI data analyst** — chat with an agent (Claude Opus 4.8) that inspects your
 schema, writes and runs read-only SQL, iterates on errors, and renders the
 final result set as a table.
- **SQL notebooks** — write and execute queries in a Monaco editor with syntax
 highlighting. Run with `Cmd/Ctrl + Enter`. Notebooks and their results are
 saved.
- **Schema browser** — navigate schemas and tables from a collapsible sidebar
 tree.
- **Table explorer** — browse table data with server-side pagination, column
 sorting, and a raw `WHERE`-clause filter.
- **Fast results grid** — large result sets render in a virtualized data grid.
- **Persistent workspace** — open tabs, layout/panel sizes, the expanded tree,
 and cached query/chat results survive reloads (and follow you across browsers,
 since state is stored server-side).
- **Smart connection lifecycle** — database drivers are kept warm while in use
 and idle out when not, with the sidebar reflecting live connection status.
- **Flexible auth** — runs with no login at all for local use, or behind Google
 sign-in (with an email/domain allowlist) for multi-user deployments, where each
 person's connections, notebooks, and chats are private. Stored database
 credentials are encrypted at rest. See
 docs/authentication.md.
- **Pluggable drivers** — Postgres ships today; the driver registry is built to
 add more engines (MySQL, Snowflake, …).

## Tech stack

Next.js 16 · React 19 · TypeScript · Tailwind CSS 4 · Monaco Editor ·
glide-data-grid · Zustand · Vercel AI SDK (`@ai-sdk/anthropic`) · Postgres (`pg`)

## Getting started

### Prerequisites

- Node.js 20+
- A Postgres database for storing app metadata (connections, notebooks, chat
 history). Any Postgres works — local, Neon, Supabase, Vercel Postgres, etc.
- An Anthropic API key for the AI agent.

### Install

```bash
git clone <your-repo-url> dribble
cd dribble
npm install
```

### Configure

Copy the example env file and fill in the values:

```bash
cp .env.example .env.local
```

```bash
# Metadata storage (connections, notebooks, chat history).
# Any Postgres works — Vercel Postgres / Neon / Supabase / local.
DATABASE_URL=postgres://user:pass@host:5432/dribble

# Secret used to encrypt stored DB credentials (and sign the auth session).
# Required. Generate with: openssl rand -hex 32
APP_SECRET=

# Powers the AI chat agent (claude-opus-4-8).
ANTHROPIC_API_KEY=
```

That's all you need to run locally — with no auth configured, the app starts
**without a login screen** and all data belongs to a single built-in user.

The required metadata tables are created automatically on first run.

#### Optional: Google sign-in (multi-user)

To require login and keep each user's data private, configure Google OAuth — see
docs/authentication.md for the full setup. In short,
add to `.env.local`:

```bash
AUTH_GOOGLE_ID=
AUTH_GOOGLE_SECRET=
# Restrict who may sign in (leave empty to allow any Google account):
AUTH_ALLOWED_EMAILS=you@example.com
AUTH_ALLOWED_DOMAIN=example.com
```

Register ` /api/auth/callback/google` as an authorized redirect URI on the
Google OAuth client. Setting these enables the login screen automatically.

### Run

```bash
npm run dev
```

Open http://localhost:3000 (you're in directly when no
auth is configured; otherwise sign in with Google), add a database connection,
and start querying.

To build and run a production server:

```bash
npm run build
npm start
```

## A note on AI-generated code

This project was written largely with the help of AI coding tools (Claude Code).
All code has been reviewed before being committed, but you should review it
yourself before relying on it in production.

## License

Released under the MIT License.

# Djomoa | محرك التقويم التاريخي

## 关联链接

- http://localhost:3000
- https://dribblesql.com

## 导航

- 项目页：[[10-项目/github.com_e67d6792]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
