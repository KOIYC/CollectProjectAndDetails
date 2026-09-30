---
type: "corpus"
item_id: "337d6d1c5199996f"
title: "开源了一个会自己进化的 App：在对话里说一句，你 Mac 上的 Claude Code 就改代码并上线"
source: "v2ex"
source_name: "V2EX"
url: "https://www.v2ex.com/t/1245483"
project_url: "https://github.com/TimeLovercc/mojito"
author: "TimeLover"
published_at: "2026-09-29T03:39:16"
captured_at: "2026-09-30T18:52:39+08:00"
lang: "zh"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-30"
pub_day: "2026-09-29"
tags:
  - 语料
  - v2ex
  - 17
metrics: {"replies": 0}
comments_count: 0
comments_total: 0
discovered_via: "v2ex:独立开发"
---

# 开源了一个会自己进化的 App：在对话里说一句，你 Mac 上的 Claude Code 就改代码并上线

> [!info] 一句话导读
> 个人 AI 时代，现在这种 App 的形态还适应未来吗？像 Meta Muse 这样的云端 agent 就是终点吗？我们的答案是「会进化的 App 」。

> [!meta]- 语料信息（点开展开）
> 来源：V2EX（post）
> 原帖：<https://www.v2ex.com/t/1245483>
> 指标：回复=0
> 作者：TimeLover　|　发布：2026-09-29T03:39:16
> 项目链接：<https://github.com/TimeLovercc/mojito>
> 采集：2026-09-30T18:52:39+08:00　|　id：`337d6d1c5199996f`

## 正文

个人 AI 时代，现在这种 App 的形态还适应未来吗？像 Meta Muse 这样的云端 agent 就是终点吗？我们的答案是「会进化的 App 」。

**Mojito**（ MIT 开源）：在对话里说一句「把下一步放最上面，加粗」，跑在你自己 Mac 上的 Claude Code 就去改代码、构建、发布到手机 / Mac / 网页版，推送告诉你改了什么。

![](  )

三个原则：
- **薄代码**：服务器上的 hub （ FastAPI + SQLite ）只存数据、提供 API 、发推送，功能不写死
- **agent 掌握上下文**：Claude Code 跑在你自己的 Mac 上，懂你的日程、邮件、文件，也懂这个 App 自己的代码和设计文档
- **和你一起进化**：小改动直接上线，大改动先等你点同意（目前由维护会话按文档判断，代码里还没强制）

一天里长出来的东西（真实记录）：
- 「想要个订阅页」→ 订阅页 + 每个来源一键运行
- 「 iPhone 也要能用」→ 当晚就有了能加到桌面的网页版和 Web Push
- 「通知收到两遍」→ 自己查到原因（安卓通知库自己又显示了一份）并修好
- 「桌面版像拉长的手机」→ 重做成 Mac 原生风格（新版还在开发）
- 「加个英文界面」→ 中英切换

技术栈：Expo （ Android + PWA ）、Tauri （ Mac ）、FastAPI + SQLite 、Claude Code 。

实话实说：还是 alpha ，要自己部署（一台服务器或常开的电脑）；依赖 Claude Code ；数据在你自己的机器上，但 agent 读到的内容会发给你选的模型提供方。

GitHub： https://github.com/TimeLovercc/mojito

欢迎拍砖。独立项目，与 Meta 无关。

## 导航

- 项目页：[[10-项目/github.com_72ef040c]]
- 渠道页：[[50-渠道/v2ex]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
