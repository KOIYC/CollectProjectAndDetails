---
type: "corpus"
item_id: "aff8a1c001d12e7e"
title: "Show HN: Capacitor – shared mem for Claude Code, Cursor and other coding agents"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=48734560"
project_url: "https://capacitor.kurrent.io/"
author: "lougarou"
published_at: "2026-06-30T15:56:30Z"
captured_at: "2026-09-21T01:44:17+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-21"
pub_day: "2026-06-30"
tags:
  - 语料
  - hn_show
  - author_lougarou
  - story_48734560
  - show_hn
metrics: {"points": 2, "comments": 2, "engagement_velocity": 2}
comments_count: 2
comments_total: 2
discovered_via: "hn:show_hn:113d"
---

# Show HN: Capacitor – shared mem for Claude Code, Cursor and other coding agents

> [!info] 一句话导读
> Hi HN! I’m Lokhesh, I am part of the Product and AI team at a small startup, Kurrent. We built Capacitor, and here’s honestly how it started:One night our Engin…

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=48734560>
> 指标：点赞=2 · 评论=2 · engagement_velocity=2
> 作者：lougarou　|　发布：2026-06-30T15:56:30Z
> 项目链接：<https://capacitor.kurrent.io/>
> 采集：2026-09-21T01:44:17+08:00　|　id：`aff8a1c001d12e7e`

## 正文

Hi HN! I’m Lokhesh, I am part of the Product and AI team at a small startup, Kurrent. We built Capacitor, and here’s honestly how it started:One night our Engineering Lead, Alexey, left Claude Code running overnight to finish a task. In the morning his machine had auto-updated the OS and his session was gone. No context, no record of what had been done, nothing. He dug into the Claude Code docs, learned about session resume and transcript files, and realized there’s an enormous amount in those transcripts that’s normally invisible. How the agent reasoned through the task. Every file change. Every tool call. Every failed command and dead end. All of it. Gold!That’s when he thought, ‘what if my machine dies and I lose all of that?’ And then, ‘what if I could share it with my team?’ That’s how Capacitor came to be.Capacitor records agent sessions (prompts, responses, tool calls, code changes, etc.) into an event store (KurrentDB under the hood). Each session gets a unique ID. You can resume it in any agent, on any machine, or hand it to a teammate without re-explaining everything.Here are some of the things we use it for:- Survive on restart
- Hand a session over from a desktop to a laptop when you need to travel
- Remember what I’ve done before (+ why and how)
- Ask a second opinion (from a human or agent)
- Share knowledge with peers
- Explain the reasoning behind the code written by an agent
- Hand over when I get sick or take a day offI’m doing this post because I’d love to get feedback from the HN community on how we can make Capacitor better. What works well? What could be improved? What should we add?Get it here: https://capacitor.kurrent.io/api/auth/start?tier=free
Check out the docs: https://capacitor.kurrent.io/docs/getting-started/quickstart...Note: We designed Capacitor as a cloud service to make setup easy, but are open to suggestions on how best to package it.

## 评论（2/2）

> **alexey_zim** · 2026-06-30T15:59:11.000Z　
> Hey, Alexey is here and if there are any questions or any feedback - I'm here to chat.

---

> **kgdunn1** · 2026-06-30T22:01:45.000Z　
> Looks interesting especially as I expect more models, more coding agents, more software and less time!

## 关联链接

- https://capacitor.kurrent.io/api/auth/start?tier=free
- https://capacitor.kurrent.io/docs/getting-started/quickstart...Note:

## 导航

- 项目页：[[10-项目/capacitor.kurrent.io_3365eef7]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
