---
type: "corpus"
item_id: "45d55fe64964b201"
title: "Show HN: Prefixwise 0.12 – a paper and a spec for why prompt caches miss"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50581015"
project_url: "https://github.com/tejachavali/prefixwise"
author: "tchavali"
published_at: "2026-11-20T19:58:55Z"
captured_at: "2026-11-21T14:45:01+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-11-21"
pub_day: "2026-11-20"
tags:
  - 语料
  - hn_show
  - author_tchavali
  - story_50581015
  - show_hn
metrics: {"points": 2, "comments": 0, "engagement_velocity": 2}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:3d"
---

# Show HN: Prefixwise 0.12 – a paper and a spec for why prompt caches miss

> [!info] 一句话导读
> tejachavali/prefixwise

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50581015>
> 指标：点赞=2 · 评论=0 · engagement_velocity=2
> 作者：tchavali　|　发布：2026-11-20T19:58:55Z
> 项目链接：<https://github.com/tejachavali/prefixwise>
> 采集：2026-11-21T14:45:01+08:00　|　id：`45d55fe64964b201`

## 正文

# tejachavali/prefixwise

Model-agnostic ledger of avoidable agent token spend: name why prompt cache misses, price the miss, prove fixes without losing task success.

- Stars: 27
- Forks: 0
- Watchers: 27
- Open issues: 1
- License: MIT License
- Default branch: main
- Created: 2026-11-06T04:18:24Z

## Languages

- Dockerfile
- Jupyter Notebook
- Python
- Shell

## Top Contributors

- tejachavali (146 contributions)
- claude (51 contributions)

---

## README

# Prefixwise

CI
PyPI
License: MIT

**Your agent resends its whole conversation every turn, and one changed byte near the top means the provider charges full price for everything after it. Prefixwise tells you which byte, what it cost, and fixes the common causes for you.**

Providers and engines report *how many* tokens missed the prompt cache, not *why*. Prefixwise sits between your agent and the model and does four things:

- **Identify.** One named cause for every request, with its evidence, its cost and its fix.
- **Fix.** `--optimize` repairs the request before it is sent. Only fixes that passed a replay against live models.
- **Prevent.** `prefixwise check` fails CI when a code change would break the cache.
- **Auto-detect.** It recognises vLLM and SGLang behind a URL and, when the engine publishes KV events, subscribes to them on its own.

It stores hashes and counts, never your prompts.

```bash
pip install prefixwise
prefixwise run -- claude             # any agent with an API key: claude, codex, opencode, your own
prefixwise report --session latest   # the session turn by turn
prefixwise run --optimize -- claude  # the same agent, with the proven fixes applied
```

No API key (Claude Code or Codex on a subscription)? `prefixwise import claude-code` reads the logs already on your machine.

## What you see

A real run against the Anthropic API (Claude Sonnet 4.6): an eight-turn agent whose tool list comes back in another order on turn 4 and returns on turn 6 (the run, with the agent).

```
$ prefixwise run --ledger before.db -- python agent.py
8 requests, 26,932 prompt tokens, 75% served from cache. Cost $0.0356.
Avoidable: 3,375 tokens ($0.0116), 12.5% of prompt tokens. Fix these, biggest first:
  1. The same tools were sent in a different order or format (2 requests, 3,375 tokens, $0.0116).
     Fix: Send tools in a fixed order with deterministic serialization (or let the proxy do it: prefixwise serve --fix canonical_tools).
     Prefixwise can do it for you: prefixwise run --fix canonical_tools (proven)
Expected misses (not waste): 1 x first request of a session: nothing to reuse yet.
```

