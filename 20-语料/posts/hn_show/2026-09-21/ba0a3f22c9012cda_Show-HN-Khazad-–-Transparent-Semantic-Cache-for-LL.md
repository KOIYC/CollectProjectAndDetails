---
type: "corpus"
item_id: "ba0a3f22c9012cda"
title: "Show HN: Khazad – Transparent Semantic Cache for LLM Calls on Redis Vector Sets"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=48725166"
project_url: "https://github.com/GuglielmoCerri/khazad"
author: "guglielmoce"
published_at: "2026-06-29T21:01:04Z"
captured_at: "2026-09-21T03:11:03+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-21"
pub_day: "2026-06-29"
tags:
  - 语料
  - hn_show
  - author_guglielmoce
  - story_48725166
  - show_hn
metrics: {"points": 3, "comments": 0, "engagement_velocity": 3}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:113d"
---

# Show HN: Khazad – Transparent Semantic Cache for LLM Calls on Redis Vector Sets

> [!info] 一句话导读
> GuglielmoCerri/khazad

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=48725166>
> 指标：点赞=3 · 评论=0 · engagement_velocity=3
> 作者：guglielmoce　|　发布：2026-06-29T21:01:04Z
> 项目链接：<https://github.com/GuglielmoCerri/khazad>
> 采集：2026-09-21T03:11:03+08:00　|　id：`ba0a3f22c9012cda`

## 正文

# GuglielmoCerri/khazad

Transparent, transport-layer semantic cache for LLM API calls, powered by Redis 8 Vector Sets.

- Stars: 33
- Forks: 2
- Watchers: 33
- Open issues: 0
- License: MIT License
- Default branch: main
- Created: 2026-06-13T15:20:47Z

## Languages

- Python

## Topics

- anthropic
- embeddings
- gemini
- llm
- openai
- python
- redis
- semantic-cache
- vector-search

## Top Contributors

- GuglielmoCerri (35 contributions)

---

## README

 Khazad — You shall not pass.

Python 3.10+
License: MIT
PyPI
Redis 8

*Transparent, transport-layer semantic cache for LLM API calls powered by Redis Vector Sets.*

```
$ uv run --group examples python -P examples/openai.py
  [Khazad] HTTP transport patches installed
  [Khazad] Initialized — threshold=0.90, embedder=huggingface
  [Khazad] Cache flushed
  [Khazad] Loading embedding model: redis/langcache-embed-v2
  Warning: You are sending unauthenticated requests to the HF Hub. Please set a HF_TOKEN to enable higher rate limits and faster downloads.
  Loading weights: 100%|████████████████████████████████████████████████| 134/134 [00:00<00:00, 10758.95it/s]
  [Khazad] CACHE MISS - Forwarding to API
  [call 1] 7918.4ms — The capital of Spain is **Madrid**.
  [Khazad] CACHE HIT - Similarity: 1.00 - Latency: 276ms
  [call 2] 279.9ms — The capital of Spain is **Madrid**.
  {'total_requests': 2, 'cache_hits': 1, 'cache_misses': 1, 'hit_rate': 0.5, 'avg_hit_similarity': 0.9996}
  [Khazad] HTTP transport patches removed
  [Khazad] Stopped — original HTTP transports restored
```

 ~50% fewer API calls · ~96% faster on hits · ~50% lower spend · 100% transparent
 Illustrative figures at a 0.50 hit rate (280ms cache replay vs. ~7900ms upstream call). Your numbers depend on traffic.

Khazad intercepts LLM HTTP traffic at the **transport layer** and serves semantically equivalent requests from a Redis vector cache, **with zero changes to your application code**.

## How it works

Key properties:

- **Model-aware** — each `(provider, model)` pair gets its own vector set, so a `gpt-4o` answer is never served to a `gpt-4o-mini` call, no matter how similar the prompt. Set `cache_scope="host"` to scope by **provider host only**, letting every model or deployment on the same provider share one cache (different providers stay isolated — see Configuration).
- **Conversation-aware** — the whole message list (system, user, assistant) is embedded, not just the last user turn. Two different conversations ending with the same follow-up question ("What about its population?") never collide.
- **Streaming both ways** — cache hits replay as real SSE streams (sync and async clients); cache misses that stream are captured chunk-by-chunk with no added latency and reassembled into a canonical JSON response, so a streamed answer can later serve a non-streamed request and vice versa. Aborted streams are never cached.

## Why use it

Semantic caching trades exactness for cost and latency. Know the trade before turning it on. Use it when you have:

