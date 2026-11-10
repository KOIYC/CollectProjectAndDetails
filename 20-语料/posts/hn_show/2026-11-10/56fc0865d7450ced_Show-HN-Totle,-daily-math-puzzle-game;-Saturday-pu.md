---
type: "corpus"
item_id: "56fc0865d7450ced"
title: "Show HN: Totle, daily math puzzle game; Saturday puzzles have the fewest answers"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50433154"
project_url: "https://playtotle.com/"
author: "zemelett"
published_at: "2026-11-09T22:25:18Z"
captured_at: "2026-11-10T09:49:42+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-11-10"
pub_day: "2026-11-09"
tags:
  - 语料
  - hn_show
  - author_zemelett
  - story_50433154
  - show_hn
metrics: {"points": 2, "comments": 0, "engagement_velocity": 2}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:3d"
---

# Show HN: Totle, daily math puzzle game; Saturday puzzles have the fewest answers

> [!info] 一句话导读
> My oldest two kids are off to college and since leaving we've been playing the Wordle and 'sharing' our solutions with each other. It's been a fun way to stay c…

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50433154>
> 指标：点赞=2 · 评论=0 · engagement_velocity=2
> 作者：zemelett　|　发布：2026-11-09T22:25:18Z
> 项目链接：<https://playtotle.com/>
> 采集：2026-11-10T09:49:42+08:00　|　id：`56fc0865d7450ced`

## 正文

My oldest two kids are off to college and since leaving we've been playing the Wordle and 'sharing' our solutions with each other. It's been a fun way to stay connected with them, and it's become a bit of a challenge to see if we can beat each other's solutions. This got me thinking about other ways I could connect with them. The thing about the Wordle is that it doesn't take a large commitment of time, you can just pull it out when you've a few spare minutes. So I set out to build a game that would borrow from many of the themes that keep pulling us back to Wordle. What I created is called Tōtle which fits another one of our (okay my) favorite things; Dad jokes and puns (as it’s pronounced total).Here's how it works. You get five different numbers from a number pool 1 to 20, and a target from the remaining pool. Combine two at a time with + − × ÷, using all five numbers, every result a positive whole number, each puzzle always takes 4 moves. You get 3 rounds and 4 undos per round; a medal for fewest moves (perfect 4 = crown). There's a spoiler-free share card, like Wordle’s grid.The combinatorics math works out like this: C(20,5) (that's choose 5 from 20) × 15 possible target numbers = 232,560 possible puzzles. An interesting side quest: exhaustive search discovered that exactly 6 can’t be solved. They all are from the group of 6 numbers: 3, 7, 16, 17, 19, 20. If any one of those is chosen as the target the other 5 cannot make the target. I'm not sure if there are any interesting reasons or patterns.Every puzzle was sorted into 7 difficulty bands, by how many solutions each has, to provide a way to add increasing difficulty along the week. Sunday draws from the easiest 30%, Saturday from the hardest 3%, the game shows “harder than X% of puzzles” on the hardest days; Saturdays so far have been in the 98th–99th percentile of difficulty. 5 Saturdays were discovered to have exactly one answer (answer here means ways that only regroup or reorder the same moves count as one); the first is #68, Saturday, December 19, 2026.A few things I'd love to know from y'all:Difficulty: does the Sunday-to-Saturday curve feel right, and are Saturdays too hard? I've experimented with a mode that offers some help. But it's still under development.First-time play: was anything confusing, like dragging vs. tapping or how rounds work?Phones: How does it play on your phone vs your computer?

## 导航

- 项目页：[[10-项目/playtotle.com_51a1a839]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
