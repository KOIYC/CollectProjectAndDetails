---
type: "corpus"
item_id: "e8c0bbd4b5c7e214"
title: "Show HN: Android-on-Device Harness – N8N Meets Tasker Meets AI"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49879515"
project_url: "https://github.com/ankurCES/Mahout"
author: "ankurCES"
published_at: "2026-09-28T15:24:07Z"
captured_at: "2026-09-29T09:42:55+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-29"
pub_day: "2026-09-28"
tags:
  - 语料
  - hn_show
  - author_ankurCES
  - story_49879515
  - show_hn
metrics: {"points": 2, "comments": 0, "engagement_velocity": 2}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:3d"
---

# Show HN: Android-on-Device Harness – N8N Meets Tasker Meets AI

> [!info] 一句话导读
> On-device workflow automation for Android — n8n meets Tasker. Every device capability is a node. Visual DAG editor, AI chat operator, 14 AI providers, on-device…

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49879515>
> 指标：点赞=2 · 评论=0 · engagement_velocity=2
> 作者：ankurCES　|　发布：2026-09-28T15:24:07Z
> 项目链接：<https://github.com/ankurCES/Mahout>
> 采集：2026-09-29T09:42:55+08:00　|　id：`e8c0bbd4b5c7e214`

## 正文

# ankurCES/Mahout

On-device workflow automation for Android — n8n meets Tasker. Every device capability is a node. Visual DAG editor, AI chat operator, 14 AI providers, on-device RAG, MCP support.

- Stars: 1
- Forks: 0
- Watchers: 1
- Open issues: 0
- Default branch: main
- Created: 2026-09-27T05:40:32Z

## Languages

- HTML
- Kotlin
- Shell

## Topics

- agentic-ai
- ai-agent
- android
- android-n8n
- clean-architecture
- coroutines
- jetpack-compose
- kotlin
- material3
- mobile-harness
- mvvm
- n8n
- n8n-alternative
- n8n-mobile
- on-device-ai
- open-source
- workflow-automation

## Top Contributors

- luminordagent (3 contributions)
- ankurCES (2 contributions)

---

## README

 Mahout

 Mahout is a fully open-source, on-device, FOSS alternative to Tasker for Android.
 On-device workflow automation for Android — n8n meets Tasker. Tasker on AI steroids..

---

Every device capability is a **node**. Wire any node to any other node. Build automation workflows visually, or describe what you want and let **Build with AI** draft it. Run them manually, on schedules, or from real-world triggers — notifications, location, sensors, media, and more.

All AI runs on-device (Gemini Nano) or through your own API keys — **no cloud subscription, no account, your data stays on your phone.**

## Screenshots

 Dashboard Run counts, AI spend, system health
 Workflows All your automations, one list

 Editor Drag-drop DAG canvas
 Chat Operator AI assistant, token-by-token streaming

 Build with AI Describe a workflow, AI drafts it
 Knowledge On-device RAG index

 Skills Agent skills + enable switches
 Permissions One-tap grant-all stepper

---

## How It Works

### Nodes & Lanes

Every node is one self-contained Kotlin `object : Node` — a spec (params, inputs/outputs, gates, timeout) plus an `execute(ctx, input)` method. Nine lanes organise ~90+ nodes:

| Lane | What it contains |
|---|---|
| **Triggers** | Manual, schedule, notifications, sensors, location, calendar, webhooks, charging, proximity, system broadcasts |
| **Data** | HTTP requests, device info, media metadata, knowledge search, variable store |
| **Logic** | Conditions (if/else), loops, JS eval, text & math, merge, wait/delay |
| **AI** | Ask AI, Classify, Extract, Agent (tool-using loop), MCP tool/resource, Decision routing |
| **Actions** | Notifications, system settings (torch, DND, Wi-Fi, Bluetooth), send intents, file writes, playlist entries, knowledge ingest |
| **Apps** | Deep-link launches, shell commands, JS runtime, workspace file I/O, UI automation (Accessibility) |

### Visual Editor

A draggable, zoomable DAG canvas. Drop nodes from the palette, wire them together, configure params. The same params that drive the UI also drive Agent tool schemas, templating, validation, and log redaction.

### Template System

Fields are wired through a simple syntax that feels like a templating language:

```
{{title}}  {{meta.artist}}  {{items[0].name}}    &larr; current item fields
{{$node.HTTP.body.x}}                             ← upstream node's first output
{{$vars.counter}}                                  ← global variable
{{$now}} {{$date}} {{$time}}                      ← built-in values
{{field ?? "default"}}                            ← fallback when missing
```

### Chat Operator

An approval-gated AI assistant that manages your workflows, runs, knowledge, skills, and a coding sandbox — all from a natural-language interface. Four permission modes:

- **Plan** — no tools, read-only thinking
- **Ask** — per-call approval
- **Auto** — risk-based: safe actions (read/search) never ask, coding actions (shell/JS) ask, destructive actions (delete, UI automation) always require approval
- **Bypass** — time-limited full automatic, with a kill switch

The chat streams token-by-token and retains a turn history with tool-use results.

### AI Providers

11 OpenAI-compatible providers (OpenAI, OpenRouter, MiniMax, Gemini, Grok, DeepSeek, Mistral, Groq, Together, Ollama, Custom) + Claude SDK + Gemini Nano (on-device). All through **your own keys** — no Mahout cloud costs anything.

### Knowledge Base

On-device RAG: index documents, folders, URLs, pasted text, Notes, and Playlists. Room FTS4 storage with BM25 ranking. The Agent can search it with `knowledge_search`.

### MCP Support

Connect remote MCP servers (stdio or SSE) and expose their tools to the Agent or as plain workflow nodes.

### Panels

Running workflows control (suspend, cancel, resume), background host monitor, second-opinion, risk assessment, and System One decision engine — all from the Dashboard.

---

## Build

```bash
# Prerequisites: Android Studio Koala+, Java 17, Gradle 8.7+, NDK (for Room schema export)

git clone https://github.com/ankurCES/Mahout.git
cd Mahout

# Build & install
./build.sh profile   # or debug; or ./gradlew :app:installDebug
adb install -r app/build/outputs/apk/profile/app-profile.apk
```

See `docs/PLAN-v5.md` for the verification smoke-test plan.

---

## Architecture

```
Mob8NApp (manual DI)
  ├── Catalog (fused lane lists)
  ├── Engine (facade: start, save, run, chat, knowledge, skills)
  │   ├── TriggerHub (receiver/worker event dispatch)
  │   ├── Executor (pure Kotlin DAG runner, JVM-testable)
  │   ├── Knowledge (Room FTS4 RAG)
  │   ├── RoomPersistence (Room DAO seam)
  │   └── HostService / NotifListener (two live hosts)
  └── Lanes
      ├── core/      Nodes, Graph, Executor, Template, Params, Gates, Persistence
      ├── triggers/  Schedule, notifications, sensors, location, webhooks
      ├── data/      HTTP, device, media, knowledge, store
      ├── logic/     Conditions, loops, JS, text/math, wait
      ├── actions/   Notify, settings, intents, files, playlist
      ├── ai/        Ask, classify, extract, Agent, MCP Client, streaming
      ├── apps/      Shell, JS runtime, UI automation, workspace
      └── ui/        All Compose screens, theme, motion
```

Key design decisions:
- **One currency**: `kotlinx.serialization.json.JsonObject` for items, logs, templates, LLM I/O, Room blobs. No DTOs.
- **One node = one `object : Node`**: spec + execute in the same file, appended to its lane's `all` list.
- **Pure-Kotlin executor**: no Android types in core except a nullable `Context` handle. JVM-testable.
- **Two live hosts**: `NotifListenerService` (system-kept-alive) + `HostService` (specialUse FGS when needed).
- **Suspend/resume survives process death**: engine state persisted to Room before notifying or enqueuing a delay.
- **Manual DI, no Hilt, no ViewModels, no navigation-compose, no Retrofit/Moshi/Gson**.
- **Ponytail comments** mark deliberate shortcuts with a ceiling and an upgrade path.
- **Secrets**: plaintext app-private prefs, excluded from backup, masked in UI, redacted from logs.

---

## Testing

```bash
./gradlew test     # 674+ JVM unit tests (pure-Kotlin core, template, graph, permissions, motion)
```

The core executor, template engine, graph validation, param validation, gates, motion tokens, and dashboard math are all JVM-tested. Android instrumentation tests cover the rest.

---

## License

MIT — see the LICENSE file.

---

 Built with Kotlin, Compose, and an elephant's patience.

## 关联链接

- https://github.com/ankurCES/Mahout.git

## 导航

- 项目页：[[10-项目/github.com_b2347ef1]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
