---
type: "corpus"
item_id: "2889c4fd8057a258"
title: "My Stripe webhook trusted an older event over the customer's actual subscription state"
source: "reddit"
source_name: "Reddit 独立开发版块"
url: "https://www.reddit.com/r/microsaas/comments/1xjxdmp/my_stripe_webhook_trusted_an_older_event_over_the/"
project_url: "https://andrady.co/"
author: "Pale_Ferret_8241"
published_at: "2026-10-31T09:26:16+08:00"
captured_at: "2026-11-10T09:52:11+08:00"
lang: "en"
kind: "post"
topic: "开发者工具"
shard: "2026-11-10"
pub_day: "2026-10-31"
tags:
  - 语料
  - reddit
  - r/microsaas
metrics: {"score": 3, "comments": 20, "upvote_ratio": 1}
comments_count: 14
comments_total: 20
discovered_via: "reddit:14d+settle10"
---

# My Stripe webhook trusted an older event over the customer's actual subscription state

> [!info] 一句话导读
> I've been building a multi-tenant SaaS starter using Next.js, Supabase and Stripe. Initially, most of my attention went into getting the features working: authe…

> [!meta]- 语料信息（点开展开）
> 来源：Reddit 独立开发版块（post）
> 原帖：<https://www.reddit.com/r/microsaas/comments/1xjxdmp/my_stripe_webhook_trusted_an_older_event_over_the/>
> 指标：得分=3 · 评论=20 · 赞踩比=1
> 作者：Pale_Ferret_8241　|　发布：2026-10-31T09:26:16+08:00
> 项目链接：<https://andrady.co/>
> 采集：2026-11-10T09:52:11+08:00　|　id：`2889c4fd8057a258`

## 正文

