---
type: "corpus"
item_id: "27da3fcdd94386bc"
title: "Show HN: A SEO Tool to get found by Google and get cited by AI"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50566502"
project_url: "https://mozolite.com/"
author: "eduardpantazi"
published_at: "2026-11-19T21:16:46Z"
captured_at: "2026-11-20T09:45:52+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-11-20"
pub_day: "2026-11-19"
tags:
  - 语料
  - hn_show
  - author_eduardpantazi
  - story_50566502
  - show_hn
metrics: {"points": 2, "comments": 0, "engagement_velocity": 2}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:3d"
---

# Show HN: A SEO Tool to get found by Google and get cited by AI

> [!info] 一句话导读
> Skip to content Mozolite Leaderboard Free tools Blog Pricing Sign in Scan a site

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50566502>
> 指标：点赞=2 · 评论=0 · engagement_velocity=2
> 作者：eduardpantazi　|　发布：2026-11-19T21:16:46Z
> 项目链接：<https://mozolite.com/>
> 采集：2026-11-20T09:45:52+08:00　|　id：`27da3fcdd94386bc`

## 正文

Skip to content Mozolite Leaderboard Free tools Blog Pricing Sign in Scan a site
Get found on Google Bing DuckDuckGo and in AI answers .
 Scan your page to see what keeps it from ranking, then fix it in order.
Website address
 Run free scan
Free account, no card. First report in full, then $3 each or lifetime. See pricing
Google
 Bing
 DuckDuckGo
 Brave
 ChatGPT
 Claude
 Perplexity
 Gemini
 Get discovered on major search engines and AI assistants. Mozolite is not affiliated with these companies.
One score, and what it means for search
 First, a report says in one plain sentence whether search engines can find the page. Then it shows the search readiness score and how many things need fixing.
 Search counts for 40% of the score
 Five steps: crawl, index, appear, speed, quality
 Each step says how many things to fix or review
n northwind-bakery.com
 Mobile
 Sample report
 Scanned in 21.4 s
Search engines can find this page. 8 open issues affect how it is found and ranked.
 Search issues 8
 To fix in total 6
 Page weight 2.41 MB
71 Needs work
 Search readiness
0 1 Crawl Can search engines reach this page? 1 to fix
 0 2 Index Will the page be kept in the index? 1 to fix
 0 3 Appear How will it look in results and AI answers? 1 to fix
 0 4 Speed Does it load fast enough? 3 to fix
 0 5 Quality Is it safe and usable for everyone? All clear
Findings you can hand to someone else
 Most audit tools name the problem and stop. Instead, each Mozolite finding says what is wrong, why it matters for search and what to change, with the files it applies to.
 What is wrong? One sentence a client can read, without the jargon.
 Does it affect search? A note when the issue touches crawling, indexing or ranking.
 What do I change? The fix in plain words, in the order to do it.
 Where exactly? The files or elements involved, with sizes and timings.
A typical audit line
 Eliminate render-blocking resources
 Potential savings of 1,240 ms
The same finding in a Mozolite report
 No render-blocking resources Affects search High impact 4 resources 4 resources
 Two stylesheets and two scripts in the head stop the page from painting until they finish downloading. On a slow phone that adds about 1.2 seconds before anything shows.
 Why it matters for search: Blocking files delay Largest Contentful Paint, a Core Web Vital.
 How to fix
 Add defer to analytics.js and slider.js. Put the CSS for the first screen inline, then load theme.css and fonts.css after it.
File Size Blocks for
 /assets/theme.css 82.3 KB 520 ms
 /assets/slider.js 59.8 KB 310 ms
 /assets/analytics.js 44.7 KB 260 ms
 /assets/fonts.css 9.2 KB 150 ms
Start here
 1 Main content is in the HTML before JavaScript runs Index 38% in the HTML
 2 www and non-www lead to one address Crawl Both answer
 3 AI assistants can fetch this page to answer a question Appear 4 of 6 blocked
See the page the way a search result shows it
 The report draws your title and description as a search result and checks their length. It also measures how easy the text is to read.
 Title and description checked against what fits
 Reading ease on the Flesch scale, with the numbers behind it
 Checks for AI assistants sit in the same step
How it can look as a search result
 n northwind-bakery.com https://northwind-bakery.com
 Northwind Bakery: sourdough and pastries baked daily
 Fresh sourdough, croissants and seasonal cakes from our ovens in Portland. Order before 2 pm for pickup the same day, or have it delivered.
Title : 52 characters 25 to 60 fits
 Description : 139 characters 70 to 160 fits
Reading ease (Flesch)
 64 of 100
 Plain English
