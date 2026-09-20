---
type: "corpus"
item_id: "2df32d848d6e68d5"
title: "My experience of implementing GGPO-style rollback netcode for my 3D melee arena fighter"
source: "reddit"
source_name: "Reddit 独立开发版块"
url: "https://www.reddit.com/r/IndieDev/comments/1ujqz3u/my_experience_of_implementing_ggpostyle_rollback/"
project_url: "https://v.redd.it/y1894v72lfah1"
author: "AbyssDeepen"
published_at: "2026-06-30T22:35:17+08:00"
captured_at: "2026-09-21T01:30:35+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-21"
pub_day: "2026-06-30"
tags:
  - 语料
  - reddit
  - r/indiedev
  - Discussion
metrics: {"score": 3, "comments": 0, "upvote_ratio": 0.71}
comments_count: 0
comments_total: 0
discovered_via: "reddit:113d+settle3"
---

# My experience of implementing GGPO-style rollback netcode for my 3D melee arena fighter

> [!info] 一句话导读
> Over the past few months, I’ve been working on the netcode for my 3D melee arena fighter Rasen and I’d like to share my experience.

> [!meta]- 语料信息（点开展开）
> 来源：Reddit 独立开发版块（post）
> 原帖：<https://www.reddit.com/r/IndieDev/comments/1ujqz3u/my_experience_of_implementing_ggpostyle_rollback/>
> 指标：得分=3 · 评论=0 · 赞踩比=0.71
> 作者：AbyssDeepen　|　发布：2026-06-30T22:35:17+08:00
> 项目链接：<https://v.redd.it/y1894v72lfah1>
> 采集：2026-09-21T01:30:35+08:00　|　id：`2df32d848d6e68d5`

## 正文

**Hi everyone,**

Over the past few months, I’ve been working on the netcode for my 3D melee arena fighter Rasen and I’d like to share my experience.

**Unreal Engine systems**

Although I knew about GGPO netcode from the beginning, I was so intimidated by the amount of work involved. Instead, I started with delay-based networking, then experimented with Unreal's Character Movement Component, tried the Unreal Mover, and even built some custom networking solutions on top of the CMC.

Unfortunately, none of these were a good enough fit for this kind of fast-paced, parry-based, knockback-heavy combat.

Even with low ping, either the latency felt very high or there were visible corrections and out-of-sync animations. Also, my custom animation syncing was conflicting with the CMC's built-in root motion syncing and knockbacks were especially really bad.

**GGPO rollback netcode**

While experimenting with all these systems, I learnt more and more about GGPO solutions. With no other option, I finally decided to implement my own GGPO rollback architecture in Unreal Engine, along with the custom deterministic physics and movement required for it to all work.

Fortunately, the game had already been developed for offline play first, so I knew exactly what needed to be simulated. From the beginning, I've been trying to keep everything lightweight, deterministic and precomputed wherever possible.

After about 2 months of work, many battles with input prediction bugs, getting stuck on some movement bugs and finding a way to somehow bake and store 3D weapon collision data, I finally did it.

I was genuinely surprised by how cheap the simulation was: \~0.01ms per simulation tick with 8 characters. The snapshot size also seems to be small at \~0.04 KB per character.

**Result & reflection**

The game now features GGPO-style rollback netcode for up to 8 players, keeping controls responsive even under high ping, jitter and packet loss.

This is the most challenging system I've built so far. Although it was intimidating at first, it ended up being the most fun and rewarding system I've worked on.

I also made a [Youtube Devlog](https://youtu.be/7O7Tol3Ymvo) showcasing the gameplay under various stress tests, along with some performance statistics.

Hope this encourages you to try implementing your own rollback netcode if your game runs into similar issues.

## 关联链接

- https://youtu.be/7O7Tol3Ymvo

## 导航

- 项目页：[[10-项目/v.redd.it_cf94fbc4]]
- 渠道页：[[50-渠道/reddit]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
