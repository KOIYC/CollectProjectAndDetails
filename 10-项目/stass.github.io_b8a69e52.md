---
type: "project"
title: "Show HN: erXos – a microkernel OS in Erlang based on Genera/Plan 9/QNX ideas"
project_url: "https://stass.github.io/erXos"
first_seen: "2026-11-20T09:45:52+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_stass
  - story_50568169
  - show_hn
lang: "en"
---

# Show HN: erXos – a microkernel OS in Erlang based on Genera/Plan 9/QNX ideas

> [!info] 一句话导读
> What if every Erlang process were an operating-system process? With as much system code and drivers written in Erlang itself. This is something I was pondering …

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://stass.github.io/erXos>
> 首次收录：2026-11-20T09:45:52+08:00
> 来源渠道：HN Show HN
> 标签：author_stass, story_50568169, show_hn
> 最新指标：点赞=3 · 评论=3 · engagement_velocity=3

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-11-20T09:45:52+08:00 | HN Show HN | 点赞=3 · 评论=3 · engagement_velocity=3 | [[20-语料/posts/hn_show/2026-11-20/6b90b8be0e5ac7d4_Show-HN-erXos-–-a-microkernel-OS-in-Erlang-based-o]] |

## 摘要正文

What if every Erlang process were an operating-system process? With as much system code and drivers written in Erlang itself. This is something I was pondering for a while, and finally was able to prototype thanks to AI coding agents.erXos is a capability-based microkernel OS in Erlang: drivers, filesystems, and the network stack are all supervised Erlang processes, same as any app.The kernel itself is Fiasco, in C++, slightly modified for erXos needs. This is an OS I wanted for a long time: an Erlang machine where every BEAM process is a process visible to the OS and scheduler, not something bolted on top.You can try it right now with nothing to install: there is an emulator on the website that boots the whole OS in the browser ARM64 emulator. At the rc prompt, try `ps`, `top`, `ping` or `erl` and write any kind of erlang code. There's a Pi 4 SD image and a QEMU image too. The goal is to build an ultra-reliable microkernel OS with hot code loading and both system and BEAM-based isolation. The latter is one thing that would allow you to run millions of processes on the system, something that would be prohibitive on a microkernel alone due to the context switch overhead. Capabilitie…
