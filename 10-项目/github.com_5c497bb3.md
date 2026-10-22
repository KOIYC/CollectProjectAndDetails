---
type: "project"
title: "Show HN: ReviewerAgent and StopContinue, for CC and Codex with Pi"
project_url: "https://github.com/rladr-org/reviewer-agent"
first_seen: "2026-10-22T09:46:18+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_raylad
  - story_50188494
  - show_hn
lang: "en"
---

# Show HN: ReviewerAgent and StopContinue, for CC and Codex with Pi

> [!info] 一句话导读
> This package is designed to solve two problems:1. Frontier models like Fable 5.1, Opus 5.5, Astra 6.0 and Sol 6.1 all make errors and bugs that can be found by …

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://github.com/rladr-org/reviewer-agent>
> 首次收录：2026-10-22T09:46:18+08:00
> 来源渠道：HN Show HN
> 标签：author_raylad, story_50188494, show_hn
> 最新指标：点赞=2 · 评论=0 · engagement_velocity=2

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-10-22T09:46:18+08:00 | HN Show HN | 点赞=2 · 评论=0 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-10-22/d0f5c0489f6d3c85_Show-HN-ReviewerAgent-and-StopContinue,-for-CC-and]] |

## 摘要正文

This package is designed to solve two problems:1. Frontier models like Fable 5.1, Opus 5.5, Astra 6.0 and Sol 6.1 all make errors and bugs that can be found by another model (even a much smaller model like Luna).2. In what is supposed to be a long development run, for example against a plan, models will decide to stop before they are finished, when there is obviously more work to do, or to ask a question they already should know the answer to.ReviewerAgent blocks git commits and sends them to another agent that reviews the staged files and either allows the commit or returns a list of issues to fix.StopContinue evaluates every agent stop and determines if it still has work to do or if it is asking a question that it has the answer to already. In either of those cases, it prompts the agent to keep working and specifies next steps or answers to questions, based on the current plan document and chat history.The system works for and is tested on Claude Code and Codex as the developer harness, and either of those or any other model, through Pi, as the reviewer.I've developed it over the last 4 months or so and used it daily over that period.Take a look if it sounds useful. It's been tes…