- High-volume, repetitive traffic: FAQ bots, support assistants, RAG front-ends where many users ask near-identical questions
- Dev / test / CI environments — stop paying for the same prompt on every run
- Demos and load tests where deterministic, instant responses are a feature
- Cost ceilings on internal tools

**Operational caveats:**

- **Privacy**: prompts are embedded and responses are stored **in clear text in Redis**. If prompts may contain PII or secrets, set a `ttl`, enable Redis AUTH/TLS, and treat the Redis instance with the same care as your logs.
- **Process-wide patch**: Khazad wraps *every* `httpx.Client`/`AsyncClient` created after `init()` — non-LLM httpx traffic passes through untouched, but the patch is process-global. Call `stop()` on shutdown. Use `hosts=[...]` to restrict interception to the endpoints you actually want cached.
- **httpx-only**: SDKs built on `httpx` are covered (OpenAI, Anthropic, Gemini via `google-genai`, Mistral, and most proxies). SDKs using `requests`, `aiohttp`, or `boto3` (AWS Bedrock) are not intercepted.
- **Single process**: the patch lives in the Python process that called `init()`. Multiple workers share the Redis cache but each needs its own `init()`.
- **False-positive control**: start at `threshold=0.90` and *raise* it if you see wrong hits. Watch `avg_hit_similarity` in `get_stats()` — if it sits near your threshold, your traffic may be too diverse to cache safely.

## Getting Started

### Prerequisites

- Python >= 3.10
- Redis 8 (Vector Sets support required)

```bash
docker run -d --name redis8 -p 6379:6379 redis:8
```

### Installation

**From PyPI**:

```bash
uv add khazad
```

For the OpenAI embedding backend (optional):

```bash
uv add khazad[openai-embeddings]
```

**Local / development install:**

```bash
git clone https://github.com/GuglielmoCerri/khazad.git
cd khazad
uv sync --group dev
```

`uv sync` reads `pyproject.toml`, creates `.venv` if it doesn't exist, and installs the project itself in editable mode — no separate `pip install -e .` needed.

To use the local checkout from another project:

```bash
uv add --editable /path/to/khazad
```

## Usage

Use the `Khazad` class directly when you need explicit control over the instance, useful in long-running services, tests, or dependency injection:

```python
from khazad import Khazad

cache = Khazad(
    redis_url="redis://localhost:6379",
    threshold=0.90,
    ttl=3600,
    log_level="DEBUG",
)

print(cache.is_active())   # True
print(cache.get_stats())   # Stats(total_requests=0, ...)
```

Available functions: `init()`, `stop()`, `get_stats()`, `flush()`, `is_active()`. See API Reference for details.

### Examples

Khazad activates once and intercepts **every** LLM SDK that uses `httpx` underneath, no per-provider wiring needed. For further examples see the examples folder.

Pick the provider you use:

 OpenAI — official SDK against api.openai.com

```python
import os
import time

from openai import OpenAI

from khazad import Khazad

cache = Khazad(redis_url="redis://localhost:6379", threshold=0.90, log_level="DEBUG")

client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

prompt = "What is the capital of Italy?"

for i in range(2):
    start = time.perf_counter()
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}],
    )
    elapsed = (time.perf_counter() - start) * 1000
    print(f"[call {i + 1}] {elapsed:.1f}ms — {response.choices[0].message.content}")

print(cache.get_stats().to_dict())
cache.stop()
```

Matches `*/chat/completions` and `*/responses` paths. Streaming requests also cached.

 Azure OpenAI — Azure deployments with Entra ID auth via AzureOpenAI SDK

```python
import os
import time

from azure.identity import DefaultAzureCredential, get_bearer_token_provider
from openai import AzureOpenAI

from khazad import CacheScope, Khazad

cache = Khazad(
    redis_url="redis://localhost:6379",
    threshold=0.90,
    cache_scope=CacheScope.HOST,
    namespace="azure_openai_example",
)

endpoint = os.environ["AZURE_OPENAI_ENDPOINT"]
deployment = os.environ.get("AZURE_OPENAI_DEPLOYMENT", "gpt-4.1")
token_provider = get_bearer_token_provider(
    DefaultAzureCredential(), "https://cognitiveservices.azure.com/.default"
)
api_version = os.environ.get("AZURE_OPENAI_API_VERSION", "2024-12-01-preview")

client = AzureOpenAI(
    api_version=api_version,
    azure_endpoint=endpoint,
    azure_ad_token_provider=token_provider,
)

prompt = "What is the capital of Spain?"

for i in range(2):
    start = time.perf_counter()
    response = client.chat.completions.create(
        model=deployment,
        messages=[{"role": "user", "content": prompt}],
    )
    elapsed = (time.perf_counter() - start) * 1000
    print(f"[call {i + 1}] {elapsed:.1f}ms — {response.choices[0].message.content}")

print(cache.get_stats().to_dict())
cache.stop()
```

