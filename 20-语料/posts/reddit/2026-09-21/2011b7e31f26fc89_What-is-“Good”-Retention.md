---
type: "corpus"
item_id: "2011b7e31f26fc89"
title: "What is “Good” Retention?"
source: "reddit"
source_name: "Reddit 独立开发版块"
url: "https://www.reddit.com/r/indiehackers/comments/1uj1how/what_is_good_retention/"
author: "kev_habits"
published_at: "2026-06-30T02:58:56+08:00"
captured_at: "2026-09-21T03:03:02+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-21"
pub_day: "2026-06-30"
tags:
  - 语料
  - reddit
  - r/indiehackers
  - Technical Question
metrics: {"score": 3, "comments": 24, "upvote_ratio": 1}
comments_count: 32
comments_total: 32
discovered_via: "reddit:113d+settle3"
---

# What is “Good” Retention?

> [!info] 一句话导读
> Hi, I posted about what users count on here before and I wasn’t sure if I was actually tracking properly for gamified lives. Many people commented saying to foc…

> [!meta]- 语料信息（点开展开）
> 来源：Reddit 独立开发版块（post）
> 原帖：<https://www.reddit.com/r/indiehackers/comments/1uj1how/what_is_good_retention/>
> 指标：得分=3 · 评论=24 · 赞踩比=1
> 作者：kev_habits　|　发布：2026-06-30T02:58:56+08:00
> 项目链接：—
> 采集：2026-09-21T03:03:02+08:00　|　id：`2011b7e31f26fc89`

## 正文

Hi, I posted about what users count on here before and I wasn’t sure if I was actually tracking properly for gamified lives. Many people commented saying to focus on retention instead…

So here’s the question how do I know what retention number to target, and how should I be quantifying this?

For context:

I’m currently on day 15 post launch
32 users (goal is 100 by day 30)
16 registered users (made an apple sign in act)
16 unregistered users/guest users (made a guest act, hit the core feature)

Retention stats:
(D1 & D7 stats are active users not just coming back)

Registered users: D1: 25% D7: 36.4% stickiness: 31.6% (DAU/MAU)

Guest Users: D1: 14.3% D7: 22.2%, guest came back day 7: 10(out of 16, 62.5%)

Averaging 2 new users per day 50/50 signed in or guest.

No conversions yet which I’m fine with because I’m targeting a 1% conversion for the start so hopefully 1 paid user at 100 users.

I’d love to know what my goal retention should be and If you guys have any tips to improve retention.

## 评论（32/32）

> **Hefty-Door-5821**（1 分） · 2026-06-30T03:02:40+08:00　
> your retention for registered users is actually pretty good for day 15, d7 at 36% is not bad at all for a new app. most people would be happy with that in the first month
>
> the guest numbers are a bit lower but 10 out of 16 coming back on day 7 is decent, maybe think about why those 6 didn't return. is there something in the core feature that gets boring quick? that's where i'd dig in
>
> for goals i always heard 20-30% d1 and 10-20% d7 is like baseline for early stage, you're already above that so just keep doing what you're doing and maybe add some small thing that pulls people back in day 2 or 3

---

> **kev_habits**（1 分） · 2026-06-30T03:07:30+08:00　
> Thanks for the feedback! Yeah I am a bit confused on the discrepancy between registered and non registered users i think that digging into that may be helpful as you suggested. Yeah for day 2,3,4 etc I’ve been trying to figure out how I can incentivize the user to get back into the app but haven’t figured out what may help there

---

> **RobertMathe89**（1 分） · 2026-06-30T03:43:59+08:00　
> Good retention depends heavily on your product type, but one thing most SaaS founders miss is separating "real churn" from "payment churn."
>
> You can have solid D7/D30 engagement and still lose users silently to expired cards or failed renewals. That shows up as churn in your analytics but it's actually a billing problem, not a product problem.
>
> For a gamified app, focus on habit loops first. But once you have paid subs, track involuntary churn separately. I run a small tool that handles failed payment recovery, and the number of founders who don't realize how much this leaks is wild.
>
> For early stage, I'd say D1 >40%, D7 >20%, D30 >10% is a decent starting target. But benchmarks vary a lot by category.

---

> **andrew_zol**（1 分） · 2026-06-30T06:18:33+08:00　
> I think it also massively depends on the niche/app type. There are products that are supposed to be used sporadically (e.g. when use has some sporadic problem to solve and he remembers that you have a service for that), other kids of applications require every day engagement. Also I think it's to early to make serious conclusions until you have more users and your statistics will be more representative

---

> **kev_habits**（1 分） · 2026-06-30T06:23:08+08:00　
> I appreciate the feedback, I’m in the habit tracking area so obviously there’s a heavy churn from users themselves just not being motivated enough to even do what they want to do. However I’m trying to see how I can help more users stay on track so retention is basically my most important metric

---

> **andrew_zol**（1 分） · 2026-06-30T06:47:47+08:00　
> Is that a mobile app or website?

---

