---
type: "corpus"
item_id: "36e01ccedbaff5e8"
title: "两个月了，我的“自研”游戏引擎进展"
source: "bilibili"
source_name: "B 站"
url: "https://www.bilibili.com/video/BV1qrtY6hEmz"
author: "那只敏捷的棕毛狐狸"
published_at: "2026-09-01T05:15:01+08:00"
captured_at: "2026-09-30T18:53:00+08:00"
lang: "zh"
kind: "post"
topic: 开发者工具
shard: "2026-09-30"
pub_day: "2026-09-01"
tags:
  - 语料
  - bilibili
  - 游戏引擎
  - unreal
  - godot
  - 游戏开发
  - AI
  - 人工智能
metrics: {"play": 9582, "danmaku": 3, "favorites": 114}
comments_count: 0
comments_total: 0
discovered_via: "bili:独立开发"
---

# 两个月了，我的“自研”游戏引擎进展

> [!info] 一句话导读
> 📝 完整更新记录（自 2026-07-12 上次视频）

> [!meta]- 语料信息（点开展开）
> 来源：B 站（post）
> 原帖：<https://www.bilibili.com/video/BV1qrtY6hEmz>
> 指标：播放=9582 · 弹幕=3 · 收藏=114
> 作者：那只敏捷的棕毛狐狸　|　发布：2026-09-01T05:15:01+08:00
> 项目链接：—
> 采集：2026-09-30T18:53:00+08:00　|　id：`36e01ccedbaff5e8`

## 正文

## 📝 完整更新记录（自 2026-07-12 上次视频）

### 🎨 渲染管线
- 全面迁移至 **WebGPU (Dawn)**，删除 bgfx，唯一渲染路径
- **Clustered Forward+ 集群渲染**：光源按视锥集群剔除
- **PBR + IBL**：BRDF LUT 预积分、间接光 GGX 预滤波
- **CSM 级联阴影（6 级）** + PCF 软阴影，级联边界固定正交范围防抖动
- **SSAO**（Crytek 深度重建，半分辨率 + 深度感知模糊）
- Bloom

## 导航

- 项目页：—（本条不是项目，按设计不建实体页）
- 渠道页：[[50-渠道/bilibili]]
- 赛道：`开发者工具`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
