---
type: "corpus"
item_id: "b8a04cb555ded084"
title: "220 signups, 0 paying users. My product requires a habit my users don't have. How do you fix that?"
source: "reddit"
source_name: "Reddit 独立开发版块"
url: "https://www.reddit.com/r/microsaas/comments/1xs4n4x/220_signups_0_paying_users_my_product_requires_a/"
author: "Powerful-Run-1485"
published_at: "2026-11-10T05:40:28+08:00"
captured_at: "2026-11-20T09:46:53+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-11-20"
pub_day: "2026-11-10"
tags:
  - 语料
  - reddit
  - r/microsaas
metrics: {"score": 4, "comments": 48, "upvote_ratio": 1}
comments_count: 42
comments_total: 48
discovered_via: "reddit:14d+settle10"
---

# 220 signups, 0 paying users. My product requires a habit my users don't have. How do you fix that?

> [!info] 一句话导读
> I'm 20, solo dev, and I've been building a trading journal for prop firm traders for about a year. I built it because I trade prop accounts myself and nothing o…

> [!meta]- 语料信息（点开展开）
> 来源：Reddit 独立开发版块（post）
> 原帖：<https://www.reddit.com/r/microsaas/comments/1xs4n4x/220_signups_0_paying_users_my_product_requires_a/>
> 指标：得分=4 · 评论=48 · 赞踩比=1
> 作者：Powerful-Run-1485　|　发布：2026-11-10T05:40:28+08:00
> 项目链接：—
> 采集：2026-11-20T09:46:53+08:00　|　id：`b8a04cb555ded084`

## 正文

I'm 20, solo dev, and I've been building a trading journal for prop firm traders for about a year. I built it because I trade prop accounts myself and nothing out there fit how I actually work.

The main idea: you log a trade by uploading a screenshot of your chart, and AI reads it and fills in the trade for you (entry, SL, TP, direction, result). I chose screenshots on purpose. There's no broker connection or automation, because I didn't want anything touching people's prop accounts and putting them at risk.

It also tracks your accounts by phase (Phase 1, Phase 2, Funded), so you can see how you're doing in each challenge separately. On top of that you get stats, psychology patterns and an economic calendar.

Here's where I'm at:
\~220 signups, all free, zero paying customers
Only \~26% log their first trade
7-day retention is around 5%
I emailed \~50 inactive users asking for feedback. Zero replies.

The core problem, I think: journaling only pays off after weeks of consistent logging, and most traders simply don't have that habit. Logging trades feels like homework. The value (spotting patterns, seeing why you keep failing) shows up way too late, so people leave before they ever get it. I added history import to reduce the effort, but activation barely moved.

On top of that, my distribution kept breaking. My main X accounts got suspended, so new signups mostly dried up.

I'm not looking for trading advice specifically. I'd love to hear from anyone who's built a product that depends on users forming a habit (fitness, finance, note-taking, language learning, whatever):
How did you get users to the "aha" moment before they had invested much effort?
Did you ever narrow down to a super specific use case to make the value obvious? Did it work?
When users won't answer feedback emails, how did you actually get to talk to them?

Happy to share more numbers or details. Brutal honesty welcome.

## 评论（42/48）

> **nextammy**（2 分） · 2026-11-10T06:03:00+08:00　
> Your numbers point to the same issue: the first trade is doing too much work. 26% activation and 5% retention after a week is not a pricing problem yet, it is an onboarding problem. I would make the first win happen before any real journaling. Let a new user upload one screenshot and show them one clear insight right away, like their biggest losing pattern or a simple win rate by setup, without asking them to set up accounts or phases first. If that first upload feels useful on its own, the second one is much easier. Narrowing helps here too. Instead of a journal for all prop traders, focus on one painful moment, like traders who just failed a challenge and want to know why. That makes the value obvious in one sentence and makes it easier to find them in the places they already talk. For the silent users, email is probably too easy to ignore. Try a short in-app prompt right after signup, or right after they abandon the first upload, asking what stopped them. One question, with a few quick options, will get more replies than an open email. You could also offer five short calls in exchange for a month free, and put that offer inside the product where active users will see it, not only in email. I would fix activation before worrying about paying customers. If you can get first trade logging from 26% to 50% or so, the retention and conversion numbers will tell you a very different story.

