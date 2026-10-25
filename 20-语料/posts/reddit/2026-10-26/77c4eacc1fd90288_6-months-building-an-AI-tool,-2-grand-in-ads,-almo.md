---
type: "corpus"
item_id: "77c4eacc1fd90288"
title: "6 months building an AI tool, 2 grand in ads, almost no paying users. We turned off ads and things finally started working."
source: "reddit"
source_name: "Reddit 独立开发版块"
url: "https://www.reddit.com/r/microsaas/comments/1x6pg96/6_months_building_an_ai_tool_2_grand_in_ads/"
author: "kkurtzz"
published_at: "2026-10-15T23:55:46+08:00"
captured_at: "2026-10-26T00:20:27+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-10-26"
pub_day: "2026-10-15"
tags:
  - 语料
  - reddit
  - r/microsaas
metrics: {"score": 6, "comments": 19, "upvote_ratio": 0.875}
comments_count: 14
comments_total: 19
discovered_via: "reddit:14d+settle10"
---

# 6 months building an AI tool, 2 grand in ads, almost no paying users. We turned off ads and things finally started working.

> [!info] 一句话导读
> I've spent the last six months working on an AI tool that redesigns existing PowerPoint presentations. After a lot of building, testing, and trying pretty much …

> [!meta]- 语料信息（点开展开）
> 来源：Reddit 独立开发版块（post）
> 原帖：<https://www.reddit.com/r/microsaas/comments/1x6pg96/6_months_building_an_ai_tool_2_grand_in_ads/>
> 指标：得分=6 · 评论=19 · 赞踩比=0.875
> 作者：kkurtzz　|　发布：2026-10-15T23:55:46+08:00
> 项目链接：—
> 采集：2026-10-26T00:20:27+08:00　|　id：`77c4eacc1fd90288`

## 正文

I've spent the last six months working on an AI tool that redesigns existing PowerPoint presentations. After a lot of building, testing, and trying pretty much everything in the playbook to get customers, we're finally seeing some traction.

The numbers are still small (okay, very small), but looking back it's interesting how wrong we were about almost everything.

**First mistake: building for the customer we wanted**

Our original plan was personalized sales presentations. Upload your branding, point the tool at a prospect's website, get a tailored pitch deck.

Everything from our homepage to onboarding and pricing was written for sales reps.

We spent about $2,000 on Meta and Google ads. Around 5% of clicks turned into free signups, but as far as we can tell, not a single one became a paying customer.

In five months, we got four mid-tier subscriptions. All four canceled before their second payment.

Not exactly the recurring revenue machine we'd imagined...

**Second mistake: pricing for the wrong behavior**

Everyone who paid had spent 1.5 to 2 hours inside the product first. People who made one presentation and left never paid.

And why would they? Our free plan let them finish their deck and export it with a small badge. They'd already gotten what they came for.

We had a $12 badge-removal option buried in Stripe that nobody ever used. In one 30-day period, we recorded exactly ONE checkout click.

We'd built subscriptions for people who needed presentations regularly, but most users only needed to finish one.

**So we turned off ads and bet on organic**

At some point, paying to acquire users who weren't paying us stopped making sense.

We decided we'd either figure out organic growth or move on.

We'd read plenty about optimizing for LLMs, so we went all in on AEO/GEO, or whatever we're calling it this week.

Schema markup, structured FAQ content, feature-specific landing pages, direct answers to questions people might ask an assistant, internal linking, Bing indexing. Basically every recommendation we could find.

We weren't convinced it would work, but at least it didn't require another $2,000 in ads.

Then something interesting happened.

**ChatGPT started sending us users**

We'd created a few pages about redesigning existing PowerPoints, a feature we'd barely emphasized. Google search volume for that problem was practically nonexistent.

But those pages started showing up in ChatGPT answers.

In one 30-day window:

* ChatGPT sent 53 visitors. About 35 signed up.
* Google organic sent 80 visitors. Zero signed up, mostly brand traffic and an unrelated free calculator.

A 66% signup rate from ChatGPT referrals. Pretty crazy from someone who's spent a long time in SaaS marketing.

We don't know which optimizations helped, but we'd stumbled into demand our keyword research hadn't revealed.

So we doubled down on those pages, expanded the answers around that use case, and watched the traffic keep growing.

**And it turned out we'd been targeting the wrong people entirely**

Our actual users weren't sales reps. They were students, academics, consultants, and freelancers making class presentations, thesis defenses, and internal reviews.

