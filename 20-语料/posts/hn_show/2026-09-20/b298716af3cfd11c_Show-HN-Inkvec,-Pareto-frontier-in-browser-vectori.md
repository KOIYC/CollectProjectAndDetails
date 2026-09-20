---
type: "corpus"
item_id: "b298716af3cfd11c"
title: "Show HN: Inkvec, Pareto frontier in-browser vectorizer (Open Source)"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49761511"
project_url: "https://github.com/logolabs/inkvec"
author: "stefatorus"
published_at: "2026-09-18T23:13:10Z"
captured_at: "2026-09-20T14:01:34+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-20"
pub_day: "2026-09-18"
tags:
  - 语料
  - hn_show
  - author_stefatorus
  - story_49761511
  - show_hn
metrics: {"points": 2, "comments": 3, "engagement_velocity": 2}
comments_count: 3
comments_total: 3
discovered_via: "hn:show_hn:90d"
---

# Show HN: Inkvec, Pareto frontier in-browser vectorizer (Open Source)

> [!info] 一句话导读
> SoTA Vectorizer on the pareto frontier

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49761511>
> 指标：点赞=2 · 评论=3 · engagement_velocity=2
> 作者：stefatorus　|　发布：2026-09-18T23:13:10Z
> 项目链接：<https://github.com/logolabs/inkvec>
> 采集：2026-09-20T14:01:34+08:00　|　id：`b298716af3cfd11c`

## 正文

# logolabs/inkvec

SoTA Vectorizer on the pareto frontier

- Stars: 2
- Forks: 0
- Watchers: 2
- Open issues: 2
- License: Apache License 2.0
- Default branch: main
- Created: 2026-09-15T19:10:29Z

## Languages

- HTML
- JavaScript
- Python
- Rust
- Shell

## Top Contributors

- Stefatorus (1 contributions)

---

## README

Inkvec reads a PNG, JPEG, WebP, GIF, BMP or TIFF and writes an SVG whose geometry is decided by the evidence in the pixels:

