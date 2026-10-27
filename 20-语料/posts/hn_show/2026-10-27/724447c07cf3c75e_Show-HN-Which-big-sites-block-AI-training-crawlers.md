---
type: "corpus"
item_id: "724447c07cf3c75e"
title: "Show HN: Which big sites block AI training crawlers but let AI search in"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50258781"
project_url: "https://getkavel.com/ai-crawlers"
author: "alishaikha"
published_at: "2026-10-27T13:18:22Z"
captured_at: "2026-10-27T23:46:32+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-10-27"
pub_day: "2026-10-27"
tags:
  - 语料
  - hn_show
  - author_alishaikha
  - story_50258781
  - show_hn
metrics: {"points": 2, "comments": 1, "engagement_velocity": 2}
comments_count: 1
comments_total: 1
discovered_via: "hn:show_hn:3d"
---

# Show HN: Which big sites block AI training crawlers but let AI search in

> [!info] 一句话导读
> SiteCheck QuoteDesk Free tools Guides Pricing Contact

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50258781>
> 指标：点赞=2 · 评论=1 · engagement_velocity=2
> 作者：alishaikha　|　发布：2026-10-27T13:18:22Z
> 项目链接：<https://getkavel.com/ai-crawlers>
> 采集：2026-10-27T23:46:32+08:00　|　id：`724447c07cf3c75e`

## 正文

Skip to content
 K Kavel
 ☰
SiteCheck QuoteDesk Free tools Guides Pricing Contact
Scan your website free
Research · AI crawler study
 Which big websites
block AI crawlers?
We checked the robots.txt rules of 945 well-known websites for 14 AI crawlers: news, retail, SaaS, finance, government and more. October 2026 check, finished 22 October 2026. We check again every month.
Look up a site If a site is not one of the 945 in the study, we check it live.
25.9% block at least one AI crawler in robots.txt (193 of 746 sites we could read)
9.2% block AI training but leave every AI search crawler open (69 sites)
13.9% turned away our test request identifying as GPTBot or ClaudeBot (see the limits below)
Blocked most often
 14 crawlers
Crawler Kind Sites blocking it
CCBot
 Common Crawl Training 19.6% (146)
 Bytespider
 ByteDance Training 18.4% (137)
 ClaudeBot
 Anthropic Training 18.1% (135)
 Applebot-Extended
 Apple AI-use control 17% (127)
 GPTBot
 OpenAI Training 16.9% (126)
 Meta-ExternalAgent
 Meta Training 16.8% (125)
 PerplexityBot
 Perplexity Search 15.3% (114)
 Google-Extended
 Google AI-use control 13.5% (101)
 Amazonbot
 Amazon General 13.3% (99)
 OAI-SearchBot
 OpenAI Search 9.4% (70)
 ChatGPT-User
 OpenAI User fetcher 9.2% (69)
 Claude-User
 Anthropic User fetcher 8.8% (66)
 Perplexity-User
 Perplexity User fetcher 8.7% (65)
 Claude-SearchBot
 Anthropic Search 8.3% (62)
By kind of site
Sites Checked Block any AI crawler Block GPTBot
US and international news 74 79.7% 56.8%
 Reference 27 77.8% 48.1%
 UK news 63 76.2% 60.3%
 Big tech 55 29.1% 18.2%
 Ecommerce brands 58 15.5% 10.3%
 Travel 29 13.8% 10.3%
 AI companies 44 13.6% 4.5%
 B2B marketplaces and distributors 22 13.6% 9.1%
 UK trade suppliers 40 12.5% 5%
 SaaS and developer tools 120 9.2% 2.5%
 Education 46 8.7% 4.3%
 Government 32 6.3% 3.1%
 UK retail 50 6% 2%
 Agencies 36 5.6% 2.8%
 Finance 50 0% 0%
