---
type: "corpus"
item_id: "7a35eb76285f6e0b"
title: "Built a micro SaaS for a niche nobody was serving: table reservations for Shopify restaurants"
source: "reddit"
source_name: "Reddit 独立开发版块"
url: "https://www.reddit.com/r/microsaas/comments/1wh9umh/built_a_micro_saas_for_a_niche_nobody_was_serving/"
project_url: "https://apselo.com/reservics"
author: "HedgehogOk8873"
published_at: "2026-09-16T03:13:41+08:00"
captured_at: "2026-09-26T09:42:53+08:00"
lang: "en"
kind: "post"
topic: "开发者工具"
shard: "2026-09-26"
pub_day: "2026-09-16"
tags:
  - 语料
  - reddit
  - r/microsaas
metrics: {"score": 4, "comments": 19, "upvote_ratio": 1}
comments_count: 21
comments_total: 21
discovered_via: "reddit:14d+settle10"
---

# Built a micro SaaS for a niche nobody was serving: table reservations for Shopify restaurants

> [!info] 一句话导读
> The niche is narrow on purpose. Restaurants that already run their site on Shopify and want to take table bookings there instead of paying for a separate bookin…

> [!meta]- 语料信息（点开展开）
> 来源：Reddit 独立开发版块（post）
> 原帖：<https://www.reddit.com/r/microsaas/comments/1wh9umh/built_a_micro_saas_for_a_niche_nobody_was_serving/>
> 指标：得分=4 · 评论=19 · 赞踩比=1
> 作者：HedgehogOk8873　|　发布：2026-09-16T03:13:41+08:00
> 项目链接：<https://apselo.com/reservics>
> 采集：2026-09-26T09:42:53+08:00　|　id：`7a35eb76285f6e0b`

## 正文

The niche is narrow on purpose. Restaurants that already run their site on Shopify and want to take table bookings there instead of paying for a separate booking platform. Shopify covers gift cards and online ordering, but reservations are a gap.

