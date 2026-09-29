---
type: "corpus"
item_id: "6e7dbc88ad5d933f"
title: "Show HN: Decide – Jev decisions in the shell, scripts, and agent skills"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49878492"
project_url: "https://github.com/vsekhar/decide"
author: "vsekhar"
published_at: "2026-09-28T14:23:59Z"
captured_at: "2026-09-29T09:42:55+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-29"
pub_day: "2026-09-28"
tags:
  - 语料
  - hn_show
  - author_vsekhar
  - story_49878492
  - show_hn
metrics: {"points": 2, "comments": 0, "engagement_velocity": 2}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:3d"
---

# Show HN: Decide – Jev decisions in the shell, scripts, and agent skills

> [!info] 一句话导读
> All software makes decisions. Code handles the deterministic ones. Decision models like Jev handle the judgement calls.A decision model takes context and questi…

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49878492>
> 指标：点赞=2 · 评论=0 · engagement_velocity=2
> 作者：vsekhar　|　发布：2026-09-28T14:23:59Z
> 项目链接：<https://github.com/vsekhar/decide>
> 采集：2026-09-29T09:42:55+08:00　|　id：`6e7dbc88ad5d933f`

## 正文

All software makes decisions. Code handles the deterministic ones. Decision models like Jev handle the judgement calls.A decision model takes context and questions with a fixed set of choices, and returns answers with a calibrated probability. No prose, nothing to parse. Decision models are 200x faster and 400x cheaper than LLMs making comparable judgements.I wanted to play around with decision models in more places and without writing code or manually calling APIs. I wanted scripts to read like natural language and agents to be able to pick up the tool and use it after simply reading the help output. brew install vsekhar/tap/decide
 decide --set-config --model typesafe:jev-latest --api-key
 API key:

 decide "Is Atlanta the capital of Georgia?"
 yes

 # Choose from among options
 decide "What kind of weather is typical in Florida?" \
 --option rainy \
 --option sunny \
 --option snowy
 sunny

 # Provide context (32k context window)
 decide --context @ticket.txt \
 "Which team handles this ticket?" \
 --option shipping \
 --option billing \
 --option returns
 billing

 # Pick a level, least to most, explain each to the model
 decide --context @ticket.txt \
 "How urgent is this ticket?" \
 --level not_urgent="Customer feedback or feature request" \
 --level somewhat_urgent="Customer problem, not blocked" \
 --level urgent="Customer blocked"
 somewhat_urgent

 # Multiple questions in one call, name questions for easier parsing
 decide --context @ticket.txt \
 "Which team handles this ticket?" \
 --name team \
 --option shipping \
 --option billing \
 --option returns \
 "How urgent is this ticket?" \
 --level not_urgent \
 --level somewhat_urgent \
 --level urgent \
 "Should we issue a refund?"
 team=billing
 somewhat_urgent
 yes

 # Script-friendly exit codes
 if decide --context "$body" "Is this message spam?" -q; then
 mv "$file" spam/
 fi

Other features:- Confidence: gate on the model's confidence in its answer with --min-confidence and --fallback- Question files: load questions from a file, useful for detailed questionnaires under version control- Scriptable: 0 is decided or yes, 1 is no, 2 is unsure, 10 is your mistake, 11 is network/model problem- Agent skill: agents can get cursory information about files quickly and cheaply before or instead of reading them (example skill included in the repo) - token efficient, no MCP- Statistics and distribution: output the model's confidence and probabilities across your choices- JSON: read context as JSON objects, write decisions as JSON objects- Streaming: decide once per line from stdin using --each (for JSONL pipelines)- Economical: two orders of magnitude cheaper than LLMs (Jev: $0.042/Mtok input, free output)- Fast: typical latency of 200ms end-to-end (400 token context with 5 questions)- Scalable: unlimited questions per call, processed in parallelLimitations:- Typesafe or OpenRouter API key required- macOS 26+ pre-built via Homebrew; macOS 15 and Linux build from source (requires Swift 6.2)- Jev only (so far the only publicly available decision model)See also:- DecisionModels (https://github.com/vsekhar/DecisionModels): Swift library for static and dynamic decision model calls, inspired by Apple's FoundationModels library, and powering decide.- llm-typesafe (https://github.com/simonw/llm-typesafe): JSON-oriented input and output, integrated into the general purpose (and very popular) llm command by simonw which is written in Python and has 14 runtime dependencies.Swift 6.2, Apache 2.0What do you think about the command line model? How are you plugging decision models into your systems?

## 关联链接

- https://github.com/simonw/llm-typesafe
- https://github.com/vsekhar/DecisionModels

## 导航

- 项目页：[[10-项目/github.com_44d811bf]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
