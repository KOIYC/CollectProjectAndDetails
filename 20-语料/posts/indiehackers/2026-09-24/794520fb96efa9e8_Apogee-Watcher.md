---
type: "corpus"
item_id: "794520fb96efa9e8"
title: "Apogee Watcher"
source: "indiehackers"
source_name: "Indie Hackers 产品库"
url: "https://www.indiehackers.com/product/apogee-watcher"
project_url: "https://apogeewatcher.com/blog/when-to-use-synthetic-vs-real-user-monitoring-performance"
captured_at: "2026-10-22T09:48:20+08:00"
lang: "en"
kind: "project"
topic: "开发者工具"
shard: "2026-09-24"
tags:
  - 语料
  - indiehackers
metrics: {}
comments_count: 0
comments_total: 0
discovered_via: "ih:products"
---

# Apogee Watcher

> [!info] 一句话导读
> Home Starting Up Case Studies DB Products Ideas DB Vibe Coding Tools Subscribe to IH+

> [!meta]- 语料信息（点开展开）
> 来源：Indie Hackers 产品库（project）
> 原帖：<https://www.indiehackers.com/product/apogee-watcher>
> 指标：—
> 作者：—　|　发布：—
> 项目链接：<https://apogeewatcher.com/blog/when-to-use-synthetic-vs-real-user-monitoring-performance>
> 采集：2026-10-22T09:48:20+08:00　|　id：`794520fb96efa9e8`

## 正文

Home Starting Up Case Studies DB Products Ideas DB Vibe Coding Tools Subscribe to IH+
Starting Up Case Studies
 Ideas DB Products DB Sign in Join
Apogee Watcher
 Solving web performance for agencies and solopreneurs
Visit Website
Apogee Watcher Solving web performance for agencies and solopreneurs
 Posts 30+
 Revenue $0 / mo
 Website Twitter
Brotli and Gzip Compression: Shrink Text Assets Without Breaking PageSpeed Scores
The CDN dashboard says compression is on. A host panel lists Brotli as enabled. Then a lab run on the priority URL still flags Enable text compression, or the Performance score barely moves while Time to First Byte gets worse after someone raised the Brotli level on dynamic HTML.
 In our experience that gap is rarely "nobody turned compression on." It is a mismatch between which responses are compressed, which layer applies Content-Encoding, and what Lighthouse actually measures on that URL. Brotli usually wins on HTML, CSS, and JavaScript; gzip stays the fallback when br is unavailable. The win is text on the wire, not a second envelope around JPEG, PNG, or WebP.
 What we recommend agencies verify after every deploy:
 1. Compress text/html, CSS, JavaScript, JSON, and SVG; leave already-compressed images and fonts alone.
 2. Prefer Brotli when negotiation succeeds, with gzip as the safety net.
 3. Precompress static fingerprinted assets at build time; keep moderate quality for dynamic HTML so origin CPU does not inflate TTFB.
 4. Request each failing audit URL with Accept-Encoding: br, gzip and confirm Content-Encoding before chasing the green tick alone.
 5. Re-run the same lab profile after the change and watch TTFB and LCP, not only the Enable text compression audit.
 Double compression, wrong MIME allow-lists, and max Brotli quality on uncached HTML are the failure modes we still see on client portfolios. Compression sits beside Cache-Control and CDN rules; it is not a substitute for fixing an oversized LCP image.
 Read more: Brotli and gzip compression for PageSpeed
Apogee Watcher
2 Upvotes
1 Comment
TTFB Won't Go Down? Server-Side Culprits Beyond the Theme
You put the site behind a CDN, trimmed the theme, deferred scripts, and still watch Waiting (TTFB) eat the PageSpeed Insights waterfall. The next ticket proposes a bigger hosting plan. In our experience that upgrade often treats the symptom while the origin keeps doing too much work per uncached request, or background jobs steal capacity when real visitors arrive.
 When DNS and TLS are already short, high Time to First Byte is almost always origin processing: PHP execution, database queries, remote calls inside the page build, or contention from other jobs on the same machine. A page cache can hide this until a logged-in session, cart cookie, or query-string variant bypasses the edge. Lab tests then look slow while marketing reports that the CDN is on.
 Server-side checklist we walk before the next hosting invoice:
 Disable request-driven WP-Cron; trigger due events from system cron on a fixed interval, then compare TTFB at :05 and :55 past the hour
