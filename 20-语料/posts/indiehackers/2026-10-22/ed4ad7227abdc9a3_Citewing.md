---
type: "corpus"
item_id: "ed4ad7227abdc9a3"
title: "Citewing"
source: "indiehackers"
source_name: "Indie Hackers 产品库"
url: "https://www.indiehackers.com/product/citewing"
captured_at: "2026-11-07T09:46:15+08:00"
lang: "en"
kind: "project"
topic: "AI 工具/Agent"
shard: "2026-10-22"
tags:
  - 语料
  - indiehackers
metrics: {}
comments_count: 0
comments_total: 0
discovered_via: "ih:products"
---

# Citewing

> [!info] 一句话导读
> Home Starting Up Case Studies DB Products Ideas DB Vibe Coding Tools Subscribe to IH+

> [!meta]- 语料信息（点开展开）
> 来源：Indie Hackers 产品库（project）
> 原帖：<https://www.indiehackers.com/product/citewing>
> 指标：—
> 作者：—　|　发布：—
> 项目链接：—
> 采集：2026-11-07T09:46:15+08:00　|　id：`ed4ad7227abdc9a3`

## 正文

Home Starting Up Case Studies DB Products Ideas DB Vibe Coding Tools Subscribe to IH+
Starting Up Case Studies
 Ideas DB Products DB Sign in Join
CiteWing
 Get recommended by AI
Visit Website
CiteWing Get recommended by AI
 Posts 7
 Website
November 6, 2026
 I made $0 from SEO for 5 months, then 2 mentions in AI-cited lists brought 31 signups in a week
Ok so for five months I basically got nothing from SEO, like I was writing posts every week and maybe got 40 visitors a day on a good day, and the money side was a flat zero lol. Honestly I was about to give up on content and just throw the little budget I had left at ads, which felt awful tbh
 Then I started checking which pages chatbot answers were pulling from when people asked stuff like best invoicing software for freelancers, and it was mostly old listicles nobody had touched in years. I picked two that were a bit outdated but still relevant, found the person who maintained each page, and sent a short note asking if they'd consider adding a mention, nothing salesy, just what CiteWing does for people in that niche and why I thought it fit their list
 Both replied within three days, one said yes right away and the other wanted a screenshot of the feature which was fine. Within a week I had 31 signups, and I'd guess like 20ish came from clicks off those two listings, maybe 6 from Google after that, and the rest I genuinely can't trace back to anything. Part of me thinks I just got lucky with timing, part of me thinks the pitch was specific enough that the owners didn't feel like they were getting spammed
 The part that isn't working is directories, I submitted to like 15 of them and got maybe 2 approvals, and most of my cold emails to random blogs just get ignored, so I'm still stuck on how to find pages that get cited instead of just pages that rank. Right now I'm mostly guessing which ones are worth the email and that feels kinda like starting over every time
Tom Han
5 Upvotes
6 Comments
November 2, 2026
 Our 45 referring domains lose AI citations to a 2021 blog with 60, what's driving it?
For one query, the core one every founder in this space types in, I checked which pages the answer engines were citing. Three kept showing up: a comparison listicle on a big review site, a Reddit thread, and an old blog post from 2021. We rank above all three in regular results, which stung.
 Referring domains first. The listicle has maybe 400ish, the Reddit thread is linked from way more forums than that, the old blog has around 60, and we have roughly 45. So links alone don’t explain why a blog with fewer links than us keeps getting picked up.
 Then Search Console: the old blog gets impressions for a bunch of long-tail phrasings nobody else targets. Our page also had a canonical pointing at the wrong version after a template update in the fall, and two of the three cited pages get crawled much more often than ours. I don’t know yet whether crawl frequency matters for citations.
 My guess is the cited pages answer the question in the first two lines with a clean list, while ours buries the answer under a long intro. I’m fixing the canonical this week and restructuring the top of the page. I haven’t confirmed the canonical is what’s suppressing citations, so I’ll post an update if the fix changes anything. What I’m still unsure of is how much weight to put on structure versus links.
 I’m building a tool called CiteWing around this exact problem because doing this check by hand took me a week.
Tom Han
23 Upvotes
2 Comments
October 28, 2026
 pulled 60 pages that ChatGPT keeps citing for 'best [category] tools', only 9 had a contact email on the page
So I pulled the 60 pages that keep showing up when you ask ChatGPT for best tools in a category, mostly listicles and comparison posts from smaller blogs, what got me was only 9 of them had a contact email anywhere on the page, the rest meant digging through about pages or just guessing from the domain
 Matching them to owners took way longer than I thought, for each page I checked the footer, the about page, and the author byline, then wrote down whatever channel looked real, idk maybe 5 minutes a page on average, I kept a sheet with the page, the owner, the channel, and why it fit what I was pitching
 I used CiteWing to send the messages on autopilot, nothing fancy, just saying I saw the page in a list and asking if they'd be open to adding a mention or link if it made sense. Only a handful wrote back, a couple said no thanks, and one said they'd look into it and then went quiet, tbh I thought more people would at least reply
 The two who linked back had some stuff in common, both were smaller sites that updated their list posts pretty often, both had a real person's name on the page, and both had an active comment section. The stale pages run by faceless companies mostly ignored me. My sample is tiny so take it with a grain of salt :)
