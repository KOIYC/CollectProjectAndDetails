---
type: "corpus"
item_id: "cb6571118e375415"
title: "I built and launched a SaaS for comic collectors as a solo developer. The hardest part wasn’t the AI."
source: "reddit"
source_name: "Reddit 独立开发版块"
url: "https://www.reddit.com/r/SaaS/comments/1wuitnc/i_built_and_launched_a_saas_for_comic_collectors/"
author: "SnooRevelations3503"
published_at: "2026-10-01T06:29:51+08:00"
captured_at: "2026-10-11T09:45:30+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-10-11"
pub_day: "2026-10-01"
tags:
  - 语料
  - reddit
  - r/SaaS
metrics: {"score": 4, "comments": 14, "upvote_ratio": 0.84}
comments_count: 13
comments_total: 14
discovered_via: "reddit:14d+settle10"
---

# I built and launched a SaaS for comic collectors as a solo developer. The hardest part wasn’t the AI.

> [!info] 一句话导读
> I’m a lifelong collector of comics, and I was really unhappy with the apps being offered to collectors (the latest ones are actually from marketplaces that want…

> [!meta]- 语料信息（点开展开）
> 来源：Reddit 独立开发版块（post）
> 原帖：<https://www.reddit.com/r/SaaS/comments/1wuitnc/i_built_and_launched_a_saas_for_comic_collectors/>
> 指标：得分=4 · 评论=14 · 赞踩比=0.84
> 作者：SnooRevelations3503　|　发布：2026-10-01T06:29:51+08:00
> 项目链接：—
> 采集：2026-10-11T09:45:30+08:00　|　id：`cb6571118e375415`

## 正文

I’m a lifelong collector of comics, and I was really unhappy with the apps being offered to collectors (the latest ones are actually from marketplaces that want to track what people own), So, managing a serious collection had become really fragmented.

Cataloguing in one place.
Market research through Google.
Spreadsheets for tracking.
Price guides for values.
Marketplace searches when I wanted actual comparable sales.

I wanted one mobile app that could make all of that feel simple.

So I built ComiCollector.

I started thinking that I could lean on AI to help out and keep things simple.

But I massively underestimated how complicated “simple” would become. AI isn't ready for these types of complex tasks. I could go on for hours about just how bad it is, but it forced me to leverage deterministic programming as the real bedrock for the application. Deterministic rules, structured data, market evidence, filtering, caching, validation and a lot of guardrails.

The principle became:

**AI can help interpret the market. It doesn’t get to invent the market.**

That changed the architecture of the entire product.

The backend eventually grew into market-assessment pipelines, reusable market intelligence, background refresh workers, subscriptions and usage limits, a production database, blue/green deployment, and infrastructure designed with a path to load balancing and AWS/Kubernetes if usage eventually justifies it.

So, what started as a simple project to make a pretty interface for comic books turned into a project that dragged on for well over a year and has become a technical behemoth.

For other SaaS founders, especially solo builders, I’m curious:

**At what point did your “simple product” turn into a much bigger system than you originally expected?**

And did that complexity ultimately become part of your moat, or just something you had to keep fighting? I'd be really interested in hearing about your journey.

## 评论（13/14）

> **UpperWorld11**（0 分） · 2026-10-01T06:31:28+08:00　
> Your price guide and your refresh workers are the same product, and that's where the year went. A guide fed by asking prices drifts up forever, since nobody delists a book they think is worth 300. Sold comps are the input that can't lie, so the pipeline keeping them fresh is the only part a competitor can't copy in a weekend. Are yours reading sold prices or listings?

---

> **Predream1**（0 分） · 2026-10-01T06:31:39+08:00　
> A comic's price has a shelf life, so every screen that shows one needs a refresh path and a rule for what to do when no comps turn up. Cataloging stays easy. Valuation is a pipeline you never stop feeding, which is what yours turned into. Where do the comps come from now, actual sold listings or asking prices?

---

> **SnooRevelations3503**（1 分） · 2026-10-01T06:38:24+08:00　
> Both actually. The real way to keep a tab on upward momentum is to monitor sales. So, we've incorporated them both into the app's assessment system.

---

> **SnooRevelations3503**（1 分） · 2026-10-01T06:39:31+08:00　
> Second question on the same topic. I'm not giving up my bag of tricks. But we track both. The database already has more than 200,000 comps and is growing as people continue to assess their books.

---

> **pAlelane02**（1 分） · 2026-10-01T08:14:25+08:00　
> a year of solo building on a niche vertical is a big bet. whats your distribution plan look like? the build is one thing but getting collectors to actually switch from their current fragmented workflow is usually the harder problem

---

> **SnooRevelations3503**（1 分） · 2026-10-01T09:36:48+08:00　
> Well ... it's on both app stores. So, I'm distributing through that. But, you're right the challenge is in getting them to consider ditching the way they've been doing things for a better way (welcome to 2026!). Whether you wondering what that stack is worth that you have in your garage or your walking through the aisles of a Con, having live market insights/data/pricing in your pocket is a pretty powerful selling point. I've yet to meet a collector that thinks otherwise. ... being able to sell with 1 click on eBay is a big plus too (the app even fills in the listing details so you don't need to). Anyways ... onwards.

---

> **AutoModerator**（1 分） · 2026-10-01T09:50:20+08:00　
> Low-Effort/AI content is auto-removed.
>
> *I am a bot, and this action was performed automatically. Please [contact the moderators of this subreddit](/message/compose/?to=/r/SaaS) if you have any questions or concerns.*

---

> **SnooRevelations3503**（1 分） · 2026-10-01T09:52:17+08:00　
> https://preview.redd.it/fh1grpmohrsh1.png?width=1170&format=png&auto=webp&s=7093af04a5bbc40f6af107d6304c1c8164db66eb
>
> This is the bottom half of the Market Insight Note that we create with every book you assess. Average time is 30 seconds to get a result. But, as more people use the app, that will drop. We've seen some come back in less than 5 seconds.

---

> **Predream1**（1 分） · 2026-10-01T19:22:39+08:00　
> 200k comps sounds like plenty until you filter down to one book. Most issues have no sale in the last year, so the useful output is a range plus how thin the evidence is, not one confident number. Collectors screenshot the confident number when it turns out wrong.

---

> **SnooRevelations3503**（1 分） · 2026-10-01T21:21:58+08:00　
> We've got this under control. But, thanks.

---

> **UpperWorld11**（1 分） · 2026-10-01T21:42:28+08:00　
> Blending them only helps if each listing drops out of the estimate as soon as it sells or goes stale. One that has sat for sixty days is an ask nobody accepted, and it keeps dragging up the value of everything comparable. A sold price should replace it outright.

---

> **SnooRevelations3503**（1 分） · 2026-10-01T22:15:47+08:00　
> You're point is valid. But, there are ways to incorporate it (guards, blends, stale weighting). My app isn't using some crappy system of averages. It's based on actuarial science (seriously, two actuaries have been avid contributors). There are similarities to insurance industry models.

---

> **UpperWorld11**（1 分） · 2026-10-01T22:41:10+08:00　
> Actuarial is a stronger frame than averaging, and what decides the output is what happens to the silent cases. A listing pulled after sixty days and a book that hasn't sold in a year both ended without a sale, so they are censored observations, not prices. Do you decay them out of the pool over time?

## 导航

- 项目页：[[10-项目/I-built-and-launched-a-SaaS-for-comic-collectors_cb657111]]
- 渠道页：[[50-渠道/reddit]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
