---
type: "corpus"
item_id: "0b2fae6455afbeed"
title: "Show HN: Phive, a Gomoku-like game to play with friends or solo"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=48340891"
project_url: "https://phive.app/"
author: "0xCA1EB"
published_at: "2026-05-30T21:43:00Z"
captured_at: "2026-09-21T01:43:12+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-21"
pub_day: "2026-05-30"
tags:
  - 语料
  - hn_show
  - author_0xCA1EB
  - story_48340891
  - show_hn
metrics: {"points": 19, "comments": 9, "engagement_velocity": 19}
comments_count: 9
comments_total: 9
discovered_via: "hn:show_hn:144d"
---

# Show HN: Phive, a Gomoku-like game to play with friends or solo

> [!info] 一句话导读
> In 2025, my family and I had a long streak of playing a Gomoku / Go Bang / five-in-a-row based game called OK Play. I built a web version so that we could play …

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=48340891>
> 指标：点赞=19 · 评论=9 · engagement_velocity=19
> 作者：0xCA1EB　|　发布：2026-05-30T21:43:00Z
> 项目链接：<https://phive.app/>
> 采集：2026-09-21T01:43:12+08:00　|　id：`0b2fae6455afbeed`

## 正文

In 2025, my family and I had a long streak of playing a Gomoku / Go Bang / five-in-a-row based game called OK Play. I built a web version so that we could play any time we wanted (i.e. on our phones after kiddos went to sleep).The first player to get five-in-a-row (horizontally, vertically, or diagonally) wins. In the first phase of play, players take turns placing their pieces next to existing pieces (always edge-to-edge; you can't place a piece with only a corner-to-corner connection). After players exhaust their pieces, play moves into the movement phase: you pick up an existing piece you own and place it according to the previous placement rules. During the movement phase, you cannot move a piece that would leave other pieces disconnected. Play continues in player order until someone wins.I wrote the app using Elixir's Phoenix framework with Daisy UI / Tailwind CSS for styling. The app is deployed on Gigalixir via its generous free plan. I am by no means a frontend developer / designer, so there's for sure better ways to implement things than what I have here. I mostly focused on making it mobile friendly and getting it to support light and dark mode. There likely exists browser / device specific bugs, since we've only tested it out on our phones (iPhone 13 Pro, Safari / Chrome) and my computer (MacBook Pro, Safari). Happy to hear any suggestions, frontend or otherwise, if you have them!Developing this has been a real journey. Highlights have included learning about Gomoku and its variants, articulation points (and Trajan's algorithm for strongly connected components), and the Monte Carlo tree search algorithm (for the intermediate level "AI" mode I've recently added for single-player use). Lowlights have all been CSS related.I'd love to add a "matchmaking" mode in the future. I haven't really looked too much into the mechanics for how that's usually done though - it'll be a great learning opportunity!

## 评论（9/9）

> **gus_massa** · 2026-05-31T22:55:15.000Z　
> I played against the AI.The red "new game" button is too visible. I pressed it twice in the first times, and then I learned to not press it. Perhaps it would be nice to hide it a little.When the AI has an obvious move like in the case "Ai Hu Hu Hu Hu " , then the AI plays too fast. We made some games a long time ago and we added a minimal delay (like .2 seconds?) so it's easier to understand that you play and later the AI plays. (Also, to make the computer seem smarted, because it has to think a lot :) .)

---

> **iainmerrick** · 2026-06-03T09:11:40.000Z　
> Nice work, this is fun! I've only played against the AI so far, managed to win on Beginner.I think it would benefit from some little animations so it's clearer what's going on. But making that work nicely across both desktop and mobile could be a real pain, so I wouldn't blame you for punting it until later. :)A smaller suggestion: maybe draw all the spare pieces on screen, rather than just displaying e.g. "15 pcs" as text. That way you can see at a glance when your stock is dwindling. Experts won't need that but it could be useful for beginners.

---

> **mainecoder** · 2026-06-03T13:23:07.000Z　
> Here are my thoughts this is an amazing idea and I can see incredible potential because of its simplicity, I won on beginner one so far please play OPus Magnum by Zactronics for some inspiration this could be more developed. I can see myself playing this with piano music in the background and a story line. Additionally, when it start it does not have to start from zero you can add puzzles where a play was already happening and you are trying to win to make it more challenging. PLease talk to people with Game design experience and puzzle solvers. Awesome job

---

> **casey2** · 2026-06-03T19:34:49.000Z　
> AI is way too easy, even on advance it loses before end game (to a noob) and goes completely off rails during the endgame.There should be a way to determine where a move is placed, either slowing down the placement or highlighting the last move.

---

> **0xCA1EB** · 2026-06-01T01:27:11.000Z　
> I genuinely appreciate that feedback! I'll get a minimal delay patched in tomorrow (plus a new approach to the New Game button).

---

> **0xCA1EB** · 2026-06-03T09:53:52.000Z　
> Okay so I happened to catch this comment fresh-out-of-the-oven and spent the last 30 minutes working on this: https://cdn.zappy.app/475bb0a1f788709fee92401ee6860bb3.pngI'm happy with that change! I'll get it pushed live.As for animations ... :grimacing: I'm afraid that's beyond my current skill level lol.

---

> **gus_massa** · 2026-06-01T18:29:24.000Z　
> I like the new version.Is it posible to make a bot that is not so good playing the game?

---

> **0xCA1EB** · 2026-06-01T20:29:00.000Z　
> I took a stab at it - there's a new Beginner / Intermediate / Expert page when starting a solo game. :DIt's tough striking a balance between too easy / too tough. Let me know what you think if you give it a try!I also added a Share button:- Beginner: https://phive.app/replay/9ZM3MH455K- Advanced: https://phive.app/replay/M36SWRHR37

---

> **gus_massa** · 2026-06-01T22:07:39.000Z　
> I finaly won a game! Agaist the easy bot :)

## 导航

- 项目页：[[10-项目/phive.app_431eca5c]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
