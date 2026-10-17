---
type: "corpus"
item_id: "9e983f14c24b2ce1"
title: "Micro SaaS: free temp mail + OTP API — just shipped VS Code/Cursor extensions. What would you build next?"
source: "reddit"
source_name: "Reddit 独立开发版块"
url: "https://www.reddit.com/r/microsaas/comments/1wzcaxj/micro_saas_free_temp_mail_otp_api_just_shipped_vs/"
author: "WispInbox"
published_at: "2026-10-07T03:47:39+08:00"
captured_at: "2026-10-17T13:36:54+08:00"
lang: "en"
kind: "post"
topic: "开发者工具"
shard: "2026-10-17"
pub_day: "2026-10-07"
tags:
  - 语料
  - reddit
  - r/microsaas
metrics: {"score": 3, "comments": 8, "upvote_ratio": 1}
comments_count: 8
comments_total: 8
discovered_via: "reddit:14d+settle10"
---

# Micro SaaS: free temp mail + OTP API — just shipped VS Code/Cursor extensions. What would you build next?

> [!info] 一句话导读
> I’ve been building a tiny product for a problem I hit constantly while testing signups:

> [!meta]- 语料信息（点开展开）
> 来源：Reddit 独立开发版块（post）
> 原帖：<https://www.reddit.com/r/microsaas/comments/1wzcaxj/micro_saas_free_temp_mail_otp_api_just_shipped_vs/>
> 指标：得分=3 · 评论=8 · 赞踩比=1
> 作者：WispInbox　|　发布：2026-10-07T03:47:39+08:00
> 项目链接：—
> 采集：2026-10-17T13:36:54+08:00　|　id：`9e983f14c24b2ce1`

## 正文

Hey r/microsaas

I’ve been building a tiny product for a problem I hit constantly while testing signups:

Create temp email → wait for OTP → copy code → paste into app

(and repeat that in Playwright / Cypress / the editor all day)

\*\*What it is\*\*

WispInbox — disposable inbox for signups & OTP.

• Web inbox (no account needed for free)

• API: create mailbox + long-poll wait for OTP

• Free: 3 OTP API calls/day · Pro: unlimited

• Just shipped: VS Code + Cursor extensions

Happy to drop the site / install / docs in a reply if anyone wants them.

\*\*Business model (honest)\*\*

Free tier + ads, Pro for unlimited OTP API / longer retention. Early revenue is tiny — still in distribution mode.

\*\*Ask\*\*

If you build micro SaaS / do QA:

1. Would you use an editor extension for temp mail, or only HTTP API in tests?

2. Is custom domain (so forms don’t block disposable domains) the obvious next feature?

3. Anything you’d refuse to pay for vs something you’d pay for immediately?

Blunt feedback welcome. Trying to stay micro and useful.

## 评论（8/8）

> **ApplicationOne4927**（1 分） · 2026-10-07T04:19:28+08:00　
> 3 OTP calls a day is a demo, not a free tier. You're pitching this at Playwright and Cypress suites, where one run burns through that before the first assertion. So what does Pro actually cost, since that's the only number here that matters?

---

> **WispInbox**（1 分） · 2026-10-07T04:23:47+08:00　
> Fair point - 3 OTP waits/day is intentionally a smoke-test quota, not a CI quota. One Playwright run will chew through it.
>
> **Pro pricing (INR):**
>
> * **Individual** \- ₹9 for 14 days, then **₹35/month** (1 address, unlimited OTP API)
> * **Group** \- ₹129 intro / **₹279/month** (10 addresses)
> * **Business** \- ₹349 intro / **₹777/month** (30 addresses)
>
> Free web inbox stays unlimited for manual use. Free OTP API is just to try the wait endpoint; for Cypress/Playwright suites you’ll want Pro on that mailbox.
>
> If \~₹35/mo for unlimited OTP wait is a no-go for your setup, tell me what monthly budget + call volume you’d actually pay for and I’ll take that seriously.

---

> **Tellenze**（1 分） · 2026-10-07T04:24:15+08:00　
> For tests of your own app, I'd add the 'after' filter to the first API example. It lets you check only mail received since the current signup attempt. Your docs list it, but the sample leaves it out. A resend-code example would make that benefit easy to see.

---

> **WispInbox**（1 分） · 2026-10-07T04:29:29+08:00　
> Good catch - docs listed `after` but the first sample skipped it.
>
> Updated the primary cURL + Node examples to:
>
> 1. stamp time **before** signup / send-code
> 2. pass `after=…` on `/api/otp`
> 3. show a **resend** flow (stamp again → click Resend → wait with the new `after`)
>
> Live here: [https://wispinbox.com/api-docs/](https://wispinbox.com/api-docs/)
>
> That way Playwright/Cypress only match mail from the current attempt, not an older code in the same mailbox. Thanks for the nudge.

---

> **Tellenze**（2 分） · 2026-10-07T04:36:51+08:00　
> Could the first email still match if it arrives late, after the resend's 'after' time? The docs describe a filter on arrival time. I'd add that case to the resend test, so it checks delayed emails as well as codes already in the inbox.

---

> **WispInbox**（1 分） · 2026-10-07T04:46:45+08:00　
> Yep - that’s a real race.
>
> `after` filters on **when we received the message**, not when your app sent it. So if email #1 is delayed and lands *after* you stamp for resend, it can still match the second wait.
>
> Safest patterns:
>
> 1. `markSeen=1` **on the first wait +** `unseenOnly=1` **on the resend wait** (so a late first email that’s already been consumed doesn’t win)
> 2. **Assert** `resent.code !== first.code` in the test
> 3. Or **use a fresh mailbox per attempt** when you want zero ambiguity
>
> Updated the docs/examples with that caveat + the `markSeen` / `unseenOnly` resend flow: [https://wispinbox.com/api-docs/](https://wispinbox.com/api-docs/)
>
> Thanks for pushing on the edge case — that’s exactly how these APIs get bitten in CI.

---

> **alankffman**（1 分） · 2026-10-07T05:14:41+08:00　
> does custom domain mean I bring my own, or you sell me a fresh one nobody's blocklisted yet?

---

> **daniel933912**（1 分） · 2026-10-07T06:02:51+08:00　
> the extension matters less than you think. ci never clicks, so the api path decides if this sticks, the extension is just for hand testing on your own machine.
>
> on custom domain, handing out fresh domains stops working fast. the disposable check most signup forms run is a list that updates every few days, so anything you hand out gets burned. letting people point their own catch-all domain at your inbox is the version that survives, and that's the one I'd pay for.

## 导航

- 项目页：—（本条不是项目，按设计不建实体页）
- 渠道页：[[50-渠道/reddit]]
- 赛道：`开发者工具`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