No to training, yes to AI search
 These sites block at least one AI training crawler (GPTBot, ClaudeBot, CCBot, Meta-ExternalAgent, Bytespider) but leave every AI search crawler (OAI-SearchBot, Claude-SearchBot, PerplexityBot) open.
 airbnb.com · alibaba.com · aliexpress.com · amplitude.com · asda.com · axios.com · bbcgoodfood.com · bostonglobe.com · businessinsider.com · calendly.com · campaignlive.co.uk · canva.com · cbsnews.com · coursera.org · descript.com · dictionary.com · ea.com · espn.com · figma.com · foodnetwork.com · fortune.com · freshbooks.com · genius.com · github.com · goodreads.com · healthline.com · indiamart.com · lakeland.co.uk · latimes.com · lonelyplanet.com · loom.com · machinemart.co.uk · marketingweek.com · mcmaster.com · medium.com · moneyweek.com · netflix.com · newstatesman.com · nintendo.com · petsathome.com · postman.com · prospectmagazine.co.uk · prweek.com · radiotimes.com · rexel.co.uk · semafor.com · skyscanner.net · slate.com · snapchat.com · speedyservices.com · techcrunch.com · techradar.com · temu.com · theregister.com · thesaurus.com · theweek.co.uk · tomshardware.com · toolstation.com · tortoisemedia.com · tripadvisor.com · trustpilot.com · vinted.com · warbyparker.com · webmd.com · which.co.uk · who.int · wpp.com · zalando.com · zoominfo.com
Lists
Sites that block ClaudeBot but allow GPTBot
 Sites that block GPTBot but allow ClaudeBot
 Sites that block AI training but allow AI search
 Sites that block all 14 AI crawlers
How we checked, and the limits
For each site we read robots.txt and apply the rules for the homepage, crawler by crawler, following the robots.txt standard (RFC 9309). A crawler is "blocked" if robots.txt asks it not to read the homepage.
We also ask for the homepage once as GPTBot and once as ClaudeBot. Our requests come from Cloudflare's network, not from OpenAI or Anthropic, so a firewall that checks where crawlers really come from may refuse our test and still let the real crawler in.
199 sites are left out of the robots.txt figures: 127 turned away our request for robots.txt or sent a web page instead of the file (usually bot protection), 51 answered it with a server error, and 21 could not be reached. What their robots.txt says to real crawlers is unknown.
18 sites had no robots.txt rules at all (a 404 or an empty file), which under the standard means every crawler is allowed; they count as blocking nothing.
robots.txt is a request, not a lock. This shows what sites ask, not what AI companies do.
The list of sites was put together by Kavel; it is not a statistical sample of the web. This page was built and written with AI.
Download the data (CSV)
What does your site allow?
 Check your own site live, crawler by crawler. Free, no signup.
 Check my site Full agent-readiness scan Email me the monthly update
K Kavel
 Free tools Guides For AI agents Terms Privacy Refunds Contact
Kavel is a trading name of Lumen Labs Limited, registered in England and Wales, company number 16386579.
Support: support@getkavel.com
Automated checks are not legal advice, and a scan result is not a guarantee of how any AI agent will behave.
Start monthly monitoring
We scan your homepage every month and email you a report with what is new, fixed and still open. Cancel any time.
Your website address
 Email for your reports
 I own this website or have permission to check it, and I agree to the terms and privacy policy .
 You will pay $39 a month. Price shown in your local currency.
Continue to payment Close
Tell me when it's ready
We'll email you once, when this is available. No spam, and no sharing your address.
Email
 Website
Yes, email me about this. I can unsubscribe at any time.
Notify me Close

## 评论（1/1）

> **alishaikha** · 2026-10-27T13:21:47.000Z　
> Per-crawler totals, 746 sites with a readable robots.txt, checked 21 to 22 October 2026 (number of sites that block it, and what the operator says it's for):CCBot (Common Crawl, training): 146
> Bytespider (ByteDance, training): 137
> ClaudeBot (Anthropic, training): 135
> Applebot-Extended (Apple, token for AI use of Applebot's fetches): 127
> GPTBot (OpenAI, training): 126
> Meta-ExternalAgent (Meta, training): 125
> PerplexityBot (Perplexity, search): 114
> Google-Extended (Google, token for AI use of Googlebot's fetches): 101
> Amazonbot (Amazon, general): 99
> OAI-SearchBot (OpenAI, search): 70
> ChatGPT-User (OpenAI, fetches triggered by a user): 69
> Claude-User (Anthropic, fetches triggered by a user): 66
> Perplexity-User (Perplexity, fetches triggered by a user): 65
> Claude-SearchBot (Anthropic, search): 62Same data as a CSV, one row per site: getkavel.com/ai-crawlers/data.csv

## 导航

- 项目页：[[10-项目/getkavel.com_9592fc4f]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
