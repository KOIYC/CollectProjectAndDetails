---
type: "project"
title: "Show HN: Capacitor – shared mem for Claude Code, Cursor and other coding agents"
project_url: "https://capacitor.kurrent.io/"
first_seen: "2026-09-21T01:44:17+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_lougarou
  - story_48734560
  - show_hn
lang: "en"
---

# Show HN: Capacitor – shared mem for Claude Code, Cursor and other coding agents

> [!info] 一句话导读
> Hi HN! I’m Lokhesh, I am part of the Product and AI team at a small startup, Kurrent. We built Capacitor, and here’s honestly how it started:One night our Engin…

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://capacitor.kurrent.io/>
> 首次收录：2026-09-21T01:44:17+08:00
> 来源渠道：HN Show HN
> 标签：author_lougarou, story_48734560, show_hn
> 最新指标：点赞=2 · 评论=2 · engagement_velocity=2

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-09-21T01:29:55+08:00 | HN Show HN | 点赞=2 · 评论=2 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-09-21/aff8a1c001d12e7e_Show-HN-Capacitor-–-shared-mem-for-Claude-Code,-Cu]] |
| 2026-09-21T01:44:17+08:00 | HN Show HN | 点赞=2 · 评论=2 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-09-21/aff8a1c001d12e7e_Show-HN-Capacitor-–-shared-mem-for-Claude-Code,-Cu]] |

## 摘要正文

Hi HN! I’m Lokhesh, I am part of the Product and AI team at a small startup, Kurrent. We built Capacitor, and here’s honestly how it started:One night our Engineering Lead, Alexey, left Claude Code running overnight to finish a task. In the morning his machine had auto-updated the OS and his session was gone. No context, no record of what had been done, nothing. He dug into the Claude Code docs, learned about session resume and transcript files, and realized there’s an enormous amount in those transcripts that’s normally invisible. How the agent reasoned through the task. Every file change. Every tool call. Every failed command and dead end. All of it. Gold!That’s when he thought, ‘what if my machine dies and I lose all of that?’ And then, ‘what if I could share it with my team?’ That’s how Capacitor came to be.Capacitor records agent sessions (prompts, responses, tool calls, code changes, etc.) into an event store (KurrentDB under the hood). Each session gets a unique ID. You can resume it in any agent, on any machine, or hand it to a teammate without re-explaining everything.Here are some of the things we use it for:- Survive on restart - Hand a session over from a desktop to a l…
