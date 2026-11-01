---
type: "corpus"
item_id: "251e052c941da5aa"
title: "We had a dream for an online fighting game with too many players, so we built custom rollback netcode to make it possible"
source: "reddit"
source_name: "Reddit 独立开发版块"
url: "https://www.reddit.com/r/IndieDev/comments/1xc3gh1/we_had_a_dream_for_an_online_fighting_game_with/"
project_url: "https://v.redd.it/7zdv0tzvrwwh1"
author: "purpleplattypus"
published_at: "2026-10-22T07:57:46+08:00"
captured_at: "2026-11-01T09:39:36+08:00"
lang: "en"
kind: "post"
topic: 开发者工具
shard: "2026-11-01"
pub_day: "2026-10-22"
tags:
  - 语料
  - reddit
  - r/indiedev
metrics: {"score": 8, "comments": 4, "upvote_ratio": 0.9}
comments_count: 4
comments_total: 4
discovered_via: "reddit:14d+settle10"
---

# We had a dream for an online fighting game with too many players, so we built custom rollback netcode to make it possible

> [!info] 一句话导读
> For the better part of the last 2 years our small team has been building an online party fighter.

> [!meta]- 语料信息（点开展开）
> 来源：Reddit 独立开发版块（post）
> 原帖：<https://www.reddit.com/r/IndieDev/comments/1xc3gh1/we_had_a_dream_for_an_online_fighting_game_with/>
> 指标：得分=8 · 评论=4 · 赞踩比=0.9
> 作者：purpleplattypus　|　发布：2026-10-22T07:57:46+08:00
> 项目链接：<https://v.redd.it/7zdv0tzvrwwh1>
> 采集：2026-11-01T09:39:36+08:00　|　id：`251e052c941da5aa`

## 正文

For the better part of the last 2 years our small team has been building an online party fighter.

Most fighting games are about endlessly beating on your friends in 1v1s -- we're trying to mix it up and put you on the *same team* as your friends, and have you face off against other teams in wacky mini-games until only one team remains.

We built custom rollback netcode from the ground up so that we could do crazy stuff like 12-player matches on huge stages with lots of items.

If this sounds up your alley, check it out: [Punch Upon A Time Demo](https://store.steampowered.com/app/4485570/Punch_Upon_a_Time/)

If you have questions about the networking stack, please feel free to ask in the comments!

## 评论（4/4）

> **letskoya**（1 分） · 2026-10-22T08:14:59+08:00　
> With 12 players, does one high-ping connection increase the rollback window for everyone, or can you contain its impact? Curious how you handle that with lots of items in play.

---

> **Vontre**（2 分） · 2026-10-22T09:56:37+08:00　
> Short answer is we have simple relay servers that mediates input packets. If a packet arrives very late, the server actually stomps it and instructs all clients (including the sender) to use prediction instead. Effectively if your real ping to the server is 500 or more it won't let you play at all, everything you try to do just gets stomped. We have various matchmaking settings and a server distribution service to ensure players have acceptable pings.

---

> **Inside_Preference641**（1 分） · 2026-10-22T11:17:48+08:00　
> The team format sounds appealing for friends with different skill levels. Do the mini-games give the less experienced player useful jobs beyond winning fights, so a strong teammate can help without effectively playing the whole round for them?

---

> **purpleplattypus**（1 分） · 2026-10-22T14:40:11+08:00　
> Exactly, yeah! In a few different ways:
>
> Objective modes do a lot of the heavy lifting here. In Capture the Flag, flag runner may be a good fit for the more experienced player while other players can move around less and just focus on preventing your team's flag from being stolen. In King of the Hill, you always want to make sure one player is on the main stage either scoring points or contesting the other team. Experienced player can go offstage to secure a KO while less experienced player stays on the point and fights off grounded threats. There's also just some more random / chaotic modes like Musical Chairs, Dodgeball, and Spotlight where you never know who will make the lucky play / be in the right place at the right time.
>
> In addition, some rounds will actually ask the team of 3 to split up - 2v2 Soccer and 1v1 Sumo for example. Experienced player can go to 1v1 Sumo, and the other two can team up in Soccer. When either match finishes you immediately go to spectate the remainder of your other team's match, so they can cheer on / give tips in Soccer, or they can catch the end of the experienced player showing their stuff in Sumo.

## 关联链接

- https://store.steampowered.com/app/4485570/Punch_Upon_a_Time/

## 导航

- 项目页：[[10-项目/v.redd.it_aab7f72c]]
- 渠道页：[[50-渠道/reddit]]
- 赛道：`开发者工具`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
