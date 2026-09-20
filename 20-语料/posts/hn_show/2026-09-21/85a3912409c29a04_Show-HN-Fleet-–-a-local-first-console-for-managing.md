---
type: "corpus"
item_id: "85a3912409c29a04"
title: "Show HN: Fleet – a local-first console for managing Dockerized Hermes AI Agents"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=48724767"
project_url: "https://github.com/matt454/agent-fleet-console"
author: "matt454"
published_at: "2026-06-29T20:31:10Z"
captured_at: "2026-09-21T03:11:03+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-21"
pub_day: "2026-06-29"
tags:
  - 语料
  - hn_show
  - author_matt454
  - story_48724767
  - show_hn
metrics: {"points": 8, "comments": 0, "engagement_velocity": 8}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:113d"
---

# Show HN: Fleet – a local-first console for managing Dockerized Hermes AI Agents

> [!info] 一句话导读
> matt454/agent-fleet-console

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=48724767>
> 指标：点赞=8 · 评论=0 · engagement_velocity=8
> 作者：matt454　|　发布：2026-06-29T20:31:10Z
> 项目链接：<https://github.com/matt454/agent-fleet-console>
> 采集：2026-09-21T03:11:03+08:00　|　id：`85a3912409c29a04`

## 正文

# matt454/agent-fleet-console

- Stars: 7
- Forks: 0
- Watchers: 7
- Open issues: 0
- License: MIT License
- Default branch: main
- Created: 2026-06-04T15:25:19Z

## Languages

- CSS
- Dockerfile
- HTML
- JavaScript
- Python
- Shell
- TypeScript

## Top Contributors

- matt454 (7 contributions)

---

## README

Fleet readme banner

# Fleet

Fleet is a local-first web console for creating, configuring, monitoring, and operating Dockerized Hermes agents across one or more trusted machines.

It is primarily built for Hermes Agent and the NVIDIA-focused Hermes variant, Nemo Hermes. Standard Hermes agents are the default path; Nemo Hermes agents are supported when the `nemohermes` runner is available or automatic installation is enabled.

It gives a single operator view for the parts that become noisy once you run more than one agent: service health, provider defaults, shared credentials, chat sessions, browser sidecars, VNC, terminal access, local web publishing, backups, restores, clones, remote nodes, and setup readiness.

Fleet is designed for technical operators running personal or team-controlled agent infrastructure on a workstation, homelab, VPN, or trusted LAN. Runtime state and secrets stay local by default; the repository keeps source code separate from `.env`, `runtime/`, `data/`, `logs/`, `secrets/`, and `vendor/hermes-agent/`.

## Screenshots

Fleet dashboard showing agents grouped by host with health and update status

Agent gateway modal showing terminal access

## What Fleet Does

- Creates Hermes Docker agents from a repeatable local baseline.
- Creates Nemo Hermes sandbox agents when the `nemohermes` runner is available or auto-install is enabled.
- Coordinates local agents and trusted remote Fleet nodes from the same dashboard.
- Shows agent state, service counts, health, memory readiness, gateway diagnostics, drift, and update status.
- Opens agent chat, session history, dashboard, VNC, local web preview, and container terminal surfaces.
- Saves fleet-wide provider defaults for OpenAI Codex, Ollama, Custom endpoints, and OpenRouter.
- Stores shared provider credentials in ignored local files and syncs them into selected agents.
- Supports Codex device login and controlled sync of Codex auth state into agents.
- Creates Telegram-enabled agents through the onboarding pairing flow.
- Publishes static files from each agent workspace through a per-agent webhost sidecar.
- Backs up, restores, and clones agents while excluding secrets unless an operator explicitly opts in.
- Runs release and setup audits that keep runtime state, tokens, logs, and oversized source files out of git.

## Requirements

- Node.js 20+ and npm 10+
- Docker with Docker Compose v2
- git, when Fleet should clone the default Hermes source checkout automatically
- Optional: `nemohermes` on `PATH` for Nemo Hermes sandbox agents

The onboarding screen checks these requirements. From a terminal, run the same check with:

```bash
npm run init:baseline
```

