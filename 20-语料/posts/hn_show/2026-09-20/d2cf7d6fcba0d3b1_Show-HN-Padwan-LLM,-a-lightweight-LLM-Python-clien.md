---
type: "corpus"
item_id: "d2cf7d6fcba0d3b1"
title: "Show HN: Padwan-LLM, a lightweight LLM Python client"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49731552"
project_url: "https://github.com/polarsen-io/padwan-llm"
author: "Orelus"
published_at: "2026-09-16T19:12:12Z"
captured_at: "2026-09-20T09:36:58+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-20"
pub_day: "2026-09-16"
tags:
  - 语料
  - hn_show
  - author_Orelus
  - story_49731552
  - show_hn
metrics: {"points": 4, "comments": 0, "engagement_velocity": 4}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:90d"
---

# Show HN: Padwan-LLM, a lightweight LLM Python client

> [!info] 一句话导读
> polarsen-io/padwan-llm

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49731552>
> 指标：点赞=4 · 评论=0 · engagement_velocity=4
> 作者：Orelus　|　发布：2026-09-16T19:12:12Z
> 项目链接：<https://github.com/polarsen-io/padwan-llm>
> 采集：2026-09-20T09:36:58+08:00　|　id：`d2cf7d6fcba0d3b1`

## 正文

# polarsen-io/padwan-llm

Minimal, provider-agnostic Python client for large language models, built on niquests.

- Stars: 3
- Forks: 0
- Watchers: 3
- Open issues: 1
- License: MIT License
- Homepage: https://polarsen-io.github.io/padwan-llm/
- Default branch: master
- Created: 2026-02-14T21:40:56Z

## Languages

- Just
- Python
- Shell

## Topics

- agent
- gemini
- grok
- http2
- llm
- mcp
- mistral
- niquests
- openai
- python3

## Top Contributors

- Andarius (63 contributions)
- Polarsen-bot (20 contributions)

---

## README

 Padwan LLM

Lightweight, unified async client for OpenAI, Gemini, Mistral, Grok, Anthropic, and any OpenAI-compatible API.
Single runtime dependency (niquests), automatic HTTP/2 and HTTP/3 negotiation.

For the full interactive CLI/TUI, use the separate `padwan-cli` package.

## Installation

```bash
pip install padwan-llm
```

## Library Usage

### One-shot chat

```python
from padwan_llm import LLMClient

async with LLMClient(model="gpt-4o") as client:
    response, usage = await client.complete_chat(
        [{"role": "user", "content": "Hello!"}]
    )
    print(response["content"])
```

### Streaming with `ConversationState`

```python
from padwan_llm import LLMClient, ConversationState

state = ConversationState(system="You are a concise assistant.")

async with LLMClient(model="gpt-4o") as client:
    state.add_user_message("What's Python?")

    stream = client.stream_chat(state.messages)
    chunks: list[str] = []
    async for text in stream:
        print(text, end="", flush=True)
        chunks.append(text)

    state.add_assistant_message("".join(chunks))
    if stream.usage:
        state.accumulate_usage(stream.usage)
```

### Agentic loop with `AgentSession`

`AgentSession` drives a multi-turn conversation that can dispatch tool calls on each
round, feed the results back, and repeat until the model returns a plain text answer.
The `mcp_tools` list accepts both individual `McpTool` instances and whole
`McpTransport` servers — transports are entered as part of the session lifecycle:

```python
from padwan_llm import AgentSession, LLMClient, McpStdio

async with AgentSession(
    client=LLMClient(model="gpt-4o"),
    mcp_tools=[McpStdio(command="uvx", args=["my-mcp-server"])],
    system="You have access to tools. Use them when helpful.",
) as session:
    async for chunk in session.stream("What's the weather in Paris?"):
        print(chunk, end="", flush=True)

    # Or collect the full response in one call:
    text = await session.send("And in London?")
```

`AgentSession` supports sequential or parallel tool execution, approval hooks,
per-tool error handlers, and optional snapshot persistence via a
`ConversationStore` protocol — see docs/agents.md.

### MCP (Model Context Protocol)

Both streamable-HTTP and stdio MCP transports are built in:

```python
from padwan_llm import McpStreamable, McpStdio

# Remote MCP server over HTTP (with optional bearer token)
async with McpStreamable(url="https://mcp.example.com/mcp", token="sk-...") as mcp:
    for tool in mcp.tools:
        print(tool.name, tool.description)

# Local subprocess
async with McpStdio(command="uvx", args=["my-mcp-server"]) as mcp:
    result = await mcp.tools[0].handler({"query": "hello"})
```

See docs/mcp.md for the full feature matrix and architecture.

### Gemini thinking models

Gemini's reasoning models can stream their internal thought tokens separately from
the final answer. Wire an `on_thought` callback to receive them:

```python
from padwan_llm import GeminiClient

thoughts: list[str] = []
async with GeminiClient(
    model="gemini-2.5-flash",
    on_thought=thoughts.append,
    thinking_config={"thinkingBudget": 2048, "includeThoughts": True},
) as client:
    stream = client.stream_chat([{"role": "user", "content": "What is 7 * 8?"}])
    async for chunk in stream:
        print(chunk, end="")

print("\n---\nReasoning:", "".join(thoughts))
```

## One-Shot Command

```bash
export OPENAI_API_KEY=...

padwan-llm "Hello!" -m gpt-4o-mini

# Or without installing:
uvx padwan-llm "Hello!" -m gpt-4o-mini
```

## Supported Models

Auto-detected providers: **OpenAI**, **Gemini**, **Mistral**, **Grok**, **Anthropic** (`claude-*`).

Any OpenAI-compatible API (Groq, Together AI, Ollama, vLLM, ...) is supported via `OpenAIClient` with a custom `base_url`.

## Testing

Unit tests run by default (no API keys needed):

```bash
uv run pytest
```

E2e tests require API keys. Create a `.env` file or pass one with `--env-file`:

```bash
uv run pytest tests/e2e/ -m e2e
uv run pytest tests/e2e/ -m e2e --env-file path/to/.env
```

Tests for providers whose API key is missing are automatically skipped.

## Environment Variables

```bash
OPENAI_API_KEY=...
GEMINI_API_KEY=...
MISTRAL_API_KEY=...
GROK_API_KEY=...
ANTHROPIC_API_KEY=...
```

## 关联链接

- https://mcp.example.com/mcp
- https://polarsen-io.github.io/padwan-llm/

## 导航

- 项目页：[[10-项目/github.com_f906b624]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
