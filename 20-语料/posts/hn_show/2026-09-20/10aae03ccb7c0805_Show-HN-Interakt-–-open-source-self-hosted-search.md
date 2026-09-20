---
type: "corpus"
item_id: "10aae03ccb7c0805"
title: "Show HN: Interakt – open-source self-hosted search and AI chat for your website"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49732963"
project_url: "https://github.com/alphasolutionsrepo/interakt"
author: "interakt"
published_at: "2026-09-16T21:01:06Z"
captured_at: "2026-09-20T14:03:45+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-20"
pub_day: "2026-09-16"
tags:
  - 语料
  - hn_show
  - author_interakt
  - story_49732963
  - show_hn
metrics: {"points": 2, "comments": 1, "engagement_velocity": 2}
comments_count: 1
comments_total: 1
discovered_via: "hn:show_hn:90d"
---

# Show HN: Interakt – open-source self-hosted search and AI chat for your website

> [!info] 一句话导读
> alphasolutionsrepo/interakt

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49732963>
> 指标：点赞=2 · 评论=1 · engagement_velocity=2
> 作者：interakt　|　发布：2026-09-16T21:01:06Z
> 项目链接：<https://github.com/alphasolutionsrepo/interakt>
> 采集：2026-09-20T14:03:45+08:00　|　id：`10aae03ccb7c0805`

## 正文

# alphasolutionsrepo/interakt

- Stars: 8
- Forks: 1
- Watchers: 8
- Open issues: 2
- License: MIT License
- Homepage: https://interakt.app
- Default branch: main
- Created: 2026-06-01T20:51:42Z

## Languages

- CSS
- Dockerfile
- JavaScript
- Shell
- TypeScript

## Top Contributors

- naalpha (20 contributions)
- alpharv (4 contributions)
- hjaAlpha (1 contributions)

---

## README

# Interakt — Local Developer Setup

AI-powered search and chat platform. This README gets a new developer running the full stack locally — backend admin/API + demo site — and walks through first-boot configuration.

📖 **Documentation:** docs.interakt.app

## Repo layout

```
interakt/
├── backend/      # Admin dashboard + REST APIs (Next.js, Drizzle, Postgres + Elasticsearch)
│   └── infra/    # docker-compose for local Postgres + Elasticsearch
└── demo-site/    # Example consumer app built against the Interakt APIs (Next.js)
```

Both apps are Next.js. Backend runs on **3000**, demo-site on **3001**.

## Prerequisites

- Node.js 24 LTS (see `.nvmrc`)
- Docker + Docker Compose (for local Postgres + Elasticsearch)

## 1. Backend

```bash
cd backend

# Runtime config — fill in the three openssl-generated secrets at the top of the file
cp .env.example .env

# Admin user — change at least the password
cp setup/setup.config.example.yaml setup/setup.config.yaml

# Install, start local Postgres + Elasticsearch, run dev server
npm install
npm run infra:up
npm run dev
```

Backend is up at **http://localhost:3000**. Log in with the admin email/password from your YAML.

On first `npm run dev` the server automatically:

1. Applies Drizzle migrations to both DBs (main + analytics).
2. Seeds the AI provider catalog and prompt templates.
3. Creates the admin user from `setup/setup.config.yaml`.

### Backend scripts

| Script | What it does |
|---|---|
| `npm run dev` | Start dev server (auto-migrates + auto-seeds + auto-creates admin) |
| `npm run infra:up` | Start local Docker stack (Postgres + Elasticsearch) |
| `npm run infra:down` | Stop containers, keep volumes |
| `npm run infra:reset` | Stop and wipe volumes (fresh DB next boot) |
| `npm run lint` / `lint:fix` / `lint:strict` | Lint |
| `npm run format` | Prettier |
| `npm run type-check` | TypeScript no-emit check |
| `npm run test` / `test:watch` / `test:coverage` | Vitest |

### Bring your own Postgres / Elasticsearch

If you already have services running, skip `npm run infra:up` and point `POSTGRES_URL`, `ANALYTICS_POSTGRES_URL`, and `ELASTICSEARCH_URL` in `.env` at your endpoints. `npm run dev` still handles migrations and seeding.

## 2. Run the initial setup

Sign into http://localhost:3000 with the admin from `setup/setup.config.yaml`, then in the admin UI go to **Platform → Initial Setup** (or open `http://localhost:3000/setup` directly) and:

1. Configure an AI provider (Ollama for local/free, OpenAI for cloud). **Required** — until a provider is configured and set as the system default, the in-app docs and help assistant aren't available (the docs get indexed using the default provider's embedding model).
2. Load the **Fashion Catalog** demo data — gives you sample content plus ready-made Search and AI experiences (with access tokens) for the demo-site.

This is the fastest path to "I see the whole thing working." The wizard creates an index, a data source, the four tools over it, and two pre-configured experiences — enough to point the demo site at and chat with it.

## 3. Read the in-app docs

Once the default provider is set, the docs come online. Spend ten minutes on the **conceptual overview** before deep-clicking around the admin — it explains how indexes, tools, MCP connections, and chat experiences relate to each other, so the screens stop looking like a wall of unrelated settings.

Two ways to get there:

- **Open `http://localhost:3000/docs`** for the full documentation site.
- Or hit the **?** icon at the top-right of any admin screen — it opens a help drawer with the docs page for whatever you're looking at, plus an **Ask** tab backed by Interakt's own AI assistant running over the docs (dogfooding the same pipeline your chat experiences use).

Recommended starting points:

1. What is Interakt — the building-blocks glossary.
2. Architecture — how Interakt fits together — the mental model with illustrations.

## 4. Demo site

A standalone Next.js app that consumes the Interakt APIs as a reference integration. No env file needed.

```bash
cd demo-site
npm install
npm run dev
```

Open **http://localhost:3001**. It defaults to talking to the backend at `http://localhost:3000`.

Each demo route is a separate experience and needs its own access token (issued in the admin UI; loading the Fashion Catalog above is the fastest way to get them):

| Route | Token type |
|---|---|
| `/search-interface`, `/experience/smart-search`, `/experience/guided-search` | Search Experience |
| `/chat` | AI Experience |
| `/dropin-demo` | Search and/or AI Experience |

Open the route, click the gear icon, paste the backend URL and matching token, Save. Settings persist in localStorage, one per route.

## APIs at a glance

- `POST /api/search` — search with filtering, sorting, suggestions
- `POST /api/chat` — AI chat with context awareness
- Admin APIs for templates, providers, indexes, analytics

API keys are issued from the admin UI.

## License

MIT © Alpha Solutions.

# Plexus · Store and monitor your telemetry, beautifully.

## 评论（1/1）

> **Yashjain413** · 2026-09-17T04:59:53.000Z　
> Pretty interesting. I think one thing we’ve been facing recently is the need for AI chat to help users navigate the actual product, not just the website.Customers often know the outcome they want to achieve, but have no idea what steps they need to take to get there. For example, they might want to launch a campaign, but don’t know where to start or what they need to configure.Having something like an AI assistant that understands the product and guides them through every step of the process could be really helpful. It could essentially take the user from the outcome they want to achieve and walk them through the entire workflow.

## 关联链接

- http://localhost:3000
- http://localhost:3000**.
- http://localhost:3000/docs`**
- http://localhost:3000/setup`
- http://localhost:3000`.
- http://localhost:3001**.
- https://interakt.app

## 导航

- 项目页：[[10-项目/github.com_eaa5da1d]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
