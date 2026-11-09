---
type: "project"
title: "Show HN: Recalc – Spreadsheet where cells can be Claude Code or Codex terminals"
project_url: "https://github.com/sshah03/recalc"
first_seen: "2026-11-09T09:39:29+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_sshah03
  - story_50413970
  - show_hn
lang: "en"
---

# Show HN: Recalc – Spreadsheet where cells can be Claude Code or Codex terminals

> [!info] 一句话导读
> I built this because it was useful for me when building evals/benchmarks, and I decided to put it up for free for others. The goal was quite simple, make it eas…

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://github.com/sshah03/recalc>
> 首次收录：2026-11-09T09:39:29+08:00
> 来源渠道：HN Show HN
> 标签：author_sshah03, story_50413970, show_hn
> 最新指标：点赞=3 · 评论=2 · engagement_velocity=3

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-11-09T09:39:29+08:00 | HN Show HN | 点赞=3 · 评论=2 · engagement_velocity=3 | [[20-语料/posts/hn_show/2026-11-09/a909e06a46ca9a3e_Show-HN-Recalc-–-Spreadsheet-where-cells-can-be-Cl]] |

## 摘要正文

I built this because it was useful for me when building evals/benchmarks, and I decided to put it up for free for others. The goal was quite simple, make it easy to use a lead claude code / codex session in a panel on the side, while allowing every cell to also be a terminal session running claude/codex, and make it possible to continue a session in an actual terminal window if I needed to. They can all talk to each other using cells on the grid, named cells, or the MCP server that effectively glues the app together. I also found it useful for managing context within related but disparate sessions.My real benchmark runs with recalc are internal to my startup, so to demonstrate some of the functionality I built a small FDA Bench with the tool (obtain and put together dossier's of FDA submissions, and see if a harnessed Claude could have accurately predicted pass/fail): https://github.com/sshah03/recalc#a-model-benchmarkIt is still very much a work in progress, but given the versatility of spreadsheet apps, wanted to see how others see themselves using it and what doesn't exist that would be useful to them. Currently runs locally on macs, linux as well but that's less tested, and Win…
