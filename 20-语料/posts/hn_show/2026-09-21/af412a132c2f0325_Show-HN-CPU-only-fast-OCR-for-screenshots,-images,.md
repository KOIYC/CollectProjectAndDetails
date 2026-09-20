---
type: "corpus"
item_id: "af412a132c2f0325"
title: "Show HN: CPU-only fast OCR for screenshots, images, PDFs, webpages"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=48344012"
project_url: "https://github.com/kouhxp/textsnap"
author: "mrkn1"
published_at: "2026-05-31T08:32:26Z"
captured_at: "2026-09-21T01:43:03+08:00"
lang: "en"
kind: "post"
topic: "未分类"
shard: "2026-09-21"
pub_day: "2026-05-31"
tags:
  - 语料
  - hn_show
  - author_mrkn1
  - story_48344012
  - show_hn
metrics: {"points": 9, "comments": 8, "engagement_velocity": 9}
comments_count: 8
comments_total: 8
discovered_via: "hn:show_hn:144d"
---

# Show HN: CPU-only fast OCR for screenshots, images, PDFs, webpages

> [!info] 一句话导读
> Show HN: CPU-only fast OCR for screenshots, images, PDFs, webpages

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=48344012>
> 指标：点赞=9 · 评论=8 · engagement_velocity=9
> 作者：mrkn1　|　发布：2026-05-31T08:32:26Z
> 项目链接：<https://github.com/kouhxp/textsnap>
> 采集：2026-09-21T01:43:03+08:00　|　id：`af412a132c2f0325`

## 正文

Show HN: CPU-only fast OCR for screenshots, images, PDFs, webpages

## 评论（8/8）

> **arnabdey0503** · 2026-05-31T08:50:43.000Z　
> Have you done benchmark againest other methods?

---

> **explosion-s** · 2026-05-31T12:21:18.000Z　
> Why is no GPU a pull here? Is there usually an activation overhead GPU request or something?

---

> **ajithhyd** · 2026-06-01T11:19:18.000Z　
> Can it support other languages?

---

> **quanglee** · 2026-06-02T08:51:41.000Z　
> Do you have some benchmark on how fast it is on cpu? I checked the repo and the huggingface page but only found gpu-based benchmarks

---

> **mrkn1** · 2026-05-31T12:21:53.000Z　
> I haven't. But the evals of the underlying model are published here, including on Omnibench. https://huggingface.co/PaddlePaddle/PaddleOCR-VL-1.5

---

> **mrkn1** · 2026-05-31T12:22:43.000Z　
> No, simply, my laptop only has a CPU.

---

> **mrkn1** · 2026-06-01T14:06:15.000Z　
> It should support 109 languages. More info here: https://huggingface.co/PaddlePaddle/PaddleOCR-VL

---

> **mrkn1** · 2026-06-02T17:21:33.000Z　
> I have not. My experience has been a few seconds for an 1024x1024 with medium density of text, FWIW. Feel free to try it on a few test images, model is pretty small and fast, but yeah no formal evals on CPU.

## 导航

- 项目页：[[10-项目/github.com_1c470881]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`未分类`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
