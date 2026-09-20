---
type: "corpus"
item_id: "dbdfc52c10d890f3"
title: "Show HN: LingBot-World 2.0 (1.3B) running at 16 FPS on one RTX 5090"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49758853"
project_url: "https://github.com/kaarelkaarelson/lingbot-world-v2-realtime"
author: "kaarelson"
published_at: "2026-09-18T19:12:19Z"
captured_at: "2026-09-20T14:01:47+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-20"
pub_day: "2026-09-18"
tags:
  - 语料
  - hn_show
  - author_kaarelson
  - story_49758853
  - show_hn
metrics: {"points": 3, "comments": 2, "engagement_velocity": 3}
comments_count: 2
comments_total: 2
discovered_via: "hn:show_hn:90d"
---

# Show HN: LingBot-World 2.0 (1.3B) running at 16 FPS on one RTX 5090

> [!info] 一句话导读
> kaarelkaarelson/lingbot-world-v2-realtime

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49758853>
> 指标：点赞=3 · 评论=2 · engagement_velocity=3
> 作者：kaarelson　|　发布：2026-09-18T19:12:19Z
> 项目链接：<https://github.com/kaarelkaarelson/lingbot-world-v2-realtime>
> 采集：2026-09-20T14:01:47+08:00　|　id：`dbdfc52c10d890f3`

## 正文

# kaarelkaarelson/lingbot-world-v2-realtime

1.3B world model running at 16 FPS on an RTX 5090

- Stars: 11
- Forks: 1
- Watchers: 11
- Open issues: 0
- License: Other
- Homepage: https://kaarelkaarelson.com/lingbot/
- Default branch: main
- Created: 2026-09-16T19:35:12Z

## Languages

- Makefile
- Python
- Shell

## Top Contributors

- kaarelkaarelson (93 contributions)
- qiuyu96 (4 contributions)
- zelingao98 (3 contributions)
- zhujiapeng (2 contributions)
- FelixYuan-YF (1 contributions)
- pPetrichor (1 contributions)
- JingyeChen (1 contributions)
- zliucz (1 contributions)
- EzioBy (1 contributions)
- YichongLu (1 contributions)

---

## README

# LingBot-World 2.0 realtime

 Blog  · 
 Original paper

A 1.3B world model running at ** 16.1 FPS on one RTX 5090**. 2.7× faster than the original paper's code with lossless performance.

lingbot play dragon at 16 fps

## Performance vs other engines

| Engine | s / chunk | FPS | Ours vs it |
|---|---|---|---|
| Original paper's code | 2.68 | 6.0 | **2.7×** |
| SGLang Diffusion | 2.48 | 6.45 | **2.5×** |
| LightX2V | 2.07 | 7.73 | **2.1×** |
| NVIDIA FlashDreams | 1.85 | 8.65 | **1.9×** |
| **Ours** | 0.98 | **16.1** | — |

the same clip at each engine's measured cadence

Measured with `lingbot bench` on a stock RunPod RTX 5090 (2026-09-17).

## Quick start

### Setup

~15 min on Linux, needs a Hugging Face token to download the weights.

```bash
git clone https://github.com/kaarelkaarelson/lingbot-world-v2-realtime
cd lingbot-world-v2-realtime
HF_TOKEN=hf_... ./setup.sh && . .venv/bin/activate
```

### Play

```bash
lingbot play dragon
```

The first start compiles for about 2.5 min, later starts take 35 s.

### Commands

| Key | Action |
|---|---|
| `W` `A` `S` `D` | move (hold `Shift` to run) |
| `Q` `E` | down / up |
| `←` `→` `↑` `↓` | look (45°/s); mouse drag also looks |
| `R` | restart the world from the image |
| `Esc` | quit |

### Scripts

