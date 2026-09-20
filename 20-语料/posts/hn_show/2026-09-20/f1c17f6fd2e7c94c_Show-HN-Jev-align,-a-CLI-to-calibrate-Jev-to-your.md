---
type: "corpus"
item_id: "f1c17f6fd2e7c94c"
title: "Show HN: Jev-align, a CLI to calibrate Jev to your judgement"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49770872"
project_url: "https://github.com/sutro-sh/jev-align"
author: "sethkim"
published_at: "2026-09-19T23:05:55Z"
captured_at: "2026-09-20T09:48:16+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-20"
pub_day: "2026-09-19"
tags:
  - 语料
  - hn_show
  - author_sethkim
  - story_49770872
  - show_hn
metrics: {"points": 2, "comments": 0, "engagement_velocity": 2}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:3d"
---

# Show HN: Jev-align, a CLI to calibrate Jev to your judgement

> [!info] 一句话导读
> Build calibrated AI classifiers from human feedback using Jev and GEPA.

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49770872>
> 指标：点赞=2 · 评论=0 · engagement_velocity=2
> 作者：sethkim　|　发布：2026-09-19T23:05:55Z
> 项目链接：<https://github.com/sutro-sh/jev-align>
> 采集：2026-09-20T09:48:16+08:00　|　id：`f1c17f6fd2e7c94c`

## 正文

# sutro-sh/jev-align

Build calibrated AI classifiers from human feedback using Jev and GEPA.

- Stars: 132
- Forks: 10
- Watchers: 132
- Open issues: 0
- License: Apache License 2.0
- Homepage: https://pypi.org/project/jev-align/
- Default branch: main
- Created: 2026-09-19T02:12:23Z

## Languages

- Makefile
- Python
- Shell

## Topics

- active-learning
- classification
- cli
- gepa
- human-in-the-loop
- jev
- prompt-optimization
- typesafe-ai

## Top Contributors

- sethkimmel3 (21 contributions)

---

## README

# jev-align

`jev-align` is an experimental CLI from Sutro for building
AI Functions with TypeSafe's Jev.

It finds uncertain examples, asks you to label them, and uses
GEPA to improve the function. Use it in your
application and keep learning from production examples.

## Demo

https://github.com/user-attachments/assets/81650587-e3f1-4655-8213-ed5f6e120e9a

## Quick start

Requires Python 3.11 or newer.

```shell
uv tool install jev-align
export TYPESAFE_API_KEY="..." # Or use Vercel or Cloudflare below
export OPENAI_API_KEY="..." # or ANTHROPIC_API_KEY / GEMINI_API_KEY
jeva
```

Start the CLI with either `jeva` or `jev-align`.

Use `pip install jev-align` if you do not use
uv. The guided setup discovers local CSV,
Parquet, and JSONL files and includes three ready-to-run examples.

## How it works

Each round:

1. Evaluates the configured dataset and measures uncertainty.
2. Selects ambiguous rows plus a random audit sample for you to label.
3. Uses your accumulated labels and optional rationales to run GEPA.
4. Shows the score, certainty change, and proposed definition diff.
5. Lets you accept, reject, rewind, or resume later.

Every label comes from you. A higher training score never accepts a proposal
automatically.

## Task types

| Type | Output |
| --- | --- |
| Binary | `True` or `False` |
| Multiclass | Exactly one fixed label |
| Multilabel | Zero or more fixed labels |
| Score | One level from an ordered rubric |

## Configuration

The guided **Advanced** menu configures:

- 5, 10, 15, or 20 training annotations per round.
- An optional 20% held-out evaluation set.
- GEPA's metric-call budget, which defaults to 300.

By default, `jev-align` uses the first 1,000 rows—or the entire dataset when it
is smaller—and lets you concatenate all fields or select specific columns.

Everything can also be configured with flags:

```shell
jeva optimize posts.csv \
  --question "Is the post related to aviation?" \
  --column title \
  --column text \
  --pool-size 1000
```

Use repeated `--class "NAME=DESCRIPTION"` options for multiclass or multilabel
tasks, and repeated `--score-level` options for scoring tasks. Run
`jeva optimize --help` for the complete flag reference.

## Jev providers

Jev can run directly through TypeSafe AI, Vercel AI Gateway, or Cloudflare
Workers AI. The guided setup detects configured providers and lets you choose.

```shell
# Vercel AI Gateway
export AI_GATEWAY_API_KEY="..."
jeva optimize data.csv --question "Is this relevant?" --column text \
  --backend vercel

# Cloudflare Workers AI
export CLOUDFLARE_ACCOUNT_ID="..."
export CLOUDFLARE_API_TOKEN="..."
jeva optimize data.csv --question "Is this relevant?" --column text \
  --backend cloudflare
```

These routes do not require a `TYPESAFE_API_KEY`. The chosen provider is saved
with the AI Function, so later runtime calls use the same provider. GEPA's
reflection model is configured separately.

## Reflection models

GEPA's reflection model is separate from the JEV model evaluating your data.
OpenAI, Anthropic, and Gemini models are detected automatically. Any
LiteLLM provider—including Fireworks,
local vLLM, and other OpenAI-compatible endpoints—can be supplied with
`--reflection-model provider/model`.

```shell
export HOSTED_VLLM_API_BASE="http://localhost:8000/v1"
jeva optimize data.csv --question "Is this relevant?" --column text \
  --reflection-model "hosted_vllm/Qwen/Qwen3-8B"
```

## Controls

- Arrow keys and Enter navigate menus.
- `b` returns to the previous label; `/back` leaves the rationale prompt.
- Space toggles choices in multilabel tasks.

## Saved AI Functions

```shell
jeva functions
jeva optimize --resume .jev-align/runs/<run-id>
```

## Keep learning from production

Load an AI Function in your application and capture useful production examples:

```python
from jev_align import AIFunction

is_aviation = AIFunction.load(
    ".jev-align/runs/<run-id>",
    capture=True,
)

prediction = is_aviation(
    title="Airport expansion",
    text="A new runway opens next year.",
)
```

Later, resume the AI Function and label the captured examples. GEPA uses that
feedback to propose the next version:

```shell
jeva functions
```

## Using a coding agent

See AGENTS.md for detailed setup, provider configuration, CLI
operation, and development guidance for coding agents.

## Affiliation

Sutro is not affiliated with TypeSafe AI, the makers of Jev.

## 关联链接

- http://localhost:8000/v1
- https://github.com/user-attachments/assets/81650587-e3f1-4655-8213-ed5f6e120e9a
- https://pypi.org/project/jev-align/

## 导航

- 项目页：[[10-项目/github.com_79e601de]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
