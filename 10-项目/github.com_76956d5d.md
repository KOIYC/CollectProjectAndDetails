---
type: "project"
title: "Show HN: Eulix - Code navigation for large codebases"
project_url: "https://github.com/Nurysso/eulix"
first_seen: "2026-09-20T09:41:47+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_Nurysso
  - story_49714268
  - show_hn
lang: "en"
---

# Show HN: Eulix - Code navigation for large codebases

> [!info] 一句话导读
> Show HN: Eulix - Code navigation for large codebases

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://github.com/Nurysso/eulix>
> 首次收录：2026-09-20T09:41:47+08:00
> 来源渠道：HN Show HN
> 标签：author_Nurysso, story_49714268, show_hn
> 最新指标：点赞=5 · 评论=0 · engagement_velocity=5

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-09-20T09:23:24+08:00 | HN Show HN | 点赞=5 · 评论=0 · engagement_velocity=5 | [[20-语料/posts/hn_show/2026-09-20/ca230c3f6c39cd38_Show-HN-Eulix-Code-navigation-for-large-codebases]] |
| 2026-09-20T09:37:11+08:00 | HN Show HN | 点赞=5 · 评论=0 · engagement_velocity=5 | [[20-语料/posts/hn_show/2026-09-20/ca230c3f6c39cd38_Show-HN-Eulix-Code-navigation-for-large-codebases]] |
| 2026-09-20T09:40:15+08:00 | HN Show HN | 点赞=5 · 评论=0 · engagement_velocity=5 | [[20-语料/posts/hn_show/2026-09-20/ca230c3f6c39cd38_Show-HN-Eulix-Code-navigation-for-large-codebases]] |
| 2026-09-20T09:41:47+08:00 | HN Show HN | 点赞=5 · 评论=0 · engagement_velocity=5 | [[20-语料/posts/hn_show/2026-09-20/ca230c3f6c39cd38_Show-HN-Eulix-Code-navigation-for-large-codebases]] |

## 摘要正文

Show HN: Eulix - Code navigation for large codebases | Hacker News  Show HN: Eulix - Code navigation for large codebases  3 points by Nurysso 34 minutes ago | hide | past | favorite | discuss  Hey I've been working on Eulix, a tool for navigating large codebases.  It parses a repository into symbols, call graphs and other structural information, then combines that with keyword and semantic retrieval to find relevant code.  I tested it on OpenStack (~6.9M LOC / 29k files). One query about Nova's PCI passthrough scheduling pulled back the relevant filters, helpers and related call paths in well under a second once indexed.  Some queries don't need an LLM at all, since Eulix can answer directly from the structured codebase data.  It's open source and runs locally:  https://github.com/Nurysso/eulix  I'd especially like feedback from people who've worked on code search, static analysis, or large monorepos.  on a side note it may be able to handle 30M+ loc codebase too, I haven't been able to test such huge repos cause I don't have a good enough gpu to embed parsers output! :)
