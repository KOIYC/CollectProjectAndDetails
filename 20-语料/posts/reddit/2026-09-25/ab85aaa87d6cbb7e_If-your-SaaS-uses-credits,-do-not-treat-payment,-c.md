---
type: "corpus"
item_id: "ab85aaa87d6cbb7e"
title: "If your SaaS uses credits, do not treat payment, credits and invoices as one thing"
source: "reddit"
source_name: "Reddit 独立开发版块"
url: "https://www.reddit.com/r/SaaS/comments/1wgksa9/if_your_saas_uses_credits_do_not_treat_payment/"
author: "rameezdev"
published_at: "2026-09-15T08:16:45+08:00"
captured_at: "2026-09-25T13:43:26+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-25"
pub_day: "2026-09-15"
tags:
  - 语料
  - reddit
  - r/SaaS
metrics: {"score": 6, "comments": 6, "upvote_ratio": 0.8}
comments_count: 9
comments_total: 9
discovered_via: "reddit:14d+settle10"
---

# If your SaaS uses credits, do not treat payment, credits and invoices as one thing

> [!info] 一句话导读
> If your SaaS already has paying customers, this is one thing I would be very careful about.

> [!meta]- 语料信息（点开展开）
> 来源：Reddit 独立开发版块（post）
> 原帖：<https://www.reddit.com/r/SaaS/comments/1wgksa9/if_your_saas_uses_credits_do_not_treat_payment/>
> 指标：得分=6 · 评论=6 · 赞踩比=0.8
> 作者：rameezdev　|　发布：2026-09-15T08:16:45+08:00
> 项目链接：—
> 采集：2026-09-25T13:43:26+08:00　|　id：`ab85aaa87d6cbb7e`

## 正文

If your SaaS already has paying customers, this is one thing I would be very careful about.

A payment system is not just a payment gateway.

In many SaaS products, especially usage-based products, the customer does not directly pay for one action every time. They buy credits, balance, tokens or some kind of internal value first. Then the product consumes that balance when they use a service.

At the start, this looks simple.

Customer pays money.
Credits are added.
Invoice is created.
Customer uses the product.

But once the product grows, this simple flow becomes risky if everything is treated as one process.

I think payments, credits and invoices should be connected, but they should not be the same thing.

Payment should answer one question:

Did we actually receive the money?

Credits should answer another question:

What value did the customer receive inside the product?

Invoice should answer another question:

What financial document needs to be created for accounting?

These three things can happen close together, but they can also fail separately.

For example, if the payment is successful but the invoicing provider is down, the customer should not lose the credits they already paid for. The invoice job can be retried later. The payment should not be processed again.

The same thing applies to duplicate callbacks. Payment providers can send the same event more than once. If your system simply says “callback received, add credits,” you can accidentally give the same credits twice.

So the system needs to record that this payment attempt or transaction has already been processed. After that, repeated callbacks should not create another credit grant.

Another important thing is pricing.

Do not assume that credits always have one fixed price forever.

If your SaaS has different plans, regions, portals, customer groups, discounts or old pricing, then “100 credits” may not always mean the same amount of money.

That is why the historical amount paid should be stored with the credit purchase. Reports should not calculate old revenue using today’s pricing. Today’s price is not always the truth about yesterday’s transaction.

At small scale, people can hold these things together manually. Someone can create invoices, check payments, fix balances and answer customer questions.

But when the product grows, this manual work becomes a hidden operational risk.

A person can miss an invoice.
A payment can be recorded but credits not added.
Credits can be added twice.
A refund can happen but the internal balance is not adjusted.
A customer can ask what happened and nobody has a clear history.

The real problem is not only automation.

The real problem is traceability.

When money enters the system, the SaaS should know what happened, what was given to the customer, what invoice was created, what failed, what was retried and what is still pending.

I think this is where many SaaS products start feeling fragile. Not because the main product idea is bad, but because the business workflow behind it is not designed like a real system.

For founders who already have paying SaaS customers, I would look at this before it becomes painful:

Can one successful payment ever add credits twice?

Can invoice failure block a customer from using what they paid for?

Can you explain why a customer balance changed?

Can you recreate the history of a payment, credit grant, invoice and refund?

Can your team safely retry failed work without repeating successful work?

If the answer is unclear, the payment system may be working only because the volume is still small.

That is usually the stage where it is worth fixing the architecture before growth makes every mistake more expensive.

## 评论（9/9）

> **Slight_Guest3459**（0 分） · 2026-09-15T08:29:38+08:00　
> Strong distinction. One thing I’d add is making the credit grant an immutable ledger entry keyed to the provider event or transaction, while the displayed balance is a projection. Refunds and chargebacks can then create compensating entries instead of editing history. Keep invoice state and entitlement state separate too; support can answer “what happened?” from the ledger even when webhooks arrive out of order. Idempotency keys help, but an audit trail plus a reconciliation job is what catches cases where the provider and app disagree.

---

> **rameezdev**（0 分） · 2026-09-15T08:32:03+08:00　
> Yes, I agree with this.
>
> The balance should not really be treated as the source of truth. The source of truth should be the credit movements behind it.
>
> A successful payment creates a credit grant. A refund or chargeback should create another entry that reverses or adjusts the entitlement, not silently edit the old record. Otherwise after a few months nobody can explain why the balance changed.
>
> The point about invoice state and entitlement state being separate is also important. A customer can be entitled to use the product even if invoice generation is pending or failed. Support should be able to see that clearly instead of guessing from one final balance number.
>
> Idempotency protects one part of the problem, especially duplicate callbacks. But it does not replace audit history or reconciliation. You still need a way to compare what the provider says happened with what the application believes happened.
>
> That is the difference between “we added credits after payment” and “we can explain the whole lifecycle of this transaction.”

