---
type: "corpus"
item_id: "c4ba94e53e6cb05a"
title: "Show HN: Wattai.dev – Free Decision Intelligence"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49776584"
project_url: "https://wattai.dev/"
author: "namanvyas"
published_at: "2026-09-20T15:05:46Z"
captured_at: "2026-09-21T09:44:03+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-21"
pub_day: "2026-09-20"
tags:
  - 语料
  - hn_show
  - author_namanvyas
  - story_49776584
  - show_hn
metrics: {"points": 2, "comments": 0, "engagement_velocity": 2}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:3d"
---

# Show HN: Wattai.dev – Free Decision Intelligence

> [!info] 一句话导读
> wattai Try it Benchmarks API Download on-device decision model · hosted API: 1,024 input tokens · apache-2.0

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49776584>
> 指标：点赞=2 · 评论=0 · engagement_velocity=2
> 作者：namanvyas　|　发布：2026-09-20T15:05:46Z
> 项目链接：<https://wattai.dev/>
> 采集：2026-09-21T09:44:03+08:00　|　id：`c4ba94e53e6cb05a`

## 正文

wattai Try it Benchmarks API Download on-device decision model · hosted API: 1,024 input tokens · apache-2.0 · free in the v0.5 preview
 wattai is a decision model that runs on your own machine. You send it a piece of text and a list of options. It returns the option that fits, plus a calibrated probability for every option you sent.
 It never generates a string. It scores the options you supply and hands back a calibrated distribution over them. On CLINC150 it scores 96.3% against TypeSafe Jev at 87%, the only benchmark both have run. That Jev figure comes from an independent pre-registered eval. The wattai figure is its own v2 measurement.
 Download the 726 MB f16 build and run it offline. Or call the hosted API at api.wattai.dev, free during the preview, with no key and no account for 1,000 calls a day. In five two-question requests on September 20, 2026, the hosted API took 2.16–2.41 seconds round trip, including 1.79–1.85 seconds of reported server inference. Your network and server load will affect timing. Local latency depends on your hardware and is not benchmarked here.
Download the f16 build ↓ Call the API, no key →
 Try a decision
 Edit the text, choose your questions, and run a real API request. No key or account needed. These examples use the hosted model; your input is sent to the server.
Customer ticket Invoice Security incident Agent trace
 input text From: Dana Novak
Subject: Return Label — order #236758
Hi support,
How do I get a return label for the printer?
This is unacceptable and I need this fixed today. questions What is the customer's main intent? choice · 5 options How urgent is the ticket (1 lowest, 5 highest)? score · 5 options Does the customer explicitly ask for a refund? noul · 2 options Which product is the ticket about? choice · 4 options Ask wattai → 4 questions · one request
live response
 Run the example to see which options fit, with a probability for each.
Where wattai beats TypeSafe Jev
 On CLINC150, wattai scores 96.3% and TypeSafe Jev scores 87%. That Jev figure comes from an independent pre-registered eval, and the wattai figure is its own v2 measurement. CLINC150 is the only apples-to-apples number between the two, and every other Jev cell reads not run, which means not evaluated. Expected calibration error is 4.1 for wattai, averaged across ten tasks, against 12 for Jev, the midpoint of an independently measured range. Lower is better.
 wattai is distilled from SmolLM2-360M. Against that base zero-shot it scores 82.3% on MNLI against 33%, and 81.5% on BoolQ against 63%.
chart table
 task CLINC150, intent + out-of-scope MNLI, natural-language inference BoolQ, yes/no reading ARC-Easy, grade-school science ARC-Challenge OpenBookQA CommonsenseQA HellaSwag, continuation PIQA, physical commonsense MMLU (5-shot subject knowledge) Calibration error (ECE, lower is better)
wattai builds other models not evaluated on this task: SmolLM2-360M .
wattai: v2 tern_synth · jev: independent pre-registered eval · sm2: not published
What the confidence does not tell you
 The probability says which of your options fits best, not whether any of them fit. A sentence about the weather, scored against bug, feature and praise, comes back praise with a number that looks like any other answer. If none-of-the-above is a real outcome, send it as an option; add_none appends one for you.
Use it in your app
 Send the text once and ask as many questions about it as you like. They share a prefill, so ten questions cost about what one costs.
curl Python SDK JavaScript SDK Copy example
 Install the official client: npm install @typesafe-ai/sdk . Node.js 20 or newer.
 request import { choice , score , TypeSafeClient } from " @typesafe-ai/sdk " ;
const client = new TypeSafeClient ({
 apiKey : " anonymous " ,
 baseURL : " https://api.wattai.dev " ,
 defaultModel : " watt-v0.5 " ,
 });
