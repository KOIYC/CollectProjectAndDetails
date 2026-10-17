---
type: "corpus"
item_id: "53e3515b8fca52f4"
title: "Our cheapest customers generate our most expensive tickets. What did you change?"
source: "reddit"
source_name: "Reddit 独立开发版块"
url: "https://www.reddit.com/r/SaaS/comments/1wyk8m4/our_cheapest_customers_generate_our_most/"
author: "arslannasir128"
published_at: "2026-10-06T05:03:15+08:00"
captured_at: "2026-10-16T09:36:29+08:00"
lang: "en"
kind: "post"
topic: AI 工具/Agent
shard: "2026-10-16"
pub_day: "2026-10-06"
tags:
  - 语料
  - reddit
  - r/SaaS
metrics: {"score": 8, "comments": 31, "upvote_ratio": 1}
comments_count: 31
comments_total: 31
discovered_via: "reddit:14d+settle10"
---

# Our cheapest customers generate our most expensive tickets. What did you change?

> [!info] 一句话导读
> The big accounts barely write in. The low-tier ones open a ticket for everything, and every one of those tickets costs the same support hour.

> [!meta]- 语料信息（点开展开）
> 来源：Reddit 独立开发版块（post）
> 原帖：<https://www.reddit.com/r/SaaS/comments/1wyk8m4/our_cheapest_customers_generate_our_most/>
> 指标：得分=8 · 评论=31 · 赞踩比=1
> 作者：arslannasir128　|　发布：2026-10-06T05:03:15+08:00
> 项目链接：—
> 采集：2026-10-16T09:36:29+08:00　|　id：`53e3515b8fca52f4`

## 正文

The big accounts barely write in. The low-tier ones open a ticket for everything, and every one of those tickets costs the same support hour.

I started tracking hours by plan instead of by ticket, and the picture flipped. The accounts that pay the least burn the most time.

For the rest of you running support, do you track cost per tier, and what did you change when you saw it?

## 评论（31/31）

> **pinkdragon_Girl**（1 分） · 2026-10-06T05:07:38+08:00　
> This is normal you need to find a way to prevent these tickets by having a better platform

---

> **UpperWorld11**（1 分） · 2026-10-06T05:26:17+08:00　
> Split those hours into setup questions and actual bugs before you change pricing. The cheap tier signs up on its own, so the walkthrough your bigger accounts got in onboarding comes back one ticket at a time. What does the split look like?

---

> **recon_demon1859**（1 分） · 2026-10-06T05:41:54+08:00　
> I would break the tickets down by category before changing the plans. If most of the time is going to setup or the same few questions, fix those in the product and docs first. After that, give lower tiers an async response time and keep hands-on help for higher plans. If a cheap plan still costs more to support than it brings in, the price or plan needs to change.

---

> **sheapabra**（1 分） · 2026-10-06T07:41:09+08:00　
> tbh the real question is whether those low-tier accounts ever upgrade. if they do at a decent rate, the support cost is basically acquisition cost. if they dont, you're subsidizing them indefinitely and the pricing needs to change

---

> **Acrobatic-Laugh1856**（0 分） · 2026-10-06T11:13:39+08:00　
> tracking support hours by plan is a simmple but relly usefulll metric.

---

> **nbass668**（2 分） · 2026-10-06T11:17:31+08:00　
> We support both enterprises clients and small businesses. And its true... the small businesses are the most annoying even though their yearly subscription costs less than one month for a corporate client. It’s because small business owners use the software themselves and are always asking for more features or updates, whereas employees at corporate firms just get training and follow instructions and call if something breaks.
>
> But funny enough its those same small business clients that give us the most input and ideas for new features.
>
> It is the way it is and we accept it... the difference is with small clients we dont budge or give discounts while corproate clients gets 3 months full POC at no cost to convince them .

---

