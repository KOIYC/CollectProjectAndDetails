---
type: "corpus"
item_id: "ce6eb6ae18e358e1"
title: "Show HN: Cppbolt – A lightweight C++ to WebAssembly compiler written in Rust"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50369009"
project_url: "https://github.com/AJTimePyro/cppbolt"
author: "ajtimepyro"
published_at: "2026-11-04T17:45:40Z"
captured_at: "2026-11-05T11:21:45+08:00"
lang: "en"
kind: "post"
topic: "开发者工具"
shard: "2026-11-05"
pub_day: "2026-11-04"
tags:
  - 语料
  - hn_show
  - author_ajtimepyro
  - story_50369009
  - show_hn
metrics: {"points": 3, "comments": 1, "engagement_velocity": 3}
comments_count: 1
comments_total: 1
discovered_via: "hn:show_hn:3d"
---

# Show HN: Cppbolt – A lightweight C++ to WebAssembly compiler written in Rust

> [!info] 一句话导读
> Hey HN! I've been working on cppbolt, a lightweight C++ to WebAssembly compiler written in Rust.The idea was to build something that can compile and run C++ dir…

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50369009>
> 指标：点赞=3 · 评论=1 · engagement_velocity=3
> 作者：ajtimepyro　|　发布：2026-11-04T17:45:40Z
> 项目链接：<https://github.com/AJTimePyro/cppbolt>
> 采集：2026-11-05T11:21:45+08:00　|　id：`ce6eb6ae18e358e1`

## 正文

Hey HN! I've been working on cppbolt, a lightweight C++ to WebAssembly compiler written in Rust.The idea was to build something that can compile and run C++ directly in the browser without downloading a massive LLVM/Clang toolchain.Unlike projects that bundle LLVM/Clang and can require 100+ MB of compiler assets, cppbolt's compiler payload is around 1 MB. It compiles a supported subset of C++17 directly to standard WebAssembly binaries.Some things it supports:
- Classes, inheritance, virtual functions and operator overloading
- Templates and a subset of the C++ standard library
- Pointers, references, arrays and dynamic memory
- Lambdas, structured bindings and range-based loopsIt comes with a browser playground, CLI and npm package.A few caveats: this is still a work in progress, it doesn't implement the full C++17 standard, and it might not work as expected with certain C++ programs. I'm particularly interested in feedback on the compiler architecture, language support and potential use cases and also interested in connecting with someone who might want to use it in their application.Try it out:
- Playground: https://ajtimepyro.is-a.dev/cppbolt/
- Docs: https://ajtimepyro.is-a.dev/cppbolt/book/
- GitHub: https://github.com/AJTimePyro/cppbolt
- npm: https://www.npmjs.com/package/cppboltWould love to hear what you think, especially from people who've worked on compilers or WebAssembly.

## 评论（1/1）

> **adamkumpf** · 2026-11-04T18:51:52.000Z　
> WebAssembly really is the future of cross-platform apps. With so many existing C++ projects and optimized code, being able to convert them is highly useful.Just curious, have you tried to open a cpp project and use a tool like Claude to just convert it to WebAssembly and compare? That would make a great data point if you can show that cppbolt can do it much better/faster.

## 关联链接

- https://ajtimepyro.is-a.dev/cppbolt/
- https://ajtimepyro.is-a.dev/cppbolt/book/
- https://www.npmjs.com/package/cppboltWould

## 导航

- 项目页：[[10-项目/github.com_b24e1447]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`开发者工具`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