---

> **XRay-Tech**（1 分） · 2026-11-10T06:27:19+08:00　
> You've got the right idea, but I'd push on one thing: 74% never logging a first trade is a different problem from "journaling is a habit".  Habit failure shows up at week 2.  Not logging even once means the first session didn't give people a reason to bother.  I would fix the time to first value before worrying about retention.
>
> Currently the payoff of your product is "stats after weeks of logging."  What if the first session delivered something useful with no history needed?  For example, upload your last 10-20 screenshots and get a one page report back.  That's a bigger ask than a single trade, but it pays off in 5 minutes instead of 5 weeks.  Your history import was the correct instinct, but if the output after import isn't immediately interesting, it won't move activation.
>
> On narrowing the use case, the phase tracking is the most differentiated thing you described, and it's the one that ties to something prop traders feel right now: not blowing the challenge.  Something like distance to daily loss limit, drawdown left, consistency rule status.  That is value on day one, and it gives people a reason to open the app before a session, not after as homework.  "Protect your challenge fee" is a much easier pitch than "journal your trades," and is a natural thing to charge for, as people already pay for the challenge.
>
> For feedback, I would ignore the inactive list.  A cold email from a product feels like a survey, and 50 sends with zero replies is normal.  Talk to the roughly 57 who did log a trade, especially the few who came back, and offer a short call in exchange for a free month.  Just a few conversations will give you more information than an email blast could.  Prop trading Discords and subreddits are also full of people complaining about exactly this, so you can ask there without pitching.
>
> Finally, with 220 signups, I would treat everything as a hypothesis, not a verdict.  Pick one change (instant first-session report, or lead with phase tracking), run it on the next 30 signups, and see if the 26% moves.

---

> **Brufacee**（1 分） · 2026-11-10T09:21:05+08:00　
> The 26% first-trade rate makes me want to watch the screenshot upload before adding habit features. Could you ask a few people who did log one to show you that first session? They have less distance to travel than the inactive users, and may remember what nearly stopped them.

---

> **Ok_Climate9032**（1 分） · 2026-11-10T09:31:14+08:00　
> Small thing: if activation is "logged their first trade", history import shouldn't move it much, since importing isn't logging a trade. That number was never going to react to that feature.

---

> **techtuber101**（1 分） · 2026-11-10T09:51:59+08:00　
> i'd read your own numbers as a first-session problem, not a habit problem. 26% logging a first trade means 74% saw the empty state and left. that's before anyone needs a habit.
>
> two things to try this week: let people try it with zero signup, upload a screenshot and show the one insight right there. then email the 50 inactive users differently, don't ask for feedback (nobody replies to that), ask one yes/no question like "did you fail a challenge in the last month?" and reply to every answer by hand.
>
> also the value being weeks away is fixable by showing a sample journal pre-filled with example trades, so they see the payoff on day one.

---

> **luke_qualified_hires**（1 分） · 2026-11-10T10:52:13+08:00　
> This!

---

> **shredmaster19**（1 分） · 2026-11-10T13:51:06+08:00　
> Have you mapped user sentiment at each touchpoint of your users’ journeys throughout their experience? Would be helpful to conduct a user journey mapping workshop.

---

