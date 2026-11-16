---
type: "corpus"
item_id: "f0b1896d64790934"
title: "开源了 Browser Hands：让 Codex/Cursor 也能用上 Claude 官方插件级浏览器操作"
source: "v2ex"
source_name: "V2EX"
url: "https://www.v2ex.com/t/1256953"
project_url: "https://github.com/214140846/browser-hands"
author: "Thor88"
published_at: "2026-11-13T14:40:15"
captured_at: "2026-11-16T10:06:32+08:00"
lang: "zh"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-11-16"
pub_day: "2026-11-13"
tags:
  - 语料
  - v2ex
  - 17
metrics: {"replies": 0}
comments_count: 0
comments_total: 0
discovered_via: "v2ex:独立开发"
---

# 开源了 Browser Hands：让 Codex/Cursor 也能用上 Claude 官方插件级浏览器操作

> [!info] 一句话导读
> 平时重度用 Claude Code 、Codex 还有 Hermes 、OpenClaw 这类 Agent 干活，经常需要让它们帮忙在网页上填表、点后台、查资料。但浏览器控制这块一直用得很憋屈，折腾了几个周末，干脆自己写了个开源工具叫 **Browser Hands**，今天发出来给大伙试用。

> [!meta]- 语料信息（点开展开）
> 来源：V2EX（post）
> 原帖：<https://www.v2ex.com/t/1256953>
> 指标：回复=0
> 作者：Thor88　|　发布：2026-11-13T14:40:15
> 项目链接：<https://github.com/214140846/browser-hands>
> 采集：2026-11-16T10:06:32+08:00　|　id：`f0b1896d64790934`

## 正文

平时重度用 Claude Code 、Codex 还有 Hermes 、OpenClaw 这类 Agent 干活，经常需要让它们帮忙在网页上填表、点后台、查资料。但浏览器控制这块一直用得很憋屈，折腾了几个周末，干脆自己写了个开源工具叫 **Browser Hands**，今天发出来给大伙试用。

**它是什么**

简单说，就是一个 Chrome 扩展 + 一个本地运行的 MCP Server （打包完就一个 450 KB 左右的单文件 JS ）。不需要起云端 VM ，也不用开无头浏览器，直接让任何支持 MCP 的 Agent 接管你平时正在用的 Chrome——点击、输入、读页面、截图、跑 JS 、录 GIF 都行。

**为什么不用现成的方案？**

做之前把市面上的方案基本试了一圈，各有各的难受：

1. **Claude / Codex 官方 Chrome 插件**：体验确实顶，但绑定了单一厂商和订阅。我平时同时用 Codex 、Cursor 、Hermes 、WorkBuddy ，这些 Agent 根本享受不到同等待遇。而且官方插件内置权限限制太多，跑个流程动不动就弹窗让你确认，效率全卡在人工点按钮上。
2. **Playwright / Chrome DevTools MCP 这类工具**：每次新起一个干净的浏览器实例，没有我现成的 Cookie 和登录态；连接经常莫名其妙断开；运行的时候还会抢窗口焦点，动不动触发风控验证。
3. **ego**：试过一阵，资源占用偏高，开几个任务电脑就开始发热风扇狂转。

**Browser Hands 解决了什么问题**

* **多 Agent 并行不打架**：每个 Agent 会话会分配独立的 Chrome 标签组（ Tab Group ），各自只能看到和操作自己组里的标签页，多开并行互不干扰。也支持自定义标签组。
* **多 Google Profile 切换**：像我平时工作号和个人号是分开两个 Chrome Profile 的，Agent 能直接识别每个 Profile 的名称和邮箱，切换很稳。
* **省 Token 且不发热**：页面读取优先走无障碍树（ Accessibility Tree ）和纯文本，必要时才截图；截图直接走 Chrome DevTools Protocol 底层缩放，不在页面里跑 Canvas 渲染。我自己在 Mac 上开很多标签页跑任务，CPU 占用很低，本子基本不怎么烫。
* **内置快速小模型路由（ quick_task ）**：遇到纯机械的点击路径，可以通过 `quick_task` 交给小模型（ JEV ）去跑，单步决策大概 0.2 到 0.5 秒，省主模型 Token 也省时间。同时内置了 `stopBefore` 机制，遇到 Submit 、Pay 、Delete 这类关键按钮会硬性卡住等你确认（这个功能需要配 Typesafe 或 OpenRouter 的 Key ，其他所有基础功能零配置开箱即用）。
* **Prompt 零成本迁移**：一共 26 个工具接口，其中 16 个的参数和命名直接对齐了 Claude in Chrome ，原来的提示词基本不用改就能直接用。

**三步安装**

1. 终端跑一行 `curl | sh` 安装脚本（如果本地装了 `claude` CLI ，会自动帮你把 MCP 配置注册进 Claude Code ）。
2. 打开 Chrome 扩展管理页，开启开发者模式，“加载已解压的扩展程序”选中扩展目录。
3. 其他客户端（ Cursor / Codex 等）把本地 MCP 配置贴进去就能连上。

**目前的不足（先打个预防针）**

* 目前只适配了 **macOS**（需要 Node 18+ 和 Chrome ）。
* 业余时间单人维护，刚开源出来，目前还没来得及整理严格的量化跑分数据，上面的体验描述全基于我自己的日常重度使用。

项目采用 MIT 协议开源，现在仓库里才 8 个 Star ，冷启动阶段非常需要大家帮忙踩踩坑。如果觉得思路还行，欢迎去点个 Star 或者提 Issue 吐槽：

GitHub: https://github.com/214140846/browser-hands

## 导航

- 项目页：[[10-项目/github.com_2e738b74]]
- 渠道页：[[50-渠道/v2ex]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
