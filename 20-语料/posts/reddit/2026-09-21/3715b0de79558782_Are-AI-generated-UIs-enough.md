---
type: "corpus"
item_id: "3715b0de79558782"
title: "Are AI generated UIs enough?"
source: "reddit"
source_name: "Reddit 独立开发版块"
url: "https://www.reddit.com/r/SaaS/comments/1t00cpl/are_ai_generated_uis_enough/"
project_url: "https://wattfactory.fit/"
author: "robputt796"
published_at: "2026-04-30T23:54:37+08:00"
captured_at: "2026-09-21T02:59:54+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-21"
pub_day: "2026-04-30"
tags:
  - 语料
  - reddit
  - r/SaaS
metrics: {"score": 15, "comments": 36, "upvote_ratio": 1}
comments_count: 38
comments_total: 38
discovered_via: "reddit:174d+settle3"
---

# Are AI generated UIs enough?

> [!info] 一句话导读
> For a bit of context I've been building a SaaS, it started off as a project for myself as I got fed up of paying Zwift for their indoor cycling experience, thei…

> [!meta]- 语料信息（点开展开）
> 来源：Reddit 独立开发版块（post）
> 原帖：<https://www.reddit.com/r/SaaS/comments/1t00cpl/are_ai_generated_uis_enough/>
> 指标：得分=15 · 评论=36 · 赞踩比=1
> 作者：robputt796　|　发布：2026-04-30T23:54:37+08:00
> 项目链接：<https://wattfactory.fit/>
> 采集：2026-09-21T02:59:54+08:00　|　id：`3715b0de79558782`

## 正文

Hello,

For a bit of context I've been building a SaaS, it started off as a project for myself as I got fed up of paying Zwift for their indoor cycling experience, their price has been bumped 3 times since my original sign up and has soared from £6.99 to £17.99 a month. As a casual user who only cycles indoors once a week almost £5 per ride seems like poor value. So I thought about what I would like to replace it, first I looked at some other options like Rouvy, TrainerDay and so on. I found they are either expensive also, or very basic on features. One thing I particularly wanted was the ability to cycle real world routes that I could cycle outdoors based on real map data. The app I have been building uses OSM and elevation data to simulate routes on Bluetooth and ANT+ capable trainers so you can effectively ride anywhere virtually. It doesn't have the fancy 3D metaverse of things such as Zwift and MyWhoosh but overall seems to work pretty well.

