---
type: "corpus"
item_id: "84f7f1ede5071a92"
title: "Show HN: Who and where are your anagranames?"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50371286"
project_url: "https://louisabraham.github.io/anagranames"
author: "Labo333"
published_at: "2026-11-04T20:48:19Z"
captured_at: "2026-11-05T11:21:45+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-11-05"
pub_day: "2026-11-04"
tags:
  - 语料
  - hn_show
  - author_Labo333
  - story_50371286
  - show_hn
metrics: {"points": 2, "comments": 0, "engagement_velocity": 2}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:3d"
---

# Show HN: Who and where are your anagranames?

> [!info] 一句话导读
> Hi HN!I made this fun app which combines quite a few ideas, I thought you might like the story:A few months ago I had the idea of looking for anagrams of names.…

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50371286>
> 指标：点赞=2 · 评论=0 · engagement_velocity=2
> 作者：Labo333　|　发布：2026-11-04T20:48:19Z
> 项目链接：<https://louisabraham.github.io/anagranames>
> 采集：2026-11-05T11:21:45+08:00　|　id：`84f7f1ede5071a92`

## 正文

Hi HN!I made this fun app which combines quite a few ideas, I thought you might like the story:A few months ago I had the idea of looking for anagrams of names. I started with french names using official statistics about first and last names, which also gave me a pretty simple model for likely anagrams: P(first + last) = P(first) * P(last).Then, I started checking which anagra-names (I coined the term) appeared in the 2021 Facebook leak.Finally, I improved my ranking using a factorization model.All this is available as a light and fast webpage thanks to a lot of cool algorithmic tricks detailed here: https://louisabraham.github.io/anagranames/how.htmlAbout the use of AI:Claude Code was fantastic for building the frontend (including the interactive globe) and writing the MLX code (I would otherwise have used PyTorch, which is slower on my machine). It also handled the quantization with very little guidance, which was particularly useful since I'm not an expert in that area.That said, I'm glad I learned CS before LLMs existed and still master it enough to work out the ideas and specs for everything else in my head / on paper before handing the implementation over to the agent.

## 关联链接

- https://louisabraham.github.io/anagranames/how.htmlAbout

## 导航

- 项目页：[[10-项目/louisabraham.github.io_5937ae65]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
