---
type: "corpus"
item_id: "e3a37d55b3475f58"
title: "I built a personal dashboard that pulls my money, running, journal and reading into one place"
source: "reddit"
source_name: "Reddit 独立开发版块"
url: "https://www.reddit.com/r/SideProject/comments/1xept54/i_built_a_personal_dashboard_that_pulls_my_money/"
author: "ZebrafishWrangler"
published_at: "2026-10-25T09:45:05+08:00"
captured_at: "2026-11-04T09:52:43+08:00"
lang: "en"
kind: "post"
topic: "开发者工具"
shard: "2026-11-04"
pub_day: "2026-10-25"
tags:
  - 语料
  - reddit
  - r/SideProject
metrics: {"score": 13, "comments": 18, "upvote_ratio": 1}
comments_count: 14
comments_total: 18
discovered_via: "reddit:14d+settle10"
---

# I built a personal dashboard that pulls my money, running, journal and reading into one place

> [!info] 一句话导读
> For the last little while I've been building a self-hosted dashboard that runs on my laptop. It's a Flask (Python) backend with a React/Vite frontend. There are…

> [!meta]- 语料信息（点开展开）
> 来源：Reddit 独立开发版块（post）
> 原帖：<https://www.reddit.com/r/SideProject/comments/1xept54/i_built_a_personal_dashboard_that_pulls_my_money/>
> 指标：得分=13 · 评论=18 · 赞踩比=1
> 作者：ZebrafishWrangler　|　发布：2026-10-25T09:45:05+08:00
> 项目链接：—
> 采集：2026-11-04T09:52:43+08:00　|　id：`e3a37d55b3475f58`

## 正文

For the last little while I've been building a self-hosted dashboard that runs on my laptop. It's a Flask (Python) backend with a React/Vite frontend. There are five sections:

1. Home (a one-screen summary of my week)

2. Financials

3. Running

4. Journal

5. Books

Everything runs locally, and there's no cloud service (yet), and the data is plain CSV and JSON files I own. (The screenshots use made-up data)

Where the data comes from:

* Money: my bank and credit card PDF statements fill in historic data back to 2015, parsed into transactions, plus Plaid runs to keep accounts synced day to day. For Plaid I signed up for my own developer account and connected my accounts to it, so no third-party budgeting app sits in between. A small scikit-learn model and some keyword rules sort transactions into categories. On top of that sit monthly budgets with a "free to spend" number, automatic subscription detection, savings goals, retirement balances and a loan/debt payoff tracker.
* Running: synced from Garmin Connect (runs, routes, HRV, sleep, VO2 max, training load) through the community garminconnect Python library. Garmin doesn't offer an official personal API, so this is unofficial. It also tracks mileage on each pair of shoes and my upcoming and past races.
* Journal: written in the app, with photos. Entries are geotagged using OpenStreetMap.
* Books: looked up through Open Library and Google Books, with covers saved locally.

The goal was one screen that answers "how am I doing?" across the parts of my life I actually track.

What I'd love feedback on:

* What would you want on a Home screen like this, and what's missing?
* Would you use something like this if it were open source?
* Any other input?

Thanks everyone!

## 评论（14/18）

> **QuanTradin**（1 分） · 2026-10-25T10:26:19+08:00　
> parsing bank PDFs back to 2015 is the brave part, statement layouts change every few years and break every parser I've tried. did the scikit model actually beat your keyword rules, or do the rules still catch most of it?

---

> **ZebrafishWrangler**（1 分） · 2026-10-25T10:30:20+08:00　
> https://reddit.com/link/1xept54/video/zrtf4kckyixh1/player

---

> **ZebrafishWrangler**（1 分） · 2026-10-25T10:34:50+08:00　
> Yes, it was a lot of back and forth for awhile but it ended up working out eventually! It took combining both pdfplumber and Tesseract OCR to fully parse everything but really nice to have the full historical data (whether or not I actually use it lol)
>
> The scikit model is probably overkill tbh. The keywords matching catches mostly everything, but I have found that the scikit model will catch things when Plaid/banks slightly change descriptions that come through the API so it is nice for that.

---

> **bkdev98**（1 分） · 2026-10-25T12:27:40+08:00　
> How do you work out the "free to spend" number, budget minus spent so far, or does it hold back bills that haven't hit yet? I make a budgeting app built around a similar number and taking out bills and savings first, then splitting the rest over the days to payday, was the part that made it trustworthy.

---

