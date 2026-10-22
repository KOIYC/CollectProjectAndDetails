---
type: "corpus"
item_id: "d0f5c0489f6d3c85"
title: "Show HN: ReviewerAgent and StopContinue, for CC and Codex with Pi"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50188494"
project_url: "https://github.com/rladr-org/reviewer-agent"
author: "raylad"
published_at: "2026-10-21T22:22:59Z"
captured_at: "2026-10-22T09:46:18+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-10-22"
pub_day: "2026-10-21"
tags:
  - 语料
  - hn_show
  - author_raylad
  - story_50188494
  - show_hn
metrics: {"points": 2, "comments": 0, "engagement_velocity": 2}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:3d"
---

# Show HN: ReviewerAgent and StopContinue, for CC and Codex with Pi

> [!info] 一句话导读
> This package is designed to solve two problems:1. Frontier models like Fable 5.1, Opus 5.5, Astra 6.0 and Sol 6.1 all make errors and bugs that can be found by …

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50188494>
> 指标：点赞=2 · 评论=0 · engagement_velocity=2
> 作者：raylad　|　发布：2026-10-21T22:22:59Z
> 项目链接：<https://github.com/rladr-org/reviewer-agent>
> 采集：2026-10-22T09:46:18+08:00　|　id：`d0f5c0489f6d3c85`

## 正文

This package is designed to solve two problems:1. Frontier models like Fable 5.1, Opus 5.5, Astra 6.0 and Sol 6.1 all make errors and bugs that can be found by another model (even a much smaller model like Luna).2. In what is supposed to be a long development run, for example against a plan, models will decide to stop before they are finished, when there is obviously more work to do, or to ask a question they already should know the answer to.ReviewerAgent blocks git commits and sends them to another agent that reviews the staged files and either allows the commit or returns a list of issues to fix.StopContinue evaluates every agent stop and determines if it still has work to do or if it is asking a question that it has the answer to already. In either of those cases, it prompts the agent to keep working and specifies next steps or answers to questions, based on the current plan document and chat history.The system works for and is tested on Claude Code and Codex as the developer harness, and either of those or any other model, through Pi, as the reviewer.I've developed it over the last 4 months or so and used it daily over that period.Take a look if it sounds useful. It's been tested on MacOS and Linux (Ubuntu), and has agent assisted install, update, and removal scripts, for convenience.Stats:Over four months of daily use of the system while developing it (from late June til today), reviewerAgent (usually a GPT Luna model) gated 3,877 commits, running about 7,600 reviews in total, so about half of those commits were rejected at least once.The coding agent (Fable or Opus) almost never disagreed with the reviewer's judgements: over the last month, for example, it pushed back on just 3 of 693 rejections.Each rejection listed an average of two required fixes and most rejected commits were accepted after a second round (90% within five attempts).Rejection rates increased with commit size: only 23% of code commits under 50 lines were sent back, but 72% of those over 1,000 lines were initially rejected.Here's an example of a bug that it caught last month for me. More examples in the README:The Fable 5.1 developer agent wrote a wrapper script that runs a set of R validation checks against a freshly loaded database and records whether each one passed. (One of two required fixes shown.)REQUIRED FIXES (blocking) 2. docs/database-phase-loader/local-load/run_r_checks.sh:4-6 pipes each R check through
 tail without pipefail or explicit status handling, so a failed Rscript can still
 produce a zero exit status and be recorded as successful. Preserve and propagate each
 check's exit status.

In a shell pipeline the exit status is that of the last command, so `Rscript check.R | tail` reports `tail`'s success even when the check fails. The script prints the tail of the failing check's output, exits 0, and records a pass. A broken load would have been certified as validated.

## 导航

- 项目页：[[10-项目/github.com_5c497bb3]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
