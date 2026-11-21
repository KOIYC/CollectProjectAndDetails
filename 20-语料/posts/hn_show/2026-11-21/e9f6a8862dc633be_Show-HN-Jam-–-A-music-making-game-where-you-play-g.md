---
type: "corpus"
item_id: "e9f6a8862dc633be"
title: "Show HN: Jam – A music making game where you play gigs to earn studio gear"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50584066"
project_url: "https://jam.resonantdsp.com/"
author: "garrinm"
published_at: "2026-11-20T23:51:32Z"
captured_at: "2026-11-21T14:45:01+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-11-21"
pub_day: "2026-11-20"
tags:
  - 语料
  - hn_show
  - author_garrinm
  - story_50584066
  - show_hn
metrics: {"points": 2, "comments": 1, "engagement_velocity": 2}
comments_count: 1
comments_total: 1
discovered_via: "hn:show_hn:3d"
---

# Show HN: Jam – A music making game where you play gigs to earn studio gear

> [!info] 一句话导读
> The idea comes from Chrome Music Lab, which was addictive and satisfying. I felt it could be that fun and easy to put down musical ideas and hear them grow into…

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50584066>
> 指标：点赞=2 · 评论=1 · engagement_velocity=2
> 作者：garrinm　|　发布：2026-11-20T23:51:32Z
> 项目链接：<https://jam.resonantdsp.com/>
> 采集：2026-11-21T14:45:01+08:00　|　id：`e9f6a8862dc633be`

## 正文

The idea comes from Chrome Music Lab, which was addictive and satisfying. I felt it could be that fun and easy to put down musical ideas and hear them grow into something more substantial. Simple at first, but with progressively more depth if the player wants to go there. That was the seed, and it spiraled from there into Jam.You start with one instrument, and you write parts on a piano roll. Create your own music or play gigs (levels) to earn coins and buy more gear. Each gig is built around one musical idea, so you pick up some music knowledge as you go. Friends can join your studio with a link and write parts alongside you.In my other Show HNs I've always come with my own code. In this case I didn't write the code, but I'm still proud of the outcome and I hope some of you will enjoy it too.The audio code is Rust/WASM running in a worklet. This is the part I had prior experience in, and it's been fun getting that into a browser. The instruments are decent and the signal chains hold their own. The front end is the agent's own design in three.js. The optimization work there was interesting because of how busy the UI gets and how many elements come into view. I focused on measuring React renders per interaction, instruction counts for the audio engine, load times and frame times. The result is something that runs decently even on a phone.The multiplayer side is simple. Each studio is a Cloudflare Durable Object that holds the song. Players connect to it over a WebSocket and send small actions (add a note, turn a knob). The object applies each action, stores the result and sends the updated session to anyone else in the room. This simple setup allows collaborative music making out of the gate, even though it's not the game's main focus (yet).This is a beta: feedback, comments and criticisms are all welcome. You can get into the game with no signup, and if you want to save your progress you'll be prompted to enter an email address.

## 评论（1/1）

> **mselma** · 2026-11-21T01:39:53.000Z　
> Tested it out, it’s awesome, got me bobbing along

## 导航

- 项目页：[[10-项目/jam.resonantdsp.com_4a53f1e9]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
