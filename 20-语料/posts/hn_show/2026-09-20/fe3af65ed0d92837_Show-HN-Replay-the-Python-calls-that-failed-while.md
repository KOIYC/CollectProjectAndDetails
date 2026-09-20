---
type: "corpus"
item_id: "fe3af65ed0d92837"
title: "Show HN: Replay the Python calls that failed while a dependency was down"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49714038"
project_url: "https://github.com/baldurhq/baldur"
author: "mcbg1541"
published_at: "2026-09-15T15:28:39Z"
captured_at: "2026-09-20T09:37:12+08:00"
lang: "en"
kind: "post"
topic: "开发者工具"
shard: "2026-09-20"
pub_day: "2026-09-15"
tags:
  - 语料
  - hn_show
  - author_mcbg1541
  - story_49714038
  - show_hn
metrics: {"points": 3, "comments": 0, "engagement_velocity": 3}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:90d"
---

# Show HN: Replay the Python calls that failed while a dependency was down

> [!info] 一句话导读
> Self-healing reliability layer for Python — circuit breaker, retry, and fallback behind a single decorator. Framework-agnostic core with Django, FastAPI, Flask,…

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49714038>
> 指标：点赞=3 · 评论=0 · engagement_velocity=3
> 作者：mcbg1541　|　发布：2026-09-15T15:28:39Z
> 项目链接：<https://github.com/baldurhq/baldur>
> 采集：2026-09-20T09:37:12+08:00　|　id：`fe3af65ed0d92837`

## 正文

# baldurhq/baldur

Self-healing reliability layer for Python — circuit breaker, retry, and fallback behind a single decorator. Framework-agnostic core with Django, FastAPI, Flask, and Celery adapters.

- Stars: 1
- Forks: 0
- Watchers: 1
- Open issues: 2
- License: Apache License 2.0
- Homepage: https://baldur.sh
- Default branch: main
- Created: 2026-06-30T12:38:18Z

## Languages

- Dockerfile
- HTML
- Python
- Shell

## Topics

- celery
- circuit-breaker
- dead-letter-queue
- django
- error-handling
- fastapi
- fault-tolerance
- flask
- prometheus
- python
- rate-limiting
- redis
- reliability
- resilience
- retry
- self-healing
- sre

## Top Contributors

- gotoUSA (464 contributions)
- dependabot[bot] (4 contributions)

---

## README

# Baldur

CI
Python 3.11+
License: Apache 2.0
PyPI
Docs
OpenSSF Best Practices

**Baldur** is a self-healing reliability layer for Python applications. It puts
circuit breaker, retry, and fallback behind a single decorator, so a flaky
downstream stops cascading into your service — and it ships the operational
surface you need to actually run that in production: health checks, Prometheus
and OpenTelemetry metrics, graceful shutdown, and a built-in web console. The
core is framework-agnostic, with first-class adapters for Django, FastAPI,
Flask, and Celery.

Terminal demo: the payment gateway dies mid-traffic — five failed charges are captured, the breaker trips, and on recovery Baldur replays all five. Zero lost.

*Real run of the shipped demo: the gateway dies mid-traffic — five charges
fail and are captured with their arguments, the circuit breaker opens and
shields the dying dependency, and the moment it closes again Baldur replays
all five for real. Zero lost. Reproduce it yourself:*

```bash
pip install "baldur-framework[celery]"
python -m baldur.scripts.demo_self_healing
```

*(The breaker states and DLQ tallies in the recording are read live from the
running framework. In your own service the same story surfaces as Baldur's
structured log events, live breaker state in the built-in web console, and
the Prometheus/OpenTelemetry metrics.)*

## Why Baldur?

- **One decorator, whole pipeline.** `@baldur.protected("name")` composes
 circuit breaker, retry with backoff, timeout, fallback, and idempotency into
 one ordered pipeline — instead of hand-wiring three separate libraries and
 hoping they interact correctly under failure.
- **Zero-config start, production path built in.** Out of the box everything
 runs on an in-memory backend — no Redis, no env vars, no Docker. When you
 move to multiple workers, add Redis and the same code shares state across
 the fleet. Call sites never change.
- **Operate it, don't just import it.** A built-in web console shows every
 breaker's live state and gives you runtime on/off controls; health checks
 tell your load balancer the truth; metrics come standard.
- **Framework-native.** Django, FastAPI, Flask, and Celery adapters wire the
 cache, metrics, and lifecycle hooks at startup, so protection works with
 your framework's idioms rather than around them.

## Install

The Python package is `baldur` (you `import baldur`); the PyPI distribution is
`baldur-framework`.

```bash
pip install baldur-framework                 # framework-agnostic core
pip install baldur-framework[django]         # Django integration
pip install baldur-framework[fastapi]        # FastAPI integration
pip install baldur-framework[flask]          # Flask integration
pip install baldur-framework[celery]         # Celery task protection
pip install baldur-framework[redis]          # Redis-backed shared state
pip install baldur-framework[prometheus]     # Prometheus metrics
```

