---
type: "corpus"
item_id: "ddb482011eaab069"
title: "Ran my first playtest here is what I learned"
source: "reddit"
source_name: "Reddit 独立开发版块"
url: "https://www.reddit.com/r/buildinpublic/comments/1xi6x8d/ran_my_first_playtest_here_is_what_i_learned/"
project_url: "https://v.redd.it/kvg3p666m4yh1"
author: "rectangle_so"
published_at: "2026-10-29T09:35:04+08:00"
captured_at: "2026-11-08T12:52:11+08:00"
lang: "en"
kind: "post"
topic: "游戏"
shard: "2026-11-08"
pub_day: "2026-10-29"
tags:
  - 语料
  - reddit
  - r/buildinpublic
metrics: {"score": 6, "comments": 12, "upvote_ratio": 1}
comments_count: 12
comments_total: 12
discovered_via: "reddit:14d+settle10"
---

# Ran my first playtest here is what I learned

> [!info] 一句话导读
> I finally got about 20 people together to test Poached last week

> [!meta]- 语料信息（点开展开）
> 来源：Reddit 独立开发版块（post）
> 原帖：<https://www.reddit.com/r/buildinpublic/comments/1xi6x8d/ran_my_first_playtest_here_is_what_i_learned/>
> 指标：得分=6 · 评论=12 · 赞踩比=1
> 作者：rectangle_so　|　发布：2026-10-29T09:35:04+08:00
> 项目链接：<https://v.redd.it/kvg3p666m4yh1>
> 采集：2026-11-08T12:52:11+08:00　|　id：`ddb482011eaab069`

## 正文

I finally got about 20 people together to test Poached last week

& halfway through, everyone started freezing and jumping around. soooo my first playtest failed(ish)

Poached is the biggest game I’ve attempted for EggVerse so far. Think MOBA (League/DOTA) x capture the flag (Fat Princess) typa game. 12 v 12 with matches aiming to run around 12-15 minutes

The matches started fine, which made the lag even more confusing. Turns out, every time the server saved the match, it stopped sending updates to the players until the save finished. The longer the match went on, the longer the saves took… & the worse it got

I rebuilt how rooms handle traffic and load-tested it with bots. In those tests, frame freezes went from 7 to 0, and worst-case ping dropped from about 150 ms to about 70 ms. Promising, but bots aren’t people, so the next playtest will be the real check

But the good part? People actually enjoyed the game & the only feedback i got was pretty much "cosmetic"

* They didn’t know they could break trees/rocks, so I’m adding outlines around things you can break
* They couldn’t tell when they were being targeted by the towers, so I’m adding a red outline
* The map was confusing, so I’m simplifying the layout with signs in the game & a map before the match starts
* Way too many announcements going off, so I’m saving those for bigger achievements like first crack or an “omelette” (basically a pentakill)

A lot of it was stuff that made sense to me because I’ve been staring at it for hours, but wasn’t obvious to someone playing for the first time. Also I guess the lag made it hard for anyone to really understand whats going on. But here’s what else I’ve been working on

* Went all in on the clay texture look & I love it
* Added defensive objects like gates/spikes & offensive ones like catapults/ladders
* Added fish to the river that swim away from you, which I thought was cute and funny
* Ive been refining the skill animations
* Posting content daily, minimum once but usually hitting around 3 a day
   * although none have popped off even though i thought some shouldve
* Constantly improving the minigames, and Couch Play

Meanwhile the arcade itself is still growing!! Since my last update here

* 571 -> 624 visitors
* 179 -> 213 players
* 1,643 -> 2,032 game starts
* 7 hours -> 15 hours 11 minutes of tracked gameplay

Seeing people spend their precious time using something I built is the most gratifying feeling in the entire world & I'm sure probably everyone here understands. Money is great, but providing value to someone is just so much more addicting.

Still building solo, but I am open to co-founders. preferably if you live in Toronto 🫣

If you’ve built games before, what’s something players struggled with that seemed obvious to you?

