---
type: "corpus"
item_id: "b26b9791e6c102a9"
title: "Show HN: LiSkat: Free real-time Skat with Elo and bots"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=48725442"
project_url: "https://liskat.com/"
author: "iNic"
published_at: "2026-06-29T21:22:32Z"
captured_at: "2026-09-21T02:54:40+08:00"
lang: "en"
kind: "post"
topic: "游戏"
shard: "2026-09-21"
pub_day: "2026-06-29"
tags:
  - 语料
  - hn_show
  - author_iNic
  - story_48725442
  - show_hn
metrics: {"points": 3, "comments": 2, "engagement_velocity": 3}
comments_count: 2
comments_total: 2
discovered_via: "hn:show_hn:113d"
---

# Show HN: LiSkat: Free real-time Skat with Elo and bots

> [!info] 一句话导读
> Skat is a ~200 year old 3-player German trick-taking card game. I built a free site to play it online, solo against bots or with other people (matchmaking and E…

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=48725442>
> 指标：点赞=3 · 评论=2 · engagement_velocity=3
> 作者：iNic　|　发布：2026-06-29T21:22:32Z
> 项目链接：<https://liskat.com/>
> 采集：2026-09-21T02:54:40+08:00　|　id：`b26b9791e6c102a9`

## 正文

Skat is a ~200 year old 3-player German trick-taking card game. I built a free site to play it online, solo against bots or with other people (matchmaking and Elo).The bots are what I keep tinkering with. Card play is a linear model over hand features, with the weights tuned by self-play search. Bidding and declaring use Monte-Carlo rollouts.No signup needed to practice against the bots. It's all TypeScript (Svelte plus a small WebSocket server).GitHub: https://github.com/nic-kup/liskat

## 评论（2/2）

> **ekymz** · 2026-06-29T21:42:32.000Z　
> Nice bot architecture. How do you handle the Skat card phase committing blind before seeing the full hand seems like the hardest part to model.

---

> **iNic** · 2026-06-30T07:29:29.000Z　
> This is part of the MC rollout. I simulate the bot playing games with seeing the Skat, and playing games without seeing the Skat. Then it is based purely on which game has higher EV. Which cards to discard when looking at the Skat is another MC rollout.It is worth saying that the MC rollouts are fairly cheap because the playing architecture is cheap.

## 关联链接

- https://github.com/nic-kup/liskat

## 导航

- 项目页：[[10-项目/liskat.com_3335b8bb]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`游戏`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
