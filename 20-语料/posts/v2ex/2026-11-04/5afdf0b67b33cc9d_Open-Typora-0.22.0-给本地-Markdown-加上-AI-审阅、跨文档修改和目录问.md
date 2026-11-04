---
type: "corpus"
item_id: "5afdf0b67b33cc9d"
title: "Open Typora 0.22.0：给本地 Markdown 加上 AI 审阅、跨文档修改和目录问答"
source: "v2ex"
source_name: "V2EX"
url: "https://www.v2ex.com/t/1254264"
project_url: "https://github.com/AniChikage/open-typora"
author: "anichikage"
published_at: "2026-11-03T14:31:54"
captured_at: "2026-11-04T09:58:05+08:00"
lang: "zh"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-11-04"
pub_day: "2026-11-03"
tags:
  - 语料
  - v2ex
  - 1135
metrics: {"replies": 0}
comments_count: 0
comments_total: 0
discovered_via: "v2ex:独立开发"
---

# Open Typora 0.22.0：给本地 Markdown 加上 AI 审阅、跨文档修改和目录问答

> [!info] 一句话导读
> 我是 Open Typora 的开发者。10 月在这里分享过这个开源 Markdown 编辑器，最近把 AI 相关的工作流补到了 0.22.0 ，来更新一下进展。

> [!meta]- 语料信息（点开展开）
> 来源：V2EX（post）
> 原帖：<https://www.v2ex.com/t/1254264>
> 指标：回复=0
> 作者：anichikage　|　发布：2026-11-03T14:31:54
> 项目链接：<https://github.com/AniChikage/open-typora>
> 采集：2026-11-04T09:58:05+08:00　|　id：`5afdf0b67b33cc9d`

## 正文

我是 Open Typora 的开发者。10 月在这里分享过这个开源 Markdown 编辑器，最近把 AI 相关的工作流补到了 0.22.0 ，来更新一下进展。

GitHub （源码、使用说明和安装包）： https://github.com/AniChikage/open-typora

## 这次主要增加了什么

- **选区改写，逐处审阅。** 选中一段文字，说清要求，先看原文和建议的差异；决定保留哪些改动，再应用到文档，也可以一次撤销。
- **跨文档修改。** 明确选择最多 4 份文档，先生成修改计划，再逐文件、逐处审阅。数字、常见日期、链接和代码默认受保护，也可以锁定术语；检测到受保护内容变化时会阻止应用，结果仍需自己核对。
- **参考文件和目录问答。** 改写时用 `@文件` 补充上下文。目录问答先在本机检索，勾选要发送的片段，再交给模型回答，并核对引用的原文；答案可以带 Markdown 脚注插入文档。
- **本地版本历史与整批恢复。** AI 修改前保留恢复点，跨文档批次记录可以跨重启保留；如果后续内容已经变了，会阻止整批恢复，避免覆盖新的修改。历史保留有上限，重要文件仍应另外备份。

平时照常写普通 `.md` 文件，不用把笔记搬进某个云端知识库。即时渲染、源码切换、分屏、表格、HTML/PDF 导出也都在。

## 两张桌面实拍

写作界面，使用专门准备的公开示例文档：

![Open Typora 0.22.0 桌面写作界面](  )

跨文档修改入口：选中两份公开草稿，并设置数字、链接、代码和术语的保留约束，准备生成修改计划：

![Open Typora 跨文档 AI 修改与保留约束](  )

## 模型和平台

AI 是可选功能，需要自己配置 OpenAI 兼容 API 、OpenRouter 、LM Studio 或 Ollama 。选中的文字、要求和相关资料会发给所选模型服务；是否离线、费用和数据保留取决于你的配置和服务商。网页试玩只展示基础编辑，AI 功能请用桌面版。

目前提供 macOS 14+ Apple Silicon 、Windows 10/11 x64 和 Linux x64 安装包，支持中文和英文界面。项目采用 MIT 许可证，独立实现，与 Typora 官方无关联，功能和兼容性还在完善。

如果这个方向对你有用，欢迎试用、在 GitHub 提问题或给个 Star ，也欢迎分享给写 Markdown 的朋友。尤其想听听：你会用跨文档修改统一哪些材料，哪些内容是绝对不能被 AI 改掉的？

上次的帖子： https://www.v2ex.com/t/1249106

文案由 AI 协助整理；功能信息已按当前 README 、AI 文档和 0.22.0 Release 核对。两张图均为本机 0.22.0 桌面界面，使用公开示例。

## 关联链接

- https://www.v2ex.com/t/1249106

## 导航

- 项目页：[[10-项目/github.com_29e6a4cf]]
- 渠道页：[[50-渠道/v2ex]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
