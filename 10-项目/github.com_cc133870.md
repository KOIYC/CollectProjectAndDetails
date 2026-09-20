---
type: "project"
title: "Show HN: KaozKit – JavaScript LLM agents on an engine built for microcontrollers"
project_url: "https://github.com/sebastien-burel/KaozKit"
first_seen: "2026-09-20T14:06:25+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_sebastienburel
  - story_49712640
  - show_hn
lang: "en"
---

# Show HN: KaozKit – JavaScript LLM agents on an engine built for microcontrollers

> [!info] 一句话导读
> sebastien-burel/KaozKit

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://github.com/sebastien-burel/KaozKit>
> 首次收录：2026-09-20T14:06:25+08:00
> 来源渠道：HN Show HN
> 标签：author_sebastienburel, story_49712640, show_hn
> 最新指标：点赞=3 · 评论=3 · engagement_velocity=3

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-09-20T09:23:24+08:00 | HN Show HN | 点赞=3 · 评论=3 · engagement_velocity=3 | [[20-语料/posts/hn_show/2026-09-20/3185e869b86a4071_Show-HN-KaozKit-–-JavaScript-LLM-agents-on-an-engi]] |
| 2026-09-20T09:37:15+08:00 | HN Show HN | 点赞=3 · 评论=3 · engagement_velocity=3 | [[20-语料/posts/hn_show/2026-09-20/3185e869b86a4071_Show-HN-KaozKit-–-JavaScript-LLM-agents-on-an-engi]] |
| 2026-09-20T14:06:25+08:00 | HN Show HN | 点赞=3 · 评论=3 · engagement_velocity=3 | [[20-语料/posts/hn_show/2026-09-20/3185e869b86a4071_Show-HN-KaozKit-–-JavaScript-LLM-agents-on-an-engi]] |

## 摘要正文

# sebastien-burel/KaozKit  JavaScript LLM agents on the XS engine, embedded in Swift. Snapshots, resident agents, confined tools.  - Stars: 5 - Forks: 1 - Watchers: 5 - Open issues: 0 - License: Other - Homepage: https://tykaoz.bzh - Default branch: main - Created: 2026-06-17T13:36:15Z  ## Languages  - C - JavaScript - Shell - Swift  ## Topics  - agents - ai - apple-silicon - javascript - llm - llm-agents - macos - mlx - moddable - swift - swift-package - xs  ## Top Contributors  - sebastien-burel (97 contributions) - phoddie (1 contributions)  ---  ## README  # KaozKit  **Autonomous LLM agents, written in JavaScript, running inside your Swift app.**  KaozKit embeds the XS engine (Moddable) in a Swift package. An agent is a small JS module — `export function run(input)` — that drives a language model, calls tools, and reads/writes memory. The JS heap can be **snapshotted to disk and restored in a fresh process**, so resident agents survive app restarts with their full state.  Platform Swift License  ```js // demo/weather.js — runs inside the engine export async function run(input) {   const reply = await host.llm.chat(     [{ role: "user", content: input.question }],     { tools: […
