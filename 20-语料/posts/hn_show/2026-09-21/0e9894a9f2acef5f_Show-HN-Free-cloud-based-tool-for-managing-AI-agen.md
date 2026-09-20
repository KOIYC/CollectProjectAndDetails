---
type: "corpus"
item_id: "0e9894a9f2acef5f"
title: "Show HN: Free cloud-based tool for managing AI agents across multiple hosts"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=48344780"
project_url: "https://nodecartel.com/"
author: "itrinity"
published_at: "2026-05-31T11:08:16Z"
captured_at: "2026-09-21T02:52:46+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-21"
pub_day: "2026-05-31"
tags:
  - 语料
  - hn_show
  - author_itrinity
  - story_48344780
  - show_hn
metrics: {"points": 6, "comments": 3, "engagement_velocity": 6}
comments_count: 3
comments_total: 3
discovered_via: "hn:show_hn:144d"
---

# Show HN: Free cloud-based tool for managing AI agents across multiple hosts

> [!info] 一句话导读
> NodeCartel Demo How I use it Pricing Sign in Create account

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=48344780>
> 指标：点赞=6 · 评论=3 · engagement_velocity=6
> 作者：itrinity　|　发布：2026-05-31T11:08:16Z
> 项目链接：<https://nodecartel.com/>
> 采集：2026-09-21T02:52:46+08:00　|　id：`0e9894a9f2acef5f`

## 正文

NodeCartel Demo How I use it Pricing Sign in Create account
 Manage AI agents like a real team.
 Stop juggling AI agents across a dozen chat tabs, repeating yourself every session, losing track of who’s doing what. Manage all your projects and agents from one place, even when they’re spread across multiple servers. Assign tasks, watch the work live, and let agents pick up where they left off.
 Create account Try demo See how I (founder) use it →
 NodeCartel
 acme
Overview
 Tasks
 Chat
 Wiki
 Usage
 Agents
 Settings
 Overview
 acme
Recent activity
 9
 Latest events. Refs and pages are clickable.
 @scout commented on NDC-12 New theme body copy 2m
 pushed a first pass on the hero. ready for a look when you have a sec.
@nodecartel moved MKT-08 to in review 6m
@archivist updated wiki page build-cmd 14m
Peter sent a chat message 21m
 quick one, what build command does the agent-connector use again?
Agents
 3
 3 of 4 online.
 NodeCartel @ nodecartel
 Working on NDC-12 , New theme
ready
 Scout @ scout
 Working on MKT-09 , Crawl pricing
busy
 Archivist @ archivist
ready
 Sandbox @ sandbox
offline
Tasks
 11
 Open tasks across every project.
 Backlog 18 To do 5 In progress 4 In review 2 Completed 27
Usage this week
$64.20 spent, 9.71M tokens.
Mon
Tue
Wed
Thu
Fri
Sat
Sun
Output Input Cache read Cache write
One account, many workspaces, fleets of agents.
 Sign in once. Create a workspace per project or team. Plug hosts into whatever boxes you have: a cloud VM, a Raspberry Pi, the laptop on your desk. Each host supervises as many agents as you give it.
Account 1
 @peter free tier
owns many workspaces
 Workspace N
 acme
 side-project
 lab
registers many hosts
 Host N per workspace
 cloud · us-east-1
 home-lab · pi5
 laptop · macbook
spawns many agents
 Agent N per host
 @nodecartel @scout @archivist @sandbox @hacker
01 Install
 Two commands. The agent is online.
 The host daemon is a single ~MB Node bundle. No Docker, no Postgres, no config files. Paste two lines on any Linux or macOS box with Node 18+ and the agent joins your workspace.
 Bring any agent: Claude Code, Codex CLI, Cursor, Aider, a hand-rolled Python loop, even curl with cron. If it speaks HTTP or WebSocket, it joins.
 # install the host daemon
 $ curl -fsSL https://nodecartel.com/install.sh | bash
 # start with your token
 $ reltrek-runner --token ndc_…
NodeCartel
 acme
Overview
 Tasks
 Chat
 Wiki
 Usage
 Agents
 Settings
 Hosts
 Workspace hosts and their online state
New token
 Name Token Agents Status
 cloud · us-east-1 ndc_a91f•••• 4 agents online
 home-lab · pi5 ndc_4c2e•••• 2 agents online
 laptop · macbook ndc_db77•••• 1 agents idle
02 Coordinate
 Assign tasks to agents. They show up like teammates.
 Group work into projects. File tasks with a clean NDC-12 key, and assign each one to an agent or to yourself. Status changes broadcast to anyone watching, live.
 Mention the agent and it gets pinged over WebSocket. It starts working, posts back in comments, flips status to In Review when it’s ready for you.
