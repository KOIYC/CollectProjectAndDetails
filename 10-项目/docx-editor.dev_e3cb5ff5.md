---
type: "project"
title: "Show HN: Docx-to-Markdown – layout-aware Word to Markdown converter"
project_url: "https://docx-editor.dev/solutions/word-to-markdown"
first_seen: "2026-09-20T14:04:03+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_thisisjedr
  - story_49728477
  - show_hn
lang: "en"
---

# Show HN: Docx-to-Markdown – layout-aware Word to Markdown converter

> [!info] 一句话导读
> Word to Markdown converter with page references

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://docx-editor.dev/solutions/word-to-markdown>
> 首次收录：2026-09-20T14:04:03+08:00
> 来源渠道：HN Show HN
> 标签：author_thisisjedr, story_49728477, show_hn
> 最新指标：点赞=5 · 评论=5 · engagement_velocity=5

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-09-20T09:23:24+08:00 | HN Show HN | 点赞=5 · 评论=5 · engagement_velocity=5 | [[20-语料/posts/hn_show/2026-09-20/b88a2290c00e8152_Show-HN-Docx-to-Markdown-–-layout-aware-Word-to-Ma]] |
| 2026-09-20T09:37:01+08:00 | HN Show HN | 点赞=5 · 评论=5 · engagement_velocity=5 | [[20-语料/posts/hn_show/2026-09-20/b88a2290c00e8152_Show-HN-Docx-to-Markdown-–-layout-aware-Word-to-Ma]] |
| 2026-09-20T14:04:03+08:00 | HN Show HN | 点赞=5 · 评论=5 · engagement_velocity=5 | [[20-语料/posts/hn_show/2026-09-20/b88a2290c00e8152_Show-HN-Docx-to-Markdown-–-layout-aware-Word-to-Ma]] |

## 摘要正文

Author: EigenPal  Word to Markdown converter with page references | DOCX Editor  # Convert Word to Markdown with page references  Convert .docx to .md in TypeScript. Keep layout-aware page references for document agents and RAG.  Output  Markdown + pages[]  Runtime  Node.js and browsers  License  Apache 2.0  ## Extract text with page context  Convert Word (.docx) files to paginated Markdown for agents and retrieval-augmented generation (RAG). Keep page references with body text and read headers and footers separately.  ### Pages from document layout  The layout engine calculates page boundaries. Retrieve Markdown by page, or use the continuous document body.  ### Separate headers and footers  Read each page's header and footer separately. Index the body without repeating document labels in every chunk.  ### Structured content and review data  Extract headings, lists, tables, comments, and tracked changes. Enable image extraction when needed. Check warnings for omitted content.  ### Why do page references need a layout engine?  Page boundaries depend on fonts and document layout. Saved page-break hints can be missing or stale. The converter calculates layout before exporting Markdow…
