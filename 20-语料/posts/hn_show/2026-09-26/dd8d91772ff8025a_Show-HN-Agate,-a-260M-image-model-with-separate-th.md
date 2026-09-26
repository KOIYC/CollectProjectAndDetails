---
type: "corpus"
item_id: "dd8d91772ff8025a"
title: "Show HN: Agate, a 260M image model with separate thinker and renderer"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49848811"
project_url: "https://huggingface.co/Logolabs/agate-preview-001"
author: "stefatorus"
published_at: "2026-09-25T19:25:29Z"
captured_at: "2026-09-26T09:41:08+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-26"
pub_day: "2026-09-25"
tags:
  - 语料
  - hn_show
  - author_stefatorus
  - story_49848811
  - show_hn
metrics: {"points": 3, "comments": 0, "engagement_velocity": 3}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:3d"
---

# Show HN: Agate, a 260M image model with separate thinker and renderer

> [!info] 一句话导读
> Agate is a 260M-parameter text-to-image model trained from scratch in 145 GPU-hours. It scores 0.550 on GenEval with the official scorer, level with SDXL's publ…

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49848811>
> 指标：点赞=3 · 评论=0 · engagement_velocity=3
> 作者：stefatorus　|　发布：2026-09-25T19:25:29Z
> 项目链接：<https://huggingface.co/Logolabs/agate-preview-001>
> 采集：2026-09-26T09:41:08+08:00　|　id：`dd8d91772ff8025a`

## 正文

# Agate Preview 001

Agate is a 260M-parameter text-to-image model trained from scratch in 145 GPU-hours. It scores 0.550 on GenEval with the official scorer, level with SDXL's published 0.55 and above SD 1.5 (0.43), SD 2.1 (0.50) and PixArt-α (0.48). It is small enough to run in under two seconds on a consumer GPU.

Built by LogoLabs, which makes AI logo generation, as a better small model for icon generation.

## At a glance

| What | Text-to-image, 256 × 256, English prompts |
| --- | --- |
| Size | 260M parameters with TAESD, 308.5M with SD-VAE: 190.9M generator + 68.1M text encoder + decoder |
| Training | From scratch, 144.7 GH200-hours, under 13 h wall-clock, 146.9M images seen (≈26 epochs) |
| Energy | 81.8 kWh and 2.45 kg CO₂e for Agate; 176.7 kWh for the whole project, measured with perun |
| GenEval (official) | 0.550. SDXL 0.55, SD 2.1 0.50, PixArt-α 0.48, SD 1.5 0.43 (published) |
| Qwen-Image-Bench (1,000 prompts) | 28.2, against SD 1.5's 29.1; on the Pareto frontier among open models of similar size |
| Speed | 1.9 s per image on an RTX 4060 (50 steps); also runs in the browser: WebGPU demo |
| Strengths | Placing objects (left of, on top of), binding colours to objects, faces, styles, flat logos, long prompts |
| Weaknesses | Exact text, counts above three, negation, anything above 256 px; not yet converged |
| Licence | MIT, for code and weights |
| Status | Research preview. A technical report and system card accompany this release. |

- Generator: 191M-parameter thinker-steered convolutional flow model (FCDM-T2). A small recurrent transformer (the thinker) reads the prompt and plans a 16 × 16 region map. That map steers a convolutional U-Net working on SD-VAE latents.
- Text encoder: Ettin-68M, fine-tuned jointly with the generator, 512-token context.
- Decoder: SD-VAE-ft-MSE, or TAESD for speed.
- Parameter count: the headline 260M assumes the tiny TAESD decoder: 190.9M generator + 68.1M Ettin + 1.2M TAESD. The pipeline's default decoder is the full SD-VAE (49.5M), which makes it 308.5M. The VAE encoder is only needed for training.
- Data: FLUX-Reason-6M, 5,654,461 of its 5,890,279 images, each with up to 8 English caption fields. Compute: Arrhenius (EuroHPC, NAISS, Sweden), NVIDIA GH200.
- Licence: MIT, for the code and the weights.

Jump to: The idea · Quick start · Why Agate · Results · Side by side · Test battery · How it works · Training · Safety · Energy · Failures · Acknowledgements

## The idea: plan, then paint

Agate's central design choice is to split image generation between two specialists.

- The thinker is a transformer. It sees the whole noisy canvas at once. It is told how far denoising has come, and it cross-attends to up to 512 text tokens, so it can pick out what matters in a long prompt. It knows 2D positions, so "left of" and "above" are real relations. It thinks in four loops, then writes a 16 × 16 plan of regions in latent space.
- The renderer is a convolutional U-Net built on FCDM. Its 7 × 7 convolutions carry strong image priors: edges, textures, light. It stays cheap at full resolution. It has no attention and never sees the text. It only follows the plan.

Convolutions paint well but cannot reason about a sentence or relate one side of the image to the other. Transformers reason well but are expensive and prior-poor at pixel level. So Agate plans with attention where planning happens, on a coarse grid, and paints with convolutions.

