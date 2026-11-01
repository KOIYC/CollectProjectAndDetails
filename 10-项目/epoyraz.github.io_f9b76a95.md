---
type: "project"
title: "Show HN: NES Contra (1987) port (ASM –> C and then C –> WebAssembly)"
project_url: "https://epoyraz.github.io/nes-contra-us"
first_seen: "2026-11-01T09:38:09+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_tevlon
  - story_50319169
  - show_hn
  - front_page
lang: "en"
---

# Show HN: NES Contra (1987) port (ASM –> C and then C –> WebAssembly)

> [!info] 一句话导读
> Based on vermiceli's annotated disassembly of Contra: https://github.com/vermiceli/nes-contra-us. Thanks for the great work.I ported it in two steps. First to C…

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://epoyraz.github.io/nes-contra-us>
> 首次收录：2026-11-01T09:38:09+08:00
> 来源渠道：HN Show HN
> 标签：author_tevlon, story_50319169, show_hn, front_page
> 最新指标：点赞=50 · 评论=31 · engagement_velocity=50

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-11-01T09:38:09+08:00 | HN Show HN | 点赞=50 · 评论=31 · engagement_velocity=50 | [[20-语料/posts/hn_show/2026-11-01/4c65a4f2eeb6e95c_Show-HN-NES-Contra-(1987)-port-(ASM-–-C-and-then-C]] |

## 摘要正文

Based on vermiceli's annotated disassembly of Contra: https://github.com/vermiceli/nes-contra-us. Thanks for the great work.I ported it in two steps. First to C: the game logic is translated routine by routine from the 6502 assembly, and checked frame by frame against the original in the Mesen emulator. Then the C code to WebAssembly so it runs in the browser.The cherry on top: online multiplayer, so two players can play co-op over the internet.Source: https://github.com/epoyraz/nes-contra-us
