---
type: "corpus"
item_id: "2f5286fbb9f920ea"
title: "Show HN: Decispher – persistent engineering context and memory for coding agents"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49509142"
author: "iamalizaidi"
published_at: "2026-08-31T12:53:52Z"
captured_at: "2026-09-21T03:11:22+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-21"
pub_day: "2026-08-31"
tags:
  - 语料
  - hn_show
  - author_iamalizaidi
  - story_49509142
  - show_hn
metrics: {"points": 5, "comments": 0, "engagement_velocity": 5}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:52d"
---

# Show HN: Decispher – persistent engineering context and memory for coding agents

> [!info] 一句话导读
> Show HN: Decispher – persistent engineering context and memory for coding agents

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49509142>
> 指标：点赞=5 · 评论=0 · engagement_velocity=5
> 作者：iamalizaidi　|　发布：2026-08-31T12:53:52Z
> 项目链接：—
> 采集：2026-09-21T03:11:22+08:00　|　id：`2f5286fbb9f920ea`

## 正文

Show HN: Decispher – persistent engineering context and memory for coding agents | Hacker News

Show HN: Decispher – persistent engineering context and memory for coding agents

5 points by iamalizaidi 44 minutes ago | hide | past | favorite | discuss

Hello HN,

I'm Ali, building Decispher.

The problem we're working on is that coding agents repeatedly rediscover context that already exists inside an engineering organization.

A developer working on a feature can combine information from previous PRs, Jira tickets, Slack discussions, ownership boundaries, architectural decisions and their own experience. Coding agents usually start with a prompt and a repository, then spend tokens searching for that same context—or miss it entirely.

Decispher is a context and memory layer for engineering agents.

It currently has three parts:

1) Context Engine

Engineering context is usually fragmented across systems. Decispher connects records from engineering platforms and combines related fragments into context units that agents can retrieve for a task.

For example, context around a component might include previous PRs, related issues, architectural decisions, ownership information and implementation history.

We also built Branch Story, which records an AI coding session and turns its execution into a structured handoff on the PR:

Prompt → plan → actions → result.

2) Memory Plane

The Memory Plane stores persistent context at the user, team and project levels.

This includes working preferences and engineering conventions. Teams can also create reusable memory sets for example frontend, payments-backend, or project-specific sets and inject the relevant memory based on the task.

On LongMemEval, our current system reaches:

a) 89% accuracy on the oracle split using GPT-4.1-mini as extractor and reader b) 81% on LongMemEval -S dataset (89% with frontier models) c) 38× median token reduction

I'm happy to share more details about how we measure retrieval quality and token reduction.

3) Worker Agent

Decispher also has an autonomous worker agent that uses the Context Engine and Memory Plane while working on a task.

It can take work from sources such as Jira and Slack, retrieve relevant context and ownership information, and ask the humans involved when the available context is insufficient instead of guessing. Those answers can then become available as context for future work.

The Context Engine, Memory Plane and Worker Agent can be used independently.

Setup

npx decispher init

This connects a repository and configures the agent integration.

npx decispher link

This links your decispher account to your repo.

Decispher works with MCP compatible agents, with specific integrations for Claude, Codex, Grok Build and Cursor. We also have a VS Code/OpenVSX extension for viewing context and writing handoffs.

Notes:

a) The Context Engine does not clone source code; it reads and writes through the GitHub API. b) The Worker Agent uses an isolated sandbox with no network route out except through an allowlisted proxy. c) Worker sandboxes are destroyed after a run. d) Raw messages and text are encrypted at rest and automatically purged. Sessions are currently purged 7 days after merge or 30 days after last activity, with configurable retention.

We also have an MIT-licensed open-source project called Decision Guardian for surfacing ADR context on PRs.

The Context Engine is available now. Memory and the Worker Agent are rolling out gradually.

I'm especially interested in feedback and we are also looking for design partners.

Happy to answer.

Ali

This is a follow-up to my previous Show HN post:

https://news.ycombinator.com/item?id=48762112

The major additions since then are the Memory Plane, LongMemEval results, Worker Agent sandboxing and Branch Story for AI-generated work on PRs.

## 关联链接

- https://news.ycombinator.com/item?id=48762112

## 导航

- 项目页：[[10-项目/Show-HN-Decispher-–-persistent-engineering-conte_2f5286fb]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
