---
type: "project"
title: "Show HN: Jevopt: Making intelligent compiler optimisation decisions with Jev"
project_url: "https://github.com/Ramneet-Singh/jevopt"
first_seen: "2026-09-22T12:53:31+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_ramneet_singh
  - story_49795171
  - show_hn
lang: "en"
---

# Show HN: Jevopt: Making intelligent compiler optimisation decisions with Jev

> [!info] 一句话导读
> Can Jev optimise the size of compiled binaries better than clang -Oz?Turns out it can (sometimes)! Introducing jevopt: making intelligent compiler optimisation …

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://github.com/Ramneet-Singh/jevopt>
> 首次收录：2026-09-22T12:53:31+08:00
> 来源渠道：HN Show HN
> 标签：author_ramneet_singh, story_49795171, show_hn
> 最新指标：点赞=2 · 评论=0 · engagement_velocity=2

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-09-22T12:53:31+08:00 | HN Show HN | 点赞=2 · 评论=0 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-09-22/b1f64c90a4886849_Show-HN-Jevopt-Making-intelligent-compiler-optimis]] |

## 摘要正文

Can Jev optimise the size of compiled binaries better than clang -Oz?Turns out it can (sometimes)! Introducing jevopt: making intelligent compiler optimisation decisions with Jev. I used Jev to make intelligent inlining decisions at each LLVM IR call-site. Here’s why and how I did it.Everywhere I looked, I saw cool Jev demos, so I thought I'd apply it to my area: systems programming and compilers. When optimising binary size (e.g. in embedded systems), choosing whether to inline a function call is tricky, because while it can duplicate code, it can also enable optimisations that ultimately eliminate code!Jevopt uses Jev's "intelligence" to make this choice. At each discretionary call site, Jev sees the current caller/callee LLVM IR, original C/C++ source, build context, and 7 structural facts about the program. It returns one choice: inline or keep out of line.So how well does it work? I evaluated jevopt on all 19 Embench 1.0 programs. Aggregated with geometric mean, the .text in its programs is 7.87% larger than clang -Oz, meaning that jevopt loses in aggregate. However, it sometimes achieves big wins over the mature clang heuristic.E.g., on Statemate, jevopt produces a .text of 2…