See what I’m building @ [eggverse.co](http://eggverse.co)

## 评论（12/12）

> **rectangle_so**（1 分） · 2026-10-29T09:35:37+08:00　
> Join the next Poached playtest on November 5 at 8pm (11 spots left)
>
> It's only 30 mins & would love your feedback!
> \+ you get an exclusive skin 🤭
>
> [**https://luma.com/i49c02im**](https://www.linkedin.com/safety/go/?url=https%3A%2F%2Fluma%2Ecom%2Fi49c02im&urlhash=TU1B&mt=iIk6GcUM1F2IlmGnXca2w9kEKILz7iCXJQBWOPOk8QjwnLKfqgjNIuwq4mS9kQfEaxJw07uoBSXatS5Jkz3qSSQJ5lemYVuHTIFcFKiDRAVkZyxJnZJiLGdgEvNF__-IPwspgtVcRA5iIIvkWXhn7VO81K1PEoES&isSdui=true)

---

> **Low-Store-6877**（2 分） · 2026-10-29T09:58:03+08:00　
> Freezing halfway through with 20 testers on a 12v12 is desync, plain. Photon relay at 24 players falls over fast, so you either move to headless dedicated servers (Fish-Net, Mirror) or drop to 6v6. 12-15 minute matches is already a lot of state to keep synced for a first playtest.

---

> **investigatormaker**（2 分） · 2026-10-29T10:03:54+08:00　
> Twenty people can't fill a 12 v 12 match, so the network fix isn't really confirmed until a test has 24 real players and runs the full 12 to 15 minutes, since the save stalls grew with match length. All four fixes are visual, so after each match ask testers one question per fix: did you break a tree or rock, did you notice a tower targeting you, did the pre-match map help, which announcements stuck. That shows which change actually landed.
>
> I make ThreadFox. We find relevant Reddit conversations and post for your business. We'll post 3 replies free first, no card; then the $79 Pilot covers seven days and up to 50 posts and replies. No automatic renewal. [https://threadfox.vip/p/eyubn/managed](https://threadfox.vip/p/eyubn/managed)
>
> Where did the first 20 testers come from?

---

> **ManufacturerMany2829**（2 分） · 2026-10-29T10:18:28+08:00　
> Ouch, but honestly 20 people showing up for a first test beats the usual silence. Freezing halfway through rather than at the start smells like a leak or a GC spike, so log memory and frame times on the next run and see if it hits the same minute again. 12v12 at 24 slots means you were near full load too.

---

> **QuanTradin**（2 分） · 2026-10-29T10:29:33+08:00　
> the save blocking the tick loop is a classic, and finding it from the symptom getting worse with match length is good debugging. bots at 0 freezes comes with an asterisk though: people pile onto the same objective at the same moment in a way bots never do, so load-test the teamfight, not the average.

---

> **rectangle_so**（1 分） · 2026-10-29T11:01:42+08:00　
> I actually had more than 20 sign ups but only 20 showed up & they were all people I knew throughout my life. Def a good point to ask those questions back to them, I will keep that in mind for the next test!

---

> **rectangle_so**（1 分） · 2026-10-29T11:03:41+08:00　
> I've thought about hosting my game on a different platform, but I tested it again during a pitch at builders sunday & it seemed to be a lot smoother than the first time. So hopefully its fixed this time, but I won't know until I try again.

---

> **rectangle_so**（1 分） · 2026-10-29T11:04:46+08:00　
> Yeeeep, I think I've fixed it so I'm hoping my next playtest on Nov 5 goes smoothly

---

> **rectangle_so**（1 分） · 2026-10-29T11:08:23+08:00　
> So I ran another small test with 24 people when i presented at Shopifys builder sundays, and it seemed to hold up but it also wasnt the full match. I added logs in anticipation and didnt see any spikes, which is a great sign but we will see on the next test on Nov 5.
>
> but yeah honestly it was quite disappointing because I felt like I let all of those people down with a bad playing experience. brutal.

---

> **InformalSong2789**（2 分） · 2026-10-29T12:50:26+08:00　
> Honestly the fact that 20 people showed up and you still found the root cause is a win. Most first playtests just crash and nobody knows why. You'll get em on Nov 5.

---

> **rectangle_so**（1 分） · 2026-10-30T07:36:20+08:00　
> I appreciate you!! Well I hope I found the root cause, not sure if there is something else hiding for me 😂

---

> **InformalSong2789**（2 分） · 2026-10-30T08:09:25+08:00　
> there's always something else hiding lol, but that's just game dev. root cause or not, you're way ahead of where most people are after a first playtest

## 关联链接

- http://eggverse.co

## 导航

- 项目页：[[10-项目/v.redd.it_e597a9d2]]
- 渠道页：[[50-渠道/reddit]]
- 赛道：`游戏`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
