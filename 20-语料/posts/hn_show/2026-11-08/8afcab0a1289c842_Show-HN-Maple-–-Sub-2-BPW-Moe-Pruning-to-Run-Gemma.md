---
type: "corpus"
item_id: "8afcab0a1289c842"
title: "Show HN: Maple – Sub-2-BPW Moe Pruning to Run Gemma 4 26B at 45 TPS on a 6GB GPU"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50410253"
project_url: "https://github.com/AmSach/maple"
author: "AmSach"
published_at: "2026-11-08T03:48:04Z"
captured_at: "2026-11-08T12:50:31+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-11-08"
pub_day: "2026-11-08"
tags:
  - 语料
  - hn_show
  - author_AmSach
  - story_50410253
  - show_hn
metrics: {"points": 2, "comments": 0, "engagement_velocity": 2}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:3d"
---

# Show HN: Maple – Sub-2-BPW Moe Pruning to Run Gemma 4 26B at 45 TPS on a 6GB GPU

> [!info] 一句话导读
> MAPLE: Manifold-Activated Pruning of Latent Experts for Sub-2-BPW MoE LLMs

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50410253>
> 指标：点赞=2 · 评论=0 · engagement_velocity=2
> 作者：AmSach　|　发布：2026-11-08T03:48:04Z
> 项目链接：<https://github.com/AmSach/maple>
> 采集：2026-11-08T12:50:31+08:00　|　id：`8afcab0a1289c842`

## 正文

# AmSach/maple

MAPLE: Manifold-Activated Pruning of Latent Experts for Sub-2-BPW MoE LLMs

- Stars: 0
- Forks: 0
- Watchers: 0
- Open issues: 0
- License: Other
- Default branch: master
- Created: 2026-11-07T17:32:34Z

## Languages

- Batchfile
- Python

## Top Contributors

- AmSach (16 contributions)

---

## README

# MAPLE: Manifold-Activated Pruning of Latent Experts

License
DOI
Google Scholar
Hugging Face
Direct Download
Format
Hardware

> **Sub-2-BPW Structural Compression for Mixture-of-Experts (MoE) LLMs**
> Compressing **Gemma 4 26B-A4B** from **9.92 GB to 4.75 GB** (1.48 effective bits/param), enabling **100% In-VRAM GPU Execution** on 6 GB laptop GPUs with **45.4 Tokens/Second** throughput.

**Author**: Aman Sachan (Google Scholar | amansachan92905@gmail.com)
**Organization**: Independent Systems Research

---

## Domain Specialization: Technical Reasoning and Code Synthesis

> **Model Focus:**
> This 4.75 GB checkpoint is profiled and pruned specifically for **Python programming, algorithm synthesis, data structures, and formal STEM reasoning**.
> By excising 80 dormant multilingual and general conversational experts, the active 48-expert manifold preserves deductive reasoning and syntax generation while fitting entirely within consumer 6 GB VRAM.

### Custom Domain MoE Pruning Pipeline
The MAPLE pruning pipeline is domain-agnostic and can be applied to any specialized field (such as medicine, finance, legal analysis, or creative writing) using the scripts in this repository:
1. **Calibration**: Run `engine/maple_profile.py` with your custom text corpus (e.g., `engine/calibration_corpus.txt` or a proprietary dataset) to profile routing frequency and activation energy via `llama-imatrix`.
2. **Selection**: MAPLE scores experts according to the composite energy metric and outputs `engine/expert_selection_map.json`.
3. **Container Assembly**: Run `engine/maple_build.py` to slice the unpruned base model and assemble an optimized sub-2-BPW GGUF container for 100% in-VRAM edge execution.

---

## Model Distribution and Direct Execution

The pre-built, verified 4.75 GB GGUF container is hosted on Hugging Face:

- **Hugging Face Model Repository**: AmSach/Gemma-4-26B-A4B-MAPLE-Sub5GB-GGUF
- **Direct Binary Download**: gemma-4-26B-A4B-MAPLE-IQ2_XXS.gguf (4.75 GB)

### Direct Execution via `llama.cpp`:
```bash
llama-cli \
  -hf AmSach/Gemma-4-26B-A4B-MAPLE-Sub5GB-GGUF \
  -ngl 99 \
  -c 2048 \
  -n 512 \
  --temp 0.4 \
  --top-p 0.9 \
  --repeat-penalty 1.1 \
  -r "<turn|>" \
  -p "<|turn>user\nExplain why the sky is blue using Rayleigh scattering.\n<turn|>\n<|turn>model\n"
```
*(llama-cli downloads the 4.75 GB GGUF container directly from Hugging Face and allocates all 30 layers into GPU VRAM at 45.4 TPS).*

---

## Overview

While global multilingual pre-training necessitates 128–256 experts to serve hundreds of human languages and encyclopedic domains, localized edge deployments (such as English technical reasoning and code generation) activate only a narrow subset of experts.

MAPLE discovers this latent manifold by profiling live forward-pass expert activations via `llama-imatrix`, scoring experts via a composite frequency-energy metric:

