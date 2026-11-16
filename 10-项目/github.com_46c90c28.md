---
type: "project"
title: "Show HN: Claudette - Mistral models in Claude Code"
project_url: "https://github.com/raed667/claudette"
first_seen: "2026-11-16T10:00:05+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_Raed667
  - story_50508283
  - show_hn
lang: "en"
---

# Show HN: Claudette - Mistral models in Claude Code

> [!info] 一句话导读
> Claude Code + Mistral = 🧡

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://github.com/raed667/claudette>
> 首次收录：2026-11-16T10:00:05+08:00
> 来源渠道：HN Show HN
> 标签：author_Raed667, story_50508283, show_hn
> 最新指标：点赞=3 · 评论=1 · engagement_velocity=3

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-11-16T10:00:05+08:00 | HN Show HN | 点赞=3 · 评论=1 · engagement_velocity=3 | [[20-语料/posts/hn_show/2026-11-16/5d99e641848349e5_Show-HN-Claudette-Mistral-models-in-Claude-Code]] |

## 摘要正文

# raed667/claudette  Claude Code + Mistral = 🧡  - Stars: 1 - Forks: 0 - Watchers: 1 - Open issues: 0 - License: MIT License - Default branch: main - Created: 2026-11-15T13:27:25Z  ## Languages  - Python - Shell  ## Topics  - claude - claude-ai - claude-code - mistral - mistral-ai - mistral-api - mistral-large - mistralai  ## Top Contributors  - raed667 (2 contributions)  ---  ## README  # claudette  Run Claude Code with Mistral models.  `claudette` is a drop-in wrapper around `claude`. It starts a small local proxy that translates Claude Code's requests for Mistral's API, then runs `claude` against it. It keeps its own config directory, so your regular Claude Code setup, login and history are left alone.  Anthropic doesn't support running Claude Code on non-Claude models, so treat this as best-effort. The limitations are listed below.  ## Requirements  - Claude Code - uv - A Mistral API key from console.mistral.ai  Tested on macOS. Linux should work but hasn't been tested, and Windows isn't supported.  ## Install  ```sh curl -fsSL https://raw.githubusercontent.com/raed667/claudette/main/install.sh | bash ```  The installer asks for your Mistral API key and stores it in `~/.config/c…