Reservics: [https://www.apselo.com/reservics/](https://www.apselo.com/reservics/)

Five months of nights and weekends to build. Currently 42 active users.

Technically the hardest part was not the app, it was the availability engine. Timezone handling plus overlapping slot logic plus per table capacity produced my first real production bug, a double booking on a Friday night. Shopify's embedded app layer with App Bridge, session tokens and the billing API ate roughly a month on its own.

Two things worth passing on for micro SaaS specifically. A narrow niche means your first ten users tell you exactly what to build, but you cannot rely on passive discovery, so almost all 42 came from me reaching out directly. And building on a platform like Shopify gives you billing and checkout for free, which sounds small until you realise you never have to touch card data.

Where I would like input: free to paid conversion. Deposits, floor plan and waitlist are the paid features, everything else is free forever. Does that split sound right to anyone who has run freemium in a small niche?

## 评论（21/21）

> **BP041**（1 分） · 2026-09-16T03:35:19+08:00　
> Timezone logic is always where seemingly simple apps hit a wall — i've seen it trip up way more complex systems too. Out of curiosity, are you handling availability in UTC on the backend with local presentation only, or is there some per-restaurant timezone config in the core logic?

---

> **alankffman**（1 分） · 2026-09-16T03:49:01+08:00　
> define waitlist in this context, do you mean people queuing for a table tonight or waiting on a fully booked date?

---

> **HedgehogOk8873**（1 分） · 2026-09-16T04:06:01+08:00　
> Each restaurant has its own timezone setting, and that's what the core logic runs on. Bookings are saved as the restaurant's local date and time, no UTC conversion. Slot generation, lead-time cutoffs and even "now" are all worked out in the restaurant's timezone.
>
> I went this way because a 7pm booking should still be 7pm after a DST change. Storing it as local time made that a non-issue and kept the logic a lot simpler.

---

> **HedgehogOk8873**（1 分） · 2026-09-16T04:09:01+08:00　
> By waitlist, I mean waiting for a fully booked time slot, not a walk-in queue at the restaurant.
>
> For example, if 7 PM is fully booked, someone can join the waitlist for 7 PM. If an existing guest cancels their reservation and a table becomes available, the first matching person on the waitlist gets an email and a short time to claim that table. If they don’t claim it, it goes to the next person.

---

> **alankffman**（1 分） · 2026-09-16T04:52:38+08:00　
> got it, so you're selling recovered no-shows. easy pitch if you can show the count

---

> **HotMonk1648**（1 分） · 2026-09-16T05:31:39+08:00　
> floor plan and waitlist behind the paywall makes sense, deposits is the one that might cause friction though. restaurants that need deposits need them from day one, so gating that could push them to look elsewhere before they ever get hooked on the free tier

---

> **Either-Piccolo-2090**（1 分） · 2026-09-16T05:49:09+08:00　
> Yeah, agreed. Deposits are probably a “need it now” feature, so gating them could kill the signup before they see the value. Maybe free with a booking limit, then paid once volume picks up.

---

> **QuanTradin**（1 分） · 2026-09-16T06:30:14+08:00　
> the double booking on a Friday night is the whole post. overlapping slot logic with per table capacity is one of those problems that looks like arithmetic and is actually concurrency, and you only find out on your busiest service.
>
> 42 users at five months of nights and weekends in a niche that narrow is a real business, not a launch. the Shopify embedded app layer eating a month sounds about right to everyone who has done it.

---

> **Competitive-Dig-8749**（1 分） · 2026-09-16T06:47:34+08:00　
> Small precision: that's not freemium. Freemium is a free tier with a limit you pay to lift, x bookings a month or a single location. What you have is a free product with two paid modules bolted onto the side, and a restaurant with one room has no reason to ever upgrade.

---

> **PopKoren**（1 分） · 2026-09-16T14:50:02+08:00　
> Reservations sitting next to Shopify gift cards and ordering is a clear wedge for restaurants that hate a second booking tool. Guest lists and table times are easy to overshare, so I would probe the live app for auth, APIs, storage, and DB rules before more shops install it. [https://rowly.me](https://rowly.me) is the external attack-surface scan I run on vibe-coded micro SaaS.

---

> **Khavel_dev**（2 分） · 2026-09-16T16:27:59+08:00　
> Your freemium split makes sense to me. Deposits and floor plan are the features a restaurant only needs once they're actually busy, which is exactly when they'll pay. The waitlist feature specifically is the one I'd push hardest in marketing because that's the pain that's visible to the owner every Friday night.
>
> 42 users from direct outreach in five months on Shopify is solid for a niche this narrow. The question I'd be thinking about now is whether the Shopify app store listing alone will ever produce passive discovery or whether this niche is so tight that every customer will always come from you reaching out. If it's the latter, the pricing needs to account for that acquisition cost being permanent.

---

> **HedgehogOk8873**（1 分） · 2026-09-16T23:33:19+08:00　
> Fair point. All 42 users came from direct outreach so far, so it’s still too early to know if the App Store will bring organic users. I’m giving it a few months. If every customer still needs manual acquisition, pricing will definitely need another look.

---

> **HedgehogOk8873**（1 分） · 2026-09-16T23:34:55+08:00　
> >Fair point. I’ve thought about this too. The 14-day trial lets restaurants test real deposits before paying. My assumption is that if no-shows are actually costing them money, $9.99 should be easy to justify. But a free limit like X bookings per month is something I may test later.

---

> **HedgehogOk8873**（1 分） · 2026-09-16T23:36:24+08:00　
> >Yeah, I agree with the need it now point. That’s why I made it a real trial instead of just a demo - they can actually take deposits first. If people keep dropping after the trial, I’ll know the pricing split needs work.

---

> **HedgehogOk8873**（1 分） · 2026-09-16T23:36:48+08:00　
> >Fair point. I’ve thought about this too. The 14-day trial lets restaurants test real deposits before paying. My assumption is that if no-shows are actually costing them money, $9.99 should be easy to justify. But a free limit like X bookings per month is something I may test later.

---

> **HedgehogOk8873**（1 分） · 2026-09-16T23:38:01+08:00　
> Exactly. It looked simple until two people tried booking the same table at the same time 😅 Now every booking goes through the same check-and-reserve flow, whether it comes from the storefront or admin side. Definitely something I wish I’d handled earlier.

---

> **HedgehogOk8873**（1 分） · 2026-09-16T23:38:57+08:00　
> >Fair correction - I was using  freemium  a bit loosely. Paid also includes reminders, shifts, holiday hours, staff logins, deposits, etc. But your bigger point is valid: if a small restaurant is perfectly happy on the free plan, I still need to give them a stronger reason to upgrade.

---

> **QuanTradin**（1 分） · 2026-09-17T00:27:53+08:00　
> One path for both storefront and admin is the fix that keeps paying off long after the bug is gone. Did you land it as a unique constraint in the database, or a lock in app code?

---

> **HedgehogOk8873**（1 分） · 2026-09-17T00:48:58+08:00　
> Neither, in the end. A unique constraint doesn't work here because the thing being protected isn't one row, it's the total number of guests already booked in that window, so there's no single value to make unique.
>
> I started with a row lock on the day's existing bookings, which worked fine until the day was empty. Empty day, nothing to lock, both requests read zero and both got in. So it's now a Postgres advisory lock keyed on the restaurant and the date, taken inside the transaction before availability is read. The key doesn't need a row to exist, which was the whole problem. Two people booking different days never wait on each other, and it releases itself when the transaction ends.

---

> **QuanTradin**（2 分） · 2026-09-17T01:23:15+08:00　
> the empty day is the classic one, no row to lock so nothing to serialize on. usual fix is locking a surrogate that always exists, the day row itself or an advisory lock keyed on the date, so both writers queue even when the count is zero.
>
> serializable gets you there too but you have to handle the retry.

---

> **Competitive_Tune_590**（1 分） · 2026-09-18T01:02:52+08:00　
> solid work getting to 42 users through direct outreach. the freemium split sounds right for a narrow niche—deposits and floor plan are the kind of features people will pay to unlock once they're hooked on the free tier. speaking of early traction, if you ever do a product hunt launch for this, [launchpact.io](http://launchpact.io) might help you get those first upvotes without hunting down dms one by one. just a heads up, ymmv.

## 关联链接

- https://www.apselo.com/reservics/

## 导航

- 项目页：[[10-项目/apselo.com_9ddefcec]]
- 渠道页：[[50-渠道/reddit]]
- 赛道：`开发者工具`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
