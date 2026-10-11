---
type: "corpus"
item_id: "fe246620c01d9abb"
title: "True per-pixel ray tracing light system in RPG Maker MZ for my game, Junko."
source: "reddit"
source_name: "Reddit 独立开发版块"
url: "https://www.reddit.com/r/IndieDev/comments/1wuknol/true_perpixel_ray_tracing_light_system_in_rpg/"
project_url: "https://v.redd.it/6akql2zzvqsh1"
author: "Sufficient-Pick710"
published_at: "2026-10-01T07:54:16+08:00"
captured_at: "2026-10-11T09:45:37+08:00"
lang: "en"
kind: "post"
topic: SaaS/B2B
shard: "2026-10-11"
pub_day: "2026-10-01"
tags:
  - 语料
  - reddit
  - r/indiedev
  - Video
metrics: {"score": 81, "comments": 13, "upvote_ratio": 0.98}
comments_count: 13
comments_total: 13
discovered_via: "reddit:14d+settle10"
---

# True per-pixel ray tracing light system in RPG Maker MZ for my game, Junko.

> [!info] 一句话导读
> This is an effects system I've been developing myself while locked away from society, ignoring all social norms and bodily needs.

> [!meta]- 语料信息（点开展开）
> 来源：Reddit 独立开发版块（post）
> 原帖：<https://www.reddit.com/r/IndieDev/comments/1wuknol/true_perpixel_ray_tracing_light_system_in_rpg/>
> 指标：得分=81 · 评论=13 · 赞踩比=0.98
> 作者：Sufficient-Pick710　|　发布：2026-10-01T07:54:16+08:00
> 项目链接：<https://v.redd.it/6akql2zzvqsh1>
> 采集：2026-10-11T09:45:37+08:00　|　id：`fe246620c01d9abb`

## 正文

This is an effects system I've been developing myself while locked away from society, ignoring all social norms and bodily needs.

I was unsatisfied with other solutions, which while extremely clever, didn't really give me the freakish realism I was looking for.

I am EXTREMELY proud of this and I can't wait to see how I can make my scenes more atmospheric.

## 评论（13/13）

> **OwO-animals**（2 分） · 2026-10-01T09:19:56+08:00　
> Intresting. I've been recently trying to use light in my game and actually I am quite happy with default lighting, but I am interested in how you managed raytracing. I was thinking the game could interpret pixels of each tile as unit and then make it brighter based on a ray of light that would bounce twice or thrice maybe with falling power. But I never tried it and I don't know if it would even work lol. Pretty cool result though!

---

> **GottaWigAtDaWigStore**（6 分） · 2026-10-01T09:54:08+08:00　
> As someone who has only recently gotten started with RPG Maker it always makes me smile to see something so unique made with the engine. Great stuff!

---

> **SharkScoops**（1 分） · 2026-10-01T09:58:45+08:00　
> This is awesome looking. And you have it running natively in MV? What's the performance like?

---

> **Sufficient-Pick710**（5 分） · 2026-10-01T10:17:51+08:00　
> Yes, this is native! Performance is incredibly lightweight. Framedrops will probably occur on weaker hardware determinant on GPU strength, I have yet to test on a system that's weak enough to encounter this consistently. I've tested on my main PC and a Chromebook.
>
> Regardless, performance is important to me - in the name of common sense practices I have added options ingame for the player to change the lighting resolution, reflection resolution, weather qualitywall shading resolution, shadow quality, how many shadow casters can be active at once, and if you still don't get full performance after that, you can turn down the internal resolution.
>
> I've also added placeholder framework for adding different quality presets, I'll adjust these over time as I get feedback from eventual playtesters.

---

> **Sufficient-Pick710**（3 分） · 2026-10-01T10:38:38+08:00　
> So the important distinction is that it really does perform ray-marching for its shadows, but it is not a conventional full 3D/RTX ray tracer.
>
> My plugin takes a 2D image and builds a 3D height model determined on what graphic is being processed. Then, for every visible point being lit, it determines whether that point can see the light, and if not, that point becomes shadowed. It also calculates how high above the ground the ray is at every step so a light can pass over a short table but be stopped by a tall bookcase.
>
> In other words, it reverse-engineers a fake 3D representation out of RPG Maker's 2D rendering conventions, then ray-marches through that representation on the GPU.

---

> **Sufficient-Pick710**（1 分） · 2026-10-01T10:40:09+08:00　
> The engine is only limited by your own mind. In the words of a wise man from Earthbound, "You got to expand your mind an' use this stuff creatively."

---

> **Justindr0107**（2 分） · 2026-10-01T10:44:16+08:00　
> I know this post is about lighting and it looks amazing so I have no notes there, but im surprised you didn't add droplets hitting the pavement/puddles when raining, and how would that affect the lighting?

---

> **Sufficient-Pick710**（2 分） · 2026-10-01T10:47:55+08:00　
> All in due time!
>
> It's in the pipeline as I continue working on the weather graphics. Getting the ripples from raindrops and reflection to work well was first on my list, I'm currently working on the particle system that will tie it together, and working out how to automate more of the process for tiling so I can have taller objects drip water down, windows streak water across, etc. Exciting, overkill stuff.

---

> **Academic_Pool_7341**（3 分） · 2026-10-01T10:57:54+08:00　
> Hay I was just thinking how cool this would be earlier today! I really like the way this turned out. Nice!
>
> What kind of game is this? I feel like it could look very good for an exploration or horror game. Do you have a steam page?

---

> **Sufficient-Pick710**（3 分） · 2026-10-01T11:07:47+08:00　
> This is a horror game with limited combat elements! You take on a role of a paranormal investigator.
>
> I don't have a Steam page just yet, but I will start the process of setting one up, as well as an Itch page.

---

> **The_Krytos_Virus**（2 分） · 2026-10-01T11:29:13+08:00　
> Man this looks goooooood
>
> ![gif](giphy|uDwKGxTFrADvO)

---

> **Acceptable_West_1312**（2 分） · 2026-10-01T12:36:41+08:00　
> I love how flexible RPG Maker is, to the point that people are making their own engines, basically turning it into this meme
>
> https://preview.redd.it/deqyk1y8bssh1.jpeg?width=360&format=pjpg&auto=webp&s=dfa678f40c5ddc5b16857921ceac658c126645a5

---

> **_Bethel__**（2 分） · 2026-10-01T15:40:59+08:00　
> My goodness

## 导航

- 项目页：[[10-项目/v.redd.it_735e1210]]
- 渠道页：[[50-渠道/reddit]]
- 赛道：`SaaS/B2B`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
