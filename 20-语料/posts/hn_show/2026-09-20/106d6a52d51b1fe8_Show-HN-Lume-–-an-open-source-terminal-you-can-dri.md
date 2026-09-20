---
type: "corpus"
item_id: "106d6a52d51b1fe8"
title: "Show HN: Lume – an open-source terminal you can drive from your phone"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49712433"
project_url: "https://uselume.dev/"
author: "hugomyb"
published_at: "2026-09-15T13:43:06Z"
captured_at: "2026-09-20T09:37:16+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-20"
pub_day: "2026-09-15"
tags:
  - 语料
  - hn_show
  - author_hugomyb
  - story_49712433
  - show_hn
metrics: {"points": 2, "comments": 0, "engagement_velocity": 2}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:90d"
---

# Show HN: Lume – an open-source terminal you can drive from your phone

> [!info] 一句话导读
> Lume — open-source terminal: command blocks, AI, remote control

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49712433>
> 指标：点赞=2 · 评论=0 · engagement_velocity=2
> 作者：hugomyb　|　发布：2026-09-15T13:43:06Z
> 项目链接：<https://uselume.dev/>
> 采集：2026-09-20T09:37:16+08:00　|　id：`106d6a52d51b1fe8`

## 正文

Lume — open-source terminal: command blocks, AI, remote control

 $ open source · local-first · no telemetry NEW what's new →

# Your terminal, wherever you go.

 An open-source terminal with command blocks, inline AI and split panes — plus a QR code that turns your phone into the same session. No account, no telemetry.

Rust Tauri 2 SolidJS xterm.js not Electron not a fork

BLOCKS 0

## The terminal you left running is in your pocket.

Every other terminal stops at the edge of your desk. Scan the code, and the same live session is in your hand — same panes, same scrollback, same shell.

on your network

Termux-style key row, live directory completion, swipe-to-move-cursor and a tab bar. Same Wi-Fi by default.

or from anywhere

A cloudflared tunnel you start and stop yourself. Nothing stays open behind your back.

while you're away

Kick off a migration or a CLI agent, walk away, get the notification, check it from the sofa.

 # how the pairing, the tunnel and the token actually work → Control your terminal from your phone

## Everything a terminal should be.

A terminal emulator with blocks, panes and palettes — powerful where it counts, invisible where it shouldn't get in the way.

~/lume $ lume --features

 [01]

### Command blocks

Each command and its output is an isolated block. Jump between them, copy, re-run — no scrolling through a wall of text.

### Inline AI

Explain a block, or turn plain English into a command. Bring your own Claude, Codex, OpenAI or Ollama — keys stay local.

### Panes & tabs

Split, tab, rearrange by drag-and-drop. Panes, sizes and working directories survive a restart.

### Autocomplete

Inline suggestions from your history, the files around you, your aliases and your `PATH`.

### File tree sidebar

Follows the active pane's directory instead of fighting it. Right-click actions are yours to define.

### SSH palette

Your `~/.ssh/config` hosts, one fuzzy search away. A few letters, enter, connected.

### Workflows

The commands you can never remember, saved as snippets with named arguments — recalled from the palette, not from a stale gist.

 [08]

### Themes, fonts & 14 languages

9 themes, custom fonts, Nerd Font support, remappable keys — and a UI translated into 14 languages, not just English.

### Local & self-updating

Everything runs on your machine — no account, no telemetry — with signature-verified auto-updates.

## Warp is open-source now. So why not just fork it?

Fair question. Lume is the alternative that isn't a fork — and that changes three things.

~/lume $ git log --oneline | tail -1 › initial commit — from nothing

 [01]

### A fork inherits the weight

 Forking gets you the features and the mass that came with them. Lume started from nothing, so there was never anything to strip out — 3.3 to 8.2 MB, depending on your OS.

### A fork inherits the licence

 Lume is MIT. Fork it, rebrand it, sell it, ship it across your company — no conversation with legal. Copyleft forks stay copyleft; MIT hands the choice back to you.

 [03]

### A fork inherits upstream

 Every fork spends its life rebasing onto someone else's roadmap. Lume answers to nobody — which is how a feature like phone control gets built at all.

3.3 MB WINDOWS .EXE 5.0 MB.DEB / .RPM 8.2 MB MACOS .DMG MIT LICENCE

 # sizes measured on the v1.1.2 artefacts. Lume shares no code with Warp and is not affiliated with it. Want Warp's exact feature set? Use Warp — this is a smaller bet.

## See it in action.

Real screenshots of the app, not mockups.

### An assistant in your prompt, not in charge of it.

Ask what a block did, or describe what you want and get the command — inserted, never auto-run. A deliberate choice: you keep the last keystroke.

### Lay it out the way you think.

A CLI agent in one pane, your dev server in another — and the whole layout comes back exactly as you left it tomorrow.

### Configurable to the last detail.

Appearance, shell, AI providers, shortcuts, language — one panel. Export and import the whole config as JSON.

## Questions, answered.

? Warp is open-source now — why use Lume?+

Because a fork inherits everything: the codebase, the licence, and the job of chasing upstream forever. Lume shares no code with Warp — it's an independent open-source terminal, and it does one thing no Warp build does: it follows you to your phone.

? Is Lume a fork of Warp?+

No. Written from scratch in Rust with Tauri 2, SolidJS and xterm.js — no shared code, no lineage, no trademark. The block-based workflow is a convention, not a codebase.

? How does remote control work?+

Lume serves a small page from your own machine; scan a QR code to drive a pane from your phone. Across networks, it opens a cloudflared tunnel that you start and stop.

? Does Lume send my data anywhere?+

No. No account, no telemetry, no cloud. AI is off until you configure it, and your API keys stay local — they're even excluded from config export.

? Which AI providers can I use?+

Claude and Codex through their local CLIs, or OpenAI, DeepSeek, Ollama and any OpenAI-compatible endpoint with your own key. Opt-in, picked in Settings.

? Why MIT and not AGPL?+

So you can actually use it: fork Lume, rebrand it, ship it in a commercial product, with no conversation with legal. Copyleft licences stay copyleft — MIT leaves the choice to you.

? Why are the macOS & Windows builds unsigned?+

Certificates cost money, so early releases ship unsigned — a one-time prompt to bypass. Each release has a signature file and the source is public, so you can verify or rebuild.

? What is Lume built with?+

Rust + Tauri 2 + SolidJS + xterm.js. A native binary: 3.3 MB on Windows, 5 MB on Debian, 8.2 MB on macOS. Not Electron.

## Get Lume.

Free, MIT, no sign-up form between you and a working terminal.

~ $ lume install › detecting os…

### macOS

Universal — Intel & Apple Silicon · 8.2 MB

Unsigned for now: on first launch, right-click → Open.

### Windows

Windows 10 & 11 (x64) · 3.3 MB

↓ .exe

SmartScreen may warn: More info → Run anyway.

### Linux

AppImage · .deb · .rpm · AUR · 5 MB

 `curl -fsSL https://uselume.dev/install.sh | bash` copy all downloads

# prefer a package manager? `yay -S lume-bin` on Arch. Every release auto-updates in-app.

# Better AI Answers From Sources You Trust | Bulkgrid

## 关联链接

- https://uselume.dev/install.sh

## 导航

- 项目页：[[10-项目/uselume.dev_71e61eff]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
