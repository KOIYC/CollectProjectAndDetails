---
type: "corpus"
item_id: "4efe7f11fca994b0"
title: "Show HN: Ouijit, command terminals running coding agents"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=48732590"
project_url: "https://github.com/ouijit/ouijit"
author: "pbjerkeseth"
published_at: "2026-06-30T13:37:01Z"
captured_at: "2026-09-21T01:44:50+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-21"
pub_day: "2026-06-30"
tags:
  - 语料
  - hn_show
  - author_pbjerkeseth
  - story_48732590
  - show_hn
metrics: {"points": 4, "comments": 2, "engagement_velocity": 4}
comments_count: 2
comments_total: 2
discovered_via: "hn:show_hn:113d"
---

# Show HN: Ouijit, command terminals running coding agents

> [!info] 一句话导读
> Hey folks, I started working on Ouijit around the start of the new year, and its since become the daily driver for myself and a handful of other engineers (that…

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=48732590>
> 指标：点赞=4 · 评论=2 · engagement_velocity=4
> 作者：pbjerkeseth　|　发布：2026-06-30T13:37:01Z
> 项目链接：<https://github.com/ouijit/ouijit>
> 采集：2026-09-21T01:44:50+08:00　|　id：`4efe7f11fca994b0`

## 正文

Hey folks, I started working on Ouijit around the start of the new year, and its since become the daily driver for myself and a handful of other engineers (that I know of).The initial reason I built it was over dissatisfaction with how most agent orchestrators abstract stuff behind chat UIs, require login, or only support their companies own model/harness. I didn’t want to keep cobbling together scripts for worktree isolation between tasks though, so the yak shaving began. A couple weeks in, I received a message from a friend sharing that they just finished an 8 hour session working in it and they really liked it, and that they’d even shared it with their coworkers unprompted. I’ve been a software engineer/designer for ~10 years and its hard to put into words how rewarding that felt.Some things I think are unique about Ouijit:- Sandboxing is a first-class consideration, Ouijit supports running tasks in per-project Lima VMs. Right now I'm looking into making sandboxing pluggable so you can bring-your-own agent environment local or in the cloud, with a few baked in defaults.- Integrated agents are automatically aware of a session-scoped CLI that enables them to orchestrate and drive tasks from any Ouijit terminal, with no additional setup.- Tasks have lifecycle hooks that can trigger prompts, scripts, or both when tasks start, resume, move to review, or move to done.- You can organize child terminals, markdown, and url previews to terminals. It's a little like Claude artifacts in that way.Supports macOS and linux; integrates with Claude Code, Codex, Pi, and OpenCode agent harnesses.Free and open source, no login, no telemetry.Website: https://ouijit.comGithub : https://github.com/ouijit/ouijit

## 评论（2/2）

> **griffinJH23** · 2026-06-30T13:49:15.000Z　
> That's tremendously inspiring work. I love that it's open source and free of a login and telemetry. I'll check it out!

---

> **pbjerkeseth** · 2026-06-30T14:22:42.000Z　
> Thank you!

## 关联链接

- https://ouijit.comGithub

## 导航

- 项目页：[[10-项目/github.com_b2732c98]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
