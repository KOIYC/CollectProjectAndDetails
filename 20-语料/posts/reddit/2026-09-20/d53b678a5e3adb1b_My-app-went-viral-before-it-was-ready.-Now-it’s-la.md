---
type: "corpus"
item_id: "d53b678a5e3adb1b"
title: "My app went viral before it was ready. Now it’s launched and I’m struggling to get users. Did I mistake interest for validation?"
source: "reddit"
source_name: "Reddit 独立开发版块"
url: "https://www.reddit.com/r/SaaS/comments/1wibn45/my_app_went_viral_before_it_was_ready_now_its/"
author: "Thin_Sky"
published_at: "2026-09-17T06:16:26+08:00"
captured_at: "2026-09-20T09:49:29+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-20"
pub_day: "2026-09-17"
tags:
  - 语料
  - reddit
  - r/SaaS
metrics: {"score": 6, "comments": 27, "upvote_ratio": 0.88}
comments_count: 27
comments_total: 27
discovered_via: "reddit:7d+settle3"
---

# My app went viral before it was ready. Now it’s launched and I’m struggling to get users. Did I mistake interest for validation?

> [!info] 一句话导读
> I'm a developer trying to figure out this marketing thing. I built a wedding planning app for my own wedding. It helps couples organize their wedding and also h…

> [!meta]- 语料信息（点开展开）
> 来源：Reddit 独立开发版块（post）
> 原帖：<https://www.reddit.com/r/SaaS/comments/1wibn45/my_app_went_viral_before_it_was_ready_now_its/>
> 指标：得分=6 · 评论=27 · 赞踩比=0.88
> 作者：Thin_Sky　|　发布：2026-09-17T06:16:26+08:00
> 项目链接：—
> 采集：2026-09-20T09:49:29+08:00　|　id：`d53b678a5e3adb1b`

## 正文

I'm a developer trying to figure out this marketing thing. I built a wedding planning app for my own wedding. It helps couples organize their wedding and also has a guest concierge that answers questions about schedules, transport, etc.

I made a post about it on the ClaudeAI subreddit and it got a ton of attention. A ton of comments were people saying they'd use it for their weddings. However, the app wasn't fully ready yet so I spent a bit more time finishing things up.

Now it's in general access, with a generous free tier, and I'm struggling to get people to actually use it. I followed up with people from the original post. Many didn’t respond, one tried it and stopped, and one is still using it.

I've started running some instagram ads and I use posthog to collect landing page metrics. My latest snapshot had 322 tracked visitors from paid instagram. **Only one recorded signup-button click and no recorded signups.**

It's still early and I did recently fix a mobile scrolling issue, so I'm not assuming the numbers tell the whole story. But it's really discouraging seeing people visit and then just leave.

Now I'm wondering whether:

* My Instagram ads are attracting curious people who don’t have a wedding to plan. (Im targeting people with interests in 'weddings' and other similar words)
* The ad and landing page aren’t communicating the same thing.
* The landing page just isn't good.
* I lost the initial interest by taking too long to launch.
* My biggest fear: the reddit response was mostly enthusiasm about an AI project, rather than actual demand.

I'm A/B testing my landing pages but I'm also wondering if I'm focusing on the wrong thing entirely.

Has anyone else had a ton of initial interest that didn't turn into actual users? How did you figure out if it was your marketing or if people just didn't want the product?

Any feedback or help is super appreciated.

## 评论（27/27）

> **cicygo**（2 分） · 2026-09-17T06:21:07+08:00　
> Instagram wedding interest targeting mostly reaches people browsing ideas, not couples who already booked a venue and have a date set. 322 visitors turning into one click on the signup button is closer to an audience problem than a landing page problem. The builder thread that blew up had the same shape, that crowd upvotes anything with an agent in it and none of them had a wedding to plan. Do you capture a wedding date anywhere on the page yet?

---

> **West_Inevitable_2281**（2 分） · 2026-09-17T06:24:13+08:00　
> You may have two different experiments mixed together. The Reddit post tested whether an AI project sounded interesting to AI enthusiasts. The Instagram campaign is testing whether broadly wedding-interested visitors will click. Neither necessarily tests demand from couples actively dealing with planning and guest questions. Before changing the landing page again, I’d look closely at the one person who is still using it. What was different about their situation, and what job are they repeatedly using the app for?

---

> **Thin_Sky**（1 分） · 2026-09-17T06:24:50+08:00　
> I don't capture any info yet. I thought about putting something like or a single multiple choice question with choices of 'im getting married', 'someone i know is getting married', 'im just curious' -- but I wound up not doing it because I don't want anyone bouncing due to friction. Do you think I should give it a try?
>
> "Instagram wedding interest targeting mostly reaches people browsing ideas, not couples who already booked a venue and have a date set."
>
> Honestly, this sounds like my target audience.
>
> Sometimes I tell instagram ad to go for a mix of actions. It looks like a majority of the new followers I get are bots.
>
> I wonder if I should try local ads?

---

