---
type: "corpus"
item_id: "ca4a4f22e4c07ff3"
title: "What do you use for customer support, and how do you handle customers who get stuck?"
source: "reddit"
source_name: "Reddit 独立开发版块"
url: "https://www.reddit.com/r/SaaS/comments/1x6o02a/what_do_you_use_for_customer_support_and_how_do/"
author: "bucknell73"
published_at: "2026-10-15T23:01:17+08:00"
captured_at: "2026-10-25T23:28:28+08:00"
lang: "en"
kind: "post"
topic: AI 工具/Agent
shard: "2026-10-25"
pub_day: "2026-10-15"
tags:
  - 语料
  - reddit
  - r/SaaS
metrics: {"score": 5, "comments": 22, "upvote_ratio": 1}
comments_count: 18
comments_total: 22
discovered_via: "reddit:14d+settle10"
---

# What do you use for customer support, and how do you handle customers who get stuck?

> [!info] 一句话导读
> I'm trying to understand how small B2B SaaS teams handle customer support, and I'd like to hear what works for you.

> [!meta]- 语料信息（点开展开）
> 来源：Reddit 独立开发版块（post）
> 原帖：<https://www.reddit.com/r/SaaS/comments/1x6o02a/what_do_you_use_for_customer_support_and_how_do/>
> 指标：得分=5 · 评论=22 · 赞踩比=1
> 作者：bucknell73　|　发布：2026-10-15T23:01:17+08:00
> 项目链接：—
> 采集：2026-10-25T23:28:28+08:00　|　id：`ca4a4f22e4c07ff3`

## 正文

I'm trying to understand how small B2B SaaS teams handle customer support, and I'd like to hear what works for you.

* What tools do you use (help desk, live chat, email, calls)?
* When a customer is stuck and can't explain the problem, what do you do? Screenshots, screen recordings, a video call?
* Is there a step in your support process that you find annoying or that costs you customers?
* Do you run support yourself, or do you have a dedicated person?

I'm early in this and want to learn from real setups, not marketing pages. Thanks for any insight.

## 评论（18/22）

> **HuckleberryNo1307**（2 分） · 2026-10-15T23:31:02+08:00　
> the stuck-customer one is where support threads go to die. they tell you what they clicked, not what broke, and you spend twenty messages reverse-engineering a sentence. whatever tool you pick, make step one of the process "what were you trying to do" - that question alone kills half the back and forth

---

> **Tedikraska**（1 分） · 2026-10-15T23:59:49+08:00　
> i do it all myself with crisp for chat and plain email behind it. when someone's stuck i skip the back and forth and send them a quick loom of me doing the exact thing they're trying to do, that fixes most of them in one reply. and if two people get stuck on the same step i treat it as a ui bug, not a support ticket.

---

> **AutoModerator**（1 分） · 2026-10-16T00:00:49+08:00　
> Low-Effort/AI content is auto-removed.
>
> *I am a bot, and this action was performed automatically. Please [contact the moderators of this subreddit](/message/compose/?to=/r/SaaS) if you have any questions or concerns.*

---

> **beigs-sl**（2 分） · 2026-10-16T00:59:03+08:00　
> Email and a shared inbox will carry you further than you'd think. You just need to be prepared for the spam.  What actually saves me the most time though is asking for a screen recording instead of a description, our application has screen recording built-in, and a quick thirty-second video usually shows me the problem right away. Most of support is people trying to describe a screen, and they're bad at it, I am too. And I would run it yourself as long as you can stand to.

---

> **SCS-AI**（2 分） · 2026-10-16T01:27:44+08:00　
> The step that quietly costs you customers isn't the stuck ticket, it's the silent gap before your first reply. Someone who's stuck is already a bit frustrated, and every minute of nothing turns a small bug into a reason to leave. An instant auto-ack with a real ETA -- "got it, you'll have an answer from me by end of day" -- does more for retention than fast resolution does. They stop refreshing and go back to work.
>
> On the stuck customer, the "what were you trying to do" point above is right. I'd add one thing to it: ask what they expected to happen vs what actually did. The gap between those two is almost always where the real bug is, and it skips the twenty-message reverse-engineering. Screen recordings help, but "send me a recording" is itself a step people get stuck on, so hand them the exact button to start it.
>
> The part that compounds: tag every ticket by the step it died on, not by topic. After a month your top three tags stop being a support queue and start being your roadmap. Repeat tickets on one step are a UX score for that step, not a people problem.
>
> And run it yourself as long as you can stand to. Early tickets are product research you can't buy -- the day they stop surprising you is the day you hand it off, not before.

---

> **kkaramazzov**（2 分） · 2026-10-16T02:27:44+08:00　
> I maintain a few products. so I built a support tool that fits my workflow (bubblegram.co)
> It covers live chat widget and email. When a customer reaches out, I get a Telegram message, reply there, and it goes straight back to the widget or their inbox. Recently I added automated replies: AI reads my site, docs and notes, and answers on its own. When it's unsure, it hands off to me.
>
> When customer is stuck its usually design / onboarding issue. Iterate and test again, onboarding is tricky to nail.

---

> **fernandops**（2 分） · 2026-10-16T05:57:47+08:00　
> A support message is much easier to investigate if it includes the page URL, app version and the failed request's ID automatically. A recording shows what the person saw; that context lets you find the corresponding error without asking them to open developer tools.

---

> **Ok-Yi**（2 分） · 2026-10-16T06:39:47+08:00　
> generally screenshots are very helpful. they're easy for the customer to do (oppose to video recordings) and you can see what actually is going on on their screen. Often it turned out to be a user error. However, the most long-term fix for us has been good self-serve search on the docs/site so they find the answer (or get an AI answer from that content) before they open a ticket. Full disclosure, I'm building FlowSearch (flowsearch.io) for exactly that. It crawls your published pages (including your knowledge base) and gives live results plus optional AI answers.

