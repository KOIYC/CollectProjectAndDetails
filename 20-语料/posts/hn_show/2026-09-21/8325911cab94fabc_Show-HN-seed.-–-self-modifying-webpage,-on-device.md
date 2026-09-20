---
type: "corpus"
item_id: "8325911cab94fabc"
title: "Show HN: seed. – self-modifying webpage, on-device LLM, site in the URL"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=48344326"
project_url: "https://oxedom.github.io/seed"
author: "oxedom"
published_at: "2026-05-31T09:45:43Z"
captured_at: "2026-09-21T02:52:47+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-21"
pub_day: "2026-05-31"
tags:
  - 语料
  - hn_show
  - author_oxedom
  - story_48344326
  - show_hn
metrics: {"points": 2, "comments": 1, "engagement_velocity": 2}
comments_count: 1
comments_total: 1
discovered_via: "hn:show_hn:144d"
---

# Show HN: seed. – self-modifying webpage, on-device LLM, site in the URL

> [!info] 一句话导读
> local · chrome built-in (gemini nano)

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=48344326>
> 指标：点赞=2 · 评论=1 · engagement_velocity=2
> 作者：oxedom　|　发布：2026-05-31T09:45:43Z
> 项目链接：<https://oxedom.github.io/seed>
> 采集：2026-09-21T02:52:47+08:00　|　id：`8325911cab94fabc`

## 正文

seed · control
 +
modify →
copy url
 config
 reset
provider config
×
provider
anthropic (claude)
 openai (responses)
 local · chrome built-in (gemini nano)
api key
model
claude-sonnet-4-6 (sonnet 4.6)
 claude-opus-4-7 (opus 4.7 · most capable)
 claude-haiku-4-5-20251001 (haiku 4.5 · fast)
api key
model
Uses OpenAI's Responses API directly from this browser. The key is stored in localStorage and sent only with generation requests.
Uses Chrome's built-in window.LanguageModel API (Gemini Nano, runs entirely on-device). No API key, no network calls.
checking availability…
Setup: Chrome 127+ with the flag chrome://flags/#prompt-api-for-gemini-nano enabled. The model downloads (~1–2 GB) on first use.
Note: Gemini Nano is small and may struggle to produce well-formed HTML for complex prompts. Best results on short, focused requests.
save
seed · generating
 00:00
contacting model…
 cancel

## 评论（1/1）

> **oxedom** · 2026-05-31T09:48:58.000Z　
> I had this idea to build a webpage that can rewrite itself on the edge using a local model and a simple harness in the frontend, while playing around with storing HTML state in the URL.Currently supports Gemini Nano (local), Anthropic, or OpenAI.
> Gemini Nano is a lot less impressive than the SOTA models, but it's still fun to see it work!https://github.com/oxedom/seed

## 导航

- 项目页：[[10-项目/oxedom.github.io_bf929736]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