(Four lines of the output are left out here: the proxy's address, the `-- prefixwise: this run --` header, a note on 46 tokens written and never read, and the pointer to the ledger. The record has all of it.) `prefixwise report --ledger before.db --session latest` shows where it happened:

```
Session run-20261110-010636: 8 requests, 26,932 prompt tokens, cache hit rate 74.6%, 3,375 avoidable, cost $0.0356   (claude-sonnet-4-6)

turn  prompt  cached    hit             cause  first changed     cost  avoidable  avoidable $
----  ------  ------  -----  ----------------  -------------  -------  ---------  -----------
1      3,286       0   0.0%       first_write              -  $0.0125          0      $0.0000
2      3,309   3,283  99.2%              none    messages[8]  $0.0017          0      $0.0000
3      3,332   3,306  99.2%              none   messages[10]  $0.0016          0      $0.0000
4      3,355       0   0.0%  tool_reserialize       tools[0]  $0.0132      3,329      $0.0115
5      3,378   3,352  99.2%              none   messages[14]  $0.0019          0      $0.0000
6      3,401   3,329  97.9%  tool_reserialize       tools[0]  $0.0016         46      $0.0002
7      3,424   3,398  99.2%              none   messages[18]  $0.0020          0      $0.0000
8      3,447   3,421  99.2%              none   messages[20]  $0.0013          0      $0.0000
```

"first changed" is the block where the prompt stopped matching the previous request, counted over the whole prompt: tools, then system, then messages. Turn 4 paid for the whole prompt again. Turn 6 went back to the first order and read 3,329 tokens, the prefix turn 3 had written under that order: the older entry was still cached.

With `--optimize`, same agent and same prompts:

| | before | with `--optimize` |
|---|---:|---:|
| Served from cache | 74.6% | 87.1% |
| Cost of the run | $0.0356 | $0.0250 |
| Avoidable tokens | 3,375 | 0 |

## Results

Every number is from a live run against real models, and each links to its record. The full table is in the guide.

| Claim | Result |
|---|---|
| Agrees with Anthropic's own miss reason | **32 of 32** misses Anthropic named (1, 2) |
| Names injected changes at scale, on real agent trajectories | **1,772 of 1,772** seen, **0** named as another cause, **0** false alarms on 3,622 turns that only appended, on vLLM and SGLang with real Claude Code trajectories and generated conversations (records) |
| Names injected causes on open models | **120 of 120** on vLLM, vLLM + LMCache and SGLang (vLLM, LMCache and SGLang) |
| Tells an engine eviction from everything else | **5 of 5**, confirmed from KV events (vLLM, SGLang); a prefix LMCache or HiCache restored counted as a hit **5 of 5**, through the proxy and inside vLLM (record, inside vLLM) |
| The tool-order fix saves what was predicted | **99.9%** on Claude, **97.5%** on vLLM, task success flat (one of 60 turns changed on Qwen3-4B) (record) |
| The cache-marker fix pays for itself | **106.8%** of predicted savings, prompt cost down **85.6%** with the write surcharge included, task success flat (record) |
| Works with real agents | Claude Code, Codex, opencode, the Anthropic and OpenAI SDKs (record, opencode) |
| Costs almost nothing | **2 to 4 ms** per request at 2k tokens, 12 to 23 ms at 120k (streamed to unstreamed), about 100 requests/s per process on 4 CPUs; 33,358 requests in a soak, 0 errors (record) |

## Ways in

Each takes about thirty seconds. All write the same ledger and print the same report.

| You have | Do this |
|---|---|
| An agent you run from a terminal | `prefixwise run -- ` |
| A service, several agents, or a gateway | `prefixwise serve --upstream https://api.anthropic.com`, and point clients at it |
| Your own vLLM server | `vllm serve ... --middleware prefixwise.PrefixwiseMiddleware`: no proxy, no port change (docs/VLLM.md) |
| vLLM with LMCache | the same `--middleware` flag, or `prefixwise serve --upstream ` in front, which detects the engine (docs/LMCACHE.md) |
| SGLang, with or without HiCache | `prefixwise serve --upstream ` in front; it detects the engine (docs/SGLANG.md) |
| Your own Python code | `client = prefixwise.wrap(Anthropic())` (or OpenAI) |
| LiteLLM | `litellm.callbacks = [PrefixwiseCallback()]` |
| Claude Code or Codex on a subscription | `prefixwise import claude-code` / `prefixwise import codex` |
| A gateway's request log (JSON Lines) | `prefixwise import gateway --path requests.jsonl`: yesterday's traffic, the live proxy's verdicts, nothing changed in production |

## Identify

Nineteen causes, each marked as waste or as a legitimate miss. The ones people meet most:

| Cause | What happened | Fix |
|---|---|---|
| `tool_reserialize` | The same tools, in another order or with other bytes | `--optimize` does it, or sort them yourself |
| `volatile_system` | A timestamp or id in the system prompt changed | Move it to the latest user message |
| `history_edit` | Earlier messages were rewritten | Append, do not rewrite; compact at task boundaries |
| `breakpoint_misplaced` | Anthropic: no `cache_control`, or one that stays too early | `--optimize` places them, or add one on the last message |
| `ttl_expired` | The gap since the last turn outlived the cache | A longer TTL, if the reads pay for it |
| `evicted` | A self-hosted engine dropped the session's blocks | More KV memory, or an offload tier |

Beyond the report: `prefixwise explain --diff a.json b.json` shows what changed between two requests, `prefixwise fixes` ranks fixes by dollars, and every non-streaming response carries an `X-Prefixwise-Cause` header (for a stream, look the request up by its id). All causes and details: guide.

## Fix

`--optimize` (on `serve` and `run`, or `PREFIXWISE_OPTIMIZE=1` for the vLLM middleware) applies every fix that has passed a replay against a live model. A fix earns its place by realising at least half of what Prefixwise predicted with task success flat.

- **`canonical_tools`** sorts the tool list and each tool's keys, so a list that drifts between turns stops breaking the cache.
- **`auto_breakpoints`** (Anthropic's API only) adds `cache_control` markers to a request that has none, once the same prefix was seen within the cache window. A one-shot request never pays for a write nobody reads, and a client's own markers are never touched.

Off by default. If the upstream rejects a request carrying markers Prefixwise placed, the client's original is sent instead; `canonical_tools` changes only the order of tools and keys. `prefixwise fixes` says whether a fix paid off on your traffic. Fixes that would change what the model reads, such as moving a timestamp, stay advice.

## Prevent

```bash
prefixwise check -- pytest tests/agent_scenarios      # exit 2 on a cache regression
```

The costly regressions pass every functional test: a tool list built from a set, a timestamp added to the system prompt, a marker moved. `prefixwise check` runs your agent's scenarios against a local mock provider, with no API calls, and fails on four: tools in a changed order, a volatile system prompt, a misplaced marker, a mutated tool result. As a GitHub Action:

```yaml
- uses: tejachavali/prefixwise@v0.12
  with:
    command: pytest tests/agent_scenarios
```

Details, allow-lists and baselines: guide.

## Self-hosted engines

On vLLM and SGLang, with `pip install "prefixwise[engines]"` and the engine publishing its KV-cache events, Prefixwise reads them, so an eviction is confirmed and not inferred, and a prefix that LMCache or HiCache restored from CPU memory is labelled `host_restored`: a hit the GPU alone would have missed. It also names what a chat template costs, such as a reasoning model recomputing its previous answer every turn. Step by step: vLLM, LMCache, SGLang, how the engine join works.

## In production

Prometheus metrics with an alert rule and a Grafana dashboard (docs), OpenTelemetry spans (docs), an HTTP API (docs), a collector for several proxies, and sinks to JSONL or ClickHouse (architecture). Measured overhead is 3 ms per request at 2k tokens.

## Limits

- **One traffic shape per proof.** `canonical_tools` was proven on Claude Haiku 5.5 and Qwen3-4B, `auto_breakpoints` on Haiku 5.5 only; both on scripted multi-turn sessions seconds apart, not an agent's own traffic.
- **OpenAI's own verdict is unchecked.** Its diagnostics answered `unavailable` on every call we made. Prefixwise still classifies OpenAI traffic.
- **A change is located per block, not per token.** An edit at the end of a long system prompt is reported for the whole block.
- **Long sessions and many agents at once** are less tested than short ones.
- **Dollars need a price.** Models in the dated table are priced; others show a dash until you add rates.
- **Ollama and llama.cpp report no cached tokens** (most builds): Prefixwise names every change to the prompt, but cannot tell a hit from a miss there, and says so.
- **API keys only.** An agent signed in with a subscription cannot be routed through a proxy; use `prefixwise import` for those.

The full list, with what was and was not verified live: guide.

## More

- The full guide: every way in, every cause, the command and environment reference, production notes.
- How it decides: the decision procedure, the evidence behind each cause, and the invariants the tests check.
- Use cases, data and metrics, architecture, changelog, security.
- Working on Prefixwise: `pip install -e ".[dev]" && python -m pytest tests -q`. Read docs/WORKLOG.md first.

MIT. See LICENSE.

# aivorynet/aivory-code

## 关联链接

- https://api.anthropic.com`,

## 导航

- 项目页：[[10-项目/github.com_7608b5a9]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
