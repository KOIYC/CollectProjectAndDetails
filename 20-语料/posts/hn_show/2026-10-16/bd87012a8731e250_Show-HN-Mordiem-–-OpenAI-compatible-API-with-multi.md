---
type: "corpus"
item_id: "bd87012a8731e250"
title: "Show HN: Mordiem – OpenAI-compatible API with multi-network failover"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50103434"
project_url: "https://mordiem.com/"
author: "mordiem"
published_at: "2026-10-15T13:31:39Z"
captured_at: "2026-10-16T09:35:18+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-10-16"
pub_day: "2026-10-15"
tags:
  - 语料
  - hn_show
  - author_mordiem
  - story_50103434
  - show_hn
metrics: {"points": 2, "comments": 0, "engagement_velocity": 2}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:3d"
---

# Show HN: Mordiem – OpenAI-compatible API with multi-network failover

> [!info] 一句话导读
> MORDIEM Models Docs MDM MCU

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50103434>
> 指标：点赞=2 · 评论=0 · engagement_velocity=2
> 作者：mordiem　|　发布：2026-10-15T13:31:39Z
> 项目链接：<https://mordiem.com/>
> 采集：2026-10-16T09:35:18+08:00　|　id：`bd87012a8731e250`

## 正文

MORDIEM Models Docs MDM MCU
 Sign in Get API key
 Menu OpenAI-compatible · Base
 One API, Every Model.
Own your inference.
 Get an API key How does it work?
 — Models
 — Modalities
 — 7-day volume · tokens
 — Compute capacity · DIEM
Text, images, video, and audio
 Every modality through one interface. Point an OpenAI SDK at Mordiem and keep the same request shape.
 Chat Images Video Speech Embeddings
 Higher availability
 Requests fail over across keys and providers when one is rate-limited or down. Callers keep a single endpoint.
 Price and performance
 Per-token and per-image prices are listed up front. No subscription, and your own provider keys are billed at cost.
Models
 Live catalog prices. Text is per million tokens. Images are per generation.
All Text Images Video Audio
Model Context Input / 1M Output / 1M
 Loading catalog…
Full catalog →
 Start in three steps
 OpenAI-compatible. Failover is automatic.
1 Create an API key One key covers every model on the exchange.
2 Add credit Pay with USD, Zcash, or stake Mordiem Compute Units (MCU).
3 Call the API Set the base URL. Existing OpenAI SDKs work without a rewrite.
quickstart.py
 from openai import OpenAI
client = OpenAI(
 api_key= "mr_sk_..." ,
 base_url= "https://api.mordiem.com/api/v1" ,
 )
# One key. Failover is automatic.
 client.chat.completions.create(
 model= "llama-3.3-70b" ,
 messages=[ { "role" : "user" , "content" : "Hello" } ],
 )
Mordiem Models Docs MDM MCU Help Terms Privacy

## 关联链接

- https://api.mordiem.com/api/v1

## 导航

- 项目页：[[10-项目/mordiem.com_d5b8cb05]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
