---
type: "corpus"
item_id: "5059e747dd53b092"
title: "Show HN: A new benchmark for testing LLMs for deterministic outputs"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=47950283"
project_url: "https://interfaze.ai/blog/introducing-structured-output-benchmark"
author: "khurdula"
published_at: "2026-04-29T16:01:51Z"
captured_at: "2026-09-21T01:41:43+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-21"
pub_day: "2026-04-29"
tags:
  - 语料
  - hn_show
  - author_khurdula
  - story_47950283
  - show_hn
metrics: {"points": 60, "comments": 30, "engagement_velocity": 60}
comments_count: 30
comments_total: 30
discovered_via: "hn:show_hn:174d"
---

# Show HN: A new benchmark for testing LLMs for deterministic outputs

> [!info] 一句话导读
> When building workflows that rely on LLMs, we commonly use structured output for programmatic use cases like converting an invoice into rows or meeting transcri…

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=47950283>
> 指标：点赞=60 · 评论=30 · engagement_velocity=60
> 作者：khurdula　|　发布：2026-04-29T16:01:51Z
> 项目链接：<https://interfaze.ai/blog/introducing-structured-output-benchmark>
> 采集：2026-09-21T01:41:43+08:00　|　id：`5059e747dd53b092`

## 正文

When building workflows that rely on LLMs, we commonly use structured output for programmatic use cases like converting an invoice into rows or meeting transcripts into tickets or even complex PDFs into database entries.The model may return the schema you want, but with hallucinated values like `invoice_date` being off by 2 months or the transcript array ordered wrongly. The JSON is valid, but the values are not.Structured output today is a big part of using LLMs, especially when building deterministic workflows.Current structured output benchmarks (e.g., JSONSchemaBench) only validate the pass rate for JSON schema and types, and not the actual values within the produced JSON.So we designed the Structured Output Benchmark (SOB) that fixes this by measuring both the JSON schema pass rate, types, and the value accuracy across all three modalities, text, image, and audio.For our test set, every record is paired with a JSON Schema and a ground-truth answer that was verified against the source context manually by a human and an LLM cross-check, so a missing or hallucinated value will be considered to be wrong.Open source is doing pretty well with GLM 4.7 coming in number 2 right after GPT 5.4.We noticed the rankings shift across modalities: GLM-4.7 leads text, Gemma-4-31B leads images, Gemini-2.5-Flash leads audio.For example, GPT-5.4 ranks 3rd on text but 9th on images.Model size is not a predictor, either: Qwen3.5-35B and GLM-4.7 beat GPT-5 and Claude-Sonnet-4.6 on Value Accuracy. Phi-4 (14B) beats GPT-5 and GPT-5-mini on text.Structured hallucinations are the hardest bug. Such values are type-correct, schema-valid, and plausible, so they slip through most guardrails. For example, in one audio record, the ground truth is "target_market_age": "15 to 35 years", and a model returns "25 to 35". This is invisible without field-level checks.Our goal is to be the best general model for deterministic tasks, and a key aspect of determinism is a controllable and consistent output structure. The first step to making structured output better is to measure it and hold ourselves against the best.

## 评论（30/30）

> **stared** · 2026-04-29T17:16:03.000Z　
> Thank you for sharing benchmark. However, the results are selective.Why no Opus 4.7? Why Gemini 3.1 Pro is missing?If there is some other criterion (e.g. models within certain time or budget), great - just make it explicit.When I see "Top 5 at a glance" and it missed key frontier models, I am (at best) confused.

---

> **zihotki** · 2026-04-29T17:50:44.000Z　
> I wonder if this benchmark brings any value. Models are already quite capable and reach high scores in it.

---

> **dalberto** · 2026-04-29T17:55:28.000Z　
> A benchmark without Opus 4.6/4.7 feels incomplete.

---

> **iLoveOncall** · 2026-04-29T17:59:52.000Z　
> This is just a hallucinations benchmark on a subset of outputs, not sure there's a value over general hallucinations benchmarks?> Our goal is to be the best general model for deterministic tasksI'm sorry but this simply doesn't make sense. If you want a deterministic output don't use an LLM.

---

