---
type: "corpus"
item_id: "6eefd881cf0544a6"
title: "Show HN: Task Manager for AI Agents (MCP, Opensource)"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=47958608"
project_url: "https://github.com/agentrq/agentrq"
author: "mrtnx"
published_at: "2026-04-30T05:43:18Z"
captured_at: "2026-09-21T01:41:17+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-21"
pub_day: "2026-04-30"
tags:
  - 语料
  - hn_show
  - author_mrtnx
  - story_47958608
  - show_hn
metrics: {"points": 6, "comments": 4, "engagement_velocity": 6}
comments_count: 4
comments_total: 4
discovered_via: "hn:show_hn:174d"
---

# Show HN: Task Manager for AI Agents (MCP, Opensource)

> [!info] 一句话导读
> AgentRQ is a (optionally) human-in-the-loop, self learning closed loop task manager for agents. Agents can create and schedule tasks for themself and work on th…

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=47958608>
> 指标：点赞=6 · 评论=4 · engagement_velocity=6
> 作者：mrtnx　|　发布：2026-04-30T05:43:18Z
> 项目链接：<https://github.com/agentrq/agentrq>
> 采集：2026-09-21T01:41:17+08:00　|　id：`6eefd881cf0544a6`

## 正文

AgentRQ is a (optionally) human-in-the-loop, self learning closed loop task manager for agents. Agents can create and schedule tasks for themself and work on them on their own schedule.In high level it comes with one supervisor MCP that controls workspaces(worker agents) and unlimited number of isolated workspace MCPs (self learning agents).Each workspace/agent has a mission/persona for the agent. And self-learning-loop note.I am using it about 6 weeks in production, and completed more than 500 tasks. I just released the opensource version(as is in production) under Apache 2.0 license.Currently it supports Gemini CLI and Claude code. I am going to extend support all major agents soon.Happy to answer any questions.

## 评论（4/4）

> **chloeeekim** · 2026-04-30T10:18:08.000Z　
> Interesting approach.I’m especially curious about the “self-learning loop” — in practice, does it actually improve outcomes over time, or does it tend to reinforce suboptimal patterns?And How much autonomy do the agents actually have in practice?I’ve found that fully autonomous loops tend to need a lot of guardrails to stay useful.

---

> **fule** · 2026-04-30T15:26:39.000Z　
> How does a team setup look like? Maybe tested it with someone?

---

> **mrtnx** · 2026-05-01T00:32:48.000Z　
> > does it actually improve outcomes over time
> Yes, after every execution (optionally), you are able to attach self-eval and update the skills accordingly.> does it tend to reinforce suboptimal patterns?
> I was thinking on a ML approach but kept myself lazy and decided go all in with LLM self-evaluation notes.> How much autonomy do the agents actually have in practice?
> 100% is possible but if you are asking personally: I define what I need and give them personality/mission to accomplish in multiple worksplace.> I’ve found that fully autonomous loops tend to need a lot of guardrails to stay useful.
> I can tell, it did what I was not able to do mentally and physically. It is a huge unlock for creating time for myself.

---

> **mrtnx** · 2026-05-01T00:34:05.000Z　
> I assigned it to self-document: https://agentrq.com/docs I verified all steps one by one. Please let me know if I can help you onboard.

## 导航

- 项目页：[[10-项目/github.com_30bf3fa9]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