> **RajatKhoware**（1 分） · 2026-10-06T12:31:55+08:00　
> We hit this with retainer clients. The fix was splitting tickets into setup questions vs real bugs before touching pricing. Most cheap-tier tickets are onboarding gaps wearing a support ticket costume. Fix the product and docs first, then give low tiers async response times and keep hands-on help for higher plans. Also check if low-tier accounts ever upgrade. If they do, that support cost is acquisition cost. If they don't, your pricing is wrong.

---

> **gmsniperx**（1 分） · 2026-10-06T16:58:19+08:00　
> Have you thought about connecting AI to answer them first where knowledge is taken from docs? The difficult part is to keep te docs updated and that is why we built our own system which answers tickets and also udpated help docs on new releases (with screenshots) and also covers gaps from unanswered tickets.  This can save you from spending resources on low-tier customers who are always difficult to handle. and btw, our system is opensource so you can self-host it if you want.

---

> **arslannasir128**（1 分） · 2026-10-06T21:43:48+08:00　
> Auto-updating the doc on release is the half nobody ships, so that part is real.
>
> The one I can't solve is the account. A refund answer depends on that customer's plan, and a fresh doc can still be wrong about the person asking it.

---

> **arslannasir128**（1 分） · 2026-10-06T21:46:21+08:00　
> Mostly billing and plan state on my side, not bugs. Seat counts, invoices, why a charge moved since last month.
>
> I wanted a doc to take those. It never could, because the answer is about that account and not about the product.

---

> **arslannasir128**（1 分） · 2026-10-06T21:58:02+08:00　
> The upgrade test is the sharp one and I had it backwards.
>
> Where I'd push is the split itself. Half of what landed on the cheap tier wasn't a how-do-I, it was someone asking whether the answer holds for their account. No product fix and no doc closes that.

---

> **arslannasir128**（1 分） · 2026-10-06T21:59:42+08:00　
> The small accounts are the ones telling you what to build next. The trained enterprise user asks for the thing that already exists.
>
> I stopped pricing those hours as pure waste.

---

> **arslannasir128**（1 分） · 2026-10-06T22:01:19+08:00　
> That's the line I'd put above the whole analysis.
>
> The trap is nobody owns both numbers. Support carries the cost, growth owns the upgrade rate, and neither one is asked to hold the other.

---

> **UpperWorld11**（1 分） · 2026-10-06T22:16:29+08:00　
> No doc was ever going to take those, since each one is a lookup only their account can answer. A seat added mid cycle gets prorated into the invoice and the total moves with no visible reason, so people open a ticket about a number that is correct. Put what changed and when on the invoice page, and the live seat count on the plan page. Most of that queue closes itself.

---

> **gmsniperx**（1 分） · 2026-10-06T23:51:27+08:00　
> We are using helpin (dot) io and connected with our Paddle's MCP. Each customer request is first authenticated if it is from the actual customer and then the agent is asked to make a STRICTLY read-only request to check billong data for that customer.
>
> For changes, someone approves and the agent  performs the billing action via MCP. So, that part is also solved.

---

> **arslannasir128**（1 分） · 2026-10-07T00:15:19+08:00　
> The prorated seat is the ticket I see most. The number's right, nothing on the page says why it moved, so they open a ticket to check.
>
> I'd put the change line under the total, not on a second screen nobody opens. That's the cheap fix and everyone wants to skip it.

---

> **arslannasir128**（1 分） · 2026-10-07T00:17:59+08:00　
> The auth-before-read step is the one most setups skip, good on you.
>
> I'd still push back on solved. A read-only call to a stale record returns a confident wrong answer, and nothing in the response says how old it is.

---

> **arslannasir128**（1 分） · 2026-10-07T00:21:30+08:00　
> Fair, that closes the write side. The read is where I'm stuck. A billing record forty eight hours stale returns a confident wrong answer and nothing in the payload says how old it is.
>
> Does yours hit Paddle live on every question, or a cached copy?

---

