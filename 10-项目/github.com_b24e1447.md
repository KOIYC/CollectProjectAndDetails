---
type: "project"
title: "Show HN: Cppbolt – A lightweight C++ to WebAssembly compiler written in Rust"
project_url: "https://github.com/AJTimePyro/cppbolt"
first_seen: "2026-11-05T11:21:45+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_ajtimepyro
  - story_50369009
  - show_hn
lang: "en"
---

# Show HN: Cppbolt – A lightweight C++ to WebAssembly compiler written in Rust

> [!info] 一句话导读
> Hey HN! I've been working on cppbolt, a lightweight C++ to WebAssembly compiler written in Rust.The idea was to build something that can compile and run C++ dir…

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://github.com/AJTimePyro/cppbolt>
> 首次收录：2026-11-05T11:21:45+08:00
> 来源渠道：HN Show HN
> 标签：author_ajtimepyro, story_50369009, show_hn
> 最新指标：点赞=3 · 评论=1 · engagement_velocity=3

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-11-05T11:21:45+08:00 | HN Show HN | 点赞=3 · 评论=1 · engagement_velocity=3 | [[20-语料/posts/hn_show/2026-11-05/ce6eb6ae18e358e1_Show-HN-Cppbolt-–-A-lightweight-C++-to-WebAssembly]] |

## 摘要正文

Hey HN! I've been working on cppbolt, a lightweight C++ to WebAssembly compiler written in Rust.The idea was to build something that can compile and run C++ directly in the browser without downloading a massive LLVM/Clang toolchain.Unlike projects that bundle LLVM/Clang and can require 100+ MB of compiler assets, cppbolt's compiler payload is around 1 MB. It compiles a supported subset of C++17 directly to standard WebAssembly binaries.Some things it supports: - Classes, inheritance, virtual functions and operator overloading - Templates and a subset of the C++ standard library - Pointers, references, arrays and dynamic memory - Lambdas, structured bindings and range-based loopsIt comes with a browser playground, CLI and npm package.A few caveats: this is still a work in progress, it doesn't implement the full C++17 standard, and it might not work as expected with certain C++ programs. I'm particularly interested in feedback on the compiler architecture, language support and potential use cases and also interested in connecting with someone who might want to use it in their application.Try it out: - Playground: https://ajtimepyro.is-a.dev/cppbolt/ - Docs: https://ajtimepyro.is-a.de…
