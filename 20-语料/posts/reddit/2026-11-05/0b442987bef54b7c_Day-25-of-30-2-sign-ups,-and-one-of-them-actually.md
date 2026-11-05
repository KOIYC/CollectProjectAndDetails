---
type: "corpus"
item_id: "0b442987bef54b7c"
title: "Day 25 of 30: 2 sign-ups, and one of them actually set it up"
source: "reddit"
source_name: "Reddit 独立开发版块"
url: "https://www.reddit.com/r/microsaas/comments/1xf9tkt/day_25_of_30_2_signups_and_one_of_them_actually/"
author: "Southern_Kitchen3426"
published_at: "2026-10-26T02:26:56+08:00"
captured_at: "2026-11-05T11:22:40+08:00"
lang: "en"
kind: "post"
topic: 开发者工具
shard: "2026-11-05"
pub_day: "2026-10-26"
tags:
  - 语料
  - reddit
  - r/microsaas
metrics: {"score": 7, "comments": 16, "upvote_ratio": 1}
comments_count: 14
comments_total: 16
discovered_via: "reddit:14d+settle10"
---

# Day 25 of 30: 2 sign-ups, and one of them actually set it up

> [!info] 一句话导读
> Day 25 of trying to get my first 10 paying customers for AskVerb, in public.

> [!meta]- 语料信息（点开展开）
> 来源：Reddit 独立开发版块（post）
> 原帖：<https://www.reddit.com/r/microsaas/comments/1xf9tkt/day_25_of_30_2_signups_and_one_of_them_actually/>
> 指标：得分=7 · 评论=16 · 赞踩比=1
> 作者：Southern_Kitchen3426　|　发布：2026-10-26T02:26:56+08:00
> 项目链接：—
> 采集：2026-11-05T11:22:40+08:00　|　id：`0b442987bef54b7c`

## 正文

Day 25 of trying to get my first 10 paying customers for AskVerb, in public.

Two new sign-ups today. And one of them did something that almost never happens: they set up their site and tested it in development. Not live on their product yet, but they went past signing up and actually tried it. After everything people told me about why sign-ups stall, that one test means a lot.

I was out most of the day, touching grass and spending time with family after the pitch day. I think I needed it.

Back tomorrow for day 26.

If you've tried a tool in a test setup and then never moved it to production, what was the thing that stopped you?

## 评论（14/16）

> **jeremdesign**（2 分） · 2026-10-26T04:09:17+08:00　
> For me it usually stalls at the last step, because I don't want to break the live version that's already working. I end up leaving the test setup running and telling myself I'll switch it over later, then I just don't. That one test you got is a good sign, don't lose it by waiting for a perfect moment to go live.

---

> **Southern_Kitchen3426**（1 分） · 2026-10-26T04:12:36+08:00　
> Yeah your right that is the moment people stall and the "don't touch when the code is working" is a untold rule gotta find a way to help it make it to prod 😅

---

> **MobileXapps**（2 分） · 2026-10-26T04:58:30+08:00　
> That last step is the real wall. People are fine testing in development, then scared the script will break their live product. Two things usually help: let them turn it on for themselves only first, behind a query parameter or an admin login, so it's live on their real site but invisible to customers. And show a one-click way to turn it off, right in the dashboard. Knowing they can undo it in 5 seconds removes most of the fear.
>
> The person who set it up in dev is worth a quick call now. Ask what would make them comfortable pushing it live, they'll tell you exactly what your onboarding is missing.

---

> **Ctbhatia**（2 分） · 2026-10-26T05:15:33+08:00　
> what does going live cost them, a config swap or redoing the setup against real data? the dev test proves the flow, not the migration

---

> **Competitive_Tune_590**（1 分） · 2026-10-26T11:41:13+08:00　
> day 25 chasing those first ten, good to see one signup go past the form. i use replyhey myself, it scans reddit for relevant buyer talk, checks sub rules so you don't get banned, and pre-drafts replies. might save you some scrolling, ymmv. https://replyhey.com

---

> **Entire-Sound7074**（1 分） · 2026-10-26T15:51:07+08:00　
> fue más allá del registro" = probó el modo dev y no lo puso en producción. o sea, sigue siendo cero clientes.

---

> **vladzoff**（2 分） · 2026-10-26T21:56:46+08:00　
> I'd check whether the person who tested it can actually change the live site. A dev test can go well, but publishing a snippet may require a different owner, a review, or approval. The useful question isn't only “what made you hesitate?” but “who has to say yes before this can go live?” That separates onboarding friction from a permission or ownership blocker.

---

> **Southern_Kitchen3426**（2 分） · 2026-10-26T22:01:33+08:00　
> The person who tested it might not even be the one who can touch the live site. I'm asking that one today: who has to say yes before it goes live.

---

> **Southern_Kitchen3426**（1 分） · 2026-10-26T22:01:44+08:00　
> Both of those are going on the list. The off switch part already exists, archiving a site turns it off instantly and you can bring it back, but I clearly don't show it early enough. A way to see it on your real site before customers do is the one I don't have yet, and I think it's the fix for exactly this. And yes, messaging the dev tester today.

---

> **Southern_Kitchen3426**（1 分） · 2026-10-26T22:02:00+08:00　
> Fair distinction. For AskVerb it should be a key swap: a live site with its own key for the real domain, and the same snippet. Whether it feels like that to them is what I need to find out, because a test proving the flow is exactly where they stopped.

---

> **Southern_Kitchen3426**（1 分） · 2026-10-26T22:02:10+08:00　
> **Tienes razón, siguen siendo cero clientes de pago. Lo cuento igual porque un test en dev es lo más lejos que alguien ha llegado, y quiero entender qué lo frena antes de producción.**

---

> **Ctbhatia**（1 分） · 2026-10-26T23:35:36+08:00　
> the swap is worth instrumenting, since a key tied to the real domain only proves itself on the first request from it, so log which domain each key has actually seen before counting anyone as live. a www and an apex are the pair that slips through setup and still fails the call

---

> **Helen_Firebrand**（1 分） · 2026-10-27T00:57:51+08:00　
> Anything that involves code on their site or product AND also captures potentially sensitive customer data is going to give people the jitters.
>
> Can you beef up your security / privacy proof?
>
> These would be my first concerns if I was responsible for a product big enough for AskVerb to add value. (Granted, I am just one smol human).

---

> **AndrewHahaCO2**（1 分） · 2026-10-27T14:04:58+08:00　
> for me it's usually rollback. If I can't remove the script in 30 seconds when something gets weird, the dev test stays a dev test.

## 导航

- 项目页：—（本条不是项目，按设计不建实体页）
- 渠道页：[[50-渠道/reddit]]
- 赛道：`开发者工具`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