Very hard Hard Fairly hard Plain English Very easy
School grade 8 Aim for 9 or lower
 Words per sentence 15.2 Aim for 20 or fewer
 Long words 11% Aim for 15% or less
Loading times, and what the page weighs
 Five timings are measured in a real browser, and each one is placed on its good and poor range. The weight of the page is also split by file type.
 LCP, CLS and the other timings search engines look at
 Scripts, images, fonts and styles by size
 Every file listed, largest first, in the full report
Loading timings
 Good Needs work Poor
LCP Largest Contentful Paint Core Web Vital
 When the largest thing on screen has finished drawing.
3.4 s
 Needs work
2.5 s 4.0 s
CLS Cumulative Layout Shift Core Web Vital
 How much the layout jumps around while loading.
0.04
 Good
0.10 0.25
TBT Total Blocking Time
 How long the page was too busy to react to a tap.
180 ms
 Good
200 ms 600 ms
FCP First Contentful Paint
 When the first text or image shows up.
2.1 s
 Needs work
1.8 s 3.0 s
TTFB Time to First Byte
 How long the server took to start answering.
1.4 s
 Needs work
800 ms 1.8 s
Where the bytes go
 2.41 MB in 74 requests
See the files
Scripts 1.13 MB 47 % · 21 files
 Images 724.6 KB 29 % · 28 files
 Fonts 261.7 KB 11 % · 4 files
 Styles 147.5 KB 6 % · 6 files
 Document 93.8 KB 4 % · 1 file
 Data 87.9 KB 4 % · 14 files
 Where the bytes go
 2.41 MB in 74 requests. Sizes are as transferred, after compression.
Everything 2.41 MB 74 files 100 % of the page
 Scripts 1.13 MB 21 files 47 % of the page
 Images 724.6 KB 28 files 29 % of the page
 Fonts 261.7 KB 4 files 11 % of the page
 Styles 147.5 KB 6 files 6 % of the page
 Document 93.8 KB 1 file 4 % of the page
 Data 87.9 KB 14 files 4 % of the page
Everything 2.41 MB Scripts 1.13 MB Images 724.6 KB Fonts 261.7 KB Styles 147.5 KB Document 93.8 KB Data 87.9 KB
 Sort Largest first Name, A to Z Grouped by host Third party only
Everything
 0 files listed, 0 B
This report was made before file lists were saved. Scan the page again to see them.
Sample report. The panels are the ones your own report is built from.
 Three ways to hand it over
Share link
 Anyone with the link can read the report. They do not need an account.
PDF
 Save the full report as a PDF for a proposal or an email.
JSON
 Export every check for a ticket tracker or a script.
Everything that decides whether a page gets found
 A page has to be reached, kept, shown, loaded fast and trusted. So Mozolite checks each step, and the report follows the same order.
1 Crawl
 15 checks
 Can search engines reach this page?
 Status code, redirects and broken requests
 robots.txt, sitemap, and whether the page is in it
 HTTPS, the TLS certificate, www and non-www
 Links a crawler can follow
2 Index
 17 checks
 Will the page be kept in the index?
 noindex, canonical and where the canonical leads
 Content that only shows up with JavaScript
 Sitemap, robots.txt and the page telling the same story
 Soft 404s, meta refresh, hreflang that links back
3 Appear
 24 checks
 How will it look in results and AI answers?
 Title width in pixels, description and headings
 Rich result fields, breadcrumbs and the site name
 Share image size, favicon size, alt and link text
 AI assistants: crawler access, opt-out tags, llms.txt
4 Speed
 20 checks
 Does it load fast enough?
 Core Web Vitals: LCP, CLS and TBT, measured in Chrome
 Render-blocking files, unused JavaScript, page weight
 Image formats, sizing and lazy loading
 Mobile viewport and content width
5 Quality
 125 checks
 Is it safe and usable for everyone?
 Accessibility: WCAG 2.2 A and AA rules via axe-core
 Security: TLS version, HSTS, CSP, cookies
 Console errors, HTTP/2, doctype and charset
 Readability: Flesch Reading Ease and grade level
Ranked by search impact
 The report opens with the open issues that affect search, most important first, whichever step they come from.
Scan a page
How the score is worked out
 Here is the sample report's score, worked out with the same code that scores your page.
1 Each check scores 0 to 1
 A pass scores 1, a fail 0, and partial results land in between. Also, checks that matter more for search weigh more: high impact counts 10, medium 6, low 3. Finally, an area score is the points earned out of the points possible.
 SEO 38.5 of 54 points = 71
