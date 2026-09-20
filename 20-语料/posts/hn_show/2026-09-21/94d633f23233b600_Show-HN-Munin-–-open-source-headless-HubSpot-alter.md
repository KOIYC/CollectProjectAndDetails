---
type: "corpus"
item_id: "94d633f23233b600"
title: "Show HN: Munin – open-source headless HubSpot alternative"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=48731360"
project_url: "https://github.com/getmunin/munin"
author: "kman_85"
published_at: "2026-06-30T11:51:19Z"
captured_at: "2026-09-21T02:53:10+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-21"
pub_day: "2026-06-30"
tags:
  - 语料
  - hn_show
  - author_kman_85
  - story_48731360
  - show_hn
metrics: {"points": 3, "comments": 3, "engagement_velocity": 3}
comments_count: 3
comments_total: 3
discovered_via: "hn:show_hn:113d"
---

# Show HN: Munin – open-source headless HubSpot alternative

> [!info] 一句话导读
> The customer platform for the agentic era. MCP-first, open source, self-hostable.

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=48731360>
> 指标：点赞=3 · 评论=3 · engagement_velocity=3
> 作者：kman_85　|　发布：2026-06-30T11:51:19Z
> 项目链接：<https://github.com/getmunin/munin>
> 采集：2026-09-21T02:53:10+08:00　|　id：`94d633f23233b600`

## 正文

# getmunin/munin

The customer platform for the agentic era. MCP-first, open source, self-hostable.

- Stars: 11
- Forks: 0
- Watchers: 11
- Open issues: 17
- License: MIT License
- Homepage: https://www.getmunin.com
- Default branch: main
- Created: 2026-04-29T16:19:16Z

## Languages

- CSS
- Dockerfile
- HTML
- JavaScript
- PLpgSQL
- Shell
- TypeScript

## Topics

- analytics
- chat-widget
- cms
- crisp-alternative
- crm
- customer-platform
- headless
- hubspot-alternative
- intercom-alternative
- knowledge-base
- mcp
- mcp-first
- mcp-server
- outreach
- salesforce-alternative

## Top Contributors

- kmonsoe (676 contributions)
- github-actions[bot] (197 contributions)
- dependabot[bot] (6 contributions)

---

## README

# Munin

> Open-source, headless HubSpot alternative.

 Website ·
 See it in action ·
 Documentation ·
 MCP Registry

CRM, conversations, outreach, CMS, knowledge base, and analytics on one Postgres schema — exposed as tools your agents drive, not screens you click through. Headless the way a headless CMS is: there's a thin dashboard for settings, auth, and human-in-the-loop review, but the apps themselves have no admin UI. Every action runs through MCP tools, callable from any MCP-compatible client (Claude, Cursor, ChatGPT, custom runners) — same tools, same permissions, same audit log, whether a human or an agent is driving. Munin even ships its own: an in-process, per-org agent runner that answers live conversations and works the curation queue against an LLM provider you configure — so the platform runs out of the box, with external MCP clients optional.

 The dashboard — a thin shell for settings, auth, and human-in-the-loop review. No admin UI for app data; it drives the same MCP tools your agents call.

 The embeddable chat widget — answering a live customer from the knowledge base, ready to hand off to a human and be picked back up by the agent.

## Modules at a glance

| Module | Tools | What it does |
|---|---|---|
| Knowledge Base | `kb_*` | documents, hybrid search, audience scoping |
| Conversations | `conv_*` | channels, messages, handover |
| CRM | `crm_*` | contacts, companies, deals |
| CMS | `cms_*` | collections, entries, assets |
| Outreach | `outreach_*` | campaigns, drafts, propose-only |
| Analytics | `analytics_*` | page-view + search events |

These six modules aren't separate products — they share one Postgres schema, one permission model, and one audit log. Watch how they tie together:

## Core modules

#### Knowledge Base
- Markdown articles organized into spaces, each scoped to the audiences allowed to see it.
- Hybrid search that blends keyword matching with meaning-based results.
- Website import — crawl a public site and turn each page into an article in the background, automatically dropping articles when their source page disappears.
- Full version history with restore, plus a review queue for proposed edits.

#### Conversations
- One inbox across email, chat widget, voice (Threll.ai / Vapi), and SMS (Twilio / MessageBird).
- Inbound *and* outbound — agents answer conversations and can place outbound calls.
- Assignable, organized by topic, and searchable across every message.
- Built-in handoff to a human, with notifications to your own systems as conversations change.

#### CRM
- Contacts, companies, deals, activities, pipelines, and segments.
- AI-written summaries and suggested next actions, kept separate from what people edit by hand.
- Consent tracking — the lawful basis and source for each contact, required before they can be added to any outreach.
- Automatic duplicate detection that proposes merges for review, plus bulk contact import.

