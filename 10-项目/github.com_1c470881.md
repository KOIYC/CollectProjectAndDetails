---
type: "project"
title: "Show HN: CPU-only fast OCR for screenshots, images, PDFs, webpages"
project_url: "https://github.com/kouhxp/textsnap"
first_seen: "2026-09-21T02:52:47+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_mrkn1
  - story_48344012
  - show_hn
lang: "en"
---

# Show HN: CPU-only fast OCR for screenshots, images, PDFs, webpages

> [!info] 一句话导读
> Snap any image, screenshot, or webpage into plaintext. No GPU. No cloud. One command.

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://github.com/kouhxp/textsnap>
> 首次收录：2026-09-21T02:52:47+08:00
> 来源渠道：HN Show HN
> 标签：author_mrkn1, story_48344012, show_hn
> 最新指标：点赞=9 · 评论=8 · engagement_velocity=9

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-09-21T01:27:24+08:00 | HN Show HN | 点赞=9 · 评论=8 · engagement_velocity=9 | [[20-语料/posts/hn_show/2026-09-21/af412a132c2f0325_Show-HN-CPU-only-fast-OCR-for-screenshots,-images,]] |
| 2026-09-21T01:43:03+08:00 | HN Show HN | 点赞=9 · 评论=8 · engagement_velocity=9 | [[20-语料/posts/hn_show/2026-09-21/af412a132c2f0325_Show-HN-CPU-only-fast-OCR-for-screenshots,-images,]] |
| 2026-09-21T02:52:47+08:00 | HN Show HN | 点赞=9 · 评论=8 · engagement_velocity=9 | [[20-语料/posts/hn_show/2026-09-21/af412a132c2f0325_Show-HN-CPU-only-fast-OCR-for-screenshots,-images,]] |

## 摘要正文

# kouhxp/textsnap  Snap any image, screenshot, or webpage into plaintext. No GPU. No cloud. One command.  - Stars: 179 - Forks: 6 - Watchers: 179 - Open issues: 0 - License: MIT License - Default branch: main - Created: 2026-05-24T13:57:05Z  ## Languages  - Python  ## Topics  - image2text - ocr - onnx - paddlepaddle - screenshot - transcription  ## Top Contributors  - kouhxp (5 contributions)  ---  ## README  # textsnap  > **Snap any image, screenshot, or webpage into plaintext. No GPU. No cloud. One command.**  textsnap demo  Python License Platforms  ``` textsnap screenshot.png ```  That's it. You get a `.txt` next to your shell, recognized on your CPU, from a screenshot, a photo, an image URL, or even a webpage.  ---  ## Why textsnap  - ⚡ **Runs on CPU.** A 0.9B PaddleOCR-VL-1.5 vision-language model, quantized to q4 ONNX, parses full pages on a plain laptop. No CUDA. No M-series-only tricks. Plain old cores, pinned to your physical-core count. - 🖼 **Images, screenshots, URLs, webpages.** Point it at a local file, a direct image URL, or a full article URL — it isolates the main content and OCRs the most prominent image. Or OCR straight from your clipboard with no argument at all…
