---
type: "corpus"
item_id: "6c55034a7af95003"
title: "I built a planner for myself. The hardest part had almost nothing to do with planning"
source: "reddit"
source_name: "Reddit 独立开发版块"
url: "https://www.reddit.com/r/EntrepreneurRideAlong/comments/1x8cq18/i_built_a_planner_for_myself_the_hardest_part_had/"
author: "CarQuiet7350"
published_at: "2026-10-17T23:15:21+08:00"
captured_at: "2026-10-27T23:48:03+08:00"
lang: "en"
kind: "post"
topic: 开发者工具
shard: "2026-10-27"
pub_day: "2026-10-17"
tags:
  - 语料
  - reddit
  - r/EntrepreneurRideAlong
  - Idea Validation
metrics: {"score": 3, "comments": 18, "upvote_ratio": 0.8}
comments_count: 17
comments_total: 18
discovered_via: "reddit:14d+settle10"
---

# I built a planner for myself. The hardest part had almost nothing to do with planning

> [!info] 一句话导读
> I started this because I kept trying planners and eventually abandoning them.

> [!meta]- 语料信息（点开展开）
> 来源：Reddit 独立开发版块（post）
> 原帖：<https://www.reddit.com/r/EntrepreneurRideAlong/comments/1x8cq18/i_built_a_planner_for_myself_the_hardest_part_had/>
> 指标：得分=3 · 评论=18 · 赞踩比=0.8
> 作者：CarQuiet7350　|　发布：2026-10-17T23:15:21+08:00
> 项目链接：—
> 采集：2026-10-27T23:48:03+08:00　|　id：`6c55034a7af95003`

## 正文

I started this because I kept trying planners and eventually abandoning them.

Super Productivity, Vikunja, Planify, TickTick — some of them were genuinely good. But I kept wanting the same thing: I didn't just want to plan tomorrow. I wanted to come back a week later and understand what actually happened.

So I started building Personal Planner.

The basic loop became:

plan the day → do the work → track the real time → review what happened → use that when planning again.

It now has an hour-by-hour Day view, timers that keep planned and actual time separately, daily and weekly reviews, a year-long consistency view, Experiments for trying routines for a few weeks, and an Inbox for things I want to schedule later.

Everything works locally first, so normal use doesn't depend on a server. Sync is optional.

The funny part is that the planner UI wasn't really the hard part. Sync was.

Offline changes, reconnecting, migrations, auth and getting two devices to agree took far more work than I expected.

I also went into this without Flutter experience, and somehow it ended up running on Android, Linux, Windows and macOS.

I'm not building it with some big monetization plan either. I made something I wanted to use, then figured I may as well share it with anyone who has the same problem.

Probably the biggest thing I've learned from it is that finishing the feature is often the easy part. Making the whole thing behave predictably in real use is where most of the work starts.

I'd be curious: for people here who built something mainly because they personally wanted it, when did you realise other people might actually want it too?

## 评论（17/18）

> **AutoModerator**（1 分） · 2026-10-17T23:16:18+08:00　
> Your [comment](https://www.reddit.com/r/EntrepreneurRideAlong/comments/1x8cq18/i_built_a_planner_for_myself_the_hardest_part_had/phbgm1i/) in /r/EntrepreneurRideAlong was automatically removed because it contained a URL or a markdown link.
>
> To keep our community focused and prevent spam, we do not allow URLs or links (including Reddit internal links) in comments at this time.
> If you believe this removal was a mistake, please [contact the moderators](https://www.reddit.com/message/compose?to=/r/EntrepreneurRideAlong).
>
> *I am a bot, and this action was performed automatically. Please [contact the moderators of this subreddit](/message/compose/?to=/r/EntrepreneurRideAlong) if you have any questions or concerns.*

---

> **CarQuiet7350**（1 分） · 2026-10-17T23:16:36+08:00　
> https://preview.redd.it/ut79u58zn1wh1.png?width=1920&format=png&auto=webp&s=516837717b8351e3ca376c4962d135725fe74708
>
> Day task page here :)

---

> **CarQuiet7350**（1 分） · 2026-10-17T23:16:48+08:00　
> https://preview.redd.it/kcgeowo0o1wh1.png?width=1920&format=png&auto=webp&s=4fc4f4023504d4a096a55ef4195f1c7913c46226
>
> Daily review page here :)

