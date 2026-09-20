---
type: "corpus"
item_id: "716ef100c8987147"
title: "Show HN: Podiom – durable sessions, scheduling and goals for local Claude/Codex"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49498323"
project_url: "https://github.com/Podiom/Podiom"
author: "Maphielbso"
published_at: "2026-08-30T13:08:34Z"
captured_at: "2026-09-21T03:11:31+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-21"
pub_day: "2026-08-30"
tags:
  - 语料
  - hn_show
  - author_Maphielbso
  - story_49498323
  - show_hn
metrics: {"points": 3, "comments": 0, "engagement_velocity": 3}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:52d"
---

# Show HN: Podiom – durable sessions, scheduling and goals for local Claude/Codex

> [!info] 一句话导读
> Thin orchestration layer for local LLM agents. Durable sessions, profiles, scheduling, and native MCP/tool/skill integration.

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49498323>
> 指标：点赞=3 · 评论=0 · engagement_velocity=3
> 作者：Maphielbso　|　发布：2026-08-30T13:08:34Z
> 项目链接：<https://github.com/Podiom/Podiom>
> 采集：2026-09-21T03:11:31+08:00　|　id：`716ef100c8987147`

## 正文

# Podiom/Podiom

Thin orchestration layer for local LLM agents. Durable sessions, profiles, scheduling, and native MCP/tool/skill integration.

- Stars: 2
- Forks: 4
- Watchers: 2
- Open issues: 5
- License: MIT License
- Homepage: https://github.com/Podiom/Podiom/tree/master/docs
- Default branch: master
- Created: 2026-06-29T12:22:41Z

## Languages

- CSS
- Dockerfile
- Go
- HTML
- JavaScript
- Makefile
- PowerShell
- Shell
- Svelte
- TypeScript

## Topics

- agent-orchestration
- ai-agents
- anthropic
- automation
- claude
- claude-code
- cli
- codex
- developer-tools
- go
- golang
- llm
- llm-orchestration
- local-first
- mcp
- multi-agent
- productivity
- self-hosted
- svelte
- workflow-automation

## Top Contributors

- mar-schmidt (179 contributions)
- Copilot (5 contributions)
- lntutor (2 contributions)
- dependabot[bot] (2 contributions)
- kushin25 (1 contributions)

---

## README

# Podiom

A thin orchestration layer for local LLM agents (Claude Code and OpenAI Codex).
Podiom shells out to the native `claude` and `codex` CLIs and leans on *their*
MCP, tools, and skills, while owning its own durable truth: named agents, durable
chat sessions, a canonical history that replays onto a fresh backing CLI session
on any profile/provider switch, an embedded scheduler, and a shared project
ledger. It ships as a single Go binary with an embedded Svelte web UI.

## Why Podiom?

Managing multiple local agents is easy to start and hard to keep coherent. Podiom
stays thin on purpose:

- Durable sessions that survive provider and profile changes.
- A shared project ledger so work does not get lost between runs.
- Built-in scheduling for recurring work and follow-ups.
- Native integration with the tools you already use instead of replacing them.

## See it in action

Podiom demo: create a session, send a message, and receive a response

## Screenshots

| Agent roster | Chat session | Goal timeline |
| --- | --- | --- |
| Podiom agent roster showing named Claude and Codex agents | Podiom chat session with durable history and session usage | Podiom goal timeline showing metrics and recorded activity |

## Who is this for?

- Developers already using Claude Code or OpenAI Codex locally.
- Open-source builders who want persistent, reviewable agent work.
- Operators and tinkerers who prefer local-first workflows over cloud lock-in.
- Maintainers who need a lightweight control plane around existing agent tools.

## Quick start (dev)

### Install

macOS/Linux:

```sh
curl -fsSL https://github.com/Podiom/Podiom/releases/latest/download/install.sh | bash
```

Windows PowerShell:

```powershell
irm https://github.com/Podiom/Podiom/releases/latest/download/install.ps1 | iex
```

The installer downloads the matching release binary, verifies checksums, can set
up user-level autostart, and launches `podiom onboard` to check Claude/Codex and
create your first agent.

Every commit to `master` publishes a GitHub Release using the automatic
`v0.1. ` series. That series is intentionally monotonic rather than
calendar-based, so bursts of work can produce many releases without implying a
monthly cadence.

After install, updates can be checked and applied from the CLI or web UI:

```sh
podiom update check
podiom update apply --yes
```

Linux releases are distro-neutral static binaries.

### Development

Prerequisites: Go 1.26+, Node 20+ (for building the web UI).

```sh
# Build the web UI (vite) and both binaries into bin/ with a version stamp.
make build

# Run the daemon (foreground). It scaffolds ~/.podiom on first run.
./bin/podiomd

# In another shell, check it's live.
./bin/podiom status
```

Open http://127.0.0.1:8787 for the web UI.

To develop the frontend with hot reload, run `npm run dev` in `web/` (it proxies
API/WebSocket traffic to a running `podiomd`).

### Cross-platform builds & packaging

`podiomd` is a single static binary with the SPA embedded — no external assets,
no cgo (pure-Go SQLite via `modernc.org/sqlite`), so it cross-compiles cleanly:

```sh
make cross    # linux/darwin/windows × amd64/arm64 → bin/<os>-<arch>/
make package  # archives release artifacts into dist/ and writes SHA256SUMS
```

All runtime state lives under one overridable root, so running Podiom as a Home
Assistant add-on or in a container is a packaging step, not a rewrite:

```sh
PODIOM_HOME=/data/podiom ./bin/podiomd   # relative values are anchored absolute
```

The web bind is configurable in `config.yaml` (`server.bind` / `server.port`,
default `127.0.0.1:8787`); see Configuration.

## Layout

```
cmd/podiom/     thin CLI client
cmd/podiomd/    daemon: web server + scheduler + core
internal/       core, adapter, exec, schedule, config, store, server, client
web/            Svelte + Vite + TS + Tailwind SPA (built → embedded)
docs/           requirements, CLI reference, configuration, integration contracts
```

All runtime state lives under `$PODIOM_HOME` (default `~/.podiom/`).

## Documentation

- Requirements — the authoritative spec (v1.6).
- CLI reference
- Configuration
- Agents — durable, named colleagues and their stored defaults
- Git — how projects carry source control
- Sessions — the durable conversation unit
- SOUL.md generation — how agent identity files are generated
- Scheduling
- Projects & Roadmap
- Goals — hand an outcome to an agent; it plans, reviews, and reports back
- Workspace tools — approved per-agent CLI installs
- Voice input — speak prompts in chat, tasks, and goals (OpenAI Whisper)
- Photo attachments — attach retained photos for Claude or Codex to inspect
- Security & logging — permission modes, gateway token, redaction, run logs
- Home Assistant app — deploy Podiom as an HA add-on
- Integration contracts

## Contributing

Podiom is open source under the MIT License. Contributions are
welcome; please read CONTRIBUTING.md for setup, validation,
and pull request guidelines.

# GitHub - ArcadeMakerSources/ArcadeMaker: A cross-platform 2D game engine with its own programming language and IDE. · GitHub

## 关联链接

- http://127.0.0.1:8787
- https://github.com/Podiom/Podiom/releases/latest/download/install.ps1
- https://github.com/Podiom/Podiom/releases/latest/download/install.sh
- https://github.com/Podiom/Podiom/tree/master/docs

## 导航

- 项目页：[[10-项目/github.com_903a5bb9]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
