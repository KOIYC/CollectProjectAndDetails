---
type: "corpus"
item_id: "9f8dcf3b1e95d399"
title: "Aova"
source: "indiehackers"
source_name: "Indie Hackers 产品库"
url: "https://www.indiehackers.com/product/aova"
project_url: "https://aova.app/?promo=IH"
captured_at: "2026-10-28T09:43:59+08:00"
lang: "en"
kind: "project"
topic: "AI 工具/Agent"
shard: "2026-10-27"
tags:
  - 语料
  - indiehackers
metrics: {}
comments_count: 0
comments_total: 0
discovered_via: "ih:products"
---

# Aova

> [!info] 一句话导读
> Home Starting Up Case Studies DB Products Ideas DB Vibe Coding Tools Subscribe to IH+

> [!meta]- 语料信息（点开展开）
> 来源：Indie Hackers 产品库（project）
> 原帖：<https://www.indiehackers.com/product/aova>
> 指标：—
> 作者：—　|　发布：—
> 项目链接：<https://aova.app/?promo=IH>
> 采集：2026-10-28T09:43:59+08:00　|　id：`9f8dcf3b1e95d399`

## 正文

Home Starting Up Case Studies DB Products Ideas DB Vibe Coding Tools Subscribe to IH+
Starting Up Case Studies
 Ideas DB Products DB Sign in Join
AOVA
 AI assistants that answer from your own docs, audio, video
Visit Website
AOVA AI assistants that answer from your own docs, audio, video
 Posts 2
 Revenue $0 / mo
 Website
October 27, 2026
 Our AI assistant could answer anything. Then we noticed people still left to book somewhere else
Hey IH 👋
 Two weeks ago we posted here about AOVA: how an AI assistant we built for one psychologist's course library got 7,000+ users, and people asked for their own ( first post ). Thank you for the comments. Here's what happened next.
 What we noticed. Our assistant was good at answering. But look at what happens after a good answer: the client says "great, can I book a session?" - and the assistant could only say "here's the link". The client leaves the chat, opens a calendar, and many never finish. For an expert, the answer is not the goal. The booking, the lead, the order is.
 So for two weeks we built one thing: the assistant does the next step itself.
 What shipped
 1. Booking inside the chat. Connect Cal.com once, give the assistant a "Book a session" action. When a client wants to book, it asks which days suit them, offers 2-3 free times, reads the chosen one back and books it after the client says yes. The client gets Cal.com's confirmation email, and you get a notification.
 2. It collects leads. Name, phone, email and what they need - asked only when the client wants to book, buy or be called back (or before the first answer, if you prefer). They land under Leads in the inbox, and you can download them as a CSV.
 3. It works with the tools you already have. Ready-made actions for Shopify and WooCommerce (look up an order), HubSpot, Pipedrive and Airtable (add a client), Freshdesk (open a ticket), Mailchimp and Brevo, and Zapier, Make and n8n for everything else. For any other system you describe what you want in plain words and AI drafts the action for you to test.
 4. No website? Share a link. Every assistant can be its own page with a QR code: Instagram bio, a flyer, the front desk. Many of the experts we talk to don't have a website at all, so this mattered more than we expected.
 5. It tells you what it couldn't answer. Questions your material doesn't cover show up as a list, so you know what to write next instead of guessing.
 What we learned building it
 Actions need guardrails, or nobody will switch them on. The moment an AI can change something in your CRM, owners get nervous (we did too). So anything that changes data asks the client first, the assistant can fill in values like an order number but never choose where the request goes, keys are encrypted and never shown again, and the assistant only sees the fields you allow (an order's status, not the customer's address).
 Multi-step is where it gets hard. Answering is one message. Booking is five: which day, which time, confirm, name, email. The assistant has to remember what it offered two messages ago, and it must never book a time the client didn't confirm.
 Templates beat flexibility. Our first version was "paste any API URL". Nobody non-technical got through it. Ready-made actions where you only paste a key are what people actually use; the "describe it" option covers the rest.
 What's next. The owner app for iOS and Android, so you can see bookings and step into a conversation from your phone.
 A question for you: if an AI assistant could do one thing for your customers besides answering, what would it be? Booking, taking orders, refunds, something else? We'll build the most-asked one next.
 Try it on your own material (the link adds +500 bonus credits ): aova.app
