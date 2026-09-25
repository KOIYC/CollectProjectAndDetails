---
type: "corpus"
item_id: "03d05da97b0e59a4"
title: "Show HN: Radix – Visual UI for agentic programming"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49834964"
project_url: "https://radix-os.com/"
author: "0x1062"
published_at: "2026-09-24T18:35:20Z"
captured_at: "2026-09-25T13:42:25+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-25"
pub_day: "2026-09-24"
tags:
  - 语料
  - hn_show
  - author_0x1062
  - story_49834964
  - show_hn
metrics: {"points": 15, "comments": 17, "engagement_velocity": 15}
comments_count: 17
comments_total: 17
discovered_via: "hn:show_hn:3d"
---

# Show HN: Radix – Visual UI for agentic programming

> [!info] 一句话导读
> Hey HN, I'm Jordan from Radix.Radix is a UI tool for programming agents. You prompt your agent to generate a workspace for a task you're working on and get an i…

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49834964>
> 指标：点赞=15 · 评论=17 · engagement_velocity=15
> 作者：0x1062　|　发布：2026-09-24T18:35:20Z
> 项目链接：<https://radix-os.com/>
> 采集：2026-09-25T13:42:25+08:00　|　id：`03d05da97b0e59a4`

## 正文

Hey HN, I'm Jordan from Radix.Radix is a UI tool for programming agents. You prompt your agent to generate a workspace for a task you're working on and get an interactive widget that persists locally on disk.I built Radix because I always needed tools while I was writing code: tools to test little experiments, to play around with UI, to visualise results etc. Sometimes these would end up as python tools that read and plotted data, or separate React apps spun up just to test a single feature. Lately obviously I've been using Claude artifacts but these are quite limited.I wanted a system where it was easy to leave comments or adapt an artifact without having to give vague descriptions back to the agent, and where ideally I could actually shift away from a chat window as the main interface.I've got a pro version of Radix which I will launch soon. This current version is entirely free and is definitely a beta -- there will be rough edges!Note: There's no telemetry or data captured. Your messages run entirely through your own agent. I require a key but that's just to get an idea of how many people are using it. Everything is stored locally (the workspaces are actually just React apps which you can edit "artisanally" if you want).If you have any questions please reply here or email me hello@radix-os.comThank you!

## 评论（17/17）

> **kambli7** · 2026-09-24T18:38:22.000Z　
> What does the term agentic programming means over here?

---

> **Topfi** · 2026-09-24T19:20:14.000Z　
> Is this affiliated with WorkOS and the long going Radix UI component primitives maintained by them?

---

> **grenoire** · 2026-09-24T19:40:26.000Z　
> [flagged]

---

> **weego** · 2026-09-24T19:46:17.000Z　
> The landing page looks lovely, but the examples shown have no foundation in my head for what they're doing / showing / helping with.It's confusing enough that I don't know if this is just way above my knowledge level or whether I just don't understand what it even is.It feels like you've developed something really useful but it's so internally obvious in your own head that it's missing some steps in the explanation for everyone else on how to come along with you and see the power of it.

---

> **__MatrixMan__** · 2026-09-24T20:01:42.000Z　
> Is there a https://en.wikipedia.org/wiki/Radix_tree somewhere in there?

---

> **notuger** · 2026-09-24T20:10:11.000Z　
> I thought it was a new product from the Radix UI team focused on agents. The name is actually pretty confusing.

---

> **0x1062** · 2026-09-24T18:39:36.000Z　
> Using agents to write code

---

> **0x1062** · 2026-09-24T19:27:24.000Z　
> Nope, this is an entirely separate product and I have no affiliation with the people who worked on Radix UI, or with WorkOS.

---

> **0x1062** · 2026-09-24T19:43:02.000Z　
> It's an example of an algorithm that can be complex to read in code, but is more approachable when viewed as a diagram -- a perfect case for a tool like this.Also thank you for your feedback and taking the time to view the landing page at least!

---

> **dang** · 2026-09-24T20:04:52.000Z　
> Can you please make your points thoughtfully and not respond to people's work by ranting at them?https://news.ycombinator.com/newsguidelines.htmlhttps://news.ycombinator.com/showhn.html

---

> **0x1062** · 2026-09-24T19:55:47.000Z　
> Yes ha this is very accurate unfortunately.I'm actually using Radix right now to brainstorm and update the example on the landing page to be more descriptive.If it helps: the basic idea is that instead of an agent returning text or markdown we get it to return HTML. We then provide an app which makes working with that HTML actually useful (i.e. a sidebar to list the tools you've built, a way of commenting on the pages it generates).The most trivial example I can think of is creating a simple colour picker. With Radix you can get an agent to add a colour picker that updates the code directly when you change its value (as explained further in [1]).[1] https://radix-os.com/notes/hello

---

> **kdkdkfndjfb** · 2026-09-24T20:07:28.000Z　
> Yeah, I don’t really see the point of it just glancing at the website. In fact, that little stack of activity notifications at the bottom seem quite obstructive and unintuitive, not sure if it’s part of the product but as a UI element it looks… off.

---

> **0x1062** · 2026-09-24T20:03:13.000Z　
> Haha no sadly not, the name was chosen purely because I like the sound of it.

---

> **0x1062** · 2026-09-24T20:15:53.000Z　
> Yes sorry I may need to change that.

---

> **chrisweekly** · 2026-09-24T20:07:42.000Z　
> You'll want to strongly consider rebranding with a different name. Way too easily confused.

---

> **0x1062** · 2026-09-24T20:14:12.000Z　
> (It's not part of the free version since that works with your existing agent and you interact with it however you normally would).The message stack in the bottom are the agent replies as it works. The idea is to move away from an array of messages as the primary interface with an agent and instead make the tools the primary interface. Whether that's actually helpful is an open question but it's certainly how I prefer to work now that I've been building with it.

---

> **kdkdkfndjfb** · 2026-09-25T01:26:20.000Z　
> I see, that makes sense. Though I personally think the UI could use a little bit of a touch up.

## 导航

- 项目页：[[10-项目/radix-os.com_cfe666f3]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