It authenticates with Microsoft Entra ID (`DefaultAzureCredential`) — no API key needed — and uses `cache_scope=CacheScope.HOST` so every deployment on the same Azure resource shares one cache. API-key auth works too: Khazad matches the request path (`/chat/completions`), not the auth method or host.

 OpenAI-compatible proxies — LiteLLM, vLLM, Ollama, …

```python
import time

from openai import OpenAI

from khazad import Khazad

cache = Khazad(redis_url="redis://localhost:6379", threshold=0.90, namespace="ollama_example")

client = OpenAI(base_url="http://localhost:11434/v1", api_key="ollama")
model = "llama3"

prompt = "What is the capital of Spain?"

for i in range(2):
    start = time.perf_counter()
    response = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
    )
    elapsed = (time.perf_counter() - start) * 1000
    print(f"[call {i + 1}] {elapsed:.1f}ms — {response.choices[0].message.content}")

print(cache.get_stats().to_dict())
cache.stop()
```

Any host whose URL path ends with `/chat/completions` or `/responses` is cached. Covers vLLM (`http://host:8000/v1/...`), Ollama (`http://localhost:11434/v1/...`), Mistral, etc.

 Anthropic — Claude via official SDK

```python
import os
import time

from anthropic import Anthropic

from khazad import Khazad

cache = Khazad(redis_url="redis://localhost:6379", threshold=0.90, namespace="anthropic_example")

client = Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])
model = "claude-haiku-4-5-20251001"

prompt = "What is the capital of France?"

for i in range(2):
    start = time.perf_counter()
    message = client.messages.create(
        model=model,
        max_tokens=256,
        messages=[{"role": "user", "content": prompt}],
    )
    elapsed = (time.perf_counter() - start) * 1000
    print(f"[call {i + 1}] {elapsed:.1f}ms — {message.content[0].text}")

print(cache.get_stats().to_dict())
cache.stop()
```

Matches `api.anthropic.com/v1/messages`. Streaming responses replayed from cache as SSE.

 Google Gemini — google-genai SDK

```python
import os
import time

from google import genai

from khazad import Khazad

cache = Khazad(redis_url="redis://localhost:6379", threshold=0.90)
client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

for i in range(2):
    start = time.perf_counter()
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents="What is the capital of Italy?",
    )
    elapsed = (time.perf_counter() - start) * 1000
    print(f"[call {i + 1}] {elapsed:.1f}ms — {response.text}...")

print(cache.get_stats().to_dict())
cache.stop()
```

Matches `generativelanguage.googleapis.com/*/models/*:generateContent`. Gemini streaming (`:streamGenerateContent`) passes through uncached.

## Supported Providers

| Provider | URL pattern matched | Streaming |
|---|---|---|
| OpenAI Chat Completions | any host, path ending `/chat/completions` | cached + replayed |
| OpenAI Responses API | any host, path ending `/responses` | cached + replayed |
| Azure OpenAI | covered by chat/completions matcher | cached + replayed |
| OpenAI-compatible proxies | covered by chat/completions matcher | cached + replayed |
| Anthropic | `api.anthropic.com/v1/messages` | cached + replayed |
| Google Gemini | `generativelanguage.googleapis.com/*:generateContent` | pass-through |

## API Reference

The module exposes five functions as the singleton API. The `Khazad` class exposes the same surface as instance methods (no `init`, instantiation does that).

| Function | Description |
|---|---|
| `init(...)` | Activate the global singleton: builds the embedder, connects to Redis, installs the `httpx` transport patch. Required before any LLM traffic; calling twice without `stop()` is a no-op. See Configuration for parameters. |
| `stop()` | Restore original `httpx` transports, close Redis, and clear the singleton. Idempotent. Cached data in Redis stays. |
| `get_stats()` | Returns a dictionary with a thread-safe snapshot of cache metrics (requests, hits, misses, hit rate, avg similarity). |
| `flush()` | Clear all cached entries in the current namespace and reset stats counters. Destructive. |
| `is_active()` | Returns `True` if Khazad is currently running (initialized and not stopped). |

## Configuration

All parameters are the same whether you use `khazad.init()` or `Khazad(...)`:

```python
Khazad(
    redis_url="redis://localhost:6379",  
    threshold=0.90,                     
    ttl=3600,                            
    namespace="khazad",                 
    embedder="huggingface",              
    embedding_model="redis/langcache-embed-v2",
    log_level="INFO",                    
    hosts=None,                          
    cache_scope="model"
)
```