---

> **CarQuiet7350**（1 分） · 2026-10-17T23:17:04+08:00　
> https://preview.redd.it/4w0jjy22o1wh1.png?width=1920&format=png&auto=webp&s=e9bf43e5d739c0cba431871be24803a477b327fe
>
> Weekly review page here :)

---

> **CarQuiet7350**（1 分） · 2026-10-17T23:17:32+08:00　
> https://preview.redd.it/67ymfil3o1wh1.png?width=1704&format=png&auto=webp&s=20a6d900fc1c615757b6e6e81d18886602f42e62
>
> My favorite part experiment page :), if you like it do try it out.

---

> **Ok_Mycologist4328**（1 分） · 2026-10-17T23:26:45+08:00　
> not gonna lie this looks way more put together than i expected from a solo project. the hour-by-hour view with planned vs actual time is exactly the kind of thing i always wish other tools had but they never quite get right
>
> sync being the nightmare part checks out though, every dev i know who's tried building something offline-first ends up with the same war story. what did you use for the sync layer or did you roll your own

---

> **Hoard_space**（1 分） · 2026-10-18T03:12:01+08:00　
> Honestly, I can relate to this. Sometimes you build something just because you need it yourself, then later realise other people might need it too. The sync part sounds like a headache though ,did you expect it to take that much work when you first started?

---

> **Key_Raisin8568**（1 分） · 2026-10-18T03:47:45+08:00　
> mine was kinda the opposite, i built a thing because a few contractors i know kept griping about paying monthly for estimate software they barely used. so i knew other people wanted it before i did lol. and yeah, sync is always the monster, offline-first plus two devices disagreeing is where the weekends go

---

> **CarQuiet7350**（1 分） · 2026-10-18T11:47:24+08:00　
> No i thought it could be easy but ended up one of the most challenging parr 😅

---

> **CarQuiet7350**（1 分） · 2026-10-18T11:48:02+08:00　
> Yes man it took 3 month approx to finish this 😂

---

> **Early_Key_823**（1 分） · 2026-10-18T12:02:49+08:00　
> Hard part

---

> **CarQuiet7350**（1 分） · 2026-10-18T12:45:56+08:00　
> Thanks, really appreciate that! The planned vs actual time was actually one of the main reasons I started building this :)
>
> For sync, I went with Drift + SQLite for local storage and Supabase (PostgreSQL) for the cloud side. I ended up building my own sync layer on top of that, with a local outbox that queues changes when offline and syncs them once the connection is back.
>
> I also use a Cloudflare Worker to handle the initial Supabase project setup, but after that the app talks directly to Supabase.
>
> And yeah, you weren't kidding about offline-first being a nightmare lol 😂

---

> **Nayele_Cumbe**（1 分） · 2026-10-18T17:51:25+08:00　
> the fact that you built it for yourself first is a good sign tbh. the risk is over-fitting it to your own workflow so much that nobody else can onboard without your exact mental model. worth watching how first-time users react to the day view

---

> **CarQuiet7350**（1 分） · 2026-10-18T18:00:13+08:00　
> I feel that many people will sync to the majority of the parts :),btw have you tried it out?

---

> **CarQuiet7350**（1 分） · 2026-10-18T18:01:03+08:00　
> You can have he look of the app here
>
> https://reddit.com/link/phgwrq4/video/b8o2mftl87wh1/player

---

> **Pink_Sky_8102**（1 分） · 2026-10-18T20:14:08+08:00　
> For me, the point where other people start asking for it without much convincing is usually the signal. Building for yourself is great because you understand the problem deeply, but once strangers start using it and coming back, that’s when it starts feeling like more than just a personal tool.

---

> **CarQuiet7350**（1 分） · 2026-10-18T20:19:51+08:00　
> Yes definitely man that's what I am feeling right now, btw what's your first impressions on the app :)

## 导航

- 项目页：[[10-项目/I-built-a-planner-for-myself.-The-hardest-part-h_6c55034a]]
- 渠道页：[[50-渠道/reddit]]
- 赛道：`开发者工具`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
