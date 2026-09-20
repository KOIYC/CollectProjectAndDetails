---
type: "project"
title: "Show HN: Jeff – A read-only CLI for semantic code review using Jev"
project_url: "https://github.com/Alurith/jeff"
first_seen: "2026-09-20T14:02:12+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_imalessandro
  - story_49757757
  - show_hn
lang: "en"
---

# Show HN: Jeff – A read-only CLI for semantic code review using Jev

> [!info] 一句话导读
> Catch code issues before they catch you.

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://github.com/Alurith/jeff>
> 首次收录：2026-09-20T14:02:12+08:00
> 来源渠道：HN Show HN
> 标签：author_imalessandro, story_49757757, show_hn
> 最新指标：点赞=26 · 评论=4 · engagement_velocity=26

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-09-20T09:23:24+08:00 | HN Show HN | 点赞=26 · 评论=4 · engagement_velocity=26 | [[20-语料/posts/hn_show/2026-09-20/064321616114d82c_Show-HN-Jeff-–-A-read-only-CLI-for-semantic-code-r]] |
| 2026-09-20T09:36:37+08:00 | HN Show HN | 点赞=26 · 评论=4 · engagement_velocity=26 | [[20-语料/posts/hn_show/2026-09-20/064321616114d82c_Show-HN-Jeff-–-A-read-only-CLI-for-semantic-code-r]] |
| 2026-09-20T14:02:12+08:00 | HN Show HN | 点赞=26 · 评论=4 · engagement_velocity=26 | [[20-语料/posts/hn_show/2026-09-20/064321616114d82c_Show-HN-Jeff-–-A-read-only-CLI-for-semantic-code-r]] |

## 摘要正文

# Alurith/jeff  Catch code issues before they catch you.  - Stars: 30 - Forks: 1 - Watchers: 30 - Open issues: 0 - Default branch: master - Created: 2026-09-18T14:13:58Z  ## Languages  - Go - Just  ## Topics  - golang - jev  ## Top Contributors  - Alurith (5 contributions)  ---  ## README  # jeff  **Catch code issues before they catch you.**  A read-only Go CLI that semantically checks your files against your rules using Jev, locally or in CI.  ## Usage  ```sh # Check files in the current directory or at the provided paths jeff check [--output-format text|json] [--no-cache] [PATH...]  # Store or remove the TypeSafe credential jeff auth login jeff auth logout ```  ## Authentication and configuration  Set `TYPESAFE_API_KEY` or store a credential with `jeff auth login`. Stored credentials use the operating system's keyring; `jeff auth logout` removes the saved credential.  Use `TYPESAFE_BASE_URL` to point to a compatible endpoint during testing.  ## Current rules  | Code | Rule | Description | | --- | --- | --- | | `GEN001` | Unclear responsibility | Finds files that mix unrelated responsibilities. | | `GEN002` | Misleading naming | Finds important names that do not match their behavi…
