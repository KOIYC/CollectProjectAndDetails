---
type: "corpus"
item_id: "5849687f97ebbe37"
title: "Show HN: Hillock: Local neuro-symbolic memory engine in <1.2GB VRAM"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49501209"
project_url: "https://github.com/roandejager/Hillock"
author: "roandejager5"
published_at: "2026-08-30T18:10:46Z"
captured_at: "2026-09-21T03:11:29+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-21"
pub_day: "2026-08-30"
tags:
  - 语料
  - hn_show
  - author_roandejager5
  - story_49501209
  - show_hn
metrics: {"points": 12, "comments": 3, "engagement_velocity": 12}
comments_count: 3
comments_total: 3
discovered_via: "hn:show_hn:52d"
---

# Show HN: Hillock: Local neuro-symbolic memory engine in <1.2GB VRAM

> [!info] 一句话导读
> License: GNU Affero General Public License v3.0

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49501209>
> 指标：点赞=12 · 评论=3 · engagement_velocity=12
> 作者：roandejager5　|　发布：2026-08-30T18:10:46Z
> 项目链接：<https://github.com/roandejager/Hillock>
> 采集：2026-09-21T03:11:29+08:00　|　id：`5849687f97ebbe37`

## 正文

# roandejager/Hillock

- Stars: 5
- Forks: 0
- Watchers: 5
- Open issues: 0
- License: GNU Affero General Public License v3.0
- Default branch: master
- Created: 2026-06-11T20:18:44Z

## Languages

- Python

## Top Contributors

- roandejager (46 contributions)

---

## README

# Hillock 🧠

Hi! This is **Hillock**, a local, personal memory system that integrates symbolic data structures with high-dimensional vector computing. I started hacking on this because standard vector databases always felt way too heavy, expensive, and over-engineered just to run a quick, offline chatbot on my own computer.

⚠️ **Heads up:** This project is very much a work in progress and honestly, it isn't all that yet. Right now it's a personal, highly experimental research prototype. However, the ultimate ambition is to build a mathematically sound, completely gradient-free cognitive layer for secure, privacy-first local applications.

---

## ⚙️ How It Works (The General Flow)

Here is a quick look at how data moves through the system:

```text
       [Raw Text / PDFs]
               │
               ▼  (Parallel Ingestor)
       [ Ollama (Qwen3) ]
         │            │
         ▼            ▼
    [SQLite Graph]  [Hebbian Memory]
         │            │
         └─────┬──────┘
               ▼
       [VSA/HDC Reservoir] ──► [Gating Controller (Hillock)]
```
*(Note: This ASCII diagram was made with AI, so it might not be 100% correct or perfectly aligned, but it shows the general idea of how things connect.)*

Basically, it splits the work into a few different layers:
* 💾 **SQLite Graph**: Stores the permanent, hard facts as simple triples (like `Marie_Curie` -> `born_in` -> `Poland`) so the system has a solid ground truth.
* ⚡ **Hebbian Plasticity**: Dynamically tracks which entities are being talked about in the chat and strengthens the connections between them, like a simple digital synapse.
* 🌀 **Hyperdimensional Computing (HDC)**: Uses a 10,000-dimensional vector that constantly updates with conversational history, which helps the system resolve pronouns (like "he" or "she") and decide when to block a query to prevent hallucinations.

---

## 📹 Live Interactive Demo (Terminal Cast)

Here is a short terminal recording showing Hillock ingesting a document in real-time, mapping associations, and aggressively blocking an unanswerable question to prevent an LLM hallucination:

Hillock Gating Demo

---

## 📊 Scientific Benchmarking Baselines

We evaluated Hillock under our **Long-Form Research Benchmark**, consisting of a highly complex, 30-sentence historical/scientific text and 30 diverse queries (including hard negatives designed to bait hallucinations).

To ensure absolute scientific honesty and avoid the "evaluation inflation" common in modern AI projects, we run our benchmarks cold on a completely wiped, fresh database. Using a local, heavy **Qwen 3 (5.2B)** model on consumer hardware, here are our exact baseline metrics:

| Metric | Score | Diagnostic Meaning |
| :--- | :---: | :--- |
| **Extraction Precision** | **10.6%** | Percentage of extracted database triples that were perfectly structured. |
| **Extraction Recall** | **22.7%** | Completeness of automatically indexed relations over the 30 complex sentences. |
| **Retrieval Accuracy** | **30.0%** | Exact-string match accuracy on answerable historical queries. |
| **Gate Accuracy** | **30.0%** | Gating success rate (blocking unanswerable queries/hard negatives). |

### The "Qwen 3" Paradox (Why the scores are what they are):
* **The Ingestion Bottleneck**: A 30-sentence dense academic text is highly complex. A local model easily gets confused by multi-clause grammar. It extracted noisy relations like `[Grace_Hopper] -[became_a_pioneer]-> [developed_the_first_compiler]` instead of a clean `[Grace_Hopper] -[developed]-> [compiler]`.
* **The expressiveness penalty**: Interestingly, Qwen 3 actually performed *worse* on paper than Qwen 2 (1.5B). This is because Qwen 3 is *too* smart and expressive. Instead of extracting rigid, simple triples like `[Marie_Curie] -[born_in]-> [Poland]`, it extracted beautifully natural, historically accurate triples like `[Marie_Curie] -[spent_childhood_in]-> [Poland]`. The strict, exact-string evaluation harness penalized this, proving how rigid standard AI benchmarks are, and why we need flexible semantic path matching in future versions.
* **Stable Vector Normalization**: Despite the small model extraction noise, the HDC Semantic Matcher itself is mathematically highly stable. By keeping all candidate facts strictly bound to exactly 3 unique components (Subject, Object, and best-matching Predicate word), we prevent shorter facts from having artificially higher similarity scores.

