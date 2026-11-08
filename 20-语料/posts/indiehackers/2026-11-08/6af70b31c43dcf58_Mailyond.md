---
type: "corpus"
item_id: "6af70b31c43dcf58"
title: "Mailyond"
source: "indiehackers"
source_name: "Indie Hackers 产品库"
url: "https://www.indiehackers.com/product/mailyond"
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

# Mailyond

> [!info] 一句话导读
> Home Starting Up Case Studies DB Products Ideas DB Vibe Coding Tools Subscribe to IH+

> [!meta]- 语料信息（点开展开）
> 来源：Indie Hackers 产品库（project）
> 原帖：<https://www.indiehackers.com/product/mailyond>
> 指标：—
> 作者：—　|　发布：—
> 项目链接：—
> 采集：2026-11-08T12:54:09+08:00　|　id：`6af70b31c43dcf58`

## 正文

Home Starting Up Case Studies DB Products Ideas DB Vibe Coding Tools Subscribe to IH+
Starting Up Case Studies
 Ideas DB Products DB Sign in Join
Mailyond
 One inbox for every domain you own
Visit Website
Mailyond One inbox for every domain you own
 Posts 3
 Revenue $0 / mo
 Website Twitter
October 24, 2026
 Using a free Chrome extension as a distribution channel for an email SaaS
I have 1 paying customer for Mailyond (one inbox for all your domains), so most of my time goes into getting it found, not building features.
 In October I added free DMARC, SPF, DKIM and MX checkers to the site. People who search for those usually own a domain and are fixing their email, which is close to who I'm selling to. This week the same checks went into a Chrome extension: you click it on any site and it shows that domain's records, each with a pass, warning or fail. There's a Full report link back to the checker on mailyond.com .
 Why an extension: the Chrome Web Store is a search engine I wasn't in yet, and the extension reuses the API my checkers already run on, so it cost me very little to build.
 A few things I didn't expect:
 The store rejected the first version in under 5 minutes for keyword spam. The description named the email providers it detects. Removing them fixed it.
It's in 9 languages. Claude Code wrote the descriptions and made localized screenshots, so translating cost almost nothing.
The Full report links have UTM tags, so I'll know how many people go from the extension to the site. I'll post the numbers in a few weeks.
 Has anyone tracked a free extension all the way to paying customers?
Rareș
11 Upvotes
2 Comments
October 24, 2026
 Went from 0 customers to $10 MRR, then rebuilt onboarding because people are scared of touching their DNS
In my last update here I had 0 customers after 2 months, and nobody outside of me had connected a domain.
 On Oct 2 that changed. The one person outside of me who had connected a domain reached the end of their 7-day trial, Polar charged the card, and Mailyond got its first $10 MRR. I never reached out to them, they found it on their own. I had Oct 31 written down as the date I'd kill it if nobody paid, so it survives for now. I still don't know if they chose to pay or just didn't cancel, I'll probably find out when it renews at the start of November.
 Activation is still the real problem though. On r/microsaas I wrote about giving a free month to about 80 people, and zero of them connected a domain. Most of the 17 comments said the same thing: people are scared of breaking the email they already use. A few suggested starting on a subdomain, checking where the current mail goes before changing anything, or just doing the setup together on a call.
 So this week I shipped pretty much that:
 - Adding a domain now starts on a subdomain by default (like mail.yourdomain.com ), so the root domain's MX and your current inbox stay untouched
 - Before you change anything, it shows where the root domain's mail goes today, for example "currently goes to Google Workspace"
 - A link to book a 15 min setup call if you'd rather do it together
 - If you sign up and don't add a domain in about 2 days, you get one email from me explaining the subdomain vs root domain setup
 Other things that shipped since the last update:
 - A Pro plan at $20 for 10 domains and up to 3 people. Before it, the step after Basic ($10 for 5 domains) was Agency at $40 for 30, so a solo founder with 6 domains had to pay 4x. Basic and Pro have a 7-day free trial
 - An MCP server, so Claude Code, Grok Bot or any MCP client can read the inbox across all your domains and reply from the address the customer wrote to
 - The send API is Resend-compatible and now passes List-Unsubscribe headers through, so one-click unsubscribe works for marketing mail
 - A new site, and a clearer one-liner: send and answer email across all your domains ( mailyond.com )
 If you've ever signed up for something that needed DNS changes on a domain you already use for email, what would have made you actually go through with it?
Rareș
1 Upvote
1 Comment
September 6, 2026
 0 customers after 2 months, and the most useful feedback I got was "it looks vibe coded"
I launched Mailyond at the end of June. One inbox for every domain you own plus a send API, built because I run 5 products on 5 domains and I was answering all of their support from my personal Gmail.
 Since then: 0 customers. And nobody outside me has connected a domain to it.
 The numbers behind that:
 Around 80 people contacted, across a warm list, DMs and Reddit threads where they described this exact problem. 10 of them got a 100% off coupon. 2 registered, 1 added a domain, 0 finished the setup.
 One Reddit post did 151K views and sent almost nobody to the site. Links are banned in that sub so that one is on me.
 Search: 3,630 impressions, 22 clicks, around position 21, 0 signups.
 100 visitors in a month, 3 signups, 0 domains connected after.
 My explanation for a while was switching cost. Everybody I spoke to already has something cobbled together that annoys them but works, and a free month doesn't beat "I'd have to change DNS on a domain that currently receives real mail".
 Then someone who actually opened the landing page wrote this:
 "it looks like a vibe coded inbox that you're giving away for free. I wouldn't use it either. It's not to say it's bad, I just would never feel excited to use a service like that."
 What he's describing is the absence of any sign that a real person runs it. And I'm asking people to point their MX record at that.
 So now I have 3 explanations for 0 activations and I can't tell which one is doing the work:
 1. Switching cost. Their setup is annoying but it already works.
 2. Something in the onboarding stops them. Someone else pointed out that if people were really that content, fewer of them would have started at all. Starting and not finishing looks more like hitting a wall than being happy.
 3. They don't trust a product built by one guy enough to move email onto it.
 The third one is the one I have no idea how to fix.
 So the question, for anyone who has been on the other side of this: what made you trust a tool built by a single person enough to put something like email or DNS through it? I'm guessing at answers like a real name and face, a public changelog, fast support replies, or just not being free.
 And if you run more than one domain and you're on the Resend or Cloudflare forwarding plus Gmail send-as stack, I'll give you a free month and do the setup with you on a call. I'll prepare the DNS records for your domain before we talk so you just paste them in. You can also point a subdomain like support.yourdomain.com at it and leave your main email exactly where it is.
 mailyond.com
Rareș
2 Upvotes
Comment
About
 I run multiple products each with their own domains and I handle support by email.
I needed one product to view all support emails and reply to them from the right @ address.
People
 Rareș Founder
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

- 项目页：[[10-项目/Mailyond_6af70b31]]
- 渠道页：[[50-渠道/indiehackers]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
