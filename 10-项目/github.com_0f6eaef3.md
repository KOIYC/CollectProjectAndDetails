---
type: "project"
title: "Show HN: Intent-lens – see what Claude Code is about to do, before it does it"
project_url: "https://github.com/Dhananjay-JSR/claude-mods/tree/main/plugins/intent-lens"
first_seen: "2026-11-03T09:40:36+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_dhananjay-jsr
  - story_50341363
  - show_hn
lang: "en"
---

# Show HN: Intent-lens – see what Claude Code is about to do, before it does it

> [!info] 一句话导读
> claude-mods/plugins/intent-lens at main · Dhananjay-JSR/claude-mods

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://github.com/Dhananjay-JSR/claude-mods/tree/main/plugins/intent-lens>
> 首次收录：2026-11-03T09:40:36+08:00
> 来源渠道：HN Show HN
> 标签：author_dhananjay-jsr, story_50341363, show_hn
> 最新指标：点赞=2 · 评论=1 · engagement_velocity=2

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-11-03T09:40:36+08:00 | HN Show HN | 点赞=2 · 评论=1 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-11-03/84b380aca78dc647_Show-HN-Intent-lens-–-see-what-Claude-Code-is-abou]] |

## 摘要正文

claude-mods/plugins/intent-lens at main · Dhananjay-JSR/claude-mods · GitHub  ## Folders and files  | Name | Name | Last commit message | Last commit date | | --- | --- | --- | --- | | parent directory.. | | | | | .claude-plugin | .claude-plugin | | | | assets | assets | | | | hooks | hooks | | | | tests | tests | | | | README.md | README.md | | | | tsconfig.json | tsconfig.json | | | | View all files | | | |  ## README.md  # intent-lens  See what Claude is about to do — before it does it.   Part of the claude-mods marketplace.   A real Claude Code session with intent-lens loaded.  A Claude Mod that shows the intent of a tool call in one line above the prompt, while the call is still pending.  Claude Code shows you a tool row after Claude has already decided to act. `intent-lens` translates the call into a human sentence first, in the place your eyes already are. It reads either the tool's own arguments (free, instant) or asks Claude to phrase it (a few tokens).  ## Why  In auto mode, Claude Code moves faster than you can read, and the commands it writes are made for the shell, not for you. A `find | xargs | awk` pipeline tells you almost nothing at a glance, and once it runs, the …