> **N_Moon_3019**（1 分） · 2026-11-10T13:51:10+08:00　
> Zero replies to 50 churn emails is the expected result, not a failure — someone who left doesn't owe you a conversation. They do leave one-line reviews on other apps, though.
>
> Concretely: list the 5 journal / prop-firm apps your users most likely came from, pull their most recent ~200 reviews, and read only the 1-2 star ones. Not for sentiment — you're looking for one sentence shape: "I stopped because ___". Manual logging is too slow. P&L wrong after a partial close. Can't import from MT4/MT5. Paywall hit at the wrong moment. Whichever sentence repeats most across those five apps is the honest answer to "should I narrow, and to what".
>
> Two things show up in that data and not in your own analytics:
>
> - The abandonment reason is rarely "didn't see the value". It's "the value arrived after work I didn't want to do". Your 5% D7 and your own "logging feels like homework" note are the same fact stated twice.
> - Day-1 quitters and day-30 quitters say different things. Sort by date window, not by count: 200 reviews is two days for a popular app and two years for a quiet one, so the same number is a different story.
>
> On the aha moment: for a journal the aha isn't "I logged a trade", it's "it told me something about myself I didn't know" — and that needs N trades. So either shrink N (screenshot import is the right instinct) or show a partial aha at N=2: here's what your first two trades already suggest, and what we'd show you at 20.
>
> Not a habit product, but I build ReviewFold, which turns store reviews into a report with the source reviews behind each finding — so this is the loop I run when I need to know why people leave. You can do it by hand for 5 apps in an afternoon, no tool needed.

---

> **kbr89**（1 分） · 2026-11-10T15:10:27+08:00　
> Agree with the first-session read. One thing that moved this number for me: don't let a new user land on an empty journal. Pre-fill the account with one sample trade already logged, with the stats and the phase view populated, and a clear button to replace it with their own screenshot. People need to see what the product looks like after a week of use before they'll do the first week of work.
>
> I had the same 74% problem with beyondtube (beyondtube dot pro), where new users had to import a video before seeing anything. Showing a finished example on the first screen helped more than any email sequence. Also, skip asking churned users for feedback. Watch three people who did sign up try to log their first trade on a call, you'll see the blocker in ten minutes.

---

> **mantasn**（1 分） · 2026-11-10T15:36:14+08:00　
> Lots of good onboarding advice here already. But one narrower thing is that the first trade depends on the AI reading the screenshot right. If it gets the entry or the stop loss wrong on someone's first try, they won't trust it with a second one. Its gone.
>
> Of the 74% who never logged a trade, how many uploaded a screenshot and left at the result screen? If that's a big share, it's an accuracy problem, not a habit problem.

---

> **Powerful-Run-1485**（1 分） · 2026-11-10T16:29:02+08:00　
> The “traders who just failed a challenge” angle hit hard, because that’s literally why I built it. I failed challenges and couldn’t tell you why.
>
> One thing I’m going to steal directly: the in-app question right after someone abandons the first upload. One question, 4 options, no email. That’s cheap to build and probably gets more data in a week than my email did in a month.
>
> The 5 calls for a free month I’m doing too. I’ll report back on whether the 26% moves.

---

> **Powerful-Run-1485**（2 分） · 2026-11-10T16:32:19+08:00　
> The “protect your challenge fee” reframe is the most useful thing in this thread for me. It also fits better than you might think, because the phase tracking already exists (Phase 1 / Phase 2 / Funded per account). Right now it’s buried as a filter instead of being the front door.
>
> On the import point: CSV import is actually already part of onboarding, so the effort side is mostly covered. What you said about the output is what’s missing. After importing, people land on a normal dashboard, not something that says “here’s what your last 30 trades reveal”. So the import works, but there’s no payoff moment after it.
>
> So two changes, both about flipping what comes first:
> \- After CSV import: show a one-page report right away (worst session/day, avg R lost on rule breaks, where the drawdown came from) instead of dropping them into the app
> \- Phase view as the entry point: add your challenge rules (daily loss, max DD, target), see drawdown left + distance to target on day one, and let trades feed that view
>
> That gives people a reason to open it *before* a session, which is the opposite of homework. I’ll test one of these on the next \~30 signups like you said and see if the 26% moves.

---

> **Powerful-Run-1485**（2 分） · 2026-11-10T16:32:44+08:00　
> Pulled the numbers. Of \~210 signups, \~120 created a challenge account but only 53 ever saved a trade, so 67 people did the setup and stopped right at the first trade. That’s exactly where your accuracy theory would show up. I don’t track abandoned scans yet, so I’m adding that today. You may well be right.

