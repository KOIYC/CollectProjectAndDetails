---
type: "corpus"
item_id: "8ba116380fd955b4"
title: "Show HN: 49Agents – 2D Canvas IDE for Orchestrating Agents, Repos, Issues"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=47942287"
project_url: "https://github.com/49Agents/49Agents"
author: "alpadurza"
published_at: "2026-04-28T23:34:10Z"
captured_at: "2026-09-21T02:52:42+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-21"
pub_day: "2026-04-28"
tags:
  - 语料
  - hn_show
  - author_alpadurza
  - story_47942287
  - show_hn
metrics: {"points": 21, "comments": 2, "engagement_velocity": 21}
comments_count: 2
comments_total: 2
discovered_via: "hn:show_hn:174d"
---

# Show HN: 49Agents – 2D Canvas IDE for Orchestrating Agents, Repos, Issues

> [!info] 一句话导读
> Open-source 2D IDE for managing AI agents in native CLIs, terminal, gits, beads issues, and files across multiple projects and machines. Self-host on a single m…

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=47942287>
> 指标：点赞=21 · 评论=2 · engagement_velocity=21
> 作者：alpadurza　|　发布：2026-04-28T23:34:10Z
> 项目链接：<https://github.com/49Agents/49Agents>
> 采集：2026-09-21T02:52:42+08:00　|　id：`8ba116380fd955b4`

## 正文

# alpbahadur/49Agents

Open-source 2D IDE for managing AI agents in native CLIs, terminal, gits, beads issues, and files across multiple projects and machines. Self-host on a single machine via localhost OR host on a cluster via Tailscale OR connect to app.49agents.com (coming soon)

- Stars: 378
- Forks: 39
- Watchers: 378
- Open issues: 14
- License: Other
- Homepage: https://49agents.com
- Default branch: main
- Created: 2026-02-27T02:28:57Z

## Languages

- CSS
- HTML
- JavaScript
- Shell

## Topics

- claude-code
- cli
- codex
- ide
- terminal-based
- vibecoding

## Top Contributors

- MYRADhub (197 contributions)
- alpbahadur (31 contributions)
- claude (3 contributions)
- Jalil-g (1 contributions)
- qaraalp (1 contributions)

---

## README

 49 Agents IDE

 The first 2D agentic IDE. Open source.

 All agents. All terminals. All projects. All machines. One unified space.

 Before

 49

---

| Before | 49 |
|--------|--------------|
| 14 terminal tabs | One zoomable canvas |
| SSH into each machine | All machines, zero SSH |
| Alt-tab to check Claude | Claude status on every pane |
| Can't work from phone | Any device, anywhere |
| Terminal-only, no files | Monaco editor on the canvas |
| 🤷 | Git graph |
| 🤷 | Interactive issue tables (Beads) |
| 🤷 | Permission notifications |
| 🤷 | Markdown notes |

---

## Quick Start

```bash
git clone https://github.com/49Agents/49Agents.git
cd 49Agents
./49ctl setup    # interactive setup (one time)
./49ctl start    # start cloud server + agent
```

Open `http://localhost:1071`. No account, no login, no token.

Don't want to self-host? **49agents.com**
tutorial

---

## Desktop App (macOS)

Download the latest `.dmg` from GitHub Releases.

After downloading, macOS will block the app because it is not notarized. Run this once to allow it:

```bash
xattr -cr /Applications/49Agents.app
```

Then open 49Agents normally. It runs as a tray icon — look for it in your menu bar.

Updates are delivered in-app: click the tray icon and choose **Check for Updates**.

---

## Features

### Canvas and Workspace

- [x] **Infinite canvas** — no tabs, no splits. Place panes anywhere on a zoomable surface
- [x] **Drag, resize, arrange** — your workspace grows with your thinking, not your monitor
- [x] **Zoom levels** — zoom out for the big picture, zoom in to focus
- [x] **Persistent layout** — everything stays where you put it

### Terminals

- [x] **Real tmux sessions** via ttyd — full ANSI color, scrollback, your shell config
- [x] **Broadcast input** — type once, send keystrokes to multiple terminals simultaneously

### Multi-Machine

- [x] **Zero SSH** — connect agents from any machine to one canvas
- [x] **HUD overlay** — live CPU, RAM, and Claude API usage across all connected machines

### Access