Tom Han
12 Upvotes
6 Comments
October 25, 2026
 Made 5 hidden test pages to see which AI bots read robots.txt, at least 3 skipped it
So I kept wondering if the bots crawling my sites check robots.txt before grabbing a page, everyone says the big ones respect it but nobody seems to post the logs to prove it?? so I set up a little experiment over a few weeks and used CiteWing to check whether any of the pages started showing up in AI answers, made five plain html pages on a test subdomain with nothing linking to them, not in the sitemap, no nav, zero links, then disallowed two of them in robots.txt and left the other three open
 Pulled the raw access logs and filtered by user agent, the annoying part was sorting real crawlers from scrapers faking a browser string so I checked the IPs against the published lists, biggest surprise was how fast a couple of them showed up, within hours even though nothing pointed at those pages
 A handful more came back over the next few days and at least three bots went straight to a page without requesting robots.txt first, which threw me off since that's literally the file they're supposed to read first, still not sure if that means they ignore it or just cached it from some request I can't see, and I don't know if they hit robots.txt from a different IP earlier so honestly the logs raise more questions than they answer tbh
Tom Han
15 Upvotes
9 Comments
October 23, 2026
 Agency wanted $1,800 a month for link building and the sample report had 14 links nobody visits
Agency pitched me $1,800 a month for link building last week and I was kinda ready to say yes, they attached a sample report with 14 links in it, almost all directory listings on sites with basically zero traffic, a couple were old business profiles still showing my old address??
 I asked which of those pages get any visitors and whether anyone in my niche reads them, the guy got vague and said directories are a good trust signal, when I asked what they would go after next he had no list, just said they would reach out to relevant sites once the retainer started so I would be paying every month to find out what they were even targeting
 So I spent a few evenings finding pages that already cite stuff in my space, the ones answering the which one is best questions, then emailed the owners myself with a short note, got a handful of replies which is honestly normal but way better than paying someone to guess
 The part I'm still stuck on is tracking where those links end up after someone says yes, some get edited later or removed and I only notice when rankings move, right now I use citewing to check every couple weeks where the links sit and it tells me when one disappears, I'd rather something watch the list and flag when a link disappears but I haven't found a setup I trust yet so it's still a spreadsheet
Tom Han
12 Upvotes
5 Comments
October 22, 2026
 Ran the same niche AI query for 3 weeks, 2 domains got cited in almost every run
For about three weeks I ran the same narrow query every couple days, the one about invoicing software for US freelancers, and logged every site the AI answers pointed to in their sources, boring work but kinda fun, I also ran it all through CiteWing so I could see when the cited sites shifted
 The thing that surprised me was how much the same domains kept repeating, the top two showed up in almost every run, one was a comparison blog and the other was a regional forum thread nobody I know reads, the weird one was an old freelancer guide that kept getting cited every single week even though the page hasn't been touched in years
 Then I emailed a couple of the site owners asking if they'd add a newer option to their list, one replied already and the rest are still quiet!!
 Two things stood out, the forum thread kept getting picked even when the main keyword barely showed up in its title, and the comparison blog skipped most of the bigger names in the niche which felt like a gap nobody was filling, idk if this is a real pattern or just a quirk of one query, I also switched browsers halfway through so the numbers might be off, not sure how much of it holds up yet
Tom Han
15 Upvotes
8 Comments
October 21, 2026
 50ish 'best alternatives' searches, same 3 page types every time, and that's where the paying buyers hang out
So I spent a weekend running like 50ish searches for best alternatives stuff in the AI answer engines people use now, mostly typing in the big names everyone compares for project management and CRM, and I kept a list of which pages got cited in the answers
 Three page types kept showing up, first were roundup listicles from smaller blogs that rank for best X alternatives and never get updated, second were comparison pages on review sites with a table and maybe five competitors, third were little resource lists on GitHub or inside newsletters, and honestly the big names were already in every single one which was not shocking tbh
 What got me is why the newer brands almost never make those pages, my guess is editors are swamped and most of them just assume the editor will find them, plus a lot of these pages only have a contact form that goes nowhere,I emailed a few myself and got zero replies which kinda stung
 Right now I put together CiteWing that finds these pages and checks whether the answer engines start mentioning a brand after you reach out, still early and the outreach part is the hard bit because nobody wants a template that reads like spam, I haven't figured that one out yet
Tom Han
15 Upvotes
3 Comments
About
 I’m building CiteWing because knowing your brand is missing from AI answers isn’t enough. Its agent finds articles AI cites and helps you contact publishers to earn mentions, so more buyers discover your product.
People
 Tom Han Founder
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

- 项目页：[[10-项目/Citewing_ed4ad722]]
- 渠道页：[[50-渠道/indiehackers]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
