---
type: "corpus"
item_id: "cda5465b44205da7"
title: "Show HN: Maple – Run Gemma 4 26B on a 6GB Laptop GPU at 45 TPS (Sub-2-BPW)"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50415106"
project_url: "https://amsach.github.io/maple"
author: "AmSach"
published_at: "2026-11-08T17:13:03Z"
captured_at: "2026-11-09T09:39:29+08:00"
lang: "en"
kind: "post"
topic: "开发者工具"
shard: "2026-11-09"
pub_day: "2026-11-08"
tags:
  - 语料
  - hn_show
  - author_AmSach
  - story_50415106
  - show_hn
metrics: {"points": 4, "comments": 0, "engagement_velocity": 4}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:3d"
---

# Show HN: Maple – Run Gemma 4 26B on a 6GB Laptop GPU at 45 TPS (Sub-2-BPW)

> [!info] 一句话导读
> Portability & MoE Guide

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50415106>
> 指标：点赞=4 · 评论=0 · engagement_velocity=4
> 作者：AmSach　|　发布：2026-11-08T17:13:03Z
> 项目链接：<https://amsach.github.io/maple>
> 采集：2026-11-09T09:39:29+08:00　|　id：`cda5465b44205da7`

## 正文

MAPLE
 v1.0 GGUF
Benchmarks
 Architecture
 Portability & MoE Guide
 Quickstart
 Preprint
GitHub
RESEARCH PREPRINT & OPEN-WEIGHTS RELEASE
Run Gemma 4 26B 100% In-VRAM at 45.4 TPS on a 6GB Laptop GPU.
Manifold-Activated Pruning of Latent Experts (MAPLE) compresses 128-expert fine-grained MoE architectures down to 4.75 GB (1.48 effective BPW), eliminating PCIe system-RAM paging stalls forever.
Download GGUF (4.75 GB)
Read Preprint (Zenodo DOI)
llama.cpp Showcase #31894
Kaggle DOI 10.34740/KAGGLE/M/786779
Throughput
45.4 t/s
6.57x speedup vs PCIe offload
Container Size
4.75 GB
Sub-5GB (100% fits in 6GB VRAM)
Quantization
1.48 BPW
IQ2_XXS calibrated via imatrix
Expert Pruning
80 / 128
79.88% activation mass preserved
Hardware Benchmark Proof
The PCIe Paging Death Spiral, Solved.
Consumer laptops cannot run uncompressed 26B models without overflowing into system RAM over bandwidth-constrained PCIe lanes.
Inference Throughput (RTX 4050 6GB)
 6.57x Real-World Lift
Base Gemma 4 26B IQ2_XXS (9.92 GB)
 6.9 TPS (16/30 layers in VRAM)
14 layers offloaded to system RAM. Constrained by 15.75 GB/s PCIe bus bandwidth.
MAPLE 48-Expert Container (4.75 GB)
45.4 TPS (30/30 layers in VRAM)
100% In-VRAM execution. Dedicated 192 GB/s GDDR6 bus with zero host memory paging.
Test Rig
 RTX 4050 6GB Mobile
Context Window
 2,048 Tokens
Host Memory Spills
 0 Bytes (Zero Spill)
Precision & Accuracy Retention
Quality Retention (≥ 500 Tokens)
 Full benchmark completion & self-correction
100.0% Parity
Keyword & Syntax Fidelity
 Code generation & formal logic
93.8%
Activation Energy Retained
 Calibrated across Technical Corpus
79.88%
Effective Weight Precision
 Sub-2-BPW target architecture
1.48 BPW
Total Parameter Footprint
 Uncompressed 52GB -> MAPLE 4.75GB
10.9x Compression
Quality Parity: When the generation budget is set to 500+ tokens, MAPLE achieves 100% functional pass rate across syntax, logic, and data structure benchmarks with zero degradation compared to the unpruned base model.
Architectural Framing
 Domain-Targeted Pareto Distillation
