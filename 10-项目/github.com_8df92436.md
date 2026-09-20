---
type: "project"
title: "Show HN: SlideOps – slides from a repo that flag when they drift from the code"
project_url: "https://github.com/glukicov/slideops"
first_seen: "2026-09-21T02:56:42+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_lukicov
  - story_49508735
  - show_hn
lang: "en"
---

# Show HN: SlideOps – slides from a repo that flag when they drift from the code

> [!info] 一句话导读
> I kept generating slide decks about my codebases with an agent, and weeks later they would go stale. Updating them was quite costly (time & tokens), as the agen…

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://github.com/glukicov/slideops>
> 首次收录：2026-09-21T02:56:42+08:00
> 来源渠道：HN Show HN
> 标签：author_lukicov, story_49508735, show_hn
> 最新指标：点赞=23 · 评论=5 · engagement_velocity=23

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-09-21T01:33:52+08:00 | HN Show HN | 点赞=23 · 评论=5 · engagement_velocity=23 | [[20-语料/posts/hn_show/2026-09-21/82463f79ae7eee80_Show-HN-SlideOps-–-slides-from-a-repo-that-flag-wh]] |
| 2026-09-21T02:56:42+08:00 | HN Show HN | 点赞=23 · 评论=5 · engagement_velocity=23 | [[20-语料/posts/hn_show/2026-09-21/82463f79ae7eee80_Show-HN-SlideOps-–-slides-from-a-repo-that-flag-wh]] |

## 摘要正文

I kept generating slide decks about my codebases with an agent, and weeks later they would go stale. Updating them was quite costly (time & tokens), as the agent would have to re-scan the whole repo to re-generate the slides. So I made the slide deck carry its own provenance: SlideOps skill turns a repo into a slide deck, with all references to files carrying exact line range and a hash.Checking is done with standard-library Python: no model calls, no network, and very fast. For example, it distinguishes MOVED (the code shifted) from CHANGED (the content differs). Updating the slides costs tokens, but now the checking part has already given the agent just the relevant context on what exactly needs to be repaired.SlideOps ships as a Claude Code plugin and runs as a plain agent skill in Codex, Copilot CLI and OpenCode.Longer write-up: https://medium.com/@lukicov/your-documentation-is-a-build-ar...GitHub repo: https://github.com/glukicov/slideops
