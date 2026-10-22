---
type: "corpus"
item_id: "8547b24df3eb8700"
title: "[开源] AI Coding 时代，也许真不用再打开 VS Code、IDEA 了"
source: "v2ex"
source_name: "V2EX"
url: "https://www.v2ex.com/t/1250064"
project_url: "https://github.com/murongg/Tervia"
author: "murongxdb"
published_at: "2026-10-19T08:31:17"
captured_at: "2026-10-22T09:49:30+08:00"
lang: "zh"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-10-22"
pub_day: "2026-10-19"
tags:
  - 语料
  - v2ex
  - 17
metrics: {"replies": 0}
comments_count: 0
comments_total: 0
discovered_via: "v2ex:独立开发"
---

# [开源] AI Coding 时代，也许真不用再打开 VS Code、IDEA 了

> [!info] 一句话导读
> 重度使用 AI Coding 一年多，现在写代码基本都在终端里完成了。VS Code 对我来说越来越没用了，打开它几乎就为了 review 代码、看一下 Git diff 。

> [!meta]- 语料信息（点开展开）
> 来源：V2EX（post）
> 原帖：<https://www.v2ex.com/t/1250064>
> 指标：回复=0
> 作者：murongxdb　|　发布：2026-10-19T08:31:17
> 项目链接：<https://github.com/murongg/Tervia>
> 采集：2026-10-22T09:49:30+08:00　|　id：`8547b24df3eb8700`

## 正文

重度使用 AI Coding 一年多，现在写代码基本都在终端里完成了。VS Code 对我来说越来越没用了，打开它几乎就为了 review 代码、看一下 Git diff 。  

为了这点需求，还得装着一个完整的编辑器，总觉得有点浪费。想着省点硬盘空间和内存，干脆用 GPUI 给自己做了个工具，叫 Tervia 。

想法很简单，把终端、Git 和简单的文件编辑放在一起。平时在终端里跑 Claude Code 、Codex ，写完直接看改动，偶尔手动改几行，再提交，基本就够我用了。    

目前已经支持这些功能：
- 终端：多标签、分屏、输出搜索，继续用自己熟悉的 Shell ，直接跑 Claude Code 、Codex 。
- Git：看 diff 、按文件或部分改动暂存、提交，也能查看提交历史、切换分支和处理冲突。
- 文件：浏览、搜索和简单编辑，支持语法高亮、Markdown 和图片预览。复制代码时可以一起带上文件路径和行号，方便丢给 AI 。
- 多项目和 worktree：各个项目保留自己的终端、文件和草稿，也能用 worktree 同时处理不同任务。
- Agent 状态和通知：接入后能看到 AI 正在处理、等授权还是等输入，在后台完成本轮响应时也能收到桌面通知。
- 项目任务：识别 package.json 脚本、Cargo 、Makefile 等任务，直接在独立终端里运行，保留输出和执行结果。
另外也做了深浅主题、字体字号设置和中文界面这些日常会用到的东西。

**开源地址**： https://github.com/murongg/Tervia  
**支持 macOS 、windows 、linux**  
软件安装包不到 20MB ，我平时同时运行四五个项目，内存占用 100+MB ，VSCode 内存占用要 3GB 以上。
也欢迎各位根据自己的实际开发习惯，分享一些功能需求，我会参考大家的需求，再继续完善一些常见功能。


截图：

![终端](  )
![git](  )
![文件](  )

## 导航

- 项目页：[[10-项目/github.com_a1fe3f14]]
- 渠道页：[[50-渠道/v2ex]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
