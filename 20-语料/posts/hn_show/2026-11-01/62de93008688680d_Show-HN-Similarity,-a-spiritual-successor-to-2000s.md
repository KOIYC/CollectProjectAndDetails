---
type: "corpus"
item_id: "62de93008688680d"
title: "Show HN: Similarity, a spiritual successor to 2000s-era OkCupid"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50317309"
project_url: "https://similarity.com/"
author: "stickfigure"
published_at: "2026-10-31T15:53:39Z"
captured_at: "2026-11-01T09:38:09+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-11-01"
pub_day: "2026-10-31"
tags:
  - 语料
  - hn_show
  - author_stickfigure
  - story_50317309
  - show_hn
metrics: {"points": 4, "comments": 2, "engagement_velocity": 4}
comments_count: 2
comments_total: 2
discovered_via: "hn:show_hn:3d"
---

# Show HN: Similarity, a spiritual successor to 2000s-era OkCupid

> [!info] 一句话导读
> This is a side project I've been working on on-and-off (mostly off) since the 1990s. I guess you would call it an experimental "dating site" though it's designe…

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50317309>
> 指标：点赞=4 · 评论=2 · engagement_velocity=4
> 作者：stickfigure　|　发布：2026-10-31T15:53:39Z
> 项目链接：<https://similarity.com/>
> 采集：2026-11-01T09:38:09+08:00　|　id：`62de93008688680d`

## 正文

This is a side project I've been working on on-and-off (mostly off) since the 1990s. I guess you would call it an experimental "dating site" though it's designed to be fun/interesting to people who aren't single (like me).You don't need to sign in to see how it works, so try it out. There is no swiping.The original inspiration was a 90s-era website called moviecritic.com that let you rate movies and get movie suggestions via collaborative filtering. I thought "hey, what about just matching me to the _people_ with the same taste instead?" And why just movies?The closest thing to this was 2000s-era OkCupid, before it was Tinderized. I want to capture its appeal, while making something novel.Similarity is not vibe coded, though I lean pretty heavily on codex (mostly the $20/mo plan - not a lot of tokens burnt here). The stack is java, guice/gwizard, elastic beanstalk, postgres (neon), react, jotai, and few cloudflare doodads. The match engine is a custom in-memory structure; getting the LLM to load test and optimize it was really a wow moment. Everything is PaaS and designed to scale by itself, cheaply, hands-off.I'm working on some ideas to help with the chicken/egg problem but for now I have low expectations. It's cheap to run and I have a day job.Would love feedback!

## 评论（2/2）

> **claytongulick** · 2026-10-31T16:13:55.000Z　
> This is cool, I remember either OkCupid of Plenty of Fish, used to be a really interesting exercise in self reflection.You could only see someone else's answer to a question if you answered it.The questions would sometimes get deeply personal.It would make me self-reflect a lot on what an honest answer was, and whether I wanted other people to see my answer.And if not, why? Was there something I was embarrassed about? Should I be? If so, should I fix that thing?I didn't really care about the dating aspect as much as the exercise in critical self evaluation.

---

> **stickfigure** · 2026-10-31T16:21:55.000Z　
> Thanks! I tried to make the answering process part of the fun rather than a drag.When you look at someone else's profile, Similarity shows you the questions that you both feel strongly about (answered at the edges of the range) and either agree about or disagree about. The idea is that these would be conversation starters - if you both are passionate about skiing, it should be front and center.

## 导航

- 项目页：[[10-项目/similarity.com_142bea29]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
