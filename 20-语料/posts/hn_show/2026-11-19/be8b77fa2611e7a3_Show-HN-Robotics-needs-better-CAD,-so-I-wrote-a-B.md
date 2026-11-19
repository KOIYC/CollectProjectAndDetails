---
type: "corpus"
item_id: "be8b77fa2611e7a3"
title: "Show HN: Robotics needs better CAD, so I wrote a B-rep kernel and 3,487 tests"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50552140"
project_url: "https://springcraft-ai.github.io/springrep"
author: "atomarch"
published_at: "2026-11-18T21:08:47Z"
captured_at: "2026-11-19T09:43:31+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-11-19"
pub_day: "2026-11-18"
tags:
  - 语料
  - hn_show
  - author_atomarch
  - story_50552140
  - show_hn
metrics: {"points": 19, "comments": 2, "engagement_velocity": 19}
comments_count: 2
comments_total: 2
discovered_via: "hn:show_hn:3d"
---

# Show HN: Robotics needs better CAD, so I wrote a B-rep kernel and 3,487 tests

> [!info] 一句话导读
> Hey HN, I’m Tony. I’m a co-founder of Springcraft, where we have been doing a lot of CAD modeling for robot parts. Our team kept running into limitations with e…

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50552140>
> 指标：点赞=19 · 评论=2 · engagement_velocity=19
> 作者：atomarch　|　发布：2026-11-18T21:08:47Z
> 项目链接：<https://springcraft-ai.github.io/springrep>
> 采集：2026-11-19T09:43:31+08:00　|　id：`be8b77fa2611e7a3`

## 正文

Hey HN, I’m Tony. I’m a co-founder of Springcraft, where we have been doing a lot of CAD modeling for robot parts. Our team kept running into limitations with existing kernels, and so I decided to write a new B-rep kernel and a new comprehensive, kernel-agnostic B-rep conformance test suite. Both are available today under MIT licenses.The kernel, springrep, is written in safe Rust with no dependencies. It covers a broad range of our mechanical CAD needs, including advanced fillets, sweeps, lofts, shells, offsets, STEP and exact measurements and queries. Claude Code made it feasible to write this, but it took a lot of time and care to get it right.The test suite, brep-conformance, has 3,487 cases covering the modeling operations common across kernels: booleans, fillets, chamfers, shells, offsets, sweeps, lofts, STEP, and queries with expected answers coming from closed forms and exact geometry. It caught hundreds of bugs, edge cases, and hot spots in springrep that our own tests had missed, and now springrep passes all of it. We’ve also run it on a few popular open-source kernels and anyone can run it on theirs. This is the first version, so there are surely mistakes in the test and adapters. Corrections, pull requests, and new kernels are welcome.kernel: https://github.com/springcraft-ai/springrep
conformance suite: https://springcraft-ai.github.io/brep-conformance/

## 评论（2/2）

> **dofm** · 2026-11-18T22:45:45.000Z　
> Now this is a great application of an LLM.I'm sure you still have loads to solve and a lot of quite human decisions to make (because bRep is one thing; contemporary CAD 'default solutions' strike me as likely to be full of human compromises), but I can see that having an LLM on the team to help with the maths must help.Best of luck with it :-)

---

> **atomarch** · 2026-11-18T23:10:20.000Z　
> Thanks! This has been an exciting project so far, and lots more to come.

## 关联链接

- https://github.com/springcraft-ai/springrep
- https://springcraft-ai.github.io/brep-conformance/

## 导航

- 项目页：[[10-项目/springcraft-ai.github.io_45afd8c4]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