The hypothesis held, and the figure shows the evidence:

- At the same size and epoch, adding the thinker raised GenEval and Qwen-Image-Bench and lowered the loss.
- Making the planner recurrent and 2D-aware lifted position and colour binding.
- The finished model binds colours to objects far better than a 1B model whose renderer reads the text directly.

The plans above are real: we captured the thinker's output while Agate generated. The layout is already visible at step 5 of 50.

## Quick start

```bash
pip install torch transformers diffusers safetensors huggingface_hub pillow

```

```python
import sys
from huggingface_hub import snapshot_download

path = snapshot_download("Logolabs/agate-preview-001")
sys.path.insert(0, path)
from agate import AgatePipeline

pipe = AgatePipeline.from_pretrained(path, device="cuda")      # "cpu" works too, slowly
image = pipe("a green teapot and a red cup on a table", seed=0)[0]
image.save("teapot.png")

```

| Argument | Default | What it does |
| --- | --- | --- |
| `seed` | `0` | Same seed, same image. |
| `steps` | `50` | Euler steps from noise to image. |
| `cfg` | `3.0` | Classifier-free guidance against `negative_prompt`. |
| `negative_prompt` | `""` | The unconditional prompt. Agate was trained with `""`. |
| `num_images` | `1` | Images per call, one batch. |
| `autoguide` | `0.0` | Also steers away from an early checkpoint of Agate (step 27,600, shipped in `guide/`). Try `autoguide=1.0, cfg=4.0` for sharper faces and textures at about 1.5× the time. |
| `fast_vae` (from_pretrained) | `False` | Decode with TAESD instead of the full SD-VAE. |
| `cuda_graphs` (from_pretrained) | `True` | Record each denoising step once as a CUDA graph and replay it. |

On an RTX 4060, one image takes 1.9 s (2.9 s with `autoguide`). At 191M parameters, kernel-launch overhead costs more time than the arithmetic, and CUDA graphs remove most of it.

## Why Agate

Why we built it. LogoLabs builds AI logo generation. Agate is our attempt at a better small model for icon generation. We want one that places things where you ask, keeps colours bound to the right objects, runs on a consumer GPU, and can be trained from scratch on a research budget. This preview is the general-purpose base model; it is not yet specialised for icons.

It trains ultra-fast. The whole training took 144.7 GH200-hours, and the model was trained from scratch in under 13 hours of wall-clock time:

- about 5 h 15 min on 16 GPUs (4 nodes × 4) for phases 1 and 2;
- 7 h 30 min on 8 GPUs (2 nodes × 4) overnight for the caption phase.

Retraining from scratch, on your own data or for a new domain, is an overnight job rather than a research programme. More of our work is on our Hugging Face page: the Inkvec vectoriser and the LogoBrief-10K dataset.

### Where a small model wins

Large text-to-image models make better single images. Agate is for the jobs where their size is the problem: too slow, too expensive per image, too heavy to ship, or too costly to retrain.