> **broyojo** · 2026-04-29T18:08:48.000Z　
> hmm why can't structured decoding be used?

---

> **maxdo** · 2026-04-29T19:23:48.000Z　
> gpt 5.5 seems to be the recent leader overall, it make sense to include it , just to see what you trade off for speed/open source nature vs cutting edge leader.

---

> **ossianericson** · 2026-04-29T19:32:33.000Z　
> Even when the JSON pass rate is at 97% the real challenge is that the accuracy gap is invisible at the record level. Nothing flags it without a baseline to check against. Parse error is rarely where it goes wrong in my experience. 'Valid' but incorrect data is what actually reaches production.

---

> **jumploops** · 2026-04-29T21:30:05.000Z　
> I have anecdotal experience here, but I've found more success when solving the task first, and then returning it as JSON in a separate LLM call[0].Running a single non-reasoning LLM call from source data (text/image/audio in your diagram) to structured JSON seems fragile with the current state of LLMs.You're essentially asking the model to do two tasks in one pass: parse the input and then format the output. It's amazing it works a lot of the time, but reasonable to assume it won't all of the time.(As a human, when I'm filling out a complex form, I'll often jump around the document)Curious how the benchmarks change when you add an intermediary representation, either via reasoning or an additional LLM call. I'd also love to see a comparison with BAML[1].[0]In my experience we were using structured outputs as part of an agentic state machine, where the JSON contained code snippets (html/js/py/etc.). In the cases where we first prompted the model for the code, and then wrapped it in JSON, we saw much higher quality/success than asking for JSON straightaway.[1]https://boundaryml.com/

---

> **jadbox** · 2026-04-29T23:02:05.000Z　
> Wow, Qwen3.5-35B is absolutely punching above its weight. Perhaps it's the best/cheapest model for just JSON operations?

---

> **timxtokyo** · 2026-04-29T23:10:12.000Z　
> Would it be possible to add llm provider from glm5.1, minimax2.1? Those latest model have their parameters change significantly compare to previous gen

---

> **submarius** · 2026-05-04T16:00:01.000Z　
> Cool work — quick question: how should readers think about the fact that Interfaze-Beta is on the leaderboard you built? Not saying anything's wrong with the methodology, just curious how you'd recommend a third party verify the ranking is neutral to the choices you made (datasets, difficulty weights, reasoning-off default, etc.).

---

> **Flux159** · 2026-04-29T17:30:10.000Z　
> Agree that the choices are strange. Sonnet 4.6 was tested, but no Opus 4.6.Gemini 3.1 and GLM 5 came out around the same time as Sonnet 4.6 (~Feb 2026) so it's strange that they are missing, but Gemini 2.5 Flash, Gemini 3 Flash, and GLM 4.7 are there.

---

> **khurdula** · 2026-04-29T18:12:39.000Z　
> Yeah we selected models that are most commonly integrated in developer workflows and being used for structured output. Typically those models tend to be in the low -mid cost range and with no or low reasoning.For the benchmark, was kept consistent across all models and typically opus and 3.1 pro would be overkill and expensive even with reasoning off.Good point tho, will add this point in the blog too :)Also the benchmark is open source, so anyone can run a model on it and create a PR too, the leaderboard is dynamic and will automatically add that in.

---

> **khurdula** · 2026-04-29T18:16:14.000Z　
> Check out the "The JSON-pass vs Value-Accuracy gap" section in the blog. That was an eye opener.While most models were great at producing JSON schema, they were pretty bad at producing accurate values.In the graph you'll is almost a 20%-30% drop between the JSON schema pass vs the value accuracy.

---

> **khurdula** · 2026-04-29T18:55:36.000Z　
> Due to high demand, we're adding it soon!

---

> **khurdula** · 2026-05-01T23:29:47.000Z　
> We've added opus 4.6 and 4.7 to our leaderboard, they perform very closely with sonnet 4.6. Feel free to checkout our updated blog again :D

---

