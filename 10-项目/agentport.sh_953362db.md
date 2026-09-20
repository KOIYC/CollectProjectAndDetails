---
type: "project"
title: "Show HN: AgentPort – Open-source Security Gateway For Agents"
project_url: "https://agentport.sh/"
first_seen: "2026-09-21T01:41:41+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_yakkomajuri
  - story_47950752
  - show_hn
lang: "en"
---

# Show HN: AgentPort – Open-source Security Gateway For Agents

> [!info] 一句话导读
> Hey HN!I've been wanting to use something like OpenClaw for a while but couldn't get myself to give it access to anything important due to all the risks involve…

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://agentport.sh/>
> 首次收录：2026-09-21T01:41:41+08:00
> 来源渠道：HN Show HN
> 标签：author_yakkomajuri, story_47950752, show_hn
> 最新指标：点赞=8 · 评论=3 · engagement_velocity=8

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-09-21T01:09:14+08:00 | HN Show HN | 点赞=8 · 评论=3 · engagement_velocity=8 | [[20-语料/posts/hn_show/2026-09-21/8deac700e6eee8b2_Show-HN-AgentPort-–-Open-source-Security-Gateway-F]] |
| 2026-09-21T01:13:42+08:00 | HN Show HN | 点赞=8 · 评论=3 · engagement_velocity=8 | [[20-语料/posts/hn_show/2026-09-21/8deac700e6eee8b2_Show-HN-AgentPort-–-Open-source-Security-Gateway-F]] |
| 2026-09-21T01:41:41+08:00 | HN Show HN | 点赞=8 · 评论=3 · engagement_velocity=8 | [[20-语料/posts/hn_show/2026-09-21/8deac700e6eee8b2_Show-HN-AgentPort-–-Open-source-Security-Gateway-F]] |

## 摘要正文

Hey HN!I've been wanting to use something like OpenClaw for a while but couldn't get myself to give it access to anything important due to all the risks involved. Prompt injection is still a problem (even though some people seem to ignore it) and so are hallucinations and mishaps that cause agents to do things like delete production data [1].Even harnesses like Claude Code and Codex are subject to this, particularly since we're getting progressively looser about how we run them e.g. Conductor is really popular and runs agents without any sandboxing.That means we're in a bit of an all-or-nothing situation. There are people who just ignore the risks and connect everything to their agents and reap benefits from it while being subject to more risk, and there are others that just don't connect anything because they are mindful of the potential issues.I've been quite cautious but have wanted to run more autonomous agents and so I built the component I needed to enable me to do so: AgentPort.AgentPort is a gateway that connects to any service (e.g. Gmail, GitHub, Stripe, PostHog, Linear) and let's you set granular permissions for what the agent can do automatically, what it needs your app…