The big problem is I am a backend person and my UX skills are non existent. Is an AI generated UX good enough to get you started and launch or do you need more polish than that? Are there any techniques that can be used beyond basic prompt engineering that can tune the output of the AI to do better? The current marketing page and app can be accessed at [https://wattfactory.fit](https://wattfactory.fit/) if you wanna take a look and pass judgement. Any other feedback also gladly received.

Many thanks,

## 评论（38/38）

> **Casperzwaart100**（2 分） · 2026-05-01T00:03:56+08:00　
> It mainly just looks unprofessional. Provided it works, and the logic makes sense, its fine for an MVP tbh.
>
> I think the UX is something a lot of people forget in the whole UX/UI concept. The fact it works is most important for now.
>
> For a free programme your current look would be fine, but personally I would not pay for something purely because it looks cheap and ugly.

---

> **FlashyAverage26**（3 分） · 2026-05-01T00:07:26+08:00　
> yeah ai generated ux is fine to start but not enough to win
>
> you don’t need polish you need clarity and usability first
>
> if users can’t understand what to do in 5 seconds they will leave no matter how good backend is
>
> best move is copy proven ux from competitors and simplify it
>
> also your value is ride real routes cheaper than zwift make that obvious instantly
>
> ai can help but real improvement comes from watching users struggle and fixing that
>
> like this is my saas [stak.co.in](http://stak.co.in) i built this landing page fully ai generated and i know it's not good and i need to change it in the near future and try to take some inspiration from existing templates (from framer)

---

> **FlashyAverage26**（0 分） · 2026-05-01T00:10:33+08:00　
> i totally agree with you
>
> and if you see my saas do you think the same?

---

> **ikooloo**（2 分） · 2026-05-01T00:23:59+08:00　
> UI/UX is such a personal thing - but, your users (or lack of them) will tell you... If you get some sign-ups, just ask them - it's all about the value you provide - what you have 'may' be enough, it may be that they need more.
>
> I haven't logged in but, one thing that occurred to me was whether you could just pick from standard (well known) routes and 'cycle' those - for example, I have some cycling friends who go to Majorca (Spain) every year and do nothing but talk about those routes; similarly, the have cycled some of the Tour De France routes.. I can imagine something like that could be quite useful (ride your favorite routes sort of thing).

---

> **robputt796**（1 分） · 2026-05-01T00:31:30+08:00　
> Yeah so feature wise when you login there is a dashboard, this has a few option presented as cards on a dashboard
>
> a) ROUTE mode - cycle real routes from the map
> b) WORKOUT mode - this is more about hitting particular power output targets and isn't map based but is like a virtual spin session
> c) Ride History - lists your historic rides and lets you view their stats or export them as GPX / fit file to upload into Strava (will probably develop an integration soon to automate this for users)
>
> Inside of the ROUTE mode there are a number of options
>
> a) Route Library - a library of curated routes that are famous among the cycling scene, e.g. Cap De Formentor in Spain or Alpe D'Huez a Tour De France climb in the Alps.
> b) Saved Routes - users can recall routes they have made previously
> c) Custom Route - users can create a route interactively on a map with waypoints
> d) Import GPX - users can import real world route data from their cycling computer where they have cycled outdoors previously and relive those routes in the app
>
> Features aren't too much of a problem, implementing new things is fine and pivoting is also fine. The real question is, is UX enough? Having a great physics simulation is fine but if users hate using the app it's all in vein. Like you said I probably need a few more organic users and then incentivise them with discounted or free PRO upgrade for a period of time to provide honest and useful feedback to help me iterate.

---

> **ikooloo**（2 分） · 2026-05-01T00:36:16+08:00　
> Got it - that makes sense. And, to answer your question - you'll only know the answer when some people use it. Also - I'd be careful not to confuse UI and UX. What I mean by that is that if the users' experience is clean and they realise true value, that can more than make up for a slightly poor user interface.  If someone really hates it they will tell absolutely tell you but, in my experience.
> You're a cyclist, I assume you've been using it - does the UI detract from the value?

---

> **cachejc**（2 分） · 2026-05-01T00:38:15+08:00　
> I think that UI is starting to matter more in the world of vibe coding. Back when LLMs weren't as prevalent, you could easily get away with an ugly UI but a great, functioning product. Of course, that ties in with having a good UX.
>
> But now with there being so many different choices for the same type of products, UI is becoming more and more important to distinguish yourself from others.

---

