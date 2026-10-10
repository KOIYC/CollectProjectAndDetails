---
type: "project"
title: "Show HN: Axiom: The Functional Systems Langauge"
project_url: "https://axiomlang.software/"
first_seen: "2026-10-10T09:53:50+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_chrispaig3
  - story_50028197
  - show_hn
lang: "en"
---

# Show HN: Axiom: The Functional Systems Langauge

> [!info] 一句话导读
> Skip to content 0.7.8 Why Axiom Tour Performance Status Docs Get started

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://axiomlang.software/>
> 首次收录：2026-10-10T09:53:50+08:00
> 来源渠道：HN Show HN
> 标签：author_chrispaig3, story_50028197, show_hn
> 最新指标：点赞=2 · 评论=0 · engagement_velocity=2

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-10-10T09:53:50+08:00 | HN Show HN | 点赞=2 · 评论=0 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-10-10/58fd0a7ea2eb911c_Show-HN-Axiom-The-Functional-Systems-Langauge]] |

## 摘要正文

Skip to content 0.7.8 Why Axiom Tour Performance Status Docs Get started Axiom 0.7.8 / Open source. Built in Axiom. The functional systems language  High-level thinking.  Native-level control.  Express your ideas with powerful types. Catch missing cases and check effects at compile time. Ship a native binary with no VM or garbage collector.  Build with Axiom Explore the language ↗  For people who care how their code reaches the machine. AX / NATIVE COMPILATION 001  SOURCE / .ax (fn (square x) (* x x))  NATIVE EXECUTABLE Ideas in. Machine code out.  Axiom LLVM IR Native 01 / Expressive by design Types that model your ideas. 02 / Explicit where it counts Effects the compiler checks. 03 / Native from the start LLVM. Straight to the machine.  See it in action  A small program. The whole picture. Write it. Run it. Break it. Watch the compiler catch what changed. shapes.ax — from source to executable PAUSE  shapes.ax 31 : 37  1 ( import IO )  2  3 ( data Shape  4 ( Circle { r : Float } )  5 ( Rect { w : Float, h : Float } )  6 ( Triangle { b : Float, h : Float } )  7 ( Hexagon { side : Float } ) )  8  9 ( :: area ( -> Shape Float ) )  10 ;@axiom:restrict(no-io)  11 ( fn ( area s )  12 ( …
