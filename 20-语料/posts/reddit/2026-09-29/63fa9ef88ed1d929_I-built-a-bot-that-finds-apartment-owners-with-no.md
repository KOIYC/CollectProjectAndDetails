---
type: "corpus"
item_id: "63fa9ef88ed1d929"
title: "I built a bot that finds apartment owners with no website and sends them a preview. 7,000 emails, 15 clients. Pretty proud of this one."
source: "reddit"
source_name: "Reddit 独立开发版块"
url: "https://www.reddit.com/r/SaaS/comments/1wk5abc/i_built_a_bot_that_finds_apartment_owners_with_no/"
author: "Klitolovac"
published_at: "2026-09-19T07:01:23+08:00"
captured_at: "2026-09-29T09:43:40+08:00"
lang: "en"
kind: "post"
topic: "开发者工具"
shard: "2026-09-29"
pub_day: "2026-09-19"
tags:
  - 语料
  - reddit
  - r/SaaS
metrics: {"score": 104, "comments": 69, "upvote_ratio": 0.86}
comments_count: 76
comments_total: 76
discovered_via: "reddit:14d+settle10"
---

# I built a bot that finds apartment owners with no website and sends them a preview. 7,000 emails, 15 clients. Pretty proud of this one.

> [!info] 一句话导读
> Not gonna lie, I'm pretty proud of what I built here so I wanted to share.

> [!meta]- 语料信息（点开展开）
> 来源：Reddit 独立开发版块（post）
> 原帖：<https://www.reddit.com/r/SaaS/comments/1wk5abc/i_built_a_bot_that_finds_apartment_owners_with_no/>
> 指标：得分=104 · 评论=69 · 赞踩比=0.86
> 作者：Klitolovac　|　发布：2026-09-19T07:01:23+08:00
> 项目链接：—
> 采集：2026-09-29T09:43:40+08:00　|　id：`63fa9ef88ed1d929`

## 正文

Not gonna lie, I'm pretty proud of what I built here so I wanted to share.
Everyone says web design outreach is dead and they're right - conversion is 0.2%. I sent over 7,000 emails and closed 15. But while it still works, I'm milking it.
The problem with every scraper out there is it just grabs contact@ and calls it a day. Owners never see it.
So I built my own thing and here's exactly what it does step-by-step:
1. FIND: Bot goes through local tourist board websites / municipal apartment listings. Almost every town in Croatia / EU has a public list with apartment names + owner email + phone. That's the goldmine.
2. FILTER: It checks if they already have a decent website. If they have a good one, it skips. If they have no site or a 2010 WordPress site, it keeps them.
3. SCRAPE OWNER: It digs for the actual decision maker email, not the generic one. That was the hardest part to get right.
4. BUILD PREVIEW: For each lead it generates a personalized one-page website preview with their apartment images, location, and a booking button. So they don't get a boring template, they see THEIR place.
5. DRAFT: It creates a personalized email with their name and saves it directly to my Gmail drafts as HTML. I don't send via API to avoid spam filters.
6. SEND: I just go through drafts and hit send, max 400 per day so Google doesn't get twitchy.
That's it. No magic SEO promises. Just: "Hey, you're visible on Booking but you don't own your bookings. Here's how your own site could look, you keep 100%."
Web design is cooked, I know. But I'm proud I automated 90% of this boring work.
If you're doing cold email in any other niche, the tourist board trick + owner email extraction is super valuable. Happy to answer questions.

## 评论（76/76）

> **lemontree882**（0 分） · 2026-09-19T07:06:20+08:00　
> 7000 emails to 15 clients is around 0.2%, so the preview page is clearly doing most of the selling. Whether the owners actually want a site is a different question. A host with a packed calendar on the big listing sites isn't weighing commissions, they're weighing an empty calendar against a full one, and a direct site brings no bookings on its own.
>
> How many of the 15 have taken a real direct booking so far?

---

> **Klitolovac**（3 分） · 2026-09-19T07:12:15+08:00　
> Preview definitely does most of the selling.
>
> For context, those 7k emails were sent in the last 7 days, I just started a week ago. Closed 15, but only 5 are live so far - the rest are in progress. So too early for any real direct booking data.

---

> **Predream1**（1 分） · 2026-09-19T07:26:56+08:00　
> Your filter splits the 7,000 into two very different buyers: people who never had a site and have been ignoring that pitch for years, and people sitting on an old one who already paid for a site once. The blank ones stall before they even reply. The old-site ones reply because the preview replaces something they already bought, and then they still stall at the switch, since nothing gets booked until their listings move over. Which half of the 15 is actually closing?

