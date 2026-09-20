---
type: "corpus"
item_id: "1d92e5da097ce44a"
title: "Show HN: LoongForge-Train LLMs, VLMs, diffusion and embodied models, faster"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49713630"
project_url: "https://github.com/baidu-baige/LoongForge"
author: "nullnonenilNULL"
published_at: "2026-09-15T15:03:31Z"
captured_at: "2026-09-20T09:37:12+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-20"
pub_day: "2026-09-15"
tags:
  - 语料
  - hn_show
  - author_nullnonenilNULL
  - story_49713630
  - show_hn
metrics: {"points": 2, "comments": 0, "engagement_velocity": 2}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:90d"
---

# Show HN: LoongForge-Train LLMs, VLMs, diffusion and embodied models, faster

> [!info] 一句话导读
> baidu-baige/LoongForge

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49713630>
> 指标：点赞=2 · 评论=0 · engagement_velocity=2
> 作者：nullnonenilNULL　|　发布：2026-09-15T15:03:31Z
> 项目链接：<https://github.com/baidu-baige/LoongForge>
> 采集：2026-09-20T09:37:12+08:00　|　id：`1d92e5da097ce44a`

## 正文

# baidu-baige/LoongForge

A unified, high-performance framework for training LLMs, VLMs, diffusion, and embodied models on NVIDIA GPUs and Kunlun XPUs.

- Stars: 455
- Forks: 42
- Watchers: 455
- Open issues: 12
- License: Apache License 2.0
- Homepage: https://baidu-baige.github.io/LoongForge/
- Default branch: master
- Created: 2026-04-23T08:45:42Z

## Languages

- Dockerfile
- Jinja
- Python
- Shell

## Topics

- diffusion
- distributed
- gpu
- kunlun
- llm
- lora
- megatron
- mid-training
- pretraining
- sft
- training
- vla
- vlm
- wam
- wan
- xpu

## Top Contributors

- nullnonenilNULL (160 contributions)
- Zachary-wW (40 contributions)
- kaimo455 (22 contributions)
- XueSongTap (19 contributions)
- VVsssssk (17 contributions)
- github-actions[bot] (12 contributions)
- gsl322 (11 contributions)
- pengxiangyu (8 contributions)
- NeverlanD0829 (7 contributions)
- dyedd (6 contributions)

---

## README

 English | 简体中文

 A unified, high-performance framework for training LLMs, VLMs, diffusion, and embodied models.

 🌐 Website
  · 
 📖 Docs
  · 
 ✍️ Blog
  · 
 ⚡ Quick Start
  · 
 📊 Performance
  · 
 🏛️ Supported Models
  · 
 💬 Contact

## 💡 Why LoongForge?

> 🐉 LoongForge is named after the traditional Chinese **loong boat (龙舟)**, a symbol of coordinated power and forward momentum.

**LoongForge** is a unified training framework for **LLMs, VLMs, diffusion, and embodied models**, covering **pre-training**, **continued pre-training**, and **SFT**. Its primary goal is to provide broad coverage of mainstream open-source models while delivering efficient, high-throughput training.

Before going open-source, LoongForge was developed as **AIAK-Training-LLM**, Baidu Baige's training acceleration stack. It has supported production training for enterprise customers across **Education**, **Computer Vision**, and **Embodied AI**, typically delivering **30%~50% speedup over customer baselines**, with the largest production runs reaching **5,000+ XPUs**.

## 🏗️ Architecture

Since training requirements vary across model scenarios, LoongForge builds on multiple distributed backends. LLM/VLM/diffusion run on **Megatron-LM**, while embodied models use a **torch-native DDP/FSDP** stack. Each is deeply optimized to outperform mainstream open-source baselines.

## 🔥 Latest News