n northwind-bakery.com · Sample report SEO checks Score Weight Points
 Page returns a successful status code 200 OK 200 OK 1 10 10
 Page can be indexed Yes Yes 1 10 10
 Title tag has a useful length 641 px wide 641 px wide 0.5 10 5
 Meta description is present and sized well Missing Missing 0 6 0
 Page has a single H1 heading 1 heading 1 heading 1 6 6
 Canonical URL is set correctly Points to itself Points to itself 1 6 6
 Structured data is valid JSON-LD 2 errors 2 errors 0 3 0
 Links are crawlable 3 of 48 not 3 of 48 not 0.5 3 1.5
 38.5 of 54 points
 SEO 71
2 Timings follow the Lighthouse curves
 Five timings are measured in a real Chrome and placed on the curves Lighthouse uses. For example, on mobile a largest paint at 2.5 seconds scores 0.9 and one at 4 seconds scores 0.5. Of the five, Total Blocking Time weighs most.
 Performance 61.9 of 100 points = 62
n northwind-bakery.com · Sample report Loading timings
 Good Needs work Poor
FCP First Contentful Paint
 When the first text or image shows up.
2.4 s
 Needs work
1.8 s 3.0 s
LCP Largest Contentful Paint Core Web Vital
 When the largest thing on screen has finished drawing.
4.3 s
 Poor
2.5 s 4.0 s
TBT Total Blocking Time
 How long the page was too busy to react to a tap.
580 ms
 Needs work
200 ms 600 ms
CLS Cumulative Layout Shift Core Web Vital
 How much the layout jumps around while loading.
0.13
 Needs work
0.10 0.25
TTFB Server response (TTFB)
 How long the server took to start answering.
1.0 s
 Needs work
800 ms 1.8 s
FCP
 0.71 × 10
 7.1
LCP
 0.42 × 25
 10.5
TBT
 0.52 × 30
 15.6
CLS
 0.82 × 25
 20.5
TTFB
 0.82 × 10
 8.2
61.9 of 100 points
 Performance 62
3 SEO counts most in the overall score
 Each area adds its score times its weight: SEO 40%, Performance 25%, Accessibility 15%, Security 10%, Best practices 10%. When an area could not be measured, it drops out and the others share its weight.
 Overall 28.4 + 15.5 + 12.9 + 4.8 + 9.5 = 71.1
 Good 90 to 100
 Needs work 50 to 89
 Poor 0 to 49
n northwind-bakery.com · Sample report SEO 71 × 40 % 71 × 40 % = 28.4
 Performance 62 × 25 % 62 × 25 % = 15.5
 Accessibility 86 × 15 % 86 × 15 % = 12.9
 Security 48 × 10 % 48 × 10 % = 4.8
 Best practices 95 × 10 % 95 × 10 % = 9.5
 Sum of the five shares
 71.1
 Rounded to 71. The leaderboard ranks on the unrounded number, so ties still sort.
71 Needs work
 Search readiness
Made for people who get websites found
B bakery.example 3 fixes worth doing first 58
Home page is set to noindex Title cut off at 720px Share image does not load
 mozolite.com /report/k3x9q Copied
Freelancers
 Open the sales call with proof
 Send a lead the report before you meet. That way they see what holds the site back in search, ranked, and you name the price to fix it.
 Share link
 Ranked fixes
studio.example Scan history
 Before Oct 2 54 After Nov 14 88
 +34 points
 PDF for the handover
Agencies
 Show what the redesign changed
 Scan before the work and again after it. Clients read the report without an account, and then the PDF goes into the handover.
 Scan history
 PDF export
shop.example/new Before launch
 robots.txt allows Googlebot
 The page is in the sitemap
 noindex left over from staging Fix
 Title fits in the result
Site owners
 Catch it before Google does
 Scan the page before launch. That way you find the stray noindex, the broken sitemap or the title that gets cut off first.
 First report free
 No card
Compared with Lighthouse
 Lighthouse is free and excellent for performance work. Here is what Mozolite adds for search.
Feature Lighthouse Mozolite
 Core Web Vitals in real Chrome
 Basic SEO checks: title, description, crawlable links
 Sitemap coverage, www and non-www, content that needs JavaScript
 Where the canonical leads, soft 404s, sitemap and hreflang conflicts
 Rich result fields, share image and favicon size, site name
 AI visibility: assistant access, opt-out tags, publisher data, llms.txt
 Security headers, TLS and cookies
 Issues ranked by search impact with plain fixes
 Shareable report link and PDF
 Scan history
 Read the full comparison
Pricing
 A free account opens your first report in full. Then pay per report, or once for lifetime access.
Free
$0
 A free account, no card
 3 scans with a free account
 The first one as a full report
 All five scores and Core Web Vitals
 Top issues in each category
 Every free tool