> **Thin_Sky**（1 分） · 2026-09-17T06:27:50+08:00　
> The one person still using it is was actually from the reddit post. They are using it exactly as its meant: a secretary to just keep everything organized, setting up their guest portal, styling things. Just had a call with them today and they seem really happy with it.
>
> I think you're right about the target audience being off. I just don't know how to actually reach the correct audience.

---

> **elias-nurmi**（1 分） · 2026-09-17T06:28:49+08:00　
> The claudeai crowd are builders, not brides. That sub upvotes anything that looks like a clever build, its enthusiasm is about the tech, not the wedding. So no, that wasnt validation.
>
> 322 visitors and 1 click isnt an ad targeting problem, its a landing page problem. If the page was working youd get 5 to 15 clicks from that traffic even if nobody signed up after. Check whether the signup button fires before you blame instagram.
>
> Also wedding planning is a one shot purchase. People dont browse for it, they get engaged and then they need it that week. Interest based targeting is the wrong lever, you want life event timing and you mostly cant buy that on instagram.

---

> **West_Inevitable_2281**（1 分） · 2026-09-17T06:30:34+08:00　
> That call is probably more valuable than another landing-page test. The question isn’t just where engaged couples hang out, but when this user first felt the need for a “secretary” and what words they used to describe it. That moment should point you toward both the audience and the message. Had they already chosen a venue and date when they started using it, or were they earlier in the planning process?

---

> **Thin_Sky**（1 分） · 2026-09-17T06:31:19+08:00　
> >The claudeai crowd are builders, not brides. That sub upvotes anything that looks like a clever build, its enthusiasm is about the tech, not the wedding. So no, that wasnt validation.
>
> This was my fear. I mean there were somewhere around 10-15 people in the thread that said they'd use it for their wedding but I guess that's still a unique sample slice.
>
> >Interest based targeting is the wrong lever, you want life event timing and you mostly cant buy that on instagram.
>
> This is really interesting. Ive never heard of 'live event timing' based ads. Looks like i have some research to do. Thanks!

---

> **Thin_Sky**（1 分） · 2026-09-17T06:37:46+08:00　
> They had already chosen a venue and a date. They keep mentioning this is a "simple" wedding and they don't need all the planning stuff. They just really like the fact they can tell the ai whatever they want and it takes care of it. They also seem excited about customizing the ai's behaviour when it starts interacting with their guests as a guest concierge.
>
> Here's some things they said that stood out during the call:
>
> * "especially for complicated weddings, I think the AI is really effective. I love how you can personalize it."
> * "the ease of access, the ability to use the AI to do things in a bespoke way, that's where the value comes in."
> * "impose rules on your wedding that are personalized to your wedding."
> * "\[the ai handles\] exactly the kind of problem that your standard off-the-shelf wedding website cannot solve."
> * "The entire point of the AI is to wiggle around fixed positions."
>
> I'm not sure if that's helpful or not...As I'm writing this I'm worried this is just an extremely unique individual?

---

> **That-Promotion-1456**（1 分） · 2026-09-17T06:59:00+08:00　
> facebook used to be correct channel for wedding photographers so maybe try there.

---

> **That-Promotion-1456**（1 分） · 2026-09-17T07:02:04+08:00　
> now you need to create a wedding marketplace, add photograhers, caterings, venues and get your money from deals, and not charge the couple. and create business around it. then you are not doing a SaaS but running a wedding related service business and provide real value.

---

> **alexid95**（1 分） · 2026-09-17T07:24:56+08:00　
> i'd watch 20 PostHog recordings before another A/B test. with 1 click from 322 visits, where people stop or scroll will tell you more than another headline split.

---

> **Emotional_Hat_5474**（1 分） · 2026-09-17T08:00:49+08:00　
> the point about the builder crowd upvoting anything with an agent is spot on tbh

---

> **Background-Rule3903**（1 分） · 2026-09-17T08:23:47+08:00　
> Speak to wedding planners or attend a wedding roadshow/conference you’ve got such a defined target audience you can grab in the real world at least initially

---

> **alex-veora**（1 分） · 2026-09-17T09:32:11+08:00　
> you didn't mistake interest for validation, you validated the wrong thing. the claudeai post proved builders like clever builds. nobody there was planning a wedding. that's the whole story tbh
>
> what i'd do this week instead of more ads: find 10 couples who are actually 3-9 months out. wedding subreddits, facebook groups, the friend of a friend who just got engaged. dm them, set up their wedding in the app yourself, on a call. you'll learn in 10 conversations what 322 instagram visitors will never tell you. and one of those couples will say the sentence that becomes your landing page

---

> **elias-nurmi**（1 分） · 2026-09-17T09:47:21+08:00　
> The 10 or 15 who said theyd use it are still just words, a comment costs nothing. What you want to know is did any of them actually put an email in, because a free signup is a much higher bar than a nice reply.
>
> Life event timing isnt a targeting option you toggle, its more that you catch people through search and content at the moment they get engaged. Instagram rarely knows someone just got engaged. Google does, roughly.

