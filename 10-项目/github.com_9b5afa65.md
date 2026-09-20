---
type: "project"
title: "Show HN: Jev-lint – semantic linter with plain English rules"
project_url: "https://github.com/zdenham/jev-lint"
first_seen: "2026-09-20T09:48:16+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_zdenham
  - story_49771155
  - show_hn
lang: "en"
---

# Show HN: Jev-lint – semantic linter with plain English rules

> [!info] 一句话导读
> Lint JavaScript and TypeScript against plain-English project conventions with Jev.

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://github.com/zdenham/jev-lint>
> 首次收录：2026-09-20T09:48:16+08:00
> 来源渠道：HN Show HN
> 标签：author_zdenham, story_49771155, show_hn
> 最新指标：点赞=4 · 评论=0 · engagement_velocity=4

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-09-20T09:23:24+08:00 | HN Show HN | 点赞=4 · 评论=0 · engagement_velocity=4 | [[20-语料/posts/hn_show/2026-09-20/a67062d29c8417fb_Show-HN-Jev-lint-–-semantic-linter-with-plain-Engl]] |
| 2026-09-20T09:36:34+08:00 | HN Show HN | 点赞=4 · 评论=0 · engagement_velocity=4 | [[20-语料/posts/hn_show/2026-09-20/a67062d29c8417fb_Show-HN-Jev-lint-–-semantic-linter-with-plain-Engl]] |
| 2026-09-20T09:48:16+08:00 | HN Show HN | 点赞=4 · 评论=0 · engagement_velocity=4 | [[20-语料/posts/hn_show/2026-09-20/a67062d29c8417fb_Show-HN-Jev-lint-–-semantic-linter-with-plain-Engl]] |

## 摘要正文

# zdenham/jev-lint  Lint JavaScript and TypeScript against plain-English project conventions with Jev.  - Stars: 1 - Forks: 0 - Watchers: 1 - Open issues: 0 - Default branch: main - Created: 2026-09-19T22:59:50Z  ## Languages  - TypeScript  ## Top Contributors  - zdenham (6 contributions)  ---  ## README  # jev-lint  Check JavaScript and TypeScript against project conventions written in plain English. Define inline or Markdown rules; Jev reports possible violations. Built for coding agents, with compact output by default and optional pretty or JSON output.  Early release: review findings before making them block CI. Checks use whole-file context without resolving imports, locate top-level declarations or class members, and count uncertain results separately from compliance. The tool does not edit code.  ## Install and set up  Requires Node.js **22.22+** and Git:  ```sh git clone https://github.com/zdenham/jev-lint.git cd jev-lint npm ci npm run build npm link ```  The global command links to this checkout; keep it in place. If needed, add npm's global executable directory to PATH (`$(npm prefix --global)/bin` on macOS/Linux). Update with `git pull`, `npm ci`, and `npm run build`; r…
