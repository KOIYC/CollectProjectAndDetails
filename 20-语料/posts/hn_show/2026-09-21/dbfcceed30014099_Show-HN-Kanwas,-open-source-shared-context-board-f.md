---
type: "corpus"
item_id: "dbfcceed30014099"
title: "Show HN: Kanwas, open-source shared context board for teams and agents"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=47961491"
project_url: "https://github.com/kanwas-ai/kanwas"
author: "SiNTEx"
published_at: "2026-04-30T12:35:37Z"
captured_at: "2026-09-21T02:52:27+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-21"
pub_day: "2026-04-30"
tags:
  - 语料
  - hn_show
  - author_SiNTEx
  - story_47961491
  - show_hn
metrics: {"points": 57, "comments": 4, "engagement_velocity": 57}
comments_count: 4
comments_total: 4
discovered_via: "hn:show_hn:174d"
---

# Show HN: Kanwas, open-source shared context board for teams and agents

> [!info] 一句话导读
> Kanwas — Shared context board for teams and agents

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=47961491>
> 指标：点赞=57 · 评论=4 · engagement_velocity=57
> 作者：SiNTEx　|　发布：2026-04-30T12:35:37Z
> 项目链接：<https://github.com/kanwas-ai/kanwas>
> 采集：2026-09-21T02:52:27+08:00　|　id：`dbfcceed30014099`

## 正文

# kanwas-ai/kanwas

Kanwas — Shared context board for teams and agents

- Stars: 744
- Forks: 102
- Watchers: 744
- Open issues: 7
- License: Other
- Homepage: https://kanwas.ai/
- Default branch: master
- Created: 2026-04-22T10:49:58Z

## Languages

- AppleScript
- CSS
- Dockerfile
- HTML
- JavaScript
- Shell
- TypeScript

## Topics

- agents
- canvas
- collaboration
- context-management

## Top Contributors

- marek-vybiral (2 contributions)

---

## README

 Shared context board for teams and agents

 Try Kanwas for free at kanwas.ai

# What's Kanwas?

Kanwas is a multiplayer workspace for AI work. Teams and an AI agent share the same documents, evidence, and decisions, with the agent's tool calls streaming into the same timeline everyone sees.

Kanwas canvas

## Who it's for

- **Founders.** Turn a fundraising deck, customer interviews, MVP spec, and hiring plan into one canvas where the agent helps across all of them. Less context to keep in your head, more output across many fronts.
- **Product managers.** Drop interview snippets, tickets, and competitor screenshots on a board; get a discovery readout and a PRD with every claim traceable to its source.
- **Developers.** Pull a PM's spec, designs, and research onto a canvas; work with the agent to turn it into an implementation plan with tasks and acceptance criteria. Then `kanwas pull` the markdown into your repo and hand it to Claude Code, Codex, or whatever coding agent you use.
- **Marketers.** Plan a launch with positioning, messaging, asset list, and timeline. The agent drafts copy variants you can compare side-by-side and iterate on with the team.
- **Sales.** A reusable account board: research, comms history, stakeholder map, and proposal drafts. Each deal makes the template better.

## Why teams use it

- **Shared context that compounds.** Every decision and outcome makes the next board better than the last.
- **Canvas + agent on one surface.** Work alongside AI over the same evidence, ideas, and trade-offs — transparent to everyone.
- **Sharp deliverables in minutes.** Generate structured, execution-ready artifacts for every stage of the work.
- **Your files, your repo.** Git-backed markdown filesystem with full version history. No vendor lock-in.

## Quickstart

### Prerequisites

- Docker + Docker Compose
- An Anthropic API key (and/or OpenAI API key)

### Run it

```bash
git clone https://github.com/kanwas-ai/kanwas.git
cd kanwas

# Env files — fill in API keys, APP_KEY, etc.
cp .env.example .env
cp backend/.env.example backend/.env
cp yjs-server/.env.example yjs-server/.env
cp frontend/.env.example frontend/.env

docker-compose --profile app up
```

