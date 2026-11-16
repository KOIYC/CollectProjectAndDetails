---
type: "corpus"
item_id: "e4ca0aaad4d0d89e"
title: "Show HN: Folate – Local DOM selector model that beats 7B VLMs at 1/60th the size"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50507874"
project_url: "https://github.com/figranium/folate"
author: "asernasr"
published_at: "2026-11-15T15:55:36Z"
captured_at: "2026-11-16T10:00:05+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-11-16"
pub_day: "2026-11-15"
tags:
  - 语料
  - hn_show
  - author_asernasr
  - story_50507874
  - show_hn
metrics: {"points": 2, "comments": 0, "engagement_velocity": 2}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:3d"
---

# Show HN: Folate – Local DOM selector model that beats 7B VLMs at 1/60th the size

> [!info] 一句话导读
> A lightweight, CPU-efficient neural DOM element ranker built for browser automation

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50507874>
> 指标：点赞=2 · 评论=0 · engagement_velocity=2
> 作者：asernasr　|　发布：2026-11-15T15:55:36Z
> 项目链接：<https://github.com/figranium/folate>
> 采集：2026-11-16T10:00:05+08:00　|　id：`e4ca0aaad4d0d89e`

## 正文

# figranium/folate

A lightweight, CPU-efficient neural DOM element ranker built for browser automation

- Stars: 1
- Forks: 0
- Watchers: 1
- Open issues: 1
- License: Apache License 2.0
- Default branch: main
- Created: 2026-11-14T12:25:04Z

## Languages

- Python

## Top Contributors

- asernasr (32 contributions)

---

## README

 PyPI •
 Hugging Face •
 Demo •
 Apache 2.0

 A lightweight, CPU-efficient neural DOM element ranker built for browser automation within tight memory constraints (<2 GB total footprint alongside a headless browser).

Fine-tuned from `google/electra-base-discriminator` on `osunlp/Mind2Web` and dynamically quantized to **INT8 ONNX (~107 MB)**, Folate runs purely via `onnxruntime` and `tokenizers`—requiring no PyTorch or `transformers` at inference time.

---

## Model Overview

Folate operates as a discriminative cross-encoder that scores `(natural_language_query, serialized_dom_element)` pairs in a single batched forward pass on CPU.

| Variant / Artifact | Backbone | Precision / Format | Disk Size | Runtime RAM |
| :--- | :--- | :--- | :--- | :--- |
| **`folate-int8` (Default)** | `google/electra-base-discriminator` | Dynamic `QUInt8` ONNX | ~107 MB | ~180–250 MB |
| **`folate-base`** | `google/electra-base-discriminator` | `float32` Safetensors | ~418 MB | ~1.4+ GB (PyTorch) |

### Key Capabilities

* **Zero-Hallucination Selector Grounding** — Ranks real interactive DOM nodes extracted via `lxml` XPath (` `, ` `, ` `, ` `, ` `, ARIA interactive roles, and `onclick`/`tabindex` elements), guaranteeing every returned CSS/XPath selector exists on the live page.
* **Compact Structured Serialization** — Serializes each element into a concise `96`-token representation:
 `[TAG] ... [ID/NAME/TYPE/ROLE/ARIA-LABEL/PLACEHOLDER/TITLE/ALT/HREF/DATA-TESTID] ... [TEXT] ... [PARENT] ...`
* **Edge & Low-Memory Deployment** — Designed to run alongside Chromium on resource-constrained laptops and containers without GPU acceleration.

---

## Quickstart

### Installation

```bash
pip install folate
```

Or install from source:

```bash
git clone https://github.com/figranium/folate
cd folate
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

To run the live browser examples with Playwright:

```bash
python -m pip install -r examples/requirements.txt
python -m playwright install chromium
```

### Usage

`FolateSelectorFinder` automatically downloads and caches `figranium/folate` on first run (or loads `./folate-int8` if present locally):

```python
from folate import FolateSelectorFinder

finder = FolateSelectorFinder()
matches = finder.rank("click Search Flights button", html_source, top_k=3)

for match in matches:
    print(f"{match['score']:.4f} | {match['selector']} | {match['element']}")
