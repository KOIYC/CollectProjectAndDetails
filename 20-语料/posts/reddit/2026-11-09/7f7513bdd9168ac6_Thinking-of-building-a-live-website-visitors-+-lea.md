---
type: "corpus"
item_id: "7f7513bdd9168ac6"
title: "Thinking of building a live website visitors + leads tool. Am I wasting my time?"
source: "reddit"
source_name: "Reddit 独立开发版块"
url: "https://www.reddit.com/r/microsaas/comments/1xipzs7/thinking_of_building_a_live_website_visitors/"
author: "RichCar6888"
published_at: "2026-10-30T01:13:15+08:00"
captured_at: "2026-11-09T09:41:03+08:00"
lang: "en"
kind: "post"
topic: "开发者工具"
shard: "2026-11-09"
pub_day: "2026-10-30"
tags:
  - 语料
  - reddit
  - r/microsaas
metrics: {"score": 4, "comments": 12, "upvote_ratio": 1}
comments_count: 8
comments_total: 12
discovered_via: "reddit:14d+settle10"
---

# Thinking of building a live website visitors + leads tool. Am I wasting my time?

> [!info] 一句话导读
> I’m a developer and for the past few weeks I’ve been thinking about building a simple analytics tool. Not another Google Analytics clone.

> [!meta]- 语料信息（点开展开）
> 来源：Reddit 独立开发版块（post）
> 原帖：<https://www.reddit.com/r/microsaas/comments/1xipzs7/thinking_of_building_a_live_website_visitors/>
> 指标：得分=4 · 评论=12 · 赞踩比=1
> 作者：RichCar6888　|　发布：2026-10-30T01:13:15+08:00
> 项目链接：—
> 采集：2026-11-09T09:41:03+08:00　|　id：`7f7513bdd9168ac6`

## 正文

Hey,

I’m a developer and for the past few weeks I’ve been thinking about building a simple analytics tool. Not another Google Analytics clone.

The main idea is:

\* See live visitors on the website in real time (which page they’re on, from where, device etc.)

\* Track their journey across pages

\* Capture form submissions properly with context

\* Send a short daily email summary with what happened + what to do

Targeting mostly small agencies and service businesses who find GA4 too complicated and keep missing leads.

I’m comfortable building it (React + Node), but I’m honestly not sure if people will actually pay for this. There are already tools like Plausible, Clarity, Hotjar etc.

So I wanted to ask:

\* Does this sound useful to you?

\* Would you pay around $25-30/month for something like this?

\* Or is the market already too saturated?

Just looking for honest opinions before I spend months on it.

Thanks.

## 评论（8/12）

> **chaudharyhamza89**（1 分） · 2026-10-30T01:15:03+08:00　
> You are not wasting your time, but the crowded part is generic analytics, not the specific job you described. Small agencies usually do not pay for another dashboard; they pay for missed leads being caught and explained in plain language. The daily email is therefore your strongest feature, because it turns data into one clear next action. Before building for months, I would test it with five agencies using a simple prototype and one question: did the summary change what they did that day? If the answer is yes, $25 to $30 a month is easy to justify; if not, the problem is positioning, not the market.

---

> **cocoabuilder**（1 分） · 2026-10-30T01:16:13+08:00　
> Not a waste of time, but I would narrow it before building for months. Live visitors alone are unlikely to carry $25-30 a month, because that is a nice-to-watch dashboard. The part worth paying for is the missed lead: a form that failed, a visit that reached the contact page and left, or a follow-up that never happened, with the context needed to act on it the same day.
>
> A quick test I would run first: ask five small agencies or service businesses for one lead they know they missed in the last month, and what it would have been worth to catch it. If they cannot name one, the daily summary will be interesting but not urgent. If they can, build that one alert first, and let the live view be the supporting detail rather than the product.

---

> **Tough_Currency224**（1 分） · 2026-10-30T01:23:23+08:00　
> Not a waste of time, but I’d change what you lead with.
>
> Live visitors is fun for a week, then nobody looks at it. Clarity is free and already has that kind of view. What service businesses will pay for is knowing which channel brought in each lead. Form submissions with source, pages viewed and time to convert answer that, and Plausible and Hotjar don’t really.
> The daily email is your best idea. These users won’t log into a dashboard, so the email could be the product.
> Agencies are also the better buyer: one agency with 15 client sites is worth more than 15 site owners.
> Before building, message 15–20 agency owners and ask how they track lead sources today. If the answer is messy, build a 2–3 week MVP (form capture plus the email) and try to get a few of them paying.
>
> “Simpler GA” is crowded. “Shows a service business where its leads come from” isnot.

---

> **Fit-Corner2382**（1 分） · 2026-10-30T01:36:25+08:00　
> Form context is wrong if you record the submit in the browser instead of where the form is accepted.
>
> A blocked page script can keep the live view busy while the accepted lead never shows up, and a client-side listener can turn a failed validation into a lead the daily note says to chase. Price the $25–30 per site rather than per login, or an agency will put every client on one seat and the summary will mix their leads.

---

> **BizAutomationPro**（1 分） · 2026-10-30T01:41:51+08:00　
> The better is to analyze your idea on key parametrs like market trends , pain points , competatitors cost vs your offering, what additional value you are giving which others are not giving

---

> **Lazy-Monk-6778**（1 分） · 2026-10-30T04:05:47+08:00　
> I'd test who can actually buy and deploy this before treating positive agency feedback as demand.
>
> An agency owner liking the idea doesn't mean they can add tracking to client sites, access the form backend or get approval to share lead data. Ask one agency to walk you through the last tool they installed for a client: who approved it, who did the setup, who paid and what happened when something broke. That could change your product scope more than another analytics feature.
>
> Then offer a small paid pilot on one agreed site, with a specific output and an end date. Agree beforehand who reviews the daily summary and what purchase decision follows a useful result. If the agency expects clients to pay, speak with one of those clients too; otherwise you're validating a reseller's enthusiasm rather than the budget holder's need.
>
> A $30 subscription also needs onboarding you can sustain at that price. Record the setup and support time during the pilot before assuming 15 client sites will be better than one.

---

> **Derbier-Ludobzh**（1 分） · 2026-10-30T04:59:39+08:00　
> tbh the hardest part here isn't the build, its distribution. small agencies and local service businesses get pitched software constantly, so before writing any code id figure out how you're actually going to get in front of them

---

> **Julien_tulina_ai**（1 分） · 2026-10-30T19:37:25+08:00　
> Hey, I built GTM systems for a few startups and now [Tulina.ai](http://Tulina.ai)
>
> Our customers are indeed asking for website visitors tracking to outreach afterward.
>
> Though, they don't need real time data. As they build the system to outreach automatically if they are qualified. The thing is they need IP to company or contact information. As most of the value is from leads who don't fill-in forms and are leaving the website.
>
> Some tools are already doing it such as Leadfeeder and Snitcher that we integrated into [tulina.ai](http://tulina.ai)
>
> Feel free to book a call on our website if you want to have a coffee so I can share more insights from what we see on the market.

## 导航

- 项目页：—（本条不是项目，按设计不建实体页）
- 渠道页：[[50-渠道/reddit]]
- 赛道：`开发者工具`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
