---
type: "corpus"
item_id: "a2dcd758d6fabfbe"
title: "Show HN: Prokop – Open-source AI coding workspace with cross-project memory"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49712098"
project_url: "https://github.com/capek-dev/prokop"
author: "danielbilekq"
published_at: "2026-09-15T13:20:06Z"
captured_at: "2026-09-20T14:06:36+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-20"
pub_day: "2026-09-15"
tags:
  - 语料
  - hn_show
  - author_danielbilekq
  - story_49712098
  - show_hn
metrics: {"points": 4, "comments": 3, "engagement_velocity": 4}
comments_count: 3
comments_total: 3
discovered_via: "hn:show_hn:90d"
---

# Show HN: Prokop – Open-source AI coding workspace with cross-project memory

> [!info] 一句话导读
> Your AI agent. One server. Any device.

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49712098>
> 指标：点赞=4 · 评论=3 · engagement_velocity=4
> 作者：danielbilekq　|　发布：2026-09-15T13:20:06Z
> 项目链接：<https://github.com/capek-dev/prokop>
> 采集：2026-09-20T14:06:36+08:00　|　id：`a2dcd758d6fabfbe`

## 正文

# capek-dev/prokop

Your AI agent. One server. Any device.

- Stars: 27
- Forks: 1
- Watchers: 27
- Open issues: 8
- License: Apache License 2.0
- Default branch: main
- Created: 2026-02-25T10:04:58Z

## Languages

- CSS
- HTML
- JavaScript
- PowerShell
- Shell
- TypeScript

## Topics

- agent
- agents
- ai-agent
- ai-agents
- coding-agent

## Top Contributors

- danielbilek (779 contributions)
- github-actions[bot] (6 contributions)

---

## README

 No baked-in behavior. You build the rest.

 Prokop is the server. Everything else (the LLM, the tools, the browser, the personality)
 is something you connect to it. No default system prompt, no default tools,
 no fixed personality. You opt in to each layer. Memory, skills, workflows, agents. Your call.

 Get Started ·
 Docs ·
 Chrome Extension ·
 Discord

---

## Install

**macOS / Linux:**
```bash
curl -fsSL https://raw.githubusercontent.com/capek-dev/prokop/main/install/install-prokopai.sh | bash
```

**Windows (PowerShell):**
```powershell
irm https://raw.githubusercontent.com/capek-dev/prokop/main/install/install-prokopai.ps1 | iex
```

**Run:**
```bash
prokopai init
prokopai start
prokopai open
```

The server binary includes the client and serves it at `http://localhost:8742`. Desktop app (macOS Electron) and PWA (any device) are also available. See the Getting Started guide.

---

## Features

By default, Prokop is as bare as Codex or OpenCode. A blank prompt. No memory. No skills. No session search. You opt in to each layer in **workspace settings**.

| | |
|---|---|
| **Agents** | A preconfig that comes alive. Own home directory, own memory, own skills. Access to sessions across every workspace it's ever worked in. Persistent identity that carries context from task to task. |
| **Goal Mode** | Set a completion condition. A separate evaluator inspects real tool output every turn. It loops until tests pass. |
| **Persistent Memory** | Tell it "we use pnpm" once. Two weeks later, in a new session, it already knows. Two scopes: workspace (shared context) and agent (identity). |
| **Self-Programming Skills** | The agent notices patterns and writes its own `SKILL.md` files. It programs itself. Same two scopes as memory. |
| **Session Search** | Full-text search over all past sessions, powered by SQLite FTS5. The agent searches its own history. Two scopes: workspace and agent. |
| **Parallel Workflows** | Decompose, fan out 5 concurrent subagents, synthesize one answer. Only the final result lands in the main context window. |
| **Scheduled Tasks** | Cron jobs that run as agent sessions. Daily code review, nightly dependency check, weekly changelog. No human in the loop. |
| **Structured Responses** | Define a JSON schema, apply it to the next message. A yes/no question produces a yes/no answer. |
| **Browser Automation** | ProkopaiBrowser gives the agent real hands on Chrome: read, click, fill, navigate. Same interface as files and shell. |
| **Bring Your Own Model** | OpenAI, DeepSeek, OpenRouter, MiniMax, Zhipu. Use API keys or your ChatGPT subscription via Codex. |
| **MCP Integration** | Connect any MCP server. Full OAuth handled server-side. Tools appear alongside built-in tools. |
| **Server-First** | Persistent 24/7 server. PWA on any device. Close your laptop. Open your phone. The agent never stops. |
| **Open Source** | Apache 2.0. No telemetry. No lock-in. Prompts, tools, skills, and memory are files on disk. |

---

## Why Prokop?

