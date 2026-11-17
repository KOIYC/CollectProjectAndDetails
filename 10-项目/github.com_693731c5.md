---
type: "project"
title: "Show HN: My OSS Claude Meetings alternative that works with any agent or call"
project_url: "https://github.com/wanderingstan/vibeconf-app"
first_seen: "2026-11-17T11:09:12+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_wanderingstan
  - story_50522602
  - show_hn
lang: "en"
---

# Show HN: My OSS Claude Meetings alternative that works with any agent or call

> [!info] 一句话导读
> Since February, I've been developing an agent-in-calls solution with a friend. With the announcement of Claude Meetings last week, it's now time to announce Vib…

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://github.com/wanderingstan/vibeconf-app>
> 首次收录：2026-11-17T11:09:12+08:00
> 来源渠道：HN Show HN
> 标签：author_wanderingstan, story_50522602, show_hn
> 最新指标：点赞=3 · 评论=1 · engagement_velocity=3

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-11-17T11:09:12+08:00 | HN Show HN | 点赞=3 · 评论=1 · engagement_velocity=3 | [[20-语料/posts/hn_show/2026-11-17/ce96a3517381f7fe_Show-HN-My-OSS-Claude-Meetings-alternative-that-wo]] |

## 摘要正文

Since February, I've been developing an agent-in-calls solution with a friend. With the announcement of Claude Meetings last week, it's now time to announce Vibeconferencing: an open-source project with even more functionality, support for any agent (Codex, Muse, local ollama, etc), and support for more calling platforms: Google Meet, Zoom, MS Teams, WhatsApp, Telegram, and phone calls (via Twilio).Architecture diagram: https://raw.githubusercontent.com/wanderingstan/vibeconf-app...The premise is simple: give your normal agent session the tools it needs to operate all major calling platforms, and teach it basic etiquette of how to behave in a call with others. A simple `/join-call` and boom! your session is talking to you in the call. Anything your agent can do in chat, it can do on the call. The agent is bridged to the calling platforms via a cross-platform electron app. (The raw guts of interacting with calling platforms is abstracted as the npm library `@vibeconferencing/calls`, if you'd rather roll your own.)Everything runs locally and uses your own local agent. (Tho the optional shared whiteboard feature does require being logged in on our server.) It runs on MacOS, Windows, a…
