---
type: "corpus"
item_id: "48f2355b1a12d198"
title: "Thought nobody was using my product… turns out 2 people actually are"
source: "reddit"
source_name: "Reddit 独立开发版块"
url: "https://www.reddit.com/r/microsaas/comments/1szz1zq/thought_nobody_was_using_my_product_turns_out_2/"
author: "CriticalBad4853"
published_at: "2026-04-30T23:16:35+08:00"
captured_at: "2026-09-21T03:00:15+08:00"
lang: "en"
kind: "post"
topic: "开发者工具"
shard: "2026-09-21"
pub_day: "2026-04-30"
tags:
  - 语料
  - reddit
  - r/microsaas
metrics: {"score": 3, "comments": 3, "upvote_ratio": 1}
comments_count: 6
comments_total: 6
discovered_via: "reddit:174d+settle3"
---

# Thought nobody was using my product… turns out 2 people actually are

> [!info] 一句话导读
> Been deep in the weeds polishing my public API & SDK lately.

> [!meta]- 语料信息（点开展开）
> 来源：Reddit 独立开发版块（post）
> 原帖：<https://www.reddit.com/r/microsaas/comments/1szz1zq/thought_nobody_was_using_my_product_turns_out_2/>
> 指标：得分=3 · 评论=3 · 赞踩比=1
> 作者：CriticalBad4853　|　发布：2026-04-30T23:16:35+08:00
> 项目链接：—
> 采集：2026-09-21T03:00:15+08:00　|　id：`48f2355b1a12d198`

## 正文

Been deep in the weeds polishing my public API & SDK lately.

The best way to test an API is to actually build something with it — so I spun up a small app on top of my own API.

Immediately found bugs I would’ve never caught with normal testing.

One big improvement:
switched post sending from sync → async + retries
→ success rate went up a lot

Added an extra validation layer too — some platforms are now getting more than 90% success.

Real talk:
I’ve been questioning if anyone is actually using this. Couldn’t even sleep last night thinking about it. Then this morning — got a support email asking about free plan quota reset.

Checked logs:
2 users have been actively sending posts via the API these past few days

They’re on the free plan, but honestly… that made my day.

At least it means this isn’t trash — someone actually needs it.

UniPost currently has a pretty generous free plan.

If you’re building something around social posting APIs, would love your feedback

More platforms are in review and coming soon.

unipost(dot)dev

https://reddit.com/link/1szz1zq/video/8cd36wykgcyg1/player

## 评论（6/6）

> **lowFPSEnjoyr**（1 分） · 2026-04-30T23:32:02+08:00　
> that feeling is way too relatable those first real users hit different even if it is just a couple people.
>
> honestly that is probably the best signal you can get right now especialy since they are actively usin it not just signing up and disappearing. i would try to talk to them if you can because they are basically showin you what actually matters in the product.
>
> also buildin on top of your own api is underrated you always find the real issues that way not the theoretical ones

---

> **deepakmardi**（1 分） · 2026-05-01T01:48:10+08:00　
> Only up and above

---

> **Zealousideal_Set2016**（1 分） · 2026-05-01T23:42:08+08:00　
> two active users on a free plan is still validation, don't dismiss that. the fact that someone emailed you about quota resets means they actually care about using it. biggest thing i'd say is talk to those two people directly, like get on a call if you can.
>
> figure out what their workflow looks like and what they'd pay for. i spent months building in isolation before i started doing that through PopHatch and it completley shifted how i prioritized stuff. pophatch.com.

---

> **CriticalBad4853**（1 分） · 2026-05-05T01:26:43+08:00　
> Yeah exactly — it hits way harder than I expected. I was mentally preparing for *zero* usage, so even just seeing a couple people consistently using it feels huge.
>
> And 100% agree — the fact that they’re actually sending posts (not just signing up) feels like a much stronger signal. I’m trying to figure out the best way to reach out without being annoying, but I’d love to understand what they’re actually trying to build.
>
> Also +1 on building on top of your own API — I thought things were “pretty solid” until I actually tried using it like a real user… instantly exposed a bunch of stuff I overlooked.
>
> Appreciate this — super helpful perspective

---

> **CriticalBad4853**（1 分） · 2026-05-05T01:27:17+08:00　
> **haha yeah, slow but steady**

---

> **CriticalBad4853**（1 分） · 2026-05-05T01:29:05+08:00　
> Yeah that’s a really good point — the quota email made it feel way more real. I’ve been mostly building in isolation, so I’m probably missing a lot by not talking to them directly. Definitely going to try reaching out and understand their workflow better.
>
> Out of curiosity, what changed the most for you after you started doing that?

## 关联链接

- https://reddit.com/link/1szz1zq/video/8cd36wykgcyg1/player

## 导航

- 项目页：—（本条不是项目，按设计不建实体页）
- 渠道页：[[50-渠道/reddit]]
- 赛道：`开发者工具`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