They came from 49 countries in two months. Only about 1 in 8 was American.

The median uploaded deck was 20 slides, and 23% of slides had more than 80 words. These were dense presentations people needed to make look better, not personalized sales pitches.

Our entire website was talking to somebody else.

We rewrote the messaging, made the product multilingual, and rebuilt onboarding probably a dozen times, with dedicated paths for different types of users.

We added a $13 one-time purchase offered when someone hits the free limit, instead of requiring a subscription for one deck.

We also built an integration directly into ChatGPT, letting users create and redesign presentations without leaving the conversation.

**Here's what's happened since**

Weekly signups went from 23 in mid-September to 46, then 63.

Total accounts grew from 348 to 464 in two weeks.

Activation was around 20% over the summer. Our overall activation rate has since climbed from 40% to 47%.

Paid conversion went from 0.2% to 0.9%.

Still tiny, but we'd had eight paying events in five months, then six in two weeks, with no advertising spend.

Two bought the $13 one-time option. One user opened our $9/month checkout, closed it, and bought the $13 option 24 seconds later.

That one interaction told us a lot.

But subscriptions weren't dead. One business user built nine decks in an evening, bought the $9 plan, and upgraded to $29 eighteen minutes later.

Same product, very different customers.

**What I'd tell myself six months ago**

* Watch who's actually showing up, not just who you think should.
* Don't assume low Google search volume means low demand. People are searching inside AI assistants now.
* If your free plan finishes the job, think about when and why someone would pay.
* One-time purchases aren't inherently worse than subscriptions, especially for a global audience.
* Actually watch what users do. Four canceled subscriptions and one person switching checkouts taught us more than our original assumptions.

**Where we're at now**

I'm definitely not claiming we've cracked growth. A 0.9% paid conversion rate still leaves a LOT to figure out, and six paying events in two weeks isn't proof of product-market fit.

But we're finally seeing signs that this might work, right when we were pretty close to giving up.

And despite all the talk about the coming "SaaS-pocalypse," it's made me more optimistic about niche software. There still seem to be plenty of specific problems people will pay to solve, especially when the solution fits naturally into tools they're already using.

Still figuring out the next chapter, but hopefully this is useful to someone else who's six months into building something and wondering why nobody's paying for it yet.

For context the product is Pitchboost, feel free to ask any questions about our story!

## 评论（14/19）

> **ProfitKiteer**（1 分） · 2026-10-16T00:02:43+08:00　
> Interesting, how much of that new traffic is from the ChatGPT plugin vs. ChatGPT recommending you in conversations? Good thought to get into their marketplace early, I wonder if that boosts product visibility with the LLM and makes it even more likely to recommend you too.

---

> **kkurtzz**（1 分） · 2026-10-16T00:21:25+08:00　
> It's about 50/50, no evidence to support that we're getting referred more often yet, but one interesting thing we're going to try is running ChatGPT ads that send people to the plugin's deep link in the ChatGPT marketplace... I haven't seen anyone else doing this yet.

---

> **kkurtzz**（1 分） · 2026-10-16T00:36:10+08:00　
> Exactly, from the decks they generated - super helpful as a data point!

---

> **Training-Duck-3251**（1 分） · 2026-10-16T01:22:47+08:00　
> the free plan is what gets me. you let them export the entire finished deck, badge and all, and then act surprised nobody pulls out a card? a small badge on slide 7 is not a paywall, a sales rep will 100% walk into a real client meeting with your watermark on it and not lose one second of sleep. your product was already done the moment they hit export. of course 4 people subscribed and bailed before the second payment, they probably only paid out of guilt after sitting in there for two hours.
>
> and meta ads for a powerpoint redesign tool aimed at sales reps. i dont know one sales rep who's scrolling instagram and suddenly decides his slides are the reason he's missing quota. that 2 grand was a donation. google ads for this isnt much better, nobody googles "redesign my pitch deck" unless they already have a deck and a deadline.
>
> turning off the ads was the only correct decision in the whole six months and you basically stumbled into it.

---

> **kkurtzz**（1 分） · 2026-10-16T01:27:42+08:00　
> ¯\\\_(ツ)\_/¯

---

