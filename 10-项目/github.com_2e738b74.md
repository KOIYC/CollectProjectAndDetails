---
type: "project"
title: "开源了 Browser Hands：让 Codex/Cursor 也能用上 Claude 官方插件级浏览器操作"
project_url: "https://github.com/214140846/browser-hands"
first_seen: "2026-11-16T10:06:32+08:00"
sources:
  - v2ex
tags:
  - 项目
  - v2ex
  - 17
lang: "zh"
---

# 开源了 Browser Hands：让 Codex/Cursor 也能用上 Claude 官方插件级浏览器操作

> [!info] 一句话导读
> 平时重度用 Claude Code 、Codex 还有 Hermes 、OpenClaw 这类 Agent 干活，经常需要让它们帮忙在网页上填表、点后台、查资料。但浏览器控制这块一直用得很憋屈，折腾了几个周末，干脆自己写了个开源工具叫 **Browser Hands**，今天发出来给大伙试用。

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://github.com/214140846/browser-hands>
> 首次收录：2026-11-16T10:06:32+08:00
> 来源渠道：V2EX
> 标签：17
> 最新指标：回复=0

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-11-16T10:06:32+08:00 | V2EX | 回复=0 | [[20-语料/posts/v2ex/2026-11-16/f0b1896d64790934_开源了-Browser-Hands-让-Codex-Cursor-也能用上-Claude-官方插件级]] |

## 摘要正文

平时重度用 Claude Code 、Codex 还有 Hermes 、OpenClaw 这类 Agent 干活，经常需要让它们帮忙在网页上填表、点后台、查资料。但浏览器控制这块一直用得很憋屈，折腾了几个周末，干脆自己写了个开源工具叫 **Browser Hands**，今天发出来给大伙试用。  **它是什么**  简单说，就是一个 Chrome 扩展 + 一个本地运行的 MCP Server （打包完就一个 450 KB 左右的单文件 JS ）。不需要起云端 VM ，也不用开无头浏览器，直接让任何支持 MCP 的 Agent 接管你平时正在用的 Chrome——点击、输入、读页面、截图、跑 JS 、录 GIF 都行。  **为什么不用现成的方案？**  做之前把市面上的方案基本试了一圈，各有各的难受：  1. **Claude / Codex 官方 Chrome 插件**：体验确实顶，但绑定了单一厂商和订阅。我平时同时用 Codex 、Cursor 、Hermes 、WorkBuddy ，这些 Agent 根本享受不到同等待遇。而且官方插件内置权限限制太多，跑个流程动不动就弹窗让你确认，效率全卡在人工点按钮上。 2. **Playwright / Chrome DevTools MCP 这类工具**：每次新起一个干净的浏览器实例，没有我现成的 Cookie 和登录态；连接经常莫名其妙断开；运行的时候还会抢窗口焦点，动不动触发风控验证。 3. **ego**：试过一阵，资源占用偏高，开几个任务电脑就开始发热风扇狂转。  **Browser Hands 解决了什么问题**  * **多 Agent 并行不打架**：每个 Agent 会话会分配独立的 Chrome 标签组（ Tab Group ），各自只能看到和操作自己组里的标签页，多开并行互不干扰。也支持自定义标签组。 * **多 Google Profile 切换**：像我平时工作号和个人号是分开两个 Chrome Profile 的，Agent 能直接识别每个 Profile 的名称和邮箱，切换很稳。 * **省 Token 且不发热**：页面读取优先走无障碍树（ Accessibility Tree ）和纯文本，必要时才截图；截图直接走 Chrome DevTools Protocol 底层缩放，不在页面里跑 Canvas 渲染。我自己在 Mac 上开很多标签页跑任务，CPU 占用很低，本子基本不怎么烫。 * **内置快速小模型路由（ quick_task ）**：遇到纯机械的点击路径，可以通过 `quick_task` 交给小模型（ JEV ）去跑，单步决策大概 0.2 到 0.5 秒，省主模型 Token 也省时间。同时内置了 `stopBefore` 机制，遇…
