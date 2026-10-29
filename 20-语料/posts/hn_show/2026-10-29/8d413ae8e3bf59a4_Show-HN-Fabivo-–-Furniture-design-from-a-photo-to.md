---
type: "corpus"
item_id: "8d413ae8e3bf59a4"
title: "Show HN: Fabivo – Furniture design from a photo to a numbered cut list"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50284856"
project_url: "https://fabivo.app/en"
author: "superpapotas"
published_at: "2026-10-29T05:21:10Z"
captured_at: "2026-10-29T20:41:52+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-10-29"
pub_day: "2026-10-29"
tags:
  - 语料
  - hn_show
  - author_superpapotas
  - story_50284856
  - show_hn
metrics: {"points": 3, "comments": 0, "engagement_velocity": 3}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:3d"
---

# Show HN: Fabivo – Furniture design from a photo to a numbered cut list

> [!info] 一句话导读
> Hello all,Ive been building Fabivo, a free furniture planner that runs in the browser. You sketch it simply by drawing it, (by far my favorite feature of this a…

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50284856>
> 指标：点赞=3 · 评论=0 · engagement_velocity=3
> 作者：superpapotas　|　发布：2026-10-29T05:21:10Z
> 项目链接：<https://fabivo.app/en>
> 采集：2026-10-29T20:41:52+08:00　|　id：`8d413ae8e3bf59a4`

## 正文

Hello all,Ive been building Fabivo, a free furniture planner that runs in the browser. You sketch it simply by drawing it, (by far my favorite feature of this app), clicking for boards or just selecting some starting designs.But what i think separates fabivo from others its the image to model ai assistant, which took me a looong time to develop and get some quirks fixed, thanks god latest models are focusing on 3d, thats been helping too!The photo part is an image to JSON CAD harness: the model returns a parametric furniture model in mm that the app can build and edit. That harness is also what i benchmark, and honestly its the reason the app exists. I wanted to see if a photo could turn into a plan i could take to the saw.Also finetuned some image models and found interesting stuff, that was a first. My intention was to basically reuse the drawing feature to convert a 2d line sketch from image models like gpt image / nano banana to my parametric model, which "worked", and was actually thinking of using that for prod, but then cheaper/better models at 3d launched, but anyways, i learned a lot!Im getting better performance from my harness than from plain 3js, tho this is anecdotally and havent actually benchmarked it...Happy to answer anything, especially about the harness or the cut order.edit: Adding the numbers, missed them.17 photos of real furniture, three models, same harness, medium reasoning, same tools. Scored on how close the returned structure and boards are to the gold model, so its my own set. (tho i have a hard time making a good scoring metric... just usually go by look!)Model (medium reasoning) Avg. time / photo Avg. input tokens / photo Avg. output tokens / photo Avg. tool calls / photo
 GPT-6.1 Terra 9.5 s 30,409 632 1.06
 Claude Sonnet 5.5 13.6 s 50,167 1,592 1.18
 Claude Haiku 5.5 34.9 s 66,786 6,658 2.35Terra was both cheaper per photo and the most consistent to my likings. Sonnet was close on quality, Haiku needed way more tool calls to get there.

## 导航

- 项目页：[[10-项目/fabivo.app_a9695a46]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
