---
type: "corpus"
item_id: "59740dfacb653d1e"
title: "How much should I charge for this system?"
source: "reddit"
source_name: "Reddit 独立开发版块"
url: "https://www.reddit.com/r/SaaS/comments/1xt6r24/how_much_should_i_charge_for_this_system/"
author: "Friendly_Magician101"
published_at: "2026-11-11T11:02:44+08:00"
captured_at: "2026-11-21T14:46:40+08:00"
lang: "en"
kind: "post"
topic: "开发者工具"
shard: "2026-11-21"
pub_day: "2026-11-11"
tags:
  - 语料
  - reddit
  - r/SaaS
metrics: {"score": 3, "comments": 12, "upvote_ratio": 1}
comments_count: 10
comments_total: 12
discovered_via: "reddit:14d+settle10"
---

# How much should I charge for this system?

> [!info] 一句话导读
> I’m a solo dev I’ve got a meeting with a client soon. Need a reality check on pricing.

> [!meta]- 语料信息（点开展开）
> 来源：Reddit 独立开发版块（post）
> 原帖：<https://www.reddit.com/r/SaaS/comments/1xt6r24/how_much_should_i_charge_for_this_system/>
> 指标：得分=3 · 评论=12 · 赞踩比=1
> 作者：Friendly_Magician101　|　发布：2026-11-11T11:02:44+08:00
> 项目链接：—
> 采集：2026-11-21T14:46:40+08:00　|　id：`59740dfacb653d1e`

## 正文

I’m a solo dev I’ve got a meeting with a client soon. Need a reality check on pricing.

What they want:

* Onboarding system for self-employed courier drivers working under Amazon DSPs
* Driver contracts sent through Zoho Sign, then the system auto-activates them once signed
* Payrun module: invoices for each driver, one invoice to the DSP, then pay all the drivers
* Fleet management: vehicles, accident reporting, compliance reminders

I would like some clarity on the pricing.

1. What would you charge for the build? Fixed price or hourly?
2. What’s a fair monthly retainer for maintenance and support?
3. Anything I should be careful about (payments, liability, scope creep)?

Thanks in advance, and honest numbers are welcome!

## 评论（10/12）

> **careful_keys**（1 分） · 2026-11-11T11:06:56+08:00　
> Price the payrun piece on its own, and only after you know who actually moves the money. If the system just generates invoices and a payment file the DSP executes, that's a document generator and it's the easy version. If anyone expects it to hold balances or push payments out itself, you're building a payments product, and the reconciliation, audit trail and error handling around that will be bigger than the rest of the build. Get that in writing before you quote a fixed number. On a build this size I'd go fixed price per module with a written scope, hourly for anything after that.

---

> **Friendly_Magician101**（0 分） · 2026-11-11T11:08:09+08:00　
> Hi, Could you please give an estimate on the pricing ?

---

> **CapitalSundae2758**（0 分） · 2026-11-11T11:15:21+08:00　
> Small thing, and then I'll shut up: "courier drivers" is redundant, a courier is already the person doing the driving. Unless you've got couriers who don't drive, in which case carry on.

---

> **ProspectingManual**（3 分） · 2026-11-11T11:44:45+08:00　
> Imagine fixing the wording instead of helping the guy with his actual question 😂

---

> **Wise_College6078**（1 分） · 2026-11-11T11:49:22+08:00　
> self-employed

---

> **Blobstein_Ijay**（1 分） · 2026-11-11T18:22:45+08:00　
> that payrun and fleet management piece is way bigger than it sounds on paper. If you go fixed price, break it into paid milestones and charge simply to scope out the architecture first, otherwise scope creep on the payroll edge cases will eat your margin alive

---

> **Friendly_Magician101**（1 分） · 2026-11-11T18:59:44+08:00　
> i understand that could please please give an estimate of the pricing, if possible ?

---

> **vapvarun**（1 分） · 2026-11-12T02:39:21+08:00　
> Quote it in phases rather than one fixed price: onboarding and e-sign activation first, fleet and compliance reminders second, payrun last, so the client sees value early and you learn their edge cases before touching money.
>
> Fixed price per phase works if each phase has a written list of what's in and what's out. For the retainer, tie it to a set number of support hours plus the things that will break on their own, like Zoho API changes and new compliance rules, and bill anything beyond that hourly.
>
> Put code ownership and hosting access in the contract too, so a later handover doesn't turn into a dispute.

---

> **NinjaManagrr**（1 分） · 2026-11-13T15:24:58+08:00　
> fixed price the build, hourly only for anything after signing. itemize the deliverables with quantities in the proposal so "can you also add X" becomes a change order instead of a freebie, that's where these projects bleed.

---

> **Chloe_ArceusLegal**（1 分） · 2026-11-18T05:33:18+08:00　
> Fixed price per module is typical, with 20-30% up front and each milestone signed off as completed.  The rest of the payment is split across delivery phases.
>
> No personal experience, but some research sets custom builds like this at $30-$100k unless they’re enterprise and then they can be much higher. These are agency rates, so a solo dev may charge less.
>
> There’s usually a retainer for annual maintenance priced at 15-25% of the initial build per year.

## 导航

- 项目页：—（本条不是项目，按设计不建实体页）
- 渠道页：[[50-渠道/reddit]]
- 赛道：`开发者工具`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
