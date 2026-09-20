---
type: "corpus"
item_id: "32c4d987829dfc32"
title: "Show HN: An open-source control plane for your company's AI agents"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49705577"
project_url: "https://github.com/vstorm-co/agenticos"
author: "outageroom"
published_at: "2026-09-14T23:16:39Z"
captured_at: "2026-09-20T09:37:33+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-20"
pub_day: "2026-09-14"
tags:
  - 语料
  - hn_show
  - author_outageroom
  - story_49705577
  - show_hn
metrics: {"points": 3, "comments": 0, "engagement_velocity": 3}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:90d"
---

# Show HN: An open-source control plane for your company's AI agents

> [!info] 一句话导读
> The operating system for your company's AI agents. Self-hosted, open source, and yours.

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49705577>
> 指标：点赞=3 · 评论=0 · engagement_velocity=3
> 作者：outageroom　|　发布：2026-09-14T23:16:39Z
> 项目链接：<https://github.com/vstorm-co/agenticos>
> 采集：2026-09-20T09:37:33+08:00　|　id：`32c4d987829dfc32`

## 正文

# vstorm-co/agenticos

The operating system for your company's AI agents. Self-hosted, open source, and yours.

- Stars: 11
- Forks: 4
- Watchers: 11
- Open issues: 156
- License: Apache License 2.0
- Homepage: https://vstorm-co.github.io/agenticos/
- Default branch: main
- Created: 2026-07-31T09:53:01Z

## Languages

- CSS
- Dockerfile
- HTML
- JavaScript
- Makefile
- Mako
- Python
- TypeScript

## Topics

- agentic-ai
- agents
- artificial-intelligence
- nextjs
- operating-system
- prefect
- pydantic
- pydantic-ai
- python
- typescript

## Top Contributors

- DEENUU1 (513 contributions)
- OchnikBartek (58 contributions)
- dependabot[bot] (12 contributions)
- breezeFur (1 contributions)
- labmimors (1 contributions)

---

## README

# AgenticOS

**The operating system for your company's AI agents.**
Self-hosted, open source, and yours.

CI
Coverage
Docs
Licence

Python
FastAPI
Pydantic AI
Next.js
Postgres
Conventional Commits

Documentation ·
Install ·
Your first agent ·
Concepts ·
Integrations ·
Changelog ·
Roadmap

---

**An agent here is data, not code.** Instructions, a model, a set of
capabilities, a budget. You build it in a UI, publish a version, and it runs the
same way everywhere: web chat, HTTP API, Slack, Telegram. Budgets, approvals and
audit apply identically to all of them, because every surface goes through one
runner.

```yaml
# What an agent actually is - exportable, reviewable, committable to your repo.
name: Support Copilot
instructions: |
  Answer from the product wiki and cite the document you used.
  If the wiki does not cover it, say so rather than guessing.
model_profile_id: 8f1c...
capabilities:
  - id: knowledge
    config: { default_top_k: 8 }
  - id: web_research
    approval: required
collection_ids: [b2a9...]
budget:
  monthly_usd: 50
```

## Get to a running agent

Four commands, about five minutes. Needs Docker, GNU Make, uv
and bun; on Windows, WSL2. There is no `.env` to write first -
every compose variable has a default, and the one secret that cannot have one
(`SANDBOXD_TOKEN`) is generated into `backend/.env` for you.

```bash
git clone https://github.com/vstorm-co/agenticos && cd agenticos
make dev                                          # postgres (pgvector), redis, api, prefect, sandbox
make dev-frontend                                 # the Next.js container — a separate compose file
make platform-bootstrap BOOTSTRAP_API_KEY=sk-...  # an org, an owner, a key, a model, a published agent
open http://localhost:3000                        # sign in as admin@example.com / admin123
```

Then open **Agents → Getting Started → Test** and ask it something.

`make platform-bootstrap` is the step that matters, because an empty install is a
chicken-and-egg problem: an agent needs a model, a model needs a key, a key needs
an organization. It walks that chain once. Leave `BOOTSTRAP_API_KEY` out and
everything is still created - the agent is saved as a draft rather than published,
because an agent with no model cannot answer. Add a key under **Settings → AI
providers**, then publish.

Every command here is idempotent; re-run any of them whenever you are not sure
they worked.

| | |
|---|---|
| Frontend | |
| API · OpenAPI | · `/docs` |
| Prefect | |

If something does not come up, `uv run agenticos cmd doctor` (from `backend/`)
checks the database, the vault, whether there is a model an agent could actually
run on and whether every sandbox connection answers - and says which one is
missing. Install has the step-by-step version of all of this,
the prerequisites table, the host-Python workflow and a table of what each
failure means.

## Why

Most agent frameworks give you a library. You write Python, you deploy it, and
every change to an agent's behaviour is a pull request, a review and a release.
That is the right shape for a product feature and the wrong shape for the forty
small agents a company actually wants - because the person who knows what the
agent should say is not the person with commit access.

AgenticOS moves the agent out of the code and puts governance around it instead.

