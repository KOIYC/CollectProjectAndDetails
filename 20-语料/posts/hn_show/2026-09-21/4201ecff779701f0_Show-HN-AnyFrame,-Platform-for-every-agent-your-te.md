---
type: "corpus"
item_id: "4201ecff779701f0"
title: "Show HN: AnyFrame, Platform for every agent your team builds"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=48343749"
project_url: "https://anyframe.dev/"
author: "inishchith"
published_at: "2026-05-31T07:23:40Z"
captured_at: "2026-09-21T02:52:48+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-21"
pub_day: "2026-05-31"
tags:
  - 语料
  - hn_show
  - author_inishchith
  - story_48343749
  - show_hn
metrics: {"points": 3, "comments": 0, "engagement_velocity": 3}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:144d"
---

# Show HN: AnyFrame, Platform for every agent your team builds

> [!info] 一句话导读
> AnyFrame Product Blog Changelog Docs FAQ

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=48343749>
> 指标：点赞=3 · 评论=0 · engagement_velocity=3
> 作者：inishchith　|　发布：2026-05-31T07:23:40Z
> 项目链接：<https://anyframe.dev/>
> 采集：2026-09-21T02:52:48+08:00　|　id：`4201ecff779701f0`

## 正文

AnyFrame Product Blog Changelog Docs FAQ
 Sign in
Platform for every agent
 your team builds.
 Spin up swarms of agents in minutes, for any use case, on any harness. For internal tools or customer-facing products.
 Start Building Book a demo
 AnyFrame
 A AnyFrame Inc TEAM
 + New agent BUILD
 Dashboard
 Sessions
 Agents
 Templates
 CONNECT
 Connections
 Credentials
 Agents
 New agent
 NAME TEMPLATE RUNTIME UPDATED
 No agents yet — create your first one.
Slack Discord GitHub + Many more
Any agent. Any team.
 Any tool.
 Engineering, sales, ops, support — each team wires up its own agent inside the tools it already uses.
0 1
 Any harness, swappable
 Claude Code, Cursor, Codex — switch anytime, everything else stays.
 A @anyframe forager/web
 Trigger @anyframe on PRs and issues
 Harness Claude Code Codex Cursor OpenCode Gemini CLI Claude Managed Agents soon Gemini Managed Agents soon
Sandbox fresh Ubuntu + repo · 4 vCPU
 booting Booting harness claude-code …
0 2
 Triggered where you work
 A message, ticket, or PR comment kicks off the same agent.
 #deploys · Slack 2m ago
 Maya P. 10:48
 @anyframe roll back the deploy. ingest worker is paging.
 A AnyFrame · Rolling back to v2.13.1 queued
FOR-128 · Linear IN PROGRESS Eng just now
 Fix p99 latency on /v1/search
 theo : @anyframe take this, there's a flamegraph attached.
 A AnyFrame · Ingested ticket, attached flamegraph queued
forager/web · PR #482 · GitHub 1m ago
 theo commented on src/search/index.ts
 @anyframe write tests for the new edge cases here, especially empty queries.
 A AnyFrame · Reading PR diff, writing tests queued
Slack Discord Linear GitHub Jira + many more
0 3
 It has hands and eyes
 Not just tool calls. It clicks through a real browser like a person.
 D @anyframe upgrade Acme Inc to Enterprise, 20 seats
 Desktop live
 Applications 04:41 root
 Northwind · Chromium
 app.northwind.io/billing
 Acme Inc cus_4f2a
 Plan Pro
Seats 12
Opening Acme's billing page
No API needed. It just uses the screen.
0 4
 Describe it, get a preview
 Product describes the page; the agent ships a working URL.
 slack · #marketing-site · thread 3 in thread
 A Aja S. just now
 @anyframe update the hero to focus on enterprise, and add a testimonial section under "Pricing".
A AnyFrame AGENT just now
 On it. Updating the hero copy and inserting a testimonial section. I'll use the existing card pattern from /customers .
Live preview updating for 3 collaborators on this thread
From a Slack message to a working preview.
A @anyframe forager/web
 Trigger @anyframe on PRs and issues
 Harness Claude Code Codex Cursor OpenCode Gemini CLI Claude Managed Agents soon Gemini Managed Agents soon
Sandbox fresh Ubuntu + repo · 4 vCPU
 booting Booting harness claude-code …
#deploys · Slack 2m ago
 Maya P. 10:48
 @anyframe roll back the deploy. ingest worker is paging.
 A AnyFrame · Rolling back to v2.13.1 queued
FOR-128 · Linear IN PROGRESS Eng just now
 Fix p99 latency on /v1/search
 theo : @anyframe take this, there's a flamegraph attached.
 A AnyFrame · Ingested ticket, attached flamegraph queued
forager/web · PR #482 · GitHub 1m ago
 theo commented on src/search/index.ts
 @anyframe write tests for the new edge cases here, especially empty queries.
 A AnyFrame · Reading PR diff, writing tests queued
D @anyframe upgrade Acme Inc to Enterprise, 20 seats
 Desktop live
 Applications 04:41 root
 Northwind · Chromium
 app.northwind.io/billing
 Acme Inc cus_4f2a
 Plan Pro
Seats 12
Opening Acme's billing page
slack · #marketing-site · thread 3 in thread
 A Aja S. just now
 @anyframe update the hero to focus on enterprise, and add a testimonial section under "Pricing".
A AnyFrame AGENT just now
 On it. Updating the hero copy and inserting a testimonial section. I'll use the existing card pattern from /customers .
Live preview updating for 3 collaborators on this thread
Ship agents
 inside your product.
 Our SDK does the runtime. You write a few lines and your product has agents.
agent.py Python TypeScript cURL
$ pip install anyframe Copy
 from anyframe import AnyFrame
af = AnyFrame()
agent = af.agents.create(
 name= "user-research" ,
 template= "user-research" ,
 connectors=[ "slack" , "posthog" ],
 )
run = af.sessions.run(
 agent_id=agent.id,
 text= "break down lead → demo this week" ,
 )
 print (run.summary)
Frequently Asked Questions.
How much does it cost? Free to try — every account gets 500 credits , no card required. Credits cover what your agents spend on models as they run — typically enough for a few full sessions to get a real feel for AnyFrame. Pay-as-you-go after that. Need SSO, self-hosting, or custom SLAs? Schedule a call .
Who is AnyFrame for? Teams that ship software together. Engineering, product, design, and data people who already work in Slack, Linear, and GitHub, and want a teammate that does the work, not just suggests it.
Do we always have to tag the agent, or can it act on its own? Both. Tag it from a message, ticket, or PR comment for one-off work. Put it on a schedule, a webhook, or a queue for ongoing jobs. It will pause and ask when it hits something risky or unclear.
Does an agent ever touch our production data? Not unless you point it there. Runs happen in a fresh sandbox with the repos and secrets you scope to that agent. Production access is opt-in, audited, and gated by a human approval step you control.
Can we self-host? An open-source version is coming soon, so you will be able to run AnyFrame in your own environment with your own keys, repos, and secrets. In the meantime, we run a managed version you can use today.
Platform for every agent your team builds.
 Named, sandboxed, and live in the tools each team already uses.
Start Building Book a demo
[ product ]
 blog changelog docs python sdk typescript sdk
 [ company ]
 privacy policy terms of service contact
 [ connect ]
AnyFrame
 © 2026 AnyFrame, Inc.

## 导航

- 项目页：[[10-项目/anyframe.dev_d0e5f859]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