---

> **Klitolovac**（4 分） · 2026-09-19T07:30:25+08:00　
> The blank ones almost never close. Like 12 out of the 15 are old-site ones.

---

> **tangy_header**（17 分） · 2026-09-19T07:33:21+08:00　
> That’s a smart filter good job man

---

> **Klitolovac**（4 分） · 2026-09-19T07:36:49+08:00　
> Thanks!

---

> **dank_summers**（2 分） · 2026-09-19T07:48:17+08:00　
> I've been struggling to convert with email. Do you really do 400 a day? I've been keeping myself to like 15 a day. Do you just have a bunch of email accounts?

---

> **StockAd3210**（1 分） · 2026-09-19T08:15:28+08:00　
> the personalized preview is doing all the heavy lifting here imo. cold email without something visual to anchor it is just noise. curious though, whats your churn look like after a few months? apartment owners arent exactly sticky clients for web design

---

> **Wooden_Astronomer718**（-6 分） · 2026-09-19T08:39:21+08:00　
> The part that's actually doing the work here isn't the scraping, it's the reframe: you're not pitching "you need a website," which every owner has heard and ignored, you're pitching "you're renting your guest relationship from the booking platform you're listed on and giving up 15 to 20 percent of every stay for it, here's what it looks like if you own it." That's a cost apartment owners already feel on their books, which is why a personalized preview cracks open replies that generic outreach never would. I'd lean into that framing even harder in the email copy itself, lead with the commission math for their size of property before design ever comes up. On churn, since these owners aren't sticky like SaaS clients, the stronger play is probably a small monthly fee for keeping the direct booking calendar synced rather than a one time build, otherwise you're re-selling the same 15 people every year. Also worth testing once someone converts: ask for two other owners they know, this niche runs on word of mouth inside local owner groups more than cold email ever will.

---

> **sherkon_18**（10 分） · 2026-09-19T10:04:29+08:00　
> How did you not get spammed?

---

> **AdvancedSandwiches**（1 分） · 2026-09-19T10:26:53+08:00　
> Thanks, Claude.

---

> **twendah**（1 分） · 2026-09-19T10:35:53+08:00　
> Good job! That would work on many other field as well! You could advertise pretty much anything like that.

---

> **stay_hyped**（0 分） · 2026-09-19T11:09:19+08:00　
> This is genius! I have another potential use case. Do you mind if I DM you?

---

> **Ok_Leg_2547**（0 分） · 2026-09-19T11:51:24+08:00　
> Ever thought of giving an agent an actual phone number and a voice and having it cold call your pitch? Sometimes small business owners only have a phone number posted and not an email (and vice versa). That's where I'm at just curious if you've thought of it, because if you're like me you hate cold calling.

---

> **dqsp**（1 分） · 2026-09-19T13:50:11+08:00　
> what are you charging per site

---

> **Possible_Shoe3249**（0 分） · 2026-09-19T14:42:49+08:00　
> 1. SCRAPE OWNER: It digs for the actual decision maker email, not the generic one. That was the hardest part to get right.
>
> do you mind giving some details?

---

> **Punterios**（1 分） · 2026-09-19T14:43:30+08:00　
> You said earlier that you send 400 emails per day, but now you sent 7k in a week. Math is not mathing here. And 7k emails reviewed and manually sent by you in a week?
>
> Not to mention the Gmail would be burned at this pace.
>
> I call BS / bad bot.

---

> **abtx**（5 分） · 2026-09-19T15:05:20+08:00　
> Nice. I always wonder though what’s the unit economics here. You’ve generated 7k websites to get 3 clients. That sounds like an awful lot of credits, do you use a pro or max subscription or equivalent and is it sufficient?

---

> **Correct_Support_2444**（1 分） · 2026-09-19T15:19:35+08:00　
> Is the site served by a SaaS or are these actual individual websites? This sounds like a great idea.

---

> **alloknight**（5 分） · 2026-09-19T15:23:16+08:00　
> Curious about your pricing structure for these: are you charging an upfront flat fee for the build, or doing a recurring model (hosting/maintenance) to make the numbers work on a 0.2% conversion?

---

> **One-Natural604**（2 分） · 2026-09-19T15:30:51+08:00　
> You're right, the personalized preview is key. It makes a huge difference compared to generic emails. Churn is definitely something I'm keeping an eye on.

---

> **KeenAsGreen**（0 分） · 2026-09-19T15:37:16+08:00　
> Proud to be a spammer?

---