---

> **Powerful-Run-1485**（2 分） · 2026-11-10T16:33:10+08:00　
> Good call, the people who made it through are closer to the problem than the ones who bounced. Going to ask 3/ 4 of them to share screen and redo a first upload from scratch while I stay quiet. Thanks.

---

> **Powerful-Run-1485**（1 分） · 2026-11-10T16:33:29+08:00　
> Checked it: “any trade, any source” is 53 users, and only 1 of them came through CSV. So import was never going to move activation regardless of how I measured it. Nobody’s using it.

---

> **Powerful-Run-1485**（1 分） · 2026-11-10T16:34:11+08:00　
> Two of these I’m doing, one I’m not sure about:
>
> \- Sample journal pre-filled. Yes. Right now new users land on an empty state, which is the worst possible first screen for a journal.
> \-  Yes/no question to the inactive list. “Did you fail a challenge in the last month?” is a way better opener than “any feedback?”. Sending it this week and answering every reply by hand.
> \- Zero-signup upload. I like it, but the AI scan costs me per call (Claude API), so I’d need to rate-limit it hard. Maybe 1 free scan per visitor, then signup to save it?

---

> **Powerful-Run-1485**（1 分） · 2026-11-10T16:34:21+08:00　
> Probably overkill at 220 users and solo, but the idea behind it is right. I’m going to do the lightweight version: watch a few real first sessions and note where people hesitate

---

> **Powerful-Run-1485**（1 分） · 2026-11-10T16:34:47+08:00　
> The “I stopped because X” filter is a really good way to read reviews, gonna do it by hand this week. Plan: TradeZella, Tradervue, Edgewonk, TraderSync + one prop-specific one, 1–2 star only, split by early vs late quitters like you said.
>
> The N=2 partial aha is interesting too: “here’s what your first 2 trades already suggest, here’s what we’d show at 20.” That’s basically a progress bar toward the payoff instead of making people wait blindly.

---

> **Powerful-Run-1485**（1 分） · 2026-11-10T16:35:00+08:00　
> “See what it looks like after a week before doing the first week of work” is exactly the gap. Quick question since you went through the same 74%: did you show the example as *your* fake data with a “replace with yours” button, or as a separate demo they could leave? I’m wondering whether keeping it inside their real account makes the first upload feel more natural.

---

> **mvrk57**（1 分） · 2026-11-10T17:18:10+08:00　
> your users already make the screenshots, they just post them somewhere else. a lot of prop traders drop every trade into a discord group or their tradingview ideas anyway, so a bot or share sheet that logs the trade right at that moment costs them zero extra effort. then the journal stops being homework and becomes a side effect of something they do already

---

> **shaigexp**（1 分） · 2026-11-10T17:26:52+08:00　
> Seventy-four percent bouncing before a single trade is not a habit problem, it is a "why would I bother" problem. Let someone paste one screenshot and see a useful pattern before you even ask for an account, or the journal stays a nice idea they meant to use.

---

> **techtuber101**（1 分） · 2026-11-10T17:49:44+08:00　
> yeah 1 free scan per visitor then signup to save it is the right shape. cap it by ip plus a cookie, and run the scan on a smaller cheaper model or a downscaled image first so a free scan costs you cents. show the insight blurred past the first line if you want a reason to sign up, but let them see enough to feel the payoff before they hit the wall.

---

> **Powerful-Run-1485**（1 分） · 2026-11-10T17:50:05+08:00　
> This is a really good reframe: don’t create a new habit, attach to one that already exists. And I have an easy place to test it: I run a small trading Discord where people already drop their trade screenshots in a channel.
>
> Rough version I’m thinking:
> \- Link your Discord to your account once
> \- Post your screenshot in #trades like you already do
> \- Bot reacts and the trade lands in your journal, with a reply showing the extracted entry/SL/TP so you can fix it if it’s wrong
>
> The sharesheet side (from TradingView on mobile) makes sense too, but the Discord bot is faster to build and test. Did you see this work somewhere, or is it an idea? Curious whether people mind a bot replying to their posts in public.

