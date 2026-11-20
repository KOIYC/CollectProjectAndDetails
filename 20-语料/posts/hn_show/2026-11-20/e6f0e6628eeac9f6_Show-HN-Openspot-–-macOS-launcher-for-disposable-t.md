---
type: "corpus"
item_id: "e6f0e6628eeac9f6"
title: "Show HN: Openspot – macOS launcher for disposable tools"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50560882"
project_url: "https://github.com/celishq/openspot"
author: "tniich"
published_at: "2026-11-19T14:51:21Z"
captured_at: "2026-11-20T09:45:52+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-11-20"
pub_day: "2026-11-19"
tags:
  - 语料
  - hn_show
  - author_tniich
  - story_50560882
  - show_hn
metrics: {"points": 5, "comments": 2, "engagement_velocity": 5}
comments_count: 2
comments_total: 2
discovered_via: "hn:show_hn:3d"
---

# Show HN: Openspot – macOS launcher for disposable tools

> [!info] 一句话导读
> Hi HN! We're Tony, Kolom and Anastasiia, a small team from Ukraine.Today we are open-sourcing Openspot, our research project on using generative UI in day-to-da…

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50560882>
> 指标：点赞=5 · 评论=2 · engagement_velocity=5
> 作者：tniich　|　发布：2026-11-19T14:51:21Z
> 项目链接：<https://github.com/celishq/openspot>
> 采集：2026-11-20T09:45:52+08:00　|　id：`e6f0e6628eeac9f6`

## 正文

Hi HN! We're Tony, Kolom and Anastasiia, a small team from Ukraine.Today we are open-sourcing Openspot, our research project on using generative UI in day-to-day work.The idea is simple: generate a tool (spot) for your current task using coding agent, and keep it if you like it or remove it after use if you don't. We are using Openspot daily and really enjoying the possibilities it unlocks. Some examples of spots:- caffeinate, which allows the Mac to work with the lid closed- local file and screenshot search in natural language using EmbeddingGemma 2- draw on screen during calls or before screenshots- AI agents monitoring- AirDrop, but over the network (using iroh)We built it because of two things:1. Over the past year, we (and almost every designer and engineer we know) have started making small tools using coding agents. But the DX for macOS applications is very frustrating even for coders, and you have to pay for a developer account to share them.2. And we kind of miss the days of custom Winamp skins and Twitter clients. That's why every part of Openspot is customizable, so anyone can give it their own look and feel.This is a very early stage. The code is MIT-licensed, and the core will remain free forever. We're sticking to macOS 26+ for now (because of Liquid Glass).Ask us anything, or roast it. Any feedback is very appreciated.

## 评论（2/2）

> **tniich** · 2026-11-19T14:51:31.000Z　
> A few words about the architecture.The architecture is simple and very Unix-y: it's basically the macOS API as a CLI. Any executable can talk to it over stdin/stdout and draw native UI using a plain-text protocol (or something fancier using custom SwiftUI views). Permissions, logs and all the tools live in a single place, and each tool can be shared via one signed file.Every shared spot is signed with Nostr keys, so you can always verify who made it. We chose Nostr because we don't want to control what people are allowed to share.All the spots are run in yolo mode by default, so they get the same permissions as Openspot, but you can always ask your agent to verify the code if necessary. We plan to add a sandboxing mechanism in the near future.

---

> **charly_builds** · 2026-11-19T19:52:46.000Z　
> Like it - nifty little thing

## 导航

- 项目页：[[10-项目/github.com_784008a8]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
