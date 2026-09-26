---
type: "project"
title: "zai-org/ZCode"
project_url: "https://zcode.z.ai/"
first_seen: "2026-09-26T09:43:40+08:00"
sources:
  - github_new
tags:
  - 项目
  - github_new
  - TypeScript
  - created:>2026-09-12
lang: "en"
---

# zai-org/ZCode

> [!info] 一句话导读
> <div align="center">

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://zcode.z.ai/>
> 首次收录：2026-09-26T09:43:40+08:00
> 来源渠道：GitHub 新星仓库
> 标签：TypeScript, created:>2026-09-12
> 最新指标：stars=6774 · forks=2033 · open_issues=11

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-09-22T13:05:57+08:00 | GitHub 新星仓库 | stars=5878 · forks=1684 · open_issues=11 | [[20-语料/posts/github_new/2026-09-22/11c0e859fa41d76b_zai-org-ZCode]] |
| 2026-09-22T14:16:34+08:00 | GitHub 新星仓库 | stars=5933 · forks=1703 · open_issues=11 | [[20-语料/posts/github_new/2026-09-22/11c0e859fa41d76b_zai-org-ZCode]] |
| 2026-09-24T23:59:53+08:00 | GitHub 新星仓库 | stars=6685 · forks=1994 · open_issues=11 | [[20-语料/posts/github_new/2026-09-22/11c0e859fa41d76b_zai-org-ZCode]] |
| 2026-09-25T13:44:10+08:00 | GitHub 新星仓库 | stars=6726 · forks=2009 · open_issues=11 | [[20-语料/posts/github_new/2026-09-22/11c0e859fa41d76b_zai-org-ZCode]] |
| 2026-09-26T09:43:40+08:00 | GitHub 新星仓库 | stars=6774 · forks=2033 · open_issues=11 | [[20-语料/posts/github_new/2026-09-22/11c0e859fa41d76b_zai-org-ZCode]] |

## 摘要正文

# ZCode    飞书社群 ·   Discord    简体中文 | English  ZCode 是 AI 编程工作台，提供桌面应用、浏览器界面和终端 Agent。本仓库包含客户端、后端服务、共享 UI，以及 Agent CLI 与运行时源码。  ## 更新  - 2026-9-23：更新至 ZCode v3.14.3 版本。  ## 初始化  准备 Git、Node.js **24.14.0** 和 pnpm **10.33.2**，版本以 [mise.toml](mise.toml) 为准。以下开发和打包命令均在仓库根目录执行。  ```bash pnpm bootstrap ```  `pnpm bootstrap` 安装 workspace 依赖、准备桌面本地运行资源，再执行 `build:bootstrap`。  Agent CLI 与运行时源码位于 [apps/zcode-cli/](apps/zcode-cli/)，作为普通目录随本仓库一起克隆，无需单独拉取或初始化 Git submodule。  根据需要选择其他初始化或构建入口：  | 命令                           | 用途                                                              | | ------------------------------ | ----------------------------------------------------------------- | | `pnpm install`                 | 安装依赖                                                          | | `pnpm prepare:desktop-runtime` | 准备桌面运行资源，默认包含远程资源准备                            | | `pnpm prepare:remote-assets`   | 单独准备远程运行资源                                              | | `pnpm bootstrap:with-remote`   | 初始化依赖、本地与远程资源，并串行构建相关包；跳过桌面应用 bundle | | `pnpm build`                   | 递归执行各 workspace 包的构建脚本，包括包内的资源准备步骤         |  默认 `bootstrap` 跳过远程资源准备，适合本地桌面开发。使用远程工作区或验证远程发行资源时，再运行对应准备命令。  ## 开发与运行  ### 桌面版 …