---

> **Powerful-Run-1485**（1 分） · 2026-11-10T17:52:57+08:00　
> Agree on “why would I bother”, with one nuance from my data: most people don’t bounce before an account. \~57% actually set up a challenge account, then stop before saving a single trade. So the “why bother” moment is right at the first upload, not at signup.
>
> Going to test exactly what you said: 1 free scan before signup, with one insight shown right away. If people see something useful from a single screenshot, the account becomes a way to save it instead of a hurdle.

---

> **Powerful-Run-1485**（1 分） · 2026-11-10T17:54:41+08:00　
> Makes sense, that’s basically the build spec. IP + cookie cap and downscaling I’ll do as is.
>
> The cheaper model part I’m a bit torn on, because of what mantasn said above: the free scan is the trust moment. If a smaller model misreads the SL on someone’s very first screenshot, I’ve paid less to lose them faster. So I’m thinking: downscale the image (that’s most of the cost anyway), keep the model that actually reads charts well, and only drop to a cheaper one if the numbers force it.
>
> On blurring: I’d rather show the full extracted trade + one insight, and gate what comes *next* (“save it and see how this compares to your next 10”). Blurring the payoff feels like it fights the whole point of the free scan. Will report back on what it costs per visitor.

---

> **mmdincer**（1 分） · 2026-11-10T19:01:38+08:00　
> Prop traders already obsess over the challenge rules, so I'd make the first screenshot tell them something like how close that trade put them to the daily loss limit. That's useful on day one, while the journal only pays off weeks later.

---

> **Powerful-Run-1485**（1 分） · 2026-11-10T19:50:56+08:00　
> This connects two things from this thread I hadn’t put together. \~57% of signups already set up a challenge account with its rules, and then stall at the first trade. So the rules are sitting right there, unused, at the exact moment people drop.
>
> So the first scan result would read something like:
>
> EUR/USD short · −0.8R · −400$
> Daily loss used: 80% of 500$ → one more loss like this and the day is over
> Max drawdown left: 2,600$ · Distance to target: 3,400$
>
> That’s an answer to “am I about to blow this?”, not just a logged trade. For the free scan before signup there’s no account yet, so I’d just ask “which firm + account size?” with presets (FTMO, FundingPips, etc.) and pull the rules from that. Two taps instead of a setup form.

---

> **mantasn**（1 分） · 2026-11-10T22:12:27+08:00　
> That's a big, clear drop, so good that you can see it now. One more signal you may already have: of the 53 who saved a trade, how many edited what the AI filled in before saving? If most corrected the entry or stop loss, that's the accuracy problem showing up even among the people who stayed, and fixing it would help both groups.

---

> **Powerful-Run-1485**（1 分） · 2026-11-10T22:15:58+08:00　
> I don't have that one yet. I only store the final saved trade, not what the AI originally extracted, so I can't diff them. Adding that today alongside the abandoned scan tracking, so in a week or two I'll know both numbers. Honestly this is the most useful feedback I've gotten so far, thanks for digging into it.

---

> **mantasn**（1 分） · 2026-11-10T22:21:08+08:00　
> Glad it helped! 🤝 Post the numbers here when you have them, I'm curious how it splits. And since you already got 210 people to sign up, what did you try first to get them, and was there anything that didn't work that you'd skip next time?

---

> **mmdincer**（1 分） · 2026-11-10T22:55:56+08:00　
> The presets are a good call, most people know their firm and account size without thinking. I'd still let them tweak the numbers after, in case their account doesn't match the preset.

---

