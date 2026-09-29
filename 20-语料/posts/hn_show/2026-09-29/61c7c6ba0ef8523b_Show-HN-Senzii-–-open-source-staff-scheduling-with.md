---
type: "corpus"
item_id: "61c7c6ba0ef8523b"
title: "Show HN: Senzii – open-source staff scheduling with a native MCP interface"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49878382"
project_url: "https://github.com/Senzii-App/app"
author: "cochsenreither"
published_at: "2026-09-28T14:17:42Z"
captured_at: "2026-09-29T09:42:55+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-29"
pub_day: "2026-09-28"
tags:
  - 语料
  - hn_show
  - author_cochsenreither
  - story_49878382
  - show_hn
metrics: {"points": 2, "comments": 0, "engagement_velocity": 2}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:3d"
---

# Show HN: Senzii – open-source staff scheduling with a native MCP interface

> [!info] 一句话导读
> The Senzii Scheduling Web App and MCP Server

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49878382>
> 指标：点赞=2 · 评论=0 · engagement_velocity=2
> 作者：cochsenreither　|　发布：2026-09-28T14:17:42Z
> 项目链接：<https://github.com/Senzii-App/app>
> 采集：2026-09-29T09:42:55+08:00　|　id：`61c7c6ba0ef8523b`

## 正文

# Senzii-App/app

The Senzii Scheduling Web App and MCP Server

- Stars: 0
- Forks: 0
- Watchers: 0
- Open issues: 0
- License: Apache License 2.0
- Default branch: main
- Created: 2026-08-06T22:52:47Z

## Languages

- CSS
- HCL
- HTML
- JavaScript
- Python
- Shell
- Smarty

## Top Contributors

- ochsec (12 contributions)

---

## README

# Senzii Scheduling App & MCP Server

## Stack

- **Web framework**: FastAPI
- **Database**: asyncpg (PostgreSQL, same schema as Rust)
- **Sessions**: Cookie-based, PostgreSQL-backed (same `sessions` table)
- **Email**: Resend API
- **Geocoding**: Nominatim (OpenStreetMap)
- **MCP Server**: Python MCP SDK

## Quick Start

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env  # fill in DATABASE_URL, SESSION_SECRET, etc.
uvicorn app.main:app --host 0.0.0.0 --port 3000 --reload
```

MCP server:
```bash
python -m mcp_server.main
```

## Architecture

```
app/
  main.py          — FastAPI app, all routers wired
  config.py        — Environment configuration
  db/              — Database layer (asyncpg pool, migrations, queries)
  models/          — Pydantic schemas
  middleware/      — Auth session extraction, rate limiting
  routes/          — FastAPI routers (1:1 with Rust routes)
  services/        — Email (Resend), Geocoding (Nominatim)
mcp_server/       — MCP server (Python MCP SDK)
static/           — App HTML/CSS/JS (login, dashboards, portals, SEO pages)
```

The marketing/landing site is a separate repo (`Senzii-App/site`) served from
Vercel at senzii.com. `app.senzii.com` serves only the app: `GET /` is the
sign-in page.

## License

Open-source. See LICENSE.

# geneva-render/geneva

## 导航

- 项目页：[[10-项目/github.com_3a9faf19]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
