---
type: "project"
title: "Show HN: Build Windows C++ programs on Linux"
project_url: "https://github.com/abidanBrito/build-windows-on-linux"
first_seen: "2026-11-19T09:43:31+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_abidanbrito
  - story_50553490
  - show_hn
lang: "en"
---

# Show HN: Build Windows C++ programs on Linux

> [!info] 一句话导读
> abidanBrito/build-windows-on-linux

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://github.com/abidanBrito/build-windows-on-linux>
> 首次收录：2026-11-19T09:43:31+08:00
> 来源渠道：HN Show HN
> 标签：author_abidanbrito, story_50553490, show_hn
> 最新指标：点赞=3 · 评论=0 · engagement_velocity=3

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-11-19T09:43:31+08:00 | HN Show HN | 点赞=3 · 评论=0 · engagement_velocity=3 | [[20-语料/posts/hn_show/2026-11-19/970addc55fd73862_Show-HN-Build-Windows-C++-programs-on-Linux]] |

## 摘要正文

# abidanBrito/build-windows-on-linux  Cross-compiling C++ Windows executables from Linux.  - Stars: 0 - Forks: 0 - Watchers: 0 - Open issues: 0 - License: MIT License - Default branch: main - Created: 2026-11-17T17:45:00Z  ## Languages  - C++ - CMake  ## Topics  - cross-compilation - llvm-mingw - mingw-w64 - wine - xwin  ## Top Contributors  - abidanBrito (22 contributions)  ---  ## README  # build-windows-on-linux  Build C++23 CMake 3.25+ License: MIT  Cross-compiling C++ Windows programs from Linux with four different toolchains.  There are two sample programs, tested under Wine:  - `hello`: a console hello world, using `std::println`. - `window`: a basic Win32 GUI window.  ## Toolchains  | Preset | Compiler | C++ library | SDK / CRT | ABI | |-----------------|------------|-------------|---------------------|-------| | `mingw-clang` | host clang | libstdc++ | mingw-w64 (UCRT) | GNU | | `mingw-gcc` | GCC | libstdc++ | mingw-w64 (UCRT) | GNU | | `llvm-mingw` | clang | libc++ | mingw-w64 (UCRT) | GNU | | `xwin-clang-cl` | clang-cl | MSVC STL | Microsoft SDK + CRT | MSVC |  All of them link statically, so that no extra DLLs (or `WINEPATH` shenanigans) are needed. In theory, `xwin-cla…
