---
type: "project"
title: "Show HN: OpenCode2 HUD"
project_url: "https://github.com/ndom91/opencode-hud"
first_seen: "2026-09-21T03:11:29+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_ndom91
  - story_49500245
  - show_hn
lang: "en"
---

# Show HN: OpenCode2 HUD

> [!info] 一句话导读
> OpenCode2 plugin to show more detailed state below the text input

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://github.com/ndom91/opencode-hud>
> 首次收录：2026-09-21T03:11:29+08:00
> 来源渠道：HN Show HN
> 标签：author_ndom91, story_49500245, show_hn
> 最新指标：点赞=2 · 评论=0 · engagement_velocity=2

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-09-21T01:33:52+08:00 | HN Show HN | 点赞=2 · 评论=0 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-09-21/75db65a88b83b998_Show-HN-OpenCode2-HUD]] |
| 2026-09-21T03:11:29+08:00 | HN Show HN | 点赞=2 · 评论=0 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-09-21/75db65a88b83b998_Show-HN-OpenCode2-HUD]] |

## 摘要正文

# ndom91/opencode-hud  OpenCode2 plugin to show more detailed state below the text input  - Stars: 1 - Forks: 0 - Watchers: 1 - Open issues: 0 - License: MIT License - Default branch: main - Created: 2026-08-29T12:33:06Z  ## Languages  - TypeScript  ## Topics  - hud - opencode - opencode-plugin  ## Top Contributors  - ndom91 (46 contributions)  ---  ## README  # OpenCode HUD  npm version npm downloads license OpenCode 2 plugin  OpenCode 2 plugin that displays a persistent status HUD below the text input in the TUI. It is a native TUI plugin, not an assistant-message renderer, so it does not add HUD content to a session transcript.  ## Install  Add it to the `plugins` array in `~/.config/opencode/cli.json`, for example:  ```json {   "plugins": [     "@ndom91/opencode-hud"   ] } ```  OpenCode downloads and loads the package. Restart OpenCode after changing the configuration.  > [!WARNING] > To show `5h` and `weekly` Codex subscription usage, the HUD plugin queries the OpenAI endpoint through > your system's Codex authorization. This is disabled by default. See PRIVACY.md before > enabling it with the `codexUsage` package option. This is the same mechanism as used by > CodexBar and ot…
