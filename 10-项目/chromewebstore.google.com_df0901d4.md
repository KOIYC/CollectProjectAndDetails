---
type: "project"
title: "[年度观察] 梳理了近两年 V2EX 独立开发者做的 20+ 款浏览器扩展，顺便聊聊插件出海与冷启动"
project_url: "https://chromewebstore.google.com/detail/clneekebmllhkokbpggpaaiddhcbiknh"
first_seen: "2026-11-21T14:55:12+08:00"
sources:
  - v2ex
tags:
  - 项目
  - v2ex
  - 17
lang: "zh"
---

# [年度观察] 梳理了近两年 V2EX 独立开发者做的 20+ 款浏览器扩展，顺便聊聊插件出海与冷启动

> [!info] 一句话导读
> 最近自己在做浏览器扩展的独立开发，顺手翻了翻过去两年（2025–2026）V2EX「分享创造」和「Chrome」节点下大家发布的扩展作品。

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://chromewebstore.google.com/detail/clneekebmllhkokbpggpaaiddhcbiknh>
> 首次收录：2026-11-21T14:55:12+08:00
> 来源渠道：V2EX
> 标签：17
> 最新指标：回复=0

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-11-21T14:55:12+08:00 | V2EX | 回复=0 | [[20-语料/posts/v2ex/2026-11-21/677bd903d3a50b3d_年度观察-梳理了近两年-V2EX-独立开发者做的-20+-款浏览器扩展,顺便聊聊插件出海与冷启动]] |

## 摘要正文

最近自己在做浏览器扩展的独立开发，顺手翻了翻过去两年（2025–2026）V2EX「分享创造」和「Chrome」节点下大家发布的扩展作品。  整体看下来很有意思：早期大家多是在做“改个网页样式、去个广告”的小脚本；到了 2025 下半年至 2026 年，随着 Manifest V3 全面落地以及本地 AI Agent（Claude Code、Codex、MCP 等）的爆发，独立开发者的浏览器扩展开始明显往**“AI Agent 浏览器控制”**和**“垂直场景工作流提效”**集中。  我花了点时间把近两年站内有代表性、且仍在维护的 20+ 款独立开发扩展按赛道整理了一份清单，方便大家交流和参考：  ### 1. AI Agent 浏览器控制与自动化（2026 年最热新赛道） 随着本地 CLI Agent 的普及，今年下半年集中涌现了一批让 Agent 直接复用日常 Chrome 登录态的扩展： * **Xtaff Browser**：开放 MCP 接口的浏览器操作插件，支持网站 Playbook 录制与会话暂存，让 Agent 复用日常 Chrome 登录态。 * **BeatBrowser**：MIT 开源浏览器控制插件 + 本地 Node 桥接，支持 Codex、Claude Code、Cursor 共用已登录的 Chrome，独立窗口运行并支持人工随时接管。 * **WebCLI**：解包不到 300 KB 的极简执行端，提供 25 个基础工具（读写、点击、截图等），将浏览器变成外部 AI Agent 的执行终端。  ### 2. 社交媒体与内容运营工具 * **波波小红书助手（小红书原图下载扩展）**：我自己最近开源并上架的一款轻量工具，支持无水印小红书原图、LivePhoto 与高清视频批量提取下载，纯净无广告，支持 Chrome 与 Edge。Chrome 商店：https://chromewebstore.google.com/detail/hpdomiahmefpopmpgcihooocjolkggpl * **波波抖音内容运营助手**：针对抖音网页版的自动化运营与获客工具，支持推荐流模拟挂机、多关键词搜索筛选、评论区截流及 AI 神评。Chrome 商店：https://chromewebstore.google.com/detail/clneekebmllhkokbpggpaaiddhcbiknh ｜ Edge 商店：https://microsoftedge.microsoft.com/addons/detail/jlncifnebnelgnhpfjaiggnolkldcngc * **PostKeeper**：纯本地运行的 X (Twitter) 帖子与书签收藏离线备份扩展，防原帖删除丢失。 * **全…
