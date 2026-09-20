---
type: "corpus"
item_id: "d4b20be13794a111"
title: "Show HN: Connectome-inspired spiking network you can try in the browser"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49770006"
project_url: "https://awareliquid-sparse-snn-demo.static.hf.space/index.html"
author: "EverestAn"
published_at: "2026-09-19T20:49:52Z"
captured_at: "2026-09-20T09:48:16+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-20"
pub_day: "2026-09-19"
tags:
  - 语料
  - hn_show
  - author_EverestAn
  - story_49770006
  - show_hn
metrics: {"points": 3, "comments": 0, "engagement_velocity": 3}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:3d"
---

# Show HN: Connectome-inspired spiking network you can try in the browser

> [!info] 一句话导读
> Sparse-SNN — connectome-inspired spiking network

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49770006>
> 指标：点赞=3 · 评论=0 · engagement_velocity=3
> 作者：EverestAn　|　发布：2026-09-19T20:49:52Z
> 项目链接：<https://awareliquid-sparse-snn-demo.static.hf.space/index.html>
> 采集：2026-09-20T09:48:16+08:00　|　id：`d4b20be13794a111`

## 正文

Sparse-SNN — connectome-inspired spiking network

# 🧠 Sparse-SNN

 Draw a digit — a sparse spiking neural network (5% connection density, LIF neurons, masks from Drosophila connectome statistics) classifies it with event-driven additions only. Runs entirely in your browser via ONNX Runtime Web. · model · code

## Draw

 MNIST Fashion

## Prediction

draw something, then hit Recognize

 The network spikes only ~8% of its neurons per frame; each spike is an addition, not a multiply-accumulate. Energy estimates use a 45nm CMOS model (Horowitz 2014: MAC 3.7 pJ vs add 0.9 pJ).

 5% density LIF + surrogate gradient~112× estimated energy saving Honest boundaries — research artifact, not production. Dense-MLP gap: 1.5 pts (MNIST) / 0.5 pts (Fashion). Energy figures are analytic (45nm CMOS), not measured on hardware. In our experiments the static connectome topology gave no advantage — only its statistical laws transferred. · awareliquid.ai

# Free Online DSS & DS2 Player | Secure, No Server Upload

## 导航

- 项目页：[[10-项目/awareliquid-sparse-snn-demo.static.hf.space_8de4693f]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