SenArkadiy
3 Upvotes
2 Comments
October 14, 2026
 We built an AI assistant for one expert's course library. People asked for their own, so we made it a platform
Hey IH 👋
 We're AOVA. A year ago we had to build an AI Telegram bot that answers questions from a psychologist's large library: documents, audio and video. Here's how that one bot turned into a product, and what we learned on the way.
 How it started. We looked for a ready-made solution and didn't find one that worked with recordings and could show where an answer came from. So we built it ourselves. It took about a month: transcribing the audio and video, loading everything into a knowledge base, and wiring it to Telegram.
 The key requirement: every answer had to come from that knowledge and link to its source, whether a YouTube video, a Telegram channel post or a paid course.
 It worked better than we expected. More than 7,000 people have used that first bot. They asked questions, followed the links to the sources and bought the course. Then a different kind of message started arriving: "Can you build the same for us?" We didn't build it for them one by one. We asked ourselves: what if anyone could create their own AI assistant on their own material? That became AOVA.
 Here's what it looks like today, in 90 seconds:
 https://youtu.be/9yShtdqUqWY
 What we learned
 1. Show where the answer comes from.
 Source links do two jobs: people trust the answer, and the bot becomes a sales channel. In AOVA you can attach up to 3 links to each document (e.g. "Buy the course"), and they appear as buttons when that document is cited. When the answer isn't in the material, the assistant says so instead of guessing.
 2. Most knowledge lives in recordings, not documents.
 Experts have hours of webinars, lessons and calls and very few written FAQs. Transcribing by hand was the slowest part of that first month, so in AOVA you just upload audio or video and it's transcribed automatically.
 3. When people ask for the thing you built for yourself, listen.
 We didn't plan a platform. The "can you build one for us?" messages were the market research.
 4. Start where the audience already is, then expand.
 For that first expert it was Telegram, where many questions arrive as voice notes, so the assistant understands voice in 18 languages. The same assistant now also answers on a website chat widget, in WhatsApp and through an API.
 5. Let the owner step in.
 Some questions need a human. On paid plans the assistant can hand a conversation over, the owner replies from the console, and the AI picks up again later. Clients get the personal touch only where it matters.
 6. Keep the knowledge fresh without re-uploading.
 Material changes. You can point AOVA at a website or a Dropbox folder and it keeps itself up to date. We do this ourselves: the chat on aova.app learns from our docs site. When we ship a feature and write its guide, the assistant picks it up on the next weekly refresh, and nobody re-uploads anything.
 7. Price per answer, not per seat.
 An expert's volume is spiky: quiet for weeks, then a course launch with hundreds of questions. So AOVA uses credits per answer, with a free plan and top-ups that never expire.
 The architecture, for the curious. We tried to build it properly from day one instead of rewriting it later: fully serverless on AWS (Bedrock, Lambda, Step Functions, EventBridge, DynamoDB), microservices with a database per service, event-driven communication and CQRS.
 What's next. We're building an iOS and Android app for owners, so you can see conversations and step in to answer a client from your phone.
 What we'd love from you: would you put an AI assistant like this in front of your own customers? If not, what would stop you? And if you would, what's the one thing you'd want it to do that it doesn't yet?
 If you want to try it on your own docs, this link adds +500 bonus credits when you sign up: https://aova.app/?promo=IH&utm_source=indiehackers&utm_medium=launch&utm_campaign=launch
SenArkadiy
1 Upvote
Comment
About
 We built an AI bot that answered from a creator's docs, audio and video, linking to sources like their paid course. People followed the links and bought it, then asked for their own bot. AOVA lets anyone build one.
People
 SenArkadiy Founder
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

## 关联链接

- https://aova.app/?promo=IH&utm_source=indiehackers&utm_medium=launch&utm_campaign=launch
- https://youtu.be/9yShtdqUqWY

## 导航

- 项目页：[[10-项目/Aova_ef778359]]
- 渠道页：[[50-渠道/indiehackers]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
