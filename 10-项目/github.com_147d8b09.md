---
type: "project"
title: "Show HN: Minecraft as one C file that runs inside a PDF, a terminal and a Kindle"
project_url: "https://github.com/pragyaangaur/Can-It-Run-Minecraft"
first_seen: "2026-10-27T23:46:32+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_pragyaangaur
  - story_50257980
  - show_hn
lang: "en"
---

# Show HN: Minecraft as one C file that runs inside a PDF, a terminal and a Kindle

> [!info] 一句话导读
> This is basically the doomgeneric idea but applied to Minecraft (its first version rd-132211 that came out on 13 May 2009).It's one freestanding C file with no …

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://github.com/pragyaangaur/Can-It-Run-Minecraft>
> 首次收录：2026-10-27T23:46:32+08:00
> 来源渠道：HN Show HN
> 标签：author_pragyaangaur, story_50257980, show_hn
> 最新指标：点赞=2 · 评论=0 · engagement_velocity=2

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-10-27T23:46:32+08:00 | HN Show HN | 点赞=2 · 评论=0 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-10-27/8aa2306372a7b85a_Show-HN-Minecraft-as-one-C-file-that-runs-inside-a]] |

## 摘要正文

This is basically the doomgeneric idea but applied to Minecraft (its first version rd-132211 that came out on 13 May 2009).It's one freestanding C file with no includes and no memory allocation. It runs in a terminal, over telnet as shared multiplayer, as a 20 KB wasm module, inside a PDF on Chrome and on a bare x86 PC with no OS, and on a jailbroken Kindle Paperwhite.PDFium doesn't have WebAssembly so the C goes to wasm with clang and then binaryen's wasm2js turns it into JavaScript.It also compiles for a Raspberry Pi Pico and Game Boy Advance, but I don't have any of these so haven't tested it. If someone has one would love to hear how it works there. The browser version can be played here directly: https://pragyaangaur.github.io/Can-It-Run-MinecraftUsed Claude for the C and JavaScript code because that's outside my area of work. I picked the targets and tested everything. The Kindle version ended up being an extended project so it's not in the linked repo: https://github.com/pragyaangaur/InkwellAnd if anyone has any crazier places it could run on (someone please do it on a pregnancy test) do try and share it... maybe I could add it to the repo!
