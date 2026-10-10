---
type: "corpus"
item_id: "b90df2722c6fa5ea"
title: "国庆没怎么休息，折腾出了小红书 30 天 1206 万曝光，顺手开源了一套 AI 视频 Skills"
source: "v2ex"
source_name: "V2EX"
url: "https://www.v2ex.com/t/1246951"
project_url: "https://github.com/Ucmp0001/video-production-skills"
author: "ZhouAI"
published_at: "2026-10-08T02:30:55"
captured_at: "2026-10-10T10:02:47+08:00"
lang: "zh"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-10-10"
pub_day: "2026-10-08"
tags:
  - 语料
  - v2ex
  - 17
metrics: {"replies": 0}
comments_count: 0
comments_total: 0
discovered_via: "v2ex:独立开发"
---

# 国庆没怎么休息，折腾出了小红书 30 天 1206 万曝光，顺手开源了一套 AI 视频 Skills

> [!info] 一句话导读
> 国庆几天基本没怎么休息，一直在折腾 Codex 、Claude Code 和 AI 视频制作。

> [!meta]- 语料信息（点开展开）
> 来源：V2EX（post）
> 原帖：<https://www.v2ex.com/t/1246951>
> 指标：回复=0
> 作者：ZhouAI　|　发布：2026-10-08T02:30:55
> 项目链接：<https://github.com/Ucmp0001/video-production-skills>
> 采集：2026-10-10T10:02:47+08:00　|　id：`b90df2722c6fa5ea`

## 正文

国庆几天基本没怎么休息，一直在折腾 Codex 、Claude Code 和 AI 视频制作。

没想到折腾出了点意外收获：

小红书近 30 天曝光 1206 万，播放 275 万，国庆这几天涨粉大概 2000 。

数据截图放下面，省得被说吹牛。


![小红书数据截图](图片直链)

先说结论：

AI 确实把个人做内容的门槛拉低了。但真折腾下来我发现，最麻烦的从来不是让 AI 写稿，而是怎么让它稳定地把一条视频做完。

之前踩过的坑：

稿子看着很完整，一核查事实就露馅
资料、脚本、分镜、配音、字幕经常对不上
改两句话，后面的字幕、封面、镜头全得重来
生成了一堆文件，最后自己都分不清哪个是最终版

所以国庆期间我干脆把自己的视频流程拆成了一套 Skills ，目前开源了 11 个：

资料和素材索引
基于证据的故事脚本
视频分镜与素材规划
机制解释动画
AI 概念镜头规划
配音与字幕同步
封面设计及独立审查
成片质检和发布文案

支持 Codex 、Claude Code ，以及其他兼容 SKILL.md 的 Agent 。

它不是"输入一句话，自动出大片"那种项目，更像是一套给 AI Agent 用的视频制作 SOP：每个 Skill 只干一件事，并留下对应产物，下一步可以直接接着做，出了问题也只需要局部重做。

仓库地址（ MIT 协议，免费开源，可单装也可组合用）：
https://github.com/Ucmp0001/video-production-skills

目前还在持续完善，欢迎拍砖、提 Issue 。尤其想听听大家在多 Agent 协作和视频工作流上有没有更好的思路。

说点题外话

最近也在认真折腾 X ，发现技术圈有个挺有意思的现象：很多人能花三天写出一个不错的开源项目，却不愿意花三分钟介绍它。

我以前就是这样。

现在开始把开发过程、AI 实验和踩坑经验发到 X 上，也想顺便认识更多做独立开发、AI Agent 和开源的朋友。

我的 X： https://x.com/eazymoney888

V 站有同样在经营 X 的朋友吗？欢迎在评论区留下你的 GitHub 、X 或者最近在做的项目，有意思的我都会去看看。

最后想聊一个问题：

当 AI 把内容制作成本压得越来越低，未来真正值钱的会是什么？是会写代码，是会做内容，还是知道什么东西值得做？

## 关联链接

- https://x.com/eazymoney888

## 导航

- 项目页：[[10-项目/github.com_dd82f742]]
- 渠道页：[[50-渠道/v2ex]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
