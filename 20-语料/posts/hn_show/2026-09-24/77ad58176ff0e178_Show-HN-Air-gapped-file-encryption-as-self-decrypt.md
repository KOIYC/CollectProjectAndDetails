---
type: "corpus"
item_id: "77ad58176ff0e178"
title: "Show HN: Air-gapped file encryption as self-decrypting HTML page"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49827375"
project_url: "https://cms-sfx-demo.apeleg.com/"
author: "emurlin"
published_at: "2026-09-24T07:22:17Z"
captured_at: "2026-09-24T23:57:22+08:00"
lang: "en"
kind: "post"
topic: "未分类"
shard: "2026-09-24"
pub_day: "2026-09-24"
tags:
  - 语料
  - hn_show
  - author_emurlin
  - story_49827375
  - show_hn
metrics: {"points": 7, "comments": 5, "engagement_velocity": 7}
comments_count: 5
comments_total: 5
discovered_via: "hn:show_hn:3d"
---

# Show HN: Air-gapped file encryption as self-decrypting HTML page

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49827375>
> 指标：点赞=7 · 评论=5 · engagement_velocity=7
> 作者：emurlin　|　发布：2026-09-24T07:22:17Z
> 项目链接：<https://cms-sfx-demo.apeleg.com/>
> 采集：2026-09-24T23:57:22+08:00　|　id：`77ad58176ff0e178`

## 正文

HTML CMS Tool

An error occurred

Loading

HTML CMS Tool
An error occurred
Loading

# grigio/carosello

## 评论（5/5）

> **DylanMerigaud** · 2026-09-24T07:41:03.000Z　
> Self-decrypting HTML? That's an innovative approach.

---

> **FatalLogic** · 2026-09-24T07:45:08.000Z　
> Maybe this is the source?https://github.com/ApelegHQ/ts-cms-ep-sfx

---

> **nikhilkxmar** · 2026-09-24T14:32:01.000Z　
> Cool!

---

> **emurlin** · 2026-09-24T07:55:31.000Z　
> Yeah, I was inspired by self-extracting archives. I wanted to share files with basically no dependencies.The goal was:1. Something that didn't require any installation (assuming a web browser)2. Have a single file with no network that could self-decrypt3. Be fully auditableThe second point is done by having (sort of(*)) reproducible builds and embedded OpenPGP signatures.The first point is made by cleverly manipulating the HTML structure so that it can decrypt without breaking the PGP signature. It can even decrypt using bare openssl (which was a design goal too, though getting the exact structure right took some work and bug reports).The third point is accomplished by the first two, and by the source being freely available.(*) Depends on the OS at the moment.

---

> **emurlin** · 2026-09-24T07:56:54.000Z　
> Correct

## 导航

- 项目页：[[10-项目/cms-sfx-demo.apeleg.com_0cf7108b]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`未分类`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