We did not attempt lossy random pruning across the entire internet. Gemma 4 26B uses 128 fine-grained experts where massive clusters specialize in non-English languages, translation, and non-technical trivia. For edge code generation and technical deduction, those experts are dormant overhead.
MAPLE profiles the empirical activation manifold specifically on technical, algorithmic, and deductive tokens. We prune the 80 dormant experts and preserve the 48 active ones, masking excised router logits to -inf so softmax remains numerically stable.
Within the target domain (Python algorithmic synthesis, data structures, and logic), the model retains 100% functional unit-test execution when given standard token generation headroom (-n 512). The intentional trade-off is higher out-of-domain multilingual perplexity, which enables the model to run 100% inside 6GB VRAM at 45.4 TPS instead of stalling over PCIe at 6.9 TPS.
Architectural Foundation
Manifold-Activated Latent Profiling
Why naive expert removal destroys models, and how manifold activation analysis preserves technical reasoning.
Live Routing Profiling
MAPLE passes a multi-domain calibration corpus through Gemma 4, capturing exact token-to-expert router dispatch frequencies and activation magnitudes via llama-imatrix.
Dormant Expert Excision
80 dormant experts per layer are excised based on cumulative manifold energy thresholds. The router logits are dynamically re-indexed to dispatch across the 48 preserved experts.
GGUF Quantization Slicing
Preserved expert tensor slices are quantized into IQ2_XXS block representations using importance matrix weights, packaging the complete 26B model into a single 4.75 GB binary.
Empirical Reproducibility & Portability
Dynamic Calibration & Universal MoE Support
Pruning follows your activation manifold. Understand why your workload yields your model, and how to adapt MAPLE to any Sparse MoE architecture.
Empirical Calibration Reality
Results Follow Your Calibration Corpus
MAPLE results are strictly deterministic and reproducible, but variable depending on your calibration dataset. What we released is a reference implementation on Gemma 4 26B-A4B optimized for edge technical execution.
Technical Specialization (Our Reference): Pruned 80 dormant experts, preserved 48 active ones. Reduced from 9.92 GB to 4.75 GB for 100% in-VRAM execution on 6GB GPUs.
General-Purpose Workloads: Calibrating on diverse multilingual dialogue activates a broad manifold. The optimizer may prune only 20 to 40 experts, retaining 88 to 108 experts for broad versatility.
Domain Customization: Biomedical, legal, or financial corpora activate entirely different expert clusters. If your workload is different, you get a different model.
"The reference Gemma 4 model proves the pipeline works. Your domain calibration produces your tailored edge container."
Universal SMoE Portability
Theoretically & Practically Universal Across All MoEs
Because MAPLE operates on fundamental router logits and activation variance, the mathematical formulation is directly portable to any Sparse Mixture-of-Experts transformer:
Liquid AI LFM 24B MoE
Mixtral 8x7B / 8x22B
DeepSeek-V2 / V3 MoE
Qwen 2.5 MoE (57B-A14B)
Any model using top-k router gating can be profiled via llama-imatrix or PyTorch forward hooks, sliced, and masked to -inf without retraining.
Universal Recipe
 How to Apply MAPLE to Any MoE Model (LFM-24B, Mixtral, DeepSeek)
01. CALIBRATE
 Assemble 2k-10k tokens of domain text representing your target operational workload.
02. PROFILE
 Run llama-imatrix to capture activation frequencies and channel energy matrix.
03. SCORE
 Compute composite score s = C * sqrt(sigma + eps) and rank active experts per layer.
04. MASK -INF
 Excise unselected expert tensors and set excised router logits to -inf for softmax invariance.
05. DEPLOY
 Quantize via llama-quantize (IQ2_XXS / Q4_K_M) for 100% in-VRAM execution.
Instant Local Deployment
Run in One Command
Native GGUF execution directly supported in llama.cpp, Ollama, and LM Studio.
bash - llama-cli
Copy Command
llama-cli -hf AmSach/Gemma-4-26B-A4B-MAPLE-Sub5GB-GGUF -ngl 99 -c 2048 -n 512
-hf : Hugging Face repo auto-download
-ngl 99 : Offload 100% of layers to GPU
-c 2048 : 2k context window in 4.75GB
Verified Product & Community Showcases
P
Featured on PitchHut
Z
Zenodo DOI 10.5281/zenodo.24042480
Google Scholar Profile
K
Kaggle DOI 10.34740/KAGGLE/M/786779
Citation (BibTeX)
Copy BibTeX
@article{sachan2026maple,
 title={MAPLE: Manifold-Activated Pruning of Latent Experts for Sub-2-BPW Mixture-of-Experts Language Models},
 author={Sachan, Aman},
 journal={Zenodo / CERN Open Science Preprint},
 year={2026},
 doi={10.5281/zenodo.24042480},
 url={https://doi.org/10.5281/zenodo.24042480}
}
@misc{sachan2026maple_kaggle,
 author={Sachan, Aman},
 title={MAPLE: Gemma 4 26B Sub-5GB MoE},
 publisher={Kaggle},
 year={2026},
 doi={10.34740/KAGGLE/M/786779},
 url={https://doi.org/10.34740/KAGGLE/M/786779}
}
Hugging Face Model
 GitHub Repository
 Zenodo Preprint
 llama.cpp Community
 LaunchNest Listing
 PitchHut Showcase
 Kaggle Model DOI
MAPLE Architecture by Aman Sachan. Open source under Apache 2.0. Verified without synthetic contact data.

## 关联链接

- https://doi.org/10.34740/KAGGLE/M/786779}
- https://doi.org/10.5281/zenodo.24042480}

## 导航

- 项目页：[[10-项目/amsach.github.io_422b5290]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`开发者工具`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
