---
type: "project"
title: "Show HN: Aigent-OS, a Claude Code harness that clears and resumes"
project_url: "https://github.com/wrg32786/aigent-os"
first_seen: "2026-10-28T09:39:16+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_wrg32786
  - story_50261376
  - show_hn
lang: "en"
---

# Show HN: Aigent-OS, a Claude Code harness that clears and resumes

> [!info] 一句话导读
> I run my business on four Claude Code agents: Titus, Pheme, Davinci and Metis. They write my newsletter, The AIgent (about 9k subscribers), every day through a …

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://github.com/wrg32786/aigent-os>
> 首次收录：2026-10-28T09:39:16+08:00
> 来源渠道：HN Show HN
> 标签：author_wrg32786, story_50261376, show_hn
> 最新指标：点赞=2 · 评论=0 · engagement_velocity=2

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-10-28T09:39:16+08:00 | HN Show HN | 点赞=2 · 评论=0 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-10-28/fa038e7924500fe3_Show-HN-Aigent-OS,-a-Claude-Code-harness-that-clea]] |

## 摘要正文

I run my business on four Claude Code agents: Titus, Pheme, Davinci and Metis. They write my newsletter, The AIgent (about 9k subscribers), every day through a drafting and proofreading engine that Pheme checks before scheduling. They also build AI courses, run a pipeline that turns the day's featured repo into a talking-head video of my avatar for Instagram, set up ad deals, and run Meta ads and email funnels with me. Nothing closes until I sign off. Metis posts jobs on a job board and the others claim them. The hard part wasn't any single task. It was keeping the agents coherent over weeks. Compaction kept dropping the small decisions, and then an agent would redo work I'd already ruled out. aigent-os is my fix. At a context threshold (80% by default) the agent writes a capsule, a checkpoint file in git, and has to reply with one exact line. Only then does the runner send /clear, wait for a SessionStart receipt proving a fresh session started, and resume. One ack buys at most one clear. If anything is ambiguous it stops at HOLD:clear-stalled-after-ack and doesn't retry. On resume the capsule is reference only, live state wins, and anything the writer couldn't capture is written a…
