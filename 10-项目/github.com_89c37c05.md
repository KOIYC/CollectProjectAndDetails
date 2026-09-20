---
type: "project"
title: "Show HN: YOLO FPS-per-dollar numbers for edge AI boards ($75-$215)"
project_url: "https://github.com/chorylee/edge-ai-benchmarks"
first_seen: "2026-09-20T09:37:00+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_chorylee
  - story_49729336
  - show_hn
lang: "en"
---

# Show HN: YOLO FPS-per-dollar numbers for edge AI boards ($75-$215)

> [!info] 一句话导读
> chorylee/edge-ai-benchmarks

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://github.com/chorylee/edge-ai-benchmarks>
> 首次收录：2026-09-20T09:37:00+08:00
> 来源渠道：HN Show HN
> 标签：author_chorylee, story_49729336, show_hn
> 最新指标：点赞=4 · 评论=0 · engagement_velocity=4

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-09-20T09:23:24+08:00 | HN Show HN | 点赞=4 · 评论=0 · engagement_velocity=4 | [[20-语料/posts/hn_show/2026-09-20/e117e29bdad24aea_Show-HN-YOLO-FPS-per-dollar-numbers-for-edge-AI-bo]] |
| 2026-09-20T09:37:00+08:00 | HN Show HN | 点赞=4 · 评论=0 · engagement_velocity=4 | [[20-语料/posts/hn_show/2026-09-20/e117e29bdad24aea_Show-HN-YOLO-FPS-per-dollar-numbers-for-edge-AI-bo]] |

## 摘要正文

# chorylee/edge-ai-benchmarks  - Stars: 0 - Forks: 0 - Watchers: 0 - Open issues: 0 - Default branch: main - Created: 2026-09-16T16:15:59Z  ## Top Contributors  - chorylee (1 contributions)  ---  ## README  # Edge AI Benchmarks — real FPS numbers, no vendor slides  I benchmark China's edge-AI hardware scene: street prices, BOM math, and the FPS numbers vendors would rather you didn't compare. This repo holds the raw data behind RoboKrunch — every figure traceable to a datasheet, a vendor table, or a receipt.  ## YOLO FPS per dollar (September 2026)  | Platform | NPU | Model | FPS | Board price | FPS/$ | Source | |---|---|---|---|---|---|---| | Orange Pi 5 Max (4GB) | RK3588, 6 INT8 TOPS, single NPU core | YOLOv5s | 66.1 | **$75** | 0.88 | Rockchip model zoo | | Orange Pi 5 Max (8GB) | RK3588, 6 INT8 TOPS, single NPU core | YOLOv5s | 66.1 | **$95** | 0.70 | Rockchip model zoo | | Hailo-8 M.2 module | Hailo-8, 26 dense INT8 TOPS | YOLOv5m | 156 | **~$215** | 0.73 | Hailo official tables | | Jetson Orin Nano 8GB | Orin Nano, 40 sparse INT8 TOPS | — | — | $299 MSRP / $369–$800+ street | — | NVIDIA |  Machine-readable: `benchmarks.csv`  **Read this before you screenshot the table:**  - …