> **AutoModerator**（1 分） · 2026-09-19T16:54:22+08:00　
> Low-Effort/AI content is auto-removed.
>
> *I am a bot, and this action was performed automatically. Please [contact the moderators of this subreddit](/message/compose/?to=/r/SaaS) if you have any questions or concerns.*

---

> **jafs6**（2 分） · 2026-09-19T17:38:02+08:00　
> Hi, what tech stack do you use? LLM / SLM? Local or from providers?

---

> **Rough-Stage-333**（2 分） · 2026-09-19T18:16:36+08:00　
> How did your not get into spam with a preview link/image?

---

> **Unreasonable_Hedger**（2 分） · 2026-09-19T18:42:48+08:00　
> What a deal worth? And including your time what’s the CAC?

---

> **gyanverma2**（-2 分） · 2026-09-19T19:00:36+08:00　
> Do try Vibedoctor.io if you are using AI for code assistance

---

> **Klitolovac**（10 分） · 2026-09-19T19:18:51+08:00　
> €350 upfront for the build + €120/year for hosting,domain, small changes…
>
> If I did only one time, 0.2% doesn't make sense. But with recurring, LTV is like €600-800.
>
> 15 x €350 = €5k in 7 days upfront, and the €120 stacks every year. So even with 0.2% it's worth it because the bot does all the prospecting for free.

---

> **Klitolovac**（1 分） · 2026-09-19T19:24:55+08:00　
> Preview is just the same template with their name/address swapped and placeholder photos with a note "your photos here if you agree".
>
> Once they say yes, then I build the real premium one - custom photos, copy, WhatsApp / call booking button, maps, everything. That's the one they actually pay for.

---

> **ProjectUnderway**（5 分） · 2026-09-19T19:32:36+08:00　
> I do exactly the same in a different niche. Works really nice. Good luck to you.

---

> **Tomas-AppHaven**（1 分） · 2026-09-19T20:02:18+08:00　
> Cool idea, we're probably going to see more and more AI setups making their own money almost autonomously. I recently got one from a video producing AI that scraped Hacker News and offered to make explainer videos for something in our product. They didn't pretend it was a human email, it just said "
> I'm an AI agent"

---

> **lemontree882**（1 分） · 2026-09-19T20:07:52+08:00　
> 15 closed and 5 live after one week, the ten in progress are almost never waiting on you. They stall on photos, copy and a domain, and the chasing eats an hour per client. How many of them have sent you anything to put on a page yet?

---

> **alloknight**（1 分） · 2026-09-19T20:32:24+08:00　
> AWESOME!

---

> **Careful-Key-1958**（0 分） · 2026-09-19T21:17:29+08:00　
> Here's question. You've posted this in 4 different groups why? What are you selling that program? Most spammers who sell tool do like this.

---

> **Klitolovac**（5 分） · 2026-09-19T21:26:58+08:00　
> I dont sell anything, I am just proud of myself because I bult this shit

---

> **Kindly-Tension64**（2 分） · 2026-09-19T22:24:20+08:00　
> The name ? I m interessed to use

---

> **FreshPhase**（2 分） · 2026-09-19T22:40:41+08:00　
> Nice job! If it works it works. Hope your able find more clients and build client relationships overtime.

---

> **mnabihotak**（2 分） · 2026-09-19T22:41:39+08:00　
> That's really smart. Is this app avaliable so we can use?

---

> **barknezz**（1 分） · 2026-09-19T23:22:06+08:00　
> Hey, really interesting setup. I have a small gig idea for similar audience. I have a few questions if you don't mind:
>
> * Do you send the emails in English, or in the local language of each client?
> * How do you make sure the websites don't look like generic AI-generatedAI slop sites?
> * How do you collect payments from clients? Stripe, PayPal, bank transfer, etc.?
> * Have you ever offered to set up an online payment/booking system for clients who want one?
> * How do you present yourself to clients? Do you have your own portfolio website?
> * Do you show previous work or references when talking to new clients?
> * Do you build a completely separate website for each client, or do they all run on the same system?
> * Who owns the website and domain after they pay you?
> * Do you also handle things like hosting, domain setup, SSL, updates, etc.?
> * How do you handle clients who already have an old website? Do you help them move everything over?
> * What usually makes someone say yes after they see the preview?
> * Out of the 15 clients, how many had no website and how many had an old website?
> * Do clients usually pay the €350 upfront without seeing the finished website first?
> * Have you had clients from outside Croatia? If so, which countries worked best?

---

> **Live_It_Fully**（1 分） · 2026-09-20T00:06:01+08:00　
> \++ that...

---

