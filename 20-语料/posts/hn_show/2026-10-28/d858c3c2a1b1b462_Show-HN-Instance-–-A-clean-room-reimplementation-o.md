---
type: "corpus"
item_id: "d858c3c2a1b1b462"
title: "Show HN: Instance – A clean-room reimplementation of GameMaker 8.1 in Rust"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50261794"
project_url: "https://github.com/groverburger/instance"
author: "__grob"
published_at: "2026-10-27T16:38:47Z"
captured_at: "2026-10-28T09:39:16+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-10-28"
pub_day: "2026-10-27"
tags:
  - 语料
  - hn_show
  - author___grob
  - story_50261794
  - show_hn
metrics: {"points": 2, "comments": 0, "engagement_velocity": 2}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:3d"
---

# Show HN: Instance – A clean-room reimplementation of GameMaker 8.1 in Rust

> [!info] 一句话导读
> I used GameMaker 8.1 a ton in late elementary and middle school, and GML was the first programming language I wrote. I still think it's a fun engine to use beca…

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50261794>
> 指标：点赞=2 · 评论=0 · engagement_velocity=2
> 作者：__grob　|　发布：2026-10-27T16:38:47Z
> 项目链接：<https://github.com/groverburger/instance>
> 采集：2026-10-28T09:39:16+08:00　|　id：`d858c3c2a1b1b462`

## 正文

I used GameMaker 8.1 a ton in late elementary and middle school, and GML was the first programming language I wrote. I still think it's a fun engine to use because it has so many batteries included. So I built an open-source reimplementation of it in Rust which I'm calling Instance. It opens existing .gmk and .gm81 projects and runs them on Windows, macOS and in the browser, with a more efficient GML interpreter than the original GameMaker.You can try the IDE here in your browser: https://groverburger.github.io/instance/. It comes with three example games, including Spelunky Classic built from Derek Yu's released source shared under its permissive license. Just change something and press Run to see your edits in action.Old GM games depend on a lot of quirks such as the order events run in, the exact random number generator, how sound_isplaying lags behind the audio. I wrote up the behavior as specs from the documentation, the file formats and black-box tests against the real program, then implemented it from those specs. No proprietary code was disassembled or decompiled. CLEANROOM.md describes the process.It covers most of almost all of 8.1. All the resource editors, GML and drag-and-drop actions, d3d, particles, surfaces, MIDI, mplay multiplayer and DLL calls. It can also export a game as a standalone executable or a single HTML file. Projects can be saved as folders of plain text and PNG files for git.I wrote most of the code with Claude Opus 5.5 over about three weeks. Claude banged out a pretty good reimplementation in a morning, but as always the last 20% took 80% of the work. GameMaker also turns out to work surprisingly well with LLMs. GML is small and simple, and a whole game fits in one project file.I'm happy to answer any questions!Code: https://github.com/groverburger/instance

## 关联链接

- https://groverburger.github.io/instance/.

## 导航

- 项目页：[[10-项目/github.com_d7c40565]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