| Parameter | Default | Description |
|---|---|---|
| `redis_url` | `"redis://localhost:6379"` | Connection URL for the Redis 8 instance that stores vectors and cached responses. |
| `threshold` | `0.90` | Cosine similarity threshold (0.0-1.0) above which a request counts as a cache hit. |
| `ttl` | `3600` | Time-to-live in seconds for cached response bodies; `None` means no expiry. |
| `namespace` | `"khazad"` | Prefix for all Redis keys, isolating this cache from other data and other namespaces. |
| `embedder` | `"huggingface"` | Embedding backend: `"huggingface"` (free, local) or `"openai"` (paid API). |
| `embedding_model` | `"redis/langcache-embed-v2"` | Model used to embed prompts; must match the chosen `embedder`. |
| `log_level` | `"INFO"` | Logging verbosity: `DEBUG`, `INFO`, `WARNING`, or `ERROR`. |
| `hosts` | `None` | Opt-in host allowlist; `None` means all matching hosts (see below). |
| `cache_scope` | `"model"` | Cache partitioning: `"model"` (per `(host, model)`) or `"host"` (per provider, see below). |

**`hosts` — opt-in allowlist.** By default Khazad considers traffic to any host that matches a provider URL pattern. Pass an explicit allowlist to restrict interception to the endpoints you intend to cache; everything else passes through untouched. Supports exact hosts and `*.` wildcard subdomains:

```python
khazad.init(hosts=["api.openai.com", "*.openai.azure.com"])
```

**`cache_scope` — share one cache across a provider's models.** Driven by the `CacheScope` enum (importable from `khazad`); the string values `"model"` and `"host"` are accepted too. By default (`CacheScope.MODEL`) each `(host, model)` pair gets its own vector set, so a `gpt-4o` answer never serves a `gpt-4o-mini` call. Set it to `CacheScope.HOST` to scope by **host only** — every model or deployment on the same provider then shares a single cache:

```python
from khazad import CacheScope

khazad.init(cache_scope=CacheScope.HOST)   # or cache_scope="host"
```

The host always stays part of the scope, so different providers never mix (an Azure OpenAI response is never replayed to a Gemini client). Use it only for format-compatible pools — e.g. multiple Azure OpenAI deployments, or treating `gpt-4o` and `gpt-4o-mini` as interchangeable. The trade-off is semantic: a smaller model may serve an answer originally produced by a larger one.

**Threshold guidance:**

- `0.95+` — strict, near-identical prompts only
- `0.90` — recommended default
- `0.85` — aggressive, higher hit rate

**TTL:** the response body expires in Redis after `ttl` seconds. Khazad prunes the matching vector automatically the next time it is found without a body, so expired entries clean themselves up.

## Embedding Backends

| Backend | Cost | Notes |
|---|---|---|
| `huggingface` (default) | Free | Downloads model on first use |
| `openai` | Paid | `uv add khazad[openai-embeddings]` |

## Observability

Khazad emits a log line for every intercepted request, so you can watch cache behaviour in real time. A hit reports the cosine similarity that triggered it and the replay latency; a miss notes that the request was forwarded upstream. Raise `log_level` to `DEBUG` for per-request detail, or keep it at `INFO` for just hits and misses.

```text
[Khazad] CACHE HIT - Similarity: 0.94 - Latency: 4ms
[Khazad] CACHE MISS - Forwarding to API
```

For aggregate metrics, call `get_stats()` at any time. It returns a thread-safe snapshot of total requests, hits, misses, the resulting hit rate, and the average similarity of served hits — ideal for periodic logging or exposing as a Prometheus gauge. Watch `avg_hit_similarity`: if it hovers near your `threshold`, your traffic may be too diverse to cache safely and you should raise the threshold.

```python
cache.get_stats().to_dict()
# {'total_requests': 1000, 'cache_hits': 720, 'cache_misses': 280,
#  'hit_rate': 0.72, 'avg_hit_similarity': 0.943}
```

## Contributing

Contributions welcome — see CONTRIBUTING.md. Please read it before opening a pull request, as it covers the branching model, coding conventions, and the lint and test checks your changes are expected to pass.

The unit and integration suites use fake embedders and mock transports, so the full test run needs neither a live Redis instance nor real API keys.

## License

MIT

# vmxdev/xenoeye

## 关联链接

- http://host:8000/v1/...`
- http://localhost:11434/v1
- http://localhost:11434/v1/...`
- https://cognitiveservices.azure.com/.default
- https://github.com/GuglielmoCerri/khazad.git

## 导航

- 项目页：[[10-项目/github.com_247c37b4]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
