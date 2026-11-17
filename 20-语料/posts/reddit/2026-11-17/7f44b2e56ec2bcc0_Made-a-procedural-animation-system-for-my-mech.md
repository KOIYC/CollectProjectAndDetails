---
type: "corpus"
item_id: "7f44b2e56ec2bcc0"
title: "Made a procedural animation system for my mech"
source: "reddit"
source_name: "Reddit 独立开发版块"
url: "https://www.reddit.com/r/IndieDev/comments/1xpt2n8/made_a_procedural_animation_system_for_my_mech/"
project_url: "https://v.redd.it/2rj66j44530i1"
author: "Grocery-Advanced"
published_at: "2026-11-07T08:44:28+08:00"
captured_at: "2026-11-17T11:10:04+08:00"
lang: "en"
kind: "post"
topic: 开发者工具
shard: "2026-11-17"
pub_day: "2026-11-07"
tags:
  - 语料
  - reddit
  - r/indiedev
  - Video
metrics: {"score": 185, "comments": 24, "upvote_ratio": 0.9894179894179894}
comments_count: 23
comments_total: 24
discovered_via: "reddit:14d+settle10"
---

# Made a procedural animation system for my mech

> [!info] 一句话导读
> Published: 2026-11-07

> [!meta]- 语料信息（点开展开）
> 来源：Reddit 独立开发版块（post）
> 原帖：<https://www.reddit.com/r/IndieDev/comments/1xpt2n8/made_a_procedural_animation_system_for_my_mech/>
> 指标：得分=185 · 评论=24 · 赞踩比=0.9894179894179894
> 作者：Grocery-Advanced　|　发布：2026-11-07T08:44:28+08:00
> 项目链接：<https://v.redd.it/2rj66j44530i1>
> 采集：2026-11-17T11:10:04+08:00　|　id：`7f44b2e56ec2bcc0`

## 正文

Published: 2026-11-07
Author: u/Grocery-Advanced

Reddit - The heart of the internet

 10d ago

# Made a procedural animation system for my mech

 EDIT: Thank you everyone for appreciating it! I’ve made a discord server where i’ve posted some other pics from the game and will regularly post progress updates. I’d be really happy if you joined it :) - https://discord.gg/EvJZY3tVm3

# Reddit - The heart of the internet

## 评论（23/24）

> **RoninForge_**（8 分） · 2026-11-07T09:09:13+08:00　
> That walk looks great in the open field, the way the legs settle as it moves really sells the weight. Is the foot planting IK, or is the whole stride driven by the procedural system?

---

> **Grocery-Advanced**（5 分） · 2026-11-07T09:59:23+08:00　
> Thanks! Yeah, the foot planting is ik. The weight comes from damped springs on the hips and torso, plus shifting the body over the planted foot before the next step.

---

> **RoboticElfJedi**（3 分） · 2026-11-07T10:38:01+08:00　
> Great Steampunk look, very well done. This is the sort of look that could hook people in. What's the game?

---

> **Grocery-Advanced**（2 分） · 2026-11-07T10:45:01+08:00　
> Thanks! i’m not fully decided on the exact gameplay loop yet, but i’m currently working on being able to assemble your own mech with different parts for the engine, legs, weapons  etc.
> after that maybe I’ll implement other mechs whom you have to fight and you can scrap and take their parts.
>
> None of its decided yet though, i’m just tryna make it feel good and be fun

---

> **PositiveAd6708**（1 分） · 2026-11-07T11:37:32+08:00　
> Love how the weight and sway looks I definitely wanna see some destruction

---

> **Grocery-Advanced**（1 分） · 2026-11-07T11:41:50+08:00　
> glad you like it! destruction is definitely coming next

---

> **ImScoob**（1 分） · 2026-11-07T12:17:38+08:00　
> Great! I’m actually intrigued and would wishlist this

---

> **Zeplin108**（3 分） · 2026-11-07T12:21:00+08:00　
> Hell yes, lets get some more Italian mechs!
>
> https://i.redd.it/z26bite6a40i1.jpeg

---

> **guac-o**（1 分） · 2026-11-07T13:42:18+08:00　
> So much charm! If the gameplay is fun, you’ve got something quite cool!!

---

> **RoadRocketDev**（1 分） · 2026-11-07T13:44:37+08:00　
> Gives off Mortal Engines vibes! I like it

---

> **Dangerous_Ice_6627**（1 分） · 2026-11-07T14:17:27+08:00　
> Looks awesome! Reminds me of that Love, Death & Robots episode with the farmers in mech suits!

---

> **Grocery-Advanced**（1 分） · 2026-11-07T14:25:29+08:00　
> That was actually one of the main inspirations! glad you like it

---

> **apex7734**（1 分） · 2026-11-07T17:16:41+08:00　
> Infantry would also be fun to fight I believe. But I see this and immediately see a potential warhammer battlefield simulator too so take it with a grain of salt lmao.

---

> **Manana_Split**（1 分） · 2026-11-07T18:21:14+08:00　
> Is the shadow being updated at a lower framerate than the rest of the scene? If so, how? It looks really good. My first guess is that you have a separate copy of the robot mesh that only casts shadows, and you update the transform of it at a reduced rate.

---

> **SiroStudios**（1 分） · 2026-11-07T19:19:09+08:00　
> La sombra esta muy lograda,animo.

---

> **DarkRoster**（1 分） · 2026-11-07T23:15:05+08:00　
> Are you rendering the shadow in every frame? What method did you use?

---

> **Grocery-Advanced**（1 分） · 2026-11-07T23:20:37+08:00　
> It’s a custom shadow pass. the sun draws all the shadows into one shadow map and only refreshes it every 3rd frame. I thought the choppy look was kinda cool, and it saves a bit of performance on my potato.

---

> **Grocery-Advanced**（1 分） · 2026-11-07T23:20:47+08:00　
> It’s a custom shadow pass. the sun draws all the shadows into one shadow map and only refreshes it every 3rd frame. I thought the choppy look was kinda cool, and it saves a bit of performance on my potato.

---

> **Manana_Split**（1 分） · 2026-11-07T23:23:44+08:00　
> Nice, have to test it for my game also. Looks good!

---

> **DarkRoster**（1 分） · 2026-11-07T23:29:44+08:00　
> Thanks a lot.

---

> **Emotional-Cut2952**（1 分） · 2026-11-07T23:39:22+08:00　
> have you tried a low resolution instead of a lower frame rate? I think the former with some basic blurring to overcome aliasing would work better.
>
> anyway i love this work both the procedural part, but also the fx it feels punch plus this guy somehwo feels very real and personl , love it!

---

> **Emotional-Cut2952**（2 分） · 2026-11-07T23:40:55+08:00　
> could i recommend an rpg/rtt style game where you lead a defense againt a tyranical technologically empire where peasants learn to build mechs out of their farming tools and lead a resistance?

---

> **After_Sale_2203**（1 分） · 2026-11-10T06:50:11+08:00　
> Its so satisfying..

## 关联链接

- https://discord.gg/EvJZY3tVm3

## 导航

- 项目页：[[10-项目/v.redd.it_61f3e645]]
- 渠道页：[[50-渠道/reddit]]
- 赛道：`开发者工具`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
