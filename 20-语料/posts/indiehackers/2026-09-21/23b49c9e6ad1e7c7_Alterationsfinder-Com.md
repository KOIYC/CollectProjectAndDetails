---
type: "corpus"
item_id: "23b49c9e6ad1e7c7"
title: "Alterationsfinder Com"
source: "indiehackers"
source_name: "Indie Hackers 产品库"
url: "https://www.indiehackers.com/product/alterationsfinder-com"
captured_at: "2026-09-21T03:11:35+08:00"
lang: "en"
kind: "project"
topic: "AI 工具/Agent"
shard: "2026-09-21"
tags:
  - 语料
  - indiehackers
metrics: {}
comments_count: 0
comments_total: 0
discovered_via: "ih:products"
---

# Alterationsfinder Com

> [!info] 一句话导读
> Home Starting Up Case Studies DB Products Ideas DB Subscribe to IH+

> [!meta]- 语料信息（点开展开）
> 来源：Indie Hackers 产品库（project）
> 原帖：<https://www.indiehackers.com/product/alterationsfinder-com>
> 指标：—
> 作者：—　|　发布：—
> 项目链接：—
> 采集：2026-09-21T03:11:35+08:00　|　id：`23b49c9e6ad1e7c7`

## 正文

Home Starting Up Case Studies DB Products Ideas DB Subscribe to IH+
Starting Up Case Studies
 Ideas DB Products DB Sign in Join
AlterationsFinder.com
 Find a tailor near you. Know what to pay.
Visit Website
AlterationsFinder.com Find a tailor near you. Know what to pay.
 Post 1
 Revenue $0 / mo
 Website
September 20, 2026
 6 months building. 1 Google update.
90% traffic drop. Lessons inside.
I'm a technology leader who spends his days in enterprise digital transformation and nights building niche directories.
 AlterationsFinder started as a simple observation: clothing alterations is a massive, fragmented industry with zero price transparency. If you've never had clothes altered before, you have no idea whether $40 for a hem is fair or a rip-off. There's no reference point. No central resource. Just hoping the tailor doesn't see you coming.
 So I built one.
 What I built
 AlterationsFinder is a directory of 5,700+ clothing alteration and tailoring businesses across 100 US cities — with real Google ratings, verified photos, and a free Alteration Cost Calculator that gives instant price estimates by garment type and US state.
 The tech stack is Lovable (React/Vite/TypeScript) connected to Supabase, deployed on Vercel. I scraped business data via the Google Places API, ran it through Claude API for AI-powered description enrichment, and migrated all photos to my own CDN so I wasn't dependent on Google's image URLs expiring.
 Total time from idea to live: about 3 months.
 What happened next
 Traffic climbed steadily through March and April 2026. By mid-April I was getting around 60 clicks per day from Google Search. Not huge, but growing in the right direction.
 Then April 15 arrived.
 Google ran a core algorithm update and traffic dropped 90% overnight. I went from 60 clicks to 4-6 clicks per day. Five months later I still haven't recovered to pre-update levels.
 Here's what the Google Search Console data showed: indexed pages dropped from 5,051 to 2,828 (a 44% decline from peak), "Crawled - currently not indexed" jumped from 456 pages to 3,631 pages (Google visiting and rejecting listing pages at scale), and zero external backlinks across the entire domain.
 That last point is the real lesson.
 What I got wrong
 Building the directory was the easy part. I underestimated how much domain authority matters for a programmatic content site.
 Google's core updates increasingly penalise directories and programmatic content that lacks trust signals. A site with 5,700 pages and zero external links is asking Google to take its word for it. Google doesn't.
 I also made a technical mistake that cost months: the www to non-www redirect was broken at the CDN configuration level for the entire time the site was growing. Google was indexing both www and non-www versions of every page, splitting the ranking signal across duplicates. I only caught it when I dug into the GSC coverage report after the crash.
 The redirect is fixed now. The 5,000+ redirect pages are slowly being recrawled and consolidated. But it takes months.
 What I've done since
 Rather than abandon it, I treated the crash as a product problem to solve.
 Since May I've AI-enriched all 5,700+ listings with unique descriptions using Claude API, migrated 5,700 listing photos from Google CDN to a self-hosted content CDN with SEO-optimised filenames and alt tags, published 51 blog posts across 5 content categories all with Quick Answer boxes targeting AI Overview snippets, added bilingual content for Spanish-language alteration shops (costureras, modistas) in Hialeah, El Paso, San Antonio, and Miami where the site now ranks position 1-2 for several Spanish-language queries, built city and state pages with unique editorial content per location generated via Claude API, and applied for Google AdSense which is currently pending.
 The site is in the best shape it has ever been technically. Whether Google agrees remains to be seen at the next core update.
 Current numbers (honest)
 Listings: 5,700+ across 100 US cities. Organic clicks: 3-8 per day, down from 60 at peak. Blog posts: 51. Revenue: $0. External backlinks: 0. Months since Google update: 5.
 Not a success story yet. But not dead either.
 What I'd do differently
 Get backlinks before you need them. One DR50+ link in month 1 would have changed the trajectory of the site entirely. Audit your redirect configuration before you scale — I let a misconfigured www redirect run for 6 months and that was expensive. Build content alongside listings, not after. I had 5,700 listings and zero blog content for the first 3 months and Google had no reason to trust the domain. Programmatic content needs a trust anchor — pure directory pages without editorial content are increasingly vulnerable to core updates and the blog posts and city-level editorial content should have come first.
 The site is live at alterationsfinder.com — the free Alteration Cost Calculator is the part I'm most proud of and the thing that drives the most return visits.
 Happy to answer questions about the build stack, the data pipeline, the Google Places API scraping approach, or what it actually looks like to watch your traffic fall off a cliff and have to rebuild it from the inside.
Rainer B
1 Like
Comment
About
 I built AlterationsFinder because I got quoted wildly different prices for the same alteration at three different shops and had no way to know who was fair and who was taking advantage.
 People
 Rainer B Founder
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

- 项目页：[[10-项目/Alterationsfinder-Com_23b49c9e]]
- 渠道页：[[50-渠道/indiehackers]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
