---
type: "corpus"
item_id: "87055c22b052dd55"
title: "No $10k MRR story. I built software for a really boring problem instead."
source: "reddit"
source_name: "Reddit 独立开发版块"
url: "https://www.reddit.com/r/microsaas/comments/1wi8n62/no_10k_mrr_story_i_built_software_for_a_really/"
project_url: "https://sopai.systems/"
author: "Ill-Efficiency4579"
published_at: "2026-09-17T04:21:21+08:00"
captured_at: "2026-09-25T00:18:19+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-21"
pub_day: "2026-09-17"
tags:
  - 语料
  - reddit
  - r/microsaas
metrics: {"score": 3, "comments": 9, "upvote_ratio": 0.72}
comments_count: 8
comments_total: 9
discovered_via: "reddit:7d+settle3"
---

# No $10k MRR story. I built software for a really boring problem instead.

> [!info] 一句话导读
> I’ve seen a lot of “$X in 30 days” posts lately, so I figured I’d share the complete opposite.

> [!meta]- 语料信息（点开展开）
> 来源：Reddit 独立开发版块（post）
> 原帖：<https://www.reddit.com/r/microsaas/comments/1wi8n62/no_10k_mrr_story_i_built_software_for_a_really/>
> 指标：得分=3 · 评论=9 · 赞踩比=0.72
> 作者：Ill-Efficiency4579　|　发布：2026-09-17T04:21:21+08:00
> 项目链接：<https://sopai.systems/>
> 采集：2026-09-25T00:18:19+08:00　|　id：`87055c22b052dd55`

## 正文

I’ve seen a lot of “$X in 30 days” posts lately, so I figured I’d share the complete opposite.

No big revenue number. No “we hit $10k MRR.” I don’t even have paying customers yet.

Just the story of how I accidentally ended up building a Micro SaaS for one of the least exciting B2B problems imaginable.

It started with a client of my automation studio.

They run a commercial cleaning company with around 50 employees, and they had a pretty frustrating problem: their bigger corporate clients were starting to require more and more safety/compliance documentation before renewing contracts.

Their way of managing employee certifications?

A shared spreadsheet.

And, as you can probably guess, nobody was checking it consistantly.

Certificates would expire, nobody would notice, and then suddenly an audit would come around and they’d be scrambling to figure out who was missing what.

So I built them something pretty simple.

An employee gets a new certificate → they take a photo of it or forward the certificate email → AI/OCR reads it → the expiration date gets logged automatically → management gets reminded at 90, 60, and 30 days before it expires.

Nothing revolutionary.

It just solved a problem that was actually costing them time and potentially putting contracts at risk.

Then I started thinking...

If one cleaning company has this problem, how many other businesses are dealing with the exact same thing?

That’s what eventually turned the project into SopAI.

We’re currently live with the first company on a free trial. So, to be completely transparent, $0 in revenue so far.

But honestly, i'm okay with that.

I’d rather have one real business using something I built to solve a real problem than make up a revenue milestone for a Twitter/X post.

The more I’ve looked into it, the more I’ve realized this isn’t really a “cleaning company” problem.

Construction, HVAC, janitorial, logistics, and a bunch of other businesses deal with the same general issue: compliance stops being optional when their customers start requiring it.

A couple things I’ve learned already:

**1. Boring problems can be really good problems.**

There are thousands of businesses that don't need another AI productivity app. They need someone to fix the spreadsheet/process they've been struggling with for five years.

**2. Building for one real customer first makes things way easier.**

I didn't sit down and try to dream up a SaaS product from scratch.

A real company had a real problem, I built something to fix it, and *then* I realized there might be a product here.

Now the interesting part is figuring out whether I can get anyone else to use it.

So i'm curious — has anyone else accidentally stumbled into a really boring niche and turned it into a product?

How did you get from the first company you built it for to your next few customers?

And if you're interested, I’d genuinely appreciate feedback on the landing page/message too: [**sopai.systems**](http://sopai.systems)

Especially from people who sell B2B software to traditional businesses. I'm still trying to figure out how to explain the value without making it sound like every other SaaS landing page.

## 评论（8/9）

> **QuanTradin**（0 分） · 2026-09-17T04:31:16+08:00　
> certificate expiry is a genuinely good problem to have landed on, because the pain arrives with a date attached. nobody needs convincing that it matters, they just need to have been burned once, and in that industry everyone has.
>
> the thing I would guard hardest is the OCR. a wrong expiry date read off a phone photo is worse than the spreadsheet was, because now somebody trusts it and stops checking.

---

> **Ill-Efficiency4579**（2 分） · 2026-09-17T04:36:45+08:00　
> thanks for your feedback! but the ocr scanning also includes a quick human confirmation to ensure accuracy

---

> **QuanTradin**（1 分） · 2026-09-17T05:23:09+08:00　
> the thing I'd watch is what that confirmation looks like in month three. once people trust it they stop reading and start clicking, and then you're back to raw OCR accuracy with a step in the way that everyone assumes is catching things.

---

> **Square-Chance5900**（2 分） · 2026-09-17T05:50:50+08:00　
> Thanks for sharing, and how did you find this first company that had this problem?

---

> **Ill-Efficiency4579**（2 分） · 2026-09-17T05:58:29+08:00　
> they were already a client of mine through my automation work. they brought up the problem, i built something to solve it, and that eventually turned into sopai.

---

> **AlarmingSecurity4**（0 分） · 2026-09-17T14:43:29+08:00　
> Great, now everyone will start looking for boring problems and that also will get saturated

---

> **North_Boss_9937**（1 分） · 2026-09-17T19:26:24+08:00　
> for the next few customers I'd work backwards from where the demand came from, the corporate clients asking for the paperwork before renewal. ask your first customer which clients started requiring it, then look for the other vendors on those same sites (security, HVAC, landscaping, pest control). they're probably getting the same compliance checklist from the same buyer, so you already know their pain and when it hits. that also gives you a landing page line that isn't about OCR at all, something like "have your certs ready before your client's next vendor audit"

---

> **deweetz**（2 分） · 2026-09-17T19:58:02+08:00　
> This is also where I started. I tried looking for a problem that nobody had any interest in solving because it would be "boring". I also think that looking for clients in the company that started requiring it in the beginning is the best starting point.
> What I would recommend is to include in your website presentation the study case of the first client that actually needed this and led up to building a universal solution for others.

## 关联链接

- http://sopai.systems

## 导航

- 项目页：[[10-项目/sopai.systems_f66a3fa9]]
- 渠道页：[[50-渠道/reddit]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
