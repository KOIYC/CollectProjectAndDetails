---
type: "project"
title: "Show HN: DocOCR – Convert document images to Markdown locally on macOS"
project_url: "https://github.com/riddleling/docOCR"
first_seen: "2026-09-21T02:52:54+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_riddleling
  - story_48334770
  - show_hn
lang: "en"
---

# Show HN: DocOCR – Convert document images to Markdown locally on macOS

> [!info] 一句话导读
> macOS CLI and HTTP OCR tool for converting document images to Markdown.

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://github.com/riddleling/docOCR>
> 首次收录：2026-09-21T02:52:54+08:00
> 来源渠道：HN Show HN
> 标签：author_riddleling, story_48334770, show_hn
> 最新指标：点赞=4 · 评论=0 · engagement_velocity=4

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-09-21T01:27:24+08:00 | HN Show HN | 点赞=4 · 评论=0 · engagement_velocity=4 | [[20-语料/posts/hn_show/2026-09-21/3e52d2da81d1c21a_Show-HN-DocOCR-–-Convert-document-images-to-Markdo]] |
| 2026-09-21T02:52:54+08:00 | HN Show HN | 点赞=4 · 评论=0 · engagement_velocity=4 | [[20-语料/posts/hn_show/2026-09-21/3e52d2da81d1c21a_Show-HN-DocOCR-–-Convert-document-images-to-Markdo]] |

## 摘要正文

# riddleling/docOCR  macOS CLI and HTTP OCR tool for converting document images to Markdown.  - Stars: 37 - Forks: 3 - Watchers: 37 - Open issues: 0 - License: MIT License - Default branch: main - Created: 2026-05-26T15:47:13Z  ## Languages  - Swift  ## Topics  - cli - http-server - macos - markdown - ocr - vision-framework  ## Top Contributors  - riddleling (21 contributions)  ---  ## README  # docOCR  `docOCR` is a macOS command-line OCR tool that converts document images into Markdown text. It can run as a batch CLI tool or as a local HTTP server for browser uploads and API clients.  Image  ## Table of Contents  - Features - Requirements - CLI Usage - HTTP Server - API Usage - Build - Install - Development - macOS Shortcuts: Screenshot to Markdown - Codex Skill  ## Features  - Converts image files to Markdown text. - Writes batch OCR output next to each source image using the same basename and a `.md` extension. - Converts detected paragraphs, lists, and tables into Markdown when Apple's document recognition API identifies them. - Provides a local web UI for uploading an image and viewing OCR output. - Provides a JSON API for image upload and OCR response. - Uses Apple's `Recogn…