#### CMS
- Content collections with structured fields, and entries you can publish in multiple languages.
- Rich content blocks for article bodies — callouts, quotes, media, and more.
- Scheduled publishing and a media library for images and files.
- Full version history with restore, search, and cross-references between entries.
- A public content API serves your site or app, with engagement tracking built into every entry.

#### Outreach
- Propose-only outbound email — campaigns, segments, and drafts for both first touches and replies.
- Recipients are drawn only from contacts who have recorded consent (see CRM).
- Every message waits for human approval; nothing is ever sent automatically.

#### Analytics
- Captures page views and on-site searches across anything you want to measure.
- CMS pages are tracked automatically; for any other page, you add a small tracking snippet.
- Conversion funnels and per-visitor journeys — once someone is identified, their visits link to a CRM contact, including the anonymous ones from before.
- Breakdowns by traffic source, referrer, and country, plus "what to write next" signals (popular topics, engagement, and searches that came back empty).

## Automation

#### Conversation loop
An in-process, per-org agent runner answers live conversations on every channel (chat widget, email, SMS, voice) against the LLM provider you configure — drafting and sending replies, and handing off to a human when needed.

#### Curator loop
The in-process agent runner also works a durable background job queue: scheduled KB curation, CRM hygiene, contact extraction, stale-content review, and outreach drafts, with retry and dead-letter handling.

#### Playbooks & skills
Packaged markdown procedures (`skill://module/ `) for multi-step, cross-module workflows, surfaced over MCP — followed both by Munin's own runner and by any external AI agent operating on the platform.

## Platform

#### Data portability
Symmetric `*_export` / `*_import` MCP tools (and `/v1/ /export|import` REST endpoints) per module, so an agent can move an org's data between a self-hosted server and the cloud in either direction. See `skill://playbooks/data-migration`.

#### Audit & webhooks
Every action is written to an audit log, and webhooks fan those events out to your own endpoints with signed, replayable deliveries.

#### Alerts & feedback
Operational issues surface as system alerts the agent can list, acknowledge, and resolve. An in-product feedback channel lets you file feature requests and vote on Munin's public roadmap.

#### Auth & access
Sign-in and access control run on BetterAuth, with OAuth 2.1 dynamic-client registration and team invites.

## See it in action

> Lovable builds your frontend. Munin spins up your operations. One prompt, one MCP endpoint — and the agents do the rest.

Watch Lovable build a real website from a single prompt while Munin stands up everything behind it — the CMS the blog reads from, a seeded knowledge base, analytics, and a chat widget that already knows the business. No click-ops, no screens to wire up; the agent does the work, over one MCP endpoint. Then a real customer conversation plays out: answered from the knowledge base, handed off to a human when it matters, and picked back up by the agent to close.

## Two ways to run

**Self-host** (this repo): single-tenant, invite-only.

```bash
git clone https://github.com/getmunin/munin.git
cd munin
cp .env.example .env
docker compose up
```

Secrets left at their `.env.example` placeholders are auto-generated on first boot and persisted in the `munin-data` volume — fine for local self-hosting. For shared or production deployments, set strong `MUNIN_AUTH_SECRET` + `MUNIN_KEY_PEPPER` + `MUNIN_ENCRYPTION_KEY` values (`openssl rand -base64 48`) in `.env` instead.

The first user to sign up becomes the org admin; subsequent users need an invitation token or an email whose domain is in `MUNIN_ALLOWED_EMAIL_DOMAINS`.