> **Live_It_Fully**（1 分） · 2026-09-20T00:06:33+08:00　
> The preview is probably doing most of the selling here, not the scraper.
>
> You removed the hardest part for the prospect: imagining whether a new site would actually look better than what they have now. They can see it before replying.
>
> I’d be curious how many of the 15 mentioned the preview specifically.

---

> **Klitolovac**（1 分） · 2026-09-20T00:50:52+08:00　
> Hey man, I ll try to answer on all questions
>
> \- I send emails in Croatian (its hard because of gramatics but i find a way) and English (easiest)
> \- I put it into prompt: dont create template to look like ai made it
> \- Stripe
> \- Yes, but most of them wants only whatsapp message and call button
> \- Yes, I put my company website down in email
> \- Its same sistem but many of them ask me to create some custom shit, but in most cases same sistem
> \- They already have free .hr domain in Croatia, but for non croatian clients I offer to buy domain on my name because they dont know how to do it.
> \- AI can easily move everything from their old site
> \- I dont know why they say yes tbh
> \- from 15 of them, 12 have old web
> \- They pay upfront
> \- USA and UK because of language, in future i ll train agent to do same in other languages

---

> **Klitolovac**（1 分） · 2026-09-20T01:05:15+08:00　
> Nice, good luck!✌️

---

> **Klitolovac**（1 分） · 2026-09-20T01:26:29+08:00　
> Thank you!

---

> **kourchal**（1 分） · 2026-09-20T04:30:32+08:00　
> the question how much do you spend on that if you use a subscription based ai like gpt using codex oauth yeah im with you but what about image generation + the hunting of the apartment owners it will need a scraper, if you didnt build it yourself mostly it will cost like a 5$ on the 1000 owner lets say in apify in example then
> so the question how much it cost you until you get your first client?

---

> **No-Description7890**（1 分） · 2026-09-20T05:10:14+08:00　
> Ik heb een businessplan die erg interessant kan zijn met een gelijk soort bot. Sta je open om hierover in gesprek te gaan? Stuur me een dm als je wilt dan kunnen we praten

---

> **Klitolovac**（1 分） · 2026-09-20T05:37:47+08:00　
> Cant send a message

---

> **No-Description7890**（0 分） · 2026-09-20T05:38:24+08:00　
> Ik heb je bericht

---

> **Klitolovac**（1 分） · 2026-09-20T05:44:50+08:00　
> Its for personal use, but you can dm me if you need something like that

---

> **Klitolovac**（1 分） · 2026-09-20T05:45:17+08:00　
> Unfortunately not, but if you are interested leave me dm

---

> **Klitolovac**（1 分） · 2026-09-20T05:45:49+08:00　
> Thanks!

---

> **Klitolovac**（2 分） · 2026-09-20T05:46:19+08:00　
> Its not saas, its for my personal use

---

> **Klitolovac**（1 分） · 2026-09-20T05:52:54+08:00　
> Hey, ofc

---

> **Increase-Numerous**（2 分） · 2026-09-20T07:29:45+08:00　
> I am impressed. Totally deserved your success and more 🎯

---

> **ProfessionalCost8203**（1 分） · 2026-09-20T08:56:10+08:00　
> This is the part most people miss with cold outreach math. A 0.2% close rate sounds brutal in isolation, but when acquisition cost is basically free (bot runs itself) and you have recurring revenue stacking, the numbers actually work. The €120/year is doing heavy lifting here since it compounds without any extra sales effort.

---

> **PWThinkingCritically**（1 分） · 2026-09-20T10:23:06+08:00　
> pure dog shit. just because you landed 15 clients out of 7,000 doesn't mean it's a working proof of concept. 0.02% conversion. that's 0.002. that's 1/466.67.
>
> i'll tell you why it's sickening: code kiddies typing up a prompt in chatgpt and putting out a website in an hour and thinking he's some genius. no effort, no real value. what's the problem with is? it adds no real value and is just a get-rich scheme for himself.

---

> **Kronox_100**（2 分） · 2026-09-20T10:33:04+08:00　
> They're small businesses, not some big huge operation, no? And me and some of my mates have done this getting our degrees, it's not the best obviously but pays some bills and gives you something to do lol.
>
> Main thing they seem to be after is not dealing with pms fares rather than a very detailed/personalized website, they seem to just want a website to begin with and if both parties are happy, what gives?

---

