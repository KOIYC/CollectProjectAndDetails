---
type: "project"
title: "GPT-6.2 Astra / Sol 上线实测与避坑：Plus / Codex 菜单里找不到怎么办？4.5x 速度 6x 扣量怎么算？"
project_url: "https://github.com/he20000405-pixel/he20000405-pixel.github.io"
first_seen: "2026-11-19T09:46:37+08:00"
sources:
  - v2ex
tags:
  - 项目
  - v2ex
  - 864
lang: "zh"
---

# GPT-6.2 Astra / Sol 上线实测与避坑：Plus / Codex 菜单里找不到怎么办？4.5x 速度 6x 扣量怎么算？

> [!info] 一句话导读
> V 友们好，OpenAI 在 11 月 17 日发布了 GPT-6.2 Astra 和 GPT-6.2 Sol，首发覆盖 ChatGPT Work、Codex 和 API。这两天社区里很多人在问为什么刷新后菜单里还是没有 6.2，以及 Ultrafast 到底怎么扣额度。

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://github.com/he20000405-pixel/he20000405-pixel.github.io>
> 首次收录：2026-11-19T09:46:37+08:00
> 来源渠道：V2EX
> 标签：864
> 最新指标：回复=0

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-11-19T09:46:37+08:00 | V2EX | 回复=0 | [[20-语料/posts/v2ex/2026-11-19/12fc5f61f7da415c_GPT-6.2-Astra-Sol-上线实测与避坑-Plus-Codex-菜单里找不到怎么办-4.5]] |

## 摘要正文

V 友们好，OpenAI 在 11 月 17 日发布了 GPT-6.2 Astra 和 GPT-6.2 Sol，首发覆盖 ChatGPT Work、Codex 和 API。这两天社区里很多人在问为什么刷新后菜单里还是没有 6.2，以及 Ultrafast 到底怎么扣额度。  结合 OpenAI 官方文档、实际账号界面抓包以及多家第三方机构和开发者的首日实测，我整理了一份硬核避坑笔记，省流结论放最前面：  ## 省流版结论（TL;DR）  - **去哪找模型：** 普通 Chat（聊天）菜单本轮没有加入 GPT-6.2 Astra 与 GPT-6.2 Sol。网页与客户端必须手动切换至 Work（工作） 模式，或者把 Codex 桌面端 / CLI 更新到最新版后切换。  - **日常用哪款：** 写代码、改仓库和多步骤办公首选 GPT-6.2 Sol（Work 模式默认启用，API 单价只有 GPT-6.2 Astra 的 1/4，多项基准紧咬甚至反超旗舰）；超长上下文、3D/CAD 交互、科研或高难度代码审查再切 GPT-6.2 Astra。  - **计费大坑预警：** Plus、Pro 100、Business 没有 Ultrafast；Pro 200（仅限 Codex 中的 GPT-6.2 Sol）和 Pro 500 开启 Ultrafast 时，生成速度上限为 Standard 的 4.5x，但套餐额度按 6x 扣除。API 涉及工具调用必须走 Responses API。  ---  ## 一、为什么刷新后菜单里找不到 GPT-6.2？（四步排查）  绝大多数情况不是账号没推送到，而是入口隔离或前端状态缓存导致的：  ### 1. 普通 Chat 不开放，必须切到 Work 模式  - OpenAI 在更新日志里明确写了本轮不将 GPT-6.2 加入普通 Chat 菜单。  - **同一已登录 Pro 账号 Chrome 网页端实测：** 普通「聊天」里展开菜单只能看到 GPT-6 和 GPT-5.6 Sol；切到「工作（Work）」后，收起状态的按钮仍显示旧型号 GPT-6.1 Sol，但点开下拉列表后 GPT-6.2 Astra 和 GPT-6.2 Sol 已经都在里面了。  - 别光看折叠按钮文字就以为没推送；如果界面显示的是 Power 滑杆，点旁边的 Advanced 就能选具体模型和推理强度。  ### 2. 更新 Codex 桌面端与 CLI  - 桌面端在输入框附近切模型，缺项的话先点 Menu -> Check for Updates 更新并重启；CLI 端升级到最新版后直接用 /model 查看切换。  ### 3. 核对套餐与管理员开关  - Plus、Pro、…