$$s_{e,l} = C_{e,l} \cdot \sqrt{\bar{\sigma}_{e,l} + \epsilon}$$

where:
- **`s_{e,l}`**: Composite importance score for expert `e` in layer `l`
- **`C_{e,l}`**: Empirical token activation frequency (routing count)
- **`σ̄_{e,l}`**: Mean input channel activation energy
- **`ε`**: Numerical stability floor (10⁻⁶)

Applied to Gemma 4 26B-A4B (128 routed experts, 30 layers), MAPLE excises 80 dormant experts per layer to assemble an optimized 48-expert GGUF container capturing **79.88% of active forward-pass activation mass**.

---

## Performance Benchmark (RTX 4050 6GB Laptop GPU)

| Configuration | Model Size | VRAM Allocation | Offloaded Layers | Generation Speed | Latency |
|---|---|---|---|---|---|
| **Original 128-Expert Base (Gemma 4 26B-A4B)** | 9.92 GB | 6,141 MiB (paged) | 16 / 30 | 6.9 Tokens/Sec | 144.9 ms / token |
| **MAPLE 48-Expert Container (Gemma 4 26B-A4B)** | **4.75 GB** | **4,180 MiB (100% VRAM)** | **30 / 30** | **45.4 Tokens/Sec** | **22.0 ms / token** |
| **Improvement** | **2.09x smaller** | **-32% VRAM** | **100% In-VRAM** | **6.57x speedup** | **6.58x faster** |

### Task-Level Semantic Fidelity Benchmark

| Task | Domain | Tested Capabilities | Fidelity |
|---|---|---|---|
| **T1: Fibonacci** | Code Synthesis | `def fibonacci`, `return`, `append`, `[0,1]` | **100%** |
| **T2: Binary Search Tree** | Data Structures | `class Node`, `class BST`, `insert`, `search` | **75%** (100% with context >= 500) |
| **T3: Rayleigh Scattering** | Physics Reasoning | `Rayleigh`, `wavelength`, `scattering`, `blue` | **100%** |
| **T4: Syllogistic Logic** | Formal Deduction | `transitive`, `syllogism`, set containment | **100%** |
| **Overall Mean** | | | **93.8%** |

---

## Three Documented Failure Modes Overcome

1. **The Ghost Router (Proxy-Embedding Failure):** Estimating routing by projecting Layer-0 token embeddings through deep router gates failed because non-linear attention shifts rotate deep hidden representations ($l \ge 10$) into orthogonal spaces. MAPLE enforces true forward profiling via `llama-imatrix`.
2. **Cascaded Normalization Suppression:** Multiplying expert scales by $0.795$ to counteract softmax denominator shrinkage compounded across 30 layers ($0.795^{30} \approx 0.001$), blinding the residual stream. Scales must be preserved at $1.0\times$.
3. **DRY Sampler Interference:** The `--dry-allowed-length 2` penalty broke Python syntax by penalizing mandatory 2-character keywords (`def`, `if`, `in`, `+=`). Standard nucleus sampling restored syntax fidelity.

---

## Repository Structure

```
maple/
├── README.md                           # Documentation & benchmarks
├── LICENSE                             # Apache 2.0 License
├── requirements.txt                    # Python dependencies
├── run_maple.bat                       # Interactive Windows launcher
├── upload_to_hf.py                     # Hugging Face Hub upload utility
└── engine/
    ├── maple_profile.py                # Scores & extracts top-48 experts from imatrix
    ├── maple_build.py                  # Slices & builds 4.75 GB GGUF container
    ├── benchmark.py                    # Automated 4-domain semantic fidelity suite
    ├── chat.py                         # Streaming console with live telemetry
    ├── calibration_corpus.txt          # Multi-domain calibration corpus (1,979 tokens)
    └── expert_selection_map.json       # Extracted 30-layer empirical expert indices
```

---

## Local Setup & Interactive Console

### 1. Requirements
```bash
pip install -r requirements.txt
```

### 2. Run the Interactive Chat Console
On Windows:
```cmd
run_maple.bat
```
Or via Python:
```bash
python engine/chat.py
```

---

## Model Download Links (Hugging Face Hub)

The compressed 4.75 GB GGUF model container is publicly hosted on Hugging Face:
- **Repository**: https://huggingface.co/AmSach/Gemma-4-26B-A4B-MAPLE-Sub5GB-GGUF
- **Direct Binary (4.75 GB)**: gemma-4-26B-A4B-MAPLE-IQ2_XXS.gguf

---

## Citation

```bibtex
@article{sachan2026maple,
  title={MAPLE: Manifold-Activated Pruning of Latent Experts},
  author={Sachan, Aman},
  journal={Zenodo},
  year={2026},
  doi={10.5281/zenodo.24042480},
  url={https://doi.org/10.5281/zenodo.24042480}
}
```

# Levithas

## 关联链接

- https://doi.org/10.5281/zenodo.24042480}
- https://huggingface.co/AmSach/Gemma-4-26B-A4B-MAPLE-Sub5GB-GGUF

## 导航

- 项目页：[[10-项目/github.com_47acfd08]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