Run a free scan
Pay per report
$3 per report
 Buy one or a few. No subscription.
 Every check that applies, up to 201
 Element-level details and fixes
 PDF and JSON export
 Shareable link for clients
 Credits never expire
1 report
 Buy for $3
Lifetime
 Best value
 $29 $24 once
 Founding price. 12 of 15 spots left.
 Black Friday Discount
 Enter the code at checkout for $5 off .
 BLACK5DAY Copy
Unlimited full reports (fair use, 300 per 30 days)
 Everything in pay per report
 Scan history in your dashboard
 Priority in the scan queue
 MCP server for Claude Code, Cursor and other AI tools
 All future checks and tools
Get lifetime access for $24
Payments secured by
First report free
 A free account, no card.
Pay once
 No subscription. Credits never expire.
Your page stays yours
 We keep the results, not your HTML or visitors.
Secure checkout
 Paid through Creem, the merchant of record.
Free tools
 Single checks you can run without an account.
All tools
 Security headers checker
 See which HTTP security headers a page sends, which ones are missing, and the exact line to add.
Open tool
 Meta tags and Open Graph checker
 Check the title, description, canonical and social tags of any page, and preview how it looks when shared.
Open tool
 Favicon checker
 Find every icon a site declares and see how each one looks in a browser tab, a Google result and on phone home screens.
Open tool
 Robots.txt tester
 Fetch a site's robots.txt, find its sitemap, and test whether a path is allowed for a specific crawler.
Open tool
 Redirect checker
 Follow every redirect hop from a URL to its final destination, with status codes, and check that HTTP upgrades to HTTPS.
Open tool
 AI crawler access checker
 See whether ChatGPT, Claude, Perplexity, Gemini and other AI crawlers are allowed to read a page, and whether the site has an llms.txt file.
Open tool
From the blog
 All articles
 Nov 19, 2026 · 4 min read
 AI Visibility Checklist: Guide to Get Cited by ChatGPT, Claude, Gemini and Copilot
 A short, practical checklist to help AI assistants find, read and cite your pages. Covers crawler access, content, structure, trust signals and tracking.
Nov 19, 2026 · 10 min read
 How Core Web Vitals Affect Google Rankings
 Core Web Vitals are a real Google ranking signal, but they don't decide everything. Learn what LCP, INP and CLS mean, the scores to aim for, and what to fix first.
Questions
Something else? Write to hello@mozolite.com .
Will a higher score improve my rankings? A score is not a ranking. The checks cover what search engines have documented: whether a page can be crawled and indexed, how it loads, and how it is described. Fixing them removes obstacles, but what you publish and who links to you still decide where you rank.
 How is this different from PageSpeed Insights? PageSpeed Insights runs Lighthouse, which is strong on performance but light on SEO. Mozolite measures the same Core Web Vitals with the same scoring curves, and also checks sitemap coverage, redirects, content that needs JavaScript, AI crawler access and security. The report is written so you can send it to someone who is not a developer.
 Why is my score different from PageSpeed Insights? Performance scores move between runs on every tool, because network and server timing change. We load your page in a real Chrome with mobile throttling applied, while PageSpeed Insights simulates the throttling. Our overall score also weights SEO most, so it is not the same number as a Lighthouse average.
 Does it check the whole site? No. One scan covers one page, plus the site files that affect it: robots.txt, the sitemap and llms.txt. So scan your most important pages one by one.
 Is it really free to start? Yes. A free account needs only your email, no card. Your first scan opens as the full report, with every check, its element details and fixes. You also get 2 more scans as previews, with all five scores, the Core Web Vitals and the top issues. After that, a full report costs $3 or comes with lifetime access.
 Can I scan pages behind a login? No. We only scan public URLs, the same way a search engine or a new visitor would see them.
 What do you store? The report results and a small screenshot of the first screen. We do not keep the page HTML or anything from your visitors.
See how search engines read your page
 Paste a URL and create a free account. Your first report opens in full.
 Website address
 Run free scan
Mozolite SEO audits you can read in five minutes . Built for freelancers, agencies and people who run their own sites.
Product
 Run a scan
 Pricing
 Leaderboard
 Dashboard
 Compared with Lighthouse
 MCP server
Free tools
 Security headers
 Meta tags
 Favicon
 Robots.txt
 Redirects
Company
 Blog
 Contact
 Media kit
 Terms of use
 Privacy
 Cookies
 Sitemap
© 2026 Mozolite
 Payments handled by Creem. Prices in USD.

## 关联链接

- https://northwind-bakery.com

## 导航

- 项目页：[[10-项目/mozolite.com_8725fcba]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
