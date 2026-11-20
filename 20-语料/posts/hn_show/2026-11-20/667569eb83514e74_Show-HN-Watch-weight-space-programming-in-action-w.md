---
type: "corpus"
item_id: "667569eb83514e74"
title: "Show HN: Watch weight-space programming in action with WebGPU"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50561436"
project_url: "https://tabbyml.github.io/weight-space-playground"
author: "wsxiaoys"
published_at: "2026-11-19T15:32:47Z"
captured_at: "2026-11-20T09:45:52+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-11-20"
pub_day: "2026-11-19"
tags:
  - 语料
  - hn_show
  - author_wsxiaoys
  - story_50561436
  - show_hn
metrics: {"points": 33, "comments": 3, "engagement_velocity": 33}
comments_count: 3
comments_total: 3
discovered_via: "hn:show_hn:3d"
---

# Show HN: Watch weight-space programming in action with WebGPU

> [!info] 一句话导读
> I wanted to build a full weight-space programming loop entirely in the browser with WebGPU: let an LLM inspect Qwen3.5-0.8B, edit its weights, evaluate, and rep…

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50561436>
> 指标：点赞=33 · 评论=3 · engagement_velocity=33
> 作者：wsxiaoys　|　发布：2026-11-19T15:32:47Z
> 项目链接：<https://tabbyml.github.io/weight-space-playground>
> 采集：2026-11-20T09:45:52+08:00　|　id：`667569eb83514e74`

## 正文

I wanted to build a full weight-space programming loop entirely in the browser with WebGPU: let an LLM inspect Qwen3.5-0.8B, edit its weights, evaluate, and repeat.the full loop needed too much VRAM. so I turned it into an interactive walkthrough of a concrete example: editing 0.016% of a model's weights to reduce reasoning loops, no gradient descent.Based on exp8 of “Sparks of Weight-Space Programming.”: https://news.ycombinator.com/item?id=50341174

## 评论（3/3）

> **nickandbro** · 2026-11-19T17:05:15.000Z　
> “Claude, make me a website explaining the recently viral HN article, Sparks of Weight-Space Programming. Make it pop for the visualizations and explain things very clearly”

---

> **gtirloni** · 2026-11-19T17:25:53.000Z　
> Sure, a lot of people are doing this but where do the iterations, the quality checks, the human input, etc, becomes visible? It doesn't and then we have people assuming nothing takes any effort at all anymore, which is bas for really good content that was assisted by AI.

---

> **yathern** · 2026-11-19T17:53:21.000Z　
> While I'm sure there were iterations and quality checks and human input - I don't believe there was enough.While it looks good, it's laborious to read, and presented in an odd format, that doesn't really provide any insight, just lots of flash and LLM prose. The The header alone is hard to parse without context "Rewrote 0.016% of the model's weights — and cured its infinite loops". The constant little claude-isms of chips which say "Watch it · no download" "recorded · llama.cpp · Q4_K_M" "answer key: 10 · plus " add so much visual noise, especially with the high contrast style.Less is more. The "Run it in your browser" is cool enough. Keep that and throw away the rest, or put it on a separate page.

## 关联链接

- https://news.ycombinator.com/item?id=50341174

## 导航

- 项目页：[[10-项目/tabbyml.github.io_3d57282d]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
