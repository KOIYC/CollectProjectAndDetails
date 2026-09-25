---
type: "corpus"
item_id: "c78c8a94a5b4b6ed"
title: "Sharing my experience of talking to users: How to get them and what to talk about"
source: "reddit"
source_name: "Reddit 独立开发版块"
url: "https://www.reddit.com/r/SaaS/comments/1wgm03g/sharing_my_experience_of_talking_to_users_how_to/"
project_url: "https://app.glockapps.com/"
author: "fishdev814"
published_at: "2026-09-15T09:10:36+08:00"
captured_at: "2026-09-25T13:43:26+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-25"
pub_day: "2026-09-15"
tags:
  - 语料
  - reddit
  - r/SaaS
metrics: {"score": 5, "comments": 11, "upvote_ratio": 1}
comments_count: 12
comments_total: 12
discovered_via: "reddit:14d+settle10"
---

# Sharing my experience of talking to users: How to get them and what to talk about

> [!info] 一句话导读
> I used to have a B2B product for social media content planning and growth management. \~230 signups and \~50 active users. I know the importance of talking to u…

> [!meta]- 语料信息（点开展开）
> 来源：Reddit 独立开发版块（post）
> 原帖：<https://www.reddit.com/r/SaaS/comments/1wgm03g/sharing_my_experience_of_talking_to_users_how_to/>
> 指标：得分=5 · 评论=11 · 赞踩比=1
> 作者：fishdev814　|　发布：2026-09-15T09:10:36+08:00
> 项目链接：<https://app.glockapps.com/>
> 采集：2026-09-25T13:43:26+08:00　|　id：`c78c8a94a5b4b6ed`

## 正文

I used to have a B2B product for social media content planning and growth management. \~230 signups and \~50 active users. I know the importance of talking to users, and I'd like to understand what their real workflow is or what their real opinion on my features is.

But they all come from random places on the internet and I always find it difficult to get them:

**Email almost doesn't work.** I tried to send it to the entire user base but only got 2 replies: one is "**Don't send again**", the other is "**Your email sounds too much like AI, hope it helps**". Come to think of it, it has several issues:

1. Likely your email will end up in spam. Email credibility is related to your domain settings, IP, reputation with mail providers and lots of other factors. Getting them all straight is hard work. But there's a **great tool to check if your email is gonna land in spam** at different providers: [glockapps](https://app.glockapps.com/)
2. People will only open the ones most important to their lives. When they open the inbox and face a bunch of emails, your request for feedback clearly falls outside the "important" category.
3. It lacks context. People may have opinions when using the app, but 3 days later in their mailbox, they can recall nothing and perhaps they have already forgotten your app.

And I did some research on Reddit and found many people facing the same problem! **Seems email is the only way for 90% of founders to get to users, and it sucks.**

Then I read lots of articles and found that **in-app feedback could be 10x higher than off-app feedback**, meaning you need pop-ups at the right moment to collect opinions.

**So I started putting effort into making these widgets and hooking them up with the moment**. For instance, originally I had a feature where you can put your brand name as a keyword and monitor Reddit or X to see if someone mentions it. But not many users were using it and I wanna know why. So when users go into that feature page, a widget will randomly pop up, greet users and then ask what their use case of this is and whether it's truly useful.

**And it worked well!** Later that afternoon, I got a simple but valuable message: "I monitor the keywords of niche problem instead cause my brand is not famous yet. But it's a little bit noisy". And it was a spark for me, I realized what I should have thought of: my users are not big names, so their first priority is user acquisition.

So I changed that to a credit-based paid feature - Give AI a prompt with what you are looking for and the standard, and it helps you filter the keyword monitor results. This feature keeps getting me cash every month 💰.

**Also I found putting a "Talk to founders" button with your avatar in the corner helps a great deal**. People are tired of talking to customer service or chatbots, but talking directly to the CEO, someone in charge, is much more attractive. It helped me find a frequent crashing bug on Firefox, which I didn't have time to test before launch as a solo founder. That at least helped me save my Firefox users.

Gradually I got even more interested in the user feedback tool I made, and I refactored it and made it more general. Here are some **principles I put into it to push the response rate to the limit**:

1. Be proactive. Pop up at the proper time to find users, don't let users find you - in most cases they won't. And add a cooldown to avoid spamming users.
2. In the app, with context. People don't hate talking, but you need to ask them right when and where something happened. You pick a topic that is happening and they will open up.
3. Show up as the founder, as stated before.

And **asking the right questions is very important too**. Here are some of the essences I summarized:

1. You don't just ask superficial questions like "What's your feeling" or "Do you like it". People will politely say something good. Ask for facts instead, for instance "What do you use this feature for?", "Could you walk me through your real workflow?" or "Would love to know one thing you don't like".
2. Always ask deeper when available. For example, at first I only had a feature that let a founder clone his AI stand-in to talk to users. When I recruited a new user for this tool, I just felt happy and helped him set up and debug. One day he asked me: "You never asked me why I want to use your tool." And later we talked and I realized his urgent need is user acquisition, so he actually needed a way to talk to users himself, which is better than letting AI talk. His original words were: "**I will get up at midnight to use this!**"

