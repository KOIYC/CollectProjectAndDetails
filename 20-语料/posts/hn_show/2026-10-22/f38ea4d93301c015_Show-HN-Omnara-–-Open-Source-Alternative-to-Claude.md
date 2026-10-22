---
type: "corpus"
item_id: "f38ea4d93301c015"
title: "Show HN: Omnara – Open-Source Alternative to Claude Managed Agents"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50183892"
project_url: "https://github.com/omnara-ai/omnara"
author: "kmansm27"
published_at: "2026-10-21T16:44:53Z"
captured_at: "2026-10-22T09:46:18+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-10-22"
pub_day: "2026-10-21"
tags:
  - 语料
  - hn_show
  - author_kmansm27
  - story_50183892
  - show_hn
metrics: {"points": 21, "comments": 8, "engagement_velocity": 21}
comments_count: 8
comments_total: 8
discovered_via: "hn:show_hn:3d"
---

# Show HN: Omnara – Open-Source Alternative to Claude Managed Agents

> [!info] 一句话导读
> Hey y'all, Kartik from Omnara (https://omnara.com) here. We're building an open-source API for running durable agents. You create an agent with an API call, and…

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50183892>
> 指标：点赞=21 · 评论=8 · engagement_velocity=21
> 作者：kmansm27　|　发布：2026-10-21T16:44:53Z
> 项目链接：<https://github.com/omnara-ai/omnara>
> 采集：2026-10-22T09:46:18+08:00　|　id：`f38ea4d93301c015`

## 正文

Hey y'all, Kartik from Omnara (https://omnara.com) here. We're building an open-source API for running durable agents. You create an agent with an API call, and Omnara runs the agent loop, gives the agent sandboxes to run commands in, and handles secrets, permissions, and RBAC. Each agent's state is stored in Postgres, so agents survive restarts and cost nothing while idle. You can message them and stream their events over the API.You may remember us from our early days, when we made a remote-control phone app for Claude Code and Codex. Since the harness ran on a laptop back then, we had to build a relay to reach it, it stopped when the laptop closed, and moving it to a cloud sandbox meant syncing code and agent state between machines. We didn't think remote-controlling a local agent was end-game for how people would run agents, so we built a new product where the agent runs in the cloud, any client can talk to it through an API, and it can still use your laptop as one of its machines.Anthropic and OpenAI are building hosted versions of this, like Claude Managed Agents and the OpenAI Agents API. Omnara is an open-source version you can run on your own servers and use your own models. It's basically a harness server like the opencode or codex servers, but durable, scalable, with the usual harness features like file and shell tools, subagents, compaction, permission prompts, MCP, skills, memory, yada yada yada.Here's some interesting architectural decisions we made while building this out:Most harnesses, like Claude Code, Codex, OpenCode, Pi, Goose, etc, run the agent loop in one long-lived process that keeps its log in a JSONL or SQLite file. In Omnara, the log is an append-only event log in Postgres, with inputs, model outputs and tool calls stored as typed rows in their own tables. The loop runs on stateless workers in the control plane. A worker runs one iteration of the loop, either a model call or the tool calls it produced, then releases the agent and puts the next iteration on a queue in Postgres. Whichever worker is free picks it up, so each iteration of an agent's loop can run in a different process on a different machine. Each iteration's result commits in one transaction, so the model output, its tool calls, usage and the next wakeup are saved together or not at all. If a worker dies mid-iteration, nothing commits, its lease expires, and another worker retries it. Agents waiting on a user, a tool or a retry don't hold a worker, so one worker can multiplex thousands of agents.Also unlike other harnesses, the machines that the workers (our agent loop) run on aren't where the agent runs its commands. Instead, any macOS or Linux machine with an internet connection, like your laptop or any cloud sandbox, can run a small daemon (omnarad) that connects out to Omnara, so it doesn't need any open inbound ports. The agent then gets tools for that machine, like running a command or editing a file. An agent can have any number of machines connected to it. A fun thing I like to do is I have my laptop and a cloud sandbox connected to the same agent, so when my laptop is on, my agent codes there and I can interact with it, and I have it often push to Github. When I close my laptop, my agent sees the laptop went offline, pulls the latest changes to its cloud sandbox, and continues there.The entire codebase is open source at https://github.com/omnara-ai/omnara, and it’s self hostable, even on a single machine with docker compose. You can also use the hosted version at https://omnara.com. Let me know what you think!

## 评论（8/8）

> **swyx** · 2026-10-21T23:29:10.000Z　
> with a great related talk! https://ai.engineer/talks/UPwGaM2MKHY-log-is-agent

---

> **asherdale1** · 2026-10-21T23:32:50.000Z　
> feels like everyone is converging on durable agents lately: pi durable, cloudflare agents on durable objects, vercel's durable harness

---

> **rohan_joshi** · 2026-10-22T00:49:54.000Z　
> i was looking for good self-hostable durable agents to automate a persistent keyword watcher across sm. gonna give this a go. any pointers you recommend?

---

> **kmansm27** · 2026-10-21T23:35:21.000Z　
> haha yes! this was the reasoning for making durability native in our harness

---

> **isehgal** · 2026-10-21T23:37:42.000Z　
> thanks swyx! the log is the agent is a core insight behind this

---

> **kmansm27** · 2026-10-21T23:37:36.000Z　
> Yep, I think that all harnesses will require native durability, and pi-durable is a step in the right direction. I'm skeptical of bolted-on durability, like vercel's durable-harness, because they have to neuter the harness for things they can't reliably make durable (e.g. https://github.com/vercel-labs/durable-harness/blob/fb056a3c...)

---

> **isehgal** · 2026-10-22T01:09:47.000Z　
> nice, this is close to something we run ourselves. we put up examples of sm agents that scan socials daily for keywords and DMs us (docs here https://docs.omnara.com/examples/x-signal-agent). probably the fastest starting point is to point your agent to it and ask it to swap in your keywords

---

> **swyx** · 2026-10-21T23:39:12.000Z　
> you beat pi-durable to it!

## 关联链接

- https://github.com/omnara-ai/omnara,
- https://omnara.com
- https://omnara.com.

## 导航

- 项目页：[[10-项目/github.com_b328ea61]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