Open http://localhost:5173 and you're in.

For local development (hot reload, running services with `pnpm dev`) and the architectural walkthrough, see `docs/SYSTEM_OVERVIEW.md`.

## CLI

`kanwas` is a command-line tool for syncing a workspace with your local filesystem. Useful when you want to edit notes in your editor of choice, bulk-import markdown you already have on disk, or script workspace access from CI or another agent.

### Install

```bash
npm install -g @kanwas/cli
```

### Authenticate

```bash
kanwas login
```

Opens a browser tab to authorize the CLI. Auth is stored globally in `~/.kanwas/config.json`.

### Edit a workspace locally

```bash
mkdir my-workspace && cd my-workspace
kanwas pull            # interactive picker, downloads files into the current directory
# ...edit files in your editor...
kanwas push            # uploads local changes back to the workspace
```

After the first `pull`, the directory is bound to that workspace via `.kanwas.json`. Subsequent `pull` / `push` reuse it automatically.

### Import markdown from disk

```bash
kanwas import ./notes                       # interactive workspace picker
kanwas import ./notes --name "My Workspace" # non-interactive, by name
kanwas import ./intro.md --id <uuid>        # single file, by ID
kanwas import ./notes --dest research       # place imports under a subfolder
kanwas import ./notes --overwrite           # replace files that already exist
```

Walks the source path, picks up every `.md` file (other files are skipped), preserves directory structure, and creates them in the target workspace.

### List / script

```bash
kanwas workspaces             # list workspaces
kanwas workspaces --json      # JSON output for scripting
kanwas pull --id <uuid>       # non-interactive: pin to a specific workspace
kanwas pull --name "<name>"   # non-interactive: by exact name
```

All commands accept `--id` or `--name` to skip the interactive picker, which makes them safe to use from CI or wrapping agents.

Source: `cli/` · npm: `@kanwas/cli`

## Community

Questions, ideas, want to chat with the team?

- 💬 Kanwas Kollective on Slack

## Contributing

We'd love help. A few notes:

- Read `docs/SYSTEM_OVERVIEW.md` for the mental model and project-specific gotchas (especially around Yjs/BlockNote — clone semantics and transactions matter).
- Open an issue before large changes so we can align on direction.
- Run `pnpm format` and the relevant package's lint before opening a PR.
- First-time contributors will be asked to sign our Contributor License Agreement. The CLA bot will comment on your PR with a link and the signing phrase — you only need to sign once.

## License

Kanwas is licensed under the Apache License 2.0.

## Acknowledgements

Kanwas stands on the shoulders of Yjs, BlockNote, AdonisJS, E2B, and many other great open-source projects.

# NishantJoshi00/nvim-config

## 评论（4/4）

> **abhafeez1922** · 2026-04-30T13:38:54.000Z　
> The Docker Compose setup looks pretty approachable. That said, the README should probably be more explicit about external services. It is not just “bring your LLM API key” if you want the full thing running. There are other pieces like Parallels, Composio, sandboxing, etc.A table with required, optional, and local alternative services would make it much better.Also kudos for choosing Apache 2.0 instead of one of those “open source but not really” licenses.

---

> **yvemk50abb** · 2026-04-30T13:43:08.000Z　
> I think this will work good.

---

> **ashokade** · 2026-04-30T13:55:02.000Z　
> The closest comparison in my head is Claude Code plus Obsidian, but neither really has this shape. Claude Code is great when the task is local and code-shaped. Obsidian is great for my own notes. Kanwas feels more like a place to work with others.The canvas is the part that makes it click for me personally. It is nice to be able to share a board with documents in a way that preserves the natural relationships between these. Also really like the thinking mode in agent. Asked a lot of good questions.

---

> **creazyheart** · 2026-04-30T14:10:42.000Z　
> Great project

## 关联链接

- http://localhost:5173
- https://github.com/kanwas-ai/kanwas.git
- https://kanwas.ai/

## 导航

- 项目页：[[10-项目/github.com_3ad775a5]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