## Quickstart

```bash
npm run setup
npm start
```

Open:

```text
http://127.0.0.1:5180
```

`npm run setup` prepares ignored runtime folders, creates `.env` when missing, fixes executable bits on wrapper scripts, installs npm dependencies when needed, clones the configured Hermes source when it is missing, and runs the baseline check. New env files bind the console to `0.0.0.0` so trusted LAN machines can reach it, and setup prompts for or generates `HERMES_CONSOLE_TOKEN` because LAN-visible consoles must use API auth.

`npm start` runs the baseline check, builds the frontend, and serves the production app from the Express server.

From the console host itself, open `http://127.0.0.1:5180`. From another trusted LAN machine, open `http://:5180` and enter the console token when prompted. To keep Fleet local-only, set `HERMES_CONSOLE_HOST=127.0.0.1` in `.env`.

For active development:

```bash
npm run dev
```

The API runs on `http://127.0.0.1:5180`; the Vite frontend runs on `http://127.0.0.1:5200` and proxies `/api` to the API server. In dev mode, Vite listens on `0.0.0.0` by default so LAN clients redirected by the API can reach the frontend; set `HERMES_CONSOLE_DEV_HOST=127.0.0.1` for local-only development.

## First Run

1. Run `npm run setup`.
2. Open `http://127.0.0.1:5180`.
3. Review setup checks on the onboarding screen.
4. Open **Fleet settings** and choose a provider default.
5. Add shared credentials or complete Codex device login if your selected provider needs auth.
6. Create an agent from the dashboard.
7. Open the agent detail view for chat, lifecycle, gateway, terminal, crons, credentials, and diagnostics.

By default, Fleet clones Hermes source into `vendor/hermes-agent` from `HERMES_AGENT_REPO_URL`. To use a checkout somewhere else, set:

```env
HERMES_AGENT_SRC=/path/to/hermes-agent
```

To disable automatic source download:

```env
HERMES_AGENT_AUTO_CLONE=0
```

## Documentation

- Documentation index
- Getting started
- Operator guide
- Configuration reference
- API reference
- Codebase guide
- Implementation patterns
- Release checklist
- Security policy
- Contributing guide
- Support guide

## Common Commands

```bash
npm run setup          # prepare local runtime state and dependencies
npm start              # build and serve the production console
npm run dev            # run API and Vite dev server
npm run init:baseline  # check local setup readiness
npm run check          # TypeScript type check
npm test               # run node test suite
npm run build          # production frontend build
npm run audit:release  # repository hygiene audit
npm run release:check  # full release gate
npm run knip           # unused-code audit
```

Fleet also includes repo-local wrappers:

```bash
bin/hermes-console
bin/hermes-docker status <agent>
bin/hermes-docker logs <agent>
bin/hermes-docker shell <agent>
bin/hermes-docker restart <agent>
bin/hermes-docker update <agent>
bin/hermes-docker delete <agent>
```

Use the UI for normal operation. Use the wrappers when you need a direct terminal escape hatch for local Docker agents.

## Configuration At A Glance

Fleet reads process env first, then these files when present:

1. `runtime/.env`
2. `.env`
3. `HERMES_CONSOLE_ENV_FILE`
4. `<HERMES_INSTANCES_ROOT>/.env` when `HERMES_INSTANCES_ROOT` is external

Existing process environment variables win over `.env` values. If a shell profile, service manager, or `launchctl` export still sets `HERMES_CONSOLE_HOST=127.0.0.1`, Fleet will stay loopback-only even when `.env` says `0.0.0.0`.

The most important local settings are:

```env
HERMES_INSTANCES_ROOT=./runtime
HERMES_DOCKER_BIN=./bin/hermes-docker
HERMES_AGENT_SRC=./vendor/hermes-agent
HERMES_AGENT_AUTO_CLONE=1
HERMES_CAMOFOX_CONTEXT=./docker/camofox
HERMES_WEBHOST_CONTEXT=./docker/webhost
HERMES_CONSOLE_HOST=0.0.0.0
HERMES_CONSOLE_PORT=5180
HERMES_CONSOLE_DATA_DIR=./data
HERMES_CONSOLE_SECRETS_DIR=./secrets
HERMES_CONSOLE_REQUIRE_AUTH=1
```