- **[2026/08]** 📄 Released the **TAOT paper**, introducing topology-aware dynamic expert replica placement to address expert-parallel (**EP**) load imbalance in **MoE** training with low communication overhead.
- **[2026/07]** 🤖 Released the **LoongForge-Embodied** submodule, delivering training support for mainstream **VLA** and **WAM** models, with **~2× speedup** on representative models.
- **[2026/07]** ✨ Added training support for **DeepSeek v4 flash / DeepSeek v4 pro**.
- **[2026/05]** ⚡ Accelerated **Wan 2.2** training by **116%**, and added CP and data packing support.
- **[2026/05]** ✨ Added training support for **Kimi K2.5 / K2.6**, and introduced **INT4 / NVFP4** PTQ.
- **[2026/05]** 🎉 **v0.1.0** — first official tagged release of LoongForge.
- **[2026/05]** 🌟 Powered the training and public release of **LLaVA-OneVision-2.0**.
- **[2026/05]** 🤖 Expanded VLA coverage with **GR00T N1.6**; **60%+ speedup** on Pi0.5 and GR00T training. [blog]
- **[2026/04]** 🧩 Added training support for **MiniMax-M2.7** on both NVIDIA GPU and Kunlun XPU.
- **[2026/04]** 🚀 LoongForge source code publicly available on GitHub. [blog]
- **[2025/10]** 🌟 Powered the training and public release of **LLaVA-OneVision-1.5** under **AIAK-Training-LLM**, the predecessor of LoongForge. [blog]

## ⚡ Quick Start

See the full documentation for installation, tutorials, and advanced usage — English · 中文.

**1. Install** — using **prebuilt Docker images** or **source build**:
- **NVIDIA GPU**: Installation Guide
- **Kunlun XPU**: Installation Guide

**2. Launch your first training run** — follow a tutorial for your target hardware and modality:
- **NVIDIA GPU**: LLM · VLM · VLA & WAM · Diffusion
- **Kunlun XPU**: Kunlun XPU Tutorials

**3. Explore** — browse `configs/models/` and `examples/` / `examples_xpu/` for ready-to-run scripts.

## ✨ Key Features

* **🧩 Flexible Multi-Modal Composition** — Configuration-driven assembly of VLMs from interchangeable ViT and LLM components.
* **⚡ Heterogeneous Parallelism** — Independent TP / DP / recompute per model component (e.g., ViT vs. LLM) for optimal throughput and memory. [blog]
* **🔀 Decoupled Encoder-Decoder Training** — Separates ViT and LLM into independent tasks, eliminating encoder-induced pipeline bubbles.
* **⚖️ DP Load Balancing** — Load-aware data redistribution mitigates sequence-packing imbalance, improving multi-node scaling efficiency. [blog]
* **🚀 MoE-Native Optimization** — Overlapped All2All / activation offload / compute, with **further memory reduction** beyond upstream Megatron-LM on DeepSeek-V3, Qwen3-MoE, etc.
* **🚦 MoE Expert Load Balancing** — Dynamically replicates hot experts using a topology-aware algorithm to balance Expert Parallel (EP) workloads and improve training efficiency. [Paper]
* **🔬 Adaptive FP8 Training** — End-to-end FP8 for LLMs and VLMs with standard **blockwise FP8**; optional **adaptive** mode picks per-operator precision by GEMM shape and efficiency.
* **🔧 Custom Fused Operators** — Fused kernels like **FusedDSA** for DSA-style models — TileLang version open-sourced, high-performance CUDA version available on Baidu Baige platform.
* **🔁 Flexible Checkpointing** — Offline bidirectional **Megatron ↔ HuggingFace** conversion plus native online HF load/save — no format barriers across your workflow.
* **🧰 Versatile Pipelines & Data Tools** — Out-of-the-box **Pretrain / MidTrain / SFT / LoRA**, with built-in dataset format conversion and sequence packing.
* **🤖 Embodied Model Training** — A dedicated **torch-native DDP/FSDP** subsystem for **VLA and world-action (WAM)** models (e.g. Pi0.5, GR00T N1.6, FastWAM), decoupled from the Megatron core, with flexible **DDP / ZeRO-1 / FSDP / HSDP** strategies.
* **🌐 Heterogeneous Hardware** — Native support for **NVIDIA GPUs** and **Kunlun XPUs** via a minimally-intrusive plugin design.

