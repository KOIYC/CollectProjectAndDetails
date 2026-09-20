---
type: "corpus"
item_id: "4d0ab0b69f67a2e3"
title: "Show HN: MCPJam - the first testing & evaluations platform for MCP servers"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49745351"
project_url: "https://mcpjam.com/"
author: "prathmeshmcp"
published_at: "2026-09-17T19:23:47Z"
captured_at: "2026-09-20T14:02:55+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-20"
pub_day: "2026-09-17"
tags:
  - 语料
  - hn_show
  - author_prathmeshmcp
  - story_49745351
  - show_hn
metrics: {"points": 11, "comments": 6, "engagement_velocity": 11}
comments_count: 6
comments_total: 6
discovered_via: "hn:show_hn:90d"
---

# Show HN: MCPJam - the first testing & evaluations platform for MCP servers

> [!info] 一句话导读
> MCPJam — MCP server testing, debugging & evals

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49745351>
> 指标：点赞=11 · 评论=6 · engagement_velocity=11
> 作者：prathmeshmcp　|　发布：2026-09-17T19:23:47Z
> 项目链接：<https://mcpjam.com/>
> 采集：2026-09-20T14:02:55+08:00　|　id：`4d0ab0b69f67a2e3`

## 正文

Author: MCPJam

MCPJam — MCP server testing, debugging & evals

# Test your MCP server against every major AI client.

From your first prompt to a continuous gate on every release, MCPJam shows what breaks across every AI client, and how to fix it.

Test against

+10

Capability

Claude

ChatGPT

Cursor

Cline

Client capabilities supported

Roots 3/6 Supported Not supported Not supported Partial Supported Supported

Sampling 1/6 Supported Not supported Not supported Not supported Partial Not supported

Elicitation 3/6 Supported Not supported Partial Supported Supported Not supported

Experimental 2/6 Partial Not supported Supported Not supported Supported Not supported

Skills over MCP 0/6 Not supported Not supported Not supported Not supported Not supported Not supported

Host policy

Task execution 0/6 — — — — — —

Tool confirmation 4/6 Supported Partial Supported Supported Supported Partial

supported partial MCP 2025-11-25

Know exactly which MCP capabilities work in every major client.

Teams shipping MCP servers test with MCPJam

Read case study Read case study

Read case study

Developers test on MCPJam

92,000+

Enterprises rely on MCPJam

280+

Open-source contributors

150+

MCP servers tested

42,000+

Data current as of August 2026 · Updated monthly

## After the coding agent. Before your users.

Make reliability evals, security, and protocol compliance required checks in your own pipeline. Your build ships when it clears the bar you set. Every run makes the next one stronger.

stdio · http Your app MCP server 14 tools · 2 prompts

MCP Jam Pre-production gate

Run 128

Reliability Pass Security Pass Self-improvement Running Protocol compliance Pass

Elapsed 00:38 4/5 ready

ChatGPT 94% Pass

Claude 89% Pass

Microsoft Copilot Blocked

↳ Fix: Add tool output schema

Gemini 91% Pass

Cursor 86% Pass

## Test it the way your users' agents will.

Share with human QA or agent personas, watch multi-turn journeys flow from goal to sentiment, then turn clustered failures into ranked fixes before you ship.

MCPJam · Playground

pizzaz HTTP 5 tools

pizza-map pizza-list pizza-shop

Claude

pizza-map

Mapped 6 pizzerias:

- • Tony's 4.8
- • Golden Boy 4.7
- • Little Star 4.6
- • Del Popolo 4.6
- • Delfina 4.5
- • Casey's 4.5

1.1s · 1 tool call

ChatGPT

pizza-map

Here are 6 top spots:

- • Tony's 4.8
- • Golden Boy 4.7
- • Little Star 4.6
- • Del Popolo 4.6
- • Delfina 4.5
- • Casey's 4.5

1.4s · 1 tool call

