---
type: "project"
title: "Show HN: A Firewall for AI agents with auditing"
project_url: "https://github.com/beebeeVB/trajeckt"
first_seen: "2026-09-21T03:11:01+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_beebeeVB
  - story_48726867
  - show_hn
lang: "en"
---

# Show HN: A Firewall for AI agents with auditing

> [!info] 一句话导读
> A causal firewall for AI agents: blocks multi-step tool-call chains that leak data, even when every call is individually allowed.

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://github.com/beebeeVB/trajeckt>
> 首次收录：2026-09-21T03:11:01+08:00
> 来源渠道：HN Show HN
> 标签：author_beebeeVB, story_48726867, show_hn
> 最新指标：点赞=4 · 评论=0 · engagement_velocity=4

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-09-21T01:29:55+08:00 | HN Show HN | 点赞=4 · 评论=0 · engagement_velocity=4 | [[20-语料/posts/hn_show/2026-09-21/74dc042db1b5dbf0_Show-HN-A-Firewall-for-AI-agents-with-auditing]] |
| 2026-09-21T03:11:01+08:00 | HN Show HN | 点赞=4 · 评论=0 · engagement_velocity=4 | [[20-语料/posts/hn_show/2026-09-21/74dc042db1b5dbf0_Show-HN-A-Firewall-for-AI-agents-with-auditing]] |

## 摘要正文

# beebeeVB/trajeckt  A causal firewall for AI agents: blocks multi-step tool-call chains that leak data, even when every call is individually allowed.  - Stars: 10 - Forks: 0 - Watchers: 10 - Open issues: 0 - License: Apache License 2.0 - Default branch: main - Created: 2026-05-21T19:46:02Z  ## Languages  - Dockerfile - Makefile - Python - Rust - Shell  ## Top Contributors  - beebeeVB (118 contributions)  ---  ## README  Readme · MD # trajeckt  **A runtime enforcement gateway for AI agents. It blocks multi-step exploits that every per-action security check misses — deterministically, in ~1.6ms, outside the agent's reach.**  Reading a database is allowed. Sending an email is allowed. Doing them in that order is data exfiltration. Every authorization system on the market checks one action at a time, so the sequence walks right through. trajeckt checks each call against the whole trajectory the agent has accumulated and the data flowing through it — so the exfiltration is blocked at the step that completes it, even though that step looks legal on its own.  ## Run it  The fastest way to see the real gateway enforce is Docker. It brings up the enforcement gateway plus a mock MCP upstrea…
