---
type: "project"
title: "Show HN: Robotics needs better CAD, so I wrote a B-rep kernel and 3,487 tests"
project_url: "https://springcraft-ai.github.io/springrep"
first_seen: "2026-11-19T09:43:31+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_atomarch
  - story_50552140
  - show_hn
lang: "en"
---

# Show HN: Robotics needs better CAD, so I wrote a B-rep kernel and 3,487 tests

> [!info] 一句话导读
> Hey HN, I’m Tony. I’m a co-founder of Springcraft, where we have been doing a lot of CAD modeling for robot parts. Our team kept running into limitations with e…

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://springcraft-ai.github.io/springrep>
> 首次收录：2026-11-19T09:43:31+08:00
> 来源渠道：HN Show HN
> 标签：author_atomarch, story_50552140, show_hn
> 最新指标：点赞=19 · 评论=2 · engagement_velocity=19

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-11-19T09:43:31+08:00 | HN Show HN | 点赞=19 · 评论=2 · engagement_velocity=19 | [[20-语料/posts/hn_show/2026-11-19/be8b77fa2611e7a3_Show-HN-Robotics-needs-better-CAD,-so-I-wrote-a-B]] |

## 摘要正文

Hey HN, I’m Tony. I’m a co-founder of Springcraft, where we have been doing a lot of CAD modeling for robot parts. Our team kept running into limitations with existing kernels, and so I decided to write a new B-rep kernel and a new comprehensive, kernel-agnostic B-rep conformance test suite. Both are available today under MIT licenses.The kernel, springrep, is written in safe Rust with no dependencies. It covers a broad range of our mechanical CAD needs, including advanced fillets, sweeps, lofts, shells, offsets, STEP and exact measurements and queries. Claude Code made it feasible to write this, but it took a lot of time and care to get it right.The test suite, brep-conformance, has 3,487 cases covering the modeling operations common across kernels: booleans, fillets, chamfers, shells, offsets, sweeps, lofts, STEP, and queries with expected answers coming from closed forms and exact geometry. It caught hundreds of bugs, edge cases, and hot spots in springrep that our own tests had missed, and now springrep passes all of it. We’ve also run it on a few popular open-source kernels and anyone can run it on theirs. This is the first version, so there are surely mistakes in the test and…