Copilot

pizza-map

Found 6 places nearby:

- • Tony's 4.8
- • Golden Boy 4.7
- • Little Star 4.6
- • Del Popolo 4.6
- • Delfina 4.5
- • Casey's 4.5

1.7s · 1 tool call

Show pizza places in San Francisco

### Run one prompt across every model, side by side.

| Client | Tools | Resources | Prompts | Elicit |
| --- | --- | --- | --- | --- |
| ChatGPT | | | | |
| Claude | | | | |
| Cursor | | | | |
| Copilot | | | | |
| Works | 4/4 | 4/4 | 3/4 | 3/4 |

 works degraded testing now

Client matrix

### Know exactly what works in every client.

Nightly · all personas 15 sessions · 32 traces

Human QA 12 sessions

Share with internal QA and beta testers

Agent personas 32 traces

Swarm runs multi-turn journeys nightly

CC CU GP Goal → behavior → outcome → sentiment

User acceptance testing

### Human QA and agent personas run the same journeys your users take.

4 root causes · projected 89%

Cluster failures, rank fixes, apply with one click

71%

89%

after applying top fix · +11 pts accuracy

Clarify list_charges result reuse

tool description · Cursor · conf 0.92

Require charge_id on create_refund

schema · cases 02, 04 · conf 0.88

system prompt · strict-order cases · conf 0.71

Truncate large results server-side

server config · 4/56 failures · conf 0.54

### Cluster failures, rank fixes, and apply the highest-impact change.

refund-flow claude-sonnet-5 · 3 turns · 2 tools · 1,284 tokens

user Refund order #4821 back to the original card.

assistant get_order create_refund{ order_id: 4821, amount: 129.00 }

result refund re_88213 created — $129.00 to visa ···4242

Checks 3 / 3 checks

- called create_refund exactly once
- refund amount equals order total
- no destructive tools invoked

All checks have passed

3 successful checks

mcpjam/evals— 24 cases · 96% accuracy Details mcpjam/security— 0 findings Details mcpjam/conformance— MCP 2025-11-25 Details

This branch has no conflicts with the base branch

Merging can be performed automatically.

Merge pull request

## Trusted by teams building for agents.

How teams use MCPJam to ship MCP servers with confidence.

Case study · Web MCP

Bright Data made MCPJam the official evaluation CLI for Web MCP, catching regressions before tool changes ship.

Case study · Enterprise MCP

Asana uses MCPJam every day to test MCP servers locally and in CI, without deploying for every prompt.

### Where does MCPJam fit in my stack?

In the pre-production layer between build and production, and we're SDK and framework agnostic, so we work with any MCP server however you built it. We don't instrument your code or your live traffic. We exercise your server the way real AI clients do, during dev, QA, beta, and CI/CD, because that's the window where every failure mode is still visible and cheap to fix. Once it ships into an external agent it's a black box, so the highest-value reliability work happens just before that line, which is exactly where we live.

### MCP evals vs. agent evals: what's the difference?

Agent eval and observability tools (Datadog, Braintrust, LangSmith, Arize) measure the agent you built, in a system you control that already sees the user's prompt, context, and tool calls. MCP evals measure the other side of the handshake: how your software behaves when an external agent you don't control (ChatGPT, Claude, Copilot, Cursor) decides whether to call it, with what arguments, and how it uses the result. MCPJam sits outside your system and confirms your software is production-ready for every external agent, before your users ever interact with it.

### Is it open source? Is it free?

The core is open source and free, forever: the client, Inspector, core CLI and SDK, local evals, and conformance checks, to run locally or in your own CI/CD.

Paid plans are for when your team is ready to go further:

- Live client matrix: test against continuously maintained emulations of every AI client, kept current for you so a host change never quietly breaks your tests.
- Swarm: turn loose AI agent personas that acceptance-test your software at scale.
- Chatboxes: hosted, shareable UAT environments that capture and replay every human tester session.
- AI insights: root-cause diagnosis and fix suggestions, drawn from reliability patterns across thousands of MCP servers.
- Reporting & history: team dashboards and trends across every run and release.
- Enterprise governance: SSO, audit logs, DPA, and SOC 2 (Type 2 in-progress).

### Do you touch my production traffic?

No, we are strictly pre-production. There may be an ability in the future to import traces of production traffic to bolster session data and provide better insights for you, but for now we're strictly pre-production, where we believe you can get more reliable telemetry anyway given external agents unreliably offer you production user insights.

### Do I have to keep up with every AI client myself?

No, that's the point. ChatGPT, Claude, Gemini, Cursor, Slack and the rest each support different things and change constantly. MCPJam maintains the current behavior of all of them, so your tests reflect what your users experience today without your team tracking a single client.

### How do you test something non-deterministic?

With evaluation, not assertions. MCPJam scores whether the agent selected the right tool, sent the right arguments, and completed the job across runs and clients, then diagnoses why a score dropped and what to change, so erratic behavior becomes a metric you can gate on.

### What is Swarm?

Acceptance testing run by AI agents that act like your users. You define personas; a swarm runs multi-turn journeys through your server across every client and surfaces where it fails the job, continuously and before launch.

### What are Chatboxes?

Secure, isolated UAT environments: a shareable web client that mirrors the major AI hosts, so internal QA and beta testers can break things safely, and their real sessions become regression tests automatically.

Ship knowing it works for every user, in every client.

# Key Jump - Chrome Web Store

## 评论（6/6）

> **vigjam** · 2026-09-17T19:34:03.000Z　
> love the direction, but the problem for me has been about creating stronger evals and knowing what I should be checking for. does this help me understand that?

---

> **amgutier** · 2026-09-17T21:36:10.000Z　
> how are you planning to stay compliant with the exploding number of clients users will have in practice? Or do you not think the number of clients is going to balloon?

---

> **briefrrapp** · 2026-09-18T03:35:02.000Z　
> We have been a happy user of mcpjam! Excited to see the product add more capabilities!

---

> **1ClawAI** · 2026-09-18T18:56:11.000Z　
> How would this work the our MCP? docs.1claw.co

---

> **prathmeshmcp** · 2026-09-17T23:12:53.000Z　
> yeah, in my blog on Effective MCP (https://www.mcpjam.com/blog/effective-mcp-part-1) I introduce this framework called the "User-Value Chain" that essentially breaks down the full client-server request flow into distinct stages.You want to test the full request flow between client and server: connection, tool discovery, tool selection, calls, responses, and whether the user’s GOAL was actually achieved.What's hard: an external agent sits between your user and your MCP server, in a client you don't control (ChatGPT, claude etc.). Your tests need to cover how that client and agent find and uses your tools.Recommend checking for :- (deterministic assertions + non-deterministic judge checks) at essentially every stage of the request flow from client->server (User Value Chain)- across many clients where YOUR target users are at (unfort. these clients change behavior every other day) and across harness + models- our default eval assertions cover things like input schemas, valid arguments, repeated calls, errors, latency, and response size; pair those deterministic checks with non-deterministic evals for tool choice, response interpretation, and task completion.

---

> **prathmeshmcp** · 2026-09-17T23:10:16.000Z　
> yeah the # of clients will definitely increase, we'll start by looking to stay up to date with major AI clients as best we can, see caniuse.dev for diffs in client capabilitiesWe also think giving people completely configurable clients is extremely valuable, we keep these client "templates" up to date with the latest capabilities- but folks can certainly change up protocol/extension capabilities beyond that e.g. if Copilot is planning to support more apps capabilities in the coming weeks, use the Copilot template and toggle on more MCP apps endpoints to see if you're able to make use of them

## 导航

- 项目页：[[10-项目/mcpjam.com_01b5ab5d]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
