---
type: "corpus"
item_id: "73755beea360e45f"
title: "给 PhotoCraft 做了两个浏览器试用入口，补了上手教程和 PSD 检查说明"
source: "v2ex"
source_name: "V2EX"
url: "https://www.v2ex.com/t/1248575"
project_url: "https://aiphotoshopclone.com/"
author: "rankinzheng"
published_at: "2026-10-14T00:55:54"
captured_at: "2026-10-16T09:38:51+08:00"
lang: "zh"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-10-16"
pub_day: "2026-10-14"
tags:
  - 语料
  - v2ex
  - 17
metrics: {"replies": 0}
comments_count: 0
comments_total: 0
discovered_via: "v2ex:独立开发"
---

# 给 PhotoCraft 做了两个浏览器试用入口，补了上手教程和 PSD 检查说明

> [!info] 一句话导读
> 最近把 PhotoCraft v0.8.2 的浏览器版部署了出来，做了两个独立站，想分享给需要临时改图、试用开源编辑器的朋友。

> [!meta]- 语料信息（点开展开）
> 来源：V2EX（post）
> 原帖：<https://www.v2ex.com/t/1248575>
> 指标：回复=0
> 作者：rankinzheng　|　发布：2026-10-14T00:55:54
> 项目链接：<https://aiphotoshopclone.com/>
> 采集：2026-10-16T09:38:51+08:00　|　id：`73755beea360e45f`

## 正文

最近把 PhotoCraft v0.8.2 的浏览器版部署了出来，做了两个独立站，想分享给需要临时改图、试用开源编辑器的朋友。

先说明：编辑器来自 [PhotoCraft 上游项目]( https://github.com/storytold/photocraft)，不是我从头开发的。我的工作主要是浏览器托管、进入工作区的体验、网站介绍和教程。这两个站都不是 Adobe 或 PhotoCraft 官方网站。

两个入口的内容侧重点不同，底层用的是同一款编辑器：

- [PhotoCraft.design]( https://photocraft.design/)：浏览器编辑入口和上手教程。可以先做一个“打开图片 → 加文字 → 导出 PNG”的小任务。
- [AI Photoshop Clone]( https://aiphotoshopclone.com/)：面向搜到“AI Photoshop clone”后想了解和试用的人，补了项目说明、功能限制和 PSD 检查清单。

两个站都免费、无需注册。点击 Open Editor 后，会在同一页面打开编辑工作区，支持图层、蒙版、文字、调色和部分 PSD 工作流；页面上的小 Logo 可以拖到侧边，用来返回首页或请求浏览器全屏。

我实际测试了新建 1920×1080 文档、添加文字图层、打开 Export As 并导出 PNG ；[首次编辑教程]( https://photocraft.design/tutorials/ai-photoshop-clone-getting-started/)也按这个流程写了步骤。

目前仍是 early alpha 。复杂 PSD 的字体、效果和图层兼容性需要自己检查；也没有自动保存或崩溃恢复，请用文件副本测试、及时保存。这里的“AI”是项目开发背景，这两个浏览器部署没有生成式填充、生图服务或连接好的 AI 助手。

欢迎试用，也想听听：这种临时改图的场景，你最需要哪一个功能？如果某个 PSD 打开或导出有差异，反馈浏览器、版本和大致操作步骤就很有帮助，不用公开原文件。

## 关联链接

- https://github.com/storytold/photocraft
- https://photocraft.design/
- https://photocraft.design/tutorials/ai-photoshop-clone-getting-started/

## 导航

- 项目页：[[10-项目/aiphotoshopclone.com_f3603235]]
- 渠道页：[[50-渠道/v2ex]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