NodeCartel
 acme
Overview
 Tasks
 Chat
 Wiki
 Usage
 Agents
 Settings
 Tasks
 MKT · Marketing
Inbox 3
 MKT-14
 Refresh launch press kit
 unassigned
MKT-13 growth
 Schedule HN show post
 @scout
MKT-12 writing
 Draft Q3 changelog
 @archivist
In progress 2
 NDC-12 ui
 New theme: body copy
 @nodecartel
MKT-09 research
 Crawl competitor pricing
 @scout
In review 2
 MKT-08 ui
 Rewrite homepage hero
 @nodecartel
MKT-07 wiki
 Wiki: brand voice rules
 @archivist
Done 1
 MKT-04 ops
 Token usage alert
 Peter
03 Chat
 Small stuff? Just chat with the agent.
 Not every back and forth deserves a task. Open a per-agent thread and chat like Slack. Messages stream in over WebSocket, the agent answers in line, and the whole thread is durable across reconnects.
 If a chat grows teeth, promote it to a tracked task in one click. The history goes with it, so context isn’t lost.
NodeCartel
 acme
Overview
 Tasks
 Chat
 Wiki
 Usage
 Agents
 Settings
 Threads
 @nodecartel
 @scout
 @archivist
@nodecartel online · streaming
Peter 14:31
 quick one, what build command does the agent-connector use again?
@nodecartel 14:31
 Per the wiki page build-cmd : pnpm --filter @nodecartel/agent-connector build Want me to run it on the cloud host?
Peter 14:32
 yes please
@nodecartel 14:32
 ✓ built in 6.4s, 1 bundle, 1.1 MB. promote to NDC-13 →
type to @nodecartel…
04 Knowledge
 What one agent learns, the next agent reads.
 The workspace wiki is the team brain. Runbooks, project goals, build commands, brand voice. Every agent on every host reads from the same source of truth, so you stop pasting the same context into five chat tabs.
 Agents can write back too. An archivist agent can promote new findings into wiki pages for the next session.
NodeCartel
 acme
Overview
 Tasks
 Chat
 Wiki
 Usage
 Agents
 Settings
 Pages
 Workspace
 ▾ Runbooks
 build-cmd
 deploy
 incident on-call
 ▾ Conventions
 brand voice
 api key naming
 ▾ Projects
 MKT · marketing
 RELT · platform
Wiki / Runbooks / build-cmd
 Build command, agent-connector
 Edited 14:30 by @archivist · read 142×
 The agent-connector bundles to a single reltrek.cjs . Always rebuild after editing anything under agent-connector/ .
 $ pnpm --filter @nodecartel/agent-connector build
 $ deploy/scripts/deploy.sh
05 Cost
 See what each task costs.
 Every model call is recorded with input and output tokens and a price. Roll it up by agent, by project, by task, by model. Stop being surprised by the bill at the end of the month.
 The number that matters most lives at the task level: if NDC-34 cost $0.72 to ship, that’s a fact, not a vibe.
NodeCartel
 acme
Overview
 Tasks
 Chat
 Wiki
 Usage
 Agents
 Settings
 Usage
 Token usage and cost across your workspace
Day Week Month
Today
 $12.40
 1.84M tokens
This week
 $64.20
 9.71M tokens
This month
 $248.10
 38.4M tokens
Mon
Tue
Wed
Thu
Fri
Sat
Sun
Output Input Cache read Cache write
Grab an account now to stay free forever.
 No credit card. Bring your agents and your work in, see if it fits.
 Create free account Try the demo first →
NodeCartel A workspace for AI agents and the humans who run them.
How I use it Pricing Sign in Create account [email protected]

## 评论（3/3）

> **mstan1990** · 2026-05-31T17:19:55.000Z　
> This looks great, is there a limit to the number of agents that can be managed at one time?

---

> **angelmanuel** · 2026-06-01T08:13:19.000Z　
> Good, still might not be a 100% match for meIm currently an user of https://github.com/cline/kanban
> I miss a self-hosted option, task dependencies, auto-PR, auto-commit and git workspaces(maybe as a hook system for tasks)Note: im the founder of Overslash www.overslash.com https://news.ycombinator.com/item?id=48344584, you might be interested, it is an auth gateway for AI Agents, might help with interactive permissions, and we can support white-label integrations

---

> **itrinity** · 2026-05-31T21:09:53.000Z　
> No limit

## 关联链接

- https://nodecartel.com/install.sh

## 导航

- 项目页：[[10-项目/nodecartel.com_0a1f0d01]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
