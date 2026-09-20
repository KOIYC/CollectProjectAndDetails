---
type: "project"
title: "Show HN: Jev helps you to not run malicous code"
project_url: "https://github.com/luantak/is-malicious"
first_seen: "2026-09-20T09:36:38+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_lu4p
  - story_49756921
  - show_hn
lang: "en"
---

# Show HN: Jev helps you to not run malicous code

> [!info] 一句话导读
> luantak/is-malicious

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://github.com/luantak/is-malicious>
> 首次收录：2026-09-20T09:36:38+08:00
> 来源渠道：HN Show HN
> 标签：author_lu4p, story_49756921, show_hn
> 最新指标：点赞=2 · 评论=0 · engagement_velocity=2

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-09-20T09:23:24+08:00 | HN Show HN | 点赞=2 · 评论=0 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-09-20/3b2ff37d7c401b9b_Show-HN-Jev-helps-you-to-not-run-malicous-code]] |
| 2026-09-20T09:36:38+08:00 | HN Show HN | 点赞=2 · 评论=0 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-09-20/3b2ff37d7c401b9b_Show-HN-Jev-helps-you-to-not-run-malicous-code]] |

## 摘要正文

# luantak/is-malicious  A codebase scanner that helps you not run malicous code  - Stars: 13 - Forks: 1 - Watchers: 13 - Open issues: 0 - License: MIT License - Default branch: master - Created: 2026-09-18T11:40:17Z  ## Languages  - JavaScript - Shell - TypeScript  ## Topics  - jev - security-scanner - typesafe-ai  ## Top Contributors  - luantak (16 contributions)  ---  ## README  # is-malicious?  Scan a codebase for hidden, deceptive, or data-stealing behavior with TypeSafe Jev. The CLI sends source, configuration, build, and CI files to Jev for review, then points you to suspicious files and lines.  Use it as a second opinion before running unfamiliar code. A clean report is not proof that a project is safe.  ## Quick start  You need Node.js 20 or later and a TypeSafe API key.  ```bash export TYPESAFE_API_KEY=your-api-key npx is-malicious /path/to/project ```  Omit the path to scan the current directory. Scans send file contents to the TypeSafe API and use paid input tokens. The report includes token usage and a calculated input cost.  To install the CLI globally:  ```bash npm install -g is-malicious is-malicious /path/to/project ```  ## Reading the report  Findings include a fil…
