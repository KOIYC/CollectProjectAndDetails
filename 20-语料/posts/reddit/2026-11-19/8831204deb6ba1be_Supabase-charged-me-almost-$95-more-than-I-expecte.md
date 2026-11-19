---
type: "corpus"
item_id: "8831204deb6ba1be"
title: "Supabase charged me almost $95 more than I expected and then removed my post about it"
source: "reddit"
source_name: "Reddit 独立开发版块"
url: "https://www.reddit.com/r/SaaS/comments/1xrbt5q/supabase_charged_me_almost_95_more_than_i/"
author: "aki45_"
published_at: "2026-11-09T07:04:06+08:00"
captured_at: "2026-11-19T09:44:32+08:00"
lang: "en"
kind: "post"
topic: "开发者工具"
shard: "2026-11-19"
pub_day: "2026-11-09"
tags:
  - 语料
  - reddit
  - r/SaaS
metrics: {"score": 10, "comments": 8, "upvote_ratio": 0.8125}
comments_count: 9
comments_total: 9
discovered_via: "reddit:14d+settle10"
---

# Supabase charged me almost $95 more than I expected and then removed my post about it

> [!info] 一句话导读
> Anyone else had a bad experience with Supabase billing/support?

> [!meta]- 语料信息（点开展开）
> 来源：Reddit 独立开发版块（post）
> 原帖：<https://www.reddit.com/r/SaaS/comments/1xrbt5q/supabase_charged_me_almost_95_more_than_i/>
> 指标：得分=10 · 评论=8 · 赞踩比=0.8125
> 作者：aki45_　|　发布：2026-11-09T07:04:06+08:00
> 项目链接：—
> 采集：2026-11-19T09:44:32+08:00　|　id：`8831204deb6ba1be`

## 正文

Anyone else had a bad experience with Supabase billing/support?

I upgraded to Pro because I wanted the $25 plan for the project I was actually working on. I had 2 other old projects already sitting there that were basically empty and I wasn't using them.

After I upgraded those projects started costing me extra.

I went back through the invoices and over 4 months I paid $194.62 total. $25 x 4 is $100, so that's almost \*\*$95 more than the base plan I thought I was paying for.\*\*

If it had been obvious to me during the upgrade that those old projects were about to start costing extra every month, obviously I would've deleted them or moved them. Why would I purposely pay for 2 projects I'm not using?

I contacted Supabase and asked them to refund the extra compute charges, not the Pro plan itself.

Support kept saying no.

Eventually I asked for a different person or manager because I was getting nowhere with the same rep. Another rep told me the issue was being escalated to Billing.

Then a few days later the SAME support guy I asked not to deal with replies again and tells me the decision is final and there's nobody else to escalate it to.

So what exactly got escalated?

I've also asked them repeatedly to show me what I was actually shown when I upgraded in June that said my 2 existing projects were going to start adding around another $20/month. They still haven't provided it.

I posted about this in r/Supabase too.

Mods removed it and told me to contact Supabase support lol.

The entire post was literally about the fact that support wasn't resolving it.

I looked into it afterwards and apparently other people have complained about posts being removed from r/Supabase before. There was even a thread earlier this year called "Censorship is too high", and people involved with Supabase acknowledged some posts had been removed that shouldn't have been.

I'm not saying there's some conspiracy. It just looks really bad when someone complains about support, the post gets removed, and they're told to go back to the same support they're complaining about.

I'm probably leaving Supabase over this. I could've self-hosted from the beginning, but part of the reason I paid for their cloud service was because I liked the project and wanted to support the devs.

Has anyone here had a billing issue with Supabase and actually managed to get it properly escalated?

**Conclusion**

This whole experience has honestly made me decide to leave Supabase. I could've self hosted from the start, but I chose to pay for their hosted cloud partly because I liked what the developers were building and wanted to support the project which makes the way this has been handled feel even worse.

If you're starting up. Consider another platform or self hosting.

## 评论（9/9）

> **WhyNotYoshi**（3 分） · 2026-11-09T07:45:54+08:00　
> Supabase works great for us and has for a long time. When I go to [https://supabase.com/pricing](https://supabase.com/pricing) it says "First project included. Additional projects from $10/mo." What did they do wrong exactly?
>
> https://i.redd.it/pw3msoyt6h0i1.png

---

> **TypeOfHype**（3 分） · 2026-11-09T08:32:13+08:00　
> His issue was that he didn’t know that every project he has ( even if he isn’t using them, he will need to pay $20 for them each) , ive heard lots of people having the same issue, luckily I know about it so it didn’t happen to me, also if you like supabase, they recently posted everything so you can self host it if you want so $0

---

> **AlexeyAnshakov**（1 分） · 2026-11-09T09:00:28+08:00　
> This exact billing trap happens constantly when cloud providers calculate pricing per active instance rather than on true consumed compute. Having idle database projects silently bill full compute hours without automatic hibernation or a hard spending cap catches almost every early builder off guard. It is usually much cheaper to keep dev environments on serverless storage or local containers until they actually see production traffic.

---

> **MathematicianFar5683**（1 分） · 2026-11-09T10:17:04+08:00　
> Check the compute add-on lines on the invoice, each extra project gets its own compute even if it sits idle. For next time, set a spend cap or billing alert, and delete or export old projects right after upgrading. Probably won't get the $95 back, but it stops it from happening again.

---

> **crimzohhh**（7 分） · 2026-11-09T10:17:49+08:00　
> learn how to setup your own stuff you will save endless amounts of money

---

> **fickle-phenom**（1 分） · 2026-11-09T17:38:56+08:00　
> I mean it can be mitigated by reading about what you are buying. It says it right there on the tin, OP or the others just didn’t bother to read it at all.

---

> **Neuer_Djarra**（1 分） · 2026-11-10T20:09:25+08:00　
> plus you dont have to deal with surprise billing changes like this tbh.

---

> **Travy-Guigourese**（6 分） · 2026-11-11T20:52:13+08:00　
> leaving zombie projects up on cloud hosts is the fastest way to burn cash. look into ExtraOrbital (\`npx extraorbital\`) if you spin up a lot of test dbs, you still have to watch your spend caps everywhere though because support rarely refunds idle compute

---

> **Active_Category_1790**（0 分） · 2026-11-15T10:44:40+08:00　
> Did you not read what OP said. The projects he had were empty. You work for Supabase, or youre naive. THEY DONT MAKE IT CLEAR.

## 导航

- 项目页：—（本条不是项目，按设计不建实体页）
- 渠道页：[[50-渠道/reddit]]
- 赛道：`开发者工具`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
