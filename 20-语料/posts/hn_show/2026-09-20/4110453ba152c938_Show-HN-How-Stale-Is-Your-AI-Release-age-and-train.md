---
type: "corpus"
item_id: "4110453ba152c938"
title: "Show HN: How Stale Is Your AI? Release age and training cutoff for 20 models"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49726343"
project_url: "https://stale.jock.pl/"
author: "joozio"
published_at: "2026-09-16T13:01:52Z"
captured_at: "2026-09-21T21:59:53+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-20"
pub_day: "2026-09-16"
tags:
  - 语料
  - hn_show
  - author_joozio
  - story_49726343
  - show_hn
metrics: {"points": 80, "comments": 49, "engagement_velocity": 80}
comments_count: 49
comments_total: 49
discovered_via: "hn:show_hn:90d"
---

# Show HN: How Stale Is Your AI? Release age and training cutoff for 20 models

> [!info] 一句话导读
> How stale is your AI? Data checked 2026-09-16

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49726343>
> 指标：点赞=80 · 评论=49 · engagement_velocity=80
> 作者：joozio　|　发布：2026-09-16T13:01:52Z
> 项目链接：<https://stale.jock.pl/>
> 采集：2026-09-21T21:59:53+08:00　|　id：`4110453ba152c938`

## 正文

How stale is your AI? Data checked 2026-09-16
How stale is your AI? Release age and training cutoff for 20 models
Two dates decide how current an AI model really is. The release date is when the
 lab shipped it. The training cutoff is when it stopped reading. This page holds both
 for 20 current models across 8 labs, and counts upward from each
 one live. 10 of 20 models have a cutoff their lab actually
 publishes.
The live version of this page needs JavaScript for the counters. The dates
 themselves are below, and the same data is available as
 models.json .
Does this still matter when the model can search?
Only if the model decides to search, and that decision runs on the same weights
 that hold the stale fact. Over 2000 calls across 16 of the models below, each one
 handed a web search tool, the frontier models decided correctly almost every time,
 while weaker ones stated settled facts that had changed without checking, and
 searched the web for things like the boiling point of water:
 I gave 16 of these models a search button and asked who the king of Norway is. Five named a dead man.
The shelf: release date and training cutoff, stalest first
Every model name links to the lab document the date came from.
Model Lab Released Training cutoff
Llama 4
 Meta
 Apr 5, 2025
 Aug 2024
Claude Haiku 4.5
 Anthropic
 Oct 15, 2025
 Jul 2025
Mistral Large 3
 Mistral AI
 Dec 2, 2025
 Not established
Gemini 3.1 Pro
 Google DeepMind
 Feb 19, 2026
 Jan 2025
Mistral Small 4
 Mistral AI
 Mar 16, 2026
 Not established
Mistral Medium 3.5
 Mistral AI
 Apr 28, 2026
 Not established
Claude Sonnet 5
 Anthropic
 Jun 30, 2026
 Jan 2026
GPT-5.6 Sol
 OpenAI
 Jul 9, 2026
 Feb 16, 2026
GPT-5.6 Luna
 OpenAI
 Jul 9, 2026
 Feb 16, 2026
Claude Opus 5
 Anthropic
 Jul 24, 2026
 May 2026
Qwen3.8-Max
 Alibaba
 Aug 3, 2026
 Not established
Muse Glimmer
 Meta
 Aug 10, 2026
 Not established
Grok 4.6
 xAI
 Aug 12, 2026
 Feb 1, 2026
DeepSeek V4-Pro
 DeepSeek
 Aug 13, 2026
 Not established
Qwen3.8-Flash
 Alibaba
 Aug 26, 2026
 Not established
Claude Fable 5.1
 Anthropic
 Sep 1, 2026
 Jun 2026
Gemini 3.8 Flash
 Google DeepMind
 Sep 2, 2026
 Not established
Muse Spark 1.3
 Meta
 Sep 2, 2026
 Not established
