---
type: "corpus"
item_id: "4ffbd45875966e4e"
title: "Show HN: Async multi-agent coordination across physical environments"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49714247"
project_url: "https://github.com/BlahBlah23406/agent-comms"
author: "BlahBlah23406"
published_at: "2026-09-15T15:40:45Z"
captured_at: "2026-09-20T14:06:07+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-20"
pub_day: "2026-09-15"
tags:
  - 语料
  - hn_show
  - author_BlahBlah23406
  - story_49714247
  - show_hn
metrics: {"points": 3, "comments": 2, "engagement_velocity": 3}
comments_count: 2
comments_total: 2
discovered_via: "hn:show_hn:90d"
---

# Show HN: Async multi-agent coordination across physical environments

> [!info] 一句话导读
> BlahBlah23406/agent-comms

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49714247>
> 指标：点赞=3 · 评论=2 · engagement_velocity=3
> 作者：BlahBlah23406　|　发布：2026-09-15T15:40:45Z
> 项目链接：<https://github.com/BlahBlah23406/agent-comms>
> 采集：2026-09-20T14:06:07+08:00　|　id：`4ffbd45875966e4e`

## 正文

# BlahBlah23406/agent-comms

A comprehensive, production-grade protocol and toolkit enabling AI coding agents to communicate, share work, and transfer mental models across different sessions and physical computers

- Stars: 1
- Forks: 0
- Watchers: 1
- Open issues: 0
- Default branch: master
- Created: 2026-09-10T13:47:31Z

## Languages

- PowerShell
- Python
- Shell

---

## README

# Agent Comms

Tests
Python 3.9+
License: MIT

> A lightweight protocol and toolkit for AI coding agents to share context, hand off tasks across sessions, and collaborate in real-time across machines.

---

## What It Is

When working with AI coding agents (Claude Desktop, Antigravity, Cursor, etc.), two major challenges arise:
1. **Context Loss Across Sessions:** Starting a new chat or moving to another machine resets the agent's mental model and working memory.
2. **Multi-Agent Coordination:** Agents running in different environments or physical computers cannot easily communicate, exchange state, or run coordinated tasks.

**Agent Comms** provides a unified solution:
- **Context Capsules (Out-of-Session Handoff):** Packages an agent's task roadmap, architectural decisions, rejected hypotheses, and uncommitted git diffs into a compact, portable bundle. The next agent session resumes immediately without burning context tokens.
- **AHRP Live Relay (In-Session Collaboration):** A real-time WebSocket mesh supporting peer discovery, publish/subscribe messaging, and cross-machine Remote Procedure Calls (RPC).
- **Native MCP Integration:** Works out-of-the-box with Claude Desktop, Antigravity, and Cursor via the Model Context Protocol.

---

## How It Works

### 1. Out-of-Session Handoff (Context Capsules)
Agent Comms captures cognitive state alongside your working tree without polluting Git commit history:
- **State & Decisions:** Records what worked, what was rejected, and the immediate next steps.
- **Code Diffs:** Captures staged, unstaged, and untracked changes into a clean patch.
- **Briefing Generation:** Produces a token-efficient Markdown briefing tailored for the incoming agent.

```
Machine A (Active Session)                  Machine B (New Session)
 ┌──────────────────────────┐                ┌──────────────────────────┐
 │ Agent exports capsule    │──[File/Sync]──▶│ Agent imports capsule    │
 │ (diffs + state + roadmap)│                │ (restores diffs + state) │
 └──────────────────────────┘                └──────────────────────────┘
```

### 2. In-Session Collaboration (Live Relay Mesh)
For multi-agent workflows, a lightweight relay server coordinates agents over WebSockets:
- **Peer Discovery:** Agents announce presence, roles, and hardware capabilities.
- **Cognitive Blackboard:** Replicated state where agents share real-time decisions and learnings.
- **Direct RPC:** Agents can invoke tools or run commands on peer machines.

---

## How to Get It

### Installation

**Using Pip:**
```bash
pip install git+https://github.com/BlahBlah23406/agent-comms.git
```

**Or Clone & Install Locally:**
```bash
git clone https://github.com/BlahBlah23406/agent-comms.git
cd agent-comms
pip install -e .
```

**One-Line Install Script:**
- **macOS / Linux:**
  ```bash
  curl -sSL https://raw.githubusercontent.com/BlahBlah23406/agent-comms/master/install.sh | bash
  ```
- **Windows (PowerShell):**
  ```powershell
  irm https://raw.githubusercontent.com/BlahBlah23406/agent-comms/master/install.ps1 | iex
  ```

Run initial setup:
```bash
agent-comms setup
```

---

## Quick Usage

### 1. Save Progress (Create a Capsule)
Before ending a session or switching computers:
```bash
agent-comms capsule pack \
  --task "AUTH-01" \
  --summary "Migrated auth module to JWT; integration test pending" \
  --next "Run pytest tests/test_auth.py" \
  --learning "finding:PyJWT requires algorithms=['HS256']"
```

### 2. Resume on Another Machine
Restore your uncommitted files and task briefing:
```bash
agent-comms capsule unpack "AUTH-01"
```

### 3. Run the Live Collaboration Demo
See two local agents discover each other and collaborate:
```bash
agent-comms demo
```

### 4. Use in Claude Desktop, Antigravity, or Cursor (MCP)
Agent Comms includes an MCP server exposing `export_handoff_capsule`, `import_handoff_capsule`, and `list_saved_capsules`.

Add to your MCP settings file:
```json
{
  "mcpServers": {
    "agent-comms": {
      "command": "agent-comms",
      "args": ["mcp"]
    }
  }
}
```

Once added, interact naturally with your agent:
> *"Save my progress into a handoff capsule for task AUTH-01."*
> *"Resume task AUTH-01 from my latest capsule."*

---

## Documentation

- **Natural Language User Guide** (`USER_GUIDE.md`) — Plain-English prompt examples for Claude Desktop, Antigravity, and Cursor.
- **Onboarding Guide** (`ONBOARDING.md`) — Step-by-step developer onboarding and distributed agent recipes.
- **Protocol Specification** (`SPECIFICATION.md`) — Formal AHRP wire protocol and JSON schemas.
- **Tutorial & Recipes** (`TUTORIAL.md`) — Hands-on walkthroughs and implementation examples.

# jit · just-in-time passwords for developer endpoints

## 评论（2/2）

> **arpanghoshal** · 2026-09-15T16:05:12.000Z　
> good one!

---

> **BlahBlah23406** · 2026-09-15T23:55:21.000Z　
> thanks a lot man

## 关联链接

- https://github.com/BlahBlah23406/agent-comms.git
- https://raw.githubusercontent.com/BlahBlah23406/agent-comms/master/install.ps1
- https://raw.githubusercontent.com/BlahBlah23406/agent-comms/master/install.sh

## 导航

- 项目页：[[10-项目/github.com_28fc3032]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