> **CutDry6295**（1 分） · 2026-10-25T12:39:02+08:00　
> For the Home screen, I would put data freshness beside each summary number. A “free to spend” figure based on a bank sync from yesterday, a manually imported statement, and a Garmin run from this morning should not all look equally current. A small “last updated / source / needs attention” row would make the one-screen answer more trustworthy than another chart. If you open-source it, a demo mode with the made-up data you already use in screenshots would let people explore without connecting financial or health accounts. I have only read the post, not run the app.

---

> **Recent-Day3062**（1 分） · 2026-10-25T12:47:23+08:00　
> Omg. Who hasn’t been waiting to integrate exactly these things into a single app?

---

> **sapplex1**（1 分） · 2026-10-25T13:43:37+08:00　
> The one-screen idea is what pulled me in. I tried a weekly summary like this for myself, and the part that broke my trust was stale data. A number without a date felt fine until I acted on it. I started putting the last sync time right next to each section. That small change made the whole screen feel honest. For Home, I would keep it to three things. What needs attention today. What changed since last week. And one next step. Everything else can live one tap away. I also agree with the freshness point in the comments. If a section is stale, I would rather see it greyed out than hidden. On your Home screen, would you rather show a section with old data and a stale label, or hide it until it refreshes?

---

> **alremez**（1 分） · 2026-10-25T15:38:31+08:00　
> combining my finances, running stats and reading habits might be a little too much reality for one dashboard
>
> One thing I'd add is a weekly summary of what actually changed and what deserves attention. Have you thought about that?

---

> **QuanTradin**（1 分） · 2026-10-25T20:29:57+08:00　
> pdfplumber plus Tesseract is where I'd have ended up too. overkill is fine if it was fun, and the full history lets you answer questions you haven't thought of yet.

---

> **ZebrafishWrangler**（1 分） · 2026-10-25T21:32:38+08:00　
> Yes, that is very similar to what I've done. It is evenly split across all the days, but there are those pesky big expenses/bills which you also want to account for. To get around that, those get calculated first as big jumps in the plot first and then everything else built around that. This really has helped keep me on track better. The budget is set every month including a popup you can't ignore that makes you either reuse the same budget from the last month or set up a new budget which has also forced the reflection. Thanks for the question!
>
> https://i.redd.it/tmhi5fgb8mxh1.png

---

> **ZebrafishWrangler**（1 分） · 2026-10-25T21:37:47+08:00　
> Thanks! I'm currently implementing alerts for different things like a subscription price increase, a missed Loan payment, transactions waiting to be categorized, runs with no shoe assigned, and a failed Sync. There's also already text on each page showing when it was last updated.
>
> I also have some code half written to automatically re-sync everything if it has been more than 12 hours since the last data refresh so definitely thinking about that! But luckily, there is nothing in this dashboard that is that immediately urgent and the syncing only takes a few seconds!
>
> Thanks for the input!

---

> **ZebrafishWrangler**（1 分） · 2026-10-25T21:38:39+08:00　
> Thanks! I'm currently implementing alerts for different things like a subscription price increase, a missed Loan payment, transactions waiting to be categorized, runs with no shoe assigned, and a failed Sync (including tapping on that alert to take you to that data source). There's also already text on each page showing when it was last updated.
>
> I also have some code half written to automatically re-sync everything if it has been more than 12 hours since the last data refresh so definitely thinking about that! But luckily, there is nothing in this dashboard that is that immediately urgent and the syncing only takes a few seconds!
>
> Thanks for the input!

---

> **bkdev98**（1 分） · 2026-10-25T23:12:10+08:00　
> Laying the big bills in first as jumps makes sense, otherwise rent day wrecks the daily number. Forcing the budget choice every month is a good bit of friction too.

---

> **sapplex1**（1 分） · 2026-10-26T13:41:55+08:00　
> Alerts are where stale data gets expensive, I think. A price-increase alert on last week's number is just a false alarm, but a missed-payment alert that shows up late is the one that actually costs you. That's what made me land on showing the last-sync time next to each block instead of hiding it. I'd rather see an old number labeled old than a blank space I have to guess about. For your alerts, do you fire on the last known value with a stale tag, or hold the alert until the next fresh sync? The second one feels safer, but then a sync failure means silence exactly when something went wrong.

## 导航

- 项目页：[[10-项目/I-built-a-personal-dashboard-that-pulls-my-money_e3a37d55]]
- 渠道页：[[50-渠道/reddit]]
- 赛道：`开发者工具`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
