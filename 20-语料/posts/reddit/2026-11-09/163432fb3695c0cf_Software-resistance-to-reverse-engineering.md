---
type: "corpus"
item_id: "163432fb3695c0cf"
title: "Software resistance to reverse engineering"
source: "reddit"
source_name: "Reddit 独立开发版块"
url: "https://www.reddit.com/r/SaaS/comments/1xj0bhc/software_resistance_to_reverse_engineering/"
author: "HistoricalBeat848"
published_at: "2026-10-30T07:55:17+08:00"
captured_at: "2026-11-09T09:41:07+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-11-09"
pub_day: "2026-10-30"
tags:
  - 语料
  - reddit
  - r/SaaS
metrics: {"score": 18, "comments": 39, "upvote_ratio": 0.8461538461538461}
comments_count: 35
comments_total: 39
discovered_via: "reddit:14d+settle10"
---

# Software resistance to reverse engineering

> [!info] 一句话导读
> I wanted to ask you guys what do you think will make software resistant to AI reverse engineering, and AI in general ?

> [!meta]- 语料信息（点开展开）
> 来源：Reddit 独立开发版块（post）
> 原帖：<https://www.reddit.com/r/SaaS/comments/1xj0bhc/software_resistance_to_reverse_engineering/>
> 指标：得分=18 · 评论=39 · 赞踩比=0.8461538461538461
> 作者：HistoricalBeat848　|　发布：2026-10-30T07:55:17+08:00
> 项目链接：—
> 采集：2026-11-09T09:41:07+08:00　|　id：`163432fb3695c0cf`

## 正文

Hey,

I wanted to ask you guys what do you think will make software resistant to AI reverse engineering, and AI in general ?

What I mean is the goal is obviously to provide value to users; if something is too accessible it has no value anymore hence few will pay for it (some exceptions?).

