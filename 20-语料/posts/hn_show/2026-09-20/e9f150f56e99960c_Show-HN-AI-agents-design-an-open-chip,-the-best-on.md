---
type: "corpus"
item_id: "e9f150f56e99960c"
title: "Show HN: AI agents design an open chip, the best one gets fabricated"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49753045"
project_url: "https://neruva.io/"
author: "kyleclouthier"
published_at: "2026-09-18T11:51:21Z"
captured_at: "2026-09-20T09:36:40+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-20"
pub_day: "2026-09-18"
tags:
  - 语料
  - hn_show
  - author_kyleclouthier
  - story_49753045
  - show_hn
metrics: {"points": 2, "comments": 0, "engagement_velocity": 2}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:90d"
---

# Show HN: AI agents design an open chip, the best one gets fabricated

> [!info] 一句话导读
> Neruva — The deterministic memory substrate I built for my own work

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49753045>
> 指标：点赞=2 · 评论=0 · engagement_velocity=2
> 作者：kyleclouthier　|　发布：2026-09-18T11:51:21Z
> 项目链接：<https://neruva.io/>
> 采集：2026-09-20T09:36:40+08:00　|　id：`e9f150f56e99960c`

## 正文

Author: Neruva

Neruva — The deterministic memory substrate I built for my own work

# The deterministic memory I built for my own agents.

Neruva is the custom memory & grounding substrate I run across everything I build — Cairn, SimGen, FavourBee, and my day-to-day operations — through Claude Code MCP. A records store, a knowledge graph, and deterministic snapshot/replay: reproducible, auditable recall where the same query gives the same answer and every decision can be replayed. Built for my own work first and proven there daily — open to serious pilot and licensing conversations.

Runs on Claude Code MCP · ~25 tools over api.neruva.io · live demo on request

your-agent · terminal

```
# how my agents remember — one substrate, every project
$ claude mcp add neruva

# remember once, recall deterministically — anywhere
agent_remember("Kai's tenant lease ends 2026-03-31")
agent_recall("when does Kai's lease end?")
→ 2026-03-31  ·  cited · same answer every run
```

25 tools one MCP server Replay bit-identical from seed Cited provenance on every answer Forget GDPR / Law 25 atomic

## Memory you can reproduce — and audit

The split is deliberate: the server is a deterministic substrate — storage, retrieval math, provenance, counts — while meaning and judgment stay with your agent. That boundary is what makes recall reproducible, corrections enforceable, and every decision replayable. The same trait that makes a cryptographic receipt verifiable, applied to memory.

## "Reproduce the flagged decision."

Every serious agent deployment gets asked this eventually — by a regulator, an auditor, or a customer. Logs show what an agent output. Almost none can show what it knew when it decided, or replay the decision faithfully. With EU AI Act high-risk enforcement live and MCP still lacking a standard audit trail, that gap is now a compliance problem, not a curiosity.

1

### Commit

Each agent action signs a record committing to the SHA-256 of the exact context it read.

2

### Store

The context lives in Neruva, content-addressed — the address is the hash, verified server-side on write.

3

### Fetch

An auditor, knowing only the committed hash, fetches the exact bytes back. A corrupted store read fails closed.

4

### Replay

The decision re-runs against the restored context and must reproduce the committed output byte-for-byte.

Proven on the live API with two independent agents: one agent's decision was reproduced and audited by a second agent that held nothing but the hash — byte-for-byte, no shared state — and an agent-driven tamper failed closed. Authority (who authorized the agent) is verified by the offline verifier from Cairn. Named limit: byte-for-byte replay covers deterministic decisions; LLM actions require committing model, parameters, and prompt as context.

## Seven layers, one substrate

Everything an agent needs to remember well — exposed as MCP tools over api.neruva.io. The newest is replayable agent audit.

### Records store

Append-only typed events with semantic + BM25-RRF recall. Ingest, query, timeline, compact, export to a portable .neruva file. The substrate auto-embeds text server-side.

### Agent recall

agent_remember / agent_recall / agent_context — federated retrieval across records and the knowledge graph, with cross-session fan-out and a paste-ready context block.

### Knowledge graph

Subject–relation–object triples with temporal validity. Exact multi-hop neighbors, reverse lookups ("who controls X?"), and corrections via replace-fact that keep the prior state as history.

### Deterministic replay

Snapshot a namespace to an immutable blob and restore it bit-for-bit from a seed. Time-travel queries against historical state — the same inputs always reproduce the same answer.

### Enforce-deny corrections

Tell it a fact is wrong once and the correction is enforced — recalled before extraction and injected as a mandatory override. Not retrained. It does not recur.

### Atomic forget

GDPR / Quebec Law 25 deletion: forget records by kind/tag/time/user, or hard-delete every fact about an entity in both directions — cleanly, with the audit trail intact.

### Replayable agent audit

Content-addressed context store: an agent action commits to the hash of what it read, and any flagged decision is reproduced byte-for-byte from the exact memory it was made with — the newest layer, detailed above.

## One substrate, behind everything I do

My projects and operations share a single memory layer — so decisions, corrections, and history carry across all of them, and I can replay any of it.

## Built for my own stakes. Open to yours.

# Guia.Social — Travel recommendations from people you trust

## 导航

- 项目页：[[10-项目/neruva.io_6218b8d1]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
