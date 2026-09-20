---
type: "project"
title: "Show HN: Ouijit, command terminals running coding agents"
project_url: "https://github.com/ouijit/ouijit"
first_seen: "2026-09-21T01:44:50+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_pbjerkeseth
  - story_48732590
  - show_hn
lang: "en"
---

# Show HN: Ouijit, command terminals running coding agents

> [!info] 一句话导读
> Hey folks, I started working on Ouijit around the start of the new year, and its since become the daily driver for myself and a handful of other engineers (that…

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://github.com/ouijit/ouijit>
> 首次收录：2026-09-21T01:44:50+08:00
> 来源渠道：HN Show HN
> 标签：author_pbjerkeseth, story_48732590, show_hn
> 最新指标：点赞=4 · 评论=2 · engagement_velocity=4

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-09-21T01:29:55+08:00 | HN Show HN | 点赞=4 · 评论=2 · engagement_velocity=4 | [[20-语料/posts/hn_show/2026-09-21/4efe7f11fca994b0_Show-HN-Ouijit,-command-terminals-running-coding-a]] |
| 2026-09-21T01:44:50+08:00 | HN Show HN | 点赞=4 · 评论=2 · engagement_velocity=4 | [[20-语料/posts/hn_show/2026-09-21/4efe7f11fca994b0_Show-HN-Ouijit,-command-terminals-running-coding-a]] |

## 摘要正文

Hey folks, I started working on Ouijit around the start of the new year, and its since become the daily driver for myself and a handful of other engineers (that I know of).The initial reason I built it was over dissatisfaction with how most agent orchestrators abstract stuff behind chat UIs, require login, or only support their companies own model/harness. I didn’t want to keep cobbling together scripts for worktree isolation between tasks though, so the yak shaving began. A couple weeks in, I received a message from a friend sharing that they just finished an 8 hour session working in it and they really liked it, and that they’d even shared it with their coworkers unprompted. I’ve been a software engineer/designer for ~10 years and its hard to put into words how rewarding that felt.Some things I think are unique about Ouijit:- Sandboxing is a first-class consideration, Ouijit supports running tasks in per-project Lima VMs. Right now I'm looking into making sandboxing pluggable so you can bring-your-own agent environment local or in the cloud, with a few baked in defaults.- Integrated agents are automatically aware of a session-scoped CLI that enables them to orchestrate and drive …
