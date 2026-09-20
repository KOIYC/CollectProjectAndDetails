---
type: "corpus"
item_id: "dc32bbf735cabd1f"
title: "Show HN: VT Code – open-source terminal coding agent in Rust"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=48332098"
project_url: "https://github.com/vinhnx/VTCode"
author: "vinhnx"
published_at: "2026-05-30T03:07:25Z"
captured_at: "2026-09-21T01:43:39+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-21"
pub_day: "2026-05-30"
tags:
  - 语料
  - hn_show
  - author_vinhnx
  - story_48332098
  - show_hn
metrics: {"points": 16, "comments": 6, "engagement_velocity": 16}
comments_count: 6
comments_total: 6
discovered_via: "hn:show_hn:144d"
---

# Show HN: VT Code – open-source terminal coding agent in Rust

> [!info] 一句话导读
> Show HN: VT Code – open-source terminal coding agent in Rust

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=48332098>
> 指标：点赞=16 · 评论=6 · engagement_velocity=16
> 作者：vinhnx　|　发布：2026-05-30T03:07:25Z
> 项目链接：<https://github.com/vinhnx/VTCode>
> 采集：2026-09-21T01:43:39+08:00　|　id：`dc32bbf735cabd1f`

## 正文

Show HN: VT Code – open-source terminal coding agent in Rust

## 评论（6/6）

> **ninja333** · 2026-05-30T04:37:57.000Z　
> Can I run a local LLM and connect to it?

---

> **afshinmeh** · 2026-05-30T04:48:48.000Z　
> what does "LLM-native code understanding" mean in this context?

---

> **tjb777** · 2026-06-05T12:43:44.000Z　
> thanks for the project, it's great

---

> **vinhnx** · 2026-05-30T05:07:42.000Z　
> Thank you for checking out VT Code! Yes, VT Code supports connecting to local LLMs through two main providers: LM Studio and Ollama. But local LLMs inference is experimenting, as I don't have enough hardware with large VRAM to test it, my main machine is MacBook Pro M4 with just 16 GB Ram. The community always have asked for it and I would love to have sought contributor on these regards. My initial vision is to support open weight and local inference. So LM Studio and Ollama are supported but still have bugs. https://github.com/vinhnx/VTCode/blob/a154162f/docs/provider...Notes: VT Code also supports custom OpenAI-compatible providers through the custom providers' configuration, allowing you to connect to any local LLM server that exposes an OpenAI-compatible API: https://github.com/vinhnx/VTCode/blob/a154162f/docs/config/C...

---

> **vinhnx** · 2026-05-30T05:03:46.000Z　
> Thank you for checking out VT Code! “LLM-native code understanding” refers to VT Code's approach of using LLM as the primary mechanism for semantic code analysis rather than relying solely on traditional static analysis tools. I have tried using ast-grep for structured code parsing understanding as a ground truth before/after the agent executes a code analysis or does a code edit/write operation and code context understanding and symbol analysis. I also tried to use tree-sitter to enhance the user's prompt parser grammar. Example: currently I use tree-sitter bash grammar to check for user input prompts for Unix commands: “run cargo fmt” -> VT Code will detect and understand right away the intent is to run a bash command -> parse and hand it to the harness -> wait for the stdout/err. Then, parse the stdio handle to the LLM as an agent loop. This is to save context and parser roundtrip.This is just my naive implementation, so as “llm-native code understanding,” VT Code will use LLMs to perform deep code understanding across multiple programming languages as a fallback if my enhance `ast-grep` + ripgrep + tree-sitter implementation is failed, but this relies on the model's intelligent. If you follow end-of last year post-training breakthrough (GPT-5.1 and Opus 4.5 era, November 2025), I read somewhere from Anthropic and OpenAI researchers that now the models are smart enough to understanding code with more context. They even have their own internal monologue so they can reason about code grammars and code context by itself. https://github.com/vinhnx/VTCode/blob/a154162f/docs/README.m...Note: I don't have enough understanding describing this cleanly as I learn by doing mostly. However, initially when I designed and built VT Code, I had a vision of using and for AST-enhanced grep code for replacement of std grep. I also use my grep tool, called grep. `perg`). I also wanted to parse source code into concrete syntax trees usable in compilers, interpreters, text editors, and static analyzers. Also, I thought of using LSP but still exp. All this might be overhead for a small open source coding harness, but I love to build, so I thought to myself, why not, just build and learn.

---

> **vinhnx** · 2026-06-05T13:11:34.000Z　
> Thank you for checking out VT Code! I'm happy that people use and like it. Let me know if there are anything I need to make it better.

## 导航

- 项目页：[[10-项目/github.com_679ae14c]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