Prokop connects **to** things. The browser. Your codebase. Any LLM. Prokop is the hub.
Everything else is a surface you choose to connect.

- **No baked-in behavior.** Every AI coding agent ships with hidden system prompts you can't change. Claude Code has a long system prompt buried in the npm package. Cursor has behavior rules that override your preferences. Prokop ships with none of that. The system prompt is composed from files you control. Every layer is visible and replaceable.

- **Everything is opt-in.** By default, Prokop is a blank slate. You build the agent you want, layer by layer. Turn on memory. Turn on skills. Turn on session search. Or don't. Your call.

- **You bring the keys, you keep the data.** Runs on your machine. No telemetry, no vendor lock-in, no subscription to a single AI company.

- **Files on disk.** System prompts, tools, skills, and memory are all files. Version control them, share them, delete them. No vector database, no embedding pipeline, no hidden layers.

- **An agent that evolves.** Not through fine-tuning. Through taking notes. Memory, skills, and session search accumulate over time. Your agent on day 30 is smarter than your agent on day 1. The model didn't change. The files got richer.

---

## Architecture

```
┌───────────────────────────────────────────────────────────┐
│                      Client Layer                         │
│   Desktop (Electron) · Web/PWA · Browser Extension        │
│              WebSocket + REST (any network)               │
└──────────────────────────┬────────────────────────────────┘
                           │
┌──────────────────────────┴────────────────────────────────┐
│                   Server (@prokopai/server)               │
│                                                           │
│   Agent Loop (AI SDK v6) · Tool Executor                  │
│   Goal Loop + Evaluator · Workflow Orchestrator           │
│   MCP Manager (stdio + OAuth) · Subagent Orchestrator     │
│   Memory · Skills Registry · Session Search (FTS)         │
│   Scheduled Tasks · Structured Responses                  │
│   Ask Protocol (Permissions, Questions, Forms)            │
│   SQLite Store · Compaction Engine                        │
│                                                           │
│   ~/.prokopai/                    (data, tools, preconfigs)   │
│   ~/.prokopai/agents/<name>/      (agent home: memory,        │
│                                 skills, sessions)          │
│   <workspace>/.prokopai/          (memory, mcp.json)          │
│   <workspace>/.agents/skills/  (SKILL.md files)            │
└───────────────────────────────────────────────────────────┘
                           │
              LLM Providers (OpenAI, DeepSeek, OpenRouter,
                MiniMax, Zhipu)
```

---

## Documentation

Documentation lives in this repository: docs/index.md

| | |
|---|---|
| Getting Started | Install, initialize, first session |
| Workspaces & Sessions | Capabilities, Goal Mode, MCP, Skills, Memory, Workflows |
| Configuration | API keys, models, env vars, MCP config |
| Tools | Installed tools, capability tools, writing your own |
| Security & Auth | Auth tokens, TLS, permissions |

---

## Community

Join the Discord to follow development, share what you're building, or ask for help.

---

## License

Apache 2.0

## Legacy Compatibility

Prokop still accepts legacy `JEAN2_*` environment variables and falls back to `~/.jean2` data and workspace paths when the canonical `PROKOPAI_*` variables or `~/.prokopai` paths are absent. New setups should use the Prokop names. Run `prokopai migrate` to move an existing `~/.jean2` setup to `~/.prokopai` and rewrite legacy environment keys.

# mwbpNFTechnology/toluTag

## 评论（3/3）

> **danielbilekq** · 2026-09-15T13:20:24.000Z　
> Hi HN, I’m Daniel. Prokop is my attempt at something between Codex and Hermes Agent, only for coding.I’m building it on my own. Direction of the project comes from things I need in my actual development work (including my day job), rather than trying to cover every possible AI use case and build an “everything AI app”.I’m mainly focused on ergonomics of handling multiple projects, multiple sessions, and having continuity when working with agents. I’m also trying to reduce how often I need to open an IDE, which is why it covers common file and git operations.It’s a PWA. I think PWAs are underrated, and I don’t see much point in maintaining separate desktop and mobile apps for this. It keeps development and updates simpler.Curious whether it’s useful to others working the same way.Website and docs: https://prokopai.dev

---

> **Inozem** · 2026-09-15T14:37:53.000Z　
> why not just to use Notion?

---

> **danielbilekq** · 2026-09-15T14:40:16.000Z　
> what do you mean? thats not what that is

## 关联链接

- http://localhost:8742`.
- https://raw.githubusercontent.com/capek-dev/prokop/main/install/install-prokopai.ps1
- https://raw.githubusercontent.com/capek-dev/prokop/main/install/install-prokopai.sh

## 导航

- 项目页：[[10-项目/github.com_5454ce7f]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
