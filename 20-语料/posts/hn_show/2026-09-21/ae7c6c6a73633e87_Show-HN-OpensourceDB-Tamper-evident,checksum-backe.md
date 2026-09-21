---
type: "corpus"
item_id: "ae7c6c6a73633e87"
title: "Show HN: OpensourceDB Tamper-evident,checksum-backed decision and session replay"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49777181"
project_url: "https://github.com/ZIZKA-AI-SL/ZizkaDB"
author: "Arshad-Talpur"
published_at: "2026-09-20T16:07:23Z"
captured_at: "2026-09-21T09:44:03+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-21"
pub_day: "2026-09-20"
tags:
  - 语料
  - hn_show
  - author_Arshad-Talpur
  - story_49777181
  - show_hn
metrics: {"points": 2, "comments": 1, "engagement_velocity": 2}
comments_count: 1
comments_total: 1
discovered_via: "hn:show_hn:3d"
---

# Show HN: OpensourceDB Tamper-evident,checksum-backed decision and session replay

> [!info] 一句话导读
> Audit trail database for AI agents. Tamper-evident, checksum-backed decision logs with session replay and time-travel debugging to support EU AI Act Article 12 …

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49777181>
> 指标：点赞=2 · 评论=1 · engagement_velocity=2
> 作者：Arshad-Talpur　|　发布：2026-09-20T16:07:23Z
> 项目链接：<https://github.com/ZIZKA-AI-SL/ZizkaDB>
> 采集：2026-09-21T09:44:03+08:00　|　id：`ae7c6c6a73633e87`

## 正文

# ZIZKA-AI-SL/ZizkaDB

Audit trail database for AI agents. Tamper-evident, checksum-backed decision logs with session replay and time-travel debugging to support EU AI Act Article 12 record-keeping. Drift detection, MCP, Python & TypeScript SDKs. Self-host or cloud.

- Stars: 83
- Forks: 21
- Watchers: 83
- Open issues: 22
- License: Other
- Homepage: https://db.zizka.ai
- Default branch: main
- Created: 2026-05-10T01:21:37Z

## Languages

- CSS
- Dockerfile
- JavaScript
- PLpgSQL
- Python
- Shell
- TypeScript

## Topics

- agent-auditability
- agent-debugging
- ai-agents
- ai-audit
- ai-compliance
- article-12
- audit-logging
- audit-trail
- causal-lineage
- drift-detection-mlops
- eu-ai-act
- llmops
- mcp-server
- open-source
- python
- self-hosted
- session-replay
- tamper-evident-logs
- time-travel-debugging
- typescript

## Top Contributors

- saadamjad (193 contributions)
- Zizka-ai (115 contributions)
- arshadgit23 (23 contributions)
- saadwashmen (10 contributions)
- Subhajitdas99 (7 contributions)
- mikeaig4real (3 contributions)
- aqilaziz (3 contributions)
- lamenting-hawthorn (2 contributions)
- abdurrehman616 (1 contributions)
- HafizHamzaShahid (1 contributions)

---

## README

# ZizkaDB

**When your agent misbehaves, see why.**

Self-hosted audit trail for AI agents — one command or one dashboard click from any step back to root cause.

**This repository is the open-source self-host stack** (API, tenant dashboard, SDKs, MCP). Operator admin console and VPC deploy live in private zizkadb-cloud — see docs/REPO_SPLIT.md.

CI
License: AGPL-3.0
Release
Python SDK
LangChain
CrewAI
LiveKit
MCP

**Try it ↓** · **DEVELOPMENT.md** · **CONNECT.md** · **Contributing**

## Try it (60 seconds)

Requires Docker. First image pull may take 5–10 minutes.

```bash
curl -fsSL https://raw.githubusercontent.com/Zizka-ai/ZizkaDB/main/scripts/quickstart-remote.sh | bash
```

You should see:

```text
tool_call · lookup_order · ORD-8842
  └── llm_response · gpt-4o
        └── user_message · Why was my order delayed?
```

Run again anytime: `pip install zizkadb-sdk && zizkadb demo`

### Self-host from a clone

```bash
git clone https://github.com/Zizka-ai/ZizkaDB.git && cd ZizkaDB
bash scripts/setup-local.sh
```

| Service | URL |
|---------|-----|
| API | http://localhost:8000 |
| Dashboard | http://localhost:3001/login |
| Swagger | http://localhost:8000/swagger |

Full guide: **DEVELOPMENT.md** · Troubleshooting: wiki/Troubleshooting.md

---

## Why?

Every agent team asks: *Why did it say that? Why did it call that tool?*