const response = await client . systemOne ({
 state : { document : " From: Dana. How do I get a return label? " },
 questions : {
 intent : choice ( " What is the customer intent? " , {
 return_label : null ,
 refund_request : null ,
 shipping_delay : null ,
 }),
 urgency : score ( " How urgent is it? " , [ " low " , " medium " , " high " ]),
 },
 });
console . log ( response . answers . intent . choice );
 console . log ( response . answers . urgency . score );
 example response {
 " model " : " watt-v0.5 " ,
 " answers " : {
 " intent " : {
 " type " : " choice " ,
 " choice " : " return_label " ,
 " confidence " : 0.88756 ,
 " probabilities " : {
 " return_label " : 0.88756 ,
 " refund_request " : 0.09248 ,
 " shipping_delay " : 0.01996
 }
 },
 " urgency " : {
 " type " : " score " ,
 " score " : 1.1209 ,
 " confidence " : 0.39813
 }
 }
 }
choice categorical. pick one of up to 255 options.
 noul yes/no, returned as a probability.
 score ordered levels, so 4 sits next to 5.
 The hosted API is free in preview
 POST api.wattai.dev/v1/systemone is free during the v0.5 preview, with no key and no account up to 60 requests a minute and 1,000 calls a day. A bearer key raises that to 300 a minute and 20,000 a day.
POST /v1/systemone run typed decisions in one forward pass
 POST /v1/keys generate a bearer key with the higher rate limit
 GET /v1/health model info and current rate-limit tiers
request shape state string, required the text the model reads. the hosted API processes up to 1,024 input tokens; longer input is truncated.
 questions array, 1-32 each: {q, options, kind, add_none?}
 .q string the question in natural language
 .options array of strings, 1-255 the allowed answers. required for every kind, including noul.
 .kind "choice" | "noul" | "score" choice is categorical, noul is yes/no, score is ordered levels
 .add_none boolean, optional appends a "none of these" option. defaults on for choice, off for noul and score.
response shape results array one entry per question, in the order sent
 .argmax string the most likely option label
 .confidence 0..1 probability of the argmax
 .options array of strings the labels as scored, with "none of these" appended when you asked for it
 .probs array of 0..1 calibrated distribution over the options above
 .kind string echoes the question kind
 model string identifier of the served build
 ms int server-side inference latency in milliseconds
rate limits
 anonymous, by ip 60/min · 1,000/day no key, no account. enough for a prototype.
 bearer key 300/min · 20,000/day one request to get one, see below.
 response headers X-RateLimit-* Limit and Remaining ride on every response.
 over the limit HTTP 429 Retry-After says when to come back.
Lift the limit
 curl -X POST https://api.wattai.dev/v1/keys \
 -H " content-type: application/json " \
 -d ' {"note": "my-app-name"} '
# {"key": "wattai_xxxxxxxxxxxxxxxxxxxx",
 # "limits": {"per_min": 300, "per_day": 20000}}
# then send it on every request:
 # -H "authorization: Bearer wattai_xxxxxxxxxxxxxxxxxxxx"
/ It is a decision model, not a chat model. It never generates a string, it only picks from the options you send.
 / Options can run to 255 items, and the model scores all of them in the same pass.
 / Questions about the same state share a prefill, so ten questions cost about what one costs.
 / Five sequential two-question requests to /v1/systemone on September 20, 2026 took 2.16–2.41 seconds round trip, with 1.79–1.85 seconds reported server inference. These are observations from one client, not a latency guarantee. The live demo shows both timings for your request. Local inference depends on your hardware.
 Four builds, apache-2.0
 wattai-fp.gguf is the 726 MB f16 build, the one the benchmarks are measured on. The ternary builds score below it and fall under the SmolLM2-360M base on PIQA (66.3 against 72) and MMLU (33.7 against 36).
wattai-fp.gguf recommended the build the benchmarks are run on. unquantized weights, every point of accuracy intact. 726 MB · gguf · f16
 wattai-tern-q8.gguf ternary weights, 8-bit embeddings. a third of the size, and it keeps the calibration. 205 MB · gguf · tq2_0 · + side lora 17 MB
 wattai-tern-tq1.gguf the smallest build. same body, tq1_0 packing. for phones and edge boards. 201 MB · gguf · tq1_0
 wattai-side.gguf the higher-precision residual that pairs with a ternary body. load it as a lora in llama.cpp. 17 MB · gguf · lora · rank 16
 apache-2.0 · v0.5 preview · free to use, self-host and redistribute.
 Copyright © 2026 wattai · apache-2.0
 Try it Benchmarks API Download hello@wattai.dev

## 关联链接

- https://api.wattai.dev
- https://api.wattai.dev/v1/keys

## 导航

- 项目页：[[10-项目/wattai.dev_bf503fbf]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
