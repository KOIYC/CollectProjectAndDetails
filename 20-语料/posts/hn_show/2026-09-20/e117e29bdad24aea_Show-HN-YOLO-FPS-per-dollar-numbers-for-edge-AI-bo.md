---
type: "corpus"
item_id: "e117e29bdad24aea"
title: "Show HN: YOLO FPS-per-dollar numbers for edge AI boards ($75-$215)"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49729336"
project_url: "https://github.com/chorylee/edge-ai-benchmarks"
author: "chorylee"
published_at: "2026-09-16T16:20:59Z"
captured_at: "2026-09-20T09:37:00+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-20"
pub_day: "2026-09-16"
tags:
  - 语料
  - hn_show
  - author_chorylee
  - story_49729336
  - show_hn
metrics: {"points": 4, "comments": 0, "engagement_velocity": 4}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:90d"
---

# Show HN: YOLO FPS-per-dollar numbers for edge AI boards ($75-$215)

> [!info] 一句话导读
> chorylee/edge-ai-benchmarks

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49729336>
> 指标：点赞=4 · 评论=0 · engagement_velocity=4
> 作者：chorylee　|　发布：2026-09-16T16:20:59Z
> 项目链接：<https://github.com/chorylee/edge-ai-benchmarks>
> 采集：2026-09-20T09:37:00+08:00　|　id：`e117e29bdad24aea`

## 正文

# chorylee/edge-ai-benchmarks

- Stars: 0
- Forks: 0
- Watchers: 0
- Open issues: 0
- Default branch: main
- Created: 2026-09-16T16:15:59Z

## Top Contributors

- chorylee (1 contributions)

---

## README

# Edge AI Benchmarks — real FPS numbers, no vendor slides

I benchmark China's edge-AI hardware scene: street prices, BOM math, and the FPS numbers vendors would rather you didn't compare. This repo holds the raw data behind RoboKrunch — every figure traceable to a datasheet, a vendor table, or a receipt.

## YOLO FPS per dollar (September 2026)

| Platform | NPU | Model | FPS | Board price | FPS/$ | Source |
|---|---|---|---|---|---|---|
| Orange Pi 5 Max (4GB) | RK3588, 6 INT8 TOPS, single NPU core | YOLOv5s | 66.1 | **$75** | 0.88 | Rockchip model zoo |
| Orange Pi 5 Max (8GB) | RK3588, 6 INT8 TOPS, single NPU core | YOLOv5s | 66.1 | **$95** | 0.70 | Rockchip model zoo |
| Hailo-8 M.2 module | Hailo-8, 26 dense INT8 TOPS | YOLOv5m | 156 | **~$215** | 0.73 | Hailo official tables |
| Jetson Orin Nano 8GB | Orin Nano, 40 sparse INT8 TOPS | — | — | $299 MSRP / $369–$800+ street | — | NVIDIA |

Machine-readable: `benchmarks.csv`

**Read this before you screenshot the table:**

- **The FPS figures are vendor-reported**, not from my lab (yet). Rockchip's own model zoo claims 66.1 FPS on YOLOv5s with a single NPU core; Hailo's tables claim 156 FPS on the larger YOLOv5m. Independent verification is on the roadmap — that's the point of this repo.
- **TOPS are not fungible.** NVIDIA's 40 are *sparse* INT8, Hailo's 26 are *dense* INT8, Rockchip's 6 are INT8 on yet another architecture. Cross-vendor TOPS division is directionally useful and precisely wrong.
- **The YOLO variants differ** (v5s vs v5m), so the FPS/$ column is a rough price-performance sketch, not a ranking. The curve is smooth, not a cliff: you get what you pay for.
- **Prices are September 2026 street/list prices** and move constantly. Treat them as directional.

## Also measured

- **LLM on RK3588 CPU (not NPU):** community members have coaxed Qwen2.5-0.5B to ~12 tokens/sec via llama.cpp. A party trick, not a product strategy — the NPU can't run generative workloads, and neither can this CPU at any serious scale.

## The analysis behind the numbers

- Full breakdown of where the 4x price gap goes (Shenzhen supply chain, the software tax, BOM math): The $75 AI Computer
- Weekly dispatch on China's edge-AI hardware scene: robokrunch.com

## Contribute your numbers

Got a board and a stopwatch? Open a PR or issue with: board, SoC/NPU, model + input size, FPS, how you measured it, and what you paid. Vendor tables welcome too — label them as such and link the source.

## Corrections

Found an error? That's what this repo is for. Open an issue or email service@robokrunch.com. Corrections are published, not buried.

## License

Code: MIT. Data (`benchmarks.csv`): CC-BY-4.0 — use it, just credit RoboKrunch.

Error fetching https://twitter.com/freemyipod/status/2100255707886977402: SOURCE_NOT_AVAILABLE

## 关联链接

- https://twitter.com/freemyipod/status/2100255707886977402:

## 导航

- 项目页：[[10-项目/github.com_89c37c05]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
