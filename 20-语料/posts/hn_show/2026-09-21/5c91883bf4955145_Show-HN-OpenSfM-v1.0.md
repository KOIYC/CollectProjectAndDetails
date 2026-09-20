---
type: "corpus"
item_id: "5c91883bf4955145"
title: "Show HN: OpenSfM v1.0"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=48726208"
project_url: "https://github.com/OpenSfM/OpenSfM"
author: "AlgerianSam"
published_at: "2026-06-29T22:32:56Z"
captured_at: "2026-09-21T03:11:02+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-21"
pub_day: "2026-06-29"
tags:
  - 语料
  - hn_show
  - author_AlgerianSam
  - story_48726208
  - show_hn
metrics: {"points": 4, "comments": 0, "engagement_velocity": 4}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:113d"
---

# Show HN: OpenSfM v1.0

> [!info] 一句话导读
> Open source Structure-from-Motion pipeline and More

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=48726208>
> 指标：点赞=4 · 评论=0 · engagement_velocity=4
> 作者：AlgerianSam　|　发布：2026-06-29T22:32:56Z
> 项目链接：<https://github.com/OpenSfM/OpenSfM>
> 采集：2026-09-21T03:11:02+08:00　|　id：`5c91883bf4955145`

## 正文

# OpenSfM/OpenSfM

Open source Structure-from-Motion pipeline and More

- Stars: 76
- Forks: 13
- Watchers: 76
- Open issues: 3
- License: BSD 2-Clause "Simplified" License
- Homepage: https://opensfm.org/
- Default branch: master
- Created: 2026-04-10T09:08:21Z

## Languages

- Batchfile
- C++
- CMake
- CSS
- Emacs Lisp
- HTML
- JavaScript
- Python
- Shell

## Topics

- 3d-reconstruction
- cpp
- python
- sfm

## Top Contributors

- paulinus (1487 contributions)
- YanNoun (911 contributions)
- oscarlorentzon (246 contributions)
- fabianschenk (218 contributions)
- ybkuang (188 contributions)
- pierotofy (91 contributions)
- mlopezantequera (61 contributions)
- DodgySpaniard (25 contributions)
- github-actions[bot] (23 contributions)
- r-barnes (21 contributions)

---

## README

OpenSfM

OpenSfM
=======
Conda Docker Ubuntu 20.04 Docker Ubuntu 24.04

Coverage

Discord

## 🧟 Intro
This repository continues the original OpenSfM project, which is no longer in active development. We were maintainers and contributors of the original OpenSfM, and we will do our best to keep it alive and serve the community and our users (OpenDroneMap, WebODM and many others).

This **1.0** release focuses on the needs of those two biggest users — OpenDroneMap and WebODM — hence the strong emphasis on **GIS / geo workflows**. See the release notes for the full feature list.

## 🔭 Overview
OpenSfM is an open-source Structure-from-Motion (SfM) library written in Python with performance-critical code in C++. It reconstructs camera poses and sparse 3D points from unordered image collections, and goes all the way to **dense point clouds, meshes, and georeferenced 2D maps (DSM, orthophoto)** — with GPU acceleration throughout.

**🧩 Core pipeline**

Feature detection (SIFT, HAHOG, DSP-SIFT, AKAZE, SURF, ORB), GPU (OpenCL) matching — both online-trained binary-quantized descriptors and classic FLANN — with geometric verification, track building, and incremental + direct aerotriangulation reconstruction. Robust Ceres-based bundle adjustment, switching to a stochastic solver for very large scenes. Pair selection by GPS, capture time, file order, or image similarity (BoW / VLAD). See pipeline commands and the configuration reference.

SfM Reconstruction

**📐 Camera models**

Perspective, Brown, fisheye (OpenCV model and custom 62 / 624 parameters), spherical / equirectangular, and dual — with rolling-shutter correction. Lab-calibrated intrinsics can be injected and frozen, and multi-camera rigs are fully supported and can be auto-calibrated. See camera models and rig models.

**🧭 Geolocation & georeferencing**

GPS positions (with per-image X/Y/Z standard deviation) from EXIF or imported from a text file; ground control points and checkpoints (with per-point standard deviation) in any CRS. Horizontal + vertical coordinate systems via EPSG codes, compound EPSG, or PROJ strings, with geoids fetched on demand from the PROJ CDN, and adaptive datum-shift compensation. See georeferencing & GIS outputs and ground control points.