**Hosted** (https://www.getmunin.com): multi-tenant, one signup per org.

## Try it locally

After `docker compose up`, the backend listens on `:3001` and the dashboard on `:3000`.

1. Open `http://localhost:3000` and register the first user — they become the singleton org admin.
2. In the dashboard, go to **Settings → API keys** and mint an admin key (`mn_admin_…`). Shown once; treat like a password.
3. Poke at the API and tools:

```sh
# REST control plane — direct, no OAuth
curl -s http://localhost:3001/v1/kb/spaces \
  -H "Authorization: Bearer mn_admin_..." | jq

# MCP tool browser (recommended for poking at tools/skills)
npx @modelcontextprotocol/inspector
# In its UI: URL = http://localhost:3001/mcp, Auth = Bearer mn_admin_...

# Raw curl over Streamable HTTP — useful for sanity-checking the transport
curl -N -X POST http://localhost:3001/mcp \
  -H "Authorization: Bearer mn_admin_..." \
  -H "Content-Type: application/json" \
  -H "Accept: application/json, text/event-stream" \
  -d '{"jsonrpc":"2.0","id":1,"method":"tools/list"}'
```

The OpenAPI spec for the REST control plane is at `packages/backend-core/openapi.json`. To wire an MCP client like Claude or Cursor, see Connect your AI agent below.

## Connect your AI agent

Once you've signed up (hosted) or run `docker compose up` (self-host), point your MCP client at the URL — `http://localhost:3001/mcp` for self-host, or `https://mcp.getmunin.com` for hosted.

**Claude Code (CLI):**

```sh
claude mcp add munin http://localhost:3001/mcp
```

**Claude Desktop** — add to your MCP config:

```json
{
  "mcpServers": {
    "munin": {
      "url": "http://localhost:3001/mcp"
    }
  }
}
```

The first call triggers an OAuth consent screen in your browser, then your agent has the full tool surface — Knowledge Base, Conversations, CRM, CMS, Outreach, Analytics.

## Two trust contexts, one MCP endpoint

The same `/mcp` endpoint serves two distinct callers, audience-aware:

- **Admin agents** (Claude Desktop, Cursor, internal automation) — OAuth-authorized by you. Full tool surface, scope-gated per `kb:*`, `conv:*`, `crm:*`, `cms:*`, `outreach:*`, `analytics:*`.
- **End-user agents** (your voice AI, web chatbot, mobile app helper) — short-lived delegated tokens minted server-side from your backend, scoped to one of your end-users. Only self-service tools (read your own contact, send a message in your own conversation).

See `packages/backend-core/src/control/delegated-token.controller.ts` for the token-mint API. The `@getmunin/sdk` Node client wraps it.

## Stack

| Layer | Tech |
|---|---|
| Language & runtime | TypeScript, Node 24 LTS |
| Monorepo | Turborepo, pnpm |
| Backend | NestJS |
| Frontend | Next.js |
| Data | Postgres + pgvector, Drizzle |
| Protocol & auth | MCP Streamable HTTP, BetterAuth + OAuth 2.1 |

## Documentation

Developer docs live at **getmunin.com/docs** — guides, the REST API reference, the full MCP tool list, and the skill library.

## Contributing

Contributions are welcome. `pnpm install`, then `docker compose up` (or `pnpm dev`) gives you a full stack on `:3001` (backend) and `:3000` (dashboard). Branch from `main` as ` / ` (e.g. `feat/website-import-reconcile`), keep PRs focused, and make sure CI (lint, typecheck, test, build) passes.

See CONTRIBUTING.md for setup, commit conventions, and PR guidelines.

## Security

Found a vulnerability? Please **don't** open a public issue — email **security@getmunin.com** instead. See SECURITY.md for scope and our response timeline.

## License

MIT. See LICENSE.

Bundled third-party dependencies retain their own licenses — see THIRD_PARTY_LICENSES.md (generated by `pnpm licenses:generate`, verified in CI).

# AgentShare Agent Readiness - Chrome Web Store

## 评论（3/3）

> **kman_85** · 2026-06-30T12:21:30.000Z　
> Hi everyone, Kjell here. This is a "small" side project that I have been working on for a couple of months. The reason I started it was because I had to do cold outreach on another project that I was working on earlier this year. HubSpot was too expensive, so I hacked a small outreach tool together using Claude: Gmail + Google Sheet + Apps Script.It worked quite well, but the script quickly grew complex, and it's not ideal to manage contacts in a Google Sheet. So I decided to build what I needed once and for all and I wanted to make it completely open-source and with a MIT licence.In the link you can see the result. What started small has now grown into a full-fledged headless customer platform. It's all designed around MCP being a primary interface. Sure, it might be thin in some areas, but it works surprisingly well. Give it a spin and let me know what you think, appreciate all feedback either product or tech-wise. Here's a small 3 min video where I demo some of the features: https://vimeo.com/1204180225

---

> **blaqq2** · 2026-06-30T16:37:02.000Z　
> Congrats on the launch! I am pretty sure every great dev has built a simple workaround for a task at least once before realizing how painful it is to maintain state or even manage contacts in a spreadsheet. Will give the repo a spin during my free time, great work open-sourcing this.

---

> **kman_85** · 2026-06-30T17:31:40.000Z　
> Thanks! Looking forward to hear what you think of it.

## 关联链接

- http://localhost:3000`
- http://localhost:3001/mcp
- http://localhost:3001/mcp,
- http://localhost:3001/mcp`
- http://localhost:3001/v1/kb/spaces
- https://github.com/getmunin/munin.git
- https://mcp.getmunin.com`
- https://www.getmunin.com

## 导航

- 项目页：[[10-项目/github.com_0664b195]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
