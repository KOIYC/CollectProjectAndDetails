---
type: "corpus"
item_id: "7c69b72054a6fec5"
title: "Show HN: A medieval world where growth and citizens are pure functions of time"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50416538"
project_url: "https://github.com/retrogames23/samenland"
author: "doener"
published_at: "2026-11-08T19:56:25Z"
captured_at: "2026-11-09T09:39:29+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-11-09"
pub_day: "2026-11-08"
tags:
  - 语料
  - hn_show
  - author_doener
  - story_50416538
  - show_hn
metrics: {"points": 2, "comments": 0, "engagement_velocity": 2}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:3d"
---

# Show HN: A medieval world where growth and citizens are pure functions of time

> [!info] 一句话导读
> retrogames23/samenland

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50416538>
> 指标：点赞=2 · 评论=0 · engagement_velocity=2
> 作者：doener　|　发布：2026-11-08T19:56:25Z
> 项目链接：<https://github.com/retrogames23/samenland>
> 采集：2026-11-09T09:39:29+08:00　|　id：`7c69b72054a6fec5`

## 正文

# retrogames23/samenland

A cozy, historically grounded real-time medieval settlement simulation set in Northern Germany around 1500. Pure deterministic growth, isometric 2:1 canvas engine.

- Stars: 0
- Forks: 0
- Watchers: 0
- Open issues: 0
- License: Other
- Homepage: https://samenland.app/
- Default branch: main
- Created: 2026-11-06T20:42:12Z

## Languages

- CSS
- JavaScript
- PLpgSQL
- TypeScript

## Top Contributors

- lovable-dev[bot] (2776 contributions)

---

## README

# Samenland

**A slow, cozy, shared settlement game set in Northern Germany around 1500.**

Plant a single seed somewhere on a large shared map — and watch a hamlet grow, in real time, into a village, a market town and eventually a Hanseatic city. Your town keeps growing whether you are watching or not. Every now and then you step in: you decide on trade roads, answer visitors, commission buildings and walk through the streets as the village mayor (*Schulze*).

Live: **https://samenland.app**

## Features

- **Real-time, deterministic growth** – towns are a pure function of their seed position and founding time, so every player sees exactly the same town, even offline.
- **Shared multiplayer maps** – four regional realms, each with its own clock; neighbouring towns connect by trade roads and slowly grow together.
- **Living villagers** – every resident has a home, a craft, a daily routine, Sundays, weddings, illness and feasts, all derived from the shared clock.
- **Historical setting** – Northern Germany c. 1500: church feasts, three-field rotation, guilds, the prince's court, fires, floods and raids.
- **Day, night, seasons and weather** – real sunrise/sunset times per realm, seasonal art and atmospheric weather.
- **Isometric painted look** – 2:1 isometric canvas renderer with sprites, night window layers and depth-sorted occlusion.
- **Eight languages** – German, English, French, Spanish, Arabic (RTL), Hindi, Simplified Chinese and Japanese.

## Tech stack

- TanStack Start (React 19, SSR, server functions) on Vite 7
- TypeScript, Tailwind CSS v4
- HTML5 Canvas renderer (no game engine)
- Supabase-compatible backend (Postgres, auth, realtime) via Lovable Cloud
- Vitest for tests

## Getting started

Requirements: Node.js 20+ (or Bun).

```sh
git clone <this-repository-url>
cd samenland
npm install        # or: bun install
npm run dev        # starts the dev server on http://localhost:8080
npm test           # runs the test suite
```

The app expects backend credentials in `.env` (`VITE_SUPABASE_URL`, `VITE_SUPABASE_PUBLISHABLE_KEY`, `VITE_SUPABASE_PROJECT_ID`). Database migrations live in `supabase/migrations/`.

## Project structure

```text
src/
  game/         simulation, economy, villagers, seasons, weather and the canvas renderer
    lang/       game texts and translation catalogs
  components/   React UI (HUD, windows, overlays)
  routes/       TanStack routes and server endpoints
  assets/       sprites, music and sound
supabase/       database migrations and configuration
```

Design rules for each area are documented in the `AGENTS.md` files throughout the repository — please read them before changing game logic. The key principle: **game state is derived, not stored.** Growth, villagers, goods and events are computed from seeds and the shared clock; the database stores only player decisions.

## Contributing

Contributions are welcome — see CONTRIBUTING.md.

## License

Samenland — the source code **and all assets** (sprites, illustrations, music, sounds, texts) — is released under the MIT License.

Built with Lovable.

# README.md

## 关联链接

- http://localhost:8080
- https://samenland.app**
- https://samenland.app/

## 导航

- 项目页：[[10-项目/github.com_ba9b45a0]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
