---
type: "project"
title: "Show HN: I was able to run tiberian sun on cncnet on an M4 MacBook Pro"
project_url: "https://github.com/piyiotisk/cncnet-ts-client-package/blob/master/docs/running-tiberian-sun-on-apple-silicon-macos.md"
first_seen: "2026-09-21T03:16:05+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_piyiotisk
  - story_49112215
  - show_hn
lang: "en"
---

# Show HN: I was able to run tiberian sun on cncnet on an M4 MacBook Pro

> [!info] 一句话导读
> docs/running-tiberian-sun-on-apple-silicon-macos.md

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://github.com/piyiotisk/cncnet-ts-client-package/blob/master/docs/running-tiberian-sun-on-apple-silicon-macos.md>
> 首次收录：2026-09-21T03:16:05+08:00
> 来源渠道：HN Show HN
> 标签：author_piyiotisk, story_49112215, show_hn
> 最新指标：点赞=2 · 评论=0 · engagement_velocity=2

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-09-21T01:31:46+08:00 | HN Show HN | 点赞=2 · 评论=0 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-09-21/f14518634e641c17_Show-HN-I-was-able-to-run-tiberian-sun-on-cncnet-o]] |
| 2026-09-21T03:11:15+08:00 | HN Show HN | 点赞=2 · 评论=0 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-09-21/f14518634e641c17_Show-HN-I-was-able-to-run-tiberian-sun-on-cncnet-o]] |
| 2026-09-21T03:16:05+08:00 | HN Show HN | 点赞=2 · 评论=0 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-09-21/f14518634e641c17_Show-HN-I-was-able-to-run-tiberian-sun-on-cncnet-o]] |

## 摘要正文

# docs/running-tiberian-sun-on-apple-silicon-macos.md  - Branch: master - Repository: piyiotisk/cncnet-ts-client-package  ---  # Running CnCNet Tiberian Sun on Apple Silicon macOS  The ARM64 CnCNet client runs natively on Apple Silicon, while the original 32-bit Windows game runs through Wine.  ## Compatibility status  Tested with:  - Apple M4 - macOS 26.5.2 - .NET 8.0.129 - Wine 11.0  The launcher, CnCNet lobby connection, local skirmish, graphics, mouse, and keyboard were verified. Audio, Intel Macs, a completed live online match, and client updates have not been verified.  ## What you need  - An Apple Silicon Mac - Homebrew - Rosetta 2 - Internet access - Terminal  ## Install  Install Homebrew from brew.sh if it is not already installed. Then open Terminal and run:  ```bash softwareupdate --install-rosetta --agree-to-license brew install dotnet@8 brew install --cask wine-stable mkdir -p ~/Developer cd ~/Developer git clone https://github.com/piyiotisk/cncnet-ts-client-package.git cd cncnet-ts-client-package ./TSLauncherUnix.sh --check ```  The final command performs a preflight check and reports whether the required runtime, Wine setup, Rosetta support, and package files are ava…
