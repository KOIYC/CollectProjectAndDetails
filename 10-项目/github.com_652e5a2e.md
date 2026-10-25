---
type: "project"
title: "Show HN: EdgePad – tool for configuring edge touchpad gestures on Linux laptops"
project_url: "https://github.com/assembledev/edgepad"
first_seen: "2026-10-25T23:24:35+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_dev-e
  - story_50230557
  - show_hn
lang: "en"
---

# Show HN: EdgePad – tool for configuring edge touchpad gestures on Linux laptops

> [!info] 一句话导读
> Touchpad edge gestures for Linux/Wayland.

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://github.com/assembledev/edgepad>
> 首次收录：2026-10-25T23:24:35+08:00
> 来源渠道：HN Show HN
> 标签：author_dev-e, story_50230557, show_hn
> 最新指标：点赞=6 · 评论=0 · engagement_velocity=6

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-10-25T23:24:35+08:00 | HN Show HN | 点赞=6 · 评论=0 · engagement_velocity=6 | [[20-语料/posts/hn_show/2026-10-25/f5a4d1a14ae1e623_Show-HN-EdgePad-–-tool-for-configuring-edge-touchp]] |

## 摘要正文

# assembledev/edgepad  Touchpad edge gestures for Linux/Wayland.  - Stars: 13 - Forks: 0 - Watchers: 13 - Open issues: 0 - License: Apache License 2.0 - Default branch: main - Created: 2026-07-02T16:20:09Z  ## Languages  - Nix - Rust - Shell  ## Topics  - gestures - linux - nixos - touchpad - wayland  ## Top Contributors  - assembledev (107 contributions)  ---  ## README  # edgepad  Touchpad edge gestures for Linux/Wayland.  `edgepad` turns touchpad edges into command zones while keeping normal pointer movement on the center of the pad. Swipe from an edge to run commands such as changing workspaces, opening a launcher, or sending desktop notifications.  The hard part is input correctness: Type-B multitouch slots, mixed edge/center contacts, `SYN_DROPPED` recovery, and virtual touch cleanup are covered by replay tests before they touch real hardware.  ## Features  - Edge gestures on the left, right, top, and bottom touchpad zones. - Continuous edge sliders for stepwise controls such as volume and brightness. - Normal touchpad passthrough for unclaimed center contacts. - Long-running user-session daemon with TOML config. - Transactional config reload without releasing the touchpad gr…
