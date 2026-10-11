---
type: "project"
title: "Show HN: Chrome Relay – background tabs in your real Chrome for coding agents"
project_url: "https://github.com/aindeev/agent-chrome-relay"
first_seen: "2026-10-11T09:43:53+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_alexeyindeev
  - story_50030811
  - show_hn
lang: "en"
---

# Show HN: Chrome Relay – background tabs in your real Chrome for coding agents

> [!info] 一句话导读
> aindeev/agent-chrome-relay

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://github.com/aindeev/agent-chrome-relay>
> 首次收录：2026-10-11T09:43:53+08:00
> 来源渠道：HN Show HN
> 标签：author_alexeyindeev, story_50030811, show_hn
> 最新指标：点赞=7 · 评论=0 · engagement_velocity=7

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-10-11T09:43:53+08:00 | HN Show HN | 点赞=7 · 评论=0 · engagement_velocity=7 | [[20-语料/posts/hn_show/2026-10-11/6e1dc61b1a96c4ac_Show-HN-Chrome-Relay-–-background-tabs-in-your-rea]] |

## 摘要正文

# aindeev/agent-chrome-relay  Let your AI agents use your Chrome, signed in as you, in background tabs. By Alexey Indeev · blog: read.aindeev.com · X: @AlexeyIndeev  - Stars: 137 - Forks: 2 - Watchers: 137 - Open issues: 0 - License: MIT License - Homepage: https://agent-chrome-relay.aindeev.com - Default branch: main - Created: 2026-10-10T07:38:27Z  ## Languages  - JavaScript - Python  ## Topics  - agent-browser - ai-agents - browser-automation - cdp - chrome-extension - claude - claude-code - codex - cursor - macos - paseo  ## Top Contributors  - aindeev (6 contributions)  ---  ## README  # Chrome Relay  **Website:** https://agent-chrome-relay.aindeev.com  Lets your coding agents (Claude Code, Codex, Cursor, Paseo) use **your everyday Chrome**, with your real logins, from the command line, **in background tabs**: nothing takes focus, no dialogs, ~0.15s per command.  ```bash agent-browser --cdp "$(chrome-relay url you@company.com)" open https://app.example.com/ agent-browser snapshot -i          # the page's buttons, links and fields, each with a ref like @e5 agent-browser click @e5 agent-browser close ```  It's opt-in: nothing installs the extension for you, and it only runs on M…
