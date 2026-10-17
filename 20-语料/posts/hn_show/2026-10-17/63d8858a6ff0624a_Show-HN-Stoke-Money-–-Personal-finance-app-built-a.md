---
type: "corpus"
item_id: "63d8858a6ff0624a"
title: "Show HN: Stoke Money – Personal finance app built around a cash flow forecast"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50122776"
project_url: "https://stoke.money/"
author: "_wesley"
published_at: "2026-10-16T18:54:47Z"
captured_at: "2026-10-17T13:35:15+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-10-17"
pub_day: "2026-10-16"
tags:
  - 语料
  - hn_show
  - author__wesley
  - story_50122776
  - show_hn
metrics: {"points": 25, "comments": 19, "engagement_velocity": 25}
comments_count: 19
comments_total: 19
discovered_via: "hn:show_hn:3d"
---

# Show HN: Stoke Money – Personal finance app built around a cash flow forecast

> [!info] 一句话导读
> Hi HN,I've been through many finance tracking apps, starting with Personal Capital, then Monarch, and most recently Copilot. None of them have worked perfectly …

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50122776>
> 指标：点赞=25 · 评论=19 · engagement_velocity=25
> 作者：_wesley　|　发布：2026-10-16T18:54:47Z
> 项目链接：<https://stoke.money/>
> 采集：2026-10-17T13:35:15+08:00　|　id：`63d8858a6ff0624a`

## 正文

Hi HN,I've been through many finance tracking apps, starting with Personal Capital, then Monarch, and most recently Copilot. None of them have worked perfectly for my needs.All of these apps tend to model “cash flow” as the net sum of your transactions during a month, yet while credit card charges are reported immediately, they are typically deducted from checking (cash) accounts the following month when the bill is due. As a result, I've always had to maintain a separate spreadsheet to track my actual cash flow.These apps also have a huge focus on managing budgets, which has never been for me. My spending is rarely consistent month-to-month, so every month I'm comparing my fully justified spending against my budget, and tweaking my budget until I “pass”.So I built yet another finance tracking app. It has the usual components - accounts, transactions, categories - but the core is a cash flow projection engine, and everything else is built around it.Budgets are gone. Instead, each income/spending category is projected forward from your historical activity, but not as a flat monthly number. They land in whatever account you historically use (e.g. checking account for paychecks/rent/bills, credit/debit cards for daily spending). Credit card payments are modeled automatically based on your projected credit card balance. You can set up your own recurring transfers between accounts as well, to model savings, for example.The end result is that the app can forecast how your cash moves, and you can see in advance when any account might run low. If all of your accounts look good for the next 12 months, maybe you don't have a budgeting problem.What’s made the biggest difference for me has been the MCP integration, which I have connected to Claude (but can be connected to any AI agent of your choice). I have asked it to import historical transactions by uploading PDF account statements, categorize/tag all transactions that took place while I was on vacation, and plan transfers across my accounts to cover expected payments.I hope some people that share my frustrations will find this app useful.

## 评论（19/19）

> **freshnode** · 2026-10-16T19:36:51.000Z　
> Looks nice - really - but I wouldn't touch you till you got external validation of your security practices and shared more about what you do there on your FAQs. Encrypting access tokens is just table stakes. My finances are private and not to be trusted with just anyone. The folks you compare yourself to have that type of certification but it's not listed in the comparison.Even a SOC type 1 would show you're on the journey.

---

> **skinfaxi** · 2026-10-16T19:57:19.000Z　
> > The Service is currently published under the brand name VoidHQ as the product Stoke Money. Both names are subject to change.The governing terms are California's. I checked CA business registry and found no 'VoidHQ' or 'Void HQ'. Not sure who I would be trusting with my data.

---

> **mmmeff** · 2026-10-16T20:20:35.000Z　
> I didn't know the rocket company was getting into personal finance. https://www.stokespace.com/

---

> **pj_mukh** · 2026-10-16T20:29:26.000Z　
> Very interesting, and I've been looking for something like this. Kudos for building this. But for my information do you think you have a different handle on this vs. say ChatGPT's Plaid connection [1]. What do you think you offer differently?[1]: https://openai.com/index/personal-finance-chatgpt/

---

> **memonkey** · 2026-10-16T21:50:32.000Z　
> i looove this. i have been working on something similar. are you using AI to help with balance forecasting? would you be willing to share how it has been working out for you? how much set up is necessary for you to set it and forget it. i am currently using monarch and only ever look at account balances and only sometimes look at transactions.

---

> **jldugger** · 2026-10-16T22:19:24.000Z　
> > As a result, I've always had to maintain a separate spreadsheet to track my actual cash flow.This is more or less how I already set up GNUCash. Couple dozen scheduled transactions created 90 days into the future, with the "Future Minimum Balance" field enabled on the homescreen.For me, the time sinks are interrelated:1. Monthly reconciliation. Every month I sit down and compare the scheduled transactions with what actually happened in statements, for approximately thirty different accounts. Many don't have APIs, certainly none GNUCash would speak. This takes a lot of time and I wish I could just have this automated. Just give me exception handling on the edge cases like a new transaction category, or a forecasted negative checking balance.2. CC transaction import. This is a structural failing of banking closing down formerly open APIs. Only thing left on my BofA accounts is CSV exports. Which thankfully works with a bit of setup but the writing is on the wall and even that may soon vanish in the name of banks defending their core business.3. Stock transactions, equity grants & price tracking. This one is even harder since CSV feels structurally not up to the task of representing the "sell to cover taxes" split of RSU grants, and I never really got it working in OFX anyways. Plus I have a pretty weird collection of accounts including a pension IAP that updates once a year (and that update is retroactive to 6 months ago) and a 457b invested in restricted custom funds with no ticker symbols.

