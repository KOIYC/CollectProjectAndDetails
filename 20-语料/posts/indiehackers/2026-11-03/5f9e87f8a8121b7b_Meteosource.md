---
type: "corpus"
item_id: "5f9e87f8a8121b7b"
title: "Meteosource"
source: "indiehackers"
source_name: "Indie Hackers 产品库"
url: "https://www.indiehackers.com/product/meteosource"
captured_at: "2026-11-03T09:43:29+08:00"
lang: "en"
kind: "project"
topic: "AI 工具/Agent"
shard: "2026-11-03"
tags:
  - 语料
  - indiehackers
metrics: {}
comments_count: 0
comments_total: 0
discovered_via: "ih:products"
---

# Meteosource

> [!info] 一句话导读
> Home Starting Up Case Studies DB Products Ideas DB Vibe Coding Tools Subscribe to IH+

> [!meta]- 语料信息（点开展开）
> 来源：Indie Hackers 产品库（project）
> 原帖：<https://www.indiehackers.com/product/meteosource>
> 指标：—
> 作者：—　|　发布：—
> 项目链接：—
> 采集：2026-11-03T09:43:29+08:00　|　id：`5f9e87f8a8121b7b`

## 正文

Home Starting Up Case Studies DB Products Ideas DB Vibe Coding Tools Subscribe to IH+
Starting Up Case Studies
 Ideas DB Products DB Sign in Join
Meteosource
 Weather API for developers
Visit Website
Meteosource Weather API for developers
 Posts 2
 Revenue $0 / mo
 Website
November 2, 2026
 We built an MCP server for our weather API. Here's why, and what we learned
I'm the marketer at Meteosource, a weather API that blends 40+ global weather models with machine learning to deliver accurate, high-resolution forecasts. We recently launched an MCP server, which gives our users one more way to access that data: straight from AI tools like Claude, ChatGPT, Codex or Cursor.
 Here's why we did it and what we learned along the way.
 The idea: AI tools are becoming a place where people look for data
 More and more of our customers' work happens inside an AI chat. Someone asks Claude "which of our 12 sites had the worst weather last month?" and expects an answer, not a tutorial on how to call an API.
 If an AI tool can't reach your data, you're invisible in that moment. Someone else's data gets used, or the model guesses. For a data company, that felt like a real risk, and also a new distribution channel that's still early.
 Where it came from
 It wasn't a customer request. It was our founder's idea. He looked at the typical scenarios our customers use our API for and counted 14 of them: alerts across many locations, a morning weather briefing for branches, choosing sites for solar farms, planning outdoor work, checking how weather affects sales, proving past weather for a construction delay...
 All of these share one problem: the customer has to write code to get the answer. With MCP, they just ask.
 Decisions that shaped it
 Hosted, not installed. Users add one URL and their API key. Nothing to install, nothing to update. We run one server for everyone, with a separate cache and rate limit per key.
 Tokens are the real constraint. Raw API responses are huge. A year of daily history as plain JSON often doesn't fit in the model's context, and the analysis just fails. So the server returns compact tables and aggregates on its side (days, months, long-term normals). The output uses 4 to 7 times fewer tokens than the raw API. "Was this month warmer than normal?" is one call and one row.
 Caching saves customers money. People and agents often ask about the same places and dates again. Repeated questions hit our cache instead of the customer's quota.
 It works on the free plan. Anyone can try the forecast tools with a free key. We'd rather have people play with it than hit a paywall on the first question.
 One thing we learned along the way
 We went with a simple setup: you send your API key in a header, and that's it. It works fine in Claude, ChatGPT, Codex, Cursor and most other MCP clients, no extra login needed.
 What we didn't realize at first: some official directories, like Anthropic's connector directory, only accept servers with OAuth sign-in. So we're now considering adding OAuth. Not a blocker, but if you're building an MCP server, it's worth thinking about early.
 Numbers
 It's still early days, so no real numbers yet. We'll come back with numbers once we're able to evaluate what worked.
 What I'd love to hear from you
 Has anyone here seen real users come from MCP directories, or is it mostly developers browsing? And for those of you with a data or API product: are you treating AI tools as a distribution channel yet?
 If you want to see more details, check out our launch article . Setup and docs are at mcp.meteosource.com .
Thunder Rumbles
3 Upvotes
1 Comment
August 31, 2026
 Three pricing problems we hit selling a weather API, and what we changed
I do marketing and operations for a hyperlocal global weather API. Small team, and pricing was a tough nut to crack.
 The hard part with a data product is that it looks like a commodity. Buyers assume every forecast is the same and shop on price, even when the thing behind it isn't the same at all. So you can't price on quality, because they can't see it yet.
 Three problems we ran into.
 One plan shape can't fit a hobby project and an operations team. One customer makes 5,000 calls a day, another makes 500,000. Same features, wildly different usage. We were trying to solve both with one axis and it kept producing plans that were wrong for everybody. What worked was splitting it in two: pick your tier for features, pick your volume separately. Obvious in hindsight. Took us a while.
 A one-time-value asset doesn't belong in a subscription. We have 20 years of historical weather data. Bundle it into a plan and people pull the archive once then churn. Put it in its own tier and it gets expensive enough that only big customers can justify it. We made it metered instead, fractions of a cent per day per location, available on any plan. Pay for what you pull.
 Sometimes the right unit isn't calls. People forecasting solar and wind output kept asking for something no tier covered. The fix wasn't a new volume band, it was changing the unit. They don't think in API calls, they think in sites. So we priced per location. That one felt like the actual lesson: price in the unit your customer already counts. If they have to do arithmetic to work out what you'll cost them, you've lost them.
 Too early for me to have clean conversion data on any of this, so take it as reasoning rather than proof.
 Has anyone else priced in a unit that wasn't calls, seats, or users? What did you land on, and did it confuse people at first?
Thunder Rumbles
3 Upvotes
5 Comments
About
 We wanted a forecast API a developer could sign up for in five minutes and actually understand the pricing of, with hyperlocal data good enough to build a real product on.
People
 Thunder Rumbles Operations
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

- 项目页：[[10-项目/Meteosource_5f9e87f8]]
- 渠道页：[[50-渠道/indiehackers]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
