---
type: "project"
title: "Show HN: Texio, reliable Markdown operations for shell scripts and AI agents"
project_url: "https://github.com/Allra-Fintech/texio"
first_seen: "2026-09-20T09:36:55+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_yuzong
  - story_49736484
  - show_hn
lang: "en"
---

# Show HN: Texio, reliable Markdown operations for shell scripts and AI agents

> [!info] 一句话导读
> Reliable Markdown operations for shell scripts and AI agents

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://github.com/Allra-Fintech/texio>
> 首次收录：2026-09-20T09:36:55+08:00
> 来源渠道：HN Show HN
> 标签：author_yuzong, story_49736484, show_hn
> 最新指标：点赞=2 · 评论=0 · engagement_velocity=2

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-09-20T09:23:24+08:00 | HN Show HN | 点赞=2 · 评论=0 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-09-20/c9991863f5486f11_Show-HN-Texio,-reliable-Markdown-operations-for-sh]] |
| 2026-09-20T09:36:55+08:00 | HN Show HN | 点赞=2 · 评论=0 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-09-20/c9991863f5486f11_Show-HN-Texio,-reliable-Markdown-operations-for-sh]] |

## 摘要正文

# Allra-Fintech/texio  Reliable Markdown operations for shell scripts and AI agents  - Stars: 2 - Forks: 0 - Watchers: 2 - Open issues: 6 - License: MIT License - Default branch: develop - Created: 2026-09-03T06:53:29Z  ## Languages  - Python - Rust - Shell  ## Topics  - ai-agents - cli - coding-agents - commonmark - document-automation - github-flavored-markdown - markdown - rust  ## Top Contributors  - JonghunYu (37 contributions)  ---  ## README  # Texio  Reliable Markdown operations for shell scripts and AI agents.  Texio extracts and surgically edits Markdown by document structure. Use it when regular expressions are unsafe and rewriting the complete file would create unnecessary changes.  > `grep` finds text. `sed` changes text. Texio understands Markdown.  ## Extract a Markdown section  Install from crates.io with a current stable Rust toolchain, or use the platform-specific binary instructions.  ```sh cargo install texio-cli --locked texio --version ```  Create a small document and inspect its structure:  ```sh printf '# Demo\n\n## Installation\nold command\n\n## Usage\nkeep this\n' > demo.md texio headings demo.md --json texio section demo.md Installation ```  Preview one …
