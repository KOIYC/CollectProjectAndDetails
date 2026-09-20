---
type: "corpus"
item_id: "18a04fab9109ffdd"
title: "Show HN: Filling PDF forms with AI using client-side tool calling"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=47947347"
project_url: "https://copilot.simplepdf.com/?share=a7d00ad073c75a75d493228e6ff7b11eb3f2d945b6175913e87898ec96ca8076&form=w9&lang=en"
author: "nip"
published_at: "2026-04-29T12:22:15Z"
captured_at: "2026-09-21T01:42:09+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-21"
pub_day: "2026-04-29"
tags:
  - 语料
  - hn_show
  - author_nip
  - story_47947347
  - show_hn
metrics: {"points": 7, "comments": 1, "engagement_velocity": 7}
comments_count: 1
comments_total: 1
discovered_via: "hn:show_hn:174d"
---

# Show HN: Filling PDF forms with AI using client-side tool calling

> [!info] 一句话导读
> Hey HN!I built SimplePDF Copilot: an AI assistant that can interact with the PDF editor. It fills fields, answers questions, focuses on a specific field, adds f…

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=47947347>
> 指标：点赞=7 · 评论=1 · engagement_velocity=7
> 作者：nip　|　发布：2026-04-29T12:22:15Z
> 项目链接：<https://copilot.simplepdf.com/?share=a7d00ad073c75a75d493228e6ff7b11eb3f2d945b6175913e87898ec96ca8076&form=w9&lang=en>
> 采集：2026-09-21T01:42:09+08:00　|　id：`18a04fab9109ffdd`

## 正文

Hey HN!I built SimplePDF Copilot: an AI assistant that can interact with the PDF editor. It fills fields, answers questions, focuses on a specific field, adds fields, deletes pages, and so on.It's built on top of SimplePDF that I started 7 years ago, pioneering privacy-respecting client-side pdf editing, now used monthly by 200k+ people.As for the privacy model: the PDF itself never leaves the browser. Parsing, rendering, and field detection all run client-side.The text the model needs (and your messages) goes to whatever LLM you point at. By default that's our demo proxy (DeepSeek V4 Flash, rate-capped), but you can BYOK and point it at any cloud provider, or go fully local (I've been testing with LM Studio).Unlike the existing "Chat with PDF" tools that only retrieve the text/OCR layer, Copilot can act on the PDF: filling fields, adding fields (detected client-side using CommonForms by Joe Barrow [1], jbarrow on HN with some post-processing heuristics I added on top), focusing on fields, deleting pages, and so on.I built this because SimplePDF is mostly used by healthcare customers where document privacy is paramount, and I wanted an AI experience that didn't require shipping PII to a third party.
Stack is pretty standard:- Tanstack Start- AI SDK from Vercel- Tailwind (I personally prefer CSS modules, I'm old-school but the goal since I open source it, I figured that Tailwind would be a better fit)The more interesting part is the client-side tool calling: events are passed back and forth via iframe postMessage.If you're not familiar with "tool calling" and "client-side tool calling", a quick primer:Tool calling is what LLMs use to take actions. When Claude runs grep or ls, or hits an MCP server, those are tool calls.Client-side tool calling means the intent to call a tool comes from the LLM, but the execution happens in the browser.That matters for: speed, you can't go faster than client-to-client operations and also gives you the ability to limit the data you expose to the LLM. For the demo I do feed the content of the document to the LLM, but that connection could be severed as simply as removing the tool that exposes the content data.The demo is fully open source, available on Github [2] and the demo is the same as the link of this post [3]What's not open source is SimplePDF itself (loaded as the iframe).I could talk on and on about this, let me know if you have any questions, anything goes![1] https://github.com/jbarrow/commonforms[2] https://github.com/SimplePDF/simplepdf-embed/tree/main/copil...[3] https://copilot.simplepdf.com/?share=a7d00ad073c75a75d493228...

## 评论（1/1）

> **nip** · 2026-04-29T12:49:04.000Z　
> Just to be clear, this is a technical demo showing what's possible with client-side tool calling + local models: LLM-assisted form filling where no document data has to leave the user's machine.Use cases range from:- Filling foreign-language forms- Navigating a contract before signing: "can I trust ALL the clauses here?"- Pre-filling repetitive forms from existing data sources (CRM, EHR, etc. via MCP/RAG)Copilot is designed to be embedded; our customers ship it white-labeled inside their own products.

## 关联链接

- https://copilot.simplepdf.com/?share=a7d00ad073c75a75d493228...
- https://github.com/SimplePDF/simplepdf-embed/tree/main/copil...[3
- https://github.com/jbarrow/commonforms[2

## 导航

- 项目页：[[10-项目/copilot.simplepdf.com_61c0388a]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
