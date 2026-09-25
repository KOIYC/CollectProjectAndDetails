---
type: "corpus"
item_id: "a0f10cafe68ecc41"
title: "Show HN: Fusion-runtime – self-hosted voice agents, STT+LLM+TTS in one process"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49789320"
project_url: "https://github.com/SamarthUrs18/fusion-runtime"
author: "samarthurs18"
published_at: "2026-09-21T16:19:54Z"
captured_at: "2026-09-25T00:12:57+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-22"
pub_day: "2026-09-21"
tags:
  - 语料
  - hn_show
  - author_samarthurs18
  - story_49789320
  - show_hn
metrics: {"points": 2, "comments": 0, "engagement_velocity": 2}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:3d"
---

# Show HN: Fusion-runtime – self-hosted voice agents, STT+LLM+TTS in one process

> [!info] 一句话导读
> SamarthUrs18/fusion-runtime

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49789320>
> 指标：点赞=2 · 评论=0 · engagement_velocity=2
> 作者：samarthurs18　|　发布：2026-09-21T16:19:54Z
> 项目链接：<https://github.com/SamarthUrs18/fusion-runtime>
> 采集：2026-09-25T00:12:57+08:00　|　id：`a0f10cafe68ecc41`

## 正文

# SamarthUrs18/fusion-runtime

Self-hosted voice agent runtime: speech-to-text, an LLM and text-to-speech streaming into each other in one process.

- Stars: 3
- Forks: 0
- Watchers: 3
- Open issues: 0
- License: Apache License 2.0
- Homepage: https://fusion-runtime.dev
- Default branch: main
- Created: 2026-09-19T09:59:39Z

## Languages

- Dockerfile
- HTML
- JavaScript
- Makefile
- Python
- Shell

## Top Contributors

- SamarthUrs18 (53 contributions)

---

## README

**A self-hosted voice agent runtime.** Speech-to-text, the LLM and text-to-speech run together on
one machine and stream into each other, so a reply starts playing while it's still being generated.

**On an RTX 3090 with a 7B model: about 490 ms of processing once a turn ends**, or 991 ms
stopwatched from your last syllable — the difference is a silence wait you can configure. 127
tokens/sec, interruptions honoured mid-sentence.

## Quickstart

Requires Python 3.11–3.13.

```bash
pip install fusion-runtime
```

An agent is one file. This is the whole thing:

```python
# agent.py
from fusion_runtime import Agent, LLM, STT, TTS, Turns

agent = Agent(
    name="shopkart-orders",
    prompt="You are the order line for ShopKart. Keep answers to one short sentence.",
    stt=STT("whisper-tiny.en"),          # or "whisper-small" for better accuracy
    llm=LLM("qwen2.5-0.5b-q4", max_tokens=256),
    tts=TTS("kokoro-v1.0", voice="af_heart"),
    turns=Turns(wait_ms=500, interrupt_after_ms=300),
)
```

```bash
frun models pull agent.py     # exactly the models it names, nothing else
frun up agent.py              # add --reload to restart on every edit
```

Then talk to it from a second terminal:

```bash
pip install "fusion-runtime[talk]"
frun talk
```

That is the whole loop — one file, two commands, a conversation. Talk over the agent to
interrupt it.

`frun up` with no file runs a default agent if you just want to hear it work, and `frun doctor`
checks libraries, GPU, models and audio and says how to fix what it finds.

### In a browser instead

The runtime serves a browser client at **http://localhost:8000** — the same one you would embed
in your own page.

With no keys configured, open it and click Talk. With keys configured (`FUSION_ACCEPTED_KEYS`),
a page can't hold a secret, so it needs a short-lived session token:

```bash
frun token        # prints a URL with a token in it — open that
```

Tokens are single-use and expire in about a minute. The page is handed its next one over the
socket it already has, so a conversation keeps going without asking again. If you open the bare
URL on a server with keys, the connection closes and the page says the token wasn't accepted.

### Naming models

A model is a catalog id (`frun models list`), a file path, `hf:owner/repo` for anything on
Hugging Face, or a URL for an OpenAI-compatible endpoint. Settings the config knows are applied;
anything else is passed through to that runtime.

Secrets never go in the agent file — it names the *variable* holding a key
(`api_key_env="GROQ_API_KEY"`), so `agent.py` is safe to commit.

## On your own site

```html


<button id="talk"></button>


```

The runtime serves the browser client it uses itself, so the page you demo with is the one your
site embeds. With no `url` it connects back to wherever the script came from.

Browsers only allow a microphone on `https://`, so a deployment needs TLS and `wss://`. A page
never holds an API key: your backend mints it a short-lived token.

## Authentication

```bash
frun key new
FUSION_ACCEPTED_KEYS=web:frun_kR7m...
```

Without keys the server answers on `localhost` only, and `frun up --host 0.0.0.0` refuses to
start. `frun talk`, a backend or curl send the key in an `Authorization` header; a browser page
gets a short-lived, single-use token from `POST /v1/sessions` instead, because a page can hold
neither a secret nor a header.

Concurrency caps, message and audio limits, idle timeouts, origin allowlists and proxy trust all
have working defaults — see the docs.