- [x] **Any device** — laptop, tablet, phone. Same workspace, same layout
- [x] **Tailscale / LAN / hosted relay** — works however you connect
- [x] **Fully self-hosted** — the entire stack runs on your hardware
- [x] **No data stored server-side** — terminal I/O is relayed, never persisted

### Keyboard-First

- [x] **Tab chords** for pane switching
- [x] **WASD move mode** for spatial navigation
- [x] **Shortcut numbers** (1–9) for instant pane focus
- [x] **Broadcast mode** for multi-terminal input

---

## Architecture

```
┌──────────────┐    WSS    ┌──────────────┐    WSS    ┌──────────────┐
│  🖥️ PC       │ ────────►│  ☁️ Relay    │ ◄──────── │  📱 Browser  │
│  49-agent    │           │              │           │              │
└──────────────┘           └──────────────┘           └──────────────┘
                           Self-host or use
                            49agents.com
```

 Multi-machine setup

```
┌──────────────┐                                         ┌──────────────┐
│  🖥️ MacBook  │ ─── WSS ───┐                        ┌───│  📱 Phone   │
│  49-agent    │             │                       │   │  Browser     │
└──────────────┘             │                       │   └──────────────┘
                             │   ┌──────────────┐    │
┌──────────────┐             ├──►│  ☁️ Relay    │◄───┤   ┌──────────────┐
│  🖥️ PC       │ ─── WSS ───┤   │              │     ├───│  💻 Laptop  │
│  49-agent    │             │   │  Self-host   │    │   │  Browser     │
└──────────────┘             │   │  or use      │    │   └──────────────┘
                             │   │ 49agents.com │    │
┌──────────────┐             │   └──────────────┘    │    ┌──────────────┐
│  ☁️ Azure VM │ ─── WSS ───┘                        └───│  📱 Tablet   │
│  49-agent    │                                          │  Browser     │
└──────────────┘                                          └──────────────┘

                  Each agent independently connects
                   to the relay via WebSocket.
                  No terminal data stored server-side.
```

---

## License

BSL 1.1 — free for individuals and small teams. Converts to MIT on 2030-02-26.

# mgranados/screenshotter

## 评论（2/2）

> **2001zhaozhao** · 2026-04-29T07:00:11.000Z　
> I'm building an agent wrapper with an in-browser windowing user interface, and this is surprisingly close to what I have in mind from a UX perspective.Similarities:- Lots of UX focus with the details like keyboard shortcuts. Other gui projects straight-up forget this, and the CLI agents include it only out of necessity. I think this is the way to go because no matter how much can be automated in today's world, having the lowest-friction UX is still king in making the parts that need to be manual go as fast as possible.- The idea of a windowing system in the browser. I think we both think that agentic development is complex enough to warrant a multi-window environment being optimal.- Focus on being accessible from any device, although i don't have the persistent layout thing quite as developed as your approach.- Our monetization approach is similar (monetize hosted version). you're monetizing through hosting the remote while i want to monetize through hosting 24/7 dev machinesDifferences:- My windowing approach is a bit more safe (just focused on making a really good remote desktop) while you seem to have a more adventurous idea with the 2D zoomable canvas- I think your choice of Beads issue tracking is really interesting for context management. I don't have an equivalent in my project.- You're running agents on a dev's laptop and enabling remote access through a relay layer, whereas i'm designing my tool's backend to run directly on 24/7 dev servers.- You're using cli agents directly (like cmux) while i'm wrapping them in a GUI with ACP (like Zed)- You have monaco editor built in while I'm planning to integrate code-server- From your canvas approach i'm assuming you're rendering client side. I'm focused on server-rendered web HTML (liveview-like), mostly chosen for reasons for supporting a plugin system where plugins are server-side-only but can alter the UI. my approach probably sends more data through the wire but drains less battery than yoursOverall a bit of nice validation and food for thought. I think we have really different backend approaches but the UX portion converges nonetheless. Thanks for sharing!By the way, in the GitHub repo description, your 49agents website still says coming soon, you should probably update that.Also, the Discord invite on your website doesn't work

---

> **alpadurza** · 2026-04-29T11:53:02.000Z　
> hey zhaozhao, thanks for sharing! i will check the website... dont have much time to work on landing page lately haha

## 关联链接

- http://localhost:1071`.
- https://49agents.com
- https://github.com/49Agents/49Agents.git

## 导航

- 项目页：[[10-项目/github.com_e21b72e6]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
