---
type: "corpus"
item_id: "a246dcaed6d9c890"
title: "Show HN: Corral kill every command your agent starts"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49886422"
project_url: "https://github.com/Cardinal44/corral"
author: "CG144"
published_at: "2026-09-29T00:35:05Z"
captured_at: "2026-09-29T09:42:55+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-29"
pub_day: "2026-09-29"
tags:
  - 语料
  - hn_show
  - author_CG144
  - story_49886422
  - show_hn
metrics: {"points": 2, "comments": 0, "engagement_velocity": 2}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:3d"
---

# Show HN: Corral kill every command your agent starts

> [!info] 一句话导读
> This summer I got to intern on the backend of an AI agent and I noticed that it would run commands like tail -f or some random background jobs and exit without …

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49886422>
> 指标：点赞=2 · 评论=0 · engagement_velocity=2
> 作者：CG144　|　发布：2026-09-29T00:35:05Z
> 项目链接：<https://github.com/Cardinal44/corral>
> 采集：2026-09-29T09:42:55+08:00　|　id：`a246dcaed6d9c890`

## 正文

This summer I got to intern on the backend of an AI agent and I noticed that it would run commands like tail -f or some random background jobs and exit without terminating any of these. I got curious and looked up how Claude Code handles stuff like this, and it turns out they have similar problems.There are issues about background processes from the Bash tool not getting cleaned up when the session ends, and one where a timeout sends SIGTERM to the whole process group and ends up killing Claude Code itself. Most runners only kill the process they started, so anything that double forks, runs in the background, or keeps stdout open either survives or makes the runner hang.Corral was me attempting to make a fix for this problem, while also trying to learn about processes and signals in Linux. You run corral --wall 30s -- yourcommand and by the time it's done, nothing it started should be running.The command gets its own session so killing it can't kill you, and there's a mode where it runs in its own cgroup so the whole tree gets killed at once, including processes that may have changed sessions or process groups.If there's no cgroup available it tracks the tree through /proc instead (this is a bit weaker, it still catches processes that changed sessions once their parent dies, but it can't kill anything running as a different user or anything handed off to another service like systemd), and if it can't confirm everything is dead it exits with 120.Would love any feedback and more stuff along these lines i can do to learn more

## 导航

- 项目页：[[10-项目/github.com_a4eff253]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