| Script | |
|---|---|
| `lingbot play [scene]` | a window on the world; scenes: `lake` (default), `wall`, `stonehenge`, `alley`, `castle`, `dragon` |
| `lingbot play --image me.jpg --prompt "..."` | your own world from any image |
| `SDL_VIDEODRIVER=dummy lingbot play --headless-seconds 120` | no display (a cloud pod): same model, no window, taps `W` and prints the HUD summary |
| `lingbot bench` | the 22 s clip to `outputs/`, prints s/chunk and FPS |
| `lingbot clip --image me.jpg --action_path my_poses/ --prompt "..."` | offline generation from a camera path, `poses.npy` and `intrinsics.npy` as in `examples/` |

## Requirements

| | GPU | |
|---|---|---|
| Recommended | RTX 5090, 32 GB | everything here was measured on it; `setup.sh` ships prebuilt kernels for it (sm_120) |
| Minimum | RTX 4090, 24 GB | untested: every patch supports sm_89, expect ~12 FPS; needs `sageattention` and `flash_attn` built from source and T5 on the CPU to fit |

## Optimizations

Nothing about the model changed. The checkpoint, the sampler and the decoder are upstream's, with the same 4 steps, chunks of 4 latents and a KV window of 18 frames. I worked through the stack from the top down, cheapest and most general layer first, measured each step, and stopped at the kernel boundary. The table shows seconds per chunk after each step in the order they were applied. A chunk is 16 frames, one second of video.

| Step | Before | After | s/chunk |
|---|---|---|---|
| Host syncs | CPU↔GPU sync on every layer | bookkeeping on the GPU | 2.68 → 2.57 |
| Decoder | Wan 2.1 VAE in fp32 | fp16 with sub-pixel upsampling | 2.57 → 1.95 |
| Compiler | PyTorch eager | one compiled graph | 1.95 → 1.68 |
| Matmuls | bf16 linears | FP8 rowwise via torchao | 1.68 → 1.47 |
| Attention | FlashAttention-2 | SageAttention 2.2 | 1.47 → 1.04 |
| Kernel fusion | one kernel per operation | fused kernels for norm, RoPE, residual and FP8 quant | 1.04 → 0.98 |
| **Total** | 6.0 FPS | **16.1 FPS** | **2.68 → 0.98** |

The table compares the original paper's code with ours, per chunk. GPU busy and kernel launches come from profiler traces of both, described in sections 13 and 17 of `OPTIMIZATIONS.md`. Host syncs are counted over three chunks.

| | Original paper's code | Ours |
|---|---|---|
| FPS | 6.0 | **16.1** |
| s / chunk | 2.68 | **0.98** |
| DiT | 1.62 s | **0.64 s** |
| Decoder | 1.06 s | **0.34 s** |
| GPU busy | 90% | **98%** |
| Kernel launches | ~20,000 | **~4,800** |
| Host syncs | 110 | **2** |

What is left runs in four kernels written by others, and three of them are near the card's peak. Attention has the most room. A hand written kernel at 90 % of peak would gain about one frame per second, so there is none. The details are in section 17 of `OPTIMIZATIONS.md`. The peaks are from NVIDIA's RTX 5090 specification.

| Kernel | Reached | Peak on RTX 5090 | of peak |
|---|---|---|---|
| FP8 matmuls | 390 TFLOP/s | 419 TFLOP/s FP8 | **90 %** |
| Decoder convolutions | 173 TFLOP/s | 210 TFLOP/s FP16 | **83 %** |
| Fused elementwise | ~1.3 TB/s | 1.8 TB/s memory | **~70 %** |
| SageAttention | 543 TOPS | 838 TOPS INT8 | **65 %** |

The result is lossless. Four of the six steps are bit identical to the paper's code, and FP8 and the attention kernel were checked on identical inputs. PSNR, SSIM and LPIPS compare the same latents decoded by the paper's fp32 decoder and by ours. The rest are no reference metrics on the generated clips, measured on the first and last second. The numbers are in `quality_summary.tsv` from experiment 15.

