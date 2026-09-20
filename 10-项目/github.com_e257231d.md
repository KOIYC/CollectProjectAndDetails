---
type: "project"
title: "Show HN: Rose – reusable foundation embeddings for industrial 1H NMR"
project_url: "https://github.com/romboai/rose-1h-nmr"
first_seen: "2026-09-21T03:11:33+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_zaza3311
  - story_49497418
  - show_hn
lang: "en"
---

# Show HN: Rose – reusable foundation embeddings for industrial 1H NMR

> [!info] 一句话导读
> ROSE: a Foundation Model for Reusable One-dimensional Spectrum Embeddings in 1H NMR

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://github.com/romboai/rose-1h-nmr>
> 首次收录：2026-09-21T03:11:33+08:00
> 来源渠道：HN Show HN
> 标签：author_zaza3311, story_49497418, show_hn
> 最新指标：点赞=3 · 评论=0 · engagement_velocity=3

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-09-21T01:33:52+08:00 | HN Show HN | 点赞=3 · 评论=0 · engagement_velocity=3 | [[20-语料/posts/hn_show/2026-09-21/90c47fd20090bacc_Show-HN-Rose-–-reusable-foundation-embeddings-for]] |
| 2026-09-21T03:11:33+08:00 | HN Show HN | 点赞=3 · 评论=0 · engagement_velocity=3 | [[20-语料/posts/hn_show/2026-09-21/90c47fd20090bacc_Show-HN-Rose-–-reusable-foundation-embeddings-for]] |

## 摘要正文

# romboai/rose-1h-nmr  ROSE: a Foundation Model for Reusable One-dimensional Spectrum Embeddings in 1H NMR  - Stars: 2 - Forks: 0 - Watchers: 2 - Open issues: 1 - License: Apache License 2.0 - Homepage: https://doi.org/10.26434/chemrxiv.15007823/v1 - Default branch: main - Created: 2026-07-28T10:15:19Z  ## Languages  - Python  ## Topics  - cheminformatics - chemistry - foundation-model - nmr - pytorch  ## Top Contributors  - zaza81 (5 contributions)  ---  ## README  # ROSE-1H NMR  ChemRxiv DOI Hugging Face License  Pretrained **¹H NMR** foundation model — inference and paper adaptation protocols.  **Paper:** ChemRxiv. **Archive:** Zenodo (all versions; v0.1.0 is 10.5281/zenodo.22142632). **Weights:** `romboai/rose-1h-nmr`. **Code:** this repo.   Frozen [CLS] embeddings (UMAP). From the paper.  ## Quick start  ```bash git clone https://github.com/romboai/rose-1h-nmr.git cd rose-1h-nmr && pip install -e ".[hub]" ```  ```python from rose import load, encode model = load() z = encode(model, spectrum)  # float32, shape (4096,), linear 0–14 ppm ```  Input may also be `(B, 4096)`. `field_mhz` and `solvent_id` are optional (`solvent_id` → `configs/solvent_vocab.json`). Local weights: `load…
