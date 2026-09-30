---
type: "corpus"
item_id: "7b207103d17a1005"
title: "Show HN: Phyics-Based Dice Roller"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49900760"
project_url: "https://dice.jswidler.com/"
author: "swid"
published_at: "2026-09-29T21:19:35Z"
captured_at: "2026-09-30T18:57:45+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-30"
pub_day: "2026-09-29"
tags:
  - 语料
  - hn_show
  - author_swid
  - story_49900760
  - show_hn
metrics: {"points": 4, "comments": 2, "engagement_velocity": 4}
comments_count: 2
comments_total: 2
discovered_via: "hn:show_hn:3d"
---

# Show HN: Phyics-Based Dice Roller

> [!info] 一句话导读
> Dice — a free physics-based dice roller. Roll multiple dice at once and customize them.

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49900760>
> 指标：点赞=4 · 评论=2 · engagement_velocity=4
> 作者：swid　|　发布：2026-09-29T21:19:35Z
> 项目链接：<https://dice.jswidler.com/>
> 采集：2026-09-30T18:57:45+08:00　|　id：`7b207103d17a1005`

## 正文

Dice — a free physics-based dice roller. Roll multiple dice at once and customize them.
Tap to roll, or drag and flick to throw
Loading physics…
Settings
Settings
How many
−
 1
 +
Unique dice
Type
d4 — four-sided
 d6 — six-sided
 d8 — eight-sided
 d10 — ten-sided
 d12 — twelve-sided
 d20 — twenty-sided
Color
White
Result chip
Motion trails
Phone tilt
Sound
Tips
Tap, click or tap Space to roll.
Drag and flick to throw along your path.
Turn on Phone tilt to slide the dice by tilting your phone.

## 评论（2/2）

> **muti** · 2026-09-29T21:48:49.000Z　
> Have you analysed the fairness of the rolls? Just after a quick play around it doesn't look like there is enough energy in the throws that I would be confident it is.10,000 throws with small perturbations in the starting conditions should be distributed evenly across all sides of the die.Alternatively you could use RNG to generate a fair result, simulate the throw, and then set the sides of the die to produce the result from RNG. This is all academic though and I imagine anyone using the site won't be bothered.

---

> **swid** · 2026-09-29T21:56:00.000Z　
> There are tests, but I don't collect any real usage statistics to double check them... I could believe that if you pick up the dice and carefully throw it lightly, you can control the values more than intended, and this value would be somewhat correlated with the previous roll for quick enough rolls.I did think about changing the rotation speed of the dice before you throw, kind of speed it up and slow down. I first added the shuffling effect if you hold them; kind of a shell game animation. If I improve it more, occasionally giving some dice a swift spin would make it harder to defeat I think.Like you say, this is intended for people who are not going to cheat each other and just want to have fun, so I won't make it worse to account for it.I guess it works better on mobile with a swipe. I could change space to hold it a brief moment and throw it harder. Now that I am looking at it, that is probably what you mean.I think I want it to use physics in the end though, not map an RNG result at the end. You can see the faces and what you get is like a real die. If someone can beat it, maybe that is good for them.

## 导航

- 项目页：[[10-项目/dice.jswidler.com_8edbf151]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
