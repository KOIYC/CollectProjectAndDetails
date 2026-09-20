---
type: "corpus"
item_id: "dbb76c14769be1bd"
title: "Show HN: CUA-S1 – A System One Model for Computer Use"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49767564"
project_url: "https://github.com/trycua/cua"
author: "frabonacci"
published_at: "2026-09-19T15:52:51Z"
captured_at: "2026-09-20T09:48:16+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-20"
pub_day: "2026-09-19"
tags:
  - 语料
  - hn_show
  - author_frabonacci
  - story_49767564
  - show_hn
  - front_page
metrics: {"points": 63, "comments": 7, "engagement_velocity": 63}
comments_count: 7
comments_total: 7
discovered_via: "hn:show_hn:3d"
---

# Show HN: CUA-S1 – A System One Model for Computer Use

> [!info] 一句话导读
> Hello HN! We're Dillon and Francesco from Cua.We were wondering how many computer use tasks actually need a full general purpose LLM (e.g. gpt-6-astra, claude-o…

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49767564>
> 指标：点赞=63 · 评论=7 · engagement_velocity=63
> 作者：frabonacci　|　发布：2026-09-19T15:52:51Z
> 项目链接：<https://github.com/trycua/cua>
> 采集：2026-09-20T09:48:16+08:00　|　id：`dbb76c14769be1bd`

## 正文

Hello HN! We're Dillon and Francesco from Cua.We were wondering how many computer use tasks actually need a full general purpose LLM (e.g. gpt-6-astra, claude-opus-5 etc.) to think through all their decisions and steps. Some tasks require thinking about a plan, exploring different paths, recovering from failure. Other tasks are a question of making local decisions, like this value should go in this box, or should I check this box, or this element should be ignored.We wondered how far we could go with a small model trained to only make these kinds of decisions.Our inspiration was Typesafe's Jev and its System One Model framing. This is a nod to the dichotomy between thinking quickly, automatically, and intuitively (system 1) vs. thinking slowly, analytically (system 2), as described by Daniel Kahneman.The interesting question for us was: what happens if you give a model an interface of current context, and a set of possible choices, and you ask it to return a probability for each choice? This kind of model does not generate output token by token like most LLMs do, but rather scores the options you give it, which you can check, trust, and use to drive your app's behavior.CUA-S1 is our answer for narrow, specialized decision models for computer use. Our first release is CUA-S1-FORMS. We built this from ideas and code in jevlike, and then trained a second model just to handle form interactions. It has 706k parameters, and the original checkpoint is 2.8 MB.The first training iteration took less than 30 minutes on synthetic data. Given a set of structured elements and values extracted from a document, it predicts whether to use the given value, CHECK, CLICK, or SKIP for each element. It does not predict new values for text fields, and does not consider screenshots. Element decisions are scored together, and your code can order the actions, and Cua Driver will execute them one at a time.A first evaluation of this specialist vs. hosted Jev on our form task:- For the whole decision set: 99.7% correct vs 83.6%.- For the subset of steps that require an action: 100% correct vs 96%.- For the subset of steps that are just leaving already-filled fields alone: 100% correct vs 74%.The specialist was trained specifically for this task and convention (just press skip for already filled boxes), while hosted Jev has not been fine-tuned for it, so this is an experiment in scoped specialization.We measured 7-9 ms to score a form locally vs. 260-280 ms per call to hosted Jev including network latency, though those samples measure different things and are not end-to-end form completion times.Our interest here is in the space between a brittle script and a general agent loop. The content and layout of form fields vary enough that scripts get unwieldy, but the set of available decisions can remain narrow and well scoped. We want to explore the possibility of a general agent encountering something novel, and passing well understood decisions over to specialists like this.That is a direction we are looking into. The current release is for forms only. We're open sourced the synthetic data generation, training, evaluation, and Driver integration under libs/cua-s1 with an MIT license.Comments welcome! Especially if you are building computer-use agents and have run into a recurring decision that is too variable to script but is too narrow to call another LLM for.

## 评论（7/7）

> **badatnames** · 2026-09-19T19:31:37.000Z　
> Please give us a hyper general cookie consent popup dismissal add-on :)

---

> **AM1010101** · 2026-09-19T20:44:03.000Z　
> Would the idea be to have many specialist models (forms, wikipedia, final cut, etc) and have a parent model choose which is best (potentially also a specialist model for selecting specialist models) with the idea an llm would give a larger goal and trigger this cascade of specialists to quickly do the task?

---

> **Axsuul** · 2026-09-19T20:45:09.000Z　
> Are we able to use CUA to build a system similar to Grok Bot?

---

> **hbarka** · 2026-09-19T21:41:12.000Z　
> I read the nod to Typesafe Jev. Are you implying use of RLCD or still RLHF?

---

> **ShakataGaNai** · 2026-09-19T22:59:11.000Z　
> I think this is the logical next step in AI. There will be a few large "smart" AI models, but mostly smaller more hyper-specialized. In large part because they are faster to build....and faster/cheaper to run. As the model this post is about shows - you don't need to be able to write the works of shakespear to be able to run a computer.The frontier models are already getting STUPID expensive. More than the average person certainly can reasonably afford for any use case. And even the business users are having a hard time justifying the prices for anything other than the most bleeding edge, "big picture" things (like creating a huge project plan).

---

> **adastra22** · 2026-09-19T23:18:09.000Z　
> Nobody outside TypeSafe even knows what RLCD is, so that’s impossible to answer.

---

> **tomrod** · 2026-09-19T23:09:08.000Z　
> Conscious thought seems to follow this too. No one thinks to breath, we often get in a groove and do deep thinking during a rote task, etc.

## 导航

- 项目页：[[10-项目/github.com_1c712cad]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
