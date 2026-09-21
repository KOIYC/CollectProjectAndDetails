---
type: "corpus"
item_id: "f337e11f0c6e4042"
title: "Tax engine for SaaS?"
source: "reddit"
source_name: "Reddit 独立开发版块"
url: "https://www.reddit.com/r/SaaS/comments/1wjc0fy/tax_engine_for_saas/"
author: "Ok-Memory2809"
published_at: "2026-09-18T09:06:26+08:00"
captured_at: "2026-09-21T09:45:46+08:00"
lang: "en"
kind: "post"
topic: "开发者工具"
shard: "2026-09-21"
pub_day: "2026-09-18"
tags:
  - 语料
  - reddit
  - r/SaaS
metrics: {"score": 4, "comments": 14, "upvote_ratio": 0.84}
comments_count: 14
comments_total: 14
discovered_via: "reddit:7d+settle3"
---

# Tax engine for SaaS?

> [!info] 一句话导读
> I’m building a SaaS platform and I’m looking for a tax engine / tax calculation API that can automatically determine and calculate the appropriate sales tax, VA…

> [!meta]- 语料信息（点开展开）
> 来源：Reddit 独立开发版块（post）
> 原帖：<https://www.reddit.com/r/SaaS/comments/1wjc0fy/tax_engine_for_saas/>
> 指标：得分=4 · 评论=14 · 赞踩比=0.84
> 作者：Ok-Memory2809　|　发布：2026-09-18T09:06:26+08:00
> 项目链接：—
> 采集：2026-09-21T09:45:46+08:00　|　id：`f337e11f0c6e4042`

## 正文

I’m building a SaaS platform and I’m looking for a tax engine / tax calculation API that can automatically determine and calculate the appropriate sales tax, VAT, or GST for each transaction based on the customer’s location.

I’m looking for something that’s easy to integrate directly into our platform through an API or SDK and can automatically handle changing tax rates and jurisdictions. Since we’re an early-stage startup, I’m particularly interested in a solution that doesn’t have fees, minimum commitments, setup fees, or other significant fixed costs.

Ideally, I’d like the cost to scale primarily with our transaction volume rather than paying a large amount upfront while we’re still small.

I’ve seen solutions like Avalara, TaxJar, Stripe Tax, and similar services, but I’d love to hear from other developers about what they’re actually using.

## 评论（14/14）

> **joshdotmn**（2 分） · 2026-09-18T09:11:31+08:00　
> If you don’t use Stripe Tax, eventually you’re going to wish you had used Stripe Tax.

---

> **Ok-Memory2809**（1 分） · 2026-09-18T09:15:11+08:00　
> While Stripe and Stripe Tax would be the ideal solution, unfortunately our SaaS falls under the high-risk category (as crazy as it might sound) so we cannot use Stripe under Stripe’s Terms of Service.

---

> **joshdotmn**（2 分） · 2026-09-18T09:17:34+08:00　
> Stripe called me high-risk too, I get it.
>
> TaxJar would be a close second.

---

> **francksiduo**（1 分） · 2026-09-18T09:46:58+08:00　
> for us it came down to whether we wanted to stay merchant of record or not. paddle and lemon squeezy handle tax calc, filing and remittance because they resell your product for you, but they take a bigger cut and add a redirect at checkout. stripe tax is cheaper and stays inside your own checkout, but you still own the actual filing in each jurisdiction once you cross a threshold, which gets annoying fast. avalara and taxjar are built for a lot more volume than most early stage SaaS needs.
>
> we started with stripe tax and only looked at switching to a MoR once EU VAT thresholds started getting messy.

---

> **Suitable-Ad5348**（2 分） · 2026-09-18T13:39:06+08:00　
> TaxJar if you stay merchant of record. Avalara gets painful at low volume.
>
> or hand it to Paddle / Lemon Squeeze and let them do filing. bigger cut + checkout redirect though.

---

> **UpsetTechnology2541**（1 分） · 2026-09-18T23:28:29+08:00　
> Common ones are:
> \* Vertex (Large companies)
> \* Taxjar (being replaced by stripe tax, but doesn't have feature parity and only supports US)
> \* Kintsugi (Startup friendly, supports sales tax, VAT, GST)
> \* Avalara (It's owned by a PE firm, you can ask people about their experiences using them, they will be blunt)

---

> **Total-Reasonable**（1 分） · 2026-09-18T23:47:19+08:00　
> Tax calculation and jurisdiction rules are a separate problem from keeping your rate table current. I use vatnode's free rates endpoint for the latter; [https://vatnode.dev/vat-rates](https://vatnode.dev/vat-rates) has daily-refreshed reference rates for 45 European countries, but it won't determine the tax treatment of an individual transaction.

---

> **try-Kintsugi**（1 分） · 2026-09-19T00:09:57+08:00　
> Full disclosure, i work at kintsugi so take this with that in mind, but figured i'd chime in since this is literally what we built for people in your exact spot. handles sales tax, VAT, and GST calc via API, and the nexus tracking is automatic so you're not manually checking rules state by state as you grow. Could be worth chatting to see what that'd look like for your volume, though. Happy to answer specific questions if useful; otherwise, no worries- just wanted to put it on your radar

---

> **TaxJar_social**（1 分） · 2026-09-19T01:57:34+08:00　
> Full disclosure, I’m with TaxJar, which is part of Stripe.
>
> Based on your requirements, the key distinction is US-only versus global coverage. TaxJar’s API is focused on US sales tax, including jurisdiction-level calculations, product taxability, exemptions, and changing tax rates. For a new business that needs sales tax plus VAT/GST through one API, Stripe Tax is probably a better fit.
>
> Stripe Tax Basic offers pay-as-you-go API pricing with no recurring fees. We'd recommending checking the list of supported countries and integration requirements against your specific customer and payment flows.
>
> Whichever vendor you evaluate, I’d also compare registration/filing support, exemptions, refunds, sandbox quality, API latency, and what happens when you exceed your initial volume, not just the calculation price.
>
> Happy to answer specific questions, best of luck!

---

> **Ok-Memory2809**（1 分） · 2026-09-19T02:46:16+08:00　
> What about Saas that are considered high-risk?

---

> **TaxJar_social**（1 分） · 2026-09-19T03:28:55+08:00　
> Depending on the business, TaxJar can help support the US sales tax compliance side of things.

---

> **Ok-Memory2809**（1 分） · 2026-09-19T03:38:42+08:00　
> Check dm

---

> **HudsonScottHarper**（0 分） · 2026-09-19T15:28:41+08:00　
> if you're already on stripe, stripe tax is the least work by a mile

---

> **InvestmentFree9567**（0 分） · 2026-09-19T15:31:33+08:00　
> Even if you use any of these tax engines, you still need to handle tax reconciliation on those countries. Why don't you go with merchant of records?

## 导航

- 项目页：—（本条不是项目，按设计不建实体页）
- 渠道页：[[50-渠道/reddit]]
- 赛道：`开发者工具`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
