---
type: "corpus"
item_id: "5d62888ba2faa71d"
title: "Show HN: ComicInk – AI tool that turns a prompt into a full comic book"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=47964060"
project_url: "https://comicink.ai/"
author: "comicink"
published_at: "2026-04-30T15:33:25Z"
captured_at: "2026-09-21T01:40:49+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-21"
pub_day: "2026-04-30"
tags:
  - 语料
  - hn_show
  - author_comicink
  - story_47964060
  - show_hn
metrics: {"points": 2, "comments": 2, "engagement_velocity": 2}
comments_count: 2
comments_total: 2
discovered_via: "hn:show_hn:174d"
---

# Show HN: ComicInk – AI tool that turns a prompt into a full comic book

> [!info] 一句话导读
> Hi HN, I'm Sanjoy. I've always loved comic books and stories but can't draw. So I built ComicInk: describe a story, the AI generates a complete comic book — con…

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=47964060>
> 指标：点赞=2 · 评论=2 · engagement_velocity=2
> 作者：comicink　|　发布：2026-04-30T15:33:25Z
> 项目链接：<https://comicink.ai/>
> 采集：2026-09-21T01:40:49+08:00　|　id：`5d62888ba2faa71d`

## 正文

Hi HN, I'm Sanjoy. I've always loved comic books and stories but can't draw. So I built ComicInk: describe a story, the AI generates a complete comic book — consistent characters across panels, dialogue, cover art, the whole thing.No-signup demo at comicink.ai/quick — type a prompt, watch Gemini write a dramatic teaser of your story in real-time while the cover + page 1 render (~2 min). Free signup unlocks the full 4-page comic.The hard problem was character consistency. Most AI image tools treat each generation independently, so your hero's face morphs between panels. ComicInk stores per-character reference images + structured attributes (age group, build, hair, distinguishing features) and injects them into every panel prompt. Not perfect, but substantially better than raw text-to-image.Translation worked out better than I expected: a click renders the comic in 10+ languages while the panel art stays identical — only the dialogue and captions change. The public reader auto-detects the visitor's browser language and serves the matching edition if one exists.Getting some interest from serious book creators as well so I introduced the "Book to comic" feature. Simply upload the PDF of a book of you have written. AI reads the book, analyzes it for important plot elements and characters. You can decide to convert the book into 1 issue or split it up across multiple issues, choose the art style you want and you have a comic version of your book.Stack: Next.js 16 / Supabase / Gemini (text + images) / fal.ai (backup image provider) / Stripe / Inngest. iOS app on the App Store.Happy to answer anything. Especially curious if anyone's solved character consistency better than reference-image injection — it holds up reasonably well with the Gemini image models I use, but drifts on other providers.

## 评论（2/2）

> **Ayaan2004** · 2026-04-30T15:43:40.000Z　
> Love it. I will definitely try it

---

> **comicink** · 2026-04-30T15:58:27.000Z　
> Thanks Ayaan!

## 导航

- 项目页：[[10-项目/comicink.ai_03e256e5]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