> **Khavel_dev**（1 分） · 2026-10-16T02:25:59+08:00　
> $2k on ads for a dev tool is almost always money burned tbh. Devs are basically immune to ads - we all run blockers and skip sponsored results reflexively. The ones who do click tend to be tire kickers, not buyers.
>
> The AEO bet is smarter but it takes months to compound. The thing that actually moved the needle for tools I've worked on is writing about the specific problem you solve, not the tool itself. Like if your tool fixes X, write the best guide on solving X manually, then mention your tool does it automatically. People searching for the problem find you, and the AI models pick up the same content for recommendations.

---

> **draftsbyfatima**（1 分） · 2026-10-16T04:37:57+08:00　
> When you present your products as a pain point of your customers, it really gets noticed, and it can be improved for future use by using your experience as to how they used your product through pages and putting info you get through your past users' data and ChatGPT bringing you traffic was interesting

---

> **Agitated_Offer_4343**（1 分） · 2026-10-16T09:43:25+08:00　
> the chatgpt number isnt about chatgpt. someone who types their problem into an assistant has already said it in their own words, so a page answering that exact sentence converts. google sent you brand searches and a calculator, people who werent shopping.
>
> i wouldnt hunt for more of those with a keyword tool. mine where people describe the problem unprompted, support threads, sales calls, reddit, and write against those sentences. volume's too low for tools to surface, which is why it works

---

> **Anshkoshmod**（1 分） · 2026-10-16T11:57:01+08:00　
> Four early cancellations signal users bought for a single presentation job, not ongoing utility. Ask active users which specific deck asset they re-export monthly, then gate that recurring format so you only acquire users with repeatable workflow needs.

---

> **Maleficent-Fact8963**（1 分） · 2026-10-16T14:24:52+08:00　
> ads are a multiplier, not a spark. if nothing converts organically, paid just buys the same silence at scale. turning them off forced the question that actually mattered - who wants this enough to find it on their own

---

> **marcostfcastro**（1 分） · 2026-10-17T16:37:24+08:00　
> Hey, the person choosing a one-time purchase and the business user upgrading after creating several decks tell two quite different stories about the same product.
>
> I’d keep those groups separate in your next round of interviews. For the occasional user, the trigger might be one deadline and the desired outcome a finished presentation. For the repeat user, it might be an ongoing workflow with a very different cost of doing it manually.
>
> That could change your positioning and packaging more than another feature. It would also help distinguish “people won’t subscribe” from “this particular group doesn’t need the product repeatedly.”
>
> I recently wrote about collecting behaviour and commitment evidence before changing the roadmap. It uses SportsTech examples, but your post illustrates the same decision:
> [https://www.buildingsportstech.com/p/most-sportstech-startups-dont-need](https://www.buildingsportstech.com/p/most-sportstech-startups-dont-need)

---

> **geoffreybyers**（1 分） · 2026-10-18T04:12:28+08:00　
> The numbers reveal a brutal reality about B2B discovery today. A sixty six percent signup rate from ChatGPT versus zero from Google organic shows search is no longer the primary mechanism for finding niche tools. Traditional SEO metrics have become a leading indicator of failure. The demand is real, but it lives in the conversation, not the keyword.

---

> **wothotturd1**（1 分） · 2026-10-18T04:52:18+08:00　
> the pivot from sales reps to students and academics is interesting but those are very different willingness-to-pay segments. whats your plan for keeping the $13 price sustainable when your heaviest users are probably students with zero budget?

---

> **Easy-Purple-1659**（1 分） · 2026-10-19T12:48:41+08:00　
> The $2k wasn't wasted on ads, it was spent without looking at what the category already runs.
>
> Before writing another line of copy, pull what competitors are actually running: Meta Ad Library, Google Ads Transparency Center, TikTok's library. You'll usually find the whole niche leaning on the same three angles, and the one that keeps getting repeated longest is the one working. If your deck tool never showed a before/after next to a real client deck, that's the gap, not Instagram's audience.
>
> Two things I'd check for this tool: whether anyone in the category runs paid ads at all (plenty of B2B deck tools don't, which tells you something), and which creative format they keep alive past 30 days.
>
> Full disclosure, I built adextract, an MCP server that lets Claude query those four libraries (Meta, Google, TikTok, LinkedIn) and get structured results back instead of clicking through each one. Only relevant if you ever decide ads deserve another test, and the same research is doable by hand in about an hour.
>
> When you did run them, did you check what competitors in the deck space were running, or was it all built from scratch?

## 导航

- 项目页：—（本条不是项目，按设计不建实体页）
- 渠道页：[[50-渠道/reddit]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