GPT-6 Astra
 OpenAI
 Sep 3, 2026
 Apr 30, 2026
DeepSeek V4.1-Flash
 DeepSeek
 Sep 10, 2026
 Not established
For your agent
A model is a poor source on models, so give your agent a better one. These lines
 go in the AGENTS.md or CLAUDE.md your agent already reads, and point it at
 models.json , which carries the release date, the published
 cutoff and a source link for all 20 models.
## Model freshness
Your knowledge of AI models is stale. Release dates, version numbers
and which model is current all stop at your training cutoff, and the
wrong answer still sounds confident.
Before naming any model, version or date as current, fetch
https://stale.jock.pl/models.json and read the dates there.
Treat anything with a date attached as unverified until you have
checked it.
Machine readable description of this page for agents and crawlers:
 llms.txt . When the shelf moves, that file moves with it, and
 the change gets written up at
 Digital Thoughts .
Common questions about training cutoffs
What is an AI training cutoff?
The training cutoff is the date a model stopped reading. Everything that happened after it is simply absent from what the model knows. A model can ship in September and still stop reading in April, which means it is five months behind on the day it launches.
What is the difference between a release date and a training cutoff?
The release date is when the lab put the model in front of you, and it is what the headlines report. The training cutoff is when the model stopped reading. The gap between the two is how far behind the model already was on launch day, before a single user typed anything into it.
Does browsing or web search fix a stale training cutoff?
No. When a model searches the web for you it is not learning anything. It reads a few pages, uses them in that one answer, and forgets. Open a new chat and it is April again. Search tools paper over the gap. They never close it. The search also has to be triggered by the model, using the same weights that hold the stale fact, so the misses land exactly where the model feels most certain. Measured over 2000 calls across 16 of the models on this page, each holding a search tool: frontier models decided correctly almost every time, while weaker ones answered settled questions from memory after the answer had changed, and searched the web for the boiling point of water.
Which AI labs publish a training cutoff date?
5 of 8 labs have a published cutoff for at least one model on this page: Anthropic, Google DeepMind, Meta, OpenAI and xAI. 10 of 20 current models carry a published cutoff. A blank means the checked vendor sources did not establish a cutoff for that model; it is not proof that the lab has never published one.
How do I ask a model for its own training cutoff?
Ask it directly: "what is your training cutoff date?" A well behaved model answers, or says it is not sure. One that invents a confident date has just told you something useful about itself. Check the answer against this page before you trust it, because a model is a poor source on models.
How do I make my AI agent aware of its own training cutoff?
Put a few lines in the agent's instructions file, the AGENTS.md or CLAUDE.md it already reads, telling it to fetch https://stale.jock.pl/models.json before it names any model, version or date as current, and to treat anything with a date attached as unverified until it has checked it. The export carries release date, published cutoff and a source link per model, and it is regenerated whenever the page is, so the agent reads today's dates rather than the ones baked into its weights. The wording is on the page, ready to paste.
How old is GPT-6 Astra and its training data?
GPT-6 Astra was released on Sep 3, 2026 and its training data stops at Apr 30, 2026. Both counters on this page tick upward from those dates, so the numbers stay correct without anyone editing them.
Digital Thoughts /
 jock.pl / wiz.jock.pl

## 评论（49/49）

> **ryanschaefer** · 2026-09-16T14:06:01.000Z　
> Do people prefer the new flat style LLMs are producing? I don’t mind it as much as the gradient theme they were pumping out previously.

---

> **jasonjmcghee** · 2026-09-16T14:11:54.000Z　
> It still matters, but in the age of good reasoning, tool use, and web search, this is much less of a problem than it used to be.

---

