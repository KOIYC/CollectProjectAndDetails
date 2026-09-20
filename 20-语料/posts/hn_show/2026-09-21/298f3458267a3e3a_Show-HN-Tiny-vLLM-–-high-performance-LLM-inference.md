---
type: "corpus"
item_id: "298f3458267a3e3a"
title: "Show HN: Tiny-vLLM – high performance LLM inference engine in C++ and CUDA"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=48328184"
project_url: "https://github.com/jmaczan/tiny-vllm"
author: "yu3zhou4"
published_at: "2026-05-29T19:38:27Z"
captured_at: "2026-09-21T01:43:49+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-21"
pub_day: "2026-05-29"
tags:
  - 语料
  - hn_show
  - author_yu3zhou4
  - story_48328184
  - show_hn
metrics: {"points": 205, "comments": 18, "engagement_velocity": 205}
comments_count: 18
comments_total: 18
discovered_via: "hn:show_hn:144d"
---

# Show HN: Tiny-vLLM – high performance LLM inference engine in C++ and CUDA

> [!info] 一句话导读
> Show HN: Tiny-vLLM – high performance LLM inference engine in C++ and CUDA

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=48328184>
> 指标：点赞=205 · 评论=18 · engagement_velocity=205
> 作者：yu3zhou4　|　发布：2026-05-29T19:38:27Z
> 项目链接：<https://github.com/jmaczan/tiny-vllm>
> 采集：2026-09-21T01:43:49+08:00　|　id：`298f3458267a3e3a`

## 正文

Show HN: Tiny-vLLM – high performance LLM inference engine in C++ and CUDA

## 评论（18/18）

> **yu3zhou4** · 2026-05-29T20:39:08.000Z　
> README is in my opinion (author here) the most interesting - I wrote it to help others build useful mental model to be able to recreate the project yourself, without need to even read my code

---

> **nazgulsenpai** · 2026-05-29T20:41:34.000Z　
> I love the documentation formatted in lessons. I can't wait to read through it.

---

> **juancn** · 2026-05-29T21:42:39.000Z　
> Looks interesting, it reminds me of the first llama.cpp, but better documented.

---

> **dwa3592** · 2026-05-29T22:11:15.000Z　
> Very nice job on read me.>>Physically, LLM is a file which contains a lot of float numbers.aka atoms of the LLM.

---

> **einpoklum** · 2026-05-29T22:13:27.000Z　
> It seems the author believes checking the return values of CUDA API calls is not "tiny" enough :-(

---

> **cookiengineer** · 2026-05-29T22:26:55.000Z　
> Wanted to add that the author has an amazing blog with lots of interesting papers: https://jedrzej.maczan.pl/

---

> **xuanlin314** · 2026-05-30T02:10:54.000Z　
> The lesson-style README is a great approach. Breaking down LLM inference into digestible steps makes the codebase approachable even for people who haven't touched CUDA before.

---

> **GoldenJade** · 2026-05-30T02:56:28.000Z　
> Thanks for sharing this. As someone currently researching LLMs, I'm sure I'll be referencing this quite a bit going forward.

---

> **tom-wal** · 2026-05-30T08:10:25.000Z　
> I feel like I learned twice as much in 10 minutes reading this than I did reading LLM for Dummies. Thank you

---

> **sylware** · 2026-05-30T09:49:42.000Z　
> I am looking at a plain and simple C implemented LLM inference, and/or x86_64 assembly implemented, and/or AMD GPU RDNA assembly.Anybody?

---

> **samhoss93** · 2026-06-01T22:44:15.000Z　
> Great README. Genuinely one of the clearest walkthrough of inference internals. The KV cache section is worth lingering one as most of the OOM and throughput issues trace back to this and normally difficult to reason about. sequence length and batch size fill the cache in a way that show up under real traffic.look forward to going over the completed course.

---

> **janalsncm** · 2026-05-30T02:03:52.000Z　
> Really practical teaching approach. I clicked in to see how safetensors are loaded and just kept reading. Thanks for sharing.

---

> **lukemerrick** · 2026-05-30T15:25:28.000Z　
> I am not super familiar with C and CUDA, so I read solely for the README and enjoyed it supremely. The blend of cheerful walking through instructive examples and your philosophical takes on how to approach the exercise to get the most out of it put me in a great mood. You captured that special upbeat attitude that comes about when you're doing something as well as you can just because it's so legitimately interesting to you.

---

> **quanglee** · 2026-06-01T11:30:08.000Z　
> love the details you put into to explain different techniques. it's a bit dense though, some schemas will help i think

---

> **cyanydeez** · 2026-05-29T22:16:38.000Z　
> the universe is just atomic if statments

---

> **irishcoffee** · 2026-05-30T13:10:55.000Z　
> I heard once that c++ can become assembly at some point if you type the right things in. :)

---

> **nullpoint420** · 2026-05-30T07:51:01.000Z　
> it from bit

---

> **sylware** · 2026-05-31T11:23:29.000Z　
> Well, the whole purpose is to be independent of invisible backdoor injectors...^W I mean compiler,
> to be more accurate those compilers which deals with computer languages with an absurd and
> grotesque syntax complexity.

## 导航

- 项目页：[[10-项目/github.com_10952d2b]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