Confirm OPcache, sensible PHP worker counts, and warm critical URLs after deploy so cold workers are not the whole story
Add Redis or Memcached object cache; audit fat wp_options autoload rows and N+1 queries on the uncached path
Watch admin-ajax volume in access logs; move backup and scanner plugins off peak in the site traffic timezone
Re-test the same priority URL on an uncached miss, not only the cached marketing homepage
TTFB is not a Core Web Vital, but it still gates LCP because the main content cannot paint until HTML arrives. Fix origin compute on the miss path before doubling RAM.
 Read more: reduce TTFB when CDN and theme fixes fail
Apogee Watcher
11 Upvotes
Comment
How Lighthouse Performance Scores Are Recorded and Calculated
You paste a client URL into PageSpeed Insights and the green circle pops up. The account manager forwards it as "Google speed." That number is a lab Performance score from one controlled run. It is not a ranking factor by itself, and it is not a Chrome User Experience Report percentile.
 Lighthouse records metrics under a throttled profile (mobile or desktop), maps each raw value through an HTTP Archive scoring curve, then blends those metric scores with documented weights. Under Lighthouse 10 the blend is Total Blocking Time 30%, Largest Contentful Paint and Cumulative Layout Shift 25% each, First Contentful Paint and Speed Index 10% each. Opportunities and Diagnostics do not add points directly; they explain what might move the underlying metrics.
 What agencies keep mixing up on the same PSI screen:
 Lab Performance is synthetic, versioned, and fast after a deploy
Field Core Web Vitals come from CrUX over a rolling window, with INP instead of TBT
Colour bands (0–49 / 50–89 / 90–100) describe that lab run, not every visitor on every network
A five-point swing across a Lighthouse major can be scoring math, not a regression
How we report the number without score-chasing:
 Name the artefact: Lighthouse / PSI lab Performance, plus device and Lighthouse major when known
Show the drivers: LCP, TBT, and CLS usually explain most of the blend
Keep CrUX / Search Console on a separate slide
Prefer three or more scheduled runs over one heroic paste after a tag change
Open the Lighthouse scoring calculator before promising "ten points is one easy fix"
Apogee Watcher stores those lab scores on a schedule across listed URLs so you compare like with like. Pair the trend with metric budgets on money pages. Layer field status separately when samples exist.
 Read more: how Lighthouse performance scores are recorded and calculated
Apogee Watcher
15 Upvotes
2 Comments
How to measure LCP and INP in Safari 26.2 (and what still only Chrome reports)
For years, agency Core Web Vitals programmes had a quiet Safari blind spot. Chrome users filled CrUX, Search Console, and PageSpeed Insights field panels. Safari users on iPhone and Mac still felt slow pages, yet JavaScript often never saw largest-contentful-paint or Event Timing entries in WebKit.
 Safari 26.2 (12 December 2025) adds the Largest Contentful Paint API and the Event Timing API in WebKit. You can collect LCP and INP from real Safari sessions through PerformanceObserver, web-vitals , or your RUM vendor. Metric definitions did not change. What changed is whether Safari emits the entries at all.
 What still stays Chrome-only in Google's public field tools:
 CrUX remains a Chrome-user sample
Search Console's Core Web Vitals report still draws on that CrUX world
PageSpeed Insights field blocks stay Chrome-skewed even after you instrument Safari RUM
Scheduled Lighthouse / PSI lab runs stay useful for deploy regression, not as Safari field percentiles
Agency checklist we use once Safari 26.2+ volume appears:
 Confirm Safari version share for priority clients before rewriting SLAs
Upgrade or verify RUM so onLCP / onINP actually receive Safari sessions
Baseline by browser family for two to four weeks
Keep CrUX and Search Console as the Chrome field story for SEO conversations
Re-check Safari INP outliers on a physical device before escalating spikes
Apogee Watcher stays on the portfolio and deploy side: scheduled PageSpeed tests, budgets, and alerts across listed URLs. Safari field collection belongs in your RUM or first-party web-vitals pipeline. Layer the two. Do not pretend a lab score is a Safari percentile.
 Read more: how to measure LCP and INP in Safari 26.2
Apogee Watcher
18 Upvotes
2 Comments
October 21, 2026
 Partial Page Loads in CrUX: What Field Data Includes (and Excludes)
