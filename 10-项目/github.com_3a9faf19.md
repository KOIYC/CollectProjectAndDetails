---
type: "project"
title: "Show HN: Senzii – open-source staff scheduling with a native MCP interface"
project_url: "https://github.com/Senzii-App/app"
first_seen: "2026-09-29T09:42:55+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_cochsenreither
  - story_49878382
  - show_hn
lang: "en"
---

# Show HN: Senzii – open-source staff scheduling with a native MCP interface

> [!info] 一句话导读
> The Senzii Scheduling Web App and MCP Server

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://github.com/Senzii-App/app>
> 首次收录：2026-09-29T09:42:55+08:00
> 来源渠道：HN Show HN
> 标签：author_cochsenreither, story_49878382, show_hn
> 最新指标：点赞=2 · 评论=0 · engagement_velocity=2

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-09-29T09:42:55+08:00 | HN Show HN | 点赞=2 · 评论=0 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-09-29/61c7c6ba0ef8523b_Show-HN-Senzii-–-open-source-staff-scheduling-with]] |

## 摘要正文

# Senzii-App/app  The Senzii Scheduling Web App and MCP Server  - Stars: 0 - Forks: 0 - Watchers: 0 - Open issues: 0 - License: Apache License 2.0 - Default branch: main - Created: 2026-08-06T22:52:47Z  ## Languages  - CSS - HCL - HTML - JavaScript - Python - Shell - Smarty  ## Top Contributors  - ochsec (12 contributions)  ---  ## README  # Senzii Scheduling App & MCP Server  ## Stack  - **Web framework**: FastAPI - **Database**: asyncpg (PostgreSQL, same schema as Rust) - **Sessions**: Cookie-based, PostgreSQL-backed (same `sessions` table) - **Email**: Resend API - **Geocoding**: Nominatim (OpenStreetMap) - **MCP Server**: Python MCP SDK  ## Quick Start  ```bash python -m venv .venv && source .venv/bin/activate pip install -r requirements.txt cp .env.example .env  # fill in DATABASE_URL, SESSION_SECRET, etc. uvicorn app.main:app --host 0.0.0.0 --port 3000 --reload ```  MCP server: ```bash python -m mcp_server.main ```  ## Architecture  ``` app/   main.py          — FastAPI app, all routers wired   config.py        — Environment configuration   db/              — Database layer (asyncpg pool, migrations, queries)   models/          — Pydantic schemas   middleware/      — Auth ses…
