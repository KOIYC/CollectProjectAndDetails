---
type: "project"
title: "把 Tripo Studio 连接到 Codex 的插件"
project_url: "https://github.com/GrinZero/tripo-studio-plugin"
first_seen: "2026-10-11T09:47:34+08:00"
sources:
  - v2ex
tags:
  - 项目
  - v2ex
  - 17
lang: "zh"
---

# 把 Tripo Studio 连接到 Codex 的插件

> [!info] 一句话导读
> ![Tripo Studio for Codex Banner](  )

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://github.com/GrinZero/tripo-studio-plugin>
> 首次收录：2026-10-11T09:47:34+08:00
> 来源渠道：V2EX
> 标签：17
> 最新指标：回复=0

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-10-11T09:47:34+08:00 | V2EX | 回复=0 | [[20-语料/posts/v2ex/2026-10-11/aba5b7e328d1c10c_把-Tripo-Studio-连接到-Codex-的插件]] |

## 摘要正文

![Tripo Studio for Codex Banner](  )  为什么是 **Link your Tripo Studio**，而不是 **Tripo API**？  最近在用 Codex 写自己的 3D / 游戏项目时，我发现现有的官方工具只支持 Tripo API：  1. **明明开了网页端会员，调 API 还得再交一份钱**：很多创作者和独立开发者手里本来就有 **Tripo Studio 网页端会员**（每个月有大量套餐积分），但官方 API Key 的计费池是完全独立的——想在 Agent 里自动化生成模型，还得额外掏钱充值 API Credits 。 2. **我们需要的是整个「 Studio 工作流」，而不是裸调一个无状态接口**：做 3D 资产不是发个 Prompt 拿回一个 URL 就完事了。以往我们要在「浏览器输入 Prompt ➔ 手动下载 GLB ➔ 拖进 Blender 查面数和流形 ➔ 姿势不对切回网页重刷 ➔ 绑骨骼调动作 ➔ 导出 FBX 塞进工程目录」之间反复横跳。  所以我做了一个开源的 Codex 插件 —— **[Tripo Studio for Codex]( https://github.com/GrinZero/tripo-studio-plugin)**（ MIT License ），刚刚发布了最新的 **v0.3.4** 版本。  它不走额外的 API Key 计费中转，而是**直接把你的 Tripo Studio 网页端账号、完整创作管线、可视化工作台以及本地 Blender 后处理引擎，原封不动地连进了 Codex**。  ---  ### 💡 连入 Tripo Studio 意味着什么？  #### 1. BYO Studio Account：直接复用网页端会员与积分，零 API 溢价 插件直接复用本机的 Tripo Studio 网页登录会话，无需申请和购买 API Key 。你在网页端订购的会员积分，现在可以直接在 Codex 对话框里调用 Studio 全套最新算力： - **High Detail (H2.5 / H3.0 / H3.1)**：高精度几何建模 + 2K/4K/8K PBR 材质与局部重绘 - **Smart Mesh P2**：严格控制在 500–25,000 面的规整四边面网格，支持单次生成多个面数预算变体 - **多视角对齐建模**：支持正/左/背/右四视图一致建模 - **Rig V3 绑骨 & AI Motion**：自动适配 Mixamo / UE Mannequin / Unity Humanoid 标准骨架，支持文本生成连贯动作并重定向  #### 2. 不止是对话：68 个 MCP 工具 + 内嵌 St…
