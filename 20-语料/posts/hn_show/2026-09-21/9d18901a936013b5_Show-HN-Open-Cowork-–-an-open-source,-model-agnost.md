---
type: "corpus"
item_id: "9d18901a936013b5"
title: "Show HN: Open-Cowork – an open-source, model-agnostic computer-use agent"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49113363"
project_url: "https://github.com/coasty-ai/open-cowork"
author: "nkov47"
published_at: "2026-07-30T17:54:59Z"
captured_at: "2026-09-21T03:11:14+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-21"
pub_day: "2026-07-30"
tags:
  - 语料
  - hn_show
  - author_nkov47
  - story_49113363
  - show_hn
metrics: {"points": 2, "comments": 0, "engagement_velocity": 2}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:83d"
---

# Show HN: Open-Cowork – an open-source, model-agnostic computer-use agent

> [!info] 一句话导读
> coasty-ai/open-cowork

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49113363>
> 指标：点赞=2 · 评论=0 · engagement_velocity=2
> 作者：nkov47　|　发布：2026-07-30T17:54:59Z
> 项目链接：<https://github.com/coasty-ai/open-cowork>
> 采集：2026-09-21T03:11:14+08:00　|　id：`9d18901a936013b5`

## 正文

# coasty-ai/open-cowork

Open-source alternative to Claude Co-Work built by Claude. with BYOK

- Stars: 127
- Forks: 30
- Watchers: 127
- Open issues: 2
- License: MIT License
- Homepage: https://coasty.ai/?view=developers
- Default branch: main
- Created: 2026-06-11T19:55:21Z

## Languages

- CSS
- HTML
- JavaScript
- TypeScript

## Topics

- anthropic
- anthropic-api
- anthropic-claude
- automation
- browser-automation
- byok
- byok-ai-tools-code-assistant
- claude-cowork
- claude-cowork-alternative
- claude-cowork-free
- claude-cowork-windows
- computer-use
- computer-use-agent
- computer-use-agents
- computer-use-windows
- gemini
- llm-agents
- openai

## Top Contributors

- PrateekJannu (97 contributions)
- Adityakk9031 (1 contributions)

---

## README

 open-cowork

 Hand off computer tasks to an AI coworker — watch it work, approve from anywhere.

 An open-source agentic coworker that sees a screen and acts on it — your own desktop,
 a cloud VM, or a browser. Bring your own LLM, or use Coasty's out of the box.

 Quickstart  · 
 Bring your own LLM  · 
 Automate your PC  · 
 What it does  · 
 How it works  · 
 Docs

 Delegate a task → watch it work, step by step → get the result. Runs with zero setup.

---

## Quickstart

> **Prereqs:** Node ≥ 22.5 · pnpm 10 (`corepack enable`)

```bash
git clone https://github.com/coasty-ai/open-cowork.git && cd open-cowork
pnpm install
pnpm desktop
```

**One command, zero config.** `pnpm desktop` starts the backend and web UI, then opens the
desktop app — the build that can drive **your own screen**. With no key set it runs in **demo
mode**: a bundled mock server and a throwaway sandbox key. No account, no network, no billing.

Then, in the window:

1. Sign in with any email.
2. On **Delegate**, pick **“This computer (local screen).”**
3. Type a task → confirm the cost → watch it work.

> ⚠️ Local control moves your **real** mouse and keyboard. Stop with **Cancel** or close the
> window. Start small — safety notes in **RUN_LOCALLY.md**.

### Ways to run

| Goal | How | Cost |
| --- | --- | --- |
| **Automate your own PC** | `pnpm desktop` | demo **$0** · BYOK = your provider's rate |
| **Web app only** | `pnpm dev` → | **$0** |
| **Use your own LLM** | put a key in `.env`, or **Settings** | your provider's rate · **local = $0** |
| **Use your Coasty account** | add `COASTY_API_KEY` to `.env` | sandbox key = **$0** |

Everything has a working default. The only thing you might set is a key — and even that is
optional.

---

## Bring your own LLM

```bash
echo 'ANTHROPIC_API_KEY=sk-ant-…' >> .env
pnpm desktop
```

That's it. The desktop detects the key, picks a vision-capable model, and tells you what it
chose. Works the same with `OPENAI_API_KEY`, Gemini, xAI, Mistral, Groq, or OpenRouter — and
with **Ollama / LM Studio** for a model running entirely on your machine, no key and no cloud.

Because computer use is screenshot-driven, open-cowork verifies the model can actually **see**
before spending anything, using a bundled capability catalog of **1,105 vision-capable models**
distilled from two open databases, plus each provider's own metadata. A model that can't see images is blocked with a
clear message rather than sent a blind screenshot.

**→ Full guide: BYOK.md** — every provider, local setup, capability resolution, and
the long-horizon guards that stop a wedged run in seconds instead of burning the step cap.

---

## What it does

- 💬 **Delegate in chat** — _"rename these files and email the report"_ — and watch it execute
 step by step with a live screen view.
- 🚀 **Zero-setup managed tasks** — hand over a goal with no machine at all; Coasty
 provisions a fresh VM, runs it fully autonomously, and destroys it afterwards. The
 model-input frames it saw outlive the machine, so you can always audit what happened.
