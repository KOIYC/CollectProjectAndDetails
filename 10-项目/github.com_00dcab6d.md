---
type: "project"
title: "Show HN: OpenComputer – an open source alternative to Devin"
project_url: "https://github.com/diggerhq/opencomputer"
first_seen: "2026-11-21T14:45:01+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_iacguy
  - story_50581403
  - show_hn
  - front_page
lang: "en"
---

# Show HN: OpenComputer – an open source alternative to Devin

> [!info] 一句话导读
> Hi HN!Utpal here, I'm one of the founders of OpenComputer.OpenComputer is an open source cloud coding agent for teams that can run in your own cloud account (AW…

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://github.com/diggerhq/opencomputer>
> 首次收录：2026-11-21T14:45:01+08:00
> 来源渠道：HN Show HN
> 标签：author_iacguy, story_50581403, show_hn, front_page
> 最新指标：点赞=96 · 评论=24 · engagement_velocity=96

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-11-21T14:45:01+08:00 | HN Show HN | 点赞=96 · 评论=24 · engagement_velocity=96 | [[20-语料/posts/hn_show/2026-11-21/1f4577d836e86412_Show-HN-OpenComputer-–-an-open-source-alternative]] |

## 摘要正文

Hi HN!Utpal here, I'm one of the founders of OpenComputer.OpenComputer is an open source cloud coding agent for teams that can run in your own cloud account (AWS, GCP, Azure).We run the agent harness and the sandbox on the same durable VM (architecture in the docs [1]). First commit lands in 24s; the alternatives we benchmarked took 53-72s (benchmarks below [2]).Two other choices:- One VM per team, scalable horizontally. Sessions are isolated in git worktrees. - Session files are backed up to a repo after every turn, so any session can resume on another VM.We noticed that past ~640 session-hours a month, one always-on 4 vCPU VM is cheaper than per-session E2B sandboxes, for example. So at scale, this setup would not only be faster than current SOTA coding agents, but also more cost-efficient.Feel free to try via cloud for free [4] or self host. We would love any and all feedback, and happy to answer any questions! Full demo below [3].[1]: https://docs.opencomputer.dev/getting-started/architecture [2]: https://opencomputer.dev/blog/cloud-agents-as-fast-as-local/ [3]: https://x.com/IgorZIJ/status/2121309785882591711 [4]: https://app.opencomputer.dev