> **khurdula** · 2026-04-29T18:54:43.000Z　
> General hallucinations benchmarks tend to be knowledge specific like GPQA or MMLU but none specifically measure structured output end-to-end which is one of the biggest use case for LLMs.Many developer workflows use LLMs to produce structured artifacts due to it's flexibility of consuming unstructured inputs.> "don't use an LLM"Partially agree, that's what we're building towards at interfaze.ai a hybrid between transformers (LLMs) and traditional CNN/DNN architecture to solve this problem of "deterministic" output. This give devs the flexibility of custom schema definitions and unstructured input while still getting high quality structured output like you would get from a CNN models like EasyOCR.The industry is moving toward using LLMs for more and more deterministic tasks so this benchmarks allows us to now measure it.

---

> **nemo1618** · 2026-04-29T21:09:41.000Z　
> LLMs are not inherently non-deterministic. This is a common misconception. You used to be able to set temp=0 and a fixed seed and get the same output every time. This broke when labs started implementing batching, and no one bothered fixing it because the benefits of batching vastly outweighed the demand for deterministic output.I am hopeful deterministic output will return, though; DeepSeek v4 claims to have implemented "bitwise batch-invariant and deterministic kernels," though I haven't tested it myself.

---

> **khurdula** · 2026-04-29T18:41:42.000Z　
> We saw that structured decoding didn't make a difference in the quality of the output.Check out the paper section "6.3 Structured Decoding Ablation"Paper: https://arxiv.org/pdf/2604.25359We ran the comparison and saw no difference, so to keep the bench consistent since some models don't support structured decoding we used greedy decoding on all models.

---

> **khurdula** · 2026-04-29T20:15:48.000Z　
> Yep, we will be adding it soon as well.

---

> **khurdula** · 2026-05-01T23:28:34.000Z　
> hey! we've evaluated gpt 5.5 as well along with other frontier models. gemini and gemma models outperform it across all three modalities.Open source models like glm 4.7 still compete closely with table toppers.

---

> **khurdula** · 2026-04-30T15:57:05.000Z　
> We do love Qwen! It can be an easy choice when confused looking at this leaderboard.

---

> **khurdula** · 2026-04-30T16:04:30.000Z　
> We're updating our leaderboard with these model scores, should be out soon :D

---

> **khurdula** · 2026-05-05T22:33:34.000Z　
> We've open-sourced all code, and test sets. You can find them here: https://interfaze.ai/blog/introducing-structured-output-benc...To validate the choices and configurations, feel free to give it a reading. We also breakdown our methodology in the blog and in-depth within the paper.

---

> **khurdula** · 2026-05-01T23:25:55.000Z　
> We've updated our leaderboard having evaluated frontier models gemini 3.1 pro, opus 4.6 & 4.7, glm 5.1, deepseek v4, Kimi K2.6 as well.

---

> **stared** · 2026-04-29T19:54:50.000Z　
> Then the way to go is to use Pareto frontier, e.g. https://quesma.com/benchmarks/binaryaudit/#costIf you want to avoid using Opus 4.7 them why GPT-5.4 (unless with a disclaimer that it is low reasoning setting, or check that on medium its price is comparable with Haiku/Flash).Also, usually it is good to look at the newest model. Gemini 2.5 Flash is quite dated. Gemini 3.1 Flash Lite is the new one (https://openrouter.ai/google/gemini-3.1-flash-lite-preview).

---

> **staticshock** · 2026-04-29T21:26:59.000Z　
> The value of such a benchmark, to me, would be, "what is peak performance", not just "what is mid-tier performance". Also, possibly, "what's the per-dollar performance". Time and money permitting, I'd really want to see your benchmark extended to the large reasoning models.

---

> **sroussey** · 2026-04-29T21:55:18.000Z　
> Thinking Machines Lab uses batch invariant kernels, btw.

---

> **iLoveOncall** · 2026-04-29T22:29:19.000Z　
> > LLMs are not inherently non-deterministic.Reproducible does not mean deterministic. You cannot determine in advance what a prompt will give as output, even with a temperature of 0 and a fixed seed, therefore they are not deterministic.

---

> **nemo1618** · 2026-04-30T19:10:07.000Z　
> Huh? I'm not aware of anyone else who defines "deterministic" that way. "Deterministic" comes from "determinism," as in "the effects are fully determined by the causes" -- not "determine" as in "deduce."

## 导航

- 项目页：[[10-项目/interfaze.ai_89f1a60d]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