## Quick example

```python
import baldur

@baldur.protected("charge-customer")
def charge(order_id: str) -> dict:
    # Wrapped in a circuit breaker by default. With zero configuration this
    # runs on an in-memory fallback — no Redis, no env vars, no Docker.
    return payment_gateway.charge(order_id)
```

When the payment gateway starts failing, the breaker opens and your service
answers fast instead of stacking up timeouts. Need more than the default?
Compose the pipeline declaratively:

```python
@baldur.protected(
    "charge-customer",
    retry=True,                              # retry with exponential backoff
    timeout=5.0,                             # per-call time budget
    fallback=lambda: {"status": "queued"},   # graceful answer while OPEN
    idempotency_key="order_id",              # dedupe concurrent duplicates
)
def charge(order_id: str) -> dict:
    return payment_gateway.charge(order_id)
```

Sync and async callables are both supported — the decorator auto-detects
coroutine functions.

## What's in the box (OSS, Apache-2.0)

| Capability | What it gives you |
|------------|-------------------|
| Circuit breaker | Stops cascading failure; bounded half-open probes on recovery |
| Retry with backoff | Exponential backoff with jitter and bounded attempts |
| Fallback & composition | One ordered pipeline for all resilience patterns |
| Idempotency | Concurrent duplicate calls execute the side effect exactly once |
| Bulkhead isolation | Each dependency gets a fixed slice of concurrency, so one slow dependency can't drain every worker |
| Dead-letter queue + replay | A call that fails for good is captured with its context and replayed once the dependency recovers |
| Health checks | Liveness/readiness that reflect real dependency state |
| Graceful shutdown | Drain in-flight work cleanly on restart and deploy |
| Metrics | Prometheus and OpenTelemetry, emitted by default |
| System control | Instant kill switch and dry-run mode for Baldur's automation — no redeploy |
| Web console | Built-in operations console: live breaker state, controls, recovery |
| Precomputed cache | Health/status endpoints answer from a warm cache, so constant probing stays cheap |

The read path heals the same way. Here a Django app under live HTTP traffic
(recorded from a demo harness driving it) loses its network path to Redis for
21 seconds — every request keeps returning 200 off the in-memory cache tier,
and the Redis tier resyncs itself on recovery:

Terminal demo: a Django app keeps serving 200s through a 21-second Redis outage

## Baldur PRO

PRO adds the durable, fleet-level machinery on top of the same API — nothing in
the core gets relicensed or replaced. Highlights:
DLQ at scale (batch replay from the
console, success-rate-driven pacing, a disk-durable outbox, and archive/purge
retention), hash-chained audit trail,
unified notifications,
emergency mode,
bulkhead thread-pool isolation,
adaptive throttling,
canary recovery,
governance gates, and a
meta-watchdog that watches Baldur itself.

See the full OSS vs PRO capability matrix and
pricing.

## Documentation

Full documentation lives at ** **.

- What is Baldur? — the problem it solves and how
- Getting started: Django ·
 FastAPI ·
 Flask ·
 Celery
- Concept guides — one page per capability, linked
 throughout this README
- API reference
- Troubleshooting
- Compatibility

## Using Baldur with AI assistants

Building with an AI coding assistant (Claude Code, Cursor, Copilot, Codex)? Run
`baldur init-ai` in your repo to drop an `AGENTS.md` (read by Cursor, Copilot,
and Codex) plus a `CLAUDE.md` that imports it for Claude Code — together they
teach the assistant to reach for `@baldur.protected("name")` instead of
hand-rolling a circuit breaker. See
Using Baldur with AI assistants.

## Compatibility

| Component | Minimum | Tested in CI |
|-----------|---------|--------------|
| Python | 3.11 | 3.11 · 3.12 · 3.13 |
| Django | 4.2 | 4.2 LTS · 5.2 LTS · 6.0 |
| FastAPI | 0.100 | latest ≥ floor (smoke) |
| Flask | 2.3 | latest ≥ floor (smoke) |
| Celery | 5.3 | 5.4 |
| Redis server | — | 7.x |

See Compatibility for the full matrix, the
Python × Django test grid, and the version support policy.

## Early access

Baldur is early, and it is looking for a small number of teams already running
a Python service in production to work with directly. If that is you, the
details and how to reach me are in
Discussions.

## License

Baldur is released under the Apache License 2.0 — see LICENSE and
NOTICE.

## Contributing

Contributions are welcome under the Apache License 2.0. Pull requests are
accepted through a sign-off-based DCO flow —
see CONTRIBUTING.md for the full model.

- **Ideas, or showing what you built** →
 Discussions.
- **Bugs / feature requests / docs** → open an issue or a pull request.
- **Security** → see SECURITY.md (no public issues for vulnerabilities).
- **Usage questions / commercial** → `support@baldur.sh`.

## 关联链接

- https://baldur.sh

## 导航

- 项目页：[[10-项目/github.com_40c1e136]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`开发者工具`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
