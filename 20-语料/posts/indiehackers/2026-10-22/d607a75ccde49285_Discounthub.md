---
type: "corpus"
item_id: "d607a75ccde49285"
title: "Discounthub"
source: "indiehackers"
source_name: "Indie Hackers 产品库"
url: "https://www.indiehackers.com/product/discounthub"
project_url: "https://discounthub.uz/"
captured_at: "2026-10-22T09:48:20+08:00"
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

# Discounthub

> [!info] 一句话导读
> Home Starting Up Case Studies DB Products Ideas DB Vibe Coding Tools Subscribe to IH+

> [!meta]- 语料信息（点开展开）
> 来源：Indie Hackers 产品库（project）
> 原帖：<https://www.indiehackers.com/product/discounthub>
> 指标：—
> 作者：—　|　发布：—
> 项目链接：<https://discounthub.uz/>
> 采集：2026-10-22T09:48:20+08:00　|　id：`d607a75ccde49285`

## 正文

Home Starting Up Case Studies DB Products Ideas DB Vibe Coding Tools Subscribe to IH+
Starting Up Case Studies
 Ideas DB Products DB Sign in Join
DiscountHub
 Find real discounts and promo codes in one free app
Visit Website
DiscountHub Find real discounts and promo codes in one free app
 Posts 25
 Revenue $0 / mo
 Website Twitter
October 21, 2026
 Am I doing everything correctly?
I’m feeling discouraged. Do you think this is a normal outcome? For this project: discounthub.uz
MasterBek
19 Upvotes
1 Comment
October 11, 2026
 We Made DiscountHub Accessible to AI Agents - Now in the Official MCP Registry
I've been building DiscountHub, a platform for discovering real discounts, promotions, and promo codes from online stores.
 Recently, I started thinking about something:
 What happens to deal discovery when people start shopping through AI assistants instead of browsing websites?
 Rather than building another AI chatbot, I decided to make our existing platform accessible to the AI agents people already use.
 That's how we built DiscountHub MCP .
 What we've achieved
 ✅ Launched a public MCP server using Streamable HTTP.
 ✅ Built 8 read-only tools for searching deals, finding coupons, comparing offers, and discovering stores.
 ✅ Published DiscountHub in the official Model Context Protocol Registry.
 ✅ Successfully connected our MCP server to GitHub Copilot.
 ✅ Verified our domain and submitted the DiscountHub plugin for OpenAI review.
 The most interesting part: real testing
 We didn't want to stop at a working API endpoint.
 We connected DiscountHub MCP to GitHub Copilot and tested ordinary shopping requests.
 For example, I asked:
 "Find a laptop with at least 30% off."
 Copilot independently selected DiscountHub's tools and found a Microsoft Surface Laptop 4 listed with a 71% discount.
 Then I asked:
 "Are there any promo codes for games?"
 It found a Kinguin coupon, including its discount, expiration date, and merchant conditions.
 We also tested a request for Red Dead Redemption 2. No matching discount was found, and the agent correctly reported that instead of inventing an offer.
 During testing, we discovered an issue with merchant names across regions, such as Kinguin UE and Kinguin UK. We fixed the matching logic and added regression tests.
 Why this matters
 I believe we're moving toward a world where users won't always visit shopping websites directly.
 Instead, they'll simply tell an AI assistant what they want.
 For products like DiscountHub, that creates both a challenge and an opportunity.
 The challenge is that traditional website traffic may change.
 The opportunity is that our catalogue can now become a data source for AI-powered shopping experiences.
 And we didn't need to build our own AI agent to make that happen.
 What's next?
 DiscountHub MCP is already available through the official MCP Registry, and our plugin has been submitted for OpenAI review.
 We're continuing to explore how AI agents can discover reliable shopping offers while preserving accurate pricing, merchant terms, and affiliate attribution.
 🔗 Website: https://discounthub.uz
 🔗 MCP developer documentation: https://discounthub.uz/developers/
 🔗 Official MCP Registry: https://registry.modelcontextprotocol.io/?q=discounthub
 I'm curious: do you think AI agents will become a major way people discover deals, or will traditional shopping websites remain the primary destination?
 #BuildInPublic #MCP #AI #IndieHackers #Ecommerce
MasterBek
33 Upvotes
1 Comment
October 6, 2026
 I turned a small indie-maker experiment into a real part of DiscountHub
