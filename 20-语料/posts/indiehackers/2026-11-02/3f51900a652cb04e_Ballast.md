---
type: "corpus"
item_id: "3f51900a652cb04e"
title: "Ballast"
source: "indiehackers"
source_name: "Indie Hackers 产品库"
url: "https://www.indiehackers.com/product/ballast"
captured_at: "2026-11-02T09:41:05+08:00"
lang: "en"
kind: "project"
topic: "AI 工具/Agent"
shard: "2026-11-02"
tags:
  - 语料
  - indiehackers
metrics: {}
comments_count: 0
comments_total: 0
discovered_via: "ih:products"
---

# Ballast

> [!info] 一句话导读
> Home Starting Up Case Studies DB Products Ideas DB Vibe Coding Tools Subscribe to IH+

> [!meta]- 语料信息（点开展开）
> 来源：Indie Hackers 产品库（project）
> 原帖：<https://www.indiehackers.com/product/ballast>
> 指标：—
> 作者：—　|　发布：—
> 项目链接：—
> 采集：2026-11-02T09:41:05+08:00　|　id：`3f51900a652cb04e`

## 正文

Home Starting Up Case Studies DB Products Ideas DB Vibe Coding Tools Subscribe to IH+
Starting Up Case Studies
 Ideas DB Products DB Sign in Join
Ballast
 Run cold email up to 80% cheaper than Instantly
Visit Website
Ballast Run cold email up to 80% cheaper than Instantly
 Posts 3
 Website Twitter
November 1, 2026
 Cold email isn't broken, but the stored contact billing model is. Here is why.
I've spent the last 13 years working in email infrastructure and deliverability.
 If you look at the current market for cold outreach tools (Instantly, Smartlead, Lemlist), there is a recurring pricing pattern: they charge you based on the number of contacts stored in your database.
 This works fine for a 1-week pilot. But as you scale, it becomes a nightmare.
 You pay to store 50k leads, even if 40k of them are cold, archived, or already replied. It’s essentially a monthly tax on your own lead pipeline.
 After building and selling other SaaS tools, I decided to build Ballast to fix this specific unit economics problem for myself.
 My thesis for building this:
 1. Database rows should not be a revenue driver.
 Storing 100k email addresses in a PostgreSQL table costs fractions of a cent per month. When we built Ballast, we made stored contacts and mailboxes unlimited on every plan. You pay for what you actually push through the SMTP gateway.
 2. Deliverability is infrastructure, not just a dashboard.
 The biggest mistake I see founders make is assuming a platform handles the "hard parts" of deliverability. They treat sending like a simple API call, ignore SMTP handshake latency, and get blacklisted in days. We built automated "circuit breakers" into the engine: if bounce rates cross 3%, the campaign auto-pauses.
 3. Move the workflow to where the developer lives.
 I’m tired of babysitting SaaS dashboards. We built a native MCP server so you can stage campaigns, check lead health, and review drafts directly from Cursor or Claude. You keep the human-in-the-loop, but you don't waste time clicking around a UI.
 The takeaway
 We are currently competing with giants by offering a "send-based" pricing model instead of a "storage-based" one.
 I have a question for other bootstrappers here:
 How do you decide between charging for storage/database size vs actual utility/usage ? Have you found that usage-based pricing leads to lower churn, or does it make your MRR too unpredictable to forecast?
 Would love to hear how you approached pricing for your own tools.
Alex
13 Upvotes
Comment
October 26, 2026
 The Uploaded Contacts trap: Why we charge for emails sent instead of contacts stored
