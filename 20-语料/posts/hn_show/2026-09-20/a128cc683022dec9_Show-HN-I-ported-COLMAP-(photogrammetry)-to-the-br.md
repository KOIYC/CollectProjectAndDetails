---
type: "corpus"
item_id: "a128cc683022dec9"
title: "Show HN: I ported COLMAP (photogrammetry) to the browser in WASM and WebGPU"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49715142"
project_url: "https://offlinetools.io/colmap-landing"
author: "rsp1984"
published_at: "2026-09-15T16:40:47Z"
captured_at: "2026-09-20T09:37:11+08:00"
lang: "en"
kind: "post"
topic: "开发者工具"
shard: "2026-09-20"
pub_day: "2026-09-15"
tags:
  - 语料
  - hn_show
  - author_rsp1984
  - story_49715142
  - show_hn
metrics: {"points": 3, "comments": 0, "engagement_velocity": 3}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:90d"
---

# Show HN: I ported COLMAP (photogrammetry) to the browser in WASM and WebGPU

> [!info] 一句话导读
> COLMAP browser workspace

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49715142>
> 指标：点赞=3 · 评论=0 · engagement_velocity=3
> 作者：rsp1984　|　发布：2026-09-15T16:40:47Z
> 项目链接：<https://offlinetools.io/colmap-landing>
> 采集：2026-09-20T09:37:11+08:00　|　id：`a128cc683022dec9`

## 正文

COLMAP browser workspace

# COLMAP browser workspace

 A faithful & high-performance port of COLMAP SfM for the browser

 South Building, 128 images, Global Positioning, Original Speed

## Runs locally in your browser

No footage leaves your computer

### SIFT keypoints

Elapsed time in minutes. Lower is better.

 SIFT GPU (browser) 0:54 min

 SIFT GPU (stock COLMAP) 1:41 min

 SIFT CPU (browser) 1:25 min

 SIFT CPU (stock COLMAP) 1:46 min

 Settings: 229 images, input size 5616x3744, max_image_size 2400, max_num_features 8192, first octave 0, num octaves 4, octave resolution 3, peak=0.007, edge=10, # orientations: 2, no-affine, no-upright, no-DSP.

 Host: AMD Ryzen 7 5800X 8-Core, RTX 3700 GPU (8 GB), 32 GB RAM

### Sparse Mapping

Elapsed time in minutes. Lower is better.

 CPU (browser) 1:37 min

 CPU (stock COLMAP) 1:47 min

 Input: 229 images, 50k sparse points.

 Host: AMD Ryzen 7 5800X 8-Core, RTX 3700 GPU (8 GB), 32 GB RAM

## Inspect every frame in detail

Inspect keypoints, matches, and masks for every frame.

Depth Maps Sky Masks

 Powered by Microsoft™ MoGe™

## Extract video frames

video_frame_1.jpg

video_frame_2.jpg

video_frame_3.jpg

video_frame_4.jpg

## Crop points ...

... and cameras

## Import/Export

 Keypoints

 Matches

 Entire datasets

# Extract Images from PDF (Original Quality) | imissfiles

## 导航

- 项目页：[[10-项目/offlinetools.io_c3c8a1d2]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`开发者工具`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
