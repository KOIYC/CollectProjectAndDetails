---
type: "corpus"
item_id: "710db077aa0f21a7"
title: "Show HN: Steam-like experience for DOOM community maps and mods"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=48346050"
project_url: "https://github.com/stared/rusted-doom-launcher"
author: "stared"
published_at: "2026-05-31T14:42:48Z"
captured_at: "2026-09-21T02:52:44+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-21"
pub_day: "2026-05-31"
tags:
  - 语料
  - hn_show
  - author_stared
  - story_48346050
  - show_hn
metrics: {"points": 3, "comments": 0, "engagement_velocity": 3}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:144d"
---

# Show HN: Steam-like experience for DOOM community maps and mods

> [!info] 一句话导读
> stared/rusted-doom-launcher

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=48346050>
> 指标：点赞=3 · 评论=0 · engagement_velocity=3
> 作者：stared　|　发布：2026-05-31T14:42:48Z
> 项目链接：<https://github.com/stared/rusted-doom-launcher>
> 采集：2026-09-21T02:52:44+08:00　|　id：`710db077aa0f21a7`

## 正文

# stared/rusted-doom-launcher

Steam-like experience for DOOM maps & mods - for GZDoom & UZDoom source ports

- Stars: 16
- Forks: 3
- Watchers: 16
- Open issues: 3
- License: MIT License
- Default branch: main
- Created: 2025-11-29T11:41:42Z

## Languages

- CSS
- HTML
- JavaScript
- Python
- Rust
- TypeScript
- Vue

## Topics

- doom
- doom2
- wad
- wads

## Top Contributors

- stared (236 contributions)
- jmarucha (7 contributions)
- magnetProgramming (6 contributions)

---

## README

# Rusted Doom Launcher

A modern open-source launcher for classic Doom WADs and mods.
Browse community-made maps and episodes, then install and launch them with a single click - essentially bringing the Steam experience to Doom.

## Features

- **Browse the catalog:** Search by mood, type, and difficulty
- **Cacowards included:** Yearly awards for the best Doom maps, megawads, and mods
- **One-click play:** Download and launch with a modern source port (GZDoom or UZDoom)
- **Stack gameplay mods:** Run mods on top of any base game or WAD
- **Bring your own:** Drop in a WAD you already have
- **Track your runs:** Per-level stats and session history
- **Plays the classics:** Doom, Doom II, Final Doom, Heretic, Hexen, Freedoom
- **Auto-extracts game files:** Pulls IWADs directly from GOG installers
- **Cross-system:** macOS (Apple Silicon and Intel), Windows, Linux (dev)

If you want or need other features, open a feature request describing what you would like to see, or even better - open a pull request.

I am also open to expanding the maps, megawads and mod library - if you want to add your favorite WAD (or your WAD!), feel free to open a PR.

## Motivation

The scene is alive and well - see newest releases at Doomworld.
I got inspired by gameplays shared at Doom & Retro FPS Mods Facebook group.

I built it for myself, so I can run it on my Apple Silicon Macbook - but sharing it so others may enjoy it as well.
While there are similar apps, notably Doom Launcher, they are either Windows-only or lack features I wanted.

## Requirements

- GZDoom - Doom source port
 - works also with the newer UZDoom
- `doom.wad` and `doom2.wad` - Doom game data from GOG.com or Steam
 - The app can extract IWADs directly from GOG installers using innoextract (`brew install innoextract`)

## Install

### macOS

The easiest way is to use Homebrew via my tap stared/doom.

```bash
brew install --cask stared/doom/rusted-doom-launcher
```

Alternatively, download a binary from releases. Since it is unsigned open-source software, you must remove the quarantine attribute before running (otherwise macOS will report it as damaged):

```bash
xattr -cr /Applications/Rusted\ Doom\ Launcher.app
```

You also need a Doom engine. Install it manually or via Homebrew:

```bash
brew install --cask gzdoom
# or newer:
brew install --cask stared/doom/uzdoom
```

### Windows

See Windows binary in releases.

### Linux

No pre-built binary yet. You can run it from source — see Building from source below.

### First run

When you open the app for the first time, it will prompt you to locate your Doom engine (GZDoom/UZDoom) and your base game WADs (`doom.wad` / `doom2.wad`). If you have GOG offline installers, the app can extract the game files for you automatically (requires `innoextract`).

## Building from source

To build from source, you need pnpm and Rust.

Install dependencies and run:

```bash
pnpm install
pnpm tauri dev
```

Build for production:

```bash
pnpm tauri build
```

### AI-Assisted Debugging (MCP)

The app includes tauri-plugin-mcp-bridge for AI debugging via Claude Code.

```bash
# Install MCP server for Claude Code
npx -y install-mcp @hypothesi/tauri-mcp-server --client claude-code
```

With the app running (`pnpm tauri dev`), Claude Code can take screenshots, click elements, execute JS, and inspect the DOM.

## Tech

- Tauri 2 (it's in Rust, hence the project name)
- Vue 3 in TypeScript
- Python scripts for some processing
- Claude Code and Gemini for vibe coding

## Author

Piotr Migdał and contributors

## License

MIT

# AIGCEra/Creator

## 导航

- 项目页：[[10-项目/github.com_6b41cf8e]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