Do you think that SaaS/Software with mainly backend processes are the way to go (basically don't give out too much info on the front of the app if possible) ?

Working in some more traditional industries, I noticed some things always stayed like buying from wholesalers being less expensive than buying a small amount for a manufacturer.

What do you think still has value nowadays in software ? (or may still have in the future)

## 评论（35/39）

> **CaptainBloodEz**（6 分） · 2026-10-30T08:02:20+08:00　
> Ive always said web is the future. If you can make it an online only solution, you can hide all the important stuff behind the scenes. Regardless of what screens an AI could see, it won’t know exactly what you are truly doing to make things happen.

---

> **ThomasBuildLab**（17 分） · 2026-10-30T08:06:40+08:00　
> I think you're asking the right question, but perhaps looking at it from the wrong angle.
>
> Trying to make a SaaS resistant to AI reverse engineering might be counterproductive. It's a bit like trying to build a better paper road map just as GPS is becoming mainstream.
>
> AI is making software increasingly easy to reproduce, but more importantly, it's changing how people interact with software.
>
> Instead of asking how to protect existing features, I'd ask: what will users still need when AI agents can perform most of these tasks directly?
>
> Reliable data, persistent context, trust, continuity, and access to real-world systems may become far more valuable than the software interface itself.
>
> Keeping your logic on the backend can protect your code, but it won't necessarily protect your business.
>
> The opportunity may not be to build a SaaS that's harder to copy, but to build something that remains useful when the traditional SaaS interface is no longer necessary.

---

> **HistoricalBeat848**（1 分） · 2026-10-30T08:18:59+08:00　
> Thanks for the perspective. But this raises another question for me: why build a SaaS if it can eventually be replicated?
>
> Open source is one possibility: people either self-host it or pay you to host and maintain it. But if the value ultimately boils down to who can host it at the lowest price, won't we end up with a race to the bottom? A bit like freelance web development, where you can eventually get a website built for $10 (for free or for experience now maybe? haha).
>
> Also I agree that reliable data, trust, integrations, and access to real-world systems will remain valuable. But aren't those things also potentially replicable, at least to some extent?
>
> I'm trying to understand where sustainable competitive advantages in software businesses will come from. Not simply what will remain technically possible to build.
>
> Thanks man

---

> **HistoricalBeat848**（1 分） · 2026-10-30T08:27:10+08:00　
> Yes, there is no doubt that exposing your code on the frontend is becoming more dangerous (AI makes reverse engineering increasingly accessible). But people can also replicate your product's behaviour by observing and imitating it.
>
> If the real moats become proprietary data, distribution, and established networks, won't this give large companies an even greater advantage and reinforce monopolies?
>
> Another question: what about using proprietary LLM tools during development? Suppose Claude Code helps you debug a very specific production issue through hours of testing and experimentation. Could that experience eventually benefit other developers using the same models? In a way, are we indirectly giving away some of our technical know-how?
>
> Should we be concerned about using proprietary LLMs for commercial development, or am I overthinking this?

---

> **CaptainBloodEz**（2 分） · 2026-10-30T08:31:55+08:00　
> I think you are far overthinking this. If you want to compete with the billion dollar industries… then yeah. Worry about all of this. But if you’re only trying to compete in the multi million dollar industries… you’ll be fine. lol people imitating something genuinely useful does not mean it is as good and these people will continue to struggle to convince others to use the more inferior version of something. There are many cases where you can build something where an AI will struggle to figure out EXACTLY what you are doing on the backend.

---

> **HistoricalBeat848**（1 分） · 2026-10-30T08:35:10+08:00　
> Thanks for you perspective man. I spent some time in the blockchain ecosystem (Ethereum, etc.). I learned there that sometimes overthinking can actually help you anticipate and prevent problems. The ecosystem had become complex through years of iteration and some of those concerns were worth thinking about early on.
> 👍

---

> **PolyKernel**（3 分） · 2026-10-30T08:41:10+08:00　
> My products get cloned constantly and the clones rarely hurt, because what keeps people is months of their own data and setup sitting in my app. Moving to a copy means rebuilding all of that for a slightly cheaper price. Hiding logic in the backend helps a little, but whatever grows the longer someone uses you is what's hard to copy

---

> **FitOpinion4049**（3 分） · 2026-10-30T08:42:08+08:00　
> obfuscation only gets you so far, the real moat is in the data and integrations you build up over time. any half decent AI can replicate the code but it can't replicate years of customer usage patterns or the weird edge cases your system handles because of actual user feedback
>
> backend-first is definitely the smarter play right now, but even that won't matter if the value prop is just "we do CRUD operations faster". the stuff that sticks is when your software is so tangled into someone's workflow that ripping it out costs more than just paying you

---

> **HistoricalBeat848**（1 分） · 2026-10-30T08:49:13+08:00　
> Very nice, man. Good luck with your products!
>
> I guess building a great product and building an audience or reaching customers require different skill sets. But that's where there is a real advantage lies for someone who can do both.
>
> And this makes sense for products where users accumulate data or build workflows over time. But what about one-time-purchase products for example? Switching costs don't necessarily help you retain customers if they're unlikely to buy again anyway. Does success in those cases depend much more on distribution, reputation, and continuously reaching new customers?

---

> **Cleardeposits**（1 分） · 2026-10-30T09:21:44+08:00　
> AI has deep domain knowledge of workflows too so just being backend and being hidden may not be enough. I think there's little one can do to stop AI from reverse engineering. But if the question is will deterministic code continue to have a future over a stochastic model , I'd say yes and it depends on the use case. Routine predictable workflows will continue to be automated using deterministic code , albeit much cheaper to build maintain and price.

---

> **HistoricalBeat848**（1 分） · 2026-10-30T09:29:24+08:00　
> Thanks for your feedback. I think the bigger question is how software can remain economically sustainable. It sometimes feels like AI could undermine the very industry it's helping to create.
>
> If it eventually boils down to popularity (influencers, content marketing, etc.) and who has the largest audience selling essentially the same software, rather than actual engineering quality, it is possible that software engineering itself will lose much of its economic value.
>
> Take the automotive industry, for example. Cars can be imitated, but well-engineered vehicles still have real value. Engineering, performance, reliability, and safety remain important differentiators. What happens if well-engineered software doesn't have the same authority as well  ?
>
> Another thought: software engineers (particularly those building and deploying LLMs) are probably among the first to experience this disruption because they are close to software development workflows and understand other developers' needs. But there's little doubt that other industries will be affected too.
>
> I'd love to read some rigorous academic papers on this topic. I think understanding these dynamics offers very good insights into the broader economic and societal changes ahead.

---

> **Cleardeposits**（1 分） · 2026-10-30T09:48:17+08:00　
> yes product innovation over software engineering. code is getting cheap but knowing which problem matters , which edge cases break it and what users will actually trust is still hard.
>
> your car analogy works best where mistakes are expensive. in accounting for example a tool that's right 98% of the time is worth little because someone still has to check everything. people pay for predictability and someone standing behind the result , and that doesn’t get cheaper just because code does.

---

> **Small_Summer5817**（1 分） · 2026-10-30T10:55:12+08:00　
> This post is pretty non nonsensical. Sure you can make code harder to steal. anyone can copy your idea with AI

---

> **HistoricalBeat848**（1 分） · 2026-10-30T10:58:26+08:00　
> What do you mean by "non-nonsensical"? 😅
>
> I'm trying to start a discussion about how software businesses can remain sustainable in the AI age. I'd be interested to hear your perspective. Thanks for the feedback.

---

> **TopTippityTop**（2 分） · 2026-10-30T11:24:53+08:00　
> Invisible important logic buried in the backend. People will be able to clone the front end and visible functionality.
>
> For example.... A dating app. You can clone how it looks, but you won't how how the matching algorithm works. That's the secret sauce.

---

> **HistoricalBeat848**（1 分） · 2026-10-30T11:29:21+08:00　
> I'm not too much into dating apps but very nice example. Thanks for the feedback 👌👌
> It's true that dating apps algorithms are complete black boxes.

---

> **Low_Bridge_4413**（2 分） · 2026-10-30T11:36:26+08:00　
> I’d separate “can someone copy the product?” from “can they make customers bother switching?”
>
> A lot of SaaS moats are boring: historical records, approvals, permissions, trained workflows, integrations, billing history, habits. None of those are impossible to rebuild, but they create enough friction that a cheaper clone has to be much better, not just similar.
>
> Backend logic helps. But switching cost is usually where the business survives.

---

> **HumansAreWatching**（1 分） · 2026-10-30T12:53:33+08:00　
> Hiding logic in the backend is sensible hygiene, but it isn’t a moat. The code was never really the moat. AI just made that obvious.
>
> Your wholesaler example is the right one. Wholesalers don’t win on the product. They win on relationships, credit terms, logistics and being reliable. Software is the same. What’s hard to copy:
>
> * **Data that builds up over time.** Your customers’ history, their configurations, what your system has learned from them. A clone starts empty.
> * **Being embedded in how people work.** Integrations with their other systems, their processes built around yours, their staff trained on it. Switching is a project, not a download.
> * **Trust and accountability.** In enterprise and government work, customers buy the vendor as much as the software: security certifications, a track record, someone to ring when it breaks at 2 am. An AI can rebuild your features over a weekend. It can’t rebuild five years of passing security audits.
> * **Distribution.** Being the one they already know and already buy from.
>
> I’ve spent 20 years in enterprise software, and I can’t think of a deal we won because our code was clever. We won because they trusted us with their data and knew we’d still be around next year.
>
> If anything, AI makes this stronger. When anyone can build the features, buyers care more about who’s behind them.

---

> **Wild_Telephone5322**（1 分） · 2026-10-30T13:11:11+08:00　
> That’s a better way to frame it. The moat may end up being the data and trust around the product, not the interface itself

---

> **MoreHuman_ThanHuman**（2 分） · 2026-10-30T13:17:33+08:00　
> if it's easy to build it's not particularly valuable.

---

> **steroidmonkey66**（1 分） · 2026-10-30T13:46:25+08:00　
> Proprietary data is a major thing that cannot be replicated really. Scraping or selling that data that is not yours, is highly susceptible to lawsuits and most legitimate businesses would be very carful with that. So if you can market some data that you provider as proprietary and cannot be replicated that would be a huge selling point.

---

> **DevKokooo**（3 分） · 2026-10-30T14:10:03+08:00　
> The moat is now your brand and community, both builds trust in the product.

---

> **NeighborhoodPrize493**（2 分） · 2026-10-30T14:55:32+08:00　
> API

---

> **Strict-Prune-879**（1 分） · 2026-10-30T14:56:39+08:00　
> On parle de quoi? obtenir le frontend ok et après le backend ca sera pas possible. Et la duplication existait déja avec le clonage de site donc on peut se poser des questions mais viendra aussi le temps du juridique quand les petits malins qui font du reverse finiront devant les tribunaux

---

> **Previous_Fan_6248**（2 分） · 2026-10-30T15:15:18+08:00　
> distribution is only moat in Saas right now if u want moat u should focus on hardware AI startups it is what it is

---

> **sarkypoo**（2 分） · 2026-10-30T15:24:32+08:00　
> No download, streaming from the cloud with encryption. Give AI nothing to connect to so it can’t crawl or scrap.

---

> **Fabulous-Oven-3982**（1 分） · 2026-10-30T15:28:11+08:00　
> I doubt it. If that's the case, most tech companies would have shared their backend source code.

---

> **admiral_nivak**（1 分） · 2026-10-30T16:03:22+08:00　
> Anyone can make cornflakes or various other foods, people even do replicate them.  But a lot of people still buy Kelloggs because of branding and trust.

---

> **AutoModerator**（1 分） · 2026-10-30T18:11:05+08:00　
> Your comment was removed. Links in comments require to gain karma first in r/SaaS. Earn sub karma by commenting helpfully first.
>
> *I am a bot, and this action was performed automatically. Please [contact the moderators of this subreddit](/message/compose/?to=/r/SaaS) if you have any questions or concerns.*

---

> **AminoOxi**（1 分） · 2026-10-30T19:31:08+08:00　
> Resistance is futile.
>
> Only when mass unemployment hits 50% and more, the resistance starts.
>
> ![gif](giphy|6ozwFj8FgXGAo)

---

> **Few-Garlic2725**（1 分） · 2026-10-30T20:36:29+08:00　
> Alternative comment for same thread: AI makes features cheaper, but it doesn’t make buyer trust cheaper. Around Flatlogic, I’d look for value in places where customers need continuity: historical data, approvals, compliance trails, workflow memory, integrations, and accountability when something breaks. The question for a founder is not “can this be cloned?” It’s “what part of this workflow would a customer hate to revalidate with a clone?”

---

> **Dull-Passenger-9345**（1 分） · 2026-10-30T22:32:42+08:00　
> Open source software has already proven that the code itself is not what determines value. Upkeep, hosting difficulty, brand, customer service etc. these are the things that make software valuable.
>
> You can download an LLM that is as good as a frontier model from 6 months ago (give or take). You would think this would completely tank closed source expensive LLM’s in the enterprise category but it only served to increase demand.
>
> Long story short I wouldn’t worry about it.

---

> **ihmoguy**（3 分） · 2026-10-31T01:44:52+08:00　
> Just add some *forbidden* words to your frontend scripts so it trips any AI guardrails.
>
> https://nullpt.rs/fingerprinting-bioweapons

---

> **Ash_ArceusLegal**（2 分） · 2026-11-03T08:48:20+08:00　
> It may help to make what you handle for customers more obvious. For example, hosting and uptime or the quality of your support.
>
> Backend-heavy helps some, but accumulated data and the complexity of recreating and moving the workflow can keep customers onboard.
>
> Providing the ability to export their data is something clients want. But migrating it and customizing a new tool isn’t something many want to do.

---

> **HistoricalBeat848**（1 分） · 2026-11-03T08:52:27+08:00　
> Thanks for the feedback. It goes into the switching costs then. And in showing more expertise and seriousness for your first point as a way to differentiate?

## 导航

- 项目页：—（本条不是项目，按设计不建实体页）
- 渠道页：[[50-渠道/reddit]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
