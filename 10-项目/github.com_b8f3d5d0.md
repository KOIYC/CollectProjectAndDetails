---
type: "project"
title: "Show HN: Clanking – Turn your coding agents' activity into a subtle soundscape"
project_url: "https://github.com/chrchr/clanking"
first_seen: "2026-10-10T09:53:50+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_chrchr
  - story_50027932
  - show_hn
lang: "en"
---

# Show HN: Clanking – Turn your coding agents' activity into a subtle soundscape

> [!info] 一句话导读
> Turn agent activity into a quiet soundscape.

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://github.com/chrchr/clanking>
> 首次收录：2026-10-10T09:53:50+08:00
> 来源渠道：HN Show HN
> 标签：author_chrchr, story_50027932, show_hn
> 最新指标：点赞=2 · 评论=0 · engagement_velocity=2

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-10-10T09:53:50+08:00 | HN Show HN | 点赞=2 · 评论=0 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-10-10/ec1b386501efc88d_Show-HN-Clanking-–-Turn-your-coding-agents'-activi]] |

## 摘要正文

# chrchr/clanking  Turn agent activity into a quiet soundscape.  - Stars: 1 - Forks: 0 - Watchers: 1 - Open issues: 0 - License: MIT License - Default branch: main - Created: 2026-10-09T20:19:52Z  ## Languages  - Dockerfile - Go - Makefile - Shell  ## Top Contributors  - chrchr (104 contributions)  ---  ## README  # What's that *Clanking* sound?  For machines called "clankers", LLM agents sure don't make much noise. Are they *too* quiet? Yes! But not anymore.  Clanking turns your LLM agents' activity into a subtle soundscape. It signals when an agent is working, waiting for input, or in another state. Clanking plays cues from many agents at once and harmonizes them into a happy chorus of chattering clankers.  ## Demo  https://github.com/user-attachments/assets/437b30b0-3852-4670-b634-daad4949b651  ## Design  Coding agent hooks invoke the Clanking CLI, which reads each hook event and plays a sound cue. For tool calls, it plays a short tick on one of several notes to signal that the agent is active. Other sounds indicate that the agent is outputting a response, waiting for input or permission, has finished, or has encountered an error.  Clanking runs as a daemon that starts on its fi…