> **PWThinkingCritically**（1 分） · 2026-09-20T10:47:51+08:00　
> so I already anticipated the "if no one gets hurt" type defense. there is no serious harm done. but in a world of providing value, it's diluting the quality of online services where we are already seeing the fallback of AI -- app stores getting flooded with AI-created slop that have no added value, too similar to existing apps, have no competitive advantage, and just makes the saturated app market that much more difficult to navigate for people to find real solutions.

---

> **Kronox_100**（1 分） · 2026-09-20T11:49:15+08:00　
> If what they want is not paying idk what it is, like 15% commission to Airbnb and you provide that solution, what is a 'real solution'?  A pms with 15 billion microservices? Doesn't the money they save also give them an advantage? Yes obviously they're pennies but its not like these small businesses swim in cash, rhey just want somewhere that is their own clients can reach, doesn't take a huge cut and has relevant info. And idk these small sites for small businesses have always existed, no? Or is just the 'slop factor' the enemy? In both cases sites aren't truly that distinctive, kinda look cheap (since they are), and people who might book in them only care for if the places looks good/clean, is cheap and has dates available, they're just trying to cut airbnb out of the way

---

> **hiscognizance**（1 分） · 2026-09-20T14:18:08+08:00　
> Only a different layout and styles would need differences in the code. Otherwise you can just use the same code every time - save are the names, descriptions, images, and dynamically replace them like any other website template in history. costs almost nothing.

---

> **presencedigital-io**（1 分） · 2026-09-20T14:39:39+08:00　
> Why not just design a web page and send them an email with the image to be more cost efficient

---

> **presencedigital-io**（1 分） · 2026-09-20T14:48:19+08:00　
> How did you handle the scraper owner? What challenges did you run into? You can only find the email addresses listed on their website, but there could be multiple ones, so you’d need to determine which is the most appropriate contact.

---

> **phantino21**（1 分） · 2026-09-20T15:08:34+08:00　
> So basically this bot is an agent that runs on ai credits, right? If so what is your spend per 1000 email runs?

---

> **Low_Canary_9756**（1 分） · 2026-09-20T15:10:04+08:00　
> This is insane!
> Maybe an arrogant question but how much do you actually make with this. I’m in a similar position rn

---

> **mirubuet**（1 分） · 2026-09-20T18:42:37+08:00　
> What a smart use of AI. Welldone. The system you developed can be used in other use cases too.  I am curious to know how many agents and subagents are working from the start to finish.

---

> **agupte**（1 分） · 2026-09-20T19:57:15+08:00　
> Wouldn't CoWork do this for you without any code?

---

> **OppStream**（1 分） · 2026-09-20T21:36:16+08:00　
> Great idea! How much $ in tokens does it cost you to create such an HTML email using AI?

---

> **Keenboo2022**（1 分） · 2026-09-20T21:47:55+08:00　
> I am also curious, since its not a good idea to include links in cold outreach

---

> **Grace-Club**（1 分） · 2026-09-21T15:47:52+08:00　
> Didn’t you get spammed?

---

> **Sitista**（1 分） · 2026-09-21T16:07:49+08:00　
> curiosità: ma come fate a non finire nello spam?

---

> **Kingwilly7**（1 分） · 2026-09-23T01:52:30+08:00　
> I’m curious to know which AI tools did you use to do all this?

---

> **FutureFine11**（1 分） · 2026-09-24T15:48:00+08:00　
> feel free to tell us how you build it, no dm please

---

> **CommunityProud433**（1 分） · 2026-09-24T21:31:11+08:00　
> Fantastic job man congrats on building this, the idea and the way you put it together are really clever.
> you said sent up to 400 emails a day but 7000 emails would take at least 18 days did you mean the 15 clients signed up in one week after you started sending ?

---

> **PutCreepy3481**（1 分） · 2026-09-24T21:33:08+08:00　
> Fantastic job man congrats on building this, Wishing you all the best as you grow it.

---

> **Klitolovac**（1 分） · 2026-09-24T21:37:56+08:00　
> Thank you!

---

> **SaaS-ModTeam**（1 分） · 2026-09-24T22:18:38+08:00　
> Your content was removed because r/SaaS does not allow promotion, recommendation, launch announcements, feedback requests, recruiting, or user acquisition for SaaS products made for advertising, promotional outreach, lead/opportunity detection, or ad/content generation. This includes tools that generate, suggest, schedule, automate, or coordinate promotional posts, comments, DMs, replies, or campaigns on Reddit or other platforms. These violations may result in a permanent ban and URL blacklisting.

## 导航

- 项目页：[[10-项目/I-built-a-bot-that-finds-apartment-owners-with-n_63fa9ef8]]
- 渠道页：[[50-渠道/reddit]]
- 赛道：`开发者工具`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
