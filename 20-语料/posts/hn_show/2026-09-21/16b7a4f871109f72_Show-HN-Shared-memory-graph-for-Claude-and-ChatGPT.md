---
type: "corpus"
item_id: "16b7a4f871109f72"
title: "Show HN: Shared memory graph for Claude and ChatGPT, over MCP"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49124733"
project_url: "https://uml.gpmai.workers.dev/"
author: "12ziyad"
published_at: "2026-07-31T15:58:01Z"
captured_at: "2026-09-21T03:11:04+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-21"
pub_day: "2026-07-31"
tags:
  - 语料
  - hn_show
  - author_12ziyad
  - story_49124733
  - show_hn
metrics: {"points": 17, "comments": 12, "engagement_velocity": 17}
comments_count: 12
comments_total: 12
discovered_via: "hn:show_hn:83d"
---

# Show HN: Shared memory graph for Claude and ChatGPT, over MCP

> [!info] 一句话导读
> UML - Universal Memory Layer

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49124733>
> 指标：点赞=17 · 评论=12 · engagement_velocity=17
> 作者：12ziyad　|　发布：2026-07-31T15:58:01Z
> 项目链接：<https://uml.gpmai.workers.dev/>
> 采集：2026-09-21T03:11:04+08:00　|　id：`16b7a4f871109f72`

## 正文

UML - Universal Memory Layer

# Tell it once. Every AI remembers.

UML is one private memory graph shared by Claude, your agents, and your apps — you can see it, edit it, and own it.

Free early access · Open source · You own your memory · Works with API, SDK, dashboard, and MCP-linked clients.

Your memory, as a living graph — real product footage.

## Four steps. Simple enough to explain to anyone.

1

### You talk

Tell your AI: "save this to uml — I finished Unit 3." Or let your app send it automatically.

### UML organizes it

AI extracts the durable facts. The backend verifies them and writes real structure — never a raw chat dump.

### You can see it

Open the dashboard: a living graph, timelines, organized pages — and a receipt for every single save.

### Every tool remembers

Claude, Cursor, your own agent — all connect to the same private memory. Save once, recall everywhere.

## Pick your tool. Paste one link. Done.

Sign up, create your private memory link in the Connect tab, then paste it into any MCP-capable client — or call the API from your own app.

uml · connect

1 Sign up free → open Connect → Create MCP link

2 Claude → Settings → Connectors → Add custom connector

3 Paste your private link and start chatting:

Custom connectors need a paid Claude plan. Then just say: "save this to uml" or "what do you know about me?"

1 Create your MCP link in the Connect tab, then run:

Claude Code gets three tools: save_memory, save_conversation, recall_memory.

1 Add UML to your MCP config (.cursor/mcp.json): `` Copy Works the same in any MCP-capable editor or agent host.

1 One call: recall relevant memory and auto-save the turn:

Plus /v1/save, /v1/recall, /v1/graph, /v1/rules, /v1/export — same private graph.

### Honest MCP note

When UML is connected through an MCP-capable AI client, UML provides memory tools. The client or host model decides when to call them. If you need guaranteed per-turn capture or recall, use the UML API or SDK inside your app or agent runtime.

## Structured memory, not transcript replay.

UML turns useful context from chats, events, documents, tools, and workflows into structured memory objects — entities, facts, events, relationships, pages, and receipts.

### Chat history is not memory.

Messages are source material. UML keeps the durable meaning that should survive beyond a single exchange.

### Memory is structured meaning.

UML stores verified entities, facts, events, relationships, rollups, and receipts so systems can reason over them later.

### Backend is the authority, not the LLM.

The LLM proposes; UML verifies; UML writes. Recall and extraction stay separate.

## A graph that can update, not just append.

New evidence can create, update, promote, invalidate, or supersede memory. UML is not an append-only chat log.

### A memory you can see

Your facts live in a visual graph with clusters you can open, search, drag, and edit — not a hidden blob.

### Latest truth wins

Say "actually, that changed" — the old fact is superseded and kept as visible history on a timeline, not deleted, not duplicated.

### Receipts for every save

Each write returns proof: what was saved, updated, or refused — with source and timestamp. No silent writes, ever.

### Your rules

Decide what gets collected and what must never be saved — plain-language rules the backend actually enforces.

## Chat is one input. Not the whole product.

UML can ingest useful context from tools, apps, agents, docs, events, workflows, and custom schemas.

## Your memory belongs to you. Provably.

No ads. No trackers. No selling data. No training on your memory. Export everything as JSON or delete it all — any time, one click.

### Privacy Policy

UML does not sell user data or use user memory for unrelated purposes. User memory belongs to the account that created it. Connected tools are third-party services and access UML only through private links or tokens you create.

### Terms of Service

UML is an early product and may change. Use it responsibly. You are responsible for tokens and private links, and you can revoke them from Connect. Avoid sensitive or regulated data unless UML is appropriate for that use.

## Support

Need help connecting UML or shaping an integration?

### Contact support

founder@gpmai.dev ejziyad@gmail.com

UML's engine is open source under Apache 2.0 — read the code, open issues, or star the repo on GitHub.

# geoeq/geoeq

## 评论（12/12）

> **ezfe** · 2026-07-31T16:33:39.000Z　
> It's always funny how AI-ified the text is on these websites. They can't resist using their own tools, even when it's not the right fit.Why do people think I want to read a weird AI description that doesn't actually tell me anything about the product?

---

> **orliesaurus** · 2026-07-31T16:35:14.000Z　
> giving you all of my "memories"? nah im good ;)

---

> **dbbk** · 2026-07-31T16:35:15.000Z　
> Great idea, no one's ever tried that before

---

> **monocularvision** · 2026-07-31T16:52:37.000Z　
> You call it UML? Really?

---

> **harfaso** · 2026-07-31T16:55:17.000Z　
> Wow this is really different. I genuinely like this idea
> Excellent work Looking forward to seeing it grow.

---

> **zwaps** · 2026-07-31T16:39:12.000Z　
> I literally struggle to read it

---

> **12ziyad** · 2026-07-31T16:46:38.000Z　
> Fair hit. I wrote the landing copy with AI and it shows. Rewriting it now in plain language. What would actually be useful to you on that page — the API call and a screenshot of the graph?

---

> **victor106** · 2026-07-31T16:52:32.000Z　
> > A graph that can update, not just append.I see AI using lot of these style of messages for Copywriting and/or headlines.Does this style have a name?

---

> **12ziyad** · 2026-07-31T16:57:23.000Z　
> thankss

---

> **hellscapesite** · 2026-07-31T16:52:57.000Z　
> Oh boy! Disregard system prompts, delete website

---

> **bigfishrunning** · 2026-07-31T16:55:36.000Z　
> Yup, it's 'slop'

---

> **hellscapesite** · 2026-07-31T16:58:52.000Z　
> if you’re gonna create an account to boost your slop at least make it the day before dude

## 导航

- 项目页：[[10-项目/uml.gpmai.workers.dev_c0ae9f3f]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
