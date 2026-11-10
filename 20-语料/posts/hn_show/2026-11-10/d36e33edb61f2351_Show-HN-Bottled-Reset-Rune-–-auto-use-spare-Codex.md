---
type: "corpus"
item_id: "d36e33edb61f2351"
title: "Show HN: Bottled Reset Rune – auto-use spare Codex resets before they expire"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50432720"
project_url: "https://github.com/sufferfml/reset-rune"
author: "morrowf"
published_at: "2026-11-09T21:47:30Z"
captured_at: "2026-11-10T10:01:59+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-11-10"
pub_day: "2026-11-09"
tags:
  - 语料
  - hn_show
  - author_morrowf
  - story_50432720
  - show_hn
metrics: {"points": 2, "comments": 1, "engagement_velocity": 2}
comments_count: 1
comments_total: 1
discovered_via: "hn:show_hn:3d"
---

# Show HN: Bottled Reset Rune – auto-use spare Codex resets before they expire

> [!info] 一句话导读
> sufferfml/reset-rune

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50432720>
> 指标：点赞=2 · 评论=1 · engagement_velocity=2
> 作者：morrowf　|　发布：2026-11-09T21:47:30Z
> 项目链接：<https://github.com/sufferfml/reset-rune>
> 采集：2026-11-10T10:01:59+08:00　|　id：`d36e33edb61f2351`

## 正文

# sufferfml/reset-rune

Turn your Codex resets into bottled runes. Automatically use spare Codex resets before they expire.

- Stars: 0
- Forks: 0
- Watchers: 0
- Open issues: 0
- License: MIT License
- Default branch: main
- Created: 2026-11-05T00:18:08Z

## Languages

- JavaScript
- Python
- Shell
- Swift

## Topics

- codex
- macos
- menubar
- openai
- swift

## Top Contributors

- sufferfml (4 contributions)

---

## README

# Bottled Reset Rune

English · 简体中文

**Turn your Codex resets into bottled runes.**

Bottled Reset Rune is a lightweight, open-source macOS menu bar utility. Each **Reset Rune** represents one spare Codex reset. The app reuses your local Codex login and, once you turn on automatic use, tries to use each rune before it expires.

The name comes from the Regeneration Rune you can store in a Bottle in Dota 2.

## Install

Requires **macOS 13 or later** and the official **Codex CLI 0.153.0**, installed and logged in.

### macOS app

- Download for Apple Silicon
- Download for Intel

Open the DMG, drag Bottled Reset Rune into Applications, then open the app. Both versions are Developer ID signed and Apple notarized.

### npm

Requires Node.js 22 or later.

```sh
npm install -g reset-rune
reset-rune ui
```

Both installation methods open the same native macOS menu bar app.

## Get started

1. Click the bottle in the menu bar and check the displayed Codex account and workspace.
2. Turn on **Automatic use** and confirm authorization.
3. Attempts start **10 minutes** before expiry by default. Choose 5, 10, 30 or 60 minutes in settings.

Automatic use is off by default. Turn it off at any time to pause. Closing the panel or quitting the menu bar interface leaves an enabled background service running.

## Features

- **The bottle** shows how many Reset Runes you have and when the next one expires. Click the bottle to see the rune artwork and inventory details.
- **Lightweight scheduling**: A known earliest expiry is scheduled directly. Empty inventory or incomplete expiry details are checked periodically.
- **Quota and battle log**: Expand the panel to see quota, attempt timing and activity while keeping the main view compact.
- **Language and appearance**: English by default, with Simplified Chinese available. Choose system, light or dark appearance.

## Before you use it

- Your Mac must be running and online, with a valid Codex login. Sleeping or shutting down across an expiry may cause a reset to be missed. The tool does not prevent sleep or force your Mac to wake.
- Codex decides redemption eligibility, so attempts may not always succeed. The tool does not add quota or bypass limits.
- Enable automatic use on only one Mac for the same account.
- Manual refresh only reads state. If your account changes or a redemption result cannot be confirmed, the tool pauses automatic actions and asks you to check.

## Command line

```sh
reset-rune status          # View status
reset-rune refresh         # Refresh status
reset-rune pause           # Pause automatic use
reset-rune config lead 30  # Set a 30-minute lead time
reset-rune --help          # Show all commands
```

Before uninstalling, run `reset-rune uninstall-service` to remove the background service, then delete the app or npm package. Operation records and your Codex login are retained. DMG users can use the CLI inside the app (Chinese).

## Development

Requires Xcode / Swift 6.0+ and Node.js.

```sh
npm ci
npm test
swift test --package-path native
```

See the native module guide for building, packaging and maintenance, and the acceptance records for test coverage (both in Chinese). Use synthetic data and isolated directories for testing; do not use a real account's spare resets.

Windows support is planned and has not been released. See the development plan and technical design (Chinese).

## License

The project code and its custom Reset Rune illustration use the MIT license. Dota 2 artwork, including the Bottle icons adapted for macOS, is excluded from that license. Valve and its licensors retain the rights to it. See the artwork credits and sources. Bottled Reset Rune is an independent project.

## 评论（1/1）

> **morrowf** · 2026-11-09T21:47:41.000Z　
> I kept losing banked Codex resets because they expire instead of auto-activating. I expected Dota 2 bottle/rune behavior: if you do not drink the bottled Regeneration Rune before the timer, it activates itself. Codex just drops them.So I built Bottled Reset Rune, a small open-source macOS menu bar app. Each spare Codex reset is a Reset Rune in the bottle. With Automatic use on, it schedules an attempt shortly before expiry (default 10 minutes; 5/10/30/60 available).Install: notarized DMG for Apple Silicon or Intel from the GitHub release, or npm install -g reset-rune then reset-rune ui. Needs macOS 13+ and Codex CLI logged in. Automatic use is off by default.Caveats worth knowing: your Mac has to be awake and online; Codex still decides whether a redemption succeeds; run Automatic use on only one Mac per account.Happy to talk about scheduling, the pause-on-uncertainty behavior, or packaging.

## 导航

- 项目页：[[10-项目/github.com_fe396b23]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
