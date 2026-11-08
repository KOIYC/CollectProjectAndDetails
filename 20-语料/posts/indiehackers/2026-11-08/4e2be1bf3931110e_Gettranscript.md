---
type: "corpus"
item_id: "4e2be1bf3931110e"
title: "Gettranscript"
source: "indiehackers"
source_name: "Indie Hackers 产品库"
url: "https://www.indiehackers.com/product/gettranscript"
captured_at: "2026-11-08T12:54:09+08:00"
lang: "en"
kind: "project"
topic: "AI 工具/Agent"
shard: "2026-11-08"
tags:
  - 语料
  - indiehackers
metrics: {}
comments_count: 0
comments_total: 0
discovered_via: "ih:products"
---

# Gettranscript

> [!info] 一句话导读
> Home Starting Up Case Studies DB Products Ideas DB Vibe Coding Tools Subscribe to IH+

> [!meta]- 语料信息（点开展开）
> 来源：Indie Hackers 产品库（project）
> 原帖：<https://www.indiehackers.com/product/gettranscript>
> 指标：—
> 作者：—　|　发布：—
> 项目链接：—
> 采集：2026-11-08T12:54:09+08:00　|　id：`4e2be1bf3931110e`

## 正文

Home Starting Up Case Studies DB Products Ideas DB Vibe Coding Tools Subscribe to IH+
Starting Up Case Studies
 Ideas DB Products DB Sign in Join
GetTranscript
 YouTube transcript extractor for videos, playlist, channels
Visit Website
GetTranscript YouTube transcript extractor for videos, playlist, channels
 Posts 2
 Revenue $80 / mo
 Website
November 7, 2026
 Google indexed our Next.js homepage as an empty page, twice, and clicks fell ~90%. My Vercel checklist and open questions
I work on a small Next.js tool hosted on Vercel. Organic clicks went from ~140/day to ~10 in late September, recovered to ~75, then dropped again mid-October and only came back to ~40-50. I'm trying to figure out whether this is our fault, Google's, or Vercel's.
**The weird part:** twice now, Google indexed our homepage as an empty page. The indexed version had no title, no meta description and no content. When I test the live URL today, the server HTML is complete: title, H1, content, JSON-LD, one canonical, 200 OK. So whatever Googlebot received at those moments, I can't reproduce it.
**Ruled out (all clean)**
 - Manual actions and security issues in Search Console
 - Host status: no robots.txt, DNS or server errors for 90 days
 - One self-referencing canonical per page, and Google's selected canonical matches it
 - www redirects to the apex with a 308
 - Exact-phrase searches of our copy show no scraped duplicates
 - URL Inspection live test: 200 OK, 59 of 60 resources loaded (the only failure was analytics)
**Vercel/Next.js things I'm still checking (possible causes of an "empty" homepage)**
 - A deploy or cache revalidation window where the crawler got an empty or partial response
 - A client-side-rendering bailout (for example useSearchParams without a Suspense boundary) that leaves an empty shell in the HTML
 - Firewall or bot protection serving a challenge/interstitial page to Googlebot
 - Middleware or auth redirects sending crawlers to /sign-in or /sign-up (we saw a sign-up page show up in results)
 - Preview deployments or the *.vercel.app production alias getting indexed as duplicates
 - Soft 404s: error pages returning 200
**What lines up with the drops**
 - Google's September 2026 spam update rolled out Sept 24 to Oct 8, and there were unconfirmed volatility spikes on Oct 16, 20-21 and 24. Both drops fall in those windows, but that's correlation, not proof.
 - The site has very few real backlinks: the Search Console links report shows 6, and most look auto-generated.
**What I'm doing now**
 Leaving the main page untouched for a few weeks, building real links (directories, communities, articles), and tracking impressions per query instead of clicks.
Questions for you:
 1. Has Google ever indexed one of your pages as empty (no title, no description, no content) on Vercel/Next.js, even though the live page looked fine? What was the cause, and did you ever find out what the crawler actually received?
 2. If you went through similar drops on a young domain, how long did recovery take, and what actually moved the needle?
 3. Anything on my checklist you'd add?
Che_loveck.
1 Upvote
1 Comment
November 5, 2026
 Show IH: a free YouTube transcript extractor with bulk export and an API
I work on GetTranscript, a small web tool that pulls transcripts out of public YouTube videos, playlists and channels.
What it does:
 - Paste a link, get the text as TXT, Markdown, SRT, VTT, JSON or CSV
 - Single videos are free, no sign-up
 - Playlists and channels (up to 100 videos per job) run on pay-as-you-go credits: 1 video = 1 credit, credits never expire, failed extractions are refunded
 - REST API for developers
 - Free AI summaries for single videos
Where I'd love your opinion:
 1. Bulk jobs need credits from the first video, so there is no free bulk trial. Some competitors give a few free credits at sign-up. Would a small free bulk trial (say 10 videos) make you more likely to try it, or is "single videos free, bulk paid" a clear enough line?
 2. The preview groups captions into ~30-second paragraphs with timestamps. Readable, or would you rather see raw caption lines?
 3. What would make you trust a tool like this with a batch of 100 videos?
 Honest feedback welcome, including "this is useless because...".
Che_loveck.
5 Upvotes
Comment
About
 I wanted to test my skills and build something useful on my own — a small product that could actually earn money and help people at the same time. GetTranscript is my attempt to do both.
People
 Che_loveck. Founder
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

- 项目页：[[10-项目/Gettranscript_4e2be1bf]]
- 渠道页：[[50-渠道/indiehackers]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
