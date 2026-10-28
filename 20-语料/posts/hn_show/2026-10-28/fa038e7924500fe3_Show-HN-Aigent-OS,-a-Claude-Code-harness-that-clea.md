---
type: "corpus"
item_id: "fa038e7924500fe3"
title: "Show HN: Aigent-OS, a Claude Code harness that clears and resumes"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50261376"
project_url: "https://github.com/wrg32786/aigent-os"
author: "wrg32786"
published_at: "2026-10-27T16:10:01Z"
captured_at: "2026-10-28T09:39:16+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-10-28"
pub_day: "2026-10-27"
tags:
  - 语料
  - hn_show
  - author_wrg32786
  - story_50261376
  - show_hn
metrics: {"points": 2, "comments": 0, "engagement_velocity": 2}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:3d"
---

# Show HN: Aigent-OS, a Claude Code harness that clears and resumes

> [!info] 一句话导读
> I run my business on four Claude Code agents: Titus, Pheme, Davinci and Metis. They write my newsletter, The AIgent (about 9k subscribers), every day through a …

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50261376>
> 指标：点赞=2 · 评论=0 · engagement_velocity=2
> 作者：wrg32786　|　发布：2026-10-27T16:10:01Z
> 项目链接：<https://github.com/wrg32786/aigent-os>
> 采集：2026-10-28T09:39:16+08:00　|　id：`fa038e7924500fe3`

## 正文

I run my business on four Claude Code agents: Titus, Pheme, Davinci and Metis. They write my newsletter, The AIgent (about 9k subscribers), every day through a drafting and proofreading engine that Pheme checks before scheduling. They also build AI courses, run a pipeline that turns the day's featured repo into a talking-head video of my avatar for Instagram, set up ad deals, and run Meta ads and email funnels with me. Nothing closes until I sign off. Metis posts jobs on a job board and the others claim them.
The hard part wasn't any single task. It was keeping the agents coherent over weeks. Compaction kept dropping the small decisions, and then an agent would redo work I'd already ruled out.
aigent-os is my fix. At a context threshold (80% by default) the agent writes a capsule, a checkpoint file in git, and has to reply with one exact line. Only then does the runner send /clear, wait for a SessionStart receipt proving a fresh session started, and resume. One ack buys at most one clear. If anything is ambiguous it stops at HOLD:clear-stalled-after-ack and doesn't retry. On resume the capsule is reference only, live state wins, and anything the writer couldn't capture is written as Unknown. First run interviews you with three plain questions and makes a first plan. Each agent gets its own memory vault.
Limits, honestly: the public evidence is 11 of 11 cycles on one Windows seat. The runner can still miss a permission dialog (#104), a seat launched from inside another Claude Code session can lose its transcript (#98), and scrolling the seat window sends stray input (#99). v1.1.0 shipped on Sunday.
Try bash install.sh --dry-run, it writes nothing. I'd like to hear where the loop could still double clear or strand a session.

## 导航

- 项目页：[[10-项目/github.com_ea18cd22]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
