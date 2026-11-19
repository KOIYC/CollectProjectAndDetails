---
type: "corpus"
item_id: "22dda9e2890280b6"
title: "Show HN: KradleBench – Multi-agent AI evals in Minecraft"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50550700"
project_url: "https://kradle.ai/"
author: "jamest"
published_at: "2026-11-18T19:14:28Z"
captured_at: "2026-11-19T09:43:31+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-11-19"
pub_day: "2026-11-18"
tags:
  - 语料
  - hn_show
  - author_jamest
  - story_50550700
  - show_hn
metrics: {"points": 8, "comments": 7, "engagement_velocity": 8}
comments_count: 7
comments_total: 7
discovered_via: "hn:show_hn:3d"
---

# Show HN: KradleBench – Multi-agent AI evals in Minecraft

> [!info] 一句话导读
> Hi HN -This is James and Kemal. In past lives we led Firebase and Tensorflow/JAX respectively. HN has been a particularly big part of my (James’) career and the…

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50550700>
> 指标：点赞=8 · 评论=7 · engagement_velocity=8
> 作者：jamest　|　发布：2026-11-18T19:14:28Z
> 项目链接：<https://kradle.ai/>
> 采集：2026-11-19T09:43:31+08:00　|　id：`22dda9e2890280b6`

## 正文

Hi HN -This is James and Kemal. In past lives we led Firebase and Tensorflow/JAX respectively. HN has been a particularly big part of my (James’) career and the trajectory I’ve taken would be meaningfully different without it. Thank you!Our team shipped a benchmark: KradleBench. We test AI in Minecraft Worlds.1. The worlds are multi-agent. Humans and other AIs are in there too, often pursuing their own goals. Collaboration and conflict skills fall out of this property.2. The world are dynamic. They constantly change, which means that agents need to react. “Capture the Flag” has a single winning condition, and many different ways to achieve it. This leads to many emergent and creative strategies.3. The worlds are real-time. They are not turn-based, they do not wait for AIs to finish thinking. Nature balanced speed and intelligence in humans, we can understand this in AIs too.Underneath all this is Kradle, a platform to test and understand intelligence. It’s a petri dish where any intelligence type (LLM, World Model, Human) can be compared and generate useful information to improve current systems, whether it’s on capabilities or safety.Some findings so far:
- A skilled human was #1, until yesterday when Astra 6.2 surpassed them. We lose badly on solo tasks and out-compete on multi-agent ones
- Astra 6.2 iterates on its strategy 4x faster than Fable 5.2. The Claude family tends to think hard and stick with strategies. The OpenAI models tend to be more reactive and iterative, which serves them well in multi-agent, dynamic, real-time evals.We’ve got videos on all the top model’s page, and we’ll be producing them when a new model launches. Sign up on the site to get them and for when the platform opens.Thanks for reading,James & Kemal

## 评论（7/7）

> **TheMrZZ** · 2026-11-18T19:33:30.000Z　
> Florian from Kradle here - happy to answer any question! We're very excited about this release. We did not expect Astra 6.2 to score so high, especially with its current online reputation. Looks like it's better as an autonomous agent than a coding assistant!

---

> **gsoltis** · 2026-11-18T20:03:40.000Z　
> It's wild that if this had been published a couple days ago, humans would've been in the lead. The state of the art is changing so quickly.

---

> **olivercameron** · 2026-11-18T20:16:18.000Z　
> Who knew Minecraft would become so integral to AGI. Congrats on the launch!

---

> **vikrum** · 2026-11-18T20:24:16.000Z　
> (vikrum from Kradle here, too)One of the most interesting things about this benchmark is that it encodes latency into the score as agents navigate the world where other agents are also doing things. Just because a model can score high when there is no time limit is not useful for many important workloads like active red/blue teaming. The dimension of "collaboration" in KradleBench adds color to another piece through this same prism: with a shared goal, and possibly with differing views of the world, how do they yield results greater than if it was just a single agent? We have bits and pieces of this in our day-to-day (multiple agents coordinating to create a pr, then multiple agents reviewing PRs against a code base), however, these also lack the time constraints.I'm excited to be pushing benchmarks forward. Having a safe place like Minecraft to ratchet up these types of tests is a lot of fun.

---

> **stopachka** · 2026-11-18T20:30:02.000Z　
> Great bench! Question: from playing with the models why do you think developers seem to prefer Opus / Fable, whereas Astra does much better here? What do you think Astra is lacking for them?

---

> **TheMrZZ** · 2026-11-18T20:46:19.000Z　
> Thanks!

---

> **TheMrZZ** · 2026-11-18T20:45:37.000Z　
> Great question. It seems that Astra is an excellent autonomous model (which is how we're testing them) but has very poor interactions with humans. Like using super complex vocabulary, asking questions way too deep for the user etc... It's annoying when using it as a tool, but does not cause issues within a video game.Some people also said it over-fixated on details. For coding, maybe? But from our PoV, it's actually the first model that got a lot of details correct in Minecraft. For example in our economy eval, Astra keeps improving its strategy through the game, when other models just do not grasp the complexity of the challenge. For ex Fable uses a very basic, bad strategy, and iterates at most once in the entire game.So maybe this attention to details (coupled with a great latency) make these models worse for coding but great for autonomous, real world tasks

## 导航

- 项目页：[[10-项目/kradle.ai_c866b8c2]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
