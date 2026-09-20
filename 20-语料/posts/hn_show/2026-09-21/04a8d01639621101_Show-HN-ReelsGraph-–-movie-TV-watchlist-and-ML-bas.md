---
type: "corpus"
item_id: "04a8d01639621101"
title: "Show HN: ReelsGraph – movie/TV watchlist and ML-based discovery queue, no signup"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=48731876"
project_url: "https://reelsgraph.com/"
author: "Whiskee"
published_at: "2026-06-30T12:37:48Z"
captured_at: "2026-09-21T01:44:57+08:00"
lang: "en"
kind: "post"
topic: 开发者工具
shard: "2026-09-21"
pub_day: "2026-06-30"
tags:
  - 语料
  - hn_show
  - author_Whiskee
  - story_48731876
  - show_hn
metrics: {"points": 3, "comments": 2, "engagement_velocity": 3}
comments_count: 2
comments_total: 2
discovered_via: "hn:show_hn:113d"
---

# Show HN: ReelsGraph – movie/TV watchlist and ML-based discovery queue, no signup

> [!info] 一句话导读
> Show HN: ReelsGraph – movie/TV watchlist and ML-based discovery queue, no signup

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=48731876>
> 指标：点赞=3 · 评论=2 · engagement_velocity=3
> 作者：Whiskee　|　发布：2026-06-30T12:37:48Z
> 项目链接：<https://reelsgraph.com/>
> 采集：2026-09-21T01:44:57+08:00　|　id：`04a8d01639621101`

## 正文

Show HN: ReelsGraph – movie/TV watchlist and ML-based discovery queue, no signup

## 评论（2/2）

> **Whiskee** · 2026-06-30T12:46:06.000Z　
> Well, I had context and a nice technical explanation for it ready, but my longer comments get instaflagged since the account is new, so I'll let this cool off for a bit first.

---

> **Whiskee** · 2026-06-30T12:52:56.000Z　
> In short: it's a site to track the movies and shows you've watched and quickly figure out what to watch next rather than scrolling Netflix squares for two hours.Bit of a backstory: I've been running GamesGraph, a game backlog/discovery site, solo since 2019. The core problem there (you've got this huge pile of stuff from Steam sales, what do you even play next? Instant decision paralysis) translates pretty well to films and shows, so I decided to fork the whole thing. Same engine and same interface, except it's pointed at films and shows. I rely on the TMDB API and I've seeded the ML model with ~32 million real ratings from MovieLens, so it's based on collaborative filtering rather than genre tags.Everything you rate tells the site how to rank your watchlist, so the backlog sorts itself and gently nudges you to either watch whatever is at the top or consciously push it to the bottom. The discovery queue has a one-at-a-time format with plenty of useful filters for power users.Be aware: the TV side is admittedly a bit raw, because I've only had a few testers so far and this needs more data for accurate recommendations, so you might want to start from movies. It's completely free, no account needed unless you want to save your progress, and I'm not planning to monetize. Poke around and tell me where it gets your taste wrong or what's confusing.

## 导航

- 项目页：[[10-项目/reelsgraph.com_a10d116d]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`开发者工具`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
