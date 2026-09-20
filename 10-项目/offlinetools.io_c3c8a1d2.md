---
type: "project"
title: "Show HN: I ported COLMAP (photogrammetry) to the browser in WASM and WebGPU"
project_url: "https://offlinetools.io/colmap-landing"
first_seen: "2026-09-20T09:37:11+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_rsp1984
  - story_49715142
  - show_hn
lang: "en"
---

# Show HN: I ported COLMAP (photogrammetry) to the browser in WASM and WebGPU

> [!info] 一句话导读
> COLMAP browser workspace

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://offlinetools.io/colmap-landing>
> 首次收录：2026-09-20T09:37:11+08:00
> 来源渠道：HN Show HN
> 标签：author_rsp1984, story_49715142, show_hn
> 最新指标：点赞=3 · 评论=0 · engagement_velocity=3

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-09-20T09:23:24+08:00 | HN Show HN | 点赞=3 · 评论=0 · engagement_velocity=3 | [[20-语料/posts/hn_show/2026-09-20/a128cc683022dec9_Show-HN-I-ported-COLMAP-(photogrammetry)-to-the-br]] |
| 2026-09-20T09:37:11+08:00 | HN Show HN | 点赞=3 · 评论=0 · engagement_velocity=3 | [[20-语料/posts/hn_show/2026-09-20/a128cc683022dec9_Show-HN-I-ported-COLMAP-(photogrammetry)-to-the-br]] |

## 摘要正文

COLMAP browser workspace  # COLMAP browser workspace   A faithful & high-performance port of COLMAP SfM for the browser   South Building, 128 images, Global Positioning, Original Speed  ## Runs locally in your browser  No footage leaves your computer  ### SIFT keypoints  Elapsed time in minutes. Lower is better.   SIFT GPU (browser) 0:54 min   SIFT GPU (stock COLMAP) 1:41 min   SIFT CPU (browser) 1:25 min   SIFT CPU (stock COLMAP) 1:46 min   Settings: 229 images, input size 5616x3744, max_image_size 2400, max_num_features 8192, first octave 0, num octaves 4, octave resolution 3, peak=0.007, edge=10, # orientations: 2, no-affine, no-upright, no-DSP.   Host: AMD Ryzen 7 5800X 8-Core, RTX 3700 GPU (8 GB), 32 GB RAM  ### Sparse Mapping  Elapsed time in minutes. Lower is better.   CPU (browser) 1:37 min   CPU (stock COLMAP) 1:47 min   Input: 229 images, 50k sparse points.   Host: AMD Ryzen 7 5800X 8-Core, RTX 3700 GPU (8 GB), 32 GB RAM  ## Inspect every frame in detail  Inspect keypoints, matches, and masks for every frame.  Depth Maps Sky Masks   Powered by Microsoft™ MoGe™  ## Extract video frames  video_frame_1.jpg  video_frame_2.jpg  video_frame_3.jpg  video_frame_4.jpg  ## Crop poi…