You finish a PageSpeed Insights lab run on Tuesday. Largest Contentful Paint is green under the fixed profile. On Thursday Search Console still shows the URL amber in the Chrome UX Report field panel. The client asks which screenshot is wrong. Neither is. The lab profile finished by design. CrUX is aggregating many real Chrome visits, including ones that never matched that quiet network window.
 That is what people mean by partial page loads or partial sessions in CrUX. The phrase is not a public metric name. It covers abandoned or interrupted loads, pages that start in a background tab, back/forward cache restores, and SPA soft navigations that still sit on one document URL in classic Core Web Vitals reporting. Field data answers what happened across eligible experiences. Lighthouse answers what one controlled navigation did.
 What we keep on the deck when lab and field disagree:
 Label both clocks: dated lab URL, strategy, and profile beside CrUX form factor and collection window.
Do not treat every field metric as the same navigation set. TTFB often skips restore paths that still contribute LCP.
Align synthetic budgets with revenue and conversion templates, not only the quiet brochure URL that scored well in the lab.
For SPA-heavy products, add route-aware RUM or soft-navigation debugging until classic CrUX tooling clearly splits those routes.
A green lab card is useful regression evidence. It is weak proof that field percentiles will flip by Friday.
 Read more: partial page loads in CrUX field data
Apogee Watcher
5 Upvotes
1 Comment
October 20, 2026
 Why CrUX Has No Data for Your Site
A client forwards a PageSpeed Insights screenshot. Lab scores fill the lower half. The field block at the top says Chrome UX Report data was not found. Someone asks whether the tool is broken. It usually is not.
 CrUX only publishes field percentiles when enough opted-in Chrome sessions meet privacy and quality rules for that origin or URL. PageSpeed Insights and Search Console inherit those gaps. Lighthouse can still look complete on the same screen, which is why teams treat a blank field section as a tooling failure instead of an eligibility outcome.
 Before you promise a timeline for field data, name the gate:
 Confirm the origin string (HTTPS, www or apex). HTTP versus HTTPS and www versus apex are different origins; so are subdomains.
Check that the root is publicly discoverable (indexable, successful HTTP status). Redirect-heavy or blocked roots are a common trap.
Separate origin-absent from URL-thin: origin field data can exist while a landing path still has no URL-level rows.
Do not invent a Core Web Vitals fail from a blank field block. Missing CrUX is not a ranking penalty by itself.
Until field samples exist, keep scheduled lab budgets on the homepage and other priority URLs so the retainer still has numbers to report.
You cannot manually submit a site into CrUX. Fix discoverability, grow real Chrome traffic, and re-check on a fixed schedule. Synthetic history covers the gap until origin or URL field rows appear.
 Read more: why CrUX has no data for your site
Apogee Watcher
1 Upvote
Comment
October 20, 2026
 Why CrUX Has No Data for Your Site
A client forwards a PageSpeed Insights screenshot. Lab scores fill the lower half. The field block at the top says Chrome UX Report data was not found. Someone asks whether the tool is broken. It usually is not.
 CrUX only publishes field percentiles when enough opted-in Chrome sessions meet privacy and quality rules for that origin or URL. PageSpeed Insights and Search Console inherit those gaps. Lighthouse can still look complete on the same screen, which is why teams treat a blank field section as a tooling failure instead of an eligibility outcome.
 Before you promise a timeline for field data, name the gate:
 Confirm the origin string (HTTPS, www or apex). HTTP versus HTTPS and www versus apex are different origins; so are subdomains.
Check that the root is publicly discoverable (indexable, successful HTTP status). Redirect-heavy or blocked roots are a common trap.
Separate origin-absent from URL-thin: origin field data can exist while a landing path still has no URL-level rows.
Do not invent a Core Web Vitals fail from a blank field block. Missing CrUX is not a ranking penalty by itself.
Until field samples exist, keep scheduled lab budgets on the homepage and other priority URLs so the retainer still has numbers to report.
You cannot manually submit a site into CrUX. Fix discoverability, grow real Chrome traffic, and re-check on a fixed schedule. Synthetic history covers the gap until origin or URL field rows appear.
 Read more: why CrUX has no data for your site
Apogee Watcher
1 Upvote
Comment
October 19, 2026
 Lazy Loading for LCP and CLS: When to Use loading="lazy" (and When Not To)
