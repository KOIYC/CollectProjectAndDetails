---
type: "project"
title: "Show HN: Stop parallel AI coding sessions clobbering each other's handoffs"
project_url: "https://github.com/joshduffy/claude-handoff-guard"
first_seen: "2026-09-21T02:52:58+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_nahsuhn
  - story_48325871
  - show_hn
lang: "en"
---

# Show HN: Stop parallel AI coding sessions clobbering each other's handoffs

> [!info] 一句话导读
> joshduffy/claude-handoff-guard

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://github.com/joshduffy/claude-handoff-guard>
> 首次收录：2026-09-21T02:52:58+08:00
> 来源渠道：HN Show HN
> 标签：author_nahsuhn, story_48325871, show_hn
> 最新指标：点赞=2 · 评论=0 · engagement_velocity=2

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-09-21T01:27:24+08:00 | HN Show HN | 点赞=2 · 评论=0 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-09-21/c325ab78f52a497c_Show-HN-Stop-parallel-AI-coding-sessions-clobberin]] |
| 2026-09-21T02:52:58+08:00 | HN Show HN | 点赞=2 · 评论=0 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-09-21/c325ab78f52a497c_Show-HN-Stop-parallel-AI-coding-sessions-clobberin]] |

## 摘要正文

# joshduffy/claude-handoff-guard  Hook-enforced ownership for AI coding session handoffs  - Stars: 0 - Forks: 0 - Watchers: 0 - Open issues: 0 - License: MIT License - Default branch: master - Created: 2026-05-29T04:28:12Z  ## Languages  - JavaScript - Shell  ## Top Contributors  - joshduffy (2 contributions)  ---  ## README  # claude-handoff-guard  Hook-enforced ownership for AI coding session handoffs.  Most "handoff" tools solve *amnesia*: capture state to a markdown file, restore it after compaction or a new session. That problem is well covered. This one solves the problem nobody enforces: **concurrent clobber**. When two sessions work the same repo, or you resume on a second machine, or a background agent runs alongside an interactive one, they overwrite each other's handoff notes and you do not find out until the context you needed is gone.  The fix here is not a better template. It is a PreToolUse hook that makes a cross-session overwrite *structurally* blocked, not merely discouraged.  ## The core idea: the lock lives inside the file  Every handoff file's first line is an ownership marker:  ``` <!-- claude-session: 9e0d3802-... --> ```  There is no sidecar `.lock` file. Ow…