If you've ever used tools like Instantly, Smartlead, or Lemlist, you’ve probably noticed how their pricing tiers work:
 They charge you based on uploaded / stored contacts .
 Want to store 25,000 leads? That’s $94 to $97 every single month.
 Scale to 100,000 leads? You’re quickly paying $200–$300+/month.
 The kicker? If 15,000 of those contacts are dormant, waiting for a future campaign, or have already replied, you’re still paying for them every single billing cycle.
 I’ve spent 13 years working in email infrastructure and deliverability. When you look under the hood at actual server costs, storing contact rows in a PostgreSQL database costs fractions of a cent per year. What actually costs compute and infrastructure is sending, routing through dedicated egress relays, and warmup handling.
 Charging founders for contacts sitting idle in a table is basically a tax on your own database.
 When we started building Ballast (our cold email platform), we decided to flip the pricing model on its head:
 - Unlimited stored contacts & mailboxes across every plan.
 - Pay strictly for what you send (e.g., $19/mo for 20,000 sends).
 - If your campaign is paused or you’re doing list maintenance, your bill doesn't balloon just because leads are sitting in your workspace.
 We took the same thesis that Marc Lou argued for newsletters with MailCheap and applied it directly to outbound B2B infrastructure.
 The question for other bootstrappers:
 How did you decide between charging for storage vs usage/utility in your SaaS?
 Did moving to usage-based pricing hurt your MRR predictability, or did it lower churn because customers didn't feel penalized during slow months? Would love to hear how you approached it.
Alex
1 Upvote
Comment
October 24, 2026
 The cheap plan in cold email is a trap. Why I built an alternative that charges for sends, not seats.
A few months ago, I was helping set up an outbound pipeline.
 We picked one of the popular cold email platforms (Instantly/Smartlead/Lemlist) because the landing page promised a reasonable entry price around $35 a month.
 Then reality hit.
 First, we wanted to separate campaigns for a couple of projects, which meant paying extra for "client workspaces". Then contact limits capped how many leads we could keep in the system. By the time we unlocked a shared unibox and connected twenty mailboxes to spread sending volume safely, the bill was well over $300 a month.
 It hit me how backwards the monetization in this industry has become:
 Your emails do not leave from the platform's servers. They leave from your own Google Workspace, Microsoft 365, or custom SMTP mailboxes. The marginal compute cost for a platform to schedule an email from mailbox #1 versus mailbox #15 is virtually zero.
 Charging teams per seat or per connected mailbox is just artificial rent-seeking on people trying to send email the safe way.
 So I spent the last few months building an alternative: Ballast .
 The premise is straightforward: you pay strictly for the emails you actually send. Everything else is unbundled and unlimited on every plan:
 Unlimited mailboxes (Google, Outlook, custom SMTP)
Free built-in warmup that never eats into your monthly sending quota
Unified inbox (Unibox) included on every tier
Automated circuit breakers (if bounce rate crosses 5%, campaigns pause before domains get burned)
Built-in MCP server so you can check domains and trigger drafts directly from Claude or Cursor
The math comparison:
 Solo (5k emails): $19/mo on Ballast vs $37 on Instantly
Team (50k emails): $39/mo on Ballast vs $97 on Instantly
Agency (150k emails, 5 clients): $79/mo on Ballast vs $358 on Instantly
I launched it quietly this week. Still early, but the core engine and deliverability guardrails are rock solid.
 For anyone running outbound campaigns: what is the most annoying hidden paywall you have run into with your current stack?
Alex
5 Upvotes
Comment
About
 Cold email tools turn $30 plans into $300 with seat taxes and contact caps. Ballast fixes this: pay strictly for emails sent, with unlimited mailboxes, built-in domain safeguards, and zero hidden feature paywalls.
People
 Alex Founder
Stay informed as an indie hacker.
 Market insights that help you start and grow your business.
Subscribe
Follow @IndieHackers on X for stories and insights about founders building profitable online businesses, and to connect with others in the Indie Hackers community.
 © Indie Hackers, Inc. · FAQ · Terms · Privacy · Cookie Policy ·
Community
 Top Today Top This Week Top This Month Join
Products
 All Products Highest Revenue Add Yours
Databases
 Ideas Products Stories

## 导航

- 项目页：[[10-项目/Ballast_3f51900a]]
- 渠道页：[[50-渠道/indiehackers]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
