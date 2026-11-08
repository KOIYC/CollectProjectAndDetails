---
type: "corpus"
item_id: "73b49fd67b44af49"
title: "Building PaidCheck in public: what I learned catching \"paid but no access\" bugs in Stripe"
source: "reddit"
source_name: "Reddit 独立开发版块"
url: "https://www.reddit.com/r/buildinpublic/comments/1xi5uwf/building_paidcheck_in_public_what_i_learned/"
project_url: "https://paidcheck.app/report"
author: "Due_Anything_5861"
published_at: "2026-10-29T08:46:15+08:00"
captured_at: "2026-11-08T12:52:11+08:00"
lang: "en"
kind: "post"
topic: AI 工具/Agent
shard: "2026-11-08"
pub_day: "2026-10-29"
tags:
  - 语料
  - reddit
  - r/buildinpublic
metrics: {"score": 3, "comments": 11, "upvote_ratio": 1}
comments_count: 11
comments_total: 11
discovered_via: "reddit:14d+settle10"
---

# Building PaidCheck in public: what I learned catching "paid but no access" bugs in Stripe

> [!info] 一句话导读
> I'm building PaidCheck, a small solo project (link at the bottom is mine). It compares Stripe with who has access in your app.

> [!meta]- 语料信息（点开展开）
> 来源：Reddit 独立开发版块（post）
> 原帖：<https://www.reddit.com/r/buildinpublic/comments/1xi5uwf/building_paidcheck_in_public_what_i_learned/>
> 指标：得分=3 · 评论=11 · 赞踩比=1
> 作者：Due_Anything_5861　|　发布：2026-10-29T08:46:15+08:00
> 项目链接：<https://paidcheck.app/report>
> 采集：2026-11-08T12:52:11+08:00　|　id：`73b49fd67b44af49`

## 正文

I'm building PaidCheck, a small solo project (link at the bottom is mine). It compares Stripe with who has access in your app.

Lessons so far:

\- Stripe is the source of truth for who paid, so I read its subscription and invoice records directly and never trust the app's own state.

\- Duplicate subscriptions are harder to catch than they look. The same customer can be on a different price of the same product, or can appear twice under one email.

\- A read-only restricted key makes it far easier for a founder to try, so I wrote a step-by-step guide for creating one.

\- Traffic is tiny so far, so I'm learning distribution the slow way. I'm focusing on helpful guides for Stripe billing problems.

Question: what billing bug cost you the most that you only found when a customer complained?

[https://paidcheck.app/report](https://paidcheck.app/report)

## 评论（11/11）

> **mrsskonline**（2 分） · 2026-10-29T08:51:35+08:00　
> great tool idea u/Due_Anything_5861 the biggest billing bug i've seen - proration errors. when a user upgrades mid-cycle, stripe calculates the credit but many apps fail to apply it correctly, leading to double charges or lost access. ur tool could definitely help catch those mismatches.

---

> **Relevant-Spot-3192**（1 分） · 2026-10-29T08:52:07+08:00　
> wake me when the traffic exists

---

> **FuturisticSalamander**（1 分） · 2026-10-29T08:53:54+08:00　
> proration math is the silent killer, one decimal point off and suddenly your support inbox is on fire

---

> **OkMarionberry5500**（1 分） · 2026-10-29T08:57:45+08:00　
> Not a single number in here. How many accounts have you actualy run this against, and how many duplicates did it flag? "Harder to catch than they look" is doing a lot of work with no counts behind it.

---

> **investigatormaker**（1 分） · 2026-10-29T09:05:40+08:00　
> Without a war story of my own, I'd point PaidCheck first at states Stripe treats as normal but apps mishandle: a subscription in past\_due or unpaid while the app still grants access, a refunded or disputed charge where access is never revoked, and cancel\_at\_period\_end handled as an instant cancel, which locks out someone who paid. That last one usually surfaces only as an angry email. Each also works as one of your Stripe billing guides, titled by the symptom a founder would search for rather than the API field.
>
> I make ThreadFox. We find relevant Reddit conversations and post for your business. We'll post 3 replies free first, no card; then the $79 Pilot covers seven days and up to 50 posts and replies. No automatic renewal.
>
> [https://threadfox.vip/p/e3jzt/managed](https://threadfox.vip/p/e3jzt/managed)

---

> **AsparagusKey5662**（1 分） · 2026-10-29T09:31:01+08:00　
> "Traffic is tiny so far" and not a single number. Isn't posting the actual figures the one thing building in public is supposed to be about?

---

> **Due_Anything_5861**（1 分） · 2026-10-29T09:49:02+08:00　
> Fair point. Honest numbers: about 100 page views in the last 7 days, and the guides have barely been indexed yet. I don't have a count of accounts checked or duplicates flagged that I'd stand behind, so I left them out rather than make something up. I'll post real figures as they exist.

---

> **Due_Anything_5861**（1 分） · 2026-10-29T09:49:27+08:00　
> Thanks. Proration on mid-cycle upgrades is a good case. I only check for duplicate subscriptions after an upgrade today, not proration math, and I'd rather say that than overclaim.

---

> **chriskr7**（1 分） · 2026-10-29T11:45:57+08:00　
> Not a war story, but the class I'd point PaidCheck at first is webhook handling rather than Stripe state itself:
>
> \- Events arriving out of order, e.g. customer.subscription.updated before checkout.session.completed, so the app grants and then "un-grants" access, or the reverse.
>
> \- Handlers that aren't idempotent. Stripe retries, so a non-idempotent handler can double-grant credits or create duplicate local records. That's one way you get the "two subscriptions under one email" you mentioned.
>
> \- Trials that end without a payment method. The subscription goes to incomplete\_expired or canceled, but the app only listened for invoice.payment\_failed and never revokes access.
>
> A nightly reconcile of Stripe vs. the app's entitlements catches all three. That's basically your product, so leading with those exact scenarios in your guides might be the distribution angle.

---

> **paleflier**（1 分） · 2026-10-31T02:09:06+08:00　
> The nightly check is a good safety net, but I'd also stop letting the order events show up in decide who has access. Webhooks don't arrive in order and Stripe retries them, so if each event flips access on or off you'll end up with weird states.
>
> A more reliable approach is to treat the webhook as a "something changed" ping. When one comes in, fetch the customer's current subscription from Stripe and recompute what they should have access to from that. Then it doesn't matter if events are late, duplicated, or out of order, because you're always reading the latest state.
>
> It also helps to keep entitlements as their own thing in your app (customer X has feature Y, limit Z) instead of checking Stripe plan IDs all over your code. Then a plan change only touches one place.

---

> **Due_Anything_5861**（1 分） · 2026-11-01T02:25:12+08:00　
> This is really useful, thanks. On what PaidCheck sees today: the free report flags Stripe events your endpoint never acknowledged (failed deliveries from the last 30 days), endpoints that are disabled, and endpoints that don't listen for the subscription or checkout events an app needs. It can't see the order your handler processed events in, or whether it's idempotent. It only sees the result in Stripe, so I won't claim those two.
>
> The trial-ending-with-no-card case is one I want to test properly. If anyone here has a Stripe account (test mode is fine) and wants to try it, I'll walk you through it. It's a read-only restricted key, a couple of minutes to set up, and nothing from the free report gets stored. I'd genuinely like to hear what it gets wrong. Free report: https://paidcheck.app/report

## 导航

- 项目页：[[10-项目/paidcheck.app_44561441]]
- 渠道页：[[50-渠道/reddit]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
