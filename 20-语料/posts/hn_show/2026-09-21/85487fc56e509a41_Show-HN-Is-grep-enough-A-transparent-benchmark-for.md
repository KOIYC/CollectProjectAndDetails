---
type: "corpus"
item_id: "85487fc56e509a41"
title: "Show HN: Is grep enough? A transparent benchmark for agentic code navigation"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=48731519"
project_url: "https://entelligentsia.github.io/is-grep-enough"
author: "bonigv"
published_at: "2026-06-30T12:06:46Z"
captured_at: "2026-09-21T01:45:03+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-21"
pub_day: "2026-06-30"
tags:
  - 语料
  - hn_show
  - author_bonigv
  - story_48731519
  - show_hn
metrics: {"points": 4, "comments": 2, "engagement_velocity": 4}
comments_count: 2
comments_total: 2
discovered_via: "hn:show_hn:113d"
---

# Show HN: Is grep enough? A transparent benchmark for agentic code navigation

> [!info] 一句话导读
> Felt LSP Servers were too complex. Bash tools alone too brutish. Wanted to see what if it is a tree-sitter as a firstclass tool. Ran a bench over 10 large codeb…

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=48731519>
> 指标：点赞=4 · 评论=2 · engagement_velocity=4
> 作者：bonigv　|　发布：2026-06-30T12:06:46Z
> 项目链接：<https://entelligentsia.github.io/is-grep-enough>
> 采集：2026-09-21T01:45:03+08:00　|　id：`85487fc56e509a41`

## 正文

Felt LSP Servers were too complex. Bash tools alone too brutish. Wanted to see what if it is a tree-sitter as a firstclass tool. Ran a bench over 10 large codebases [bitcoin, django, rails, redis,...] at 5 levels of exploration complexity each. That 150 context isolated runs over the last few days. Sharing the results with full tarnsparency. All scripts, docker image scripts, all transcrpts. There is a TL;DR; but I hope you don't leave it at that. Has been quite a bit of work. Repo links are on the site.

## 评论（2/2）

> **6thbit** · 2026-06-30T12:20:19.000Z　
> This is nicely put together, it does make sense that lsps help more as complexity grows because makes navigation across symbols easier.I hope someone with a large budget can reproduce these with latest Opus/gpt.My gut feeling is that higher reasoning models tend to use grep more effectively. But intuitively lsp should still win there.

---

> **bonigv** · 2026-06-30T12:32:21.000Z　
> You are absolutely right about what we feel intuitively - LSPs should beat the shit out of the competition. But surprisingly it did not. Across 10 different LSP servers, across 5 different levels of prompt complexity it did not. Mind you, I painstakingly warmed up the LSP servers that needed it warmed. Some liked it cold and it fared equally non impressively. The pattern I saw was, LLMs (sonnet w.6 with cc) was very clever to use whatever it had to get to a verifiable answer. It could do it just with bash for sure. But as the prompt complexity grew the cost also rose.Treesitter is sitting in a sweet spot here. a vrainy LLM can find the shortest path with high quality with treesitter and a few bash calls.

## 导航

- 项目页：[[10-项目/entelligentsia.github.io_ef54b241]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
