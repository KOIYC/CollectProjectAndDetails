---
type: "project"
title: "zai-org/ZCode"
project_url: "https://zcode.z.ai/"
first_seen: "2026-09-22T14:16:34+08:00"
sources:
  - github_new
tags:
  - 项目
  - github_new
  - TypeScript
  - created:>2026-09-08
lang: "en"
---

# zai-org/ZCode

> [!info] 一句话导读
> <div align="center">

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://zcode.z.ai/>
> 首次收录：2026-09-22T14:16:34+08:00
> 来源渠道：GitHub 新星仓库
> 标签：TypeScript, created:>2026-09-08
> 最新指标：stars=5933 · forks=1703 · open_issues=11

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-09-22T13:05:57+08:00 | GitHub 新星仓库 | stars=5878 · forks=1684 · open_issues=11 | [[20-语料/posts/github_new/2026-09-22/11c0e859fa41d76b_zai-org-ZCode]] |
| 2026-09-22T14:16:34+08:00 | GitHub 新星仓库 | stars=5933 · forks=1703 · open_issues=11 | [[20-语料/posts/github_new/2026-09-22/11c0e859fa41d76b_zai-org-ZCode]] |

## 摘要正文

# ZCode    飞书社群 ·   Discord    简体中文 | English  ZCode 是 AI 编程工作台，提供桌面应用、浏览器界面和终端 Agent。本仓库包含客户端、后端服务、共享 UI，以及 Agent CLI 与运行时源码。  | 入口                 | 用途                                                           | 开发命令                       | | -------------------- | -------------------------------------------------------------- | ------------------------------ | | Desktop              | Electron 桌面应用                                              | `pnpm dev:desktop`             | | Web / ZCode 命令行版 | 终端与浏览器工作台；将 TUI、Web、后端和 Agent 组装为独立运行包 | `pnpm dev:web`                 | | Agent CLI            | 在终端中使用 `zcode`，也为 Desktop 和 Web 提供 Agent 运行时    | `pnpm --filter @zcode/cli dev` |  ## 初始化  准备 Git、Node.js **24.14.0** 和 pnpm **10.33.2**，版本以 [mise.toml](mise.toml) 为准。以下开发和打包命令均在仓库根目录执行。  ```bash pnpm bootstrap ```  `pnpm bootstrap` 安装 workspace 依赖、准备桌面本地运行资源，再执行 `build:bootstrap`。  Agent CLI 与运行时源码位于 [apps/zcode-cli/](apps/zcode-cli/)，作为普通目录随本仓库一起克隆，无需单独拉取或初始化 Git submodule。  根据需要选择其他初始化或构建入口：  | 命令                           | 用途                                                              | | ------------------------------ | -------------------------------------------------------------…
