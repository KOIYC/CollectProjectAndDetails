---
type: "corpus"
item_id: "996457c51c6d747e"
title: "自己做的语音日记 Thinkdown：中英文夹杂着说，整理成一篇通顺的笔记"
source: "v2ex"
source_name: "V2EX"
url: "https://www.v2ex.com/t/1257687"
project_url: "https://app.thinkdown.app/"
author: "benxie"
published_at: "2026-11-17T06:09:33"
captured_at: "2026-11-19T09:46:37+08:00"
lang: "zh"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-11-19"
pub_day: "2026-11-17"
tags:
  - 语料
  - v2ex
  - 17
metrics: {"replies": 0}
comments_count: 0
comments_total: 0
discovered_via: "v2ex:独立开发"
---

# 自己做的语音日记 Thinkdown：中英文夹杂着说，整理成一篇通顺的笔记

> [!info] 一句话导读
> 大家好，我是 Xie，在加州的独立开发者。

> [!meta]- 语料信息（点开展开）
> 来源：V2EX（post）
> 原帖：<https://www.v2ex.com/t/1257687>
> 指标：回复=0
> 作者：benxie　|　发布：2026-11-17T06:09:33
> 项目链接：<https://app.thinkdown.app/>
> 采集：2026-11-19T09:46:37+08:00　|　id：`996457c51c6d747e`

## 正文

大家好，我是 Xie，在加州的独立开发者。

最近做了一个语音日记 App：Thinkdown。对着它随便说，说乱了也没关系，它会把你说的话整理成一篇通顺的笔记，用的还是你自己的话。嗯啊、重复、说一半改口的都会去掉。

为什么先说中英混说：我自己说话就是中英夹杂，比如“今天 meeting 又被 push 到下周了”。系统自带的听写基本只认一种语言，另一种就乱了。Thinkdown 两种都留着，整理出来的笔记可以保持原样，也可以统一成中文或英文（一共支持 21 种语言）。

其他功能：
• 人名、地名记一次，以后都写对
• 原始录音和逐字稿都保留，随时对照
• 可以直接问自己的笔记，比如“上次见老王是什么时候？”，回答会标出是哪几篇笔记
• 日历、地点和天气、从 Day One / Notion / Obsidian 等导入，导出 Markdown 或 PDF
• iPhone、iPad、Mac、Apple Watch 和网页版，数据同步。Android 在做。

不用注册先试一次：网页版打开就是录音按钮，不用注册，说上两分钟以内，停下就能看到整理好的笔记。每个浏览器可以免登录试一次，想保存或继续录再登录。 

App Store：https://apps.apple.com/app/thinkdown/id6823237700
https://app.thinkdown.app/?ref=v2ex 


价格：免费版每条可录 15 分钟，每月 60 分钟（到 1 月底）。Pro 每月 $8.99（可试用 7 天），或每年 $59.99，今年底前订阅首年 $39.99。

怎么做的：就我一个人，大部分代码是和 AI 一起写的。后端 TypeScript（Hono + SQLite），网页 React，苹果端 SwiftUI。

求拍砖，尤其是第一分钟的体验。中文和中英混说的效果特别想听大家的反馈。

## 关联链接

- https://app.thinkdown.app/?ref=v2ex
- https://apps.apple.com/app/thinkdown/id6823237700

## 导航

- 项目页：[[10-项目/app.thinkdown.app_ab4a707d]]
- 渠道页：[[50-渠道/v2ex]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