> **ProofOfIncomeAI**（1 分） · 2026-11-11T08:10:42+08:00　
> The habit problem you described is the hard part, not the AI logging. Journaling and fitness apps often have the same shape: the useful pattern only appears after weeks, and most people are gone before that.
>
> The first action has to be useful on its own, before any streak exists. I looked at a one-person iPhone app where you take a progress photo and get a body-fat estimate immediately. Payment data from 9 November showed about $2,374 a month from 465 subscriptions. The founder has said paid ads did not pay back, and after he switched them off, customers came from free fitness tools and a blog he already had. My read, not his claim: the first photo has to be worth opening the app even if the user never comes back tomorrow.
>
> For the silent emails, I would ask one short question right after the first screenshot.

---

> **Brufacee**（1 分） · 2026-11-11T08:44:54+08:00　
> Nice, staying quiet is the hard part. I would note where they pause or need reassurance, even if they eventually complete the upload. Hope those sessions give you a clear next fix.

---

> **Powerful-Run-1485**（2 分） · 2026-11-11T15:40:58+08:00　
> Will do, I'll keep notes on every pause and every "wait, is this right?" moment, not just the drop offs. I'll post an update here once I've done the sessions. Thanks again, this thread has been more useful than months of guessing.

---

> **Competitive_Tune_590**（2 分） · 2026-11-12T02:24:08+08:00　
> tough spot. the habit gap is real — if the value only shows up after weeks, most people won't stick around. have you considered finding the few who do log consistently and talking to them directly? that small group might tell you what made it click for them. also, if you're looking for organic ways to find those early adopters on reddit, i built replyhey.com/?rh=8e7dc3e7 — it scans reddit for conversations where people are actively looking for trading tools, so you can reach them before they sign up. might help with the distribution side while you figure out retention.

---

> **After-Base-8368**（1 分） · 2026-11-12T10:43:07+08:00　
> Saw your reply about asking at the first upload. Bopmigo lets you ask “What’s stopping you from logging your first trade?” while someone is on that page, and they can answer there. Happy to help you try it on that flow.
>
> [Bopmigo](https://bopmigo.com/?utm_source=reddit&utm_medium=outreach&utm_campaign=feedback&utm_content=first_upload)

---

> **Powerful-Run-1485**（1 分） · 2026-11-12T15:33:52+08:00　
> Thanks! Yeah, talking to the consistent loggers is the plan. Already setting up a few screen share sessions with people who got through their first trade.

---

> **XRay-Tech**（1 分） · 2026-11-13T05:52:51+08:00　
> I'm glad that it helped.  It sounds like you already have most of the pieces.  It's mostly a matter of reordering what people see first.
>
> One suggestion for the test: change one thing at a time if you can.  With only about 30 signups, two changes at once will leave you guessing which one moved the number.  I would also track "logged first trade" and "came back within 7 days" separately, since the post import report should mostly affect the first and the phase view the second.  Curious to see how it goes.

---

> **Brufacee**（1 分） · 2026-11-13T08:56:33+08:00　
> Glad the thread helped. Looking forward to hearing what the sessions uncover.

---

> **mantasn**（1 分） · 2026-11-14T07:03:17+08:00　
> Curious how the abandoned-scan tracking turned out. Did it show where people stop between uploading and saving their first trade? It matters even more if you add the free scan before signup, since that one result is the whole first impression.

---

> **zibel_dub_bel**（1 分） · 2026-11-14T19:47:22+08:00　
> i’ve seen this exact friction when trying to onboard freelancers in belgrade into rigid systems here in dublin. if the habit doesn't exist, you have to build the habit for them rather than expecting them to build it first. maybe gamify the logging or make it social so they feel accountable to someone other than their own future self.

---

> **Powerful-Run-1485**（1 分） · 2026-11-16T15:46:54+08:00　
> Not yet, but this is exactly what I’m trying to figure out now. I realized I was treating it as a retention problem without really knowing where users were dropping off.
>
> I’m tracking the steps between uploading a screenshot and saving the trade, including whether users have to correct the AI results.
>
> I’ll share what I find. Really appreciate you pointing this out.

## 导航

- 项目页：—（本条不是项目，按设计不建实体页）
- 渠道页：[[50-渠道/reddit]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