A few months ago, I added the first indie-made product offer to DiscountHub as an experiment.
 At the time, I wasn't sure whether this would become an actual part of the platform or stay as a small side idea.
 Since then, several indie makers have joined, and I realized there is a useful gap here.
 Most indie founders promote launch discounts through X, Reddit, Product Hunt, Indie Hackers, or their own audience.
 But those posts disappear quickly.
 So I’ve now turned the experiment into a proper section of DiscountHub.
 DiscountHub now has a dedicated Partner Offers page for indie makers, startups and online products.
 Users can search offers by product, founder, category or offer text, while makers can submit their own launch discount or special offer for review.
 The interesting part for me is that these offers sit next to regular store discounts and promo codes, so an indie product can be discovered by people who are already actively looking for a deal.
 I think this could become much more useful than simply posting another “20% off for launch week” tweet that disappears from the feed a few hours later.
 And today I’m starting to push this side of DiscountHub more seriously.
 If you're building an indie product, SaaS, AI tool, mobile app, or other online product and you have a real discount for users, I'd love to see it.
 Partner Offers:
 https://discounthub.uz/partner-offers/
 DiscountHub:
 https://discounthub.uz/
 Video: https://youtu.be/H_FOCgNcIfA?si=Jc_uUzStIT7FGLxs
 For other indie founders: where do you currently publish your launch discounts, and does that channel keep bringing users after launch day?
MasterBek
29 Upvotes
1 Comment
October 4, 2026
 DiscountHub just got its biggest update yet
For anyone who has followed my DiscountHub updates here before: a lot has changed.
 And if you’re seeing it for the first time, DiscountHub is a free platform for finding real discounts, promo codes, store offers and direct partner deals.
 Over the last few days I rebuilt a large part of the product.
 The biggest change is that the website no longer feels like a landing page for the mobile apps.
 You can now open DiscountHub and actually use it as the product itself.
 The homepage was redesigned around discovery. Deals now have proper search and filters. Promo codes have their own browsing experience. The AI Finder can search the current DiscountHub database for requests like:
 “Show me some laptops under $700”
 There is also a proper Stores directory showing where current deals and promo codes are available, and the Partners section now has a clearer home for direct offers.
 Under the hood I also worked on AI relevance, product images, navigation, SEO pages, structured data and the legal pages.
 The biggest difference for me is simple:
 A few months ago DiscountHub felt like a collection of things I had built.
 Now it finally feels much more like one product .
 I’m not going to put every change into one giant post — there’s too much to cover properly.
 Over the next few days I’ll share more about the AI Finder, the new Deals and Promo Codes experience, Stores, direct partner offers and some of the less visible work behind the scenes.
 For now, I’d really like one piece of feedback:
 Open DiscountHub for 10 seconds. Is it immediately obvious what the product does?
 🌐 https://discounthub.uz
MasterBek
14 Upvotes
1 Comment
September 9, 2026
 DiscountHub is competing in the WebMCP Challenge 🚀
Over the last few months, I’ve been building DiscountHub — a platform that brings together real discounts, promo codes, and special offers from different stores in one place.
 The idea is simple:
 Instead of searching through dozens of stores for a working deal, DiscountHub does the searching for you.
 For the WebMCP Challenge, I pushed the project further and built a WebMCP integration that allows AI agents to interact with DiscountHub and discover deals in a structured way.
 The submission is now locked, so I can’t touch the project until judging is finished.
 That means I finally have some time to focus on something I’ve neglected for too long:
 Getting people to actually use it. 😄
 If you want to try DiscountHub:
 👉 https://discounthub.uz
 I’d especially love feedback on:
• whether finding a deal feels fast enough
• whether the current store selection is useful
• what stores or categories you would want to see next
 Building is the easy part.
 Getting distribution is the real challenge.
 #buildinpublic #indiehackers #startup #discounts #deals #promocodes #AI #WebMCP
MasterBek
4 Upvotes
Comment
September 3, 2026
 🚀 DiscountHub is officially participating in the WebMCP Challenge — and we finally finished the demo video!
Over the past few months, I’ve been building DiscountHub , a platform focused on helping people find real discounts, promotions, and promo codes without digging through endless product listings.
 For the WebMCP Challenge , we took DiscountHub a step further and added WebMCP support, allowing AI agents to interact with the website and discover:
 🔎 Real discounts
🎟️ Promo codes
🏪 Stores and active offers
🤖 Relevant deals directly through AI-assisted workflows
 And after a lot of development, testing, recording, fixing things, and recording again…
 🎬 The DiscountHub WebMCP demo video is finally finished!
 Watch the demo here:
👉 https://www.youtube.com/watch?v=r7ksxBdX0fc
 In the demo, you can see an AI agent interacting with DiscountHub through WebMCP and using the website’s tools to search for relevant offers.
 This hackathon also pushed me to do something I hadn’t planned originally: open part of DiscountHub publicly and show much more of how the project actually works.
 The main product is live here:
🌐 https://discounthub.uz
 And the WebMCP implementation is public on GitHub:
