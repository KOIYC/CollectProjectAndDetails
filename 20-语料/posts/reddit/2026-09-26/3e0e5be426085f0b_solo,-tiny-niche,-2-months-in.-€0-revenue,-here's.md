---
type: "corpus"
item_id: "3e0e5be426085f0b"
title: "solo, tiny niche, 2 months in. €0 revenue, here's what I got wrong"
source: "reddit"
source_name: "Reddit 独立开发版块"
url: "https://www.reddit.com/r/microsaas/comments/1whggen/solo_tiny_niche_2_months_in_0_revenue_heres_what/"
author: "Quoliv"
published_at: "2026-09-16T07:28:29+08:00"
captured_at: "2026-09-26T09:42:53+08:00"
lang: "en"
kind: "post"
topic: 开发者工具
shard: "2026-09-26"
pub_day: "2026-09-16"
tags:
  - 语料
  - reddit
  - r/microsaas
metrics: {"score": 11, "comments": 26, "upvote_ratio": 0.92}
comments_count: 25
comments_total: 26
discovered_via: "reddit:14d+settle10"
---

# solo, tiny niche, 2 months in. €0 revenue, here's what I got wrong

> [!info] 一句话导读
> so I'm one guy, no audience, no funding. kept seeing people who want to learn investing and then bounce off every resource that assumes u already know what an e…

> [!meta]- 语料信息（点开展开）
> 来源：Reddit 独立开发版块（post）
> 原帖：<https://www.reddit.com/r/microsaas/comments/1whggen/solo_tiny_niche_2_months_in_0_revenue_heres_what/>
> 指标：得分=11 · 评论=26 · 赞踩比=0.92
> 作者：Quoliv　|　发布：2026-09-16T07:28:29+08:00
> 项目链接：—
> 采集：2026-09-26T09:42:53+08:00　|　id：`3e0e5be426085f0b`

## 正文

so I'm one guy, no audience, no funding. kept seeing people who want to learn investing and then bounce off every resource that assumes u already know what an etf is. so I built an app for it. short lessons on how stocks and finance actually work, plus a practice mode.

stack is boring on purpose. vercel, supabase, revenuecat, posthog, finnhub for prices. nothing clever.

revenue: 0. not being cute about it, thats just what it is. a few installs, nobody paying.

stuff I got wrong:

built for 2 months before showing anyone. still 2 months of guessing.

thought launching = people finding it. it doesnt work like that at all.

my onboarding makes u finish 5 intro lessons before anything unlocks. pretty sure thats where people quit, watching the numbers to see.

what did u do to get ur first 10 paying users? feels way harder on consumer than b2b.

## 评论（25/26）

> **Quoliv**（5 分） · 2026-09-16T07:28:46+08:00　
> site's name is [quoliv.com](http://quoliv.com) if people are interested

---

> **West_Inevitable_2281**（2 分） · 2026-09-16T07:50:12+08:00　
> Before looking for the first 10 paying users, I would separate discovery from activation. With only a few installs and five required lessons before anything unlocks, you do not yet know whether people reject the product or just the gate. What percentage finishes the first lesson and reaches practice mode?

---

> **QuanTradin**（1 分） · 2026-09-16T08:33:18+08:00　
> your instinct about the onboarding gate is right, and i'd stop watching the numbers and just rip it out. five lessons before anything unlocks is asking for a commitment the size of a purchase before anyone has seen the thing they actually came for. put practice mode on the first screen.
>
> the harder bit, given the two months: lessons on how stocks work compete with free youtube, so the thing people pay for usually isnt the teaching, its the feedback on their own decisions. practice mode is probably your real product and its currently buried behind the part that looks like homework.

---

> **Connect_Tip_6469**（1 分） · 2026-09-16T08:37:46+08:00　
> the 5 lessons before anything unlocks is the whole post honestly. your user bounces off investopedia because it feels like homework, so you opened by assigning homework. thats not a churn problem, they never started. and b2b isnt easier, its just a guy who ignores your emails on purpose instead of by accident

---

> **Far_Body5596**（1 分） · 2026-09-16T08:56:06+08:00　
> nice, was curious what the landing page looked like

---

> **ai_ztn**（1 分） · 2026-09-16T09:49:49+08:00　
> The five-lesson gate is the loudest smell. You're asking people to do homework before they feel anything, and with that setup you can't tell bad product from never reached the useful action. Installs with locked practice mode mostly measure patience.
>
> I'd run one ugly experiment this week: unlock practice mode immediately (or after one 60 second taste), keep the lessons optional, and compare how many hit practice, how many come back day 2, and whether anyone pays at all. Free YouTube already teaches what an ETF is anyway. Paid usually sticks when it's feedback on their situation, not another intro curriculum.
>
> First 10 paying users almost never come from "I launched." They come from watching 20 people try the first useful action and iterating on that moment. Skip polishing onboarding until that action is proven.

