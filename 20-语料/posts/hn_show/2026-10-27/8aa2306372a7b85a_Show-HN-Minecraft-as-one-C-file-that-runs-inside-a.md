---
type: "corpus"
item_id: "8aa2306372a7b85a"
title: "Show HN: Minecraft as one C file that runs inside a PDF, a terminal and a Kindle"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50257980"
project_url: "https://github.com/pragyaangaur/Can-It-Run-Minecraft"
author: "pragyaangaur"
published_at: "2026-10-27T12:13:35Z"
captured_at: "2026-10-27T23:46:32+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-10-27"
pub_day: "2026-10-27"
tags:
  - 语料
  - hn_show
  - author_pragyaangaur
  - story_50257980
  - show_hn
metrics: {"points": 2, "comments": 0, "engagement_velocity": 2}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:3d"
---

# Show HN: Minecraft as one C file that runs inside a PDF, a terminal and a Kindle

> [!info] 一句话导读
> This is basically the doomgeneric idea but applied to Minecraft (its first version rd-132211 that came out on 13 May 2009).It's one freestanding C file with no …

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50257980>
> 指标：点赞=2 · 评论=0 · engagement_velocity=2
> 作者：pragyaangaur　|　发布：2026-10-27T12:13:35Z
> 项目链接：<https://github.com/pragyaangaur/Can-It-Run-Minecraft>
> 采集：2026-10-27T23:46:32+08:00　|　id：`8aa2306372a7b85a`

## 正文

This is basically the doomgeneric idea but applied to Minecraft (its first version rd-132211 that came out on 13 May 2009).It's one freestanding C file with no includes and no memory allocation. It runs in a terminal, over telnet as shared multiplayer, as a 20 KB wasm module, inside a PDF on Chrome and on a bare x86 PC with no OS, and on a jailbroken Kindle Paperwhite.PDFium doesn't have WebAssembly so the C goes to wasm with clang and then binaryen's wasm2js turns it into JavaScript.It also compiles for a Raspberry Pi Pico and Game Boy Advance, but I don't have any of these so haven't tested it. If someone has one would love to hear how it works there. The browser version can be played here directly: https://pragyaangaur.github.io/Can-It-Run-MinecraftUsed Claude for the C and JavaScript code because that's outside my area of work. I picked the targets and tested everything. The Kindle version ended up being an extended project so it's not in the linked repo: https://github.com/pragyaangaur/InkwellAnd if anyone has any crazier places it could run on (someone please do it on a pregnancy test) do try and share it... maybe I could add it to the repo!

## 关联链接

- https://github.com/pragyaangaur/InkwellAnd
- https://pragyaangaur.github.io/Can-It-Run-MinecraftUsed

## 导航

- 项目页：[[10-项目/github.com_147d8b09]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
