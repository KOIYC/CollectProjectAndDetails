---
type: "corpus"
item_id: "2e9c7de35f6f5d6e"
title: "Show HN: reqlan – a language for requirement graphs next to the code"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49704498"
project_url: "https://reqlan.com/"
author: "littletuna4"
published_at: "2026-09-14T21:40:28Z"
captured_at: "2026-09-20T09:37:34+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-20"
pub_day: "2026-09-14"
tags:
  - 语料
  - hn_show
  - author_littletuna4
  - story_49704498
  - show_hn
metrics: {"points": 2, "comments": 0, "engagement_velocity": 2}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:90d"
---

# Show HN: reqlan – a language for requirement graphs next to the code

> [!info] 一句话导读
> semantic *engineering* toolset

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49704498>
> 指标：点赞=2 · 评论=0 · engagement_velocity=2
> 作者：littletuna4　|　发布：2026-09-14T21:40:28Z
> 项目链接：<https://reqlan.com/>
> 采集：2026-09-20T09:37:34+08:00　|　id：`2e9c7de35f6f5d6e`

## 正文

reqlan

```
reqlan {
    semantic *engineering* toolset
}
```

Build high-quality, verifiable systems quickly by describing the parts that matter and how they relate

- less input tokens, better output tokens
- integrate your system with your actual intent
- demand excellence from your clanker, with the right atomic specification
- vibecode without the constant doubt
- tightly control the scoping of your context, with the best of a file system hierarchy and the best of a knowledge graph
- shorter prompts, better agentic search, less rework and more focus
- make your precise intent explicit, leave implicit details latent
- make your intent compilable
- core implemented in rust, so you know it's fast and reliable
- integrate compliance, testing, functional requirements, non-functional requirements, and more into your system
- build docs that resist drift, and store the things you actually care about

## What is reqlan?

A token efficient data format for writing functional requirements - supporting personal knowledge management inspired naming linking and tagging, plus an editor extension and a CLI on the same index. Engineers who wrangle complexity use it so they can focus on describing their highest-alpha ideas.

Language

`.rq` files: a name, a short body, links to ideas, code, and tests.

Why You write the alpha. Everything else points back to it. No more hunting the “real” rule in a six-month-old chat.

## How are ideas actually written

reqlan is super easy to learn, here's a few self explanatory examples.

one-liner

```
one_line_idea an idea is prose after an identifying name
```

block

```
block_idea {
    A name followed by curly braces holds a longer body and optional attributes.
    The first unmarked text is the main description.
}
```

links & attributes

```
reference_target a named idea other ideas can point at

links_and_attributes {
    Bracket refs like [reference_target] connect ideas in the graph.
    @status draft
    @tags (syntax, reference)
}
```

imports

```
import "pythonmodule.py" as importable_python_module

imports {
    You can import [importable_python_module] - arbitrary files, not only .rq.
}
```

file refs

```
file_reference {
    Point at a whole file ["./module.py"], a symbol ["./module.py".SessionStore],
    or a named test ["./module.test.py:rejects expired token"].
}
```

wildcards

```
wildcard_refs {
    One edge that fans out - path glob plus idea pattern.
    ["../panels/*.rq".*_pane] matches every *_pane idea under panels/.
}
```

typescript

```
// rq:["./syntax.rq".comment_reference]
// An rq: comment in TypeScript pins this location back to an idea.
```

```
<!-- rq:["./syntax.rq".comment_reference] -->
An `rq:` comment in Markdown pins this doc back to an idea.
```

python

```
# rq:["./syntax.rq".comment_reference]
# An rq: comment in Python pins this location back to an idea.
```

## A slice of a real graph

Imports, file anchors, wildcards, wikilinks, status, tags, and tests - one idea that tools can find.

```
from "auth.rq" import login
import "./session.rq" as session

session_refresh {
    refresh tokens rotate on use
    aligns with [session.session_expiry] and [login]
    related panes ["./ui/**/*.rq".*_pane]
    implemented in ["./src/auth/session.ts".rotateRefresh]
    proven by ["./src/auth/session.test.ts:rejects reused refresh token"]

    @status in-progress
    @tags (auth, security)
    @todo reject reuse of the old refresh token
}
```

## Roadmap

Where we're going.

Now

### Context that decides

Activity-bar signals for the next move - not just where a file came from.

### Search in context

Rank matches from the ideas and files you already have open.

### Rank the neighbourhood

Pagerank and multi-seed distance so agents get the right slice.

Later

### Idea git history

CodeLens timeline on an idea - relative dates, moves included.

### How the graph is walked

Remember traversal patterns; recommend better next hops.

# Aseiel/VideoHighlighter

## 导航

- 项目页：[[10-项目/reqlan.com_82389dfd]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
