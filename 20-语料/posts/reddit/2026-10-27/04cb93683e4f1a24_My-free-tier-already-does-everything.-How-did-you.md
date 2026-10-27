---
type: "corpus"
item_id: "04cb93683e4f1a24"
title: "My free tier already does everything. How did you decide what goes behind the paywall?"
source: "reddit"
source_name: "Reddit 独立开发版块"
url: "https://www.reddit.com/r/microsaas/comments/1x8dden/my_free_tier_already_does_everything_how_did_you/"
project_url: "https://smklog.com/"
author: "ShortArm9595"
published_at: "2026-10-17T23:42:31+08:00"
captured_at: "2026-10-27T23:47:59+08:00"
lang: "en"
kind: "post"
topic: "开发者工具"
shard: "2026-10-27"
pub_day: "2026-10-17"
tags:
  - 语料
  - reddit
  - r/microsaas
metrics: {"score": 5, "comments": 19, "upvote_ratio": 0.8571428571428571}
comments_count: 19
comments_total: 19
discovered_via: "reddit:14d+settle10"
---

# My free tier already does everything. How did you decide what goes behind the paywall?

> [!info] 一句话导读
> I run a small site that sells shipping labels (USPS, UPS, FedEx) to people who sell on eBay, Etsy and similar. You type what you're shipping, it works out the b…

> [!meta]- 语料信息（点开展开）
> 来源：Reddit 独立开发版块（post）
> 原帖：<https://www.reddit.com/r/microsaas/comments/1x8dden/my_free_tier_already_does_everything_how_did_you/>
> 指标：得分=5 · 评论=19 · 赞踩比=0.8571428571428571
> 作者：ShortArm9595　|　发布：2026-10-17T23:42:31+08:00
> 项目链接：<https://smklog.com/>
> 采集：2026-10-27T23:47:59+08:00　|　id：`04cb93683e4f1a24`

## 正文

I run a small site that sells shipping labels (USPS, UPS, FedEx) to people who sell on eBay, Etsy and similar. You type what you're shipping, it works out the box and weight, shows prices, and you buy the label. We make a small fee on each label.

There's also a paid plan. The problem: during beta I made everything free for everyone, so today the paid plan adds only one thing, which is covering surprise carrier adjustments up to a monthly limit. That's real value, but it's insurance, and people don't pay monthly for insurance they rarely need.

The obvious move is to take features away from the free tier. I don't want to: the free calculator is how people find us, and the biggest competitor in this space is completely free.

What I'm weighing:

\- no per-label fee on the paid plan, so it pays for itself for anyone shipping more than a handful a month

\- buying labels for all open eBay orders in one click

\- a yearly shipping-expense export for taxes

\- scheduled carrier pickups

For those of you whose free tier is "good enough": what did you put behind the paywall that people actually paid for? Volume, time saved, or something else?

