---
type: "project"
title: "Show HN: Corral kill every command your agent starts"
project_url: "https://github.com/Cardinal44/corral"
first_seen: "2026-09-29T09:42:55+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_CG144
  - story_49886422
  - show_hn
lang: "en"
---

# Show HN: Corral kill every command your agent starts

> [!info] 一句话导读
> This summer I got to intern on the backend of an AI agent and I noticed that it would run commands like tail -f or some random background jobs and exit without …

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://github.com/Cardinal44/corral>
> 首次收录：2026-09-29T09:42:55+08:00
> 来源渠道：HN Show HN
> 标签：author_CG144, story_49886422, show_hn
> 最新指标：点赞=2 · 评论=0 · engagement_velocity=2

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-09-29T09:42:55+08:00 | HN Show HN | 点赞=2 · 评论=0 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-09-29/a246dcaed6d9c890_Show-HN-Corral-kill-every-command-your-agent-start]] |

## 摘要正文

This summer I got to intern on the backend of an AI agent and I noticed that it would run commands like tail -f or some random background jobs and exit without terminating any of these. I got curious and looked up how Claude Code handles stuff like this, and it turns out they have similar problems.There are issues about background processes from the Bash tool not getting cleaned up when the session ends, and one where a timeout sends SIGTERM to the whole process group and ends up killing Claude Code itself. Most runners only kill the process they started, so anything that double forks, runs in the background, or keeps stdout open either survives or makes the runner hang.Corral was me attempting to make a fix for this problem, while also trying to learn about processes and signals in Linux. You run corral --wall 30s -- yourcommand and by the time it's done, nothing it started should be running.The command gets its own session so killing it can't kill you, and there's a mode where it runs in its own cgroup so the whole tree gets killed at once, including processes that may have changed sessions or process groups.If there's no cgroup available it tracks the tree through /proc instead …
