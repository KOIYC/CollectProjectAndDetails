---
type: "project"
title: "Show HN: Filling PDF forms with AI using client-side tool calling"
project_url: "https://copilot.simplepdf.com/?share=a7d00ad073c75a75d493228e6ff7b11eb3f2d945b6175913e87898ec96ca8076&form=w9&lang=en"
first_seen: "2026-09-21T01:42:09+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_nip
  - story_47947347
  - show_hn
lang: "en"
---

# Show HN: Filling PDF forms with AI using client-side tool calling

> [!info] 一句话导读
> Hey HN!I built SimplePDF Copilot: an AI assistant that can interact with the PDF editor. It fills fields, answers questions, focuses on a specific field, adds f…

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://copilot.simplepdf.com/?share=a7d00ad073c75a75d493228e6ff7b11eb3f2d945b6175913e87898ec96ca8076&form=w9&lang=en>
> 首次收录：2026-09-21T01:42:09+08:00
> 来源渠道：HN Show HN
> 标签：author_nip, story_47947347, show_hn
> 最新指标：点赞=7 · 评论=1 · engagement_velocity=7

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-09-21T01:09:14+08:00 | HN Show HN | 点赞=7 · 评论=1 · engagement_velocity=7 | [[20-语料/posts/hn_show/2026-09-21/18a04fab9109ffdd_Show-HN-Filling-PDF-forms-with-AI-using-client-sid]] |
| 2026-09-21T01:13:42+08:00 | HN Show HN | 点赞=7 · 评论=1 · engagement_velocity=7 | [[20-语料/posts/hn_show/2026-09-21/18a04fab9109ffdd_Show-HN-Filling-PDF-forms-with-AI-using-client-sid]] |
| 2026-09-21T01:42:09+08:00 | HN Show HN | 点赞=7 · 评论=1 · engagement_velocity=7 | [[20-语料/posts/hn_show/2026-09-21/18a04fab9109ffdd_Show-HN-Filling-PDF-forms-with-AI-using-client-sid]] |

## 摘要正文

Hey HN!I built SimplePDF Copilot: an AI assistant that can interact with the PDF editor. It fills fields, answers questions, focuses on a specific field, adds fields, deletes pages, and so on.It's built on top of SimplePDF that I started 7 years ago, pioneering privacy-respecting client-side pdf editing, now used monthly by 200k+ people.As for the privacy model: the PDF itself never leaves the browser. Parsing, rendering, and field detection all run client-side.The text the model needs (and your messages) goes to whatever LLM you point at. By default that's our demo proxy (DeepSeek V4 Flash, rate-capped), but you can BYOK and point it at any cloud provider, or go fully local (I've been testing with LM Studio).Unlike the existing "Chat with PDF" tools that only retrieve the text/OCR layer, Copilot can act on the PDF: filling fields, adding fields (detected client-side using CommonForms by Joe Barrow [1], jbarrow on HN with some post-processing heuristics I added on top), focusing on fields, deleting pages, and so on.I built this because SimplePDF is mostly used by healthcare customers where document privacy is paramount, and I wanted an AI experience that didn't require shipping PII…