A theme update lands on Tuesday. The speed plugin ticks "lazy load all images." By Thursday PageSpeed Insights names the hero as LCP and resource load delay jumps. The gallery below the fold is lighter. The first paint is not.
 Native loading="lazy" is a browser hint for offscreen media, not a global faster switch. When WordPress, Shopify, or a page builder injects it on every attachment, the LCP candidate often sits in that list. The browser may defer a fetch for an image that is already in the viewport. Lighthouse and PSI show the delay; CrUX follows when mobile traffic paints that same hero.
 What we use before anyone ships "lazy everything":
 Keep the confirmed LCP image eager (or explicit loading="eager" ) on mobile and desktop breakpoints.
Lazy-load body photos, related grids, footer badges, and other scroll-first media.
Reserve width and height or aspect-ratio on lazy and eager images alike so CLS does not rise when bytes arrive.
Re-check money URLs in lab after the attribute change; watch LCP element identity and load delay, not only the score.
Eager heroes and lazy galleries travel together. Write the exclusion list into the theme or retainer runbook so the next plugin install does not reverse it quietly.
 Read more: lazy loading for LCP and CLS: when to use loading="lazy"
Apogee Watcher
2 Upvotes
Comment
October 18, 2026
 WordPress Speculation and Prerender Plugins vs Core Web Vitals
A retainer client installs a wordpress prerender plugin on Tuesday. By Thursday the account lead forwards a PageSpeed Insights screenshot: homepage LCP still amber, yet the demo walkthrough from article to related post feels instant in Chrome. Two clocks, one ticket.
 WordPress 6.8 already ships speculative loading as Core behaviour for most logged-out front ends: conservative prefetch around the start of a click. The Speculative Loading plugin (and third-party prefetch tools) often push toward prerender with moderate eagerness. That can warm the next navigation and help Interaction to Next Paint on the path the user actually takes. It does not fix a cold landing from search, and broad prerender on mega-menus can waste bandwidth while the current page still fights for main-thread time.
 What we use on agency audits before anyone flips another speed toggle:
 Name the owner: Core defaults, the Speculative Loading plugin, or a stack of hover-prefetch scripts. Overlap is common.
Exclude cart, checkout, account, and GET action URLs before raising eagerness to prerender.
Judge first-visit LCP and CLS on the entry template separately from next-page feel after speculation.
Re-run the same lab profile on priority URLs after the change; watch TTFB and LCP, not only a green Instant Page demo.
Speculation multiplies whatever the destination loads. It is not a substitute for fixing the LCP resource on the URL paid traffic actually hits.
 Read more: WordPress speculation rules and prerender plugins vs Core Web Vitals
Apogee Watcher
4 Upvotes
Comment
October 17, 2026
 TTFB Is Not Only the Server: The Unattributed Slice Agencies Should Name in Reports
Monthly report deck. High Waiting (TTFB) bar from PageSpeed Insights. Someone writes "server response" under it. The hosting ticket opens before anyone asks what else sat inside that first-byte clock.
 In the browser, Time to First Byte is wider than origin PHP. Redirects, DNS, connection setup, TLS, network latency, CDN work, and browser overhead can all share the same number. Unattributed Navigation Overhead (UNO) is the residual after you subtract the phases Navigation Timing can name: redirect, DNS, connection, and request to responseStart. Harry Roberts documented the metric; agencies still leave that leftover unnamed, so it inherits the server label by default.
 CrUX can show field TTFB is poor. It cannot decompose phases. Without a Navigation Timing breakdown from real navigations (or a careful local reproduction), the whole bar looks like hosting. Hidden cross-origin hops (shorteners, trackers, even http to https) often inflate UNO while redirectCount stays at zero.
 What we want on the client slide before anyone upgrades the plan:
 Calculate UNO = TTFB minus redirect, DNS, connection, and request to responseStart (floor at zero)
Label the residual as unexplained navigation time inside TTFB, not another name for "server"
Segment campaign and referrer landings when UNO rises and lab on the final URL looks fine
Hand off to origin work only when the attributed request to first-byte span still dominates
Name the slice first. Then open the right ticket.
 Read more: TTFB is not only the server: unattributed navigation overhead
Apogee Watcher
4 Upvotes
Comment
About
 Agencies managing many sites need automated Core Web Vitals monitoring, alerts, and client-ready reports. Not fragile Lighthouse CI, costs that spiral, or enterprise-only multi-tenant. Manual checks do not scale.
 People
 Apogee Watcher Founder
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

- 项目页：[[10-项目/Apogee-Watcher_251434df]]
- 渠道页：[[50-渠道/indiehackers]]
- 赛道：`开发者工具`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