## Performance

Measured, not estimated. The production profile as it ships — RTX 3090, Qwen 7B q4 + Whisper
small + Kokoro on the one card — through the browser client, 21 September 2026:

| | Median | Range |
|---|---|---|
| **Processing** — turn ends, audio comes back | **~490 ms** | 288–657 |
| **Stopwatch from your last syllable** | **991 ms** | 858–1061 |
| ↳ of which: silence wait before the turn is judged over | ~500 ms | `turns.wait_ms` |
| Speech-to-text | 119 ms | 58–329 |
| LLM first token | 27 ms | 20–70 |
| First token → first audio (a sentence gets written, then spoken) | 430 ms | 320–509 |
| Text-to-speech real-time factor | 0.09 | speech is synthesized ~11× faster than real time |
| LLM tokens/sec | 127 | 106–130 |

**Two numbers, because there are two honest answers.** A stopwatch started at your last syllable
reads 991 ms. About 500 ms of that is the runtime waiting through silence to decide you've
finished — which elapses while you're still finishing, so people don't experience it as waiting.
What a caller feels is closer to the 490 ms of processing. Quote whichever you like, but say
which one: a voice stack claiming a number under 500 ms is almost always measuring from "we
decided the caller stopped", not "the caller stopped".

**The stages don't sum, and that's not sleight of hand.** Transcription of what you already said
runs during the silence wait. And "first token → first audio" is mostly the language model
writing a sentence — text-to-speech can't start on half a clause — so it is not a measure of how
fast Kokoro is. Kokoro's own speed is the real-time factor: 0.09, or about 126 ms of compute for
1.4 seconds of speech.

Every figure is the runtime's own per-turn telemetry (`frun talk --verbose`, or the browser
console), so you can reproduce them rather than trusting ours. Barge-in fired on every attempt.

## Several callers at once

Measured on the same 3090, real WebSocket sessions, three turns each:

| Callers | Response, median | Turns/sec |
|---|---|---|
| 1 | ~460 ms | 0.21 |
| 4 | ~740 ms | 0.55 |
| 8 | ~4600 ms | 0.69 |
| 12 | ~7500 ms | 0.74 |

**Four simultaneous callers land in the same range as one**, within run-to-run variance. Past
that it saturates: throughput plateaus around 0.7 turns/sec, so an extra caller past the knee
buys queue time rather than capacity. Eight is not a conversation.

The bottleneck is one specific thing. At twelve callers the language model's first token takes
4790 ms of a 5312 ms response, while speech-to-text stays at 76 ms and text-to-speech at 469 ms.
A single in-process llama.cpp context decodes one reply at a time; the speech stages do not care
how many callers there are.

So to go past four, move the language model out and leave speech where it is:

```python
llm = LLM("http://localhost:8080/v1", model_name="qwen2.5-7b-instruct")
```

vLLM and `llama-server -np N` both speak the API the `openai_http` runtime uses. Whether that
moves the knee, and how far, is not yet measured.

## The `frun` CLI

| | |
|---|---|
| `frun up [agent.py]` | Starts the server. `--host`, `--port`, `--reload`, `--config` |
| `frun talk` | Talks to it from a terminal, with a latency summary per turn |
| `frun models list` / `pull` | What's available, and downloading it |
| `frun key new` / `keys list` / `token` | Keys and browser tokens |
| `frun doctor` | Checks the machine and says how to fix what's wrong |
| `frun version` | The installed version. `--version` and `-V` work too |

`fusion-runtime` works as an alias for `frun`.

## Using it as a library

`frun up agent.py` covers running an agent. The pipeline can also run inside your own process —
for a queue worker, a test, or a batch job over recorded calls — with no server involved. See
`examples/sdk_example.py`, which is runnable, and
the docs.

## Documentation and contact

Everything else — configuration, turn detection, languages, the server API, telemetry, limits,
GPU setup and deployment — is at **fusion-runtime.dev/docs**.

| | |
|---|---|
| Site and docs | **fusion-runtime.dev** |
| Questions, or anything else | **hello@fusion-runtime.dev** |
| Security problems | **security@fusion-runtime.dev** — not a public issue, please (why) |

## Development

```bash
uv sync --extra dev --extra talk     # or: pip install -e ".[dev,talk]"
pytest
```

CI runs the suite on Python 3.11, 3.12 and 3.13. CONTRIBUTING.md has the
layout, the design rules a review will hold you to, and how to add a runtime.

## License

Apache-2.0. Embed it in a commercial product, rebrand it, ship it closed — keep the
copyright notice and the `NOTICE` file in what you distribute, and don't use the project's name
to imply it endorses you.

The models it downloads by default are permissive too (Whisper MIT, Silero VAD MIT, Qwen2.5
Apache-2.0, Kokoro Apache-2.0), so the whole default path is clear for commercial use. A model
you point it at yourself carries its own licence — check that one before you ship it.

# otobongfp/code-graph-view

## 关联链接

- http://localhost:8000**
- http://localhost:8080/v1
- https://`,
- https://fusion-runtime.dev
- https://your-server/fusion-runtime.js

## 导航

- 项目页：[[10-项目/github.com_4c442d6d]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
