---
type: "corpus"
item_id: "383d802841c808e6"
title: "Building a financial data SaaS solo: what I’ve learned turning an internal tool into a paid beta"
source: "reddit"
source_name: "Reddit 独立开发版块"
url: "https://www.reddit.com/r/SaaS/comments/1x73fkl/building_a_financial_data_saas_solo_what_ive/"
project_url: "https://stonkhub.net/"
author: "lockertalk11"
published_at: "2026-10-16T09:31:44+08:00"
captured_at: "2026-10-26T09:43:50+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-10-26"
pub_day: "2026-10-16"
tags:
  - 语料
  - reddit
  - r/SaaS
metrics: {"score": 4, "comments": 13, "upvote_ratio": 1}
comments_count: 12
comments_total: 13
discovered_via: "reddit:14d+settle10"
---

# Building a financial data SaaS solo: what I’ve learned turning an internal tool into a paid beta

> [!info] 一句话导读
> I'm the solo developer behind StonkHub, a market research platform that aggregates public government and market data (congressional stock trades, lobbying, fede…

> [!meta]- 语料信息（点开展开）
> 来源：Reddit 独立开发版块（post）
> 原帖：<https://www.reddit.com/r/SaaS/comments/1x73fkl/building_a_financial_data_saas_solo_what_ive/>
> 指标：得分=4 · 评论=13 · 赞踩比=1
> 作者：lockertalk11　|　发布：2026-10-16T09:31:44+08:00
> 项目链接：<https://stonkhub.net/>
> 采集：2026-10-26T09:43:50+08:00　|　id：`383d802841c808e6`

## 正文

Howdy all,

I'm the solo developer behind StonkHub, a market research platform that aggregates public government and market data (congressional stock trades, lobbying, federal contracts, SEC filings, options positioning) into one dashboard.

It started as a tool I built for my own research. Friends wanted access, then their friends did, and at some point I had to decide whether this was a side project or a product. I went with product, and wanted to share some of the decisions along the way:

* Free tier vs paid: The free account includes all government data and social features. The $25/month beta unlocks the full feature set (GEX, technical screener, full watchlists, full premarket emails). My reasoning was that the government data is the hook and the easiest thing to understand, while the analytics and scanners are what active traders will actually pay for.
* Pricing: I landed on $25/month by working backward from two things. First, cost: every paid user adds load across the data pipeline, Redis cache, MongoDB, and AI summaries, so I needed a price that stays profitable as usage grows. Second, the market: most tools covering just one of these data sets (congressional trades, GEX, or insider filings) charge as much or more on their own, so bundling them at $25 felt like a clear value without undercutting myself. The free tier carries the government data/limited stock detailed views/premarket emails, so people can see the product's value before paying for the analytics.
* Data infrastructure: Data comes from six government sources plus market data providers, all on different refresh cycles. Insider filings update hourly, GEX snapshots every 10 minutes, and the technical screener recomputes nightly. Keeping that pipeline reliable as a solo dev has been the biggest ongoing cost, in both time and money.
* Stack: Vanilla JS + Tailwind frontend with an Express (Node) backend, deployed serverless on Vercel. MongoDB holds users and historical data, Upstash Redis caches everything users hit (TTLs tuned to market hours), and \~25 Vercel cron jobs run the data pipeline. Billing through Stripe, emails through Resend, auth via JWT plus Google/GitHub OAuth, and AI summaries from gpt-4o-mini.

Things I'm still figuring out:

\* Is the free tier too generous, or is it the right top of funnel?

\* How do you price a beta without it feeling like paying to be a tester? Or should I even call it a beta?

\* What's worked for you on distribution when your audience is skeptical of anything finance-related?

Happy to go deeper on any of it. If you want to see the product, it's at https://stonkhub.net.

## 评论（12/13）

> **UpbeatMobile7651**（1 分） · 2026-10-16T09:56:06+08:00　
> the hook model here is solid, government data is like the free sample at costco and the analytics are the bulk pack you actually buy. but re: beta pricing, just call it early access and charge full freight, the word beta makes people think theyre paying to qa your product. and man 25 vercel cron jobs, thats not a pipeline thats a rube goldberg machine, i hope youve got good logging cause 3am solo debugging that sounds like actual hell

---

> **fernandops**（1 分） · 2026-10-16T12:01:49+08:00　
> With those different refresh cycles, show a separate “data as of” time for each section. A dashboard refresh at 10:05 doesn’t mean the nightly screener or the government source changed at 10:05. Also distinguish “checked, no new records” from “the job failed” in your pipeline view.

---

> **RajatKhoware**（0 分） · 2026-10-16T15:43:57+08:00　
> The jump from internal tool to paid product is brutal because your first users were colleagues who had to use it. Paying customers have a choice, and they will find every rough edge your team politely ignored. The solo founders who make it do one thing: talk to 10 strangers before writing another line of code. Internal tools solve your problem; products solve a stranger's problem. Those are different problems. What's the biggest surprise your beta users gave you?

---

> **Glass_Rent8750**（1 分） · 2026-10-16T22:03:33+08:00　
> one thing worth thinking about, $25/mo is fine now but your per-user costs sound like they scale linearly. have you modeled what margins look like at say 500 or 1000 paid users? thats where a lot of data-heavy products hit a wall

---

> **lockertalk11**（1 分） · 2026-10-17T01:13:10+08:00　
> It mathematically works for one person for $25 refreshing all day with in my opinion, generous watchlist caps being the main thing to keep in check. Everything else is on a set timer for market data/filing fetches so that isn't affected by user count whatsoever.
>
> I've got 4 paying subscribers randomly, which I believe are through chatbots after asking them. A few friends use it for free.

---

> **lockertalk11**（1 分） · 2026-10-17T01:14:20+08:00　
> It's been a slow grind over the past 9 months or so...so far so good! But yes, there have certainly been some brutal debugging nights especially towards the beginning of pushing it to a live site.

---

> **lockertalk11**（1 分） · 2026-10-17T01:14:57+08:00　
> Great comms, already have that :)

---

> **wisesheets**（1 分） · 2026-10-17T01:57:04+08:00　
> Free tier sounds right to me, with data products it's usually what gets people to trust your numbers before they pay. Which feature are your paying users actually opening every day?

---

> **lockertalk11**（1 分） · 2026-10-17T02:12:07+08:00　
> Primarily GEX, then second would be the homepage which contains the scanners for SEC, gov, and technicals. Technical table is third which is more data intensive, with 550+ tickers being calculated and refreshed 4x a day.

---

> **lockertalk11**（1 分） · 2026-10-17T02:12:44+08:00　
> I appreciate this…I’ll model it out and see. AI seems to think I’ll be fine but I think otherwise based on the stats so far.

---

> **wisesheets**（1 分） · 2026-10-17T23:29:00+08:00　
> GEX being the main draw makes sense, that's hard to find cheap anywhere else. Refreshing 550+ tickers 4x a day must add up, are you caching between runs?

---

> **lockertalk11**（1 分） · 2026-10-18T02:10:49+08:00　
> GEX only website prices are hilarious to me… it was by far the simplest feature added (other than building out the custom chart and timeline).
>
> Yes, utilizing free plan on redis still but expect to upgrade to pay as you go very soon.

## 关联链接

- https://stonkhub.net.

## 导航

- 项目页：[[10-项目/stonkhub.net_728b6106]]
- 渠道页：[[50-渠道/reddit]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
