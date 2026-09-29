---
type: "corpus"
item_id: "eb8a161a1aa228dd"
title: "Show HN: I'm a dermatologist and I vibe coded a 3D biophysical skin model"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49881201"
project_url: "https://drmagnuslynch.com/skin"
author: "sungam"
published_at: "2026-09-28T17:12:55Z"
captured_at: "2026-09-29T09:42:55+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-29"
pub_day: "2026-09-28"
tags:
  - 语料
  - hn_show
  - author_sungam
  - story_49881201
  - show_hn
metrics: {"points": 3, "comments": 0, "engagement_velocity": 3}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:3d"
---

# Show HN: I'm a dermatologist and I vibe coded a 3D biophysical skin model

> [!info] 一句话导读
> I'm a dermatologist. A year ago I posted a skin cancer quiz I vibe coded with Gemini 2.5 Pro. A top comment said that was the limit of vibe coding.This year I t…

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49881201>
> 指标：点赞=3 · 评论=0 · engagement_velocity=3
> 作者：sungam　|　发布：2026-09-28T17:12:55Z
> 项目链接：<https://drmagnuslynch.com/skin>
> 采集：2026-09-29T09:42:55+08:00　|　id：`eb8a161a1aa228dd`

## 正文

I'm a dermatologist. A year ago I posted a skin cancer quiz I vibe coded with Gemini 2.5 Pro. A top comment said that was the limit of vibe coding.This year I tried something more ambitious: SkinLab, a biophysical model of human skin that runs in the browser using WebGL. You can cut it or wound it and it heals realistically to form a scar. Then you can treat the scar with laser and watch the healing process.- 1.2 million voxels (0.25 mm resolution) for epidermis, dermis and fat.
- Spring lattice with a J-shaped collagen fibre law and tension along the skin's lines
- Healing as coupled ODEs (TGF-beta, myofibroblasts, collagen, contraction)
- One static HTML file, WebGL, three.js, no backendBy accurate I mean the constants come from published papers and it reproduces biophysical behaviour, such as incisions opening more when made more across the skin's tension lines and offloading preventing raised scars. It is not validated against patient outcomes, so it's for research and teaching, and a small step towards my lab's long term goal of an accurate cellular-resolution model of human skin.Built with Claude Code over five days. I guided the anatomy and biology through many rounds of feedback and iteration but I believe that in the future agentic models will be able to iteratively build and improve integrative models based upon analysis of published literature.The tour (top right) takes a minute and runs in real time in your browser. Feedback welcome.

## 导航

- 项目页：[[10-项目/drmagnuslynch.com_c0248d0c]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