> **arslannasir128**（1 分） · 2026-10-07T01:16:07+08:00　
> Category first is the right order. I never got mine sorting cleanly. A billing ticket about a number that moved is neither setup nor bug, and no doc fixes it. Async on the cheap tiers trims volume right up to the quiet cancel.

---

> **gmsniperx**（1 分） · 2026-10-07T02:46:06+08:00　
> It hits Paddle's api so it can get complete history of transactions of a customer.

---

> **recon_demon1859**（1 分） · 2026-10-07T09:14:49+08:00　
> The quiet cancel is the part I would watch. If async support lowers ticket volume but increases silent churn, the queue looks better while the plan gets worse. I would separate account-specific billing questions from product support, then track whether each group upgrades, cancels, or needs the same explanation again.

---

> **arslannasir128**（2 分） · 2026-10-07T21:41:57+08:00　
> The repeat is the number I'd watch. Same billing question twice in one cycle means the invoice page failed, and no reply from a human fixes that.

---

> **RajatKhoware**（1 分） · 2026-10-08T02:55:16+08:00　
> Fair push. If half the cheap-tier tickets are 'does this hold for my case' questions, that is a positioning gap, not a support gap. Those people are not confused, they are unconvinced. I would still split them out first, because once you see the real ratio of confused versus unconvinced, the pricing decision makes itself.

---

> **arslannasir128**（1 分） · 2026-10-08T03:08:39+08:00　
> Confused people ask once and move on. Unconvinced people ask the same thing twice and then stop asking at all. That second ask is where I'd draw the line, because it looks like a support ticket and behaves like a sales one.

---

> **RajatKhoware**（1 分） · 2026-10-08T13:01:22+08:00　
> That is a sharper line than mine. The second ask is not a support ticket, it is a buying signal wearing a support ticket's clothes. We started treating repeat questions as objections to close instead of tickets to answer, and the cheap tier stopped looking like a cost center.

---

> **arslannasir128**（1 分） · 2026-10-08T21:31:00+08:00　
> Careful with that one though. I tried reading the repeat ask as an objection and watched my answers get worse.
>
> Once a reply can close something, the short answer stops being about the problem. I keep the two ledgers separate now. Does yours share a queue?

---

> **arslannasir128**（1 分） · 2026-10-09T04:43:10+08:00　
> Live per question kills the stale read. The one I'd still check is the failure path, does the answer wait for Paddle or bail when the call errors?

---

> **RajatKhoware**（1 分） · 2026-10-09T12:56:17+08:00　
> Fair, and that is the failure mode of my line. If the closer starts optimizing the answer for the close instead of the problem, you get worse answers and pushier replies. The fix we landed on: the support person answers the problem fully first, and only then does the objection get logged for sales to work. Read the repeat ask as a signal, but do not let the signal corrupt the answer.

---

> **arslannasir128**（1 分） · 2026-10-10T00:53:18+08:00　
> answering fully first is the right order. the part I'd watch is the log itself.
>
> a rare objection gets worked. when a third of tickets carry one it becomes a queue nobody owns, and the pattern surfaces monthly to the person already inside it.
>
> does that log have an owner?

---

> **RajatKhoware**（1 分） · 2026-10-10T13:58:20+08:00　
> Exactly. The log works at ten tickets a week and dies at a hundred. Our fix: the objection log has an owner and a weekly review, same as the support queue. Patterns get promoted to playbook entries, and the playbook is what the support team actually reads. A log nobody reads is just a second inbox. The review is the product.

---

> **arslannasir128**（1 分） · 2026-10-14T00:57:50+08:00　
> An owner plus a standing slot is the difference between a log and a pile.
>
> The half I'd fight for is what leaves the room. A promoted pattern only pays if it changes what the customer gets, not only what the team knows. Does anything from yours ever go back to the person who raised it?

## 导航

- 项目页：—（本条不是项目，按设计不建实体页）
- 渠道页：[[50-渠道/reddit]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
