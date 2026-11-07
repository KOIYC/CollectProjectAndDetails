---
type: "corpus"
item_id: "674afa353a5f9e9a"
title: "Searching for Cold Calling Software for Agencies - help"
source: "reddit"
source_name: "Reddit 独立开发版块"
url: "https://www.reddit.com/r/SaaS/comments/1xh372u/searching_for_cold_calling_software_for_agencies/"
author: "jamsessio"
published_at: "2026-10-28T04:05:42+08:00"
captured_at: "2026-11-07T09:44:34+08:00"
lang: "en"
kind: "post"
topic: AI 工具/Agent
shard: "2026-11-07"
pub_day: "2026-10-28"
tags:
  - 语料
  - reddit
  - r/SaaS
metrics: {"score": 4, "comments": 7, "upvote_ratio": 1}
comments_count: 6
comments_total: 7
discovered_via: "reddit:14d+settle10"
---

# Searching for Cold Calling Software for Agencies - help

> [!info] 一句话导读
> I am searching for a cold calling software. Maybe someone could help with suggestions.

> [!meta]- 语料信息（点开展开）
> 来源：Reddit 独立开发版块（post）
> 原帖：<https://www.reddit.com/r/SaaS/comments/1xh372u/searching_for_cold_calling_software_for_agencies/>
> 指标：得分=4 · 评论=7 · 赞踩比=1
> 作者：jamsessio　|　发布：2026-10-28T04:05:42+08:00
> 项目链接：—
> 采集：2026-11-07T09:44:34+08:00　|　id：`674afa353a5f9e9a`

## 正文

Hi,

I am searching for a cold calling software. Maybe someone could help with suggestions.
There are many tools on the market, however I couldn’t find a suitable solution.
We run outbound cold calling for clients, setting qualified appointments.

Currently we use a tool that should have been the perfect match, however I think it’s not build properly, has many things not a tool should have in general, isn’t GDPR compliant (e.g. we can’t set DNC lists or contacts, which is needed for Europe, even they are a EU company)
Their list uploading is not good and some other things that should be standard for this kind of tools are not good or missing. Another example is the bad reporting and that they basically don’t have a good overview of set meetings.
I give them so much feedback, currently feeling more like their business development support then a client that can effectively use the tool.

Main use focus we would need:

\- Autodailer
\- Handle Different Clients/Projects/Lists
\- Has a CRM build (just need notes, buttons for meetings, DNC button, not interested and something that I can mark why the lead is not usable)
\- must be able to import different kind of numbers like direct phone and company phone and be able to sort it for the Autodailer correct
\- need to be able to set max. Touchpoints before the leads gets sorted out.
\- optional email and sms sending from the system (isn’t a criteria I would to not consider using it)
\- need to be able to get phone numbers for UK or US (without having a company there, wich is kind of normal, but the current tool doesn’t even provide that)
\- would be nice to have a call flatrate for the country included you have a phone number to make outbound calls.

Maybe someone has similar experience and found a tool that really works. Currently looking into other tools, but thought here are coming up some tools and ideas I haven’t looked into yet.

## 评论（6/7）

> **Mean_Bumblebee_8633**（1 分） · 2026-10-28T04:13:50+08:00　
> Orum might be worth a look, handles most of that multi-client autodialer stuff without falling apart. The built-in CRM bits are light but the follow-up triggers and DNC management actually work the way you'd expect, especially for EU compliance headaches. Not sure about the flatrate part though, think they tie into your own twilio or whatever.

---

> **jamsessio**（1 分） · 2026-10-28T04:31:04+08:00　
> Thanks for the reply. I just looked into it. Couldn’t find a video on their website so i checked youtube. It looks like you still have to get a normal CRM hooked up. And it’s more a AI call coaching then an Agency Tool. Funnywise I couldn’t find a pricing as it is on request, but I found a video wich states from 250€ per seat. Not a suitable option as far as I could figure it out based on the info their website provided and some videos I watched.
> But I appreciate that you took the time to respond 🙂 thanks for that
>
> ((Just one thing to the GDPR complaisance: a while back ago i search for tools to better train the reps etc. the main issue was the recording without permission (not something you do in cold calling) is not possible due to law, also AI help kind of triggers recording, normally that’s not allowed, not sure how they manage that nowadays. Also parallel call dialing isn’t allowed in the EU)

---

> **Mikewh6**（1 分） · 2026-10-28T12:34:07+08:00　
> The “unpaid product manager for your vendor” feeling is so real lol

---

> **Secret_Play9552**（1 分） · 2026-10-28T14:06:34+08:00　
> Look at Close for the dialer and CRM side. Power dialer, separate setups per client, follow-up reminders, and it picks up callbacks from unknown numbers as new leads. UK and US numbers are easy to get too. Check how it handles DNC for calls specifically before you commit, and run a trial with one real client list. Your max-touchpoints rule is the part most tools handle poorly. If nothing fits, a thin custom layer on Twilio with your own rules is less work than it sounds.

---

> **iammohamedatef**（1 分） · 2026-10-28T19:02:17+08:00　
> One thing I wil test with a small dummy list: two contacts sharing a company number with one marked DNC. Does the other copy stay in the call queue and what happens if you import the list again?
>
> JustCall’s docs flag the first case when duplicate contacts are enabled for CSV uploads. I'd ask vendors to show how they handle DNC across client lists before signing and what the full seat and calling costs are without adding a separate CRM.

---

> **SCS-AI**（1 分） · 2026-10-28T21:43:02+08:00　
> The thing that jumps out: you evaluated the last tool on a feature checklist and still got burned, so the checklist isn't the real filter. Every vendor will say yes to every line on your list. Those questions are good, but they're the second pass, not the first.
>
> First pass is compliance, because that's the part a nice UI can't fix. You're EU outbound, so parallel/predictive dialing is mostly off the table, recording is consent-gated, and DNC has to work per-list and survive a re-import. A big chunk of the market is built for US calling where all three of those are loose, and they bolt the EU settings on afterward and it shows. So I'd eliminate on those three before I even look at the autodialer or the reporting. It shrinks the list fast and saves you the weeks you just spent being someone's beta tester.
>
> Second, you can't read a dialer off a demo. Trial it with one real client list and do the three things you do a hundred times a day: import a messy list with direct and company numbers mixed, work it, mark a few DNC and not-interested, then re-import that same list and confirm the DNC ones never ring and the shared company number behaves how you expect. Someone upthread said run it on one real list and they're right, that single loop tells you more than the whole feature page.
>
> And the tell you already described without naming it: if you're three days into a trial and already writing the vendor feature requests to make it usable, you're their product manager, not their customer. A tool that actually fits won't need you to explain per-list DNC to it. That unpaid-PM feeling is the review score.
>
> On the numbers, decoupling the dialer from the number supply is usually the move. A lot of tools let you bring a UK or US number through your own SIP or Twilio instead of reselling you one, which also sidesteps the you-need-a-local-entity nonsense. Bit of setup, but you stop being hostage to whatever one vendor happens to carry in each country.

## 导航

- 项目页：—（本条不是项目，按设计不建实体页）
- 渠道页：[[50-渠道/reddit]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