For a remote Fleet node, the base URL entered in **Fleet settings -> Fleet nodes** should use the remote machine's LAN address, for example `http://192.168.3.232:5180`, plus the same bearer token stored in that remote node's `.env`.

Fleet-wide provider defaults and shared credentials are managed from **Fleet settings** and stored in ignored files:

```text
secrets/global-provider.json
secrets/global-credentials.env
secrets/global-oauth/
secrets/global-sync.json
```

Per-agent config lives under each agent folder:

```text
<agent>/
  home/
    .env
    config.yaml
    SOUL.md
  workspace/
    HERMES_WEB.md
    web/
  instance.env
  compose.yaml
```

See Configuration reference for the full environment and storage guide.

## Security Defaults

Fleet binds to `0.0.0.0` by default so trusted LAN Fleet nodes can reach it. Keep API auth enabled and set:

```env
HERMES_CONSOLE_TOKEN=<long-random-token>
HERMES_CONSOLE_REQUIRE_AUTH=1
```

The server refuses non-loopback binds unless `HERMES_CONSOLE_TOKEN` is set. `npm run setup` prompts for or generates a token when LAN binding or required auth needs one. For local-only use, set `HERMES_CONSOLE_HOST=127.0.0.1`.

Treat Fleet as a control plane. It can start and stop containers, open terminals, sync credentials, restore backups, create agents, proxy remote node actions, and optionally run self-update commands. Keep individual Hermes dashboards, Camofox VNC endpoints, and agent webhosts private unless you intentionally protect and expose them.

## Fleet Nodes

Fleet Nodes let one console coordinate other Fleet consoles on trusted machines. Add remote consoles in **Fleet settings -> Fleet nodes** with a label, base URL, optional bearer token, and enabled state.

The dashboard then merges local and remote agents, shows the host for each row, and routes create, start, stop, restart, update, delete, clone, backup, chat, gateway, terminal, and detail actions through the selected node.

Remote node bearer tokens are redacted in API responses but stored locally in `data/fleet.db`; keep `data/` private and use disk encryption on shared machines.

## Backups, Restore, And Clone

Fleet writes backups to:

```text
data/backups/
```

Backups include agent config, selected workspace files, provider defaults, and a manifest. Secrets such as `home/.env`, global credentials, OAuth state, token-like files, and generated runtime secrets are excluded unless an operator explicitly enables secret export.

Restore uses a local `.tar.gz` archive path on the console host. Restored agents receive fresh generated ports and runtime secrets. Clone duplicates a local agent into a new name and can optionally include workspace files and local per-agent credentials.

## Project Layout

```text
bin/                  fleet wrapper scripts used by the app
docker/camofox/       Camofox sidecar image context
docker/webhost/       Node.js static webhost sidecar image context
server/               Express API, services, SQLite, terminal websocket
src/                  React frontend, UI state, styles, shared models
scripts/              setup, baseline, release audit, dev/start orchestration
docs/                 user, operator, API, and maintainer documentation
runtime/              ignored default Hermes instance root
data/                 ignored SQLite database and local control state
logs/                 ignored local process logs
secrets/              ignored global provider credentials and OAuth state
vendor/hermes-agent/  ignored optional Hermes source checkout/package
```

## Releasing

Before publishing or opening a pull request:

```bash
npm run release:check
git status --short
```

For setup, onboarding, Docker, or environment changes, also run:

```bash
npm run init:baseline -- --json
```

The release gate runs type checking, tests, production build, repository hygiene audit, production dependency audit, and unused-code audit. See Release checklist for the manual review list.

# Sign in - Google Accounts

## 关联链接

- http://127.0.0.1:5180
- http://127.0.0.1:5180`.
- http://127.0.0.1:5180`;
- http://127.0.0.1:5200`
- http://192.168.3.232:5180`,
- http://:5180`

## 导航

- 项目页：[[10-项目/github.com_8ec10dbf]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