(Site is [smklog.com](http://smklog.com) if context helps.)

## 评论（19/19）

> **Tellenze**（1 分） · 2026-10-18T00:27:45+08:00　
> Your pricing page already lists eBay sync and pickup scheduling under Pro. Are beta users still getting those for free?

---

> **ShortArm9595**（1 分） · 2026-10-18T00:36:55+08:00　
> Fair catch. Right now, yes: during beta everything is open to everyone, eBay sync included, so the pricing page describes the plan as it's meant to be, not what's gated today. Pickup scheduling isn't live yet, and the page should say "coming soon" there. I'll fix that.
>
> Which is exactly the problem I'm asking about: the things listed under Pro are useful, but nobody has a reason to pay for them while they're free.

---

> **LargeLanguageModelo**（1 分） · 2026-10-18T01:26:51+08:00　
> Are you trying to charge more for more, or less for same (as your competitors)?
>
> Without knowing your space, it sounds like you're closer to the latter, which is a tough proposition.

---

> **ShortArm9595**（1 分） · 2026-10-18T01:38:47+08:00　
> Fair read, and it's the trap I'm trying not to walk into. The biggest competitor here is free, so "less for the same" is a race I can't win.
>
> The "more" is that you don't need to know your box: you type what you're shipping, it works out the size and weight, then prices USPS, UPS and FedEx against it. That's exactly what people who ship once in a while are missing, and it's why the free calculator is the hook, not the product.
>
> So the paid plan probably has to be "more for more", aimed at people who ship every week: labels straight from their store orders in one go, no surprise adjustments, fewer clicks per label. The open question is whether that crowd shows up among people who came for the box estimate. Have you seen a free-to-paid split like that work, where the free users and the paying users are basically different people?

---

> **LargeLanguageModelo**（1 分） · 2026-10-18T01:46:47+08:00　
> So quit dangling the carrot (free calculator) that is table stakes.  Just push the hell out of the upgrade features.  Those are your customers.

---

> **ShortArm9595**（1 分） · 2026-10-18T01:48:44+08:00　
> Fair, and I think you're right about who pays. The one bit I'd push back on: most free calculators make you enter the box first, and skipping that is what brings people in at all, so it stays. But it shouldn't be the pitch. For people who ship every week, the pitch has to be the upgrade itself, on its own page, not buried under "free". Thanks, this was useful.

---

> **LargeLanguageModelo**（1 分） · 2026-10-18T02:28:55+08:00　
> Sure, you'll know the market better than I.  Just coming at it from the perspective of this.  Yes, provide the free table stakes to the tire kickers.  But put your real efforts (SEO push, ad spend, etc) on catering to the folks that would find time and/or money savings from paying you.
>
> Porsche doesn't let people know the car does highway speeds, runs on gas, etc.  They put their push on the stuff that Toyota and Ford *don't* do.

---

> **ShortArm9595**（1 分） · 2026-10-18T02:35:34+08:00　
> That's a good way to put it. For us the "stuff Ford doesn't do" is probably the heavy, awkward items: a 40 lb amp or a set of wheels going across the country, where the person doesn't know the box, wants FedEx as an option, and the usual tools make them work all of that out first. That's where the effort goes. Appreciate the push.

---

> **Ludynia_Keyko**（1 分） · 2026-10-18T03:39:20+08:00　
> the bulk action stuff (buying labels for all open orders in one click) is the clearest paywall candidate imo. thats not removing value from free users, its adding a workflow shortcut that only matters once someone hits a certain volume. volume users self-select into paying.

---

> **AllenHere112**（1 分） · 2026-10-18T04:28:07+08:00　
> Insurance is the one item on your list nobody pays monthly for, and the people who would are the ones already angry at the carriers. The per-label fee is the better paywall anyway, because you can leave every feature free and just make the paid plan cost less per label than free does. Anyone shipping 20 labels a month does that arithmetic in four seconds, and nobody has to discover a gated feature first.
>
> The tax export and the scheduled pickups are yearly or occasional, so they can't carry a monthly charge. Bulk buying for open orders is the one that pays off every week, and it also fixes the hole you have right now, which is that people land on the calculator once, get their box estimate and never come back.
>
> Keep free as the front door, let the fee do the selling.

---

> **LargeLanguageModelo**（1 分） · 2026-10-18T04:36:42+08:00　
> That, or perhaps look at the volume play.  If someone has a bin of 50 items they're sending out to 50 people, what's the friction with current solutions on getting those out the door?
>
> I'd suggest not necessarily looking at the weird one-offs like a guitar amp, but the high volume where you can save someone serious time/effort by batching their labor.

---

> **ShortArm9595**（1 分） · 2026-10-18T05:05:53+08:00　
> Thanks everyone, this was more useful than I expected. Where it landed: the free calculator stays as the front door, and the paid plan becomes a volume tool, meaning buying labels for all open orders in one go, at a lower per-label price than free. Insurance-style extras and a yearly tax export aren't worth a monthly charge on their own.

---

> **Gullible_Guide402**（1 分） · 2026-10-18T11:08:49+08:00　
> I guess the rule is simple, ask users for what they willing to pay, any random person on reddit don't know what your users want.

---

> **Easy-Purple-1659**（1 分） · 2026-10-18T13:06:11+08:00　
> The fee is the cleaner lever than the features, and it fits the free tier instead of fighting it.
>
> Today you take a fee per label on free and sell insurance on paid. Flip the paid plan to no per-label fee, priced below what a weekly shipper already pays you in fees. The upgrade becomes arithmetic rather than a promise: at ten labels a month the plan is cheaper, at two it is not, and the people who pick it are the ones you want. Nothing gets pulled from the free tier, so the calculator keeps doing the job of finding you customers.
>
> The tax export is the one item I would price separately, once a year. It solves a seasonal problem, so it earns its money in January and looks like dead weight the other eleven months.

---

> **geoffreybyers**（1 分） · 2026-10-18T15:44:22+08:00　
> Insurance is a terrible hook. Nobody pays monthly for a risk they might never hit. They do pay to buy back their time. The bulk actions and exports move the sale from "maybe you'll save $10" to "you'll save 10 hours a month." That's the stronger anchor.

---

> **freedomchaserr**（1 分） · 2026-10-18T21:36:53+08:00　
> Usually I stick to the philosophy of putting everything behind the paywall. The only thing I try to provide for free is a demo of some kind.
>
> But your case doesn't seem to be that straight forward. Immediately I like the fixed rate for no per-label fee solution.
>
> Thinking more long time I would maybe even consider keeping it free if that is a possibility. I think the strength lies in volume here. You are addressing a huge market with this kind of product and there are many more features besides the ones you already listed you can provide to your customers. Eventually you will find something that naturally makes sense for monetizing.

---

> **ShortArm9595**（1 分） · 2026-10-18T22:33:59+08:00　
> That's where this thread has landed, yours and a couple of others: the paid plan should be the volume tool, not the one-off heavy stuff. Concretely: pull every open order from the store, fill in weight and box from what you set once per listing, buy all the labels in one go, and pay less per label than on free. The odd 40 lb amp stays the free front door rather than the thing I sell. Thanks for pushing on it, that's the direction I'm leaning now.

---

> **CategoryTeardowns**（1 分） · 2026-10-24T02:17:45+08:00　
> One thing that helped me with this kind of call: look at what your biggest free competitor puts behind its own paywall, and what the paid reviewers complain about. Free tools usually charge for the stuff that costs them support time or needs accounts, so that's a hint at what people will actually pay to skip. For you I'd lean toward the weekly-shipper stuff, the one-click bulk labels and the no per-label fee, since those save real time every week. The tax export is nice but people only feel it once a year, so I'd make it a bonus rather than the reason to upgrade. Then try the paywall on a small slice first, like 10 to 20 percent of new signups, before you change it for everyone.

---

> **ShortArm9595**（1 分） · 2026-10-24T03:36:26+08:00　
> Thanks, that’s a useful way to look at it. I learned a related lesson this month, the hard way.
>
> Every pain point you remove for honest customers also removes a step for the ones who don’t plan to pay. I had made checkout as light as I could: no account, no card kept on file. Then a customer gave me the weight and size for two boxes himself, said they were identical, and the carrier weighed the first one at more than half again what he’d told me. USPS billed me the difference weeks later, I invoiced him, and the invoice was simply ignored. It was only a few dollars, but one person like that is enough to turn a nice-to-have into a rule for everyone.
>
> So I went and read how the established label sellers handle it, and they all do the same thing: a card on file, carrier corrections charged to it automatically, a handling fee on top (ShipStation and [Stamps.com](http://Stamps.com) add 20%), and no new labels while a correction is unpaid. I had taken all that for friction. It’s scar tissue from exactly this situation. My checkout now does the same, and anyone who types their own weight confirms they weighed the packed box.
>
> So before I remove a step now, I ask who it was protecting. In shipping, the boring business model everyone else uses is usually the answer.

## 关联链接

- http://smklog.com

## 导航

- 项目页：[[10-项目/smklog.com_1dc91baf]]
- 渠道页：[[50-渠道/reddit]]
- 赛道：`开发者工具`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