| | |
|---|---|
| **Agents** | Built in a UI, versioned on publish, exportable as YAML into your own git repository |
| **Capabilities** | Knowledge search, web research, charts, sandboxed Python, reasoning effort - switched on per agent, never edited as code in a browser |
| **Integrations** | Any MCP server by URL, with 58 in the picker - GitHub, Linear, Notion, Slack, Stripe, Postgres, Sentry. No connector to write |
| **Models** | 27 providers, a key per organization, fallback on outage, or self-hosted Ollama and LiteLLM |
| **Knowledge** | Collections with RAG over documents, Google Drive and S3 |
| **Skills** | Written know-how the agent loads only when it decides it is relevant |
| **Governance** | Monthly budgets that stop a run, human approval for anything side-effecting, an audit trail, per-agent alerts |
| **Surfaces** | Web chat, HTTP API, Slack, Telegram, Mattermost, embeddable widgets - one runner behind all of them |
| **Access** | Permission catalog in code, roles composed from it, per-resource sharing |
| **Multi-tenant** | Organization isolation enforced by database constraints, not only by service code |

Secrets are sealed per organization: a key copied from one
tenant's database row cannot be decrypted for another, and no API response ever
returns one.

## Stack

| Component | Technology |
|---|---|
| Backend | FastAPI + Pydantic v2 |
| Database | PostgreSQL (async via asyncpg) + pgvector |
| Agent runtime | Pydantic AI |
| Tool protocol | MCP over streamable HTTP and SSE |
| Auth | JWT + refresh tokens, API keys, Google OAuth, magic links |
| Cache | Redis |
| Background work | Prefect |
| Frontend | Next.js 15 + React 19 + Tailwind v4 |

Nothing phones home. Model prices come from a bundled
`genai-prices` snapshot, and the only
outbound calls are the ones your agents make.

## Documentation

The docs are built with MkDocs and live in `docs/`.

```bash
make docs         # serve on http://localhost:8001, live reload
make docs-build   # build with --strict, which is what CI runs
```

| | |
|---|---|
| Concepts | Spec, version, exposure, run - the four nouns everything is built from |
| Permissions | The three layers, scopes, and how a grant widens access without promoting anybody |
| Governance | Budgets, approvals, alerts, audit |
| Capabilities | Every capability that ships, its tools, config and scope |
| MCP | Connections, the server catalog, OAuth, what is *not* gated |
| Models | Providers, model profiles, fallbacks, how a run is costed |
| Secrets | The vault, secret kinds, and what never leaves it |
| Skills | The format, the bundled library, skills versus knowledge |
| Channels | Slack, Telegram, Mattermost, the widget, the raw WebSocket |
| The agent spec | Field by field, generated from the source |
| Configuration | Every setting, and the production checklist |
| Architecture | Routes → services → repositories, and why |

## Development

```bash
make check          # every CI job except e2e — about five minutes
make test           # backend + the 100% coverage gate on the platform layer
make test-fast      # no coverage, for the write-run-write loop
make test-frontend  # vitest, no coverage — the loop, not the gate
make test-frontend-cov  # vitest + the gate CI applies
make lint           # ruff, ty, eslint, prettier, tsc, and the two guard scripts
make test-e2e       # playwright, against a running stack
make test-migrations  # apply and roll back the whole chain
make format         # ruff + prettier
make help           # everything else
```

`make check` is `lint test test-frontend-cov build-frontend docs-build audit` —
every job in `ci.yml` except `e2e`, which needs a
seeded backend, and the image scan, which runs only on a push to `main`. The
workflow calls those same targets rather than repeating their commands, and
`backend/tests/test_ci_parity.py` fails if the two drift.

The **platform layer** - everything AgenticOS adds on top of the generated
template - is held at 100% coverage and CI fails below it. The exact list is
`[tool.coverage.run] include` in `backend/pyproject.toml`, mirrored in
`[[tool.ty.overrides]]` because a module held to 100% coverage is held to the type
checker too. Template-inherited subsystems are reported by `make coverage-all` but
do not gate the build; see Testing for why, and for what belongs
in each test layer.

> [!IMPORTANT]
> The database must be `pgvector/pgvector:pg16`, not stock Postgres. The
> retrieval store issues `CREATE EXTENSION IF NOT EXISTS vector` the first time a
> collection is written to, and stock Postgres answers
> `extension "vector" is not available` - a 500 before any row is committed. If
> document ingestion fails on a fresh environment, check the image first.

## Contributing

Read Architecture and Patterns
first - the layering is enforced by tests, not by convention. Then
Adding a feature.

New behaviour ships with tests; a bug ships with a regression test. Run
`make check` before opening a pull request - it is every CI job except the two
named above, and a test keeps that true.

Three things that trip up a first change here:

- **An agent is data.** There is no `@agent.tool` and no agent module to decorate;
 a new tool reaches a model through the capability registry. See
 Add a capability.
- **`require(...)` gates go on collection routes only.** A permission gate on a
 per-resource route cannot see that row's grants, so it refuses a Viewer who was
 explicitly given access. Per-resource routes hand the decision to a service that
 calls `resolve_access`. See Permissions.
- **If the tool you need already exists as an MCP server, write no code.** Point at
 it and its tools appear in the Builder. See MCP.

If you work on this with an AI agent, `.claude/` holds the
repository's own rules and task skills - the same conventions, written for a machine.

## Licence

Apache License 2.0 - see `LICENSE` and `NOTICE`.

Apache-2.0 rather than MIT because AgenticOS is meant to be deployed inside other
companies: the explicit patent grant is the part their legal review asks about,
and MIT is silent on it.

---

*Built from the Full-Stack AI Agent Template.*

# JamesRyanATX/fcbnerd

## 关联链接

- http://localhost:3000
- http://localhost:8001,
- https://vstorm-co.github.io/agenticos/

## 导航

- 项目页：[[10-项目/github.com_1e9e8b1e]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
