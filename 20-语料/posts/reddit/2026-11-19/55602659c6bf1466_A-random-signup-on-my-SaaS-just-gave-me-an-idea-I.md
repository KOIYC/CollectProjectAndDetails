---
type: "corpus"
item_id: "55602659c6bf1466"
title: "A random signup on my SaaS just gave me an idea I hadn't even considered"
source: "reddit"
source_name: "Reddit 独立开发版块"
url: "https://www.reddit.com/r/SideProject/comments/1xrex8x/a_random_signup_on_my_saas_just_gave_me_an_idea_i/"
author: "_ACTUALin"
published_at: "2026-11-09T09:32:50+08:00"
captured_at: "2026-11-19T09:44:24+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-11-19"
pub_day: "2026-11-09"
tags:
  - 语料
  - reddit
  - r/SideProject
metrics: {"score": 3, "comments": 11, "upvote_ratio": 0.6666666666666666}
comments_count: 11
comments_total: 11
discovered_via: "reddit:14d+settle10"
---

# A random signup on my SaaS just gave me an idea I hadn't even considered

> [!info] 一句话导读
> Noticed someone signed up using an AgentMail email address, which I'd never come across before. Got me curious about how people are starting to use AI agents to…

> [!meta]- 语料信息（点开展开）
> 来源：Reddit 独立开发版块（post）
> 原帖：<https://www.reddit.com/r/SideProject/comments/1xrex8x/a_random_signup_on_my_saas_just_gave_me_an_idea_i/>
> 指标：得分=3 · 评论=11 · 赞踩比=0.6666666666666666
> 作者：_ACTUALin　|　发布：2026-11-09T09:32:50+08:00
> 项目链接：—
> 采集：2026-11-19T09:44:24+08:00　|　id：`55602659c6bf1466`

## 正文

Noticed someone signed up using an AgentMail email address, which I'd never come across before. Got me curious about how people are starting to use AI agents to interact with different software.

Not long after, I received an email with some pretty detailed feedback from someone who'd been testing mine. Actual issues they'd encountered, specific examples and suggestions. Exactly the kind of feedback I've been hoping to get.

But then it got me thinking... if people are already using AI agents to interact with SaaS products, why the hell am I not making mine accessible to them directly?

Ended up going down the MCP and ChatGPT plugin rabbit hole, and now I'm seriously considering adding agent compatibility to the roadmap lol.

So a random signup turned into some great feedback and an even better idea. Huge thanks to the person who took the time to test everything!

Anyone else looking into making their software accessible to AI agents?

## 评论（11/11）

> **Informal_External_55**（1 分） · 2026-11-09T09:40:47+08:00　
> Do it! Depending on your product, I’d also consider building a CLI. Agents will thank you.

---

> **_ACTUALin**（0 分） · 2026-11-09T10:08:03+08:00　
> Oh damn, that's actually worth considering too. I'm already looking into MCP compatibility, but a CLI could open up some interesting possibilities for automated workflows. Appreciate the suggestion! huge

---

> **xkft**（0 分） · 2026-11-09T11:05:44+08:00　
> in the software startup community you need to have everything AI agent accessible, otherwise someone else will build a better product that is.
>
> I ran into the same thing because I hated google workspace for setting up emails on a bunch of domains. I built a super cheap platform for it, but as I was using it, it was clear that an agent can manage everything for me. so I pivoted to making it AI-friendly including setup and account creation

---

> **lobo-solitario**（1 分） · 2026-11-09T11:08:17+08:00　
> Congrats, you have seen the future of platforms.

---

> **samurai_with_sword**（1 分） · 2026-11-09T12:49:12+08:00　
> Yup, WebMCP or MCP for any new app is a no brainer. It can even help you keep your primary app feature lite. Keep basic robist features and off load complex feature to the MCP, MCP can use the basic features as building blocks to do something more complex.

---

> **Masselier_Cynthea**（2 分） · 2026-11-10T00:55:26+08:00　
> clean API documentation is honestly 90% of the battle for agent accessibility right now. if your endpoints are predictable and well-documented, agents can already chain actions together pretty easily without needing a custom integration

---

> **_ACTUALin**（1 分） · 2026-11-10T01:05:46+08:00　
> Yeah, that's a good point. I hadn't really considered how much good API documentation could help with agent accessibility. I'm still figuring out how far I want to take that integration, especially when it comes to permissions. Having agents prepare reports would be awesome, but reviewing and approving the results still needs to stay with the person responsible.

---

> **kumard3**（2 分） · 2026-11-10T02:41:52+08:00　
> On permissions, the API keys in the email API I build are scoped as resource:verb, so emails:read and emails:send are separate and the send route checks for its own scope. A key created by another key can't get more than its parent has. For your case that would mean something like reports:create on the agent's key, and approve as a separate scope that only a person's key holds.

---

> **_ACTUALin**（1 分） · 2026-11-10T03:02:18+08:00　
> Oh, I like that approach. Separating permissions like that makes a lot of sense, especially for anything that needs approval. I'd definitely want agents to be able to prepare and submit work for review without giving them the ability to sign off on it themselves. Appreciate the example!

---

> **_ACTUALin**（1 分） · 2026-11-10T03:56:01+08:00　
> Thank you, that's pretty much the direction I'm leaning towards i thiink. Keep the existing app focused on what it does well and give agents controlled access to those functions through MCP. I'm especially interested in seeing how far that can go without compromising permissions or the review process.

---

> **dellarb**（1 分） · 2026-11-12T19:53:24+08:00　
> For sure is great approach. I have several hermes agents i can reset state of to run UAT on my releases they pick up a lot! And always build in a full fruit management api so you can just hand off to agent to use app on your behalf - you are probably 90% there with normal app architecture for sure.

## 导航

- 项目页：—（本条不是项目，按设计不建实体页）
- 渠道页：[[50-渠道/reddit]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
