---
type: "corpus"
item_id: "5db746403ebe6418"
title: "Show HN: Lite-Harness – Self-Hosted Cursor Agents (Use Claude Code/OpenCode)"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=48341726"
project_url: "https://github.com/LiteLLM-Labs/lite-harness"
author: "detente18"
published_at: "2026-05-30T23:51:21Z"
captured_at: "2026-09-21T02:52:49+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-21"
pub_day: "2026-05-30"
tags:
  - 语料
  - hn_show
  - author_detente18
  - story_48341726
  - show_hn
metrics: {"points": 6, "comments": 0, "engagement_velocity": 6}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:144d"
---

# Show HN: Lite-Harness – Self-Hosted Cursor Agents (Use Claude Code/OpenCode)

> [!info] 一句话导读
> Published: 2026-05-27

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=48341726>
> 指标：点赞=6 · 评论=0 · engagement_velocity=6
> 作者：detente18　|　发布：2026-05-30T23:51:21Z
> 项目链接：<https://github.com/LiteLLM-Labs/lite-harness>
> 采集：2026-09-21T02:52:49+08:00　|　id：`5db746403ebe6418`

## 正文

Published: 2026-05-27

# Repository: LiteLLM-Labs/lite-harness

Unified API for running OpenCode, Claude Code, Codex agents

- Stars: 81
- Forks: 17
- Watchers: 1
- Open issues: 10
- Primary language: JavaScript
- Languages: JavaScript (35.7%), TypeScript (24.6%), Python (24.1%), HTML (14.8%), Shell (0.8%)
- Default branch: main
- Created: 2026-05-27T18:10:10Z
- Last push: 2026-06-03T19:12:52Z
- Contributors: 3 (top: krrish-berri-2, ishaan-berri, oss-agent-shin)

---

# lite-harness

Call all agent harnesses using the Claude Agent SDK format.

lite-harness manages:

- One TypeScript and Python interface for multiple agent harnesses
- Harness switching with `harness`, model switching with `model`
- Claude Agent SDK-compatible streaming messages and errors

> Preview: the SDK is not published to npm or PyPI yet. Clone this repo to try
> it. If you want a packaged release, please
> [file an issue](https://github.com/LiteLLM-Labs/lite-harness/issues).

[![Discord](https://img.shields.io/badge/Discord-Chat-5865F2?logo=discord&logoColor=white)](https://discord.gg/Nkxw3rm3EE)

## Setup (clone)

```bash
git clone https://github.com/LiteLLM-Labs/lite-harness.git
cd lite-harness

# install the backend server's deps once — the SDK auto-spawns it from the clone
npm install --prefix src/sdk/server

# pick a model — set the key for your provider:
export ANTHROPIC_API_KEY=sk-ant-...   # for harness "claude-code"
export OPENAI_API_KEY=sk-...          # for harness "codex"
```

## TypeScript Usage

```bash
npm install --prefix src/sdk/typescript && npm run build --prefix src/sdk/typescript
```

```ts
import { query } from "@lite-harness/sdk";

const prompt = "Fix the failing test";

// Claude Code harness
for await (const message of query({
  prompt,
  options: { harness: "claude-code", model: "claude-opus-4-8" },
})) {
  console.log(message);
}

// Codex harness
for await (const message of query({
  prompt,
  options: { harness: "codex", model: "gpt-5.5" },
})) {
  console.log(message);
}
```

## Python Usage

```bash
pip install -e src/sdk/python      # editable install of the client (Python 3.10+)
```

```python
from lite_harness import query, AgentOptions

prompt = "Fix the failing test"

# Claude Code harness
async for message in query(
    prompt=prompt,
    options=AgentOptions(harness="claude-code", model="claude-opus-4-8"),
):
    print(message)

# Codex harness
async for message in query(
    prompt=prompt,
    options=AgentOptions(harness="codex", model="gpt-5.5"),
):
    print(message)
```

## Supported Harnesses

See [`src/sdk/server/providers/`](src/sdk/server/providers/) for the full list.

- `claude-code`: Claude Agent SDK / Claude Code behavior.

Upstream: [Python](https://github.com/anthropics/claude-agent-sdk-python),
 [TypeScript](https://github.com/anthropics/claude-agent-sdk-typescript).

- `codex`: OpenAI Codex CLI behavior.

Upstream: [openai/codex](https://github.com/openai/codex).

- `pi-ai`: Pi AI behavior.

## With LiteLLM AI Gateway

Add LiteLLM AI Gateway when you want central keys, budgets, logs, fallbacks, and
provider routing.

```bash
export LITELLM_API_BASE=https://litellm.your-company.com/v1
export LITELLM_API_KEY=sk-litellm-...
```

```ts
import { query } from "@lite-harness/sdk";

for await (const message of query({
  prompt: "Debug this production trace",
  options: {
    harness: "codex",
    model: "anthropic/claude-opus-4-8",
  },
})) {
  console.log(message);
}
```

## Docs

[SDK](src/sdk/README.md)

## License

MIT

# https://trost.co/kanji-pairs/

## 关联链接

- https://discord.gg/Nkxw3rm3EE
- https://github.com/LiteLLM-Labs/lite-harness.git
- https://github.com/LiteLLM-Labs/lite-harness/issues
- https://github.com/anthropics/claude-agent-sdk-python
- https://github.com/anthropics/claude-agent-sdk-typescript
- https://github.com/openai/codex
- https://img.shields.io/badge/Discord-Chat-5865F2?logo=discord&logoColor=white
- https://litellm.your-company.com/v1
- https://trost.co/kanji-pairs/

## 导航

- 项目页：[[10-项目/github.com_68cc1cf2]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
