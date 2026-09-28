---
type: "project"
title: "Show HN: swe-mux – A terminal multiplexer for coding agents optimized for mobile"
project_url: "https://github.com/jatoran/swe-mux"
first_seen: "2026-09-28T09:47:28+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_jatora
  - story_49867905
  - show_hn
lang: "en"
---

# Show HN: swe-mux – A terminal multiplexer for coding agents optimized for mobile

> [!info] 一句话导读
> I run a lot of coding agents at once, mostly Claude Code, Codex and pi, across several projects. I got tired of having so many windows open, of agents leaving h…

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://github.com/jatoran/swe-mux>
> 首次收录：2026-09-28T09:47:28+08:00
> 来源渠道：HN Show HN
> 标签：author_jatora, story_49867905, show_hn
> 最新指标：点赞=3 · 评论=0 · engagement_velocity=3

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-09-28T09:47:28+08:00 | HN Show HN | 点赞=3 · 评论=0 · engagement_velocity=3 | [[20-语料/posts/hn_show/2026-09-28/9d4ad25f3b265777_Show-HN-swe-mux-–-A-terminal-multiplexer-for-codin]] |

## 摘要正文

I run a lot of coding agents at once, mostly Claude Code, Codex and pi, across several projects. I got tired of having so many windows open, of agents leaving hung processes behind, of tracking which one needed input, and of having to remote into my desktop or SSH into a single shell to manage them from my phone. Even then, a terminal on a phone couldn't show me the frontend or output I needed to verify the work. I tried Orca and herdr. Both were better than my setup, but neither had a real WYSIWYG markdown notes surface, and neither had a phone interface I could actually work in.swe-mux is the terminal multiplexer I built for that. It runs any shell or CLI in real terminals on your own machine and serves the same live sessions to your desktop and your phone. It's built around agents: Claude Code, Codex, opencode, pi and oh-my-pi get a live status (working, done, or waiting on you), searchable history and resume. Anything else runs as an ordinary terminal with everything except the status.This is the actual terminal and not a UI wrapped around the agent, and you can just use it that way, or start claude in a plain shell and that pane becomes an agent session.On the desktop it's pan…