| | Original paper's code | Ours |
|---|---|---|
| PSNR | reference | **43.6 dB** |
| SSIM | reference | **0.981** |
| LPIPS | reference | **0.004** |
| MUSIQ | 68.98 | **68.99** |
| CLIP-IQA | 0.592 | **0.590** |
| Sharpness (Laplacian), first / last s | 1022 / 298 | **1023 / 298** |
| Colourfulness, first / last s | 41.9 / 50.2 | **41.9 / 50.2** |
| Brightness, first / last s | 0.692 / 0.384 | **0.692 / 0.384** |
| Flicker | 0.0381 | **0.0381** |
| DiT latents, exact preset | reference | **bit-identical** |

`OPTIMIZATIONS.md` is the full log. It has every experiment with its measurement, the profiles, and the levers that were tried and rejected.

## Presets

| `--preset` | What runs | s / chunk | FPS |
|---|---|---|---|
| `stock` | the original paper's code | 2.68 | 6.0 |
| `exact` | ours, with the DiT latents bit identical to the paper's bf16 model | 1.07 | 14.8 |
| **`fast`** (default) | ours, FP8 linears, SageAttention, compiled and fused DiT, fused fp16 decoder | ** 0.98 ** | ** 16.1 ** |

## Tests

`pytest tests/` runs on the CPU, no GPU needed. It checks the fused decoder and DiT against the stock modules and runs `lingbot play --dry` on a stand in model.

## License and credit

This repository is derived from LingBot-World 2.0 by the Robbyant team, whose paper is by Zelin Gao and others. The model, the sampler and the examples are theirs. The weights are theirs too and are not redistributed here. Upstream is licensed under CC BY-NC-SA 4.0, and so is this repository, see `LICENSE.txt`. That means non commercial use, attribution, and the same license for anything built on it. It is provided as is, without warranty. My changes are the inference patches listed under Optimizations and the `lingbot` CLI, applied on upstream commit `1895d30`. The `wan/` directory is upstream's copy of Wan2.2, which is Apache 2.0. The kernels used are SageAttention, torchao and FlashAttention.

```bibtex
@article{lingbot-world-v2,
  title   = {Infinite Worlds with Versatile Interactions},
  author  = {Zelin Gao and Qiuyu Wang and Jiapeng Zhu and Jingye Chen and Zichen Liu and Qingyan Bai and Jiahao Wang and Yufeng Yuan and Hanlin Wang and Yichong Lu and Ka Leong Cheng and Haojie Zhang and Jian Gao and Tianrui Feng and Yuzheng Liu and Yao Yao and Yinghao Xu and Xing Zhu and Yujun Shen and Hao Ouyang},
  journal = {arXiv preprint arXiv:2607.07534},
  year    = {2026}
}
```

# AI Gateway Models & Pricing - ComputeSDK

## 评论（2/2）

> **kaarelson** · 2026-09-18T19:17:35.000Z　
> Hi, I optimized a world model, Lingbot-World 2.0 1.3B, to run with real-time 16ps on an RTX 5090. It's 2.7x faster than Robbyant (Alibaba's lab), 2.5x vs SGlang, and 1.9x vs Nvidia FlashDreams engine. The drawback is that the resolution is 832×464, so you'd have to play it with a small window. It maintains lossless performance while running on a 1x consumer GeForce GPU for a model that's very compute-bound and batch size = 1! The majority of the wins came from:- running the decoder in half-precision with fp16 instead of fp32- switching FlashAttention to SageAttention- writing some custom kernels (minor)Currently works on Linux only.Run: $ lingbot play dragon

---

> **atmanactive** · 2026-09-19T11:49:02.000Z　
> Very interesting, congrats, and thanks for sharing. What are the major advantages to running something like this as opposed to running a simple Unreal Engine scene?

## 关联链接

- https://kaarelkaarelson.com/lingbot/

## 导航

- 项目页：[[10-项目/github.com_48347eed]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
