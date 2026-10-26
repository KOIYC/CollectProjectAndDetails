---
type: "project"
title: "seedds/nxnative"
project_url: "https://github.com/seedds/nxnative"
first_seen: "2026-10-26T09:44:46+08:00"
sources:
  - github_new
tags:
  - 项目
  - github_new
  - Objective-C
  - created:>2026-10-12
lang: "en"
---

# seedds/nxnative

> [!info] 一句话导读
> Play your own Nintendo Switch games natively on iPhone and iPad. Bring your game (its NSP files) and your `prod.keys`; one script turns them into an IPA that yo…

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://github.com/seedds/nxnative>
> 首次收录：2026-10-26T09:44:46+08:00
> 来源渠道：GitHub 新星仓库
> 标签：Objective-C, created:>2026-10-12
> 最新指标：stars=4343 · forks=770 · open_issues=92

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-10-26T09:44:46+08:00 | GitHub 新星仓库 | stars=4343 · forks=770 · open_issues=92 | [[20-语料/posts/github_new/2026-10-26/9e1ccc955df4e077_seedds-nxnative]] |

## 摘要正文

# nxnative  Play your own Nintendo Switch games natively on iPhone and iPad. Bring your game (its NSP files) and your `prod.keys`; one script turns them into an IPA that you sideload.  It is not an emulator: the game's own code runs directly on the Apple chip, with Switch graphics rebuilt on Metal. Nothing from any game is in this repository, and the project is not affiliated with Nintendo or any game publisher.  ## Acknowledgements  This project is built on other people's work:  - **[d2r-mobile](https://github.com/jhaizhou-ops/d2r-mobile)** (MIT) developed this native-execution approach, for Diablo II: Resurrected. nxnative started as a copy of its generic parts: the NSO rewriter, the host that stands in for Horizon, the NVN-on-Metal layer and the iOS app shell. Fixes go both ways. - **Ryujinx** (MIT): its shader translator (`Ryujinx.Graphics.Shader`, `Ryujinx.Common` and `Spv.Generator` 1.3.2, in `dm/third_party/ryujinx` with a few fixes listed in [its README](dm/third_party/ryujinx/README.md)) turns the games' Maxwell shaders into SPIR-V. Its emulation of the kernel and system services is also a reference when the host's behaviour is in doubt. - **[Atmosphère](https://github.com…