> **EngineerConfident874**（1 分） · 2026-06-30T06:54:10+08:00　
> Cool idea. I’d want to know what the app does differently after the first session, meaning what makes me come back tomorrow or next week.

---

> **kev_habits**（1 分） · 2026-06-30T06:54:31+08:00　
> It’s a mobile app

---

> **kev_habits**（1 分） · 2026-06-30T06:55:31+08:00　
> Thanks for the feedback, yeah I’ve been trying my best to ensure onboarding is spot on so users feel the value immediately instead of having to use the app for a bit to understand the value

---

> **EngineerConfident874**（1 分） · 2026-06-30T07:01:25+08:00　
> ya i hear that...

---

> **andrew_zol**（1 分） · 2026-06-30T07:07:05+08:00　
> well, then you always have a push notification option. I don't know what percentage of users are disabling them for most of the apps (like I do), but at least some part of users will allow sending them push notifications. Also you could limit some features until user is registered so user will be motivated to register.

---

> **Plan_Steadily**（1 分） · 2026-06-30T07:45:49+08:00　
> Benchmarks don’t matter yet. Your user count is still too small for the numbers to be stable, so don’t optimize around them. What matters is whether each new group of users comes back more than the last. Pay attention to what your returning users actually do in the app before they leave and what pulls them back. That is your real signal.
>
> Spend more time talking to the people who returned than looking at dashboards. They will tell you what to fix next.

---

> **NetOk7015**（1 分） · 2026-06-30T08:03:34+08:00　
> At day 15 with 32 users, I'd obsess less over industry benchmark numbers and more over whether the same person comes back for the same reason twice.
>
> Your registered D7 (36%) vs guest D7 (22%) is actually useful signal: signed-in users see enough value to return without you nagging. That's worth more than hitting a magic 40% benchmark from a blog post written for B2B SaaS with sales teams.
>
> For gamified apps, I track "did they complete the core loop twice in seven days" more than raw DAU. Guests who hit the feature once and bounced might never convert anyway; registered users who return on D3 but churn by D10 usually mean the novelty wore off before habit formed.
>
> Before chasing retention tactics, I'd pick five registered users who came back on D2 and ask what almost made them not return.
>
> What's the one action in your app that correlates most with someone coming back the next day?

---

> **BennHere**（1 分） · 2026-06-30T09:02:30+08:00　
> I think you're asking the right question, but I'd be careful about comparing your numbers to generic benchmarks with only 32 users. At this stage, I'd focus more on *why* people come back than whether your D7 is 20% or 40%.
>
> One thing I'd look at is whether retained users have something in common. Did they complete onboarding? Create an account? Finish a specific action? Finding that "aha moment" will probably improve retention more than chasing an industry average.

---

> **Active_Marsupial_736**（1 分） · 2026-06-30T09:09:57+08:00　
> I’m working through a similar question myself, so this thread is helpful.
>
>   One thing I’m still unsure about is where the focus should be at this stage. With a small number of users, is it better to focus on improving the first-session experience, or on finding the specific action that makes someone come back the next day?
>
>   For habit-style apps especially, I wonder if D1/D7 is less useful on its own unless you know what behavior happened before the return. Curious how others think about this.

---

> **Silent-Forest-8392**（1 分） · 2026-06-30T10:28:16+08:00　
> honestly it completely depends on your industry, but aiming for net negative churn is usually the real gold standard.

---

> **keulevoras**（1 分） · 2026-06-30T13:17:32+08:00　
> what does your app do?

---

> **paulretryfix**（1 分） · 2026-06-30T13:49:35+08:00　
> Sounds like you well on your way, congrats keep going

---

> **Constant_Border_8994**（1 分） · 2026-06-30T23:47:08+08:00　
> With only 16 users in each group, I wouldn’t worry too much about hitting a specific benchmark yet. One or two people can completely change those percentages.
>
> I’d focus more on the actual loop: did they reach the main feature, did they come back and use it again, and what made them return?
>
> You mentioned that 10 of the 16 guests came back by day 7. I’d honestly try to speak to those people first. Their reasons for returning will probably be more useful right now than any industry benchmark.

---

> **Kintzappltech**（1 分） · 2026-07-01T08:39:38+08:00　
> One thing that might help people give better advice: what’s the core habit you’re trying to build? Is this something users should open daily, weekly, or only when they have a specific need? The “right” retention target depends a lot on the expected usage frequency.

---

> **TryWordPolish**（1 分） · 2026-07-01T14:20:51+08:00　
> My renention is D1: 44%, D7: 20%, D30: 12%, idk if that helps. I've heard 40/20/10 be referenced as a goal, but to me it still feels low. Users are flakey though, so maybe 10% of all users sticking around long term is all we can hope for. Cheers for asking the question, because I'm curious too.

---

