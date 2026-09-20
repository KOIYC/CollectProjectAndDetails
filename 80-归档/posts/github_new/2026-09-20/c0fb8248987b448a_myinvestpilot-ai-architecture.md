---
type: "corpus"
item_id: "c0fb8248987b448a"
title: "myinvestpilot/ai-architecture"
source: "github_new"
source_name: "GitHub 新星仓库"
url: "https://github.com/myinvestpilot/ai-architecture"
project_url: "https://myinvestpilot.com/"
author: "myinvestpilot"
published_at: "2026-02-14T13:51:46Z"
captured_at: "2026-09-20T09:16:35+08:00"
lang: "en"
kind: "post"
tags:
  - 语料
  - github_new
  - topic:indie-hacker
metrics: {"stars": 327, "forks": 30, "open_issues": 0}
comments_count: 0
comments_total: 0
discovered_via: "github:14d"
archived: true
archived_at: "2026-09-20T09:16:58+08:00"
archive_reason: "排除:无主题词"
---

# myinvestpilot/ai-architecture

- **来源**：GitHub 新星仓库　|　**kind**：post
- **原帖**：https://github.com/myinvestpilot/ai-architecture
- **指标**：stars=327 · forks=30 · open_issues=0
- **作者**：myinvestpilot　|　**发布**：2026-02-14T13:51:46Z
- **项目链接**：https://myinvestpilot.com/
- **采集**：2026-09-20T09:16:35+08:00　|　**id**：`c0fb8248987b448a`

## 正文

# AI-Native System Builder: MyInvestPilot Architecture Series

> **[中文版本 (Simplified Chinese)](README.zh.md)**

Public architecture notes from building [MyInvestPilot](https://www.myinvestpilot.com/) — an AI-native investment system built through AI-driven development, constrained DSL design, hybrid agents, and a cost-aware solo cloud stack.

## Why This Repo Exists

This repository is the external technical narrative of MyInvestPilot: design choices, trade-offs, and failures from building a production system where AI writes most implementation code.

It is **not**:
- a product user manual (that belongs to product docs)
- an internal AI blueprint repo (used for private planning/execution)
- a generic prompt cookbook

The goal is straightforward: document what it actually takes to operate as an **AI-native system builder**, not just ship demos.

## The Series

### 01. Engine
**[From Rule-Based Scripts to AI-Native Engines: Why I Built a Constrained DSL](docs/01_ai_native_primitives_engine.md)**

How constrained IR (JSON DSL), schema-driven contracts, and deterministic execution work together for reliable decision systems.

### 02. Methodology
**[Why I Stopped Writing Code: The 60/40 Rule for AI-Native Engineering](docs/02_ai_driven_development.md)**

How AI-driven solo development evolved from 60/40 alignment/execution toward 90/10 in many cycles, with human quality gates still mandatory.

### 03. Agent Architecture
**[The Agent Paradox: Why We Built a "Boring" Hybrid Architecture](docs/03_hybrid_agent_architecture.md)**

Why we split Local Agent (flexible orchestration) and Remote Agent (deterministic async processing) instead of relying on a single autonomous agent.

### 04. Cloud Infrastructure
**[Running a Multi-Vendor, Event-Driven Cloud Architecture as a Solo Builder](docs/04_solo_company_infrastructure.md)**

How a multi-vendor, async-first, serverless-friendly stack supports real usage with low operational cost.

## Blog Publication

A synthesized version of this series was published on the author's blog:

**[How I Built an AI-Native Quantitative System](https://www.bmpi.dev/dev/ai-native-investment-system/)** — bmpi.dev

This post distills the key architectural decisions across all four parts: constrained DSL design, schema supply chain, prompt evolution, and the hybrid agent paradox.

## Audience

This repo is for builders working on:
- AI-native application architecture
- agent systems with reliability boundaries
- cloud-native/serverless systems for solo teams

## About

I'm Dawei ([@madawei2699](https://twitter.com/madawei2699)), an independent builder.
I previously shipped [myGPTReader](https://github.com/myreader-io/myGPTReader) and [invest-alchemy](https://github.com/myinvestpilot/invest-alchemy), which later evolved into MyInvestPilot.

## License

MIT

## 关联链接

- https://www.myinvestpilot.com/