| Use | Why a 260M model fits | Why a multi-billion model struggles |
| --- | --- | --- |
| Runs on the device | About 1 GB of weights in fp32 (half that in fp16); 1.9 s per image on an RTX 4060; small enough for a laptop, and it also runs in the browser on WebGPU. Prompts and images never leave the machine. | Needs a datacentre GPU or a paid API, so every prompt goes to a server. |
| Previews while you type | At the measured ~0.04 s per step, an 8-step draft takes about a third of a second, so a design tool can redraw on every keystroke. | Seconds per image make live preview impractical and expensive at scale. |
| Generating in bulk | About 1,900 images an hour on one consumer GPU: icon sets, variations, synthetic training data, A/B candidates. | At API prices or datacentre-GPU time, millions of images cost real money. |
| A model per customer or domain | A full retrain from scratch is an overnight run (under 13 h), and fine-tunes are cheaper still. A brand, an icon style or a product catalogue can have its own model. | Fine-tuning is costly; training from scratch is out of reach for almost everyone. |
| Research on a budget | Reinforcement learning, reward models, new samplers and architecture ablations cost GPU-hours, not GPU-years. Our whole project, every model and benchmark included, cost 323 GPU-hours. | Every experiment costs thousands of GPU-hours, so few groups can run them. |
| Layout-first pipelines | Strong on placement and colour binding (GenEval position 0.22 vs SD 1.5's 0.01), so it can sketch a composition cheaply. A larger model or a vectoriser such as Inkvec then finishes it. | Using a large model for the rough draft wastes most of its cost. |
| Offline, edge and sovereign deployments | MIT licence, no gated dependencies, trainable on a single node. It can run air-gapped and be retrained on your own infrastructure. | Licences, gated weights and hardware needs often rule these out. |

For LogoLabs the target is icon and logo generation: many candidates per brief, fast iteration, and per-client styles. That work rewards a small, fast, retrainable model over a large one.

A preview: not yet converged. Agate is a preview checkpoint, and it has not finished learning. Every benchmark was still rising when training stopped:

- GenEval went from 0.505 at epoch 16 to 0.533 at step 82.8k and 0.535 at the end.
- Qwen-Image-Bench went from 24.8 to 27.8 and then 28.4.
- The loss was still falling.

We expect roughly doubling the training, about 145 more GPU-hours, to bring very significant gains. That run is the next step.

## Results

All scores below were measured by us, with the same seeds, sampler and scorer for every model. Each model generated at its own trained resolution; every scorer then saw the image at 512 × 512 (Lanczos). SD 1.5 renders at its native 512 px; Agate and Supra2-IMG render at 256 px.

### GenEval (official scorer)

The official GenEval pipeline (Mask2Former object detector + CLIP colour classifier) on all 553 prompts. We scored every model: all our checkpoints, SD 1.5 and Supra2-IMG, one image per prompt (the chart above and the table below). Agate's headline number uses the benchmark's full four images per prompt (2,212 images). The four-image run for every other model is in progress and will be added here:

| | Single | Two obj. | Counting | Colours | Position | Colour attr. | Overall |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Agate, 4 images per prompt | 0.916 | 0.581 | 0.381 | 0.753 | 0.212 | 0.458 | 0.550 |

Published GenEval scores for context. These come from other papers and hardware; the compute column shows what each model cost to train:

| Model | Generator params | Reported training compute | GenEval |
| --- | --- | --- | --- |
| Agate (ours) | 191M (+68M text encoder) | 145 GH200-h (≈ 360–460 A100-h) | 0.55 |
| SDXL | 2.6B UNet | not published | 0.55 |
| Meissonic | 1B | ~1,150 H100-h | 0.54 |
| SD 2.1 | 865M UNet | 200,000 A100-h | 0.50 |
| PixArt-α | 0.6B (+4.3B Flan-T5-XXL) | 753 A100-days (18,000 A100-h) | 0.48 |
| SD 1.5 | 860M UNet | 150,000 A100-h (SD 1.x family) | 0.43 |

The A100 equivalence uses a GH200 : A100 wall-clock ratio of 2.5–3.2×.

Sources:

- GenEval for SD 1.5, SD 2.1 and SDXL: the GenEval paper (arXiv 2310.11513, Table 2).
- PixArt-α: the SD3 paper (arXiv 2403.03206, Table 5).
- Meissonic: arXiv 2410.08261, Table 3.
- Compute figures: each model's card or paper. PixArt-α's 753 A100-days are converted from 1,656 V100-days; an earlier version of that paper said 675.

Every model we trained, same protocol (1 image per prompt, 553 images each):

| Model | Params | GPU-h | Single object | Two objects | Counting | Colours | Position | Colour binding | Overall |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Supra2-IMG SupraLabs, DiT, same dataset, external | 104M | ~9 H100-h | 0.613 | 0.071 | 0.263 | 0.457 | 0.030 | 0.030 | 0.244 |
| FCDM v1, epoch 10 convolutional flow model | 104M | 13.7 | 0.613 | 0.081 | 0.200 | 0.500 | 0.040 | 0.110 | 0.257 |
| FCDM v1, epoch 20 + fine-tuned Flan-T5 | 104M | 34.3 | 0.725 | 0.232 | 0.275 | 0.596 | 0.060 | 0.220 | 0.351 |
| DiT reproduction, epoch 10 Supra2-style DiT on our pipeline | 104M | 13.1 | 0.650 | 0.121 | 0.150 | 0.543 | 0.050 | 0.070 | 0.264 |
| fcdm2, epoch 10 planner + wider FCDM | 193M | ~34 | 0.688 | 0.242 | 0.150 | 0.649 | 0.070 | 0.240 | 0.340 |
| fcdm2, epoch 20 planner + wider FCDM | 193M | 68.0 | 0.850 | 0.414 | 0.287 | 0.670 | 0.210 | 0.380 | 0.469 |
| Run 1 thinker, epoch 10 first thinker-steered FCDM | 103M | 19.0 | 0.688 | 0.162 | 0.163 | 0.479 | 0.030 | 0.160 | 0.280 |
| T40r, epoch 10 thinker-steered FCDM-T2, Ettin encoder | 191M | 47.3 | 0.725 | 0.414 | 0.200 | 0.574 | 0.100 | 0.330 | 0.391 |
| T40r, epoch 16 end of 512-token phase 2 | 191M | 84.4 | 0.838 | 0.566 | 0.237 | 0.702 | 0.230 | 0.460 | 0.505 |
| T40r, step 82.8k caption-mix phase, midpoint | 191M | ~127 | 0.887 | 0.576 | 0.287 | 0.745 | 0.230 | 0.470 | 0.533 |
| Agate T40r final, cosine-annealed | 191M + 68M | 144.7 | 0.912 | 0.586 | 0.312 | 0.691 | 0.220 | 0.490 | 0.535 |
| Stable Diffusion 1.5 860M UNet + CLIP, 512 px, external | 983M | 150k A100-h | 0.950 | 0.323 | 0.362 | 0.734 | 0.010 | 0.010 | 0.398 |

SD 1.5 scores 0.398 here (one image per prompt) and 0.43 in the GenEval paper (four per prompt). Run the same way, Agate scores 0.535 and 0.550.

### Qwen-Image-Bench

Qwen-Image-Bench asks its judge model, Q-Judger (fine-tuned from Qwen3.6-27B), to grade each image against a per-prompt checklist in five areas. We ran the judge exactly as published: their checklists and aggregation code, greedy decoding, thinking on.

Full benchmark, all 1,000 prompts: Agate, SD 1.5 and the open text-to-image models closest to Agate in size.

| Model | Size | Native | Licence | Total | Quality | Aesthetics | Alignment | Real-world Fidelity | Creative Generation |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Agate | 191M + 68M text enc. | 256 px | MIT | 28.2 | 25.9 | 33.8 | 28.2 | 36.6 | 14.7 |
| Stable Diffusion 1.5 | 860M UNet + 123M CLIP | 512 px | CreativeML OpenRAIL-M | 29.1 | 36.7 | 28.0 | 25.7 | 38.9 | 15.5 |
| HobbyLM-Image | 334M DiT + CLIP-L | 1024 px | Apache-2.0 | 24.0 | 31.5 | 26.0 | 18.1 | 34.7 | 8.7 |
| TinyDiT-256 | 209M DiT + Flan-T5-base | 256 px | CC BY-NC 4.0 | 26.0 | 22.3 | 30.2 | 27.8 | 37.2 | 12.7 |
| Supra2-IMG | 104M DiT + Flan-T5-base | 256 px | Apache-2.0 | 17.8 | 12.7 | 23.5 | 16.5 | 33.3 | 5.9 |

Every model, 300 evenly spaced prompts:

| Model | Total | Quality | Aesthetics | Alignment | Real-world Fidelity | Creative Generation |
| --- | --- | --- | --- | --- | --- | --- |
| Supra2-IMG | 17.7 | 12.3 | 23.4 | 18.0 | 33.8 | 5.6 |
| FCDM v1, epoch 10 | 17.3 | 11.4 | 22.7 | 18.3 | 33.8 | 4.5 |
| FCDM v1, epoch 20 | 18.8 | 12.4 | 24.7 | 19.7 | 34.6 | 7.0 |
| DiT reproduction, epoch 10 | 19.7 | 15.9 | 25.8 | 19.0 | 34.6 | 5.7 |
| fcdm2, epoch 10 | 19.5 | 13.9 | 25.9 | 19.2 | 34.8 | 7.7 |
| fcdm2, epoch 20 | 21.3 | 16.3 | 26.1 | 23.1 | 35.2 | 7.8 |
| Run 1 thinker, epoch 10 | 20.0 | 15.6 | 26.0 | 19.2 | 35.0 | 7.6 |
| T40r, epoch 10 | 23.6 | 20.3 | 29.0 | 23.9 | 35.5 | 10.6 |
| T40r, epoch 16 | 24.8 | 21.3 | 30.4 | 25.7 | 36.4 | 11.1 |
| T40r, step 82.8k | 27.8 | 26.1 | 33.4 | 28.7 | 36.4 | 13.7 |
| Agate | 28.4 | 26.3 | 34.2 | 28.9 | 36.8 | 15.5 |
| Stable Diffusion 1.5 | 28.9 | 37.5 | 28.2 | 25.1 | 39.3 | 14.3 |

On all 1,000 prompts Agate scores 28.2 against SD 1.5's 29.1, close but behind. It leads on aesthetics (33.8 vs 28.0) and alignment (28.2 vs 25.7). It trails on quality (25.9 vs 36.7) and real-world fidelity (36.6 vs 38.9). The judge sees every image at 512 px, so Agate's 256 px output is upscaled first, which likely weighs on its quality score. Across our lineage the total climbs from 17.3 to 28.4 on the 300-prompt subset.

Judge outputs that failed to parse: 0. Scores are 0–100.

### Internal image metrics

Measured with our own eval suite (5,000 images, 256 px). These track training progress; they are not comparable with FID numbers from other papers:

| Model | Params | GPU-h | FID-5k ↓ | FD-DINOv2 ↓ |
| --- | --- | --- | --- | --- |
| FCDM v1, epoch 10 | 104M | 13.7 | 36.39 | 674 |
| FCDM v1, epoch 20 | 104M | 34.3 | 33.99 | 575 |
| DiT reproduction, epoch 10 | 104M | 13.1 | 38.57 | 660 |
| fcdm2, epoch 20 | 193M | 68.0 | 34.08 | 521 |
| Run 1 thinker, epoch 10 | 103M | 19.0 | 36.23 | 574 |
| T40r, epoch 10 | 191M | 47.3 | 36.49 | 542 |
| T40r, epoch 16 | 191M | 84.4 | 34.88 | 473 |
| Agate | 191M + 68M | 144.7 | 33.70 | 419 |

## Side by side

Supra2-IMG is the closest open model to Agate: a 104M DiT trained on the same dataset at the same resolution. SD 1.5 is the reference most people know.

## From the first baseline to Agate

## Manual test battery

60 prompts in 16 categories, two seeds each, rendered once with the released settings and shown uncurated.

What we read from it (the counts are prompts × seeds):

| Category | Result |
| --- | --- |
| Attribute binding | 8 / 8. Blue car + yellow bicycle, green teapot + red cup, white cat in a black hat, pink elephant in a purple room. |
| Spatial relations | 8 / 8. Left of, on top of, above, behind. |
| Faces, people | Strong for the size. Portraits, children, groups of three. |
| Styles | Watercolour, oil, pencil, anime, 3D render and flat vector all read correctly. |
| Logos, icons | Clean flat marks (fox, mountain). Text inside a logo turns to pseudo-letters. |
| Long prompts | Follows paragraph-long scene descriptions (bookshop, still life), keeping most of the listed details. |
| Imagination | Glass giraffe, snail teapot, a city in a seashell, a whale over a desert. |
| Counting | 3 / 8. Two is reliable; three is a coin flip; four and five usually come out wrong. |
| Text | 1 / 8 exact. "HELLO" once; "OPEN" becomes "OFEN", "MAIN ST" becomes "MAM ST". |
| Negation | Fails. "An empty bowl with no fruit" comes back full of fruit. |
| Pixel art | Renders a smooth cartoon, not pixels. |
| App icon (paper plane) | The plane shape is lost. |

## How Agate works

```
prompt ──► Ettin-68M (fine-tuned, 512 tokens) ──► text tokens
                                                     │ cross-attention
noise latent 4×32×32 ─┬─► thinker: prelude(3) → core(3) × 4 loops → coda(2), dim 640, on a 16×16 grid
                      │        └─► region map ──► low-rank steering (rank 128 / 256 / 256)
                      └─► FCDM U-Net: 32² (width 288, 4 blocks) · 16² (832, 6) · 8² (1664, 2) ──► velocity

```

- Backbone: the renderer is built on FCDM by Kwon et al., Reviving ConvNeXt for Efficient Convolutional Diffusion Models (arXiv:2603.09408). We keep its ConvNeXt block (7×7 depthwise conv, LayerNorm, modulation, inverted MLP with GRN from ConvNeXt V2, gate) and its three-level U-Net, and re-balance depth and width per level. FCDM's AdaLN takes one shift, scale and gate per image; ours takes a per-pixel map from the thinker. The renderer has no attention and never sees the text or the timestep: both reach it only through the thinker's region map.
- Rectified flow (Liu et al.; Lipman et al.): t = 0 is noise, t = 1 is data, and the network predicts the velocity. Sampling is 50 Euler steps with CFG 3 (Ho & Salimans).
- The thinker is a recurrent transformer. Its core blocks share weights across 4 loops, and each loop re-injects the prelude output, as in recurrent-depth transformers. Its latent cells read the image the way RIN and Perceiver latents do. It reads the text through cross-attention, with 2D RoPE and QK-norm on its attention.
- Steering: the thinker's region map sets a per-region shift, scale and gate in every U-Net block, a spatial form of FiLM as in SPADE, through a low-rank path.
- Autoguidance (optional): following Karras et al., Agate's own step-27,600 checkpoint is the "bad" guide. Unlike the paper, we add it on top of CFG rather than replacing the unconditional branch: v = v_uncond + cfg·(v_cond − v_uncond) + w·(v_cond − v_guide).
- Why this design: ablations on earlier runs showed where parameters paid off.

- The 32 × 32 convolution blocks were the most important in the network; 8 × 8 blocks could each be removed at under 1.5 % loss.
- The planner of our earlier fcdm2 model had learned per-level constants and ignored the prompt, so the thinker replaces it.
- The 32 × 32 steering maps had an effective rank of 2–3, so steering is low-rank and put where it is used.

## Training

| Data | FLUX-Reason-6M, 256 × 256, latents cached once with SD-VAE-ft-MSE |
| --- | --- |
| Objective | Rectified-flow velocity loss, 10 % caption dropout for CFG |
| Optimiser | AdamW, β 0.9 / 0.95, gradient clip 1.0, loss-spike guard, EMA weights released |
| Phase 1, steps 0 – 28k (epochs 1–10) | 4 nodes × 4 GH200 (16 GPUs), 2 h 57 min, batch 2,048, lr 2e-4, Ettin frozen, 128 text tokens |
| Phase 2, steps 28k – 44k (to epoch 16) | 16 GPUs, 2 h 19 min, Ettin trained jointly at lr 1e-5 |
| Caption phase, steps 44k – 99.25k (to epoch ~26) | 2 nodes × 4 GH200 (8 GPUs), 7 h 32 min, batch 1,024, 512 text tokens, caption mix, constant lr then cosine to 2e-5 (10 % floor) over the last 16.5k steps |
| Total | 99,250 steps, 146.9M images seen, 144.7 GH200-hours |

Measured from the training logs:

| | Phase 1 | Phase 2 | Caption phase |
| --- | --- | --- | --- |
| Throughput, images/s (median) | 6,193 | 5,431 | 2,157 |
| Per GPU, images/s | 387 | 339 | 270 |
| Peak VRAM per GPU | 45.4 GB | 52.5 GB | 53.4 GB |
| Mean GPU utilisation | 98.5 % | 98.5 % | 98.5 % |
| Loss at end | 0.660 | 0.645 | 0.626 |

Reading Agate's loss curve.

- Epochs 0–10: a fast drop, then a steady decline at constant learning rate with the text encoder frozen.
- Epoch 10, joint Ettin training: barely visible; the loss keeps falling.
- Epoch 16, the caption swap: the loss jumps from 0.647 to 0.653 over about 2,000 steps. Three things changed at step 44,250:

- the captions switched from the original prompts, cut at 128 tokens, to the caption mix (short fields, plus 20 % of batches with the long detail caption at up to 512 tokens);
- the global batch halved from 2,048 to 1,024 (16 to 8 GPUs);
- the learning rate re-warmed from 1e-5 to 2e-4.

A new conditioning distribution and noisier small-batch gradients both raise the loss at the same learning rate, and we cannot separate the two. The loss is not comparable across the swap. Within the new mix, long captions consistently score a lower loss than short ones (0.620 against 0.628 at the end): a detailed description leaves less for the model to guess.
- Epoch 23, the cosine anneal: from step 82,750 the learning rate falls from 2e-4 to 2e-5 over the last 16,500 steps. The loss drops from 0.641 to 0.627. That is more than the previous 37,500 steps at constant learning rate managed (0.653 to 0.641), because lower-noise updates settle the weights. Over the anneal, GenEval went from 0.533 to 0.535 and Qwen-Image-Bench from 27.8 to 28.4.

Across models, loss is comparable only within one text encoder and caption setup: the DiT reproduction reached a lower loss than FCDM v1 yet scored worse on FID.

Caption mix. FLUX-Reason-6M has eight English caption fields: composition, entity, text, imaginative, style, abstract, original and detail. Not every image has every field; each image draws from the fields it has. In 80 % of batches each image draws one short caption, weighted toward composition (layout is the weakest GenEval skill). The other 20 % use every image's long detail caption (median 217 tokens). The model therefore learns both what people type and what carries the concepts, and the jump to 512 tokens stops long captions from being truncated.

## Runs in the browser

A WebGPU build runs Agate entirely in the browser with onnxruntime-web, and prompts never leave the machine. With the same starting noise it matches the PyTorch pipeline to within 5/255 per pixel. It is a 530 MB download (fp16 weights, fp32 compute), then about 6 s per 50-step image on an RTX 4060.

## Training data and safety

Why FLUX-Reason-6M. We chose a curated, fully synthetic dataset built for compositional and reasoning prompts: objects, layouts, text, styles and imaginative scenes, not people or adult content. Its authors document quality filtering (blur, noise, structural distortion) but do not describe an NSFW filter. We have not audited all 5.65M images, so we cannot promise it contains no adult images. We expect such content to be rare at most.

Red-teaming. Before release we tested Agate adversarially for sexual content and for child sexual abuse material (CSAM).

- CSAM: Agate did not produce CSAM or any sexualised depiction of a minor.
- Adult nudity: we could not get Agate to generate genitals in any attempt. The worst output was a blurry nude female figure with no anatomical detail (no areolae).

Given the training data and these results, we consider explicit or abusive output practically infeasible for this model, and misuse unlikely.

Marginal risk. Agate adds little misuse risk to what is already public. Openly available models are far more capable of harmful imagery. They include Stable Diffusion 1.5, trained on LAION-5B, a dataset later found to contain child sexual abuse material (Stanford Internet Observatory, December 2023), and the many SD 1.5 and SDXL fine-tunes trained specifically on explicit content. Anyone seeking to misuse an image model has much stronger tools than a 256 px model that cannot render anatomy. That is our assessment, not a guarantee. Agate ships without a safety classifier, so public-facing deployments should add one.

Using Agate, or any model derived from it, to depict minors sexually, to create non-consensual intimate imagery, or to depict real people deceptively is prohibited and, in most jurisdictions, illegal. Report any such output to LogoLabs through logolabs.org.

## Compute and energy

Every GPU job was wrapped in perun, which measured 99 % of T40r's GPU time directly. Energy at the wall applies an assumed data-centre PUE of 1.3; CO₂e assumes 30 g/kWh for the Swedish SE3 grid. Neither factor is confirmed by NAISS yet. Seconds perun did not cover are counted at idle power, so the totals are a floor.

| Run | Jobs | GH200-h | kWh | kg CO₂e |
| --- | --- | --- | --- | --- |
| Latent cache (SD-VAE encode of the dataset) | 11 | 4.2 | 2.6 | 0.08 |
| FCDM v1, epochs 1-10 | 2 | 13.7 | 8.7 | 0.26 |
| FCDM v1, epochs 11-20 + Flan-T5 fine-tune | 1 | 20.6 | 13.5 | 0.41 |
| DiT reproduction, epochs 1-10 | 1 | 13.1 | 8.8 | 0.26 |
| fcdm2, all phases incl. restarts | 14 | 68.0 | 33.8 | 1.01 |
| Run 1 thinker, epochs 1-10 | 1 | 19.0 | 12.6 | 0.38 |
| T40r first try (diverged at step ~1,800) | 1 | 7.8 | 3.0 | 0.09 |
| T40r phase 1 (epochs 1-10) | 1 | 47.3 | 27.7 | 0.83 |
| T40r phase 2 (joint Ettin training, to epoch 16) | 1 | 37.1 | 18.8 | 0.56 |
| T40r caption phase (2 nodes, 8 h, cosine anneal) | 1 | 60.3 | 35.2 | 1.06 |
| T40r caption phase, two failed starts | 2 | 3.5 | 0.5 | 0.02 |
| Evaluations, smoke tests, benchmarks | 44 | 30.4 | 11.4 | 0.34 |
| Whole text-to-image project | 80 | 325.0 | 176.7 | 5.30 |

Agate itself cost 144.7 GH200-hours, 81.8 kWh and 2.45 kg CO₂e, or 156.0 GPU-hours counting its diverged first try and two failed starts. The whole project, dead ends, evaluations and benchmarks included, cost 325.0 GPU-hours and 5.30 kg CO₂e.

## What went wrong along the way

This card shows the failures as well as the wins:

- T40r diverged on its first try at step ~1,800 (unclipped lr 2.8e-4). The rerun uses lr 2e-4, gradient clipping and a loss-spike guard. Cost: 7.8 GPU-h.
- The caption phase ran out of memory, 95 GB on one GPU. The trainable Ettin ran eagerly, and variable text lengths gave the compiler a new shape at every step. Fixed-length text buckets and gradient checkpointing cut it to 52.7 GB.
- A logging bug crashed a run at step 44,845. The loss-spike guard skipped a step, and a per-caption-mode loss log then indexed past its end on the GPU.
- fcdm2's planner did nothing useful. Ablations showed it had learned per-level constants plus a copy of the timestep; prompt content carried 0.17 % of its output. The thinker replaced it.
- Lower loss did not mean better images. At 104M parameters with the same recipe, the DiT reproduction reached a lower training loss than FCDM v1 but scored worse on FID. Across architectures we compare only benchmarks.
- An LLM-judged GenEval overstated scores by ~0.11 against the official scorer on the same images. This card quotes only official GenEval.
- 512 px does not work. Agate was trained only at 256 px. At 512 px it dissolves into texture instead of composing a larger scene, so the pipeline always renders 256.
- cuDNN fused attention returned NaN gradients on GH200. It is disabled in training and in the pipeline.

## Limitations and intended use

- 256 × 256 only. Upscale externally if you need more pixels.
- Text rendering is unreliable, as are counts above three and negations ("no", "empty", "without").
- Synthetic training data. Every training image was generated by FLUX.1-dev. Agate inherits that model's look and biases, and it was never trained on a photograph.
- No safety classifier is bundled with the pipeline. Photorealistic people can be generated. Do not use Agate to depict real people or to deceive.
- Intended for research, education, prototyping and small-footprint deployment.

## Licence

MIT, for the code and the weights (see `LICENSE`). Agate was trained on FLUX-Reason-6M (Apache-2.0 per its dataset card), whose images were generated with FLUX.1-dev. The text encoder is fine-tuned from Ettin-68M (MIT); the SD-VAE and TAESD decoders (MIT) are downloaded from their own repositories.

## Acknowledgements

We acknowledge EuroHPC JU for awarding the project ID EHPC-AIF-2026PG01-907 access to resources on Arrhenius GPU at NAISS, Sweden.

Thank you to the EuroHPC Joint Undertaking, and to NAISS for running Arrhenius. A small team cannot usually train a text-to-image model from scratch; this allocation made it possible, and made it possible to do it openly. Every LogoLabs model in this card was trained under that EuroHPC AI Factory allocation. Besides Agate, that covers our FCDM v1, the DiT reproduction, fcdm2, the Run 1 thinker, and the T40r checkpoints at epochs 10 and 16 and step 82.8k. Their benchmarks are above. Together they account for the full 320.1 GPU-hours.

Thanks also to:

- the authors of FLUX-Reason-6M;
- Ettin (JHU CLSP);
- SD-VAE-ft-MSE (Stability AI);
- TAESD (Ollin Boer Bohan);
- GenEval (Ghosh et al.);
- Qwen-Image-Bench (Qwen team);
- perun;
- SupraLabs, for Supra2-IMG, the baseline this work started from.

| Inkvec | Exact SVG from logos, icons and flat artwork, entirely in your browser (WebAssembly). |
| --- | --- |
| Inkvec Denoiser | 19.7M-parameter cleanup of JPEG, WebP and VAE damage before tracing. |
| Inkvec Super-Resolution | 4× upscaling for logos and icons, fine-tuned MambaIRv2-Small. |
| LogoBrief-10K | 10,000 brand logos with SVGs, design briefs and style tags, opt-out audited before publication. |

## References

Architecture and training:

- Kwon et al., Reviving ConvNeXt for Efficient Convolutional Diffusion Models (FCDM), arXiv:2603.09408: the renderer's block and U-Net.
- Liu et al., A ConvNet for the 2020s, arXiv:2201.03545; Woo et al., ConvNeXt V2 (GRN), arXiv:2301.00808.
- Jabri et al., Scalable Adaptive Computation for Iterative Generation (RIN), arXiv:2212.11972; Jaegle et al., Perceiver / Perceiver IO, arXiv:2103.03206, arXiv:2107.14795: latent cells that read the image.
- Geiping et al., Scaling up Test-Time Compute with Latent Reasoning: A Recurrent Depth Approach, arXiv:2502.05171: the thinker's looped core.
- Su et al., RoFormer (RoPE), arXiv:2104.09864; Henry et al., Query-Key Normalization, arXiv:2010.04245; Wortsman et al., Small-scale proxies for large-scale Transformer training instabilities, arXiv:2309.14322.
- Perez et al., FiLM, arXiv:1709.07871; Park et al., SPADE, arXiv:1903.07291: per-region steering.
- Zhang et al., ControlNet, arXiv:2302.05543: zero-initialised growth.
- Liu et al., Rectified Flow, arXiv:2209.03003; Lipman et al., Flow Matching, arXiv:2210.02747; Esser et al., SD3, arXiv:2403.03206.
- Ho & Salimans, Classifier-Free Guidance, arXiv:2207.12598; Karras et al., Guiding a Diffusion Model with a Bad Version of Itself (autoguidance), arXiv:2406.02507.
- Weller et al., Ettin (Seq vs Seq), arXiv:2507.11412; Warner et al., ModernBERT, arXiv:2412.13663.
- Rombach et al., Latent Diffusion, arXiv:2112.10752; SD-VAE-ft-MSE; TAESD.
- Loshchilov & Hutter, AdamW, arXiv:1711.05101; Kumar et al., Fine-Tuning can Distort Pretrained Features (LP-FT), arXiv:2202.10054.

Data and evaluation:

- Fang et al., FLUX-Reason-6M & PRISM-Bench, arXiv:2509.09680.
- Ghosh et al., GenEval, arXiv:2310.11513; Cheng et al., Mask2Former, arXiv:2112.01527; Radford et al., CLIP, arXiv:2103.00020.
- Li et al., Qwen-Image-Bench, arXiv:2605.28091; Kwon et al., vLLM, arXiv:2309.06180.
- Heusel et al., FID, arXiv:1706.08500; Stein et al., FD-DINOv2, arXiv:2306.04675; Oquab et al., DINOv2, arXiv:2304.07193.
- Gutiérrez Hermosillo Muriedas et al., perun, Euro-Par 2023.

Compared and related models:

- Podell et al., SDXL, arXiv:2307.01952; Chen et al., PixArt-α, arXiv:2310.00426 and PixArt-Σ, arXiv:2403.04692; Bai et al., Meissonic, arXiv:2410.08261.
- Xie et al., SANA, arXiv:2410.10629; Sehwag et al., MicroDiT, arXiv:2407.15811; Pernias et al., Würstchen, arXiv:2306.00637; Hu et al., SnapGen, arXiv:2412.09619.
- Supra2-IMG, TinyDiT-256, HobbyLM-Image.

The technical report cites 119 works in full.

## Citation

```bibtex
@misc{logolabs2026agate,
  title        = {Agate: a 260M text-to-image model trained in 145 GPU-hours},
  author       = {Deleanu, Stefan-Lucian},
  organization = {LogoLabs},
  year         = {2026},
  howpublished = {\url{https://huggingface.co/Logolabs/agate-preview-001}}
}

```

## 关联链接

- https://huggingface.co/Logolabs/agate-preview-001}}

## 导航

- 项目页：[[10-项目/huggingface.co_c58e1c0c]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