> **MuyJasonn**（1 分） · 2026-07-01T17:22:17+08:00　
> I'd be careful about reading too much into the numbers with only 32 users. At this stage I'd spend more time talking to every user than optimizing retention metrics.
> I'd focus on:
> Why did people come?
> Did they reach the core value quickly?
> Why didn't they come back?
> Once you have 100–200 users, the retention numbers become much more meaningful. Right now, even one or two users can swing your percentages a lot.

---

> **Afraid-Flatworm-6762**（1 分） · 2026-07-02T02:53:56+08:00　
> i think your numbers are interesting, but with 32 users i would be careful about judging it like a real benchmark yet.
>
> one or two users can change the percentages a lot at this stage, so the better question might be: who came back, what did they do, and why did they return? especially for a habit app, raw d1/d7 can be a bit misleading if people are coming back but not really completing the core habit loop.
>
> i’d probably focus less on “what is good retention” and more on finding the action that predicts retention. did they create an account, finish onboarding, complete the main habit once, get a reminder, invite someone, whatever it is. if returning users all did one same thing early, thats the thing to improve.
>
> your registered d7 doesnt look bad at all tho. i’d just talk to a few of those users before changing too much based on the dashboard.

---

> **VariousHour7390**（1 分） · 2026-07-02T12:59:37+08:00　
> For just 32 users, I'd focus more on qualitative feedback than benchmark numbers. If people are coming back and finding value, you're on the right track. Talk to your active users—they'll tell you what's worth improving.

---

> **SharpZookeepergame36**（1 分） · 2026-07-03T08:33:33+08:00　
> 32 users after 15 days is still noise. You need 50-100 active users minimum before the numbers tell you anything real.
>
> That said, here's what matters for any planner/habit developer: day 1 to day 7 retention. If half your users open it twice in week one, that's solid. If a quarter do, you might have a design problem.
>
> Simple Tracking I look at: # of users who signed up this week, what percent opened it three or more times? That's your real signal. when initial excitement fades after 2-3 weeks is the real test.
>
> Skip fancy analysis for now. Just watch: do people come back after that first dopamine hit? If yes, you're learning something. If no, ask three users why they stopped.
>
> Target 40-50 percent day 7 retention once you have enough data. Anything above that is good for this category.

---

> **camp-glow-012**（1 分） · 2026-07-04T09:57:12+08:00　
> At 32 users the percentages are really noisy (each user is \~3%), so I'd watch the shape of the curve, not a target number yet. "Good" retention isn't a magic number, it's a curve that flattens: if D7 to D30 stops declining and holds, you've got a core that found value, and that flattening is the real PMF signal. A curve trending to zero means no stickiness no matter how high D1 is.
>
> Two things: measure retention around your core action (did they do the thing that equals value), not just app-opens. And that 62.5% of guests coming back by D7 is a genuinely good sign, I'd dig into what those specific users did differently and lean into it.

---

> **_s7c_**（1 分） · 2026-07-04T16:43:21+08:00　
> By understanding the job to be done that the user needs and improving the way you solve it. Listen to their feedback and do everything to find product-market fit...
>
> This is one way of looking at this, whether it is a good or bad idea, it depends on the context, which is a mystery...

---

> **Wooden-Prune-9956**（1 分） · 2026-07-04T22:36:39+08:00　
> *"Good"* *depends* *on* *how* *often* *the* *underlying* *need* *occurs,* *so* *cross-category* *benchmarks* *mislead* *more* *than* *they* *help.* *A* *meditation* *app* *can* *expect* *daily* *curves;* *an* *invoicing* *tool* *is* *monthly* *at* *best* *—* *judging* *either* *against* *social-app* *numbers* *will* *just* *depress* *you.* *The* *shape* *matters* *more* *than* *the* *number:* *plot* *cohort* *curves* *and* *look* *for* *where* *they* *flatten.* *A* *curve* *that* *flattens* *at* *15%* *and* *holds* *for* *months* *is* *a* *real* *business;* *a* *40%* *D7* *that* *keeps* *sliding* *toward* *zero* *is* *not.* *Grow* *the* *flat* *part.*

---

> **champdeal**（1 分） · 2026-07-05T08:15:17+08:00　
> With only 32 users, I’d be careful about judging the percentages too much. I’d focus more on what returning users did differently — did they hit the core value faster, complete onboarding, or come back for the same reason twice?

---

> **Quiet_Acadia2500**（1 分） · 2026-07-06T02:54:37+08:00　
> How are you tracking everything? I just have a free website I just made and have only been seeing how many people are online at that moment and total number of visitors. Oh, and bounce rate.

---

> **ZhihaoPinknockout**（1 分） · 2026-07-07T13:31:55+08:00　
> At 15 days in, I’d honestly take the percentages with a grain of salt. The sample is still tiny, so one or two people can make the numbers look way better or worse.

---

> **Fit-Radio6598**（1 分） · 2026-07-10T05:45:59+08:00　
> try emailing the churned users to get feedback. If you can, offer a small incentive like a $5 amazon gift card for them filling out a survey

## 导航

- 项目页：—（本条不是项目，按设计不建实体页）
- 渠道页：[[50-渠道/reddit]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
