---
type: "project"
title: "Show HN: Jev-align, a CLI to calibrate Jev to your judgement"
project_url: "https://github.com/sutro-sh/jev-align"
first_seen: "2026-09-20T09:48:16+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_sethkim
  - story_49770872
  - show_hn
lang: "en"
---

# Show HN: Jev-align, a CLI to calibrate Jev to your judgement

> [!info] 一句话导读
> Build calibrated AI classifiers from human feedback using Jev and GEPA.

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://github.com/sutro-sh/jev-align>
> 首次收录：2026-09-20T09:48:16+08:00
> 来源渠道：HN Show HN
> 标签：author_sethkim, story_49770872, show_hn
> 最新指标：点赞=2 · 评论=0 · engagement_velocity=2

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-09-20T09:23:24+08:00 | HN Show HN | 点赞=2 · 评论=0 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-09-20/f1c17f6fd2e7c94c_Show-HN-Jev-align,-a-CLI-to-calibrate-Jev-to-your]] |
| 2026-09-20T09:36:34+08:00 | HN Show HN | 点赞=2 · 评论=0 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-09-20/f1c17f6fd2e7c94c_Show-HN-Jev-align,-a-CLI-to-calibrate-Jev-to-your]] |
| 2026-09-20T09:48:16+08:00 | HN Show HN | 点赞=2 · 评论=0 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-09-20/f1c17f6fd2e7c94c_Show-HN-Jev-align,-a-CLI-to-calibrate-Jev-to-your]] |

## 摘要正文

# sutro-sh/jev-align  Build calibrated AI classifiers from human feedback using Jev and GEPA.  - Stars: 132 - Forks: 10 - Watchers: 132 - Open issues: 0 - License: Apache License 2.0 - Homepage: https://pypi.org/project/jev-align/ - Default branch: main - Created: 2026-09-19T02:12:23Z  ## Languages  - Makefile - Python - Shell  ## Topics  - active-learning - classification - cli - gepa - human-in-the-loop - jev - prompt-optimization - typesafe-ai  ## Top Contributors  - sethkimmel3 (21 contributions)  ---  ## README  # jev-align  `jev-align` is an experimental CLI from Sutro for building AI Functions with TypeSafe's Jev.  It finds uncertain examples, asks you to label them, and uses GEPA to improve the function. Use it in your application and keep learning from production examples.  ## Demo  https://github.com/user-attachments/assets/81650587-e3f1-4655-8213-ed5f6e120e9a  ## Quick start  Requires Python 3.11 or newer.  ```shell uv tool install jev-align export TYPESAFE_API_KEY="..." # Or use Vercel or Cloudflare below export OPENAI_API_KEY="..." # or ANTHROPIC_API_KEY / GEMINI_API_KEY jeva ```  Start the CLI with either `jeva` or `jev-align`.  Use `pip install jev-align` if you do n…
