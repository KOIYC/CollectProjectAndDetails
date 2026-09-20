---
type: "corpus"
item_id: "de2fdadcd5f1fccc"
title: "Show HN: MemoryOps AI – governed memory lifecycle for AI assistants"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=48731779"
project_url: "https://github.com/patibandlavenkatamanideep/memoryops-ai"
author: "pvmanideep20"
published_at: "2026-06-30T12:29:41Z"
captured_at: "2026-09-21T02:53:08+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-21"
pub_day: "2026-06-30"
tags:
  - 语料
  - hn_show
  - author_pvmanideep20
  - story_48731779
  - show_hn
metrics: {"points": 3, "comments": 0, "engagement_velocity": 3}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:113d"
---

# Show HN: MemoryOps AI – governed memory lifecycle for AI assistants

> [!info] 一句话导读
> patibandlavenkatamanideep/memoryops-ai

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=48731779>
> 指标：点赞=3 · 评论=0 · engagement_velocity=3
> 作者：pvmanideep20　|　发布：2026-06-30T12:29:41Z
> 项目链接：<https://github.com/patibandlavenkatamanideep/memoryops-ai>
> 采集：2026-09-21T02:53:08+08:00　|　id：`de2fdadcd5f1fccc`

## 正文

# patibandlavenkatamanideep/memoryops-ai

Governed memory runtime for AI assistants: policy-before-storage, context admission, memory usage trace, deletion proof, leakage evals, auth adapters, vector backends, observability, evidence bundles, SDK, benchmarks, and agent integrations.

- Stars: 15
- Forks: 3
- Watchers: 15
- Open issues: 0
- License: MIT License
- Homepage: https://memoryops-ai-production.up.railway.app/
- Default branch: main
- Created: 2026-06-20T20:35:17Z

## Languages

- CSS
- Dockerfile
- JavaScript
- PLpgSQL
- Procfile
- Python
- TypeScript

## Top Contributors

- patibandlavenkatamanideep (138 contributions)
- dependabot[bot] (16 contributions)

---

## README

# MemoryOps AI

**An open-source governed memory runtime for production AI assistants.**

It controls **what becomes memory, what enters context, what must be forgotten, what
influenced an answer, and what evidence proves each decision** — treating memory as
governed state, not just a vector database.

CI
 Benchmark
 PyPI
 Python
 License
 API

> **Two version tracks:** the **platform release** (`v2.3`, the repo's feature
> milestone) is separate from the **public API + SDK contract** (`1.x`, an additive-
> compatibility promise). See docs/api-stability.md.

## Live demo

**memoryops-ai-production.up.railway.app** —
the Playground runs the real governed pipeline in-process with ephemeral session state.

MemoryOps lifecycle demo

## Try it in 30 seconds

Install the published SDK, point it at a running API, and make one scoped call that
captures and later uses memory:

```bash
# Terminal 1 — the governed API (in-memory store, no infra, no keys)
cd services/api && python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
MEMORYOPS_STORAGE=memory uvicorn app.main:app --port 8000
```

```bash
# Terminal 2 — the SDK from PyPI
pip install memoryops-sdk
python3 - <<'PY'
from memoryops import MemoryOpsClient
with MemoryOpsClient("http://127.0.0.1:8000", "demo_tenant", "demo_user") as mo:
    mo.chat("Remember that I prefer metric units.")
    reply = mo.chat("Which units should I use for distances?")
    print(reply.assistant_message)
    print([m.content for m in reply.used_memories])
PY
```

Full setup (Docker Compose, Postgres/pgvector, embeddings, LLM adapters, frontend):
**docs/quickstart.md**. SDK details: **docs/assistant-sdk.md**.

## Why this exists

Most AI "memory" is `message → vector DB → retrieve later`. MemoryOps adds the
governance that production needs:

```text
WRITE  Message → Extractor → Policy Broker → Write Service → Typed Store → Audit Log
READ   Message → Retriever → Ranker → Context Composer → Response
BACKGROUND  Decay · Reflection · Conflict · Compression
PLANES      Security · Governance · Observability · Evaluation · Reliability
```

```mermaid
flowchart LR
    M["chat message"] --> GW["Gateway"]
    GW --> EX["Extractor"] --> PB["Policy Broker"] --> WS["Write Service"] --> ST[("Typed Store")]
    GW --> RT["Retriever"] --> RK["Ranker"] --> CC["Context Composer"] --> RESP["Response"]
    PB --> AUD[["Audit Log (append-only)"]]
    WS --> AUD
```

Full design, diagrams, and where each invariant is enforced:
**docs/architecture.md**.

## Enterprise invariants (enforced in code + tests)

