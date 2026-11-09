---
type: "project"
title: "Show HN: Joggo – a self-hosted GitHub Actions runner for the Windows PC you use"
project_url: "https://github.com/telluric-dev/joggo"
first_seen: "2026-11-09T09:39:29+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_AmirCat
  - story_50413876
  - show_hn
lang: "en"
---

# Show HN: Joggo – a self-hosted GitHub Actions runner for the Windows PC you use

> [!info] 一句话导读
> License: MIT License

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://github.com/telluric-dev/joggo>
> 首次收录：2026-11-09T09:39:29+08:00
> 来源渠道：HN Show HN
> 标签：author_AmirCat, story_50413876, show_hn
> 最新指标：点赞=2 · 评论=1 · engagement_velocity=2

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-11-09T09:39:29+08:00 | HN Show HN | 点赞=2 · 评论=1 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-11-09/343053d768e1d807_Show-HN-Joggo-–-a-self-hosted-GitHub-Actions-runne]] |

## 摘要正文

# telluric-dev/joggo  - Stars: 1 - Forks: 0 - Watchers: 1 - Open issues: 0 - License: MIT License - Default branch: main - Created: 2026-10-28T07:08:46Z  ## Languages  - Dockerfile - PowerShell - Shell  ## Topics  - claude-code-plugin - github-actions - homelab - self-hosted-runner - wsl2  ## Top Contributors  - mindflyerio (6 contributions)  ---  ## README  A self-hosted GitHub Actions runner built to run for weeks on a machine someone is also using.  Not a Kubernetes operator, not an autoscaler, not a fleet. One ordinary Windows PC with 16 GB of RAM and WSL2, taking production builds since June 2026: one runner at first, containerised runner slots since September, two of them from the end of September and three since late October. Through clock drift, power loss, Windows Update reboots, memory exhaustion down to 445 MB available, and a Docker daemon that occasionally stops answering.  The code is maybe half of it. The other half is the comments: most files carry the failure that produced them, what was measured, and what was tried and did not work. That is deliberate. **`docs/memory-pressure.md` is the single most useful page here** even if you never run any of this.  > **If you …
