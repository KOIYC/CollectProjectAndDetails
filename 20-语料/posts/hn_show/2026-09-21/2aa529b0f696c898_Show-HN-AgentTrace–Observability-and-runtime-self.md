---
type: "corpus"
item_id: "2aa529b0f696c898"
title: "Show HN: AgentTrace–Observability and runtime self-healing engine for AI agents"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49780222"
project_url: "https://github.com/mohitkumar188/AgentTrace"
author: "mohitkumar18"
published_at: "2026-09-20T21:24:17Z"
captured_at: "2026-09-21T09:44:03+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-21"
pub_day: "2026-09-20"
tags:
  - 语料
  - hn_show
  - author_mohitkumar18
  - story_49780222
  - show_hn
metrics: {"points": 4, "comments": 0, "engagement_velocity": 4}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:3d"
---

# Show HN: AgentTrace–Observability and runtime self-healing engine for AI agents

> [!info] 一句话导读
> mohitkumar188/AgentTrace

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49780222>
> 指标：点赞=4 · 评论=0 · engagement_velocity=4
> 作者：mohitkumar18　|　发布：2026-09-20T21:24:17Z
> 项目链接：<https://github.com/mohitkumar188/AgentTrace>
> 采集：2026-09-21T09:44:03+08:00　|　id：`2aa529b0f696c898`

## 正文

# mohitkumar188/AgentTrace

- Stars: 1
- Forks: 0
- Watchers: 1
- Open issues: 0
- Homepage: https://agent-trace-zeta.vercel.app
- Default branch: main
- Created: 2026-09-06T11:07:22Z

## Languages

- CSS
- JavaScript
- Python
- TypeScript

## Top Contributors

- mohitkumar188 (7 contributions)

---

## README

# ⚡ AgentTrace: Production-Grade Agent Observability & Self-Healing Engine
Live Dashboard
Backend API
License: MIT

> **Live Production Demo:**
> * 🖥️ **Interactive Web Dashboard:** https://agent-trace-zeta.vercel.app/
> * ⚙️ **FastAPI Swagger Docs:** https://agenttrace-api-cdav.onrender.com/docs

An end-to-end observability SDK and dashboard for autonomous AI agent pipelines. It monitors multi-step tool calls, visualizes latency bottlenecks, and automatically repairs malformed LLM tool arguments at runtime without crashing workflows.

---

## 🎯 The Problem
LLMs frequently hallucinate tool arguments during multi-step runs:
* Passing strings instead of floats (e.g. `"1200 INR"` instead of `1200.0`)
* Inventing key names (e.g. `"user_identifier"` instead of `"user_id"`)
* Omitting required schema fields

Normally, these cause immediate runtime crashes. AgentTrace catches these failures and auto-repairs them at runtime.

---

## 💡 Architecture & Tech Stack
* **Decorator SDK:** Python, Pydantic (Validates schema before tool run)
* **Self-Healing Layer:** Fast inference via Groq to repair payloads on failure
* **Collector Backend:** FastAPI with SQLite persistence (`traces.db`)
* **Live Dashboard:** Next.js, Tailwind CSS with Payload Diff Inspector

---

## 🚀 How to Run Locally

### 1. Start Backend
```bash
# In project root
python -m uvicorn main:app --reload --port 8000

# sumanmichael/jevlang

## 关联链接

- https://agent-trace-zeta.vercel.app
- https://agent-trace-zeta.vercel.app/
- https://agenttrace-api-cdav.onrender.com/docs

## 导航

- 项目页：[[10-项目/github.com_d104c4f6]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