💻 https://github.com/MasterBek533551878/discounthub-website
 It feels great to finally have the submission and demo ready.
 Now we wait and see how DiscountHub performs in the challenge. 🚀
 Would love to hear feedback from other Indie Hackers — especially anyone experimenting with WebMCP, AI agents, or agent-friendly websites.
 #BuildInPublic #IndieHackers #WebMCP #Hackathon #AI #AIAgents #DiscountHub #OpenSource #Startup #WebDevelopment
MasterBek
15 Upvotes
Comment
August 24, 2026
 🥇 DiscountHub became #1 Product of the Day on PeerPush!
Yesterday I shared that I had launched DiscountHub on PeerPush.
 Today I received an email saying that DiscountHub was selected as the #1 Product of the Day. 🎉
 It also reached:
 ⭐ 4.9/5 rating
👍 32 upvotes
👥 18 followers
 For a project I've been building and growing mostly on my own, seeing DiscountHub reach #1 feels like a really nice milestone.
 DiscountHub helps people discover active deals and promo codes, with AI helping make finding relevant offers easier.
 🔗 DiscountHub: https://discounthub.uz
🏆 PeerPush: https://peerpush.com/p/discounthub
 Still a long way to go, but today I'm enjoying this small win. 🚀
 #buildinpublic #indiehacker #startup #AI #ecommerce
MasterBek
25 Upvotes
2 Comments
August 23, 2026
 🚀 DiscountHub is live on PeerPush — competing for Product of the Day!
Small but exciting update today:
 DiscountHub is now officially live on PeerPush 🎉
 We’re currently competing in today’s Product of the Day race.
 For those who have been following the journey: DiscountHub keeps growing as a platform that brings together real deals, promo codes, partner offers, and AI-powered deal discovery in one place.
 Every new launch platform is another experiment for me:
 Can we reach people actually looking for deals?
Which channels bring real users instead of just impressions?
How much can a solo founder grow through consistent launches and distribution?
If you have a minute, I’d really appreciate your feedback on the product — and of course, support on PeerPush would mean a lot 🚀
 I’ll share the results after the race.
 🚀 Support DiscountHub on PeerPush:
 https://peerpush.com/p/discounthub
 🌐 Check out DiscountHub:
 https://discounthub.uz
 If you have a minute, I’d really appreciate your feedback — and your support on PeerPush would mean a lot! 🙌
 #buildinpublic #indiehacker #startup #solofounder #DiscountHub
MasterBek
26 Upvotes
14 Comments
August 6, 2026
 Users have clicked through from DiscountHub to partner stores 537 times in 20 days
Twenty days ago, I updated the DiscountHub backend and started tracking outbound clicks more accurately.
 Today I checked the production database and found that users have clicked through from DiscountHub to external stores and partner offers 537 times .
 The breakdown:
 339 clicks on product discounts and deal listings
151 clicks on promo codes
47 clicks on special partner offers
These are not confirmed purchases, but they are still meaningful to me.
 It shows that people are not only visiting DiscountHub. They are finding an offer interesting enough to open the original store and continue shopping.
 DiscountHub is still an early-stage project, built without a large marketing budget, so 537 real outbound actions in 20 days feels like a good sign that the core idea is working.
 https://discounthub.uz
 #BuildInPublic #IndieHackers #StartupJourney #Ecommerce
MasterBek
30 Upvotes
5 Comments
August 5, 2026
 DiscountHub just passed 10,000 pageviews in a month
Today I received an email from Cloudflare saying that DiscountHub passed 10,000 pageviews in a single month for the first time .
 DiscountHub is a free platform for finding discounts, promo codes, store promotions and online deals. It also includes an AI shopping assistant that searches our own database for relevant offers.
 The project is still early, and pageviews do not automatically mean revenue or loyal users. But after weeks of building, publishing updates and testing different promotion channels, it is encouraging to see real growth.
 The next goal is to turn more of this traffic into returning users and understand which acquisition channels bring people who genuinely use the product.
 Project: https://discounthub.uz/
 What metric made you feel that your project was finally starting to gain traction?
MasterBek
44 Upvotes
42 Comments
About
 I’m building DiscountHub because finding real discounts and working promo codes usually means checking many coupon websites, store pages and marketplaces manually.
The goal is to make online shopping easier by bringing
 People
 MasterBek Founder
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

## 关联链接

- https://discounthub.uz
- https://discounthub.uz/developers/
- https://discounthub.uz/partner-offers/
- https://github.com/MasterBek533551878/discounthub-website
- https://peerpush.com/p/discounthub
- https://registry.modelcontextprotocol.io/?q=discounthub
- https://www.youtube.com/watch?v=r7ksxBdX0fc
- https://youtu.be/H_FOCgNcIfA?si=Jc_uUzStIT7FGLxs

## 导航

- 项目页：[[10-项目/Discounthub_76ba7950]]
- 渠道页：[[50-渠道/indiehackers]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