- A boundary sits where the anti-aliasing says it is — within **~0.05 px** on analytic test circles (the level-set extraction's own resolution limit; `crates/inkvec-trace/src/coverage.rs`), which is a synthetic-input figure, not a corpus one.
- A circle is written as ` `, not four cubics pretending to be one.
- A smooth ramp becomes a **real gradient**, not coloured bands.
- The number of coordinates is chosen by **minimum description length** — not a tolerance slider you have to guess at.

Most tracers spend points wherever their curve-fit tolerance lets them. Inkvec spends them where the artist would have: one path per region, a circle where there is a circle, shared edges between shapes that never drift apart.

---

## Results

Inkvec vs two other engines (VTracer and Trazor) on **21 cases**, scored with CIEDE2000 colour error, DISTS, DINOv3, and coordinate count. The set is fixed from the selection seed `crosscompare-2026-09-15-v1` (`bench/crosscompare_current.py`): 14 hash-selected real icons (2 per family across lucide, material-icons, simple-icons, twemoji, noto-emoji, openmoji and fluent-emoji), 4 hand-picked synthetic probes (`prim_circle`, `mosaic_pie6`, `gradient_linear`, `gradient_radial`), and 3 real brand logos drawn from an external brand dataset that is not part of this repository — a clean clone selects only the other 18 (see `docs/results/2026-09-15.md`):

| Engine | Mean dE00 ↓ | Median dE00 ↓ | DISTS ↓ | DINO ↑ | Coords vs Inkvec | Time |
|---|---|---|---|---|---|---|
| **Inkvec** | **0.132** | **0.054** | **0.0236** | **0.991** | **1×** (446) | 1.17 s |
| VTracer (default; 0.6.15 / 1.0.0-alpha.4) | 1.303 | 0.598 | 0.051 | 0.963 | 4.4× (1,943) | 0.04–0.05 s |
| VTracer (tuned, 1.0.0-alpha.4) | 1.264 | 0.579 | 0.064 | 0.954 | 2.8× (1,239) | 0.06 s |
| Trazor | 0.518 | 0.227 | 0.048 | 0.971 | 2.6× (1,172) | 2.19 s |

The two VTracer defaults (0.6.15 and 1.0.0-alpha.4) are the **same engine**: they emit byte-different files but near-identical geometry (per-case dE00 0.0001–0.0012), and only the tuned setting differs materially — they are not independent corroboration. "Coords vs Inkvec" counts each primitive (` `, ` `, ` `) as 2 coordinates and each cubic as 6, which favours engines that emit primitives. Against the artist's own file, Inkvec's like-for-like ratio (`geom_ratio`: geometry parameters ÷ ground-truth geometry parameters) is 1.402 on this set. n = 21, with no error bars or significance test; the timings are approximate.

One engine is deliberately absent from the table: `color-trace` ("potrace-color", `migvel/color_trace` — pngquant quantisation + per-layer Potrace) is not apples-to-apples, because it reproduces the raster by drawing every pixel back rather than tracing artist-shaped geometry — on these same 21 cases its median dE00 is 0.229 at a median 25,018 coordinates, against Inkvec's 0.054 at 202 — roughly 124× the coordinates. Full detail in the non-apples-to-apples section of `docs/results/2026-09-15.md`.

VTracer is meaningfully faster — this is a quality/speed trade, not a free win. Source: `docs/results/2026-09-15.md`.

Per-case colour error (dE00) over the 21 cases — the distribution behind the table's mean and median, not only the summary. Reproduce with `python tools/make_engine_distribution.py`, which reads `bench/engine_per_item.json` (one row per case × engine).

Per-case coordinate count over the same 21 cases, from the same script and data file.

**Inkvec's row was re-measured on the 0.1.1 release build** (`inkvec.exe` sha256 `73c2f67a4e42194a42f72eba9063815942accb8e05d3e70e472fad1b5d115753`), and these two distribution charts are from that same run; the competitor rows are unchanged because their binaries reproduce exactly (VTracer default 1.303 / 1,943; tuned 1.264 / 1,239; Trazor 0.518 / 1,172).

> **On the regression corpus** (246 icons from lucide, material-icons, simple-icons, noto-emoji, openmoji, twemoji — the set CI gates on): **mean dE00 0.299**, 1.46× the parameters a human author would use. That mean is a family macro-average and is outlier-driven, so read it next to the **median (per-item) 0.125** — p10 0.024, p90 0.612, worst 5.72, and 13 of the 246 cases above dE00 1.0. The typical icon sits at ~0.125, and the mean is roughly 2.4× the median because a small tail pulls it up. (An earlier 0.149 figure came from a pre-release snapshot that was not reproducible; the baseline was re-recorded against the reproducible release build — see `CHANGELOG.md`.) Source: `bench/gate/baseline.json`.

### Damaged input: JPEG, WebP, AI-decoder output

Inkvec ships an optional trained restorer that removes compression and decode damage before tracing. It is **off by default** (`--restore off`; `--restore auto` enables it only when the input looks damaged). The weights that ship — `restorer.onnx` from `Logolabs/inkvec-denoiser-001`, pulled on first use or via `tools/pull_model.py` — have **no published benchmark in this repository**, and no LPIPS or ablation figure for them is reported anywhere here. The figures that previously appeared in this section were measured during development on a different checkpoint and are not reproduced for the shipped weights; the VectorArk and StarVector numbers were those projects' own published results, measured under their protocols, not here.

---

## Install

### Pre-built binaries

Download the latest release for your platform from the Releases page.

### Build from source

```sh
cargo install --path crates/inkvec-cli
```

or from a checkout:

```sh
cargo build --release -p inkvec-cli
target/release/inkvec logo.png -o logo.svg
```

Requires **Rust 1.88** or newer. `cargo test --release --workspace` runs 200+ tests.

---

## Quickstart

```sh
inkvec logo.png -o logo.svg
```

```
  intake        2x more pixels than detail: scaling min-area x4
logo.png (512x512)
  palette       3 colours, 26 faces (0 gradient)
  planar map    29 shared edges (3 primitive)
  boundary solve  E 285.5 -> 23.0 in 7 iteration(s), 7208 point(s) moved
  symmetry      none in the label map
  repair        0 boundary refit(s) to stop rings crossing
  segments      266  (160 line, 106 cubic) from 9176 measured points, 34.5x reduction
  lambda        8.54
  wrote         logo.svg (7886 bytes)
```

Exit codes: `0` success · `1` usage/input error · `2` flat input under `--strict` · `3` debug-dump write failure.

---

## Usage

```
inkvec <input> [-o <output.svg>] [OPTIONS]
```

| Flag | Default | What it does |
|---|---|---|
| `--restore <auto\|on\|off>` | off | Trained-network cleanup for JPEG/WebP/AI-decoder damage. `auto` only restores if it looks damaged. |
| `--sr <auto\|on\|off>` | off | Super-resolution pre-pass (2-4× upscale), complementary to `--restore`. |
| `--lossy <auto\|on\|off>` | auto | Whether to trust the file as clean or trace with noise-aware intake. |
| `--max-dim ` | 2048 | Cap on the longer side; SVG is written at the original size. |
| `--time-budget ` | 0 | Advisory wall-clock budget; trace is still correct if it runs out. |
| `--no-background` | off | Drop the face that paints the whole canvas. |
| `--minify` | off | No ids, no groups, no trailing zeros — ~10% smaller, identical geometry. |

Run `inkvec --help` for the full list.

---

## Optional features

| Feature | What it adds | Cost |
|---|---|---|
| `restore-model` | Trained restorer (`--restore`) via ONNX Runtime, CPU | Downloads prebuilt ONNX Runtime at build time |
| `restore-burn` | Same network via Burn, pure Rust, no n

# AI Autocomplete for Mac, On-Device and Private | TypeSeer

## 评论（3/3）

> **stefatorus** · 2026-09-18T23:13:10.000Z　
> Novel engineering contribution implementing several papers to improve the quality of raster-to-vector conversion.From our internal testing, it's the open-source SoTA, surpassed only by vectorizer.ai.It is built in Rust, has a wasm based version you can play with, and 2 models (one for SR, one for denoising) to help it work better with in-the-wild images.https://huggingface.co/spaces/Logolabs/inkvec

---

> **louSalah** · 2026-09-18T23:15:15.000Z　
> Really nice work. Curious how much of the quality gain comes from the SR/denoising models vs the vectorization algorithm itself?

---

> **stefatorus** · 2026-09-18T23:25:18.000Z　
> On PNGs, the benefit is smaller and mainly perceptual. dE00 actually decreases with the SR model but perceptual quality increases especially if the original raster was very low resolution.On JPEGs or other lossy compression inputs, both models help significantly. They've been trained with slightly different objectives. The SR one uses standard SR loss (with extra weighting near borders), the denoiser is trained to enforce the axioms that the vectorizer uses so it's the one that's recommended for production.I haven't tried running both at the same time, but it might be worth experimenting. Both are open weight so you can check yourself if curious.https://huggingface.co/Logolabs/inkvec-denoiser-001
> https://huggingface.co/Logolabs/inkvec-sr-001

## 导航

- 项目页：[[10-项目/github.com_7a920a59]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