- 🧠 **Any model** — Anthropic, OpenAI, Gemini, xAI, Mistral, Groq, OpenRouter, or a local
 model. Coasty is just the default.
- 📺 **Supervise runs** — durable event timeline (SSE with replay); cancel, resume, or take
 over from web, desktop, or phone.
- 🔁 **Build workflows** — a versioned JSON DSL (task · assert · if · loop · parallel · retry ·
 human_approval) with validation, cost estimates, and hard server-side budget caps.
- 🖥️ **Manage machines** — provision cloud VMs, snapshot, stop, terminate, with live rates.
- 📱 **Stay in the loop** — start a run on your laptop; when it pauses for approval, the banner
 pops on your phone.
- 💸 **See cost at all times** — wallet balance, worst-case estimates, and an explicit
 confirm-the-cost handshake before anything billable starts.

| Capability | 🖥️ Desktop | 🌐 Web | 📱 Mobile |
| --- | :---: | :---: | :---: |
| Local screen control | ✅ first-class | → cloud machine | → cloud machine |
| Managed task (no machine to set up) | ✅ | ✅ | view + monitor |
| Cloud-machine control + live view | ✅ | ✅ | ✅ |
| Task chat + run dashboard | ✅ | ✅ | ✅ |
| Workflow builder | ✅ full | ✅ full | view + approve |
| Approvals / human takeover | ✅ | ✅ | ✅ |

---

## How it works

```text
 You ──► open-cowork backend ──► Coasty API ──► a screen the agent drives
            │   (the ONLY place           ├─ your own desktop   (desktop app)
            │    the API key lives)       ├─ a Coasty cloud VM  (any client)
            │                             ├─ an ephemeral VM    (managed task —
            └──► web / desktop / mobile   │    made + destroyed for you)
                 live events, approvals,  └─ a browser page     (Playwright)
                 costs
```

One shared **agent loop** (screenshot → predict → act → repeat) drives any screen through a
single `Executor` interface — `LocalExecutor`, `RemoteMachineExecutor`, or `BrowserExecutor`.
The **predict** step is its own seam, so your own LLM is just another implementation
behind the same contract; the loop, executors, and UI don't care which is behind it.

Clients never hold the API key: they talk to the backend with short-lived session tokens, and
the backend proxies to Coasty, verifies HMAC-signed webhooks, persists runs, and fans events
out over SSE. Full design in **ARCHITECTURE.md**.

## Security

`COASTY_API_KEY` exists **only** in the backend's environment — browsers, Electron renderers,
and the mobile app authenticate with short-lived session tokens and never see it. This is
enforced by tests that scan every client bundle and a runtime E2E assertion that watches every
browser request for secret material. BYO LLM keys follow the same rule, encrypted with your OS
keychain. Threat notes in **SECURITY.md**.

---

## Docs

| Guide | What's inside |
| --- | --- |
| **RUN_LOCALLY.md** | Automate your own PC with the desktop app — step by step |
| **BYOK.md** | Every provider, local models, capability resolution, long-horizon guards |
| ARCHITECTURE.md | Monorepo map, the Executor abstraction, agent loop, realtime + data model |
| SECURITY.md | Key custody, HMAC, trust boundary, threat table |
| DEPLOYMENT.md | Running the backend + each client in production |
| COOKBOOK.md | Recipes: cross-device approval, workflows, scripting the loop |
| DECISIONS.md · CONTRIBUTING.md · SUMMARY.md | Stack choices · how to contribute · what was built + coverage |

### Project layout

```text
packages/core       Coasty client, agent loop, workflow DSL, cost estimator, HMAC — isomorphic
packages/executor   Executor abstraction: LocalExecutor, RemoteMachineExecutor, BrowserExecutor
packages/llm        BYO LLM seam: any provider via the Vercel AI SDK (desktop-only)
packages/ui         Shared React design system + domain components
apps/backend        Fastify: auth, Coasty proxy (sole key holder), webhooks, SQLite, SSE
apps/web            Vite + React SPA (also hosted by the desktop shell)
apps/desktop        Electron shell + LocalRunManager (local screen control)
apps/mobile         Expo / React Native companion (monitor + approve)
tools/mock-coasty   Full offline mock of the Coasty API (REST + SSE + signed webhooks)
e2e                 Playwright end-to-end flows (web + desktop)
```

### Commands

| Command | What |
| --- | --- |
| `pnpm desktop` | full stack + the desktop app (local screen control) |
| `pnpm dev` | mock + backend + web (`--no-web` for API only) |
| `pnpm run doctor` | preflight: Node, deps, key shape, Electron binary |
| `pnpm fix:electron` | re-install Electron's binary if the desktop app won't start |
| `pnpm test` · `pnpm typecheck` · `pnpm lint` | offline checks, no spend |
| `pnpm e2e` | Playwright: web + desktop journeys vs the mock |
| `pnpm update:models` | refresh the model capability catalog |

---

## Links

- **Issues & feature requests:**
- **Report a vulnerability:** Security Advisories (see SECURITY.md)
- **Coasty:** docs · API keys

## License

MIT © Coasty / open-cowork contributors

# Show HN: secure FFmpeg | Hacker News

## 关联链接

- https://coasty.ai/?view=developers
- https://github.com/coasty-ai/open-cowork.git

## 导航

- 项目页：[[10-项目/github.com_3e57c92f]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