---

> **West_Inevitable_2281**（1 分） · 2026-09-17T10:37:06+08:00　
> I would not dismiss this person as unusually unique yet. Their language is pointing to a specific segment: couples who do not want a full planning system, but do want a flexible assistant that adapts to their particular wedding. That is different from targeting “people interested in weddings.” The next test is whether several couples with a date and venue respond to that same promise.

---

> **indie_morphme**（1 分） · 2026-09-17T11:56:58+08:00　
> 这个项目挺复杂的

---

> **indie_morphme**（1 分） · 2026-09-17T11:57:55+08:00　
> 结婚的人应该会越来越少

---

> **Thin_Sky**（1 分） · 2026-09-17T12:05:09+08:00　
> Thank you so much for your responses. Im learning it's deceptively hard to just look at the data and let it speak without allowing biases and preconceived notions to cloud things. Your outside perspective is really appreciated.

---

> **Thin_Sky**（1 分） · 2026-09-17T12:08:21+08:00　
> So far I've found it insanely difficult to get in contact with couples. Should I just be cold contacting them by DM then?

---

> **alex-veora**（1 分） · 2026-09-17T12:24:30+08:00　
> cold dm to a stranger, no, that gets ignored or reported. warm dm, yes, and the warmth is one step: comment first. r/weddingplanning and r/Weddingsunder10k have daily "how do you manage guest questions" type posts. answer 5 of those properly, no link, just help. then dm the 2 ppl whose problem matched your app exactly: "saw your post, i built something for exactly this for my own wedding, want me to set yours up for free?"
>
> the other route that worked for me in a different niche: don't chase couples, chase the ppl couples already talk to. one wedding planner or a venue coordinator sees 30 couples a season. give them the tool free, they hand it to every couple. 2 planners beat 50 dms

---

> **Thin_Sky**（2 分） · 2026-09-17T13:54:08+08:00　
> Yeah I've been reaching out to wedding planners with that exact idea in mind but not getting any responses. But I was pitching it as something to help them plan.. I think I need to refine the pitch but I'm struggling.
>
> Thanks for your advice I really appreciate it.

---

> **Guilty_Lingonberry**（1 分） · 2026-09-17T15:06:18+08:00　
> one thing your post made me think: aiDo is hard to explain as landing-page copy because the useful part is the interaction. a short clip where the host AI updates one wedding detail, then the guest concierge answers using it, would make the difference from a normal wedding site much easier to see.
>
> I’m building Retake, an agent that records browser walkthroughs. happy to make that clip for you free if it would help with the next round of testing.

---

> **buildswithtom**（1 分） · 2026-09-17T16:37:01+08:00　
> You didn't mistake interest for validation, you just had it at a much smaller scale than we did, so here's the big version of the same lesson.
>
> I build a tool that makes PowerPoints inside ChatGPT (so, disclosure: I'm the vendor in this story). Last Monday ChatGPT started suggesting our app inside conversations for some slice of users. Nothing we did, no post, no ad. In six hours we got 6,000+ sign-ups, about 25 normal days of traffic. Servers fell over, the database hit its connection limit, we found four bugs that had been in production for months. It made about $1,000 that day, more than three times the whole previous month.
>
> Then it stopped like a switch. And the next day about a third of those accounts logged in again, but only around 2 in 100 actually made a slide. The rest was people poking at the thing that had been put in front of them, same as your ClaudeAI upvotes.
>
> So the two numbers I'd watch instead of visitors and clicks: how many people do the core action once, and how many do it again a week later. 6,000 sign-ups taught me nothing about the product (besides some bugs). The 120 who came back did. Your one person still using it is the same signal, just small. Find out what's different about them before spending another dollar on Instagram.

---

> **cicygo**（1 分） · 2026-09-17T22:06:42+08:00　
> Bot followers are Instagram filling your placement with cheap inventory, not your audience talking to you. Yes to the question, put it before the email field since one tap costs a curious person nothing. Local ads are the same bet in a smaller pond, the couples with a date are the ones who just got engaged and started telling people. Check the answer split on your next hundred visitors before you touch the page again.

---

> **cicygo**（1 分） · 2026-09-17T22:16:05+08:00　
> 10 or 15 people in that thread said they would use it and one actually did. Builder subs hand out the upvote for free, signing up is a different decision.

---

> **alex-veora**（2 分） · 2026-09-18T01:33:19+08:00　
> yeah, "help you plan" is the wrong pitch for a planner, that's their job and it sounds like you're replacing them. flip it: you're the thing that saves them 40 texts a week from guests. something like "your couples' guests ask you about parking and schedules all week, i built a bot that answers them so you don't have to. want me to set it up for your next wedding, free?" and go through instagram dm not email, planners live on ig. 10 dms like that, i'd bet 2 say yes

## 导航

- 项目页：[[10-项目/My-app-went-viral-before-it-was-ready.-Now-it’s_d53b678a]]
- 渠道页：[[50-渠道/reddit]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