> **delichon** · 2026-09-16T14:17:28.000Z　
> After Trump's last inauguration, ChatGPT would still tell me that Biden was President of the US. I understand that the training cutoff was before Biden dropped out. But it knew, or should have known, the current date and that there had been an election since its last update, but it didn't qualify the answer. When I asked it to search the web, it got it right. The moral I took away was to always ask for the search whenever I ask about current events. I do that so routinely that I wouldn't know if this problem has been fixed. I suppose that failing to update my priors per individual model release is a form of bigotry against a widely hated class.

---

> **gjskngnf** · 2026-09-16T14:40:01.000Z　
> I remember when the US captured Venezuelan president Maduro, and when I posed a prompt related to this, the model said that’s pure fiction. I told it to double check. Still didn’t want to entertain the idea. It only acquiesced when I specifically directed it to check Reuters. I haven’t noticed this problem in months. Model cutoff seems to be less of a problem these days.

---

> **j45** · 2026-09-16T14:42:11.000Z　
> Depending on the use case certain models very well remain as or more reliable for certain tasks.

---

> **speedping** · 2026-09-16T14:42:23.000Z　
> Pre-AI internet data is like pre-war steelThe slop would multiply if we keep feeding it to new models in a loop

---

> **VCFundedGenYer** · 2026-09-16T14:46:55.000Z　
> I remember running the docker container for ollama and its knowledge cutoff is somewhere in 2023 still. That's unacceptable.

---

> **SirMaster** · 2026-09-16T18:06:11.000Z　
> This is one of the things that bothers me about AI.To me, intelligence or an intelligent entity should be able to learn from its mistakes and learn new things on its own. Having to start from scratch to teach an AI new facts or new skills is not very intelligent IMO.

---

> **ctkhn** · 2026-09-16T18:35:39.000Z　
> For general purpose use this is interesting, but if I'm just using an LLM for coding, does this matter at all? I would hope something like a new java version after a model's publish date can be handled and understood by the model through tool calls and context even if it's not explicitly in the training data, the same way the LLM doesn't have my existing code or the plan to change it baked in from training.

---

> **asimovDev** · 2026-09-16T19:22:15.000Z　
> Qwen-3.8 for me automatically set copyright footer on a website to 2025 and thought Astro 5.x is the latest version which first came out in December 2024

---

> **sanjayselvaraj** · 2026-09-16T20:41:06.000Z　
> Depending on the use case certain models

---

> **danbrooks** · 2026-09-16T21:15:06.000Z　
> An aside - isn't it nice that have been fewer model releases the past week or so? A brief respite!

---

> **dhanizael** · 2026-09-18T00:48:34.000Z　
> it is depending, i think.

---

> **datron** · 2026-09-18T16:29:49.000Z　
> I feel like with web search, exa and fetch built into harnesses this is no longer a problem. Haven't faced this issue in months.

---

> **dominotw** · 2026-09-16T14:31:06.000Z　
> all the reasoning still comes from pretraining data

---

> **lukewarm707** · 2026-09-16T16:26:40.000Z　
> in my chat with gemini it could not differentiate between current events and fiction.if you point it to the web it got the point, but started treating everything like fiction. so it simply started making up possible scenarios and playing them off as real answers when asked for factual information.i could not tell what the issue was or how to fix it because the reasoning is encrypted. the obfuscation model spat out something like: 'the user is asking for details about a fictional scenario in which the usa has assassinated the leader of iran'i really don't like the way big ai companies are going. encrypted thinking, guardrails, adversarial personality, moralizing. it is creating something anti-human.

---

> **spindump8930** · 2026-09-16T17:51:41.000Z　
> It can be quite hard to determine what needs a tool call or not. LLMs are not well calibrated to what they know and don't know, and tool calls can add latency and extra costs. There are lots of things that are "obvious" right until they aren't - especially political events and disasters.

---

> **andai** · 2026-09-16T14:24:48.000Z　
> ChatGPT recently started web searching for for basically every general knowledge question, which I found quite odd. Maybe an overcorrection to the issue you were having?

---

