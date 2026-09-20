---
type: "project"
title: "Show HN: I built a PDF accessibility checker that is cross platform"
project_url: "https://github.com/visionably/outloud"
first_seen: "2026-09-20T14:02:40+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_yashbhatnagar
  - story_49750366
  - show_hn
lang: "en"
---

# Show HN: I built a PDF accessibility checker that is cross platform

> [!info] 一句话导读
> What a PDF says out loud. The PDF accessibility checker that runs anywhere: PDF/UA-1 + WCAG 2.2 in your terminal, CI and browser, plus the semantic checks valid…

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://github.com/visionably/outloud>
> 首次收录：2026-09-20T14:02:40+08:00
> 来源渠道：HN Show HN
> 标签：author_yashbhatnagar, story_49750366, show_hn
> 最新指标：点赞=3 · 评论=1 · engagement_velocity=3

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-09-20T09:23:24+08:00 | HN Show HN | 点赞=3 · 评论=1 · engagement_velocity=3 | [[20-语料/posts/hn_show/2026-09-20/65f02bf67c92ae2b_Show-HN-I-built-a-PDF-accessibility-checker-that-i]] |
| 2026-09-20T09:36:42+08:00 | HN Show HN | 点赞=3 · 评论=1 · engagement_velocity=3 | [[20-语料/posts/hn_show/2026-09-20/65f02bf67c92ae2b_Show-HN-I-built-a-PDF-accessibility-checker-that-i]] |
| 2026-09-20T14:02:40+08:00 | HN Show HN | 点赞=3 · 评论=1 · engagement_velocity=3 | [[20-语料/posts/hn_show/2026-09-20/65f02bf67c92ae2b_Show-HN-I-built-a-PDF-accessibility-checker-that-i]] |

## 摘要正文

# visionably/outloud  What a PDF says out loud. The PDF accessibility checker that runs anywhere: PDF/UA-1 + WCAG 2.2 in your terminal, CI and browser, plus the semantic checks validators cannot make.  - Stars: 7 - Forks: 0 - Watchers: 7 - Open issues: 0 - License: Apache License 2.0 - Homepage: https://visionably.ai/research/outloud - Default branch: main - Created: 2026-09-17T10:15:17Z  ## Languages  - Python  ## Topics  - a11y - accessibility - cli - matterhorn-protocol - pdf - pdf-accessibility - pdf-ua - python - sarif - screen-reader - wcag - wcag22  ## Top Contributors  - superzackx (6 contributions)  ---  ## README   What a PDF says out loud.   The PDF accessibility checker that runs anywhere: PDF/UA-1 and WCAG 2.2, in your terminal, your CI and your browser.  It finds what validators find, and then what they cannot.  ```bash pipx install outloud          # or: uv tool install outloud outloud report.pdf            # check it outloud --view                # or open the app and drop files in ```  No Java. No Windows. No upload. Nothing leaves your machine.  ---  ## Why  The standard tools for checking a PDF's accessibility are **PAC**, which is a Windows desktop program, and …
