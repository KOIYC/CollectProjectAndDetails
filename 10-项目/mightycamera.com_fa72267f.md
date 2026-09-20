---
type: "project"
title: "Show HN: I built a tiny camera that knows where it is"
project_url: "https://mightycamera.com/story"
first_seen: "2026-09-20T14:06:34+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_asadm
  - story_49712254
  - show_hn
lang: "en"
---

# Show HN: I built a tiny camera that knows where it is

> [!info] 一句话导读
> I built a tiny camera that knows where it is

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://mightycamera.com/story>
> 首次收录：2026-09-20T14:06:34+08:00
> 来源渠道：HN Show HN
> 标签：author_asadm, story_49712254, show_hn
> 最新指标：点赞=5 · 评论=4 · engagement_velocity=5

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-09-20T09:23:24+08:00 | HN Show HN | 点赞=5 · 评论=4 · engagement_velocity=5 | [[20-语料/posts/hn_show/2026-09-20/81f4d13e01ff0e32_Show-HN-I-built-a-tiny-camera-that-knows-where-it]] |
| 2026-09-20T09:37:17+08:00 | HN Show HN | 点赞=5 · 评论=4 · engagement_velocity=5 | [[20-语料/posts/hn_show/2026-09-20/81f4d13e01ff0e32_Show-HN-I-built-a-tiny-camera-that-knows-where-it]] |
| 2026-09-20T14:06:34+08:00 | HN Show HN | 点赞=5 · 评论=4 · engagement_velocity=5 | [[20-语料/posts/hn_show/2026-09-20/81f4d13e01ff0e32_Show-HN-I-built-a-tiny-camera-that-knows-where-it]] |

## 摘要正文

I built a tiny camera that knows where it is | Mighty  # I built a tiny camera that knows where it is  > Onboard SLAM in a 10g camera. Twenty months from first prototype to shipping hardware.  Asad Memon · October 2024–July 2026 · From first prototypes to Batch 1  The production board: camera, IMU, and compute in one package.  I wanted SLAM for my hobby robot without adding a companion computer. The challenge was fitting visual-inertial odometry and loop closure onto a tiny, low-power camera board—and getting it to run in real time within the available compute and memory.  That became Mighty. It runs the estimation onboard and outputs position and orientation over USB or UART, so even an Arduino-based robot can consume the result. The finished board weighs 10g and produces pose at 20Hz.  My first ESP32 prototype could track image features, but the estimator hit a memory wall. Getting from that prototype to a shipping SLAM camera took twenty months of estimator optimization, hardware revisions, calibration work, and testing.  ## Position relative to what?  Mighty estimates motion relative to a local coordinate frame established when tracking starts. It gives your robot a position in…