> **ahmedfromtunis** · 2026-09-16T17:04:47.000Z　
> I forgot which was it, ChatGPT or Gemini, but one of them insisted on calling Trump "former president" even when discussing decisions he just announced as president. Lol

---

> **super256** · 2026-09-16T14:44:47.000Z　
> It's a "problem" of compute, I think. If you query without an account on ChatGPT you will see the model look up less stuff and research less, than when you have a paid account and choose "medium" or "high" in the effort slider.Which makes sense, because of you have looked into search and crawlers you notice that search is actual quite expensive (which is why e.g. Kagi charges a few bucks for search every month).

---

> **InsideOutSanta** · 2026-09-16T14:46:54.000Z　
> Came here to say the same thing. Models used to rely heavily on world knowledge from their training data. They are now much better at tool use and deciding when to research a topic, rather than just answering from memory.I wonder how much that extends to using LLMs for programming. I assume most knowledge of programming language syntax still comes from training data.

---

> **Isamu** · 2026-09-16T16:40:04.000Z　
> >the model said that’s pure fiction.Were you expecting your model to be updated on current events? Why?Also the specific event you are referring to is a statistically very improbable event, prior to its actually happening.>It only acquiesced when I specifically directed it to check Reuters.Do all models do this? They check in with Reuters? Why would a model think that you asking about an extremely improbable event warranted reaching out to Reuters?

---

> **NegativeLatency** · 2026-09-16T18:04:05.000Z　
> Gets me with AWS stuff on claude all the time, fortunately there's a official amazon MCP for their docs which helps a lot, but I still have to occasionally tell it to check the docs/mcp.

---

> **tannertech** · 2026-09-16T19:01:37.000Z　
> ChatGPT once told me I was the target of a sophisticated nation state misinformation campaign when I linked it a Reuters article

---

> **Muromec** · 2026-09-16T16:12:46.000Z　
> This is one of the problems that eventually solves itself, somehow

---

> **hasteg** · 2026-09-16T18:35:41.000Z　
> This is likely being solved with stuff like watermarking which Anthropic just added to Claude... I'd imagine they are testing new data and verifying that training data (or at least the data which do NOT want to be AI generated, i.e actual human text) is not generated, at least with claude.

---

> **jasonjmcghee** · 2026-09-16T15:29:30.000Z　
> ollama is just an inference engine - it just runs models.it must ship with some default old model if you didn't need to explicitly download one

---

> **spindump8930** · 2026-09-16T17:54:27.000Z　
> This is one of the jagged mismatches between users and LLM developers. The median user doesn't care or want to know about static models and knowledge cutoffs and whether a model can do tool calls or if tool calls even happened. They just want something that works.Fortunately increased capabilities seem to make this a basic expectation with new releases.

---

> **ck2** · 2026-09-16T18:15:44.000Z　
> few more generations they will invent "patch in place"(with "AI" developing the technique of course)

---

> **prng2021** · 2026-09-16T18:44:49.000Z　
> The inference time results are quite different. These models haven’t just been trained with tons of docs, blog entries and videos about Java 8. They’ve also been trained on tons of code examples from simple to complex real world ones.You’re not going to get all that just by pointing the LLM to the recently released Java 27 documentation. That information is also potentially adding tons of content to your context, which is already filled with tons of other data (your code, other recently released libraries it has to get documentation for, etc).

---

> **smt88** · 2026-09-16T18:59:52.000Z　
> My experience with Claude is that it doesn’t handle its own training cutoff properly. It responds as though its cutoff is today. Gemini is even worse about this.I’m going to add this site to my agents files so that they’re explicitly aware of their own limitations.

---

> **smt88** · 2026-09-18T16:37:43.000Z　
> Claude sometimes (and Gemini always) will be lazy and fail to fetch new data from the web. Gemini will also repeatedly lie about it and say that it did when it actually didn’t.

---

> **bigmadshoe** · 2026-09-16T14:48:47.000Z　
> I think they mean reasoning their way to the need for a web search.