> 📖 Deep-dive: LLM features · VLM features

## 📊 Performance

Training speedups over mainstream open-source baselines. Each row is tagged with the version it was measured on, and refreshed per-model as the stack evolves:

 📋 Details

| Model | Type | Baseline | Speedup | Measured |
|---|---|---|---|---|
| DreamZero (DROID Wan2.2-5B Full) | WAM | DreamZero | **2.67×** | master · 2026-07 |
| GR00T N1.6 | VLA | LeRobot | **2.31×** | master · 2026-07 |
| Pi0.5 | VLA | OpenPI | **2.23×** | master · 2026-07 |
| LingBot VA | WAM | LingBot-VA | **1.80×** | master · 2026-07 |
| X-VLA | VLA | X-VLA | **1.69×** | master · 2026-07 |
| DeepSeek-V3.2 Lite § | MoE + DSA | Megatron-LM | **5.04×** | v0.1.1 |
| Qwen3-VL-30B-A3B | VLM | VeOmni | **1.45×** | v0.1.1 |
| Qwen3-30B-A3B | MoE | Megatron-LM | **1.16×** | v0.1.1 |

> § Due to test-bed scale limits, **DeepSeek-V3.2** was validated separately on a reduced-layer configuration — LoongForge's **DSA CUDA kernel optimizations** still deliver **~5× speedup** over Megatron-LM and reach **64K sequence** (baseline OOMs beyond 8K).
> Numbers reflect baseline and LoongForge versions at the time of measurement (see the **Measured** column), and may evolve as implementations change.

## 🌟 Powered by LoongForge

Open-source models trained with LoongForge or its predecessor AIAK-Training-LLM:

- LLaVA-OneVision-2.0 — Next-generation multimodal model, with new VideoCaption and Spatial datasets.
- Innovator-VL — Scientific Multimodal Large Language Model for Advanced Reasoning.
- LLaVA-OneVision-1.5 — Fully open framework for democratized multimodal training.
- Qianfan-VL — Domain-Enhanced Vision-Language Models for Enterprise, 3B to 70B parameters.

## 🏛️ Supported Models

LoongForge supports a broad range of model families across LLM, VLM, diffusion, and embodied. Select a model below to open its training examples. For complete usage instructions, see the User Guide and the full model support matrix.

 LLM VLM Diffusion Embodied

 DeepSeek-V2 ✅
 DeepSeek-V3/V3.2 ✅
 DeepSeek-V4 ✅
 LLaMA2 ✅
 LLaMA3 ✅
 LLaMA3.1 ✅
 Qwen ✅
 Qwen1.5 ✅
 Qwen2 ✅
 Qwen2.5 ✅
 Qwen3 ✅
 Qwen3-Next ✅
 MiniMax-M2.1/2.5/2.7 ✅
 MIMO ✅
 GLM-5 ✅
 GLM-5.2 ✅

 Qwen2.5-VL ✅
 Qwen3-VL ✅
 Qwen3.5 ✅
 Qwen3.6 ✅
 Kimi-K2.5/2.6 ✅
 MiniCPM-V-4.6 ✅
 GLM-5.2 + Kimi-K2.6 ViT ✅
 ERNIE4.5-VL ✅
 LLaVA-OneVision-1.5 ✅
 InternVL2.5 ✅
 InternVL3.5 ✅
 CustomCombinedModel Example ✅

 Wan2.1 ✅
 Wan2.2 ✅
 Qwen-Image ✅

 Pi0.5 ✅
 GR00T-N1.6 ✅
 GR00T-N1.7 ✅
 xVLA ✅
 FastWAM ✅
 LingBot-VA ✅
 Cosmos3 ✅
 DreamZero ✅

## 📂 Repository Layout

 📁 Directory tree

