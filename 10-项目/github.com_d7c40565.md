---
type: "project"
title: "Show HN: Instance – A clean-room reimplementation of GameMaker 8.1 in Rust"
project_url: "https://github.com/groverburger/instance"
first_seen: "2026-10-28T09:39:16+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author___grob
  - story_50261794
  - show_hn
lang: "en"
---

# Show HN: Instance – A clean-room reimplementation of GameMaker 8.1 in Rust

> [!info] 一句话导读
> I used GameMaker 8.1 a ton in late elementary and middle school, and GML was the first programming language I wrote. I still think it's a fun engine to use beca…

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://github.com/groverburger/instance>
> 首次收录：2026-10-28T09:39:16+08:00
> 来源渠道：HN Show HN
> 标签：author___grob, story_50261794, show_hn
> 最新指标：点赞=2 · 评论=0 · engagement_velocity=2

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-10-28T09:39:16+08:00 | HN Show HN | 点赞=2 · 评论=0 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-10-28/d858c3c2a1b1b462_Show-HN-Instance-–-A-clean-room-reimplementation-o]] |

## 摘要正文

I used GameMaker 8.1 a ton in late elementary and middle school, and GML was the first programming language I wrote. I still think it's a fun engine to use because it has so many batteries included. So I built an open-source reimplementation of it in Rust which I'm calling Instance. It opens existing .gmk and .gm81 projects and runs them on Windows, macOS and in the browser, with a more efficient GML interpreter than the original GameMaker.You can try the IDE here in your browser: https://groverburger.github.io/instance/. It comes with three example games, including Spelunky Classic built from Derek Yu's released source shared under its permissive license. Just change something and press Run to see your edits in action.Old GM games depend on a lot of quirks such as the order events run in, the exact random number generator, how sound_isplaying lags behind the audio. I wrote up the behavior as specs from the documentation, the file formats and black-box tests against the real program, then implemented it from those specs. No proprietary code was disassembled or decompiled. CLEANROOM.md describes the process.It covers most of almost all of 8.1. All the resource editors, GML and drag-…
