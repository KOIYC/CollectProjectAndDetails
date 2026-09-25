---
type: "project"
title: "Show HN: Resume Claude Code subagents killed by a usage limit, don't redo them"
project_url: "https://github.com/error0702/agent-limit-retry"
first_seen: "2026-09-24T23:57:22+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_autorunfun
  - story_49831324
  - show_hn
lang: "en"
---

# Show HN: Resume Claude Code subagents killed by a usage limit, don't redo them

> [!info] 一句话导读
> error0702/agent-limit-retry

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://github.com/error0702/agent-limit-retry>
> 首次收录：2026-09-24T23:57:22+08:00
> 来源渠道：HN Show HN
> 标签：author_autorunfun, story_49831324, show_hn
> 最新指标：点赞=2 · 评论=0 · engagement_velocity=2

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-09-24T23:57:22+08:00 | HN Show HN | 点赞=2 · 评论=0 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-09-24/a20158dc1804abe3_Show-HN-Resume-Claude-Code-subagents-killed-by-a-u]] |

## 摘要正文

# error0702/agent-limit-retry  Keep Claude Code working through usage limits: exact reset times, handoff before the limit, headless runs that resume after the reset. MIT.  - Stars: 0 - Forks: 0 - Watchers: 0 - Open issues: 0 - License: MIT License - Homepage: https://retry.autorun.fun - Default branch: main - Created: 2026-09-24T05:25:33Z  ## Languages  - JavaScript  ## Topics  - ai-agents - claude - claude-code - cli - codex - plugin - rate-limit - usage-limit  ## Top Contributors  - error0702 (5 contributions)  ---  ## README  # agent-limit-retry  **Keep Claude Code working through usage limits.** Know the exact reset time, hand off before the limit hits, and run headless jobs that sleep through the reset and resume themselves.  npm license node Pro  中文说明  ```bash npx agent-limit-retry    # one question, then the plugin is installed and the status line is tapped alr selftest                      # simulated limit hit + resume against a local fake API; no quota spent alr status                        # your 5-hour / 7-day windows, reset times, recent limit hits ```  alr selftest and alr status  Restart Claude Code after installing. Everything runs locally: no proxy, no account, no…