**🍇 Dense reconstruction**

Multi-view depth estimation via GPU PatchMatch (OpenCL), sparse-voxel-octree TSDF fusion with optional photometric refinement, and a Surface Nets (dual-contouring) mesh. Exports the dense cloud as PLY / LAS / LAZ, the mesh as PLY, and Potree-style octree tiles for streaming web viewers. See dense reconstruction & 2D maps.

Dense Reconstruction

**🧇 2D maps — DSM & orthophoto**

Direct, TSDF-based Digital Surface Model and orthophoto rendering, with hole filling, an edge-sharpening shock filter, and robust multi-view color baking. Accurately georeferenced to the output CRS (3rd-degree polynomial fit, TPS fallback) and exported as GeoTIFF. See 2D maps.

DSM and Ortho Extraction

**🪜 Scalability**

Out-of-core submodel splitting / merging for large scenes, rig constraints for multi-camera setups, stochastic bundle adjustment, and configurable multi-processing. See large datasets.

**📦 Exports**

COLMAP, Bundler, OpenMVS, PMVS, VisualSFM, PLY, LAS/LAZ, GeoJSON, and GeoTIFF — see the exporters.

**🩺 Quality report**

SfM metrics, GPS/GCP and checkpoint error tables, and DSM/ortho previews, localized in metric or imperial units and in five languages (en/fr/es/de/it), exported as a PDF. See quality report and an example report.

**🥽 Visualisation**

A built-in JavaScript viewer for interactive 3D preview and pipeline debugging, a web point-cloud viewer fed by the Potree octree tiles, and a Rerun export of the scene with its GPS/GCP data.

Rerun Export

**🤝 Compatibility** —
Runs on Linux, macOS (Apple Silicon), and Windows. See the quickstart to get started.

**🫶 Credits** —
OpenSfM was created by Pau Gargallo and bootstrapped by Mapillarians — check out this blog post with more demos.

## 🛫 Getting Started

Install using conda lock files (see building instructions):

**Linux:**
```bash
conda create --name opensfm --file conda-linux-64.lock --yes
conda activate opensfm && pip install -e .
```

**macOS (Apple Silicon):**
```bash
conda create --name opensfm --file conda-osx-arm64.lock --yes
conda activate opensfm && pip install -e .
```

Then reconstruct a dataset:
```bash
conda activate opensfm
./bin/opensfm_run_all path/to/dataset   # Linux/macOS
bin\opensfm_run_all.bat path\to\dataset  # Windows
```

**Workflow presets** — ready-made `config.yaml` files tuned for common capture types live in `configs/` (`aerial`, `terrestrial`, `object`). Copy one into your dataset to start from sensible defaults: `cp configs/aerial.yaml path/to/dataset/config.yaml`. See workflow presets.

## ⏱️ Benchmarking

A built-in harness measures the impact of a change on **speed and quality across commits**. It builds any commit in an isolated git worktree + conda env, runs the pipeline on your datasets, and produces an HTML report that diffs the run against a reference commit (green = better, red = worse).

```bash
# Baseline, then your branch compared against it
python -m benchmark.run --config benchmark/benchmark_example.json --commit master
python -m benchmark.run --config benchmark/benchmark_example.json --commit my-feature --reference master
```

Add `--dense` to include the dense stages, or `--resume` to recover an interrupted run. See the benchmarking guide for the full workflow — resuming, report-only regeneration, and partial re-runs.

## 📚 Documentation

**Getting Started**
* Quickstart
* Building & Installation
* Pipeline Commands

**User Guide**
* Dataset structure
* Configuration reference
* Ground control points
* Rig models
* Large datasets
* Dense reconstruction & 2D maps
* Georeferencing & GIS outputs
* Quality report
* Troubleshooting

**Reference**
* Camera models & coordinate systems
* Reconstruction algorithm
* Sensor / calibration database
* Reporting

**Mathematical Notes**
* Dense matching
* Reconstruction merging

**Development**
* Benchmarking

## ⚖️ License
OpenSfM is BSD-style licensed, as found in the LICENSE file.

Example data in the README is under Creative Commons CC-BY 4.0 License by Wingtra AG, 8045 Zürich, Switzerland.

# Market Terminal

## 关联链接

- https://opensfm.org/

## 导航

- 项目页：[[10-项目/github.com_3292151c]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