I've been building a multi-tenant SaaS starter using Next.js, Supabase and Stripe. Initially, most of my attention went into getting the features working: authentication, organisations, roles, billing, API keys and usage limits. Everything appeared to work during normal usage. But when I started testing what would happen if someone deliberately tried to break things, I found four issues I hadn't caught during development. Here's what I found.
1. A privileged database function bypassed the protection I expected from RLS I had a SECURITY DEFINER function involved in a write operation. Because it executed with elevated privileges, I couldn't rely on the table's RLS policies alone. The function needed to independently validate the authenticated user's organisation membership. What I learned: Enabling RLS doesn't automatically protect every database operation. Privileged functions need their own authorization checks.
2. Stripe events arrived out of order My webhook handling wasn't adequately accounting for events arriving in an unexpected sequence. An older event could overwrite a newer subscription state. What I learned: Successfully processing a webhook doesn't guarantee that your billing state is correct. You have to account for retries, duplicate events and event ordering.
3. Webhook retries caused problems I found an issue in how webhook retries and idempotency were handled. A webhook handler needs to be safe when the same event is delivered more than once. Otherwise, retries can leave application state inconsistent.
4. Subscription data could be manipulated through an unsafe write path I found a subscription write path that trusted client-controlled data when it should have been protected. Subscription entitlements should be controlled by trusted server-side logic, not arbitrary client updates. What I changed Rather than just fixing these four individual bugs, I built a hardening suite around them. It now contains nine executable test files running against a real PostgreSQL database, covering: Cross-tenant isolation SECURITY DEFINER boundaries RBAC privilege escalation Anonymous authentication boundaries Invitation lifecycle Stripe webhook reliability Data integrity API key validation Billing enforcement I also integrated the suite into CI so these checks run during development instead of relying on me to remember every edge case manually. This work is part of B2B SaaS OS, the Next.js + Supabase starter kit I've been building.
I've documented the individual bugs, root causes and fixes here: [https://www.andrady.co/postmortems](https://www.andrady.co/postmortems)
The project itself is here: [https://www.andrady.co](https://www.andrady.co)
 My biggest takeaway Testing whether your application works and testing whether someone can make it behave in a way you didn't intend are two very different things. I spent a lot of time building features. I probably should have spent more time trying to break them. cause if i can break it so can you

## 评论（14/20）

> **Spiritual-Relation97**（0 分） · 2026-10-31T09:30:25+08:00　
> Always re-fetch the subscription from Stripe instead of trusting the webhook payload. Event order will bite EVERYONE eventually

---

> **Pale_Ferret_8241**（1 分） · 2026-10-31T09:32:49+08:00　
> That's a good point. The webhook payload tells you what happened, but it doesn't guarantee it's the latest subscription state by the time you process it. Re-fetching from Stripe gives you the current source of truth. I'd still want to guard against concurrent handlers writing stale results, though. Do you re-fetch on every subscription event?

---

> **AssignmentRegular611**（1 分） · 2026-10-31T10:04:28+08:00　
> Ordering is downstream of the real mistake, which is writing subscription state straight out of the event payload. Pull the subscription from the API in the handler and retries and duplicates stop being interesting.

---

> **Similar_Anteater2568**（1 分） · 2026-10-31T11:52:27+08:00　
> Stripe sending events out of order, shocking.

---

> **gamey-opts**（0 分） · 2026-10-31T14:33:31+08:00　
> the SECURITY DEFINER one bites a lot of supabase projects. besides checking membership inside the function, pin the search\_path on it (set search\_path = '' and schema-qualify everything), otherwise anyone who can create objects in a schema on the path can shadow something you call. and revoke execute from public and anon. postgres grants execute to public by default and supabase exposes functions in the public schema over the api, so they're callable straight from the client unless you lock that down.

---

> **unicornshedsocial**（1 分） · 2026-10-31T16:15:10+08:00　
> The simplest fix for ordering is to stop trusting the event payload for state: on any subscription event, re-fetch the subscription from Stripe and write what the API returns now, so a late `customer.subscription.updated` can't roll you back. Keep `event.id` in a unique index for idempotency, and if you do write from the payload, compare `event.created` against the last processed timestamp for that subscription and drop anything older. Worth testing by delivering the events in reverse order.

---

> **VigiliaFounder**（1 分） · 2026-10-31T16:37:40+08:00　
> Thanks for writing these up! Point 2 is one a lot of people only find out about when a customer asks why their plan looks wrong.
>
> For anyone reading who is in that spot, it helps to also watch what happens in production after the tests pass. I've built [Vigilia](https://getvigilia.com/?utm_source=reddit&utm_medium=social&utm_campaign=reddit-1xjxdmp) for this. It watches your live app, alerts you when a request fails and explains each error in plain English, with the evidence and how often it happened. Backend errors like a failing webhook are covered on Pro.
>
> Then hand the fix prompt to Claude, or just connect the MCP server.
>
> Let me know if this helps!

---

> **Pale_Ferret_8241**（1 分） · 2026-10-31T20:32:17+08:00　
> That's a fair distinction. The webhook should be treated as a signal that something changed, not necessarily as the latest source of truth. Re-fetching the current subscription from Stripe helps prevent a delayed event from rolling your local state backwards. That's an important case to cover in webhook regression tests.

---

> **Pale_Ferret_8241**（1 分） · 2026-10-31T20:32:41+08:00　
> Yeah, it sounds obvious in hindsight. The tricky part is that each webhook can be perfectly valid on its own. It's the order they arrive in that can quietly mess up your subscription state.

---

> **Pale_Ferret_8241**（1 分） · 2026-10-31T20:32:56+08:00　
> Good catch. Membership validation is only one part of securing a SECURITY DEFINER function. Pinning the search\_path (or using an empty path with schema-qualified references) and explicitly restricting EXECUTE privileges to the intended roles matter too. That's why I started testing the function itself as a separate security boundary instead of relying on table RLS alone.

---

> **Pale_Ferret_8241**（1 分） · 2026-10-31T20:33:12+08:00　
> Agreed. Treating the webhook as a trigger to reconcile state rather than blindly trusting its payload is an important distinction. The unique event ID constraint also matters for duplicate delivery. I like the reverse-order delivery test because it reproduces the actual failure much more clearly.

---

> **Pale_Ferret_8241**（2 分） · 2026-10-31T20:33:23+08:00　
> That's a good point. Automated tests catch known failure modes, but production monitoring is still important once real traffic and webhook deliveries hit the application. For Stripe failures, does Vigilia capture the event ID and delivery attempt details too? That context would be useful when debugging webhook issues.

---

> **VigiliaFounder**（1 分） · 2026-10-31T20:38:37+08:00　
> Yes, if you install the server side monitoring you will get those details. For a quick integration, first try the free monitoring on the first app which catches frontend errors.
> That's the easiest to start with.
>
> Give it a try and let me know:) I'm constantly adding more capabilities so anything you feel is missing will be a great feedback.
>
> Cheers!

---

> **Awedesk**（1 分） · 2026-11-04T01:21:05+08:00　
> I'd re-fetch in a reconciliation worker with one active job per subscription. Otherwise A can fetch an older state, B fetch a newer one, and A commit last.
>
> Persist and coalesce the work, acquire a nonblocking per-subscription claim before fetching, then commit only if that claim is still current. Keep the database transaction short and outside the API call. Use a lease token/version check so an expired worker cannot overwrite its replacement. If another event arrives during the run, schedule another pass, with bounded retries and backoff. Event-ID deduplication is separate.
>
> Also, [Stripe explicitly warns](https://docs.stripe.com/webhooks#event-ordering) that distinct events can share an `event.created` timestamp, so it should not determine event order. I'd test two handlers deliberately committing in the opposite order to their fetches.

## 关联链接

- https://www.andrady.co
- https://www.andrady.co/postmortems

## 导航

- 项目页：[[10-项目/andrady.co_01d3d797]]
- 渠道页：[[50-渠道/reddit]]
- 赛道：`开发者工具`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