1. **Tenant isolation** — one user's memory is never returned to another user/tenant.
2. **Deletion guarantee** — deleted memories are never retrieved again.
3. **Provenance** — every memory traces back to its source.
4. **Graceful degradation** — retrieval failure never blocks a response.
5. **Policy-before-storage** — unsafe/secret-like content is filtered before storage.
6. **Temporary chat** — temporary sessions never read or write memory.
7. **Auditability** — every lifecycle mutation and its audit event commit together in
 one transaction, across both the API/governance write paths and the background
 lifecycle workers, as an append-only, tamper-evident chain.
8. **Explainability** — the system can show which memories affected a response.
9. **Typed memory** — episodic/semantic/procedural/project/knowledge/system differ.
10. **Evaluation** — memory quality is testable via a golden set, not manual inspection.

## Benchmark — governance is measured, not claimed

`python benchmark/run_benchmark.py` scores the eval harness into named suites; the two
**critical** suites (deletion/leakage + tenant isolation) must be perfect or it fails.
Reproducible and offline (no keys); the same suites also run against real
Postgres + pgvector in CI (the `api-postgres` job). Current
scorecard — **50/50 (100%), critical suites perfect ✅**:

| Suite | Pass rate | | Suite | Pass rate |
| --- | --- | --- | --- | --- |
| deletion_and_leakage ★ | 12/12 | | policy_governance | 15/15 |
| tenant_isolation ★ | 17/17 | | retrieval_quality | 4/4 |
| context_admission | 2/2 | | ★ critical (must be 100%) | |

## What's shipped

All capabilities v1.3 → v2.3 are shipped: Context Admission Gate + Memory Usage Trace,
deletion-proof tombstone lineage, deleted-memory leakage evals, auth/authorization
adapters (JWT/JWKS + trusted header), vector-backend abstraction (Postgres/pgvector ·
in-memory · Qdrant · LanceDB · Weaviate), distributed tracing + Prometheus metrics,
Recall/Output gates, the Enterprise Evidence Layer (tamper-evident audit + evidence
bundles), agent-framework integrations, a public governance benchmark, transactional
mutation+audit with a fork-proof audit chain, and a fail-closed production profile
(`MEMORYOPS_PROFILE=production`) with dependency-aware readiness. Details in the
**CHANGELOG** and **docs/architecture.md**.

**Adapter honesty:** Postgres/pgvector and in-memory are *fully tested in CI* (suite +
evals + benchmark + enforced RLS). Qdrant/LanceDB/Weaviate are *contract-tested*.
Framework integrations (LangGraph · LlamaIndex · CrewAI · AutoGen · Semantic Kernel ·
OpenAI Agents SDK) are *import-guarded examples*, not live-service tested. See
**docs/adapters/**.

## Known gaps (what MemoryOps does *not* yet claim)

Kept explicit on purpose — see **docs/limitations.md** for the
authoritative list. The material ones:

- **Real-model extraction quality is measured, but on a small set.** A live run on a
 25-turn labeled set with **gemini-2.5-flash** scores **0.94 precision / 0.94 recall /
 0.94 F1 with zero fallbacks** (vs. the offline stub's 1.00 / 0.53 / 0.69), recorded in
 EXTRACTION_QUALITY.md. Broader provider/model
 coverage and larger datasets remain future work — add a key and more rows fill in:
 `python evals/run_extraction_quality.py --provider openai` (needs `OPENAI_API_KEY`).
- **The request path is synchronous.** Under load, throughput is flat and latency grows
 with concurrency in a single process (docs/performance.md); the
 cause is not yet isolated, and the async decision is deferred until the I/O-bound
 measurement (real provider + Postgres) exists.
- **No external baseline** in the benchmark yet, and **no crypto-shred / physical
 erasure** (deletion compaction is auditable content/vector clearing + tombstone).

## Deployment

Railway only (no Vercel): one project, five services (web · api · worker · Postgres ·
Redis). See **docs/deployment/railway.md**.

## Documentation

- docs/quickstart.md — full local setup (Docker, Postgres, embeddings, LLM adapters, frontend).
- docs/architecture.md — write/read paths, planes, invariants, diagrams.
- docs/api-stability.md — the stable `1.x` API + SDK surface and deprecation policy.
- docs/production-readiness.md — invariants/planes → where enforced; production vs demo.
- docs/limitations.md — the authoritative list of what MemoryOps does **not** claim.
- docs/security.md · docs/governance.md — trust boundaries, lifecycle, approvals, audit.
- docs/assistant-sdk.md — the Python SDK + integration examples.
- docs/design-decisions.md — the hard calls and rejected alternatives.
- CHANGELOG.md · infra/adr/ — release history and Architecture Decision Records.

The **agentic engineering layer** (Hermes operator skills, agentic-swe-kit phase gates,
the PR Invariant Evidence Gate) wraps the core and is never on the chat request path —
see docs/integrations/README.md.

# sod — SSH keys sealed in the Secure Enclave

## 关联链接

- http://127.0.0.1:8000
- https://memoryops-ai-production.up.railway.app/

## 导航

- 项目页：[[10-项目/github.com_56d45507]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
