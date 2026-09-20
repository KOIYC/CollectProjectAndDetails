---
type: "corpus"
item_id: "17525f5c59a25d3d"
title: "Show HN: Squishword, a word game where meaning, not spelling, matters"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49124606"
project_url: "https://squishword.com/"
author: "sbloz"
published_at: "2026-07-31T15:49:45Z"
captured_at: "2026-09-21T02:54:48+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-21"
pub_day: "2026-07-31"
tags:
  - 语料
  - hn_show
  - author_sbloz
  - story_49124606
  - show_hn
metrics: {"points": 4, "comments": 3, "engagement_velocity": 4}
comments_count: 3
comments_total: 3
discovered_via: "hn:show_hn:83d"
---

# Show HN: Squishword, a word game where meaning, not spelling, matters

> [!info] 一句话导读
> This is a little daily word game that I've been working on. I love crosswords and Wordle but they all use the spelling of words as the main constraint. With LLM…

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49124606>
> 指标：点赞=4 · 评论=3 · engagement_velocity=4
> 作者：sbloz　|　发布：2026-07-31T15:49:45Z
> 项目链接：<https://squishword.com/>
> 采集：2026-09-21T02:54:48+08:00　|　id：`17525f5c59a25d3d`

## 正文

This is a little daily word game that I've been working on. I love crosswords and Wordle but they all use the spelling of words as the main constraint. With LLMs we can build "Squishy Systems", systems that don't have to be fully procedurally defined. That can give us games that feel more like playing a board game with friends. Games that require a human judge. Because they require a judge they aren't well explored for video games, especially outside of multiplayer.Squishword is a simple first exploration of that. There's a tutorial so I won't explain all the mechanics. Simply: you try to move from one word to another by adding, subtracting, joining and dividing words. For example: "dog" splits into "bark" and "animal". You can do clever things like take "bark" + "plant" and make "tree". The inspiration comes from the "Wikipedia game" where you try to move from one random article to another just by clicking links.Tuning the judge behavior for fair results took a lot of work, and I'm not 100% happy with it yet. I built more tools and visualizations than features in the game itself. Like the 11x11 matrix of logic and wit grades for every move, to try to get the judge distribution more even. This is a "simple" example of LLMs in a product, so I'm curious how more complex workflows are dealing with it.

## 评论（3/3）

> **ryanyz10** · 2026-08-01T00:51:35.000Z　
> Just tried today’s puzzle on hard and it was super fun! I think it took me a little bit to both understand the operations and also how the judge worked. Would be nice if there was a cheat sheet to reference somewhere quickly just to see how each operation works and examples since the tutorial is a bit harder to get through quickly (say if I wanted to learn about multiplication specifically)Scoring is also a bit opaque? But overall I think this is super fun and requires a lot more creativity than say wordle.squishword · No. 1 · 31 Jul 2026 · hard · B
> storm + deft ÷ spark + sound × sound = jungle
> logic 85 · wit 60 · obscurity 37
>  Plainspoken Flawless Pioneer

---

> **sbloz** · 2026-08-01T02:09:14.000Z　
> Thanks for trying it and thanks for the feedback! It's very helpful. I think I should restructure the tutorial into a bit more of a "worksheet". That way you have some more guidance and space to experiment with just the operations. The tutorial is too long right now.Do you think the overall scoring, the per operation score, or both are too opaque? I tried to give clear visibility into the per opperation scoring. But the per puzzle scoring does need more attention. I want to reward both being smart short solutions and clever long solutions, so right now it's just an unhappy compromise.I was hoping solutions would be sort of "personal". Share the interesting connections you came up with and different ways you think about words.

---

> **ryanyz10** · 2026-08-01T02:30:02.000Z　
> Yea I think it’s mainly just not clear how I ended up with my final letter grade. I also think the hard puzzle does limit you quite a bit but maybe I’m just not creative enough hahaI think you achieved your goal! Again I think it’s super fun and it’ll definitely keep me coming back for a while

## 导航

- 项目页：[[10-项目/squishword.com_be96c258]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
