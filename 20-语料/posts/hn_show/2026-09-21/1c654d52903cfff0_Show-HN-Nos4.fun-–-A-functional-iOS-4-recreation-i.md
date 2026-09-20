---
type: "corpus"
item_id: "1c654d52903cfff0"
title: "Show HN: Nos4.fun – A functional iOS 4 recreation in the browser"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49509167"
project_url: "https://github.com/1etu/nos4"
author: "1etu"
published_at: "2026-08-31T12:55:37Z"
captured_at: "2026-09-21T03:11:22+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-21"
pub_day: "2026-08-31"
tags:
  - 语料
  - hn_show
  - author_1etu
  - story_49509167
  - show_hn
metrics: {"points": 2, "comments": 0, "engagement_velocity": 2}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:52d"
---

# Show HN: Nos4.fun – A functional iOS 4 recreation in the browser

> [!info] 一句话导读
> A complete iOS 4 recreation on the Web

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49509167>
> 指标：点赞=2 · 评论=0 · engagement_velocity=2
> 作者：1etu　|　发布：2026-08-31T12:55:37Z
> 项目链接：<https://github.com/1etu/nos4>
> 采集：2026-09-21T03:11:22+08:00　|　id：`1c654d52903cfff0`

## 正文

# 1etu/nos4

A complete iOS 4 recreation on the Web

- Stars: 1
- Forks: 0
- Watchers: 1
- Open issues: 0
- Homepage: https://nos4.fun
- Default branch: main
- Created: 2026-08-30T18:52:19Z

## Languages

- CSS
- HTML
- JavaScript
- TypeScript

## Topics

- clone
- experiment
- fun
- ios
- ios-web
- ios-web-recreation
- ios4
- recreation

## Top Contributors

- 1etu (20 contributions)

---

## README

# nOS4

**Everything you remember. Right in your browser.**

TypeScript
SolidJS
Vite
Tailwind
pnpm

**nos4.fun**

Introducing nOS4

nOS4 is a recreation of iOS 4, running in the browser.

## Why

Software used to have weight. Buttons felt like you actually press on them. Switches looked like you could
flick them. A list sat on linen, a note sat on legal paper, and a reflection under the dock
told you where the glass was. Every pixel was doing a job.

That craft is worth preserving, and the best way to understand something is to rebuild it. So that's how nos4 born.

## What's inside

Home, multitasking, and folders

Twenty-three apps — Safari, Mail, Messages, Phone, Maps, iPod, Photos, Camera, Notes,
Weather, Stocks, Clock, Calculator, Compass, Voice Memos, Contacts, Settings, App Store,
iTunes, Game Center and two games.

Underneath sit sixteen frameworks:

| | |
|---|---|
| Foundation | the notification bus and primitives |
| CoreGraphics | asset manifest |
| CoreAnimation | timing curves and transitions |
| GraphicsServices | touch delivery and the scroller state machine |
| UIKit / TextInput | controls and the keyboard |
| SpringBoard | lock screen, pages, dock, folders, multitasking |
| SpriteKit / GameKit | the game runtime and leaderboards |
| AVFoundation, CoreLocation, CoreTelephony, SceneKit, … | the rest |

Nothing imports upward. `Foundation` → `CoreGraphics` → `UIKit` → `SpringBoard` → apps.

## The apps

Safari

Mail

Phone

Maps

iTunes

App Store

Game Center

Weather

Clock

Settings

Doom

## 2010s Rich

2010s Rich

## Build

You need Node 22.6+ and pnpm 10+.

```sh
git clone https://github.com/1etu/nos4.git
cd nos4
pnpm install
```

Then run the phone:

```sh
pnpm -C apps/Phone dev
```

| Command | What it does |
|---|---|
| `pnpm -C apps/Phone dev` | the phone, on its own |
| `pnpm dev` | the debug page: event monitor beside the phone |
| `pnpm build` | production bundle into `apps/Phone/dist` |
| `pnpm typecheck` | the whole workspace, `strict` |
| `pnpm banner` | regenerate the marketing images above |

Game Center is the one part that needs a server. It is optional and everything else do work
without it. To run it, put a Postgres connection string in a root `.env`:

```sh
DATABASE_URL=postgresql://…
```

Apply `services/GameCenterService/schema/*.sql` in order, then `pnpm service`.

## Credits

**The OldOS Project** by
**Zane (@zzanehip)** — Its asset catalogue is
where nOS4's artwork comes from, nOS4 shares no code with it and every screen here was rewritten from scratch. Without it there would be nothing to measure.

Maps are drawn with OpenStreetMap tiles, geocoded
by Nominatim and routed by OSRM.
Weather comes from Open-Meteo. The App Store and iTunes read
Apple's public iTunes Search and RSS feeds. Type is set in
Inter and Helvetica Neue.

iPhone, iOS and the app designs recreated here are trademarks of Apple Inc. This is an
independent tribute, not affiliated with or endorsed by Apple.

# Show HN: Decispher – persistent engineering context and memory for coding agents | Hacker News

## 关联链接

- https://github.com/1etu/nos4.git
- https://nos4.fun

## 导航

- 项目页：[[10-项目/github.com_40b1d17a]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
