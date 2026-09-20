---
type: "corpus"
item_id: "ad3f10f4e5da0e4d"
title: "Show HN: PortScout – TUI to find and kill processes occupying your ports"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=47960684"
project_url: "https://github.com/abhaikollara/portscout"
author: "TheThirdTuring"
published_at: "2026-04-30T10:54:55Z"
captured_at: "2026-09-21T02:52:28+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-21"
pub_day: "2026-04-30"
tags:
  - 语料
  - hn_show
  - author_TheThirdTuring
  - story_47960684
  - show_hn
metrics: {"points": 4, "comments": 0, "engagement_velocity": 4}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:174d"
---

# Show HN: PortScout – TUI to find and kill processes occupying your ports

> [!info] 一句话导读
> Published: 2026-04-29

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=47960684>
> 指标：点赞=4 · 评论=0 · engagement_velocity=4
> 作者：TheThirdTuring　|　发布：2026-04-30T10:54:55Z
> 项目链接：<https://github.com/abhaikollara/portscout>
> 采集：2026-09-21T02:52:28+08:00　|　id：`ad3f10f4e5da0e4d`

## 正文

Published: 2026-04-29

# Repository: abhaikollara/portscout

- Stars: 0
- Forks: 0
- Watchers: 0
- Open issues: 0
- Primary language: Go
- Languages: Go (97.9%), Makefile (2.1%)
- License: MIT License (MIT)
- Default branch: main
- Created: 2026-04-29T14:24:44Z
- Last push: 2026-04-30T10:57:42Z
- Contributors: 1 (top: abhaikollara)
- Releases: 2
- Latest release: v0.2.0 (2026-04-29T15:10:19Z)

---

# PortScout

A terminal UI tool for monitoring network connections and managing the processes behind them. Built with [Bubble Tea](https://github.com/charmbracelet/bubbletea).

## Install

### Homebrew (macOS, Apple Silicon)

```
brew tap abhaikollara/tap
brew install portscout
```

### From source

```
go install github.com/abhaikollara/portscout@latest
```

### Manual

```
git clone https://github.com/abhaikollara/portscout.git
cd portscout
make install
```

## Usage

```
portscout            # Launch the interactive TUI
portscout 8080       # Show process details for port 8080
portscout -k 8080    # Kill the process on port 8080
portscout --version  # Print version
```

> **Note:** Some connections require elevated permissions to resolve process names. Run with `sudo` if you see `unknown` processes.

## Keybindings

| Key | Action |
| --- | --- |
| `q` / `Ctrl+C` | Quit |
| `/` | Start filtering by port, process name, protocol, or remote address |
| `Enter` | Filter mode: confirm filter. Normal mode: view process details. Group mode: drill down into process |
| `Esc` | Clear filter / exit filter mode |
| `k` | Kill selected process (with confirmation) |
| `s` | Cycle sort column (Port, Process, PID, Proto, Status, Remote) |
| `S` | Reverse sort direction |
| `f` | Freeze / unfreeze auto-refresh |
| `g` | Toggle group-by-PID view |
| `Up` / `Down` | Navigate rows |

## Features

**Live connection table** -- Shows port, process name, PID, protocol (TCP/UDP), status, and remote address. Auto-refreshes every second.

**Search and filter** -- Press `/` and type to filter by any field. Partial matches work -- typing `node` shows all Node.js connections, typing `8080` shows anything on that port.

**Process detail view** -- Press `Enter` on any row to see full process info: command line, user, CPU/memory usage, file descriptors, working directory, and start time.

**Group by PID** -- Press `g` to collapse connections by process. Shows connection count per process, sorted by most connections. Press `Enter` on a group to drill down into that process's individual connections.

**Kill processes** -- Press `k` on any row, confirm with `y`. Works in both normal and grouped views.

**Sort** -- Press `s` to cycle the sort column, `S` to reverse direction. Active sort column shows a `▲`/`▼` indicator.

**Freeze** -- Press `f` to pause auto-refresh. Useful for inspecting a snapshot without the table updating under you.

## Tech Stack

- [bubbletea](https://github.com/charmbracelet/bubbletea) -- TUI framework
- [lipgloss](https://github.com/charmbracelet/lipgloss) -- Styling
- [bubbles](https://github.com/charmbracelet/bubbles) -- Table component
- [gopsutil](https://github.com/shirou/gopsutil) -- Cross-platform process and network data

## Built with Claude

This project was built entirely using [Claude Code](https://claude.ai/code).

## License

MIT

# sslboard/throwaway

## 关联链接

- https://claude.ai/code
- https://github.com/abhaikollara/portscout.git
- https://github.com/charmbracelet/bubbles
- https://github.com/charmbracelet/bubbletea
- https://github.com/charmbracelet/lipgloss
- https://github.com/shirou/gopsutil

## 导航

- 项目页：[[10-项目/github.com_6f8332e2]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