So I added the live talking feature, so the founder gets notified when a visitor comes along.

That's my story with talking to users. I still believe it's a gold mine. It's not like other tools that directly save you the time of doing X. Instead it costs your time, but **helps you avoid detours and save more time at a higher level**, if you do it right. You will constantly get valuable insights from it, no matter whether you're a starter or a big name.

BTW, I am beta testing the feedback tool I mentioned above. DM me if interested.

## 评论（12/12）

> **Effective_Pirate5525**（1 分） · 2026-09-15T09:17:21+08:00　
> the bit about catching feedback in context is spot on
>
> id add one guardrail though, make the trigger specific enough that someone can answer from memory in 30 seconds, otherwise it turns into another generic survey
>
> after a failed search ask what they were trying to find, after a feature gets ignored ask what they expected it to do. then tag the answers by job to be done and look for repeated patterns before changing the roadmap

---

> **fishdev814**（1 分） · 2026-09-15T09:58:01+08:00　
> Totally agree. So what do you use for these kind of tools? You make your own or there's some great external tools?

---

> **Nick_RoostPay**（3 分） · 2026-09-15T10:05:23+08:00　
> Really useful breakdown. I’ve had better conversations when I ask about the last time someone did the job, what they tried, and where they got stuck, rather than asking whether they like a feature. How do you handle generic positive feedback from people who never become active users?

---

> **fishdev814**（1 分） · 2026-09-15T10:27:32+08:00　
> So
> 1.  the tool I made can actually set strategies, I set instructions for it like: "Don't satisfies on nice words, but ask for deeper reason why it is not a fit for them. Make it clear that hard truth are happily welcome for users"
> 2. The tool also got ability to get me notified when someome is online and I can chat with users myself. I normally also follow the rules to dig deeper

---

> **Mindless_Coat3229**（2 分） · 2026-09-15T12:34:35+08:00　
> Cold emails for feedback are practically useless, and your shift to in-app, context-driven micro-feedback is the exact right play.
>
> Catching users right on the feature page and showing up as a real founder instead of a support bot,makes all the difference. That pivot you made on the keyword monitor based on user workflows is a textbook win.

---

> **MiserableDocument509**（2 分） · 2026-09-15T12:37:40+08:00　
> one thing that kills these popups for me is asking right when i open the page. i havent even used the feature yet so i just dismiss it. after i actually run a search or export something, a small ask in the corner is way easier to answer. the founder button is nice only if someone actually replies the same day, otherwise people wont click it twice.

---

> **fishdev814**（1 分） · 2026-09-15T14:07:00+08:00　
> Yes, so how to trigger these popups is tricky. In the case you mentioned, should put like 60s delay or a detector that user has scrolled to certain position of the page, to make sure user already get some information.
> And for the founder button, I made this tool with AI chat. It plays like founder's AI stand-in with avatar and dig for users root question. And don't forget to add "I will forward everything to the real me" and it really helps 🙂.

---

> **fishdev814**（1 分） · 2026-09-15T14:14:39+08:00　
> Glad we share common insights on this.
>
>  But I still found many people don't have this kind of tool set up, like there's not even a simple feedback form on the page. I don't know why. I know there's bunch of priorities for founders and also I think talking to users is gold at least for me, but I am not very sure is this painful enough to let them act.

---

> **dragos_apostol**（1 分） · 2026-09-15T14:27:32+08:00　
> The context point is the whole thing in my view. Feedback quality tracks how close the ask sits to the moment of use. Three days later in an inbox people are recalling a memory of your app, not the app.
>
> The talk to founders button working makes sense to me. It flips the dynamic. A support chat says we might help you. A founder button says you might change the product. People answer the second one.
>
> One thing I'd watch: in the moment channels catch frustration well, but the people who quietly like the product still say nothing, so the picture can skew negative. Worth pairing with something that catches the happy silent majority once in a while.

---

> **fishdev814**（1 分） · 2026-09-15T18:21:46+08:00　
> Thanks for the addition. Yes, the focused more on how to identify shortcomings in your own products. But what you mentioned can definitely be done, and even better: you could have AI help check out review websites like G2 and leave reviews. I'm also thinking about making a mobile version, and then it can invite happy users to leave reviews on the App Store

---

> **fishdev814**（1 分） · 2026-09-16T09:22:21+08:00　
> Since some people are asking: The tool is https://founderping.app, made it as out of box using

---

> **lmfresneda**（1 分） · 2026-09-17T16:00:59+08:00　
> The AI email thing is real. I sent a batch and one guy replied just to tell me it read like a bot
>
> What worked was one by one, doing something for them first. 5 founders answered DMs where I had already built the thing for their pricing page
>
> The in app widget makes sense at 50 active users. I have 3, so mine is still all manual

## 导航

- 项目页：[[10-项目/app.glockapps.com_e788986c]]
- 渠道页：[[50-渠道/reddit]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
