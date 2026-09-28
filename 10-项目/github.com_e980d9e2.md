---
type: "project"
title: "Show HN: Drive your Chrome window from shell (use with Claude)"
project_url: "https://github.com/borisreitman/browser-session-ctl"
first_seen: "2026-09-28T09:47:28+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_boris1
  - story_49868143
  - show_hn
lang: "en"
---

# Show HN: Drive your Chrome window from shell (use with Claude)

> [!info] 一句话导读
> borisreitman/browser-session-ctl

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://github.com/borisreitman/browser-session-ctl>
> 首次收录：2026-09-28T09:47:28+08:00
> 来源渠道：HN Show HN
> 标签：author_boris1, story_49868143, show_hn
> 最新指标：点赞=3 · 评论=0 · engagement_velocity=3

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-09-28T09:47:28+08:00 | HN Show HN | 点赞=3 · 评论=0 · engagement_velocity=3 | [[20-语料/posts/hn_show/2026-09-28/eb1f3a833322490c_Show-HN-Drive-your-Chrome-window-from-shell-(use-w]] |

## 摘要正文

# borisreitman/browser-session-ctl  Control your browser session  - Stars: 0 - Forks: 0 - Watchers: 0 - Open issues: 0 - License: GNU General Public License v3.0 - Default branch: main - Created: 2026-09-07T01:35:43Z  ## Languages  - CSS - HTML - JavaScript  ## Top Contributors  - anonymouscommitter (27 contributions)  ---  ## README  # browser-session-ctl  Drive the Chrome window you already have open from the shell — including third-party sites you do not own.  This is not Selenium. Selenium starts a new browser. This loads an unpacked extension into your current session, so a local agent can click, type, and read the same tabs, cookies, and logins you are already using.  This makes it well suited to pairing with an AI coding agent — Claude Code, Cursor, or similar — that already runs shell commands on your machine. Rather than the agent driving a separate, logged-out browser instance, it drives the same Chrome window and tabs you have open, with your existing sessions, so it can read a page you're looking at, fill a form on a site you're already signed into, or hand off a browser task mid-flow without you re-authenticating anywhere.  ``` you / agent  --HTTP-->  sidecar :8765  --…
