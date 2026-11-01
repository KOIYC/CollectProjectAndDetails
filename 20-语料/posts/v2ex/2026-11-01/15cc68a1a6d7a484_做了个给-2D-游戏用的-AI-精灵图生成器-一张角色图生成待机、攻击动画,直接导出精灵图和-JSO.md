---
type: "corpus"
item_id: "15cc68a1a6d7a484"
title: "做了个给 2D 游戏用的 AI 精灵图生成器：一张角色图生成待机、攻击动画，直接导出精灵图和 JSON"
source: "v2ex"
source_name: "V2EX"
url: "https://www.v2ex.com/t/1253461"
project_url: "https://spritecanvas.com/zh"
author: "bobo20240310"
published_at: "2026-10-31T16:14:45"
captured_at: "2026-11-01T09:43:04+08:00"
lang: "zh"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-11-01"
pub_day: "2026-10-31"
tags:
  - 语料
  - v2ex
  - 17
metrics: {"replies": 0}
comments_count: 0
comments_total: 0
discovered_via: "v2ex:副业"
---

# 做了个给 2D 游戏用的 AI 精灵图生成器：一张角色图生成待机、攻击动画，直接导出精灵图和 JSON

> [!info] 一句话导读
> 大家好，距离上次发帖已经过去挺久了。原因是 7 月底，我又失业了，哈哈哈。

> [!meta]- 语料信息（点开展开）
> 来源：V2EX（post）
> 原帖：<https://www.v2ex.com/t/1253461>
> 指标：回复=0
> 作者：bobo20240310　|　发布：2026-10-31T16:14:45
> 项目链接：<https://spritecanvas.com/zh>
> 采集：2026-11-01T09:43:04+08:00　|　id：`15cc68a1a6d7a484`

## 正文

大家好，距离上次发帖已经过去挺久了。原因是 7 月底，我又失业了，哈哈哈。

不过这次失业我到没有那么焦虑了，原因是通过这一年的折腾，副业还是有了点成果。

然后就是哪怕失业了，我跟朋友那边也在合作做一些游戏项目，目前有稳定的订单，虽然赚的不多，但是起码饿不死。

然后我最近几个月呢，也在打磨自己的全新的产品[SpriteCanvas]( https://spritecanvas.com/zh/?utm_source=v2ex&utm_medium=social&utm_campaign=v2ex-create)，一个给 2D 游戏做角色动画的工具。

起因是自己做小游戏：角色立绘用 AI 很快就能出，但一到“让它动起来”就卡住。逐帧手画不现实；用视频模型生成一段动画，又得自己抽帧、抠背景、对齐脚底、拼成图集、写每帧时长，一套下来比做游戏还累。SpriteCanvas 就是把这条链路做完，最后给你一张游戏引擎能直接用的精灵图。

## 效果

一张参考图，生成待机和攻击动画（ 35 帧，透明背景）：

![一张参考图生成待机和攻击动画](  )

剑士三连击，38 帧：

![剑士三连击](  )

技能特效也能单独生成，每个 6 帧、透明背景：

![火球、闪电、爆炸特效](  )

导出时可以勾“像素风”，每帧重绘到小像素网格上，整张精灵图共用一套 32 色调色板，帧与帧之间颜色不闪：

![普通导出和像素风导出对比](  )

## 怎么用

1. 描述角色，或者上传你已有的角色图。一次出几张候选，挑一张。
2. 选动作：待机、行走、奔跑、攻击、跳跃是内置的，也可以自己写动作描述。所有动作都从同一个角色生成，造型不会跑偏。
3. 逐帧检查，选帧范围和帧数。
4. 导出 PNG 精灵图和 JSON 图集。JSON 是 Phaser 、PixiJS 能直接读的 JSON Hash 格式，带每帧时长和脚底锚点。

做完还能在内置试玩场里用键盘跑、跳、打几下，先看看手感：

![工作台](  )

首页就有一个能玩的示例场景，不用注册：

![首页](  )

视频演示（ YouTube Shorts ）： https://youtube.com/shorts/vfHBoUoWIm4

## 不用登录的免费工具

顺手做了几个小工具，都在浏览器里本地处理，不用注册：

- [精灵图切片]( https://spritecanvas.com/zh/sprite-sheet-slicer/?utm_source=v2ex&utm_medium=social&utm_campaign=v2ex-create)：把一张精灵图切成单帧
- [GIF 转精灵图]( https://spritecanvas.com/zh/gif-to-sprite-sheet/?utm_source=v2ex&utm_medium=social&utm_campaign=v2ex-create)、[精灵图转 GIF]( https://spritecanvas.com/zh/sprite-sheet-to-gif/?utm_source=v2ex&utm_medium=social&utm_campaign=v2ex-create)
- [视频转精灵图]( https://spritecanvas.com/zh/video-to-sprite-sheet/?utm_source=v2ex&utm_medium=social&utm_campaign=v2ex-create)

还有一套 [CC0 免费素材包]( https://spritecanvas.com/zh/free-sprite-sheets/?utm_source=v2ex&utm_medium=social&utm_campaign=v2ex-create)（苔藓骑士 5 个动作、剑士，加史莱姆、蘑菇怪、哥布林、石头巨人几个怪物和一组特效），可商用，拿去测试游戏代码也行。

## 价格

- 邮箱验证后送 40 积分，7 天内有效；之后每天送 3 积分，最多攒到 12 ，免费积分只能用于标准画质。
- 每个任务开始前会显示要花多少积分；任务失败、没有产出时，积分会退回。
- 付费套餐 Starter 起步价 $12/月；也可以不订阅，单独买积分包。

## 目前的不足

- 它不是逐像素的像素画编辑器。像素风是在导出时重绘的，单个像素还得去 Aseprite 这类编辑器里修。
- 动画是排队生成的，要等一会儿，不是秒出。
- Unity 、Godot 的导入流程还没正式验证。现在确定能直接用的是 PNG 精灵图加 JSON （ Phaser 、PixiJS 已验证）。

想听听大家的意见：你做游戏时最缺哪类动作或素材？想要哪个引擎的导出？用下来哪里卡住了？评论区或者站内反馈都可以，谢谢！

## 关联链接

- https://spritecanvas.com/zh/?utm_source=v2ex&utm_medium=social&utm_campaign=v2ex-create
- https://spritecanvas.com/zh/free-sprite-sheets/?utm_source=v2ex&utm_medium=social&utm_campaign=v2ex-create
- https://spritecanvas.com/zh/gif-to-sprite-sheet/?utm_source=v2ex&utm_medium=social&utm_campaign=v2ex-create
- https://spritecanvas.com/zh/sprite-sheet-slicer/?utm_source=v2ex&utm_medium=social&utm_campaign=v2ex-create
- https://spritecanvas.com/zh/sprite-sheet-to-gif/?utm_source=v2ex&utm_medium=social&utm_campaign=v2ex-create
- https://spritecanvas.com/zh/video-to-sprite-sheet/?utm_source=v2ex&utm_medium=social&utm_campaign=v2ex-create
- https://youtube.com/shorts/vfHBoUoWIm4

## 导航

- 项目页：[[10-项目/spritecanvas.com_ba36d3c6]]
- 渠道页：[[50-渠道/v2ex]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
