---
type: "corpus"
item_id: "ec154dc17c078c2d"
title: "Show HN: I built flightdeck – Observability and control plane for AI agents"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50263709"
project_url: "https://flightdeck-hq.com/"
author: "pykul"
published_at: "2026-10-27T18:34:12Z"
captured_at: "2026-10-28T09:39:16+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-10-28"
pub_day: "2026-10-27"
tags:
  - 语料
  - hn_show
  - author_pykul
  - story_50263709
  - show_hn
metrics: {"points": 2, "comments": 0, "engagement_velocity": 2}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:3d"
---

# Show HN: I built flightdeck – Observability and control plane for AI agents

> [!info] 一句话导读
> Self-hosted · Apache 2.0

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50263709>
> 指标：点赞=2 · 评论=0 · engagement_velocity=2
> 作者：pykul　|　发布：2026-10-27T18:34:12Z
> 项目链接：<https://flightdeck-hq.com/>
> 采集：2026-10-28T09:39:16+08:00　|　id：`ec154dc17c078c2d`

## 正文

Quickstart
 Releases
 GitHub ★
Self-hosted · Apache 2.0 · Production and coding agents
Observability and control plane for AI agent fleets .
Every LLM call, MCP event, and tool call your agents make streams to the dashboard as it happens,
 surfaced as a per-agent timeline and as a live fleet-wide feed.
 Set token budgets, MCP allow/block rules, and live directives on your production agents.
View on GitHub
 Quickstart
Coding agents attach via the Claude Code plugin .
Production agents add the flightdeck-sensor Python package to their entrypoint: init() + patch() , no other code changes.
Fleet view Streaming Paused
research-agent
support-triage
claude-code · omri
etl-summarizer
llm_call
 tool_use
 mcp_event
 policy_warn / degrade
 policy_block / kill
One row per agent, sub-agents nested under their parents, events plotted as they arrive. Hover any event to inspect it; hovering pauses the stream.
What it does
Live fleet view
Every agent on a shared timeline: LLM calls, embeddings, tool uses, MCP events, and structured errors, streamed as they happen. Click any event to inspect it.
Budgets that act
Central token budgets per flavor, enforced in-process. Warn at 80%, swap to a cheaper model at 90%, block at 100%. Defaults, all configurable, every decision a structured event.
Kill switch and directives
Stop one agent or an entire flavor from the dashboard; the signal delivers on the agent's next call. Register custom directives in Python and invoke them remotely.
MCP protection
Allowlist or blocklist the MCP servers your agents may talk to, per flavor. Misconfigured or unrecognized servers warn or block before the call leaves the process.
Sub-agent trees
Multi-agent runs render as a tree: orchestrator parent, one child session per sub-agent, linked and labeled by role. Claude Code tasks, CrewAI agents, LangGraph nodes.
Analytics and cost
Token consumption, latency, model distribution, policy volume, and estimated cost, grouped by flavor, model, framework, host, team, or role.
Architecture
Not a proxy. The sensor wraps SDK clients inside your agent's own process: init() + patch() , no other code changes, and calls go straight to the provider. Prompt capture is off by default in the sensor; the Claude Code plugin captures your own session by default and can be turned off.
Anthropic
 OpenAI
 litellm
 LangChain
 LangGraph
 LlamaIndex
 CrewAI
 bifrost
 Claude Code
 MCP
On the dashboard
Live fleet view Streaming Expand ⤢
The live fleet feed. Agents, events, run boundaries, and policy decisions on one shared clock.
Agents Expand ⤢
Every agent with token, latency, error, and cost trends, plus a per-agent drawer and swimlane.
Events Expand ⤢
Filter every event by agent, type, framework, model, or MCP server. Click through to the run.
Quickstart
Coding agents
Inside Claude Code, install the plugin from the repo's marketplace:
/plugin marketplace add flightdeckhq/flightdeck
/plugin install flightdeck@flightdeck-plugins
/reload-plugins
 Copy
Production agents
Add the sensor to your entrypoint. Nothing else changes:
# pip install flightdeck-sensor
import flightdeck_sensor
flightdeck_sensor.init(server="...", token="...")
flightdeck_sensor.patch()
 Copy
Run the stack itself with git clone https://github.com/flightdeckhq/flightdeck && cd flightdeck && make dev , dashboard on localhost:4000 . Docker Compose and a Helm chart cover production. Full walkthrough in the README .
Built and maintained by Omri Arnon · LinkedIn
 Apache 2.0 · github.com/flightdeckhq/flightdeck
Close ✕
Esc or click outside to close

## 关联链接

- https://github.com/flightdeckhq/flightdeck

## 导航

- 项目页：[[10-项目/flightdeck-hq.com_00462fe2]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