---

> **chabska** · 2026-10-17T04:26:54.000Z　
> The way I look at it, the money I've spent is the money I've spent. That it will only be deducted from my account balance at a later date is irrelevant, I can't touch that money either way.

---

> **_wesley** · 2026-10-16T19:57:19.000Z　
> Thanks, that's fair. No SOC 2 yet, but I understand if that's a dealbreaker. I will expand the FAQs/Comparison pages to make that clear.

---

> **_wesley** · 2026-10-16T21:16:36.000Z　
> Thanks, totally fair to be wary. It's a one-person project right now. I'm registering an LLC, and the terms and privacy policy pages will be updated once that's done.

---

> **_wesley** · 2026-10-16T20:30:18.000Z　
> No affiliation. Didn't know about them (at least not their logo). That's unfortunate...I will make some changes.

---

> **_wesley** · 2026-10-16T21:00:15.000Z　
> Thanks. It's an interesting time for sure. Muse also launched with Plaid integration support. I haven't tested either offering (and probably won't ever trust Meta with anything), so take these with a grain of salt:- Privacy. Stoke is a paid subscription. I’m not selling your data. Caveat: if you connect an agent over MCP, what that agent does with your data is up to you. I can't control that.- Data. The core product is the projection, and it’s only as good as the data underneath it. Plaid data is imperfect, so there’s always some cleanup to do. ChatGPT and Muse may do a decent job of recategorizing transactions and even remembering those fixes for future ones, but I think direct access to those controls (categories, rules, overrides) is a better experience than asking a chatbot.- Portability. Everything you’ve modeled lives in Stoke, not in one AI assistant's memory. You can freely switch from ChatGPT to Claude or anything else without losing anything.- Not mutually exclusive. All the questions you would ask your LLM about your finances, you can still do via the Stoke MCP, so I see it as the best of both worlds.

---

> **_wesley** · 2026-10-16T22:42:01.000Z　
> Balance forecasting is part of the app! The app has been working well for me, I have since unsubscribed from Copilot. I think the amount of setup will depend on your spending pattern. Obviously, the more transaction data, the better the forecast. Otherwise a fair amount of tweaking might be needed for it to match your expectation. The MCP makes all the projections available to your agent though, so you can certainly analyze and make those tweaks through an AI chat.

---

> **Onavo** · 2026-10-16T21:44:12.000Z　
> I would tell you to ignore that and do the exact opposite. You are targeting B2C. Avoid the hacker news crowd they are not worth the trouble for this sort of thing. It's a distraction and if you believe the product advice here companies like Dropbox won't exist because FTP is a thing.You need to spam growth and marketing. Your landing page is horrible (too boilerplate, too vibe coded, no graphics.
> Some pages have horizontal overflows on mobile. https://stoke.money/compare/simplifi). Redo it. Run ads and pay Tiktok influencers and YouTubers.Standard consumer SaaS security is more than enough for this sort of product. Your users won't know the difference between end-to-end encryption and encryption at rest and while you are nitpicking based on hacker news power user feedback others would eat your lunch already.If you are a US fintech, monetizing consumer user data is par for the course. Do what you will with that information but just know that your competitors don't simply make money from subscriptions alone.

---

> **yieldcrv** · 2026-10-16T22:08:45.000Z　
> Wyoming LLC's can be finished in less than 24 hours, EIN can take 5 minutes on the IRS website and Mercury can set up bank accounts in less than a dayin my world, there is no such things as "registering", and I say that because I've seen many people get caught up on this process for actual years. Picking the wrong state, or getting hung up on name, and things like that. Can you shift liability and process payments or not. there is a blueprint that works for this country and international access, but nearly infinite permutations that may take you a lifetime to figure out, or cost you more than it should by copy pasting Delaware for everything.

---

> **mcmcmc** · 2026-10-16T21:41:02.000Z　
> FWIW “stoke” in the context of personal finance conjures images of burning piles of cash, for me at least

---

> **pj_mukh** · 2026-10-16T21:43:26.000Z　
> Yea, all those are fair!

---

> **memonkey** · 2026-10-17T03:21:03.000Z　
> one idea i was thinking for anonymizing data when sent to models is to hash or modulo with salt some values before sending it to the model and then unhash/unmodulo on the result. in other words, a way to keep the users data their own. just an idea.

---

> **_wesley** · 2026-10-16T21:54:13.000Z　
> Thanks for the feedback!

---

> **_wesley** · 2026-10-16T22:02:11.000Z　
> Heh, not exactly what I was going for

## 导航

- 项目页：[[10-项目/stoke.money_ab644d18]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