---

## 🚀 Quick Start (How to run it)

If you want to try running this prototype, it is highly recommended to set up a clean Python virtual environment so you do not mess up your global packages. You will also need Ollama installed and running locally.

### 1. Clone and Navigate
```bash
git clone https://github.com/roandejager/Hillock.git
cd Hillock
```

### 2. Set Up Virtual Environment
```bash
# Create the environment
python -m venv .venv

# Activate it (Windows)
.venv\Scripts\activate

# Activate it (Mac/Linux)
source .venv/bin/activate
```

### 3. Install Dependencies & Pull Model
```bash
pip install -r requirements.txt
ollama pull qwen3:latest
```

### 4. Start the Chat Console
```bash
python main.py
```

Inside the console, you can use these commands:
* `/ingest [filepath]` — Index a local `.txt` or `.pdf` file.
* `/mode [strict/balanced/conversational]` — Change how conversational the AI is.
* `/reset` — Wipe the SQLite database and reset the HDC memory space.

---

## ⚖️ Licensing & Contributions

Hillock is licensed under the **GNU Affero General Public License v3.0 (AGPL-3.0)**.

To preserve our ability to dual-license the project commercially in the future (for companies who cannot open-source their code under AGPL restrictions) while keeping the core project open and free for hobbyists, all contributors must sign our **Contributor License Agreement (CLA)**.

Our automated bot (via `cla-assistant.io`) will automatically guide you through signing the CLA when you open a Pull Request. For details, see `CONTRIBUTING.md` and `CLA.md`.

---

## 📂 File Reference

* `config.py` — Holds all the hyperparameters (HDC dimensions, decay rates, etc.).
* `database.py` — The SQLite interface for symbolic fact storage.
* `ingestor.py` — Spawns parallel worker threads to chunk and parse documents.
* `plasticity.py` — Tracks Hebbian co-activation weights between concepts.
* `reservoir.py` — The vector symbolic architecture context math.
* `main.py` — Orchestrates the console loop, pronoun resolution, and gating.
* `evaluate_hillock_PROTO_ish.py` — The automated long-form evaluation script.

# mainak55512/flint

## 评论（3/3）

> **roandejager5** · 2026-08-30T18:12:02.000Z　
> Hey HN! I am Roan, and I built Hillock: a 100% local, offline neuro-symbolic memory engine built for consumer hardware (runs in <1.2 GB VRAM on a GTX 1070 or on pure CPU laptops).
> Why not standard vector RAG?Dense vector databases and 8B+ extraction models are heavy on local hardware, suffer from semantic drift, and still hallucinate when out of context. Hillock explores a deterministic alternative: SQLite Knowledge Graph: Stores ground-truth facts as relational Subject-Predicate-Object triples (zero vector drift).
>
>  Hebbian Plasticity Engine: Gradient-free associative learning across turns to surface primed context.
>
>  10,000-D Hyperdimensional Computing (VSA/HDC): Sub-millisecond similarity gating directly on CPU in discrete bipolar space.
>
>  TALON Extraction Stack: 3-stage local extraction (Fastcoref + MiniLM + GLiREL) with type-constrained schema validation, running offline without cloud calls.
>
> Refusal is Control Flow (Not Prompting)Instead of prompting an LLM to "only answer if you know", Hillock's gate is an actual programmatic check. If candidate facts fail our similarity threshold with positive predicate intent, it returns a hardcoded refusal immediately. The local LLM (Ollama) is never called with un-evidenced context, saving 100% of GPU compute on unanswerable queries.
> What is New in v0.6 (HYDRA & HyperGraph) HYDRA (Bipolar MaxSim): Adapted ColBERT-style token-level MaxSim to discrete bipolar vectors. A 2,000-D Sub-Dimensional Projection Cascade early-rejects ~95% of candidates on CPU in ~0.5ms.
>
>  HYPERGRAPH-HDC: Uses positional cyclic shifts to break binding commutativity, encoding 2-hop and 3-hop relational paths without combinatorial RAM explosion.
>
> Benchmarks (Unseeded 32-query run on a laptop CPU) Answerable Retrieval Accuracy: 54.5% (Fast-eval in 1.16s on CPU)
>
>  Hard-Negative Block Rate: 60.0% (stops trick queries cold)
>
>  Extraction Recall: 59.1% | Pooled Gate Accuracy: 56.2%
>
> Known LimitationsRetrieval quality is strictly bounded by extraction recall: if the extractor misses a fact during ingestion, the gate honestly refuses (producing a false block).The project is AGPL-3.0 licensed with 1-click quickstart launchers (run.bat / run.sh) and a standalone 21-point CPU verification suite (verify_hillock.py).GitHub: https://github.com/roandejager/HillockI would love to hear your thoughts, feedback, and critiques!

---

> **toplinesoftsys** · 2026-08-30T23:05:09.000Z　
> I did not try to play with it yet, but from what I read - it is a great idea.

---

> **roandejager5** · 2026-08-31T18:32:17.000Z　
> thanks, let me know what you think

## 关联链接

- https://github.com/roandejager/Hillock.git

## 导航

- 项目页：[[10-项目/github.com_a0359311]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
