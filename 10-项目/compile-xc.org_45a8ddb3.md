---
type: "project"
title: "Show HN: An ObjC-like compiler for Mac ARM, x86_64(Linux, Win), WASM, & others"
project_url: "https://compile-xc.org/"
first_seen: "2026-09-20T14:03:53+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_spacedcowboy
  - story_49730393
  - show_hn
lang: "en"
---

# Show HN: An ObjC-like compiler for Mac ARM, x86_64(Linux, Win), WASM, & others

> [!info] 一句话导读
> Show HN: An ObjC-like compiler for Mac ARM, x86_64(Linux, Win), WASM, & others

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://compile-xc.org/>
> 首次收录：2026-09-20T14:03:53+08:00
> 来源渠道：HN Show HN
> 标签：author_spacedcowboy, story_49730393, show_hn
> 最新指标：点赞=2 · 评论=10 · engagement_velocity=2

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-09-20T09:23:24+08:00 | HN Show HN | 点赞=2 · 评论=10 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-09-20/dc5bdb60d33b1f7f_Show-HN-An-ObjC-like-compiler-for-Mac-ARM,-x86_64(]] |
| 2026-09-20T09:36:59+08:00 | HN Show HN | 点赞=2 · 评论=10 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-09-20/dc5bdb60d33b1f7f_Show-HN-An-ObjC-like-compiler-for-Mac-ARM,-x86_64(]] |
| 2026-09-20T09:40:15+08:00 | HN Show HN | 点赞=2 · 评论=10 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-09-20/dc5bdb60d33b1f7f_Show-HN-An-ObjC-like-compiler-for-Mac-ARM,-x86_64(]] |
| 2026-09-20T09:41:43+08:00 | HN Show HN | 点赞=2 · 评论=10 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-09-20/dc5bdb60d33b1f7f_Show-HN-An-ObjC-like-compiler-for-Mac-ARM,-x86_64(]] |
| 2026-09-20T14:03:53+08:00 | HN Show HN | 点赞=2 · 评论=10 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-09-20/dc5bdb60d33b1f7f_Show-HN-An-ObjC-like-compiler-for-Mac-ARM,-x86_64(]] |

## 摘要正文

Show HN: An ObjC-like compiler for Mac ARM, x86_64(Linux, Win), WASM, & others | Hacker News  Show HN: An ObjC-like compiler for Mac ARM, x86_64(Linux, Win), WASM, & others  1 point by spacedcowboy 22 minutes ago | hide | past | favorite | discuss  Hi folks,  So this is my announcement of a compiler[1] I've been working on for about 6 months now (so yes, to get the obvious out of the way early, this was written with Claude code).  The compiler is called 'xc', stands for 'cross-C' or 'extended-C' or whatever you want, really. It's fairly similar to Objective-C in style (without the [] brackets), and in fact the first version of the language was written in ObjC.  It works on Mac M-series, Windows, and Linux - and any of these hosts can create binaries for any of {Mac M-series, Windows, Linux, Android, iOS, WASM, Arm9 (Zynq), m68k and even 6502}.  Building the compiler needs host-tools to bootstrap everything, either GNUStep on Linux, or a Mac with Xcode. Once built, however, the system is entirely self-contained, and you don't need any platform tools. I have a binary running on my iPhone which was compiled and signed on a Linux box... The suite ships with 5 host-specific assemblers, …
