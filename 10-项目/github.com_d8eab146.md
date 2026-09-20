---
type: "project"
title: "Show HN: Macros with a Behringer FCB1010 MIDI Pedalboard in macOS"
project_url: "https://github.com/JamesRyanATX/fcbnerd"
first_seen: "2026-09-20T09:38:53+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_fretlessjazz
  - story_49705442
  - show_hn
lang: "en"
---

# Show HN: Macros with a Behringer FCB1010 MIDI Pedalboard in macOS

> [!info] 一句话导读
> JamesRyanATX/fcbnerd

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://github.com/JamesRyanATX/fcbnerd>
> 首次收录：2026-09-20T09:38:53+08:00
> 来源渠道：HN Show HN
> 标签：author_fretlessjazz, story_49705442, show_hn
> 最新指标：点赞=85 · 评论=21 · engagement_velocity=85

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-09-20T09:23:24+08:00 | HN Show HN | 点赞=85 · 评论=21 · engagement_velocity=85 | [[20-语料/posts/hn_show/2026-09-20/b620df7d166b2bc1_Show-HN-Macros-with-a-Behringer-FCB1010-MIDI-Pedal]] |
| 2026-09-20T09:37:33+08:00 | HN Show HN | 点赞=85 · 评论=21 · engagement_velocity=85 | [[20-语料/posts/hn_show/2026-09-20/b620df7d166b2bc1_Show-HN-Macros-with-a-Behringer-FCB1010-MIDI-Pedal]] |
| 2026-09-20T09:38:53+08:00 | HN Show HN | 点赞=85 · 评论=21 · engagement_velocity=85 | [[20-语料/posts/hn_show/2026-09-20/b620df7d166b2bc1_Show-HN-Macros-with-a-Behringer-FCB1010-MIDI-Pedal]] |

## 摘要正文

# JamesRyanATX/fcbnerd  Do things with a Behringer FCB1010 MIDI pedalboard in MacOS  - Stars: 62 - Forks: 1 - Watchers: 62 - Open issues: 0 - License: MIT License - Default branch: main - Created: 2026-09-14T21:33:23Z  ## Languages  - Swift  ## Topics  - fcb1010 - macos - midi  ## Top Contributors  - JamesRyanATX (13 contributions)  ---  ## README  # fcbnerd  Cartoon: a developer leans back from a wide monitor with a coffee, stomping a footswitch on a MIDI pedalboard while a dog sleeps nearby.  Use a MIDI foot controller as an extra keyboard for your Mac. `fcbnerd` connects to your MIDI sources and either runs a shell command when a footswitch or pedal sends a message you've bound, or prints one JSON object per line for every message so another program can decide what a stomp means.  ```console $ fcbnerd -q --bind '1:20:127=open ~/Downloads' --bind 'pc:1:0=say hello' ```  Or stream everything for another program to handle:  ```console $ fcbnerd {"type":"connected","source":"UM-ONE","time":"2026-09-14T20:01:00.120Z"} {"type":"pc","channel":1,"program":0,"source":"UM-ONE","time":"2026-09-14T20:01:02.345Z"} {"type":"cc","channel":1,"controller":30,"value":84,"source":"UM-ONE","time":"…
