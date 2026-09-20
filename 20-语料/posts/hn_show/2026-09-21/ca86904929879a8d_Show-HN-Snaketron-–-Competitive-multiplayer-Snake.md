---
type: "corpus"
item_id: "ca86904929879a8d"
title: "Show HN: Snaketron – Competitive multiplayer Snake. Back after 14 years"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49499499"
project_url: "https://snaketron.io/"
author: "lopatin"
published_at: "2026-08-30T15:23:52Z"
captured_at: "2026-09-21T02:57:17+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-21"
pub_day: "2026-08-30"
tags:
  - 语料
  - hn_show
  - author_lopatin
  - story_49499499
  - show_hn
metrics: {"points": 5, "comments": 1, "engagement_velocity": 5}
comments_count: 1
comments_total: 1
discovered_via: "hn:show_hn:52d"
---

# Show HN: Snaketron – Competitive multiplayer Snake. Back after 14 years

> [!info] 一句话导读
> Hi HN, I just completed a rewrite of Snaketron, a competitive multiplayer Snake game. (Yes, yes, in Rust)A quick funny story about this game's history:Back in 2…

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49499499>
> 指标：点赞=5 · 评论=1 · engagement_velocity=5
> 作者：lopatin　|　发布：2026-08-30T15:23:52Z
> 项目链接：<https://snaketron.io/>
> 采集：2026-09-21T02:57:17+08:00　|　id：`ca86904929879a8d`

## 正文

Hi HN, I just completed a rewrite of Snaketron, a competitive multiplayer Snake game. (Yes, yes, in Rust)A quick funny story about this game's history:Back in 2012 I had (poorly) implemented the first version of Snaketron. The issue with it was that I was keeping game state on the client, and while I did realize that it was insecure, I also had no idea what to do about it without increasing latency to unplayable levels. I was still in school, never worked on games, and haven't even heard of the term "netcode" before. The excitement of releasing my first pet project got the better of me, and I placed this security concern in the "theoretical issues" bucket, and shipped it.No one would even notice, and if they did, they wouldn't take the time to break into my little Snake game project, right?WRONG! Hacker News absolutely lived up to its name. While I was busy with my first experience of handling a traffic surge, scaling up my database and fixing bugs, several players found the security holes and were beginning their Snake rampage. Reports were coming in of unkillable snakes so I decided to start up a game to see if I could catch it.I loaded a 1v1 and my opponent was ... space invaders. My snake was a snake. Their "snake" was a rendering of the game Space Invaders. Needless to say they were also moving around and were invincible. I really wish I had taken a video of that, but I was floored that HN not just played, but hacked, my project is such an epic way.I always wanted to rebuild it properly, so here's V2! The architecture and motivations are quite different this time around.First, the state is server authoritative and lag is compensated for by client-state prediction. The game engine is written in Rust and compiled to WASM for the client side library.To minimize the ops burden, I also imposed a strict resiliency requirement on this project: it must be auto-scalable. So a node can join the cluster and live games will rebalance to it without disrupting gameplay.I also tried to make the new Snaketron a little more fun. The core mechanic is still, like classic Snake, collecting food without crashing. But now team matches have an objective to make competitive games more structured. There's also a Bronze to Grand Master ranking sub system (if enough people play, calibrating this will be interesting) and some fun features like boosting, combos, skins, and Play Of The Game detection.On Rust: One of my original goals for doing this in Rust was so that I could learn the language. That didn't work out as well as I thought it would. Usually I learn by building stuff, but AI got so good that I stopped writing code by hand and preferred to spend my nights & weekends working on what was more intereting to me than borrow checking errors: game design and the high availability stuff.On AI: Who knows if this would have gotten done without AI. Probably not, what with my day job and other things going on in life. It's 200k LOC (most of that is tests don't worry) but still.Anyway, here are the project links. Thank you for reading, I hope you enjoy the game and any feedback is very much appreciated![0] https://snaketron.io[1] https://github.com/lopatin/snaketron[2] https://news.ycombinator.com/item?id=4028597 (original post from 2012)

## 评论（1/1）

> **zcchriti** · 2026-08-30T23:50:07.000Z　
> you reminded me of the game that used to be on old Nokia if you were born on 90s you will surely know , by the way the website is not working

## 关联链接

- https://github.com/lopatin/snaketron[2
- https://news.ycombinator.com/item?id=4028597
- https://snaketron.io[1

## 导航

- 项目页：[[10-项目/snaketron.io_1cd6c1e0]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
