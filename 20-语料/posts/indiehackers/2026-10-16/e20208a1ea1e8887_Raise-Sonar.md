---
type: "corpus"
item_id: "e20208a1ea1e8887"
title: "Raise Sonar"
source: "indiehackers"
source_name: "Indie Hackers 产品库"
url: "https://www.indiehackers.com/product/raise-sonar"
captured_at: "2026-10-16T09:37:58+08:00"
lang: "en"
kind: "project"
topic: "AI 工具/Agent"
shard: "2026-10-16"
tags:
  - 语料
  - indiehackers
metrics: {}
comments_count: 0
comments_total: 0
discovered_via: "ih:products"
---

# Raise Sonar

> [!info] 一句话导读
> Home Starting Up Case Studies DB Products Ideas DB Vibe Coding Tools Subscribe to IH+

> [!meta]- 语料信息（点开展开）
> 来源：Indie Hackers 产品库（project）
> 原帖：<https://www.indiehackers.com/product/raise-sonar>
> 指标：—
> 作者：—　|　发布：—
> 项目链接：—
> 采集：2026-10-16T09:37:58+08:00　|　id：`e20208a1ea1e8887`

## 正文

Home Starting Up Case Studies DB Products Ideas DB Vibe Coding Tools Subscribe to IH+
Starting Up Case Studies
 Ideas DB Products DB Sign in Join
Raise Sonar
 Startup deals from every platform, the moment they go live.
Visit Website
Raise Sonar Startup deals from every platform, the moment they go live.
 Post 1
 Revenue $0 / mo
 Website
October 14, 2026
 I built an alert system for 20+ equity crowdfunding platforms in three weeks of evenings
In September I started a new job, and I’m also finishing an MSc. A week into the new job I started a side project. A sensible person probably wouldn’t have done it in that order.
 The itch
 In 2016, Revolut raised on Crowdcube at $2.14 a share. In 2024, those early backers were offered about $865. Anyone with £10 and an afternoon could have been one of them.
 When I started reading about equity crowdfunding, the upside wasn’t what struck me (there are plenty of horror stories too, more on those below). What struck me was how scattered it all is. In the US there’s Wefunder, Republic and StartEngine. The UK has Crowdcube. Europe has a dozen platforms, each in its own language. Australia has Birchal and Canada has FrontFundr. Every one of them wants you to make an account and keep checking back. Raises open and close within weeks, so if you weren’t watching the right site that week, you’d never know the deal existed.
 I looked for something that pulls all of this into one place. The US has some tools, but I couldn’t find a live campaign feed for Europe or the rest of the world. So I fell back on the old engineer reflex.
 Checking it wasn’t a dumb idea
 Before writing any code, I spent a weekend on feasibility. A few things surprised me:
 The whole global market is small. There are about 2,500 startup campaigns a year, roughly 10 a day. That’s a tractable data problem, not a big-data one.
The US hands you a free government feed. Every Reg CF raise has to file a Form C with the SEC, usually a few days before the campaign goes live, and EDGAR serves it as structured data. So US coverage of new raises was close to complete on day one.
Europe has nothing like that. The regulation requires an info sheet for each offer, but nobody publishes those centrally. You either scrape or partner.
Most European platforms serve plain HTML. A few US ones are JavaScript shells or sit behind bot protection.
That was good enough to start.
 The build
 I picked the boring stack I use every day: Nest.js, React and Postgres, running as one Docker container on Railway. I even copied the database tooling from another side project verbatim, so the same commands work in both. When you only have evenings, familiarity is a feature. Serverless was tempting, but some platforms need a real headless browser, and running Playwright in a long-running container with a stable IP is far less painful.
 Each platform gets its own adapter class. Today there are 23 sources: SEC EDGAR plus platforms in 15+ countries.
 The part I’m proudest of is unglamorous. The classic failure is a scraper that breaks silently: the site gets a redesign, the selector matches nothing, the adapter returns an empty list, the poll logs “success”, and nobody notices for six weeks. To guard against that:
 Adapters throw instead of returning empty.
Every run records what it saw.
A health check flags any source that hasn’t produced a new campaign in N days.
Uptime monitoring points at that check, not just at “is the server up”. Years of on-call make you paranoid in useful ways.
 The outbound side gets the same care. Every alert has a dedupe key, so a retry never sends you “closes in 72 hours” twice. When the whole promise of the product is timing, double emails would kill trust fast.
 The unsexy stuff that ate the most time
 Naming. It started as Rise Radar, but every domain variant was taken. My rule was a free .com for under $20, which turned out to be a real constraint. It’s now Raise Sonar.
Selling from Bulgaria to UK, EU and US consumers means VAT in a lot of places. I didn’t want to become a tax expert, so I went with a merchant-of-record setup.
Timezones. The entire product boils down to “this raise closes at time T” across a dozen jurisdictions. Every timestamp carries its timezone, no exceptions.
Risk warnings and legal pages for three different regulatory regimes. Not fun, but very necessary.
What it actually does
 Raise Sonar watches 20+ platforms and every SEC Form C filing. It emails you:
 when a raise matching your rules launches
7 days, 72 hours and 24 hours before it closes
when it reaches 90% of its cap, since those raises can close early
before an early-bird perk runs out
Rules read like plain sentences, e.g. “EU + UK · SaaS, Fintech · min ticket ≤ €500” . Tell it where you live and it badges which deals you can actually invest in.
 There’s a free weekly digest. Real-time alerts cost $10 a month, and a Pro tier adds the numbers behind each raise.
 The thing I didn’t expect to put on my homepage
 While researching, I found the outcome data sobering:
 Only about 6% of UK crowdfunded companies have ever exited, and about 20% went bust.
Nearly half of US crowdfunded companies don’t file the annual reports they’re required to.
BrewDog’s crowd investors were once shown a 2,765% paper gain and got nothing when the business sold.
I put all of that on the homepage, right under the Revolut story. It felt strange for a marketing page. But a product that only shows the winners is selling lottery tickets, and I’d rather people trust the alerts. Raise Sonar doesn’t give advice or pick deals. It makes sure you see them in time to decide for yourself.
 Where it is now
 It’s just launched. Next on the list:
 an AI write-up for every raise (valuation against comparable rounds, dilution, runway), with every line linked to its source
more platforms
Telegram and WhatsApp alerts
What I’d love from you
 If you invest in crowdfunding: what would make alerts worth paying for?
If you’ve grown a niche paid newsletter or alert product: where did your first 100 subscribers come from?
Roast the landing page: raisesonar.com
BlackShadow
2 Upvotes
Comment
About
 Equity crowdfunding gave everyone access to early-stage startups. Revolut’s first crowd backers got in for £10 and were later offered over 400x their share price. Access was never the problem. Finding the deals was.
 People
 BlackShadow Founder
Stay informed as an indie hacker.
 Market insights that help you start and grow your business.
Subscribe
Follow @IndieHackers on X for stories and insights about founders building profitable online businesses, and to connect with others in the Indie Hackers community.
 © Indie Hackers, Inc. · FAQ · Terms · Privacy · Cookie Settings / Policy ·
Community
 Top Today Top This Week Top This Month Join
Products
 All Products Highest Revenue Add Yours
Databases
 Ideas Products Stories

## 导航

- 项目页：[[10-项目/Raise-Sonar_e20208a1]]
- 渠道页：[[50-渠道/indiehackers]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
