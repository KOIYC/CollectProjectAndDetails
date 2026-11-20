---
type: "corpus"
item_id: "d80cdb35ab3c8d25"
title: "Show HN: A deterministic agent memory engine in Rust with no LLM"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50567187"
project_url: "https://github.com/samvallad33/vestige"
author: "entity002"
published_at: "2026-11-19T22:11:48Z"
captured_at: "2026-11-20T09:45:52+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-11-20"
pub_day: "2026-11-19"
tags:
  - 语料
  - hn_show
  - author_entity002
  - story_50567187
  - show_hn
metrics: {"points": 2, "comments": 1, "engagement_velocity": 2}
comments_count: 1
comments_total: 1
discovered_via: "hn:show_hn:3d"
---

# Show HN: A deterministic agent memory engine in Rust with no LLM

> [!info] 一句话导读
> Deterministic Operating System and Causal Nervous System for Artificial Intelligence.

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50567187>
> 指标：点赞=2 · 评论=1 · engagement_velocity=2
> 作者：entity002　|　发布：2026-11-19T22:11:48Z
> 项目链接：<https://github.com/samvallad33/vestige>
> 采集：2026-11-20T09:45:52+08:00　|　id：`d80cdb35ab3c8d25`

## 正文

# samvallad33/vestige

Deterministic Operating System and Causal Nervous System for Artificial Intelligence.

- Stars: 661
- Forks: 73
- Watchers: 661
- Open issues: 11
- License: GNU Affero General Public License v3.0
- Homepage: https://github.com/samvallad33/vestige
- Default branch: main
- Created: 2026-01-25T07:31:09Z

## Languages

- CSS
- Dockerfile
- HTML
- JavaScript
- Python
- Rust
- Shell
- Svelte
- TypeScript

## Topics

- agent-security
- agentic-security
- ai-agents
- anthropic
- audit-log
- causal-proof-engine
- claude-code
- cursor
- developer-tools
- llm-security
- local-first
- mcp-security
- mcp-servers
- openclaw
- prompt-injection
- root-cause-analysis
- rust
- security
- security-kernel
- zero-trust

## Top Contributors

- samvallad33 (1259 contributions)
- cursoragent (176 contributions)
- claude (33 contributions)
- delandtj (12 contributions)
- randomnimbus (4 contributions)
- xsa-dev (3 contributions)
- Unforgettable-93 (3 contributions)
- caioribeiroclw-pixel (2 contributions)
- ShalokShalom (2 contributions)
- NoahToKnow (2 contributions)

---

## README

# VESTIGE

**/ˈvɛs.tɪdʒ/ · VESS-tij**

*From the Latin **vestīgium**, a physical footprint pressed into the earth, and the direct root of **investigate** (**in-vestīgāre**: to follow the track backward).*

### Deterministic, local-first memory and safety kernel for AI agents

Rust
License: AGPL-3.0
Release

No embeddings, no LLMs, no GPU, and no API keys. It runs locally on CPU.

---

## Why Vestige?

Roman trackers read *vestigia* in soil to reconstruct what passed through, how heavy it was, which way it moved, and how recently. Vestige does the same for agent memory. It records immutable footprints in an append-only log and walks the trail, instead of guessing meaning from a vector space.

Human memory systems solved truth, order, and provenance under hard limits for 5,000 years: Pāṇini's *anuvṛtti* carry-forward registers, *isnād* witness chains, Andean *khipu* top-cord rollups, Torrens title curtains, and the archaeological Harris matrix. Vestige takes those structural ideas onto a local Rust kernel.

---

## Architecture

- **Strata.** An append-only, hash-chained, signed log. Frames carry BLAKE3 payload digests and bi-temporal validity bounds (`valid_from_ms`, `valid_until_ms`). Admitted writes return receipts. Later claims supersede earlier ones; old facts stay on the log.
- **FSRS-6.** Spaced-repetition scheduling that lets unused noise fade.
- **RSB (Retroactive Salience Backfill).** The moat. *Cause never looks like the symptom.* A later turn can raise an earlier memory even when they share no words. Salience is set at write time, and new learning can raise or lower it later, a pattern described in Sheena Josselyn's engram research. In the birthday-dinner demo, a buried "felt off after Bangkok Garden" memory is raised once Maya's peanut allergy is recorded, so a later question about her birthday dinner can retrieve it.
- **Backfill.** Upstream causal walks from a failure or a later fact back to the earlier turn that caused it.
- **Rank-1 seating.** Deterministic slot-1 rules on the retrieved set, such as yielding an assistant reply to a covering user turn, with no vector index.
- **GhostLink.** Pairs recorded memories, each with a proof.
- **Operator hooks, one-use permits, and receipts.** `npx @vestige/init --guard` installs the Operator gate. A one-time owner permit lasts 15 minutes, is consumed once, and stops or allows write receipts.

---

## Benchmarks

These numbers measure retrieval: whether the right memory landed in the top k. They do not measure answer accuracy. They are the latest scores merged to `main`, from PR 709 (RSB v4, commit `5fb269b0`). Runs used the local `retrieval_bench` binary on an Intel Core i5-2520M with 8 GB RAM, CPU only, with no embeddings, no LLM, no GPU, and no API keys.

| Benchmark | Level | Metric | Score |
| :--- | :--- | :--- | :--- |
| **LoCoMo-10** CORE (1,536 questions) | Turn | Exact R@1 / R@5 | **736/1536 (47.92%)** / **1030/1536 (67.06%)** |
| **LongMemEval-S** official (470 non-abstention) | Session | Any@1 / Any@5 / All@5 / NDCG@10 | **423/470 (90.00%)** / **458/470 (97.45%)** / **407/470 (86.60%)** / **0.9229** |
| **LongMemEval-S** official (470 non-abstention) | Turn | Any@1 / Any@5 | **255/470 (54.26%)** / **364/470 (77.45%)** |
| **BEAM 100K** (355 scored questions) | Turn | Any@5 / MRR | **203/355 (57.18%)** / **0.4563** |
| **MemoryAgentBench** QA2 421K (100 questions) | Document | All@5 | **85/100 (85.00%)** |

Reproduce:

```bash
bash benchmarks/run_all.sh
```

Full tables and method notes are in benchmarks/README.md.

---

## Quick start

```bash
npx @vestige/init --guard
```

That sets up local binaries and an MCP connection for any AI agent. `--guard` adds the Operator gate. The MCP command is `vestige-mcp`:

```json
{
  "mcpServers": {
    "vestige": { "command": "vestige-mcp" }
  }
}
```

From source:

```bash
git clone https://github.com/samvallad33/vestige.git
cd vestige
cargo build --release --package vestige-mcp
```

More in Getting started.

---

## License

Built by Sam Valladares (@samvallad33). Licensed under AGPL-3.0.

*Follow the footprints.*

# FallDownTheSystem/modern-hn

## 评论（1/1）

> **0c3ca83** · 2026-11-19T22:14:19.000Z　
> If there's no LLM, why is the repo full of LLM turds?

## 关联链接

- https://github.com/samvallad33/vestige.git

## 导航

- 项目页：[[10-项目/github.com_6fb0413f]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