```

To load weights from a custom local directory:

```python
finder = FolateSelectorFinder(model_dir="./folate-int8")
```

### Programmatic Model Download

If you want to pre-fetch the quantized model weights via `huggingface_hub`:

```bash
hf download figranium/folate --local-dir ./folate-int8
```

---

## Repository Structure

```text
folate/
├── folate/
│   ├── __init__.py
│   └── ranker.py                  # Lightweight CPU inference engine & DOM serializer
├── scripts/
│   ├── prepare_data.py            # Streaming Mind2Web serializer (lxml)
│   ├── train.py                   # Fine-tuning script (bf16/fp16/CPU)
│   ├── export_onnx.py             # FP32 ONNX export + INT8 dynamic quantization
│   ├── eval_mind2web.py           # Official Mind2Web evaluator (Precision/Recall/F1, Top-1/3/5 & MRR)
│   └── eval_precision.py          # Playwright DOM-resolved selector Precision & Recall benchmark
├── examples/
│   ├── test_google.py             # Live Playwright search box grounding on google.com
│   ├── test_amazon.py             # E-commerce element ranking on amazon.com (+ offline snapshot)
│   ├── test_github.py             # Repository navigation grounding on github.com
│   └── requirements.txt           # Optional Playwright dependency for live browser tests
├── requirements.txt               # Lightweight CPU runtime dependencies
├── requirements-train.txt         # Training & ONNX export dependencies
└── LICENSE
```

---

## Evaluation & Benchmarks

Folate is evaluated on the three standard generalization splits of **Mind2Web** (`test_task`, `test_website`, and `test_domain`) across **6,037 action steps** on real-world webpages.

### Mind2Web Results (INT8 ONNX · CPU)

| Split | Description | Steps | Avg Candidates | Top-1 | Top-3 | Top-5 | MRR | Avg Latency (2 vCPU) |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **`test_task`** | Unseen tasks on seen websites | 1,256 | 50.0 | **93.31%** | 97.61% | 98.33% | 0.9566 | 2,309.9 ms/step |
| **`test_website`** | Completely unseen websites | 955 | 50.0 | **88.90%** | 95.92% | 96.65% | 0.9274 | 4,328.2 ms/step |
| **`test_domain`** | Unseen domains & verticals | 3,826 | 49.8 | **92.08%** | 97.28% | 98.61% | 0.9491 | 2,431.0 ms/step |

### Methodology & Setup

* **Task Formulation:** At each step, the model receives the natural-language task instruction, action history context, and up to **50 candidate DOM elements** (`Avg Candidates ≈ 50.0`) extracted from the page snapshot, and outputs a relevance logit per candidate.
* **Metrics:**
 * **Top-1 / Top-3 / Top-5:** Percentage of steps where a ground-truth target node (`pos_candidates`) appears within the top *k* ranked elements.
 * **Precision / Recall / F1:** Selective Top-1 precision (`TP / (TP + FP)`) and recall (`TP / Total`) across confidence probability thresholds (`--confidence-threshold`, `--thresholds`), plus candidate-level binary precision/recall.
 * **MRR (Mean Reciprocal Rank):** Average reciprocal rank for the highest-ranked ground-truth element across all evaluated steps.
* **Hardware & Runtime:** Latency is measured end-to-end per step on **2 vCPUs** with **no GPU acceleration**, using the exported INT8 quantized ONNX artifact (`onnxruntime`). Variance between `test_website` (`4,328.2 ms/step`) and `test_domain` (`2,431.0 ms/step`) reflects longer tokenized DOM attribute sequences on unseen site templates rather than candidate count.

### Comparison with GPT-6 Luna

For context against a fast, cost-efficient frontier LLM, **GPT-6 Luna** (via OpenAI's Decisions API) scores **81.8%** on **Mind2Web Multimodal** (Google Gemini Decision 1 evaluation, Nov 2026) and **81.2%** on **Mind2Web** in the Decision Index Vision suite (Nace.AI, Nov 2026), with ~326 ms median cloud API latency and ~$0.10 per 1,000 decisions (or $0.10 / $0.50 per 1M input/output tokens in standard API usage).

| Model | Type | Mind2Web Accuracy | Deployment & Runtime | Cost |
| :--- | :--- | :---: | :--- | :--- |
| **Folate (`folate-int8`)** | Specialized DOM Cross-Encoder (~107 MB) | **88.90% – 93.31%** Top-1 (91.83% overall across 6,037 steps) | 100% local CPU (`onnxruntime`, 180–250 MB RAM) | **$0** (self-hosted) |
| **GPT-6 Luna** | Frontier LLM (Decisions API) | 81.2% – 81.8% (Mind2Web Multimodal / Vision) | Cloud API (~326 ms median latency) | ~$0.10 / 1k decisions |

> **Note:** Folate is evaluated on text-based Mind2Web DOM candidates (50 candidates/step), whereas GPT-6 Luna's 81.2%–81.8% scores are on multimodal/screenshot-based Mind2Web action selection. While GPT-6 Luna is a general-purpose frontier model capable of broad reasoning and multi-step planning, Folate's task-specific ELECTRA cross-encoder achieves higher single-step DOM element grounding accuracy locally on CPU with zero API cost, zero network dependency, and zero selector hallucination.

---

## Examples

Run any of the included live browser examples from the repository root:

```bash
python examples/test_google.py
python examples/test_amazon.py --offline
python examples/test_github.py
```

---

## Training & Quantization Pipeline

To reproduce data preparation, fine-tuning, INT8 ONNX export, and evaluation from scratch on `osunlp/Mind2Web`:

```bash
python -m pip install -r requirements-train.txt

# 1. Stream and serialize Mind2Web pairs
python scripts/prepare_data.py --output-dir ./data

# 2. Fine-tune ELECTRA cross-encoder
python scripts/train.py --data-dir ./data --save-dir ./folate-base

# 3. Export to FP32 ONNX and quantize to INT8 (~107 MB)
python scripts/export_onnx.py --model-dir ./folate-base --output-dir ./folate-int8

# 4. Evaluate Mind2Web test splits (Precision, Recall, F1, Top-1/3/5 & MRR)
python scripts/eval_mind2web.py --confidence-threshold 0.5 --json-out mind2web_results.json

# 5. Run Playwright DOM-resolved selector Precision & Recall benchmark
python scripts/eval_precision.py --confidence-threshold 0.5 --json-out precision_results.json
```

---

## Intended Use & Limitations

* **Intended Use:** Single-step natural-language UI element grounding (`click`, `type`, `select`, `hover`) in local browser automation pipelines where RAM and CPU budgets are constrained.
* **Limitations:**
 * **No Multi-Step Planning:** Folate ranks candidate elements for a single action query; it does not plan multi-step workflows or parse unstructured page content.
 * **Local DOM Context Only:** Elements are serialized using their own attributes, inner text, and immediate `[PARENT]` tag—identical sibling elements without distinguishing attributes or text cannot be disambiguated visually.

---

## License

Folate is released under the Apache 2.0 License.

# ArchLog — Engineering Institutional Memory

## 导航

- 项目页：[[10-项目/github.com_751ad246]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
