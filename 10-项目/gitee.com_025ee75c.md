---
type: "project"
title: "QuotaPanel：基于 Wails 的 AI 订阅额度管理工具"
project_url: "https://gitee.com/open-tecmz/quotapanel"
first_seen: "2026-10-22T09:49:30+08:00"
sources:
  - v2ex
tags:
  - 项目
  - v2ex
  - 17
lang: "zh"
---

# QuotaPanel：基于 Wails 的 AI 订阅额度管理工具

> [!info] 一句话导读
> 在 AI 开发日益普及的今天，开发者需要同时管理 Claude 、ChatGPT 、GitHub Copilot 、Kimi 等多个平台的订阅与 API 额度。这些额度信息分散在各个控制台，难以快速掌握整体使用情况。

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://gitee.com/open-tecmz/quotapanel>
> 首次收录：2026-10-22T09:49:30+08:00
> 来源渠道：V2EX
> 标签：17
> 最新指标：回复=0

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-10-22T09:49:30+08:00 | V2EX | 回复=0 | [[20-语料/posts/v2ex/2026-10-22/db75f5c9da297f4c_QuotaPanel-基于-Wails-的-AI-订阅额度管理工具]] |

## 摘要正文

# 引言  在 AI 开发日益普及的今天，开发者需要同时管理 Claude 、ChatGPT 、GitHub Copilot 、Kimi 等多个平台的订阅与 API 额度。这些额度信息分散在各个控制台，难以快速掌握整体使用情况。  **QuotaPanel** 是一款开源的桌面端 AI 额度管理工具，基于 **Go + Wails + Vue3** 技术栈开发，支持 16 种 AI 订阅与 API 额度来源，本地优先保护隐私，跨平台支持 macOS/Windows/Linux 。  ![](  ?t=202609261508)  ## 核心特性  ### 本地优先设计  QuotaPanel 采用**本地优先**架构，所有账号密钥与浏览器会话数据均保存在本机（默认 `~/.quotapanel/`），不会上传到云端。数据目录支持通过 `QUOTAPANEL_DATA_ROOT` 环境变量自定义位置。  ### 多源额度聚合  工具支持 16 种 AI 订阅与 API 额度来源，分为两大类：  **浏览器登录类**： - Claude 订阅（ 5 小时及每周额度） - ChatGPT/Codex （订阅使用窗口） - Cursor （当前周期用量） - Xiaomi MiMo Token Plan （套餐积分与账户余额）  **API Key 类**： - GitHub Copilot （ Premium 、聊天与补全额度） - Z.ai Coding Plan 、Kimi Coding Plan 、MiniMax Token Plan - Devin/Windsurf 、Grok CLI 、OpenCode - Command Goat 、DeepSeek API 、Kimi API - OpenRouter 、OpenAI API  ### 额度可视化  通过进度条、余额明细、账期/重置时间等可视化元素，系统提供正常、即将用尽、超限三档状态色，超出阈值时会主动提示。  ![](  ?t=202609261508)  ## 技术架构  ### 技术栈  - **Go 1.24+**：后端核心逻辑与额度查询服务 - **Wails v2**：跨平台桌面应用框架 - **Vue3 + TypeScript**：前端界面开发 - **AntDesign Vue**：UI 组件库 - **TailwindCSS**：样式框架 - **SQLite**：本地数据存储  ### 项目结构  ``` quotapanel/ ├── main.go              # Wails 应用配置与入口 ├── app*.go              # App 暴…
