---
type: "project"
title: "Show HN: ToolConfig – EditorConfig, extended to formatters and linters"
project_url: "https://github.com/mathematic-inc/toolconfig"
first_seen: "2026-10-27T23:46:32+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_jrandolf
  - story_50256602
  - show_hn
lang: "en"
---

# Show HN: ToolConfig – EditorConfig, extended to formatters and linters

> [!info] 一句话导读
> mathematic-inc/toolconfig

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://github.com/mathematic-inc/toolconfig>
> 首次收录：2026-10-27T23:46:32+08:00
> 来源渠道：HN Show HN
> 标签：author_jrandolf, story_50256602, show_hn
> 最新指标：点赞=2 · 评论=0 · engagement_velocity=2

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-10-27T23:46:32+08:00 | HN Show HN | 点赞=2 · 评论=0 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-10-27/05c1ae2e716af507_Show-HN-ToolConfig-–-EditorConfig,-extended-to-for]] |

## 摘要正文

# mathematic-inc/toolconfig  EditorConfig, extended to your tools: generate .editorconfig and native tool configuration from TOML or Pkl  - Stars: 1 - Forks: 0 - Watchers: 1 - Open issues: 0 - License: MIT License - Default branch: main - Created: 2026-10-27T09:17:58Z  ## Languages  - Python - Rust  ## Top Contributors  - jrandolf (5 contributions)  ---  ## README  # ToolConfig  crates.io license ci  EditorConfig, extended to your tools.  You write EditorConfig sections in TOML, plus a table of native options for each tool. ToolConfig generates the plain `.editorconfig` that editors read and each tool's own configuration file: `rustfmt.toml`, `ruff.toml`, `.prettierrc.json`, and so on. Indentation, line width and line endings are written once, and every tool receives them in its own keys, so editors, formatters and linters cannot disagree.  ```toml # .toolconfig.toml root = true  [toolconfig] tools = ["rustfmt", "prettier", "ruff"]  ["*"] end_of_line = "lf" insert_final_newline = true indent_style = "space" indent_size = 2 max_line_length = 100  ["*.{rs,py,pyi}"] indent_size = 4  ["*.rs"] rustfmt.edition = "2024"  ["*.md"] max_line_length = 80 prettier.proseWrap = "always"  ["*.{py…