1. **Log** agent steps with `parent_id` (each step links to the one that caused it).
2. **Ask why** — terminal: `zizkadb why <event_id>` or Python: `(await db.why(event_id)).print()`
3. **See the chain** — walk back to the user message, wrong tool, or bad context.

**Dashboard (same chain):** Activity → support-bot → click an event → **Why? (causal)** tab.

---

## Connect (3 lines)

```python
import asyncio
from zizkadb import ZizkaDB

async def main():
    async with ZizkaDB(host="http://localhost:8000") as db:
        user = await db.log(agent="my-bot", event="user_message", data={"text": "Why is my order late?"})
        tool = await db.log(agent="my-bot", event="tool_call", data={"tool": "lookup_order"}, parent_id=user.event_id)
        (await db.why(tool.event_id)).print()

asyncio.run(main())
```

Full guides: **CONNECT.md** · LangChain · CrewAI · LiveKit (voice) · MCP / Cursor

---

## Integrations

| Python | TypeScript | LangChain | CrewAI | LiveKit | MCP | REST |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `zizkadb-sdk` | `zizkadb-sdk` | `zizkadb-langchain` | `zizkadb-crewai` | `zizkadb-livekit` | `uvx zizkadb-mcp` | Swagger |

Scaffold a project: `zizkadb init my-agent --template basic`

### Voice agents (LiveKit)

```bash
pip install zizkadb-livekit
```

One LiveKit call → one **Session** in Activity (transcript only, no audio in ZizkaDB). Full guide: CONNECT.md → LiveKit · docs/integrations/livekit.md · example.

---

 Managed cloud (Pro / Team) — optional

Same **Why?** feature — hosted at db.zizka.ai. No Docker to maintain.

The operator admin console, VPC deploy, and cloud-only marketing routes live in the private **zizkadb-cloud** repo — see docs/REPO_SPLIT.md.

| | **Pro** | **Team** |
| --- | --- | --- |
| Price | €29 / mo | €69 / mo |
| Events / mo† | 50k | 100k |
| API keys | 2 | 5 |

Sign up →

† Plan targets on managed cloud; not enforced in API yet. See docs/README.md.

 More features — drift, time-travel, search, GDPR

| Function | What it does |
| --- | --- |
| `db.baseline()` | Detect when agent behavior drifts vs past sessions |
| `db.at()` | Reconstruct what the agent knew at a timestamp |
| `db.search()` | Semantic search over agent history |
| `db.context_for()` | Inject relevant past events into prompts |
| `db.forget()` | GDPR erasure by metadata filter |

 FAQ

**Do I need to clone this repo?**
No — the curl quickstart downloads config + Docker images only.

**Do I need an API key locally?**
No — `http://localhost:8000` uses a built-in dev key. Dashboard: localhost:3001/login.

**How is this different from Langfuse / LangSmith?**
They **observe** span trees. ZizkaDB **audits** with explicit `parent_id` chains and `db.why()` on your Postgres — self-host under AGPL, no trace billing.

**Voice agents with LiveKit?**
Install **`zizkadb-livekit`** — one pip command, connect to Docker with `ZIZKADB_HOST=http://localhost:8000`. See LiveKit guide.

**`zizkadb demo` connection refused?**
Start the stack: `curl -fsSL …/quickstart-remote.sh | bash` or `bash scripts/setup-local.sh`.

 Docs & community

| | |
| --- | --- |
| Worked example | worked/01-support-order-delay |
| Examples | examples/ — includes LiveKit voice agent |
| LiveKit integration | docs/integrations/livekit.md |
| Self-hosting | DEVELOPMENT.md · wiki/Self-Hosting |
| Troubleshooting | wiki/Troubleshooting.md |
| Integrate any agent | docs/integrate/ |
| Issues · Discussions | Issues · Discussions |
| Contributing · Security | CONTRIBUTING.md · SECURITY.md |
| AI-assisted development | AGENTS.md · docs/ai/CODING_STANDARDS.md |

 AGPL-3.0 · MCP server MIT · Disable telemetry: export ZIZKADB_TELEMETRY=false

# doronp/jevc

## 评论（1/1）

> **Arshad-Talpur** · 2026-09-20T20:01:14.000Z　
> Any comments or feedback from community here? I would love to hear

## 关联链接

- http://localhost:3001/login
- http://localhost:8000
- http://localhost:8000/swagger
- http://localhost:8000`
- http://localhost:8000`.
- https://db.zizka.ai
- https://github.com/Zizka-ai/ZizkaDB.git
- https://raw.githubusercontent.com/Zizka-ai/ZizkaDB/main/scripts/quickstart-remote.sh

## 导航

- 项目页：[[10-项目/github.com_6eb52700]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
