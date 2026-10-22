---
type: "project"
title: "Gathin23/cleanyourtv"
project_url: "https://cleanyour.tv/"
first_seen: "2026-10-22T09:47:43+08:00"
sources:
  - github_new
tags:
  - 项目
  - github_new
  - Java
  - created:>2026-10-08
lang: "en"
---

# Gathin23/cleanyourtv

> [!info] 一句话导读
> <a href="https://cleanyour.tv"><img src="https://raw.githubusercontent.com/Gathin23/cleanyourtv/main/docs/banner.png" alt="CleanYourTV. Your TV, minus the ads. …

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://cleanyour.tv/>
> 首次收录：2026-10-22T09:47:43+08:00
> 来源渠道：GitHub 新星仓库
> 标签：Java, created:>2026-10-08
> 最新指标：stars=19453 · forks=2100 · open_issues=98

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-10-22T09:47:43+08:00 | GitHub 新星仓库 | stars=19453 · forks=2100 · open_issues=98 | [[20-语料/posts/github_new/2026-10-22/ab0e470b36e49b22_Gathin23-cleanyourtv]] |

## 摘要正文

**The viral tweet:** [x.com/gathint/status/2111379569030939102](https://x.com/gathint/status/2111379569030939102)  On 17 October 2026 I posted a before and after of my parents' TV, cleaned up by Claude Code over Wi-Fi. It reached 7.4M views, people started doing the same to their own TVs, and their replies turned into the lists here: 170+ TV models from 200+ contributors in four days. The repo was called tv-vibehack until the 19th; old links work.  ## How it works  Android TVs have the same debug bridge as Android phones. Switch on USB debugging in the TV's developer options, allow your computer once, and the rest is standard Android tooling:  | Step | What happens | |---|---| | **Back&nbsp;up** | The list of installed packages and settings. | | **Disable** | The manufacturer's telemetry, ad services, content rows and preloaded junk, with `pm disable-user`. Nothing is uninstalled, so a restore script can undo every step. | | **Install** | A small native launcher, made the default home screen. |  **No root, no cable, nothing uninstalled, and a one-line restore if you change your mind.**  The bloat differs by brand, so the prompt has your coding assistant discover it on your TV and a…