---

> **bucknell73**（1 分） · 2026-10-16T16:44:41+08:00　
> u have video recording tool installed.. did u build it yourself? or are there such service?  if so, can i get the name of it so that i can share with my team.

---

> **EmpireVault**（2 分） · 2026-10-17T01:25:27+08:00　
> I still run support myself. shared inbox plus a simple ticket form, and customers can just email it. no login required to ask for help.
>
> For stuck customers i stopped doing the long email back and forth. if it isn't sorted in two replies, i send a calendar link for a 10 minute screen share. it feels slower, but it's way faster than 15 emails, and you see exactly where they got lost.
>
> The step that cost us the most was making people log in or pick a category before they could ask anything. a lot of them just gave up. we made it as easy as sending an email and the number of tickets dropped, because the problems got caught earlier instead of turning into churn.
>
> If two people ask the same thing, that's a product fix, not a canned reply.

---

> **spiggle_64236**（1 分） · 2026-10-17T03:34:39+08:00　
> Early on I kept it boring: one shared support email + a tiny live chat widget, and I answered everything myself. For stuck and can't explain it, the reply that worked best was two lines:
>
> "What were you trying to do, and what happened instead?"
>
> "A 20-second screen recording (or even a screenshot of the page) helps a lot."
>
> The step that quietly costs customers is the silent gap before the first human reply. An auto-ack with a real ETA ("got it, I'll look within 2 hours") beats a fancy bot that asks them to repeat the story.
>
> Disclosure: I build a helpdesk (TickitDex), so I'm biased toward email + chat in one inbox with AI drafts a human approves. Until you're past \~50 tickets a month, a shared inbox is enough. Just write down the questions you answer twice.

---

> **saloprj**（2 分） · 2026-10-18T01:13:02+08:00　
> Small team here, support is split between me and one other person. What ended up mattering more than the tool: put every place customers reach you into one inbox (email, the chat on the site, WhatsApp if your users are on it), so whoever answers sees the whole history and nobody asks "what's your account email" twice.
>
> For the stuck customer, a description almost never helps. We ask for a screen recording first, and if they can't do that we jump on a short call with screen share. Five minutes on a call beats twenty messages, and you usually spot a UX problem you'd never have found from the ticket.
>
> The step that cost us the most was the silence before the first reply. We now let an AI agent answer the first message right away from our help docs, and it hands over to a person the moment it isn't sure. It doesn't solve the hard ones, but the customer isn't staring at nothing while they wait.

---

> **AutoModerator**（2 分） · 2026-10-18T22:50:35+08:00　
> Your comment was removed. Links in comments require to gain karma first in r/SaaS. Earn sub karma by commenting helpfully first.
>
> *I am a bot, and this action was performed automatically. Please [contact the moderators of this subreddit](/message/compose/?to=/r/SaaS) if you have any questions or concerns.*

---

> **lazyatom**（2 分） · 2026-10-21T16:39:18+08:00　
> Like other folk are saying, screenshots probably are the easiest thing, but you might also be able to use some of the new screen recording stuff that's built into analytics/error software like Posthog and Sentry -- it can record what the user is seeing and doing. Could be worth a shot.

---

> **-adam_**（1 分） · 2026-10-21T18:02:34+08:00　
> For our iOS apps we built a tool for it ourself, [reception.sh](http://reception.sh)
>
> Saw quite good results, users really like it when you give them attention.
>
> Also, you can turn it into a conversion as well, like offering them a discount via the chat, asking for a review etc. We also have AI to auto reply, but you gotta be careful with this, because of course, some people really don't like that (understandably so).

---

> **AntrioSanture**（1 分） · 2026-10-22T19:32:23+08:00　
> bro for a small SaaS id honestly keep support simple at first
>
> email or live chat is enough and when someone gets stuck just ask for a quick screen recording instead of going back and forth with 10 messages 😭
>
> also id keep track of questions people ask repeatedly because if 5 users get stuck at the same place its probably a UX problem not a support problem
>
> fixing that one thing can save you more time than hiring someone to answer the same question every day

---

> **SeaWealth4844**（1 分） · 2026-10-23T15:07:31+08:00　
> Solo founder, so my setup is small. A chat bubble on the site answers from the FAQ that's already on the page. Anything it can't answer comes to me as a Telegram message with the visitor's email, I reply from my phone, and they see the answer in the same chat window. Longer threads move to email.
>
> On customers getting stuck, what helped me:
>
> 1. Ask for an email the moment the bot hands off. People close the tab, and without it you can't follow up.
>
> 2. Answer where they get stuck. If a question comes in twice, it becomes an FAQ entry on that page or a UI fix.
>
> 3. Read every question that reached you once a week. That's your cheapest product research.
>
> I made the chat part (productchat, MIT, runs on your own Postgres: github.com/chidhu07/productchat), so I'm biased. It doesn't do AI answers or routing between agents, so if your team needs those, Crisp or Intercom fit better.

---

> **Particular-Pilot-834**（1 分） · 2026-10-24T01:07:53+08:00　
> I manage a customer support team, and one thing I've learned is that the software matters less than what happens when a customer gets stuck.
>
> A shared inbox and clear ownership of each issue go a long way. But the real test is whether the customer can get a resolution without repeating their story across multiple agents or channels.
>
> When evaluating AI support tools, I'd pay particular attention to human handoffs, conversation history, and how the platform measures successful resolutions versus simply closing tickets.
>
> What's your current support volume looking like?

## 导航

- 项目页：—（本条不是项目，按设计不建实体页）
- 渠道页：[[50-渠道/reddit]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