```
LoongForge/
├── loongforge/                   # Core training framework
│   ├── train/                    # Training entry points & trainers
│   │   ├── pretrain/             #   Pretrain (LLM, VLM)
│   │   ├── sft/                  #   SFT (LLM, VLM, InternVL, ERNIE)
│   │   └── diffusion/            #   Diffusion (WAN, Qwen-Image)
│   ├── models/                   # Unified model abstractions
│   │   ├── foundation/           #   LLM backbones (LLaMA, Qwen, DeepSeek, ...)
│   │   ├── encoder/              #   Vision encoders (ViT, Qwen-VL, InternVL, ...)
│   │   ├── omni_models/          #   Multi-modal composition
│   │   ├── diffusion/            #   Diffusion models (WAN, Qwen-Image)
│   │   └── common/               #   Shared layers and utilities
│   ├── embodied/                 # LoongForge-Embodied: standalone torch-native (DDP/FSDP)
│   │                             #   embodied (VLA + world-action) subsystem — see loongforge/embodied/README.md
│   ├── data/                     # Data pipelines (multi-modal, video, DP balance)
│   ├── tokenizer/                # Tokenizers
│   └── utils/                    # Config map, constants, etc.
├── third_party/Loong-Megatron/   # Patched Megatron-LM (git submodule)
├── configs/                      # Hydra YAML configs (models, data)
├── examples/                     # GPU launch scripts
├── examples_xpu/                 # Kunlun XPU launch scripts
├── tools/                        # Checkpoint conversion, data preprocessing
├── ops/                          # Custom fused operators (incl. open-sourced TileLang)
├── patches/                      # TransformerEngine patches
├── docker/                       # Dockerfiles (GPU & XPU)
├── tests/                        # E2E test suite (YAML-driven)
└── docs/                         # Documentation
```

## 🤝 Contributing

We warmly welcome community contributions — bug reports, feature proposals, and PRs alike. Please read our Contributing Guidelines before submitting.

## 📄 License

LoongForge is released under the Apache License 2.0. Some files are derived from third-party open-source projects; please refer to the specific file headers for their respective copyright and attribution.

## 📝 Citation

If you find LoongForge helpful, please cite this project:

```bibtex
@software{LoongForge2026,
  title  = {LoongForge: A unified, high-performance framework for training LLMs, VLMs, diffusion, and embodied models},
  author = {{The LoongForge Authors}},
  year   = {2026},
  url    = {https://github.com/baidu-baige/LoongForge}
}
```

If you use TAOT for MoE training in LoongForge, you can cite our paper:

```bibtex
@article{zhang2026taot,
  title   = {{TAOT}: Topology-Aware Optimal Transport for Dynamic Expert Replica Placement in {MoE} Training},
  author  = {Zhang, Lingyun and Zhang, Henghua and Gu, Shilei and Mo, Kai and Han, Shuai and Li, Shiyong and Wang, Yanpeng and Shen, Dou},
  journal = {arXiv preprint arXiv:2608.03676},
  year    = {2026},
  url     = {https://arxiv.org/abs/2608.03676}
}
```

## 🙏 Acknowledgments

LoongForge builds on NVIDIA's Megatron-LM and draws inspiration from many excellent open-source projects, including HuggingFace Transformers, LLaMA-Factory, Megatron-Bridge, and LeRobot, as well as the official implementations of the models it supports (e.g. OpenPI, NVIDIA Isaac GR00T). We sincerely thank these communities for their outstanding contributions.

## 💬 Contact

Open a GitHub issue for questions, feedback, or feature requests. You can also join our developer community:

- **WeChat** — Scan QR code to join
- **Slack** — Join here

# Show HN: FlareDB – a Rust-based streaming database with Apache Beam as interface | Hacker News

## 关联链接

- https://arxiv.org/abs/2608.03676}
- https://baidu-baige.github.io/LoongForge/
- https://github.com/baidu-baige/LoongForge}

## 导航

- 项目页：[[10-项目/github.com_8cba6633]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
