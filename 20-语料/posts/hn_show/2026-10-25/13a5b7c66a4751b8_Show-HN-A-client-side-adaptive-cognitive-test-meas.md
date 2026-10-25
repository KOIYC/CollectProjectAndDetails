---
type: "corpus"
item_id: "13a5b7c66a4751b8"
title: "Show HN: A client-side adaptive cognitive test measuring micro-hesitations"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50225764"
project_url: "https://kat-assessment.com/"
author: "mr-boombastic"
published_at: "2026-10-24T21:56:06Z"
captured_at: "2026-10-25T23:24:35+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-10-25"
pub_day: "2026-10-24"
tags:
  - 语料
  - hn_show
  - author_mr-boombastic
  - story_50225764
  - show_hn
metrics: {"points": 2, "comments": 1, "engagement_velocity": 2}
comments_count: 1
comments_total: 1
discovered_via: "hn:show_hn:3d"
---

# Show HN: A client-side adaptive cognitive test measuring micro-hesitations

> [!info] 一句话导读
> I’m not a software engineer by trade. My background is in behavioral science and human-computer interaction, but I wanted to solve a specific problem I found wh…

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50225764>
> 指标：点赞=2 · 评论=1 · engagement_velocity=2
> 作者：mr-boombastic　|　发布：2026-10-24T21:56:06Z
> 项目链接：<https://kat-assessment.com/>
> 采集：2026-10-25T23:24:35+08:00　|　id：`13a5b7c66a4751b8`

## 正文

Hi HN!
I’m not a software engineer by trade. My background is in behavioral science and human-computer interaction, but I wanted to solve a specific problem I found when applying for jobs which is the logical test. They are booooring, easy to cheat on if you really want to and provides very limited information about people. I built this prototype from scratch sing AI to bring my idea to life.
So now I've been working on this side project for a Cognitive Adaption Engine (CAT/KAT in swedish) for about three weeks. Many pre-employment screening tests i've done use a static item bank and are very liberal with the time allowed on each question, making it easy for Vision LLMs or bots to beat.
I wanted to see if I could build a fast, client-side engine (JS/SVG) that combats this problem by measuring certain biometric cognitive signatures like "switch cost" (how long it takes for your brain to re-adjust when logical rules change) and "post error-slowing".
To go beyond the simple grading of correct/incorrect, this test dynamically gives you waves of patterns/challenges through a local item bank based on your millisecond response times. If you use an LLM, the constant latencies gets punished with a lower score. If they use a script, the complete lack of natural human variance will be picked up on.
I am currently trying to calibrate a baseline and need high-aptitude users to stress-test it and to provide more data. It also makes it very fast to complete.Everything runs 100% locally in your browser and since I did use AI, I would love your feedback on how the architecture holds up and the technical approach to anti-cheating or anything that comes to mind on this topic.(Optional) When you finish the test, you can press Ctrl + Shift + X on the results page which unlocks a hidden admin console. There you can see more info on your performance and even download a HR-pdf that translate your data into three tailored interview questions. Unfortunately the admin page is in Swedish, but I believe you will get the idea.

## 评论（1/1）

> **mr-boombastic** · 2026-10-24T21:58:20.000Z　
> I should also add that this isn't supposed to replace the traditional g-factor test, but used as a supplement to gain more information about the candidate!

## 导航

- 项目页：[[10-项目/kat-assessment.com_87a738cb]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