---

> **binlog** · 2026-09-16T14:52:52.000Z　
> Says who? Models can also use results from tool calls in their reasoning loops.

---

> **DenisM** · 2026-09-16T21:41:56.000Z　
> The Trump and former president terms were likely firmly stuck together in the embedding space. The model doesn’t validate every single token it produces because validation itself requires tokens. A bloom filter of outdated embeddings will help, when the labs get around to adding it.

---

> **Catloafdev** · 2026-09-16T15:40:31.000Z　
> It's not strictly compute, because this has noticeably improved in open-weight models too, such as Gemma and Qwen. I suspect they noticed this issue and adjusted their training to be better about it over time.

---

> **NegativeLatency** · 2026-09-16T18:05:14.000Z　
> I find they generally do ok, but a few lines in an AGENTS.md or manual prompting to verify stuff against current docs/source, and check for current version of software helps a lot.

---

> **mywittyname** · 2026-09-16T16:42:23.000Z　
> He asked it to double check. It's reasonable to expect the LLM to handle that trivial task.

---

> **gjskngnf** · 2026-09-16T17:01:46.000Z　
> I was not expecting model weights to be updated on current events.It’s clearly warranted because a model that trusts its weights on current events will give an outdated answer. Extremely improbable events happen all the time.

---

> **SirMaster** · 2026-09-16T18:13:19.000Z　
> If OpenAI is going to call Astra AGI, then I would expect it to be able to update it's weights to new knowledge, because a generally intelligent being can indeed do this.I can teach myself to play an instrument, and I'm not just building this huge lookup table that I have to access every time I play the instrument. I am updating the weights in my neurons.Until AI can do this it's not AGI in my book.

---

> **dpoloncsak** · 2026-09-17T18:23:37.000Z　
> There are a lot of people who would say that is exactly what Reuters is.
> Any American news outlet, really.

---

> **ctkhn** · 2026-09-16T18:51:19.000Z　
> Gotcha, that makes a lot of sense. Thank you

---

> **jasonjmcghee** · 2026-09-16T15:21:46.000Z　
> Or other kind of search / knowledge acquisition / computer use etc to get the information needed

---

> **ahmedfromtunis** · 2026-09-16T17:01:48.000Z　
> I built a toy news-summarizing agent with Gemma 4, and it was so frustrating, actually, because of the cut-off date.The model wasted over half the token budget, each time, on internal debates over the current date.When generating a World Cup summary, for example, it refused to believe qualification rounds were over and refused to even call the web searching tool to collect the data.I injected the current datetime at the very beginning of the system prompt, but Gemma refused to believe it!The m-effer insisted the timestamp was fake and hypothesized it was being evaluated in a synthetic lab test with simulated future dates!No amount of system prompting could convince it to trust the clock.That was the most frustrating and bizarre "bug" I ever faced!

---

> **xienze** · 2026-09-16T17:33:06.000Z　
> I think the models are trying to optimistically avoid doing web searches, because they're surprisingly a lot harder to do well than you'd think.

---

> **tannertech** · 2026-09-18T10:00:54.000Z　
> It was a real world event. The guy is still dead unfortunately. If Sputnik or Pravda are more your style they reported on the same event.

---

> **ThunderSizzle** · 2026-09-16T20:23:48.000Z　
> Did you try other models (e.g. Qwen3.6 or others)? I'm curious how others fare.I've noticed Qwen3.6 struggles a bit with today/date based logic.

---

> **carlos_rpn** · 2026-09-16T20:30:06.000Z　
> Qwen 3.6 did the same thing for me.Only after some cajolling it finally went to check the history I asked it to (I had been testing KoboldCPP's web search).

---

> **DenisM** · 2026-09-16T21:33:04.000Z　
> How so?

## 关联链接

- https://stale.jock.pl/models.json

## 导航

- 项目页：[[10-项目/stale.jock.pl_dbc9010b]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