---

> **Which-Examination-74**（1 分） · 2026-09-15T16:03:21+08:00　
> Idempotency keys, a ledger and a reconciliation job all assume the event actually came from the provider. We audited the Polar webhooks across five small products of our own in August, and all five granted paid entitlement from an attacker-controlled metadata.user_id in the request body. Our bugs, not the provider's, and every one of them looked finished. One had a real HMAC helper that nothing ever called. It hashed the body alone as hex, while Polar signs id.timestamp.body as base64, so it couldn't have matched even if it had been called. Two others checked only that a signature header was present and a secret was set, under a comment reading "TODO: Implement proper HMAC". We fixed it with a Standard Webhooks verifier: timingSafeEqual, a five-minute timestamp window, and verification before JSON.parse. A forged POST returns 401 now, a correctly signed one 200. If an unverified POST can mint a credit grant, the ledger records the fraud faithfully and the reconciliation job has nothing to disagree with, because the provider never sent anything. Five products of ours isn't a large payment operation, so take the sample for what it is.

---

> **rameezdev**（1 分） · 2026-09-15T16:37:50+08:00　
> Yes, this is a very good point.
>
> What I wrote assumes the event has already passed the trust boundary. But before idempotency, ledger entries or reconciliation even matter, the webhook itself has to be verified properly.
>
> If an attacker can send a fake POST and the app accepts it as a real payment event, then the rest of the system can behave perfectly and still do the wrong thing. It will create a clean ledger entry for something that never happened.
>
> So the order should probably be:
>
> Verify the webhook signature and timestamp first.
> Only then parse and trust the event.
> Then apply idempotency.
> Then create the credit grant / entitlement entry.
> Then let invoice and reconciliation jobs run separately.
>
> The point about having an HMAC helper that is not actually called is also painfully real. A system can look secure in the codebase because the helper exists, but the actual execution path may never use it.
>
> I also like the phrase “the ledger records the fraud faithfully.” That is exactly the danger. A ledger gives traceability, but it does not prove the input was legitimate.
>
> So yes, webhook verification is the first gate. Idempotency and reconciliation are not a replacement for that.

---

> **Which-Examination-74**（1 分） · 2026-09-15T17:11:03+08:00　
> The trap in step two is the body. Polar signs id.timestamp.body, so the HMAC covers the exact bytes that arrived, and the raw string is the only thing you can verify against. If the framework parsed the body before your handler ran, those bytes are gone. Re-serialising the parsed object won't reliably reproduce them: key order, whitespace and unicode escaping can all move. What worked for us was carrying the raw body through as a string, verifying against that, 401 on failure, JSON.parse only after it passed.

---

> **rameezdev**（1 分） · 2026-09-15T17:13:49+08:00　
> He is correct. This is an important implementation detail, not just theory. The clean reply is to agree and add that this is where many webhook implementations quietly fail.
>
> Yes, that makes sense.
>
> The important detail is that you are not verifying the “meaning” of the JSON. You are verifying the exact bytes the provider signed.
>
> Once the framework has parsed the request body, you may still have the same data logically, but not the same body. Re-serialising it can change key order, whitespace or escaping, so the signature check becomes unreliable or gives a false sense of security.
>
> So the safe flow is:
>
> Keep the raw request body.
> Build the signed payload exactly the way the provider expects.
> Verify signature and timestamp against that raw body.
> Reject with 401 if it fails.
> Only then parse JSON and process the event.
>
> This is one of those small implementation details that decides whether the whole payment flow is actually secure or only looks secure in the code.

---

> **Apurv_Bansal**（2 分） · 2026-09-21T19:04:33+08:00　
> One gap in this that bites people later: what happens to already-spent credits when the underlying payment gets refunded or charged back months after the fact. If credits are just a balance, you can end up trying to claw back value the customer already consumed, which turns into a support problem, not a billing one. Treating credit consumption as its own ledger entry, separate from the payment event, at least lets you show exactly what was spent before you decide whether to claw anything back.

---

> **AutoModerator**（1 分） · 2026-09-22T05:14:04+08:00　
> Low-Effort/AI content is auto-removed.
>
> *I am a bot, and this action was performed automatically. Please [contact the moderators of this subreddit](/message/compose/?to=/r/SaaS) if you have any questions or concerns.*

---

> **rameezdev**（1 分） · 2026-09-22T05:15:42+08:00　
> That refund/chargeback issue is where simple balance columns completely break down.
>
> If you just decrement a single \`credits\` integer in a database table, a refund 60 days later forces you into a weird spot. You either drive their balance into negative numbers, or you try to wipe credits they already spent. Neither makes sense.
>
> The way I handle this is by treating credits as an event log rather than a single number.
>
> When a user buys credits, that batch gets logged as a distinct transaction. As they use the app, usage events deduct from that specific batch.
>
> If a chargeback happens later:
>
> 1. The system checks how many credits from that original batch are actually left.
>
> 2. If there are unused credits left, it cancels them.
>
> 3. If they already spent those credits, the unspent balance is zero. The system just logs a chargeback flag on the account and pauses access instead of trying to manipulate past usage.
>
> That way, your support team or database logs show the exact reality: money came in, value was consumed, money was refunded, and $0 balance remains. You don't end up with weird negative numbers or broken historical reporting.
>
> Are you running credits as a single balance column right now, or logging individual credit transactions?

## 导航

- 项目页：—（本条不是项目，按设计不建实体页）
- 渠道页：[[50-渠道/reddit]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