> **scanslop**（1 分） · 2026-05-01T00:38:22+08:00　
> **This comment has been temporarily removed for verification.**
>
> To prove you're human, click the link below to see your verification code:
>
> **[Click here to get your code](https://scanslop.com/c/aQ0UAX9EEhcEETsNCxEZVWRSVEdTQwMAAAFhWwk0KRQ9)**
>
> Then reply to this comment with just the 6-character code.
>
> This is a one-time check - once verified, all your future activity will go through automatically.

---

> **theGoatRocks**（2 分） · 2026-05-01T00:39:15+08:00　
> By far my most commercially successful Saas to date was coincidentally a cycling webapp.
>
> I’m all backend too and cobbled together the UI with twitter bootstrap (this has clearly been awhile) We’re our own worst critics but I had an UGLY baby.
>
> Didn’t matter. The experience was unique enough with ridiculously good distribution (wasn’t my department), and it did really well.
>
> Same old story, if you’re solving a problem or entertaining someone (sounds like your idea does a bit of both), users are willing to overlook poor UX/UI. At least up to a point. If you do well there will be copycats and then the better UX will draw customers away.
>
> One final point, your own post is foreshadowing. In this B2C vertical people are price sensitive. You yourself are bouncing over a few bucks a month (no shade)…your users will do the same, just FYI
>
> Good luck!

---

> **robputt796**（1 分） · 2026-05-01T00:41:45+08:00　
> No, I just want to make my legs ache and save a few £££ and this does it very well.

---

> **ikooloo**（2 分） · 2026-05-01T00:43:37+08:00　
> Well there you go.. there may well be other cyclists who value the workout rather than the UI. Find them (at least to start).

---

> **Practical_Surround_8**（2 分） · 2026-05-01T00:47:36+08:00　
> Your landing page definitely looks vibe coded (many startups are doing this these days).
>
> That being said I think its completely fine. I can very easily tell what your product does. If someone has this the problem you're solving they will pay.

---

> **robputt796**（1 分） · 2026-05-01T00:50:21+08:00　
> "You yourself are bouncing over a few bucks a month" for sure, I had a review of all my subscriptions recently, and realised that there are a bunch of things I can combine, a bunch of things I am happy to pay for and a bunch of things that are not reasonable use of funds, those £10 here and £15 there soon add up to £100 very quickly. I switched from my mobile providers main brand to their budget brand, interestingly same package was £19 a month cheaper but didn't have some of the value add stuff of the main brand (for example their loyalty app which gives you discount on a few things that I never used anyway) and I did that on 3 SIM cards easiest £57 I reclaimed in my life. After all these savings it's a real saving which I can use to treat the wife / the kids or whatever.

---

> **Low-Oil7883**（2 分） · 2026-05-01T00:51:57+08:00　
> honestly yeah AI UI is fine for v1. users care way more if the trainer actually connects and the route sim feels good than if your buttons look like they came from Dribbble.

---

> **theGoatRocks**（2 分） · 2026-05-01T00:55:21+08:00　
> Smart and totally makes sense. But that’s also the headwind we face when we build Saas for individuals vs businesses
>
> Pros and cons to both, but B2B has lower price sensitivity and churn than B2C for this reason

---

> **AdHopeful630**（1 分） · 2026-05-01T01:14:44+08:00　
> Frankly, not a fan of AI generated pages, it has no personality or clear info.
>
> Not everything need to be in dark mode.
>
> If it was me, I would have gone with something like this. Again it is just me, others might not like it.
>
> https://kommodo.ai/i/BCTHBSiqGmSe9QTz8ZtC

---

> **Adorable_Pie_1549**（2 分） · 2026-05-01T01:20:08+08:00　
> Pick a proper workflow. You need examples of good UI-s, close to what you want. And that's the starting point. Copy what works, don't invent a bicycle. Ever.

---

> **pantherggg2222**（2 分） · 2026-05-01T01:30:24+08:00　
> For a backend person with non-existent UX skills, the bottleneck is probably getting a decent-looking UI without breaking the bank. devappshowcase is worth checking because it offers a platform to showcase your app and get feedback from a technical community, which can help you validate your product-market fit. Also, try checking out some UX design courses on YouTube to get started with the basics.

---

> **scanslop**（1 分） · 2026-05-01T01:30:32+08:00　
> **This comment has been temporarily removed for verification.**
>
> To prove you're human, click the link below to see your verification code:
>
> **[Click here to get your code](https://scanslop.com/c/ZVsQXnlFEgQEHCcABAACAzRXUUBXCAMHBQFlW0VVe0deTFMOAAkAIQ)**
>
> Then reply to this comment with just the 6-character code.
>
> This is a one-time check - once verified, all your future activity will go through automatically.

---

> **scanslop**（1 分） · 2026-05-01T01:30:39+08:00　
> **This comment has been temporarily removed for verification.**
>
> To prove you're human, click the link below to see your verification code:
>
> **[Click here to get your code](https://scanslop.com/c/aVsRAXlMEhYOCyZYUUJVGGJSVEVQQwICAQ9iX0YbGxQPJw)**
>
> Then reply to this comment with just the 6-character code.
>
> This is a one-time check - once verified, all your future activity will go through automatically.

---

> **Infamous_Sentence_67**（2 分） · 2026-05-01T01:43:29+08:00　
> AI UX is very useful, but for advanced stages or complex products, it’s still better to hire a professional. Its quality can be limited when the product or user journey becomes more complex

---

> **richexplorer_**（2 分） · 2026-05-01T02:04:45+08:00　
> You don’t need perfect UX to launch, you need usable UX
>
> AI UI is fine to get started, but it won’t give you taste or flow so focus on
>
> 1. Can a new user start a ride in <30 seconds
>
> 2. Are there zero confusing steps?
>
> If yes then ship it.

---

> **robputt796**（1 分） · 2026-05-01T02:07:25+08:00　
> 1. Once signed up yes, but signup is a little slow cos email validation (I still need to configure social login in my IDP this will make it much faster)
> 2. I worked really hard on making the connection to the trainer as reliable and as simple as possible, I've tested it extensively but right now only on two types of trainer, in theory it should work for all as they follow a standard protocol but the testing isn't exhaustive :-(. This is the only thing that could be confusing for a user if their trainer doesn't follow the standards, which I am sure some don't, as always some vendor does weird stuff I am sure.

---

> **scanslop**（1 分） · 2026-05-01T02:20:05+08:00　
> **This comment has been temporarily removed for verification.**
>
> You have a pending verification. **[Click here to get your code](https://scanslop.com/c/ZFkWA3EQEj0JHiYbFQAMCyYWIhZcQwQBTgdnW0JSf0ZcRFBBYVkdIQQFAA)**
>
> Reply to this comment with just the 6-character code.

---

> **robputt796**（1 分） · 2026-05-01T02:25:31+08:00　
> 45cdge

---

> **robputt796**（1 分） · 2026-05-01T02:26:06+08:00　
> 45cd9e

---

> **RFP-guy**（2 分） · 2026-05-01T02:45:14+08:00　
> ai generated ui is fine for a dashboard, but for an experience based saas like cycling, 'good enough' is just a churn machine.
> focus on a proven component library for clarity now, and hire a real designer as soon as you have traction

---

> **scanslop**（1 分） · 2026-05-01T02:48:49+08:00　
> **This comment has been temporarily removed for verification.**
>
> You have a pending verification. **[Click here to get your code](https://scanslop.com/c/MghNVStFEhkEBiYbGA5UU2RSVkVRTQAJAg5gECYGKSY)**
>
> Reply to this comment with just the 6-character code.

---

> **Glittering-Pie6039**（2 分） · 2026-05-01T03:52:47+08:00　
> This is better than you think the dark theme with orange works for a cycling product and the hero screenshot showing real route data, wattage, and gradient immediately tells someone what the app does. That's already ahead of most ai generated slop where you can't tell what the product is until you read three paragraphs.
>
> The product screenshot in the hero looks like real software. The six feature cards are using emoji style icons that don't add anything the titles don't already say "Route Mode" doesn't need a map emoji next to it "Heart Rate Zones" doesn't need a heart the icons are decorative, not informational, and they clash with the product screenshot in the hero which looks like real software. Drop them entirely and the cards look cleaner. Either use consistent outlined icons from one library or drop them entirely and let the feature titles carry the cards, personally I would opt to just remove the emojis all across the page as they don't really add anything information wise and make it look cheap.
>
> Your strongest selling point is buried £4.99/mo vs Zwift at £17.99/mo is a massive differentiator for casual riders and you've left the pricing comparison completely implicit. A single line in the hero like "Full indoor cycling for £4.99/mo, not £17.99" would grab attention.

---

> **AutoModerator**（1 分） · 2026-05-01T04:05:36+08:00　
> Your comment was removed. Links in comments require 5 karma earned in r/SaaS. Earn sub karma by commenting helpfully first.
>
> *I am a bot, and this action was performed automatically. Please [contact the moderators of this subreddit](/message/compose/?to=/r/SaaS) if you have any questions or concerns.*

---

> **Huge_Strawberry7888**（1 分） · 2026-05-01T04:16:00+08:00　
> They are they are

---

> **robputt796**（2 分） · 2026-05-01T04:19:24+08:00　
> Thanks,
>
> This is really useful feedback, that app looking thing in the hero is indeed mocked up to look like a simplification of the actual app.
>
> I will remove the emojis in the feature cards, I think you are right they are kinda a bit much.
>
> Great point regarding moving the pricing to the Hero, I don't even think we need the competitor price, just the actual price is a winner in itself, most people in this space already know Rouvy, Zwift and Fulgaz's pricing.

---

> **Brambleworks**（1 分） · 2026-05-01T05:28:04+08:00　
> 100% agree. Before LLMs there where plenty of apps with a shitty UI, but it was more accepted because at least they where uniquely shitty, if that makes sense. Now with AI, you see the same exact UI for thousands of sites and honestly it just makes me think "They clearly just told AI to make something for them without doing anything unique, why can't I just do the same?" A distinct an unique UI, to me at least, shows that they actually put effort into making it something unique and useful, rather than just saying to an AI agent "build me a website".
>
> I feel the same about website copy as well. If an app clearly has AI generated copy that is kind of sloppy and doesn't really make sense to humans reading it, it's pretty obvious and a huge turn off for me. It means there was zero thought put into it.

---

> **scanslop**（1 分） · 2026-05-01T05:28:12+08:00　
> **This comment has been temporarily removed for verification.**
>
> To prove you're human, click the link below to see your verification code:
>
> **[Click here to get your code](https://scanslop.com/c/MlxNBC5GEjYXEz4KDRcSCyEOEA5UQwUHBw5kWExVeEdeCDYTMjs)**
>
> Then reply to this comment with just the 6-character code.
>
> This is a one-time check - once verified, all your future activity will go through automatically.

---

> **kgo_at**（1 分） · 2026-05-01T06:56:59+08:00　
> Vibe coders made it possible and fancied by the colours and designs not the architecture

---

> **scanslop**（1 分） · 2026-05-01T15:42:51+08:00　
> **This comment has been temporarily removed for verification.**
>
> To prove you're human, click the link below to see your verification code:
>
> **[Click here to get your code](https://scanslop.com/c/MQ9BVHhCEjgKAyYJFTwQCTYXDAcWTAYEBkphW0JQfkdfR1JCZVBQDjYFMjY)**
>
> Then reply to this comment with just the 6-character code.
>
> This is a one-time check - once verified, all your future activity will go through automatically.

---

> **HolidayCondition311**（2 分） · 2026-05-01T23:10:29+08:00　
> for a solo backend dev, AI-generated UI is honestly good enough to launch. what matters at this stage is whether the core flows make sense to a new user, not pixel perfection. I'd actually try UX Pilot AI for generating multiple layout variations from one prompt so you can pick what feels right before building anything.

---

> **FluidLingonberry28**（1 分） · 2026-05-05T18:33:09+08:00　
> I am a software engineer. For years, I focused on the functional part and deployment processes to get an app out. Someone else would take care of the design and user experience. Then it came time to work on my own project, and I did not have enough cash flow to hire a designer. Luckily, I found UX Pilot, and I no longer have to keep iterating through Pinterest designs anymore.
>
> AI-generated UI is good enough to get started and launch. Just give it as much context about your users and their goals upfront as possible. The more context it has, the more consistent the output gets across every screen.

## 关联链接

- https://wattfactory.fit

## 导航

- 项目页：[[10-项目/wattfactory.fit_0db6ba3d]]
- 渠道页：[[50-渠道/reddit]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