---

> **PopKoren**（1 分） · 2026-09-16T14:36:35+08:00　
> Unlocking practice earlier so you can tell product pain from homework drop-off is the right experiment on a Vercel plus Supabase stack. While you rerun that funnel, it is worth a stranger pass on the live app across auth, APIs, storage, and DB rules including those Supabase/Postgres policies. [https://rowly.me](https://rowly.me) covers that full external surface on vibe-coded micro SaaS.

---

> **HonestFeedbackTime**（1 分） · 2026-09-16T14:36:35+08:00　
> This is important OP.

---

> **devhisaria**（2 分） · 2026-09-16T14:47:03+08:00　
> Been there, my first consumer app had a 4-step signup and I killed it to one tap, activation doubled in a week. rip the gate out first, then worry about the €0.

---

> **No-Sandwich4826**（2 分） · 2026-09-16T15:43:46+08:00　
> The installs you've already got came from somewhere, and the post doesn't say where. I'd chase those down before settling on the silent build as the main mistake. Might turn out to be one referral you can't repeat.

---

> **Khavel_dev**（1 分） · 2026-09-16T16:24:21+08:00　
> Consumer is way harder than B2B because there's no single watering hole where your buyer hangs out complaining about the problem. In B2B you find the subreddit or Slack where people vent, drop value, repeat. Consumer finance education though, your people are scattered across YouTube comments and TikTok investing threads and they're not searching for a tool.
>
> The 5-lesson gate is probably hurting more than the distribution. Let people touch the practice mode immediately and gate the advanced stuff behind the lesson sequence. People who try the fun part first are more likely to circle back and actually do the onboarding.
>
> For the first 10, what worked for me: find 3-4 threads per week where someone is asking the exact question your product answers, and drop a genuinely helpful answer with no link. After a few weeks people start clicking your profile. It is slow but it compounds.

---

> **Quoliv**（1 分） · 2026-09-16T18:46:59+08:00　
> very low , i think thats the main issue

---

> **Quoliv**（1 分） · 2026-09-16T18:47:36+08:00　
> this is very useful insight thank you!

---

> **Quoliv**（1 分） · 2026-09-16T18:47:58+08:00　
> yes now that i think about it u are right, i personally wouldnt want to use an app like that now

---

> **Quoliv**（1 分） · 2026-09-16T18:48:37+08:00　
> the installs were mostly from tiktok posts i made

---

> **Quoliv**（1 分） · 2026-09-16T18:48:57+08:00　
> yes as the other people mentioned also i will remove that , i was very blind to it

---

> **West_Inevitable_2281**（1 分） · 2026-09-16T18:51:32+08:00　
> That changes the priority. You have a live activation problem before a distribution problem. I have a few thoughts, but they require looking at the onboarding, positioning, and what you measure together. Send me a chat if you want to dig into it privately.

---

> **Quoliv**（1 分） · 2026-09-16T18:52:11+08:00　
> Yes the 5-lesson thing is the main issue , thanks for pointing it out. I'll try to find some threads each week related to the app im building. Thank you very much for the feedback

---

> **QuanTradin**（1 分） · 2026-09-16T21:07:40+08:00　
> Then you already know the first ship. Put practice mode on screen one and let the lessons be optional, because the person who tries a trade will come back for the explanation on their own.

---

> **stevecam27**（1 分） · 2026-09-16T21:18:11+08:00　
> What makes this stack boring. Seems like OOB slop stack?

---

> **Deepak-AvairAI**（1 分） · 2026-09-17T00:20:35+08:00　
> B2B concentrates the pain in one place, a subreddit or Slack channel, versus scattered TikTok comments. Easier discovery, not necessarily an easier sale. Once the onboarding gate's fixed, the real test is whether anyone outside the free crowd pays for finance basics at all.

---

> **RevolutionCivil8049**（1 分） · 2026-09-17T04:54:53+08:00　
> youve got posthog in the stack and say you're watching where people quit, but with a few installs thats like 3 people bouncing for 3 different reasons, not a dropoff. how many installs is a few?

---

> **Outrageous_Knee_7506**（1 分） · 2026-09-17T05:30:57+08:00　
> launching ≠ distribution is the hardest lesson. for consumer stuff id focus on organic search since people literally google "how do stocks work" every day. building backlinks early is like buying internet real estate before anyone else notices the neighborhood. look into Outrank for that side of things, then spend your actual time fixing the onboarding and talking to users

---

> **Quoliv**（0 分） · 2026-09-17T06:52:56+08:00　
> like 4 :/

---

> **Quoliv**（0 分） · 2026-09-17T06:56:40+08:00　
> thanks for the info, ill make sure to add that!

## 导航

- 项目页：—（本条不是项目，按设计不建实体页）
- 渠道页：[[50-渠道/reddit]]
- 赛道：`开发者工具`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
