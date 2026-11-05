---
type: "project"
title: "Show HN: Safe and lightweight VMs for Coding agents"
project_url: "https://github.com/skerrysoft/safeagent"
first_seen: "2026-11-05T11:21:45+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_msjpr
  - story_50369671
  - show_hn
lang: "en"
---

# Show HN: Safe and lightweight VMs for Coding agents

> [!info] 一句话导读
> skerrysoft/safeagent

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://github.com/skerrysoft/safeagent>
> 首次收录：2026-11-05T11:21:45+08:00
> 来源渠道：HN Show HN
> 标签：author_msjpr, story_50369671, show_hn
> 最新指标：点赞=2 · 评论=0 · engagement_velocity=2

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-11-05T11:21:45+08:00 | HN Show HN | 点赞=2 · 评论=0 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-11-05/8c6f8541bc6ba8d1_Show-HN-Safe-and-lightweight-VMs-for-Coding-agents]] |

## 摘要正文

# skerrysoft/safeagent  Run agents in lightweight and safe VMs  - Stars: 2 - Forks: 0 - Watchers: 2 - Open issues: 0 - License: MIT License - Default branch: main - Created: 2026-11-03T02:27:03Z  ## Languages  - Go - Makefile - Shell  ## Top Contributors  - skerrysoft (33 contributions)  ---  ## README  # safeagent  **A lightweight Linux VM for every checkout, so parallel coding sessions can't collide, and the code they run can't reach your machine.**  Coding agents like Claude Code work best in parallel: several sessions, each in its own git worktree, each on its own task. Worktrees separate the files, but everything else is shared. Two sessions both want port 3000, one branch's migration breaks the other's database, and every command an agent runs has your whole machine within reach.  safeagent gives each worktree its own small Linux VM, with its own processes, ports, Postgres, Valkey (Redis) and Temporal, and its own copy of their data. It reads what it needs from the repository (lockfiles, compose files, monorepo packages, the local addresses its env files name), so most projects need no configuration. It plugs into Claude Code, so every worktree session gets one automatically …
