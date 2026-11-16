---
type: "corpus"
item_id: "01cc4eebd950d331"
title: "Show HN: Canban – Kanban and Workflow and Herdr Workbench for CLI Agents"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50508535"
project_url: "https://github.com/jjyr/canban"
author: "fwee"
published_at: "2026-11-15T17:06:17Z"
captured_at: "2026-11-16T10:00:05+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-11-16"
pub_day: "2026-11-15"
tags:
  - 语料
  - hn_show
  - author_fwee
  - story_50508535
  - show_hn
metrics: {"points": 5, "comments": 1, "engagement_velocity": 5}
comments_count: 1
comments_total: 1
discovered_via: "hn:show_hn:3d"
---

# Show HN: Canban – Kanban and Workflow and Herdr Workbench for CLI Agents

> [!info] 一句话导读
> Canban = Kanban + herdr workbench

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50508535>
> 指标：点赞=5 · 评论=1 · engagement_velocity=5
> 作者：fwee　|　发布：2026-11-15T17:06:17Z
> 项目链接：<https://github.com/jjyr/canban>
> 采集：2026-11-16T10:00:05+08:00　|　id：`01cc4eebd950d331`

## 正文

# jjyr/canban

Canban = Kanban + herdr workbench

- Stars: 2
- Forks: 0
- Watchers: 2
- Open issues: 0
- License: Apache License 2.0
- Homepage: https://canban.dev
- Default branch: main
- Created: 2026-11-05T16:45:16Z

## Languages

- C
- CSS
- HTML
- JavaScript
- Objective-C
- Python
- Rust
- Shell

## Topics

- canban
- herdr
- kanban
- workflow

## Top Contributors

- jjyr (227 contributions)

---

## README

 Canban

 Focus on Human Context.
 Canban = Kanban + Workflow + Herdr

 English · 简体中文

 Website (canban.dev) ·
 Philosophy ·
 Highlights ·
 Installation ·
 Related Software ·
 License

---

## Philosophy

1. **Kanban organizes human context** — specs, `#Card` references, screenshots, `@Agent` discussions, structured reports, and review gates stay together on each Card.
2. **Herdr drives native Agent CLIs with minimal interference** — run Claude Code, Codex, Antigravity (`agy`), Cursor CLI, or custom CLIs directly inside persistent PTYs with native TUIs, permissions, MCPs, skills, and session resume intact.
3. **Most work stays on Kanban and dispatches via workflows** — shape scope and review diffs on the Board while workflows isolate Git worktrees, dispatch agents, and queue merges automatically.

---

## Highlights

### Kanban for Human

Move Cards across customizable stages (`Backlog → Develop → Review`) with live `@developer`, `@reviewer`, and `@merger` status capsules right on the Board. Each Card combines Markdown specs, pasted screenshots, `#Card` / `#tag` links, `Cmd+O` Quick Open, and GitHub Issue/PR sync with approval gates for external PRs.

### GitHub Actions Style Workflows

Automate column transitions, `@agent` runs, custom scripts, conditions, human approvals, and serialized FIFO **Queue Merge** (`deliver` with automatic `@merger` conflict resolution) inside isolated per-Card Git worktrees — authored visually in Workflow Studio, in YAML, or via **Edit with agent**.

### Herdr Terminal

Press `Cmd+J` on any Card for a side-by-side terminal split or open the dedicated **Terminals** workspace. Built in Rust with `longbridge/nsh` (AppKit/Metal) and `libghostty-vt` over local or remote SSH `herdr-core`, running agent PTYs survive app restarts and upgrades across 17 built-in dark themes.

---

## Installation

**Prerequisites**: macOS 13.0+ (Apple Silicon), `git`, at least one native Agent CLI (`claude`, `codex`, `agy`, `cursor-agent`, etc.), and **Herdr Core (`hc`)** (Canban guides one-click `hc` setup on first launch if missing).

```bash
curl -fsSL https://canban.dev/install.sh | bash
```

Installs or live-upgrades `/Applications/Canban.app` without interrupting active `herdr-core` sessions, and automatically handles macOS Gatekeeper quarantine removal and local ad-hoc code signing.

---

## Related Software and Acknowledgements

Canban builds directly on these open-source projects and assets (full attributions and licenses are preserved in THIRD_PARTY_NOTICES.md):

- **Herdr (`herdr-core`)** — Persistent PTY session supervisor and JSON-RPC runtime powering native Agent CLIs and interactive terminals (Apache-2.0)
- **Sheprd** — Terminal VT/frame/input and subscription utility patterns referenced during integration (Apache-2.0)
- **NSH (`longbridge/nsh`)** — Native macOS AppKit/Metal Rust UI framework (Apache-2.0)
- **Ghostty (`libghostty-vt`)** — Commit-pinned VT parser and terminal emulation engine (MIT)
- **iTerm2-Color-Schemes** (MIT) — 16 classic terminal color palettes including Monokai, Dracula, Nord, Tokyo Night, and Catppuccin Mocha
- **Lucide** (ISC), **Lobe Icons** (MIT), and **Primer Octicons** (MIT) — UI and provider icons

---

## License

Copyright 2026 JJy \.

Licensed under the Apache License, Version 2.0.

# Anthakshari

## 评论（1/1）

> **fwee** · 2026-11-15T17:12:22.000Z　
> Hi HN! I built Canban (https://canban.dev) so I could manage human context on a Kanban board.
> If you've try vibe coding, you know how exhausting switching across terminals gets.My workflow: I discuss the feature with an agent on a card, then I drag the card into develop, the card follows a github-action-like workflow to automatically dispatch agents in a Git worktree and land changes through a local merge queue, with all feature context and progress tracked on the kanban board. Under the hood it pairs `libghostty-vt` with `herdr-core`, so it runs and detects most mainstream agent CLIs.Tech stack:- Rust- longbridge/nsh for macOS UI- libghostty-vt for terminal- herdr-core for agents

## 关联链接

- https://canban.dev
- https://canban.dev/install.sh

## 导航

- 项目页：[[10-项目/github.com_30c8e47b]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
