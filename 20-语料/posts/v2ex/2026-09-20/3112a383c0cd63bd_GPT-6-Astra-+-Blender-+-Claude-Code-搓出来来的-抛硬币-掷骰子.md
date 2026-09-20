---
type: "corpus"
item_id: "3112a383c0cd63bd"
title: "GPT-6 Astra + Blender + Claude Code 搓出来来的 抛硬币/掷骰子 模拟器，分享下开发过程"
source: "v2ex"
source_name: "V2EX"
url: "https://www.v2ex.com/t/1242891"
author: "swim2sun"
published_at: "2026-09-18T02:38:19"
captured_at: "2026-09-20T09:52:10+08:00"
lang: "zh"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-20"
pub_day: "2026-09-18"
tags:
  - 语料
  - v2ex
  - 17
metrics: {"replies": 0}
comments_count: 0
comments_total: 0
discovered_via: "v2ex:独立开发"
---

# GPT-6 Astra + Blender + Claude Code 搓出来来的 抛硬币/掷骰子 模拟器，分享下开发过程

> [!info] 一句话导读
> GPT-6 Astra 出来后最让我感兴趣的是它的 3D 建模能力，看到过网上各种 case ，让我也一直跃跃欲试。

> [!meta]- 语料信息（点开展开）
> 来源：V2EX（post）
> 原帖：<https://www.v2ex.com/t/1242891>
> 指标：回复=0
> 作者：swim2sun　|　发布：2026-09-18T02:38:19
> 项目链接：—
> 采集：2026-09-20T09:52:10+08:00　|　id：`3112a383c0cd63bd`

## 正文

GPT-6 Astra 出来后最让我感兴趣的是它的 3D 建模能力，看到过网上各种 case ，让我也一直跃跃欲试。

想到一个抛硬币的 idea ， 于是使用 codex 生成美术素材体验了一下，又使用 claude code 编写代码，最终效果挺让我满意的。


![](  )

## GPT-6 Astra + Blender 创建场景 + 骰子
手的模型是游戏素材网站找的免费可商用的模型，因为 GPT-6 Astra 目前还不擅长人体的建模。
花草树木、石头、远处的山都是 GPT-6 Astra 创建的，画风采用 low-poly 风格，既简单美观, 面数又少，适合移动端。
![](  )
![](  )


又让 gpt6 搭建出场景、制作动画
![](  )


后面决定加入掷骰子的功能，又让 AI 生成了不同面数的骰子
![](  )

感觉目前 codex 用来开发游戏的话应该没有对手，可能以后游戏资产就不是独立开发者的障碍了。

## Claude Code 编写小程序代码

最初是使用 Codex 写的，将素材导入到项目，搭建出了初版 demo ，但后面优化、细节的处理还是差点意思。一些小 bug 改来改去都解决不了。 
于是还是切换为 cc 来接手，顺利制作出了最终版本。


小程序名称：**抛个硬币小助手**


欢迎扫码体验：


![](  )

## 导航

- 项目页：—（本条不是项目，按设计不建实体页）
- 渠道页：[[50-渠道/v2ex]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
