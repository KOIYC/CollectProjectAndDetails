---
type: "project"
title: "Show HN: Relay – a harness for AI coding agents that recover and verify"
project_url: "https://relayevals.com/"
first_seen: "2026-09-30T18:28:30+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_rsathwik07
  - story_49898411
  - show_hn
lang: "en"
---

# Show HN: Relay – a harness for AI coding agents that recover and verify

> [!info] 一句话导读
> I'm tired of AI coding agents which are good for 30 seconds and then completely fail on the slightest hiccup: a failing test, a temporarily unavailable dependen…

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://relayevals.com/>
> 首次收录：2026-09-30T18:28:30+08:00
> 来源渠道：HN Show HN
> 标签：author_rsathwik07, story_49898411, show_hn
> 最新指标：点赞=3 · 评论=0 · engagement_velocity=3

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-09-30T18:28:30+08:00 | HN Show HN | 点赞=3 · 评论=0 · engagement_velocity=3 | [[20-语料/posts/hn_show/2026-09-30/7f363cfd1a4ad2d6_Show-HN-Relay-–-a-harness-for-AI-coding-agents-tha]] |

## 摘要正文

I'm tired of AI coding agents which are good for 30 seconds and then completely fail on the slightest hiccup: a failing test, a temporarily unavailable dependency, an incorrect assumption. Sometimes I end up having to babysit these agents anyway.Relay is a harness for coding agents which takes advantage of the fact that agents are often good at doing something slightly wrong, and not so good at doing something correctly and completely. Relay repeatedly tries the task and on each failure, uses the output to find a better way to do it.It does this by running the task in a loop: attempt the task, run the checks in a fresh sandbox, on failure read the error and retry instead, until the checks pass. What it learned from a run is retained, so that it doesn't repeat the same mistake, and when the checks eventually pass, it will ship the change as a normal git PR - no hidden state, no magic, the diff is human readable.A few specifics:- it runs locally, is free, and doesn't require an account to run the local agent - it uses a top-tier model to plan/review, and cheaper models to actually write code (for cost reasons) - happy to discuss why this is a good idea and why it isn't - the checks r…
