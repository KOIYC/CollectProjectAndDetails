---
type: "project"
title: "Show HN: Hotline Computer – Rootless Linux desktop container with Nix for agents"
project_url: "https://computer.hotline.dev/"
first_seen: "2026-11-17T11:09:12+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_1broseidon
  - story_50525866
  - show_hn
lang: "en"
---

# Show HN: Hotline Computer – Rootless Linux desktop container with Nix for agents

> [!info] 一句话导读
> A Linux desktop for your coding agent, in a rootless container on your machine.

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://computer.hotline.dev/>
> 首次收录：2026-11-17T11:09:12+08:00
> 来源渠道：HN Show HN
> 标签：author_1broseidon, story_50525866, show_hn
> 最新指标：点赞=2 · 评论=1 · engagement_velocity=2

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-11-17T11:09:12+08:00 | HN Show HN | 点赞=2 · 评论=1 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-11-17/bcb02ddd0a0b8b6f_Show-HN-Hotline-Computer-–-Rootless-Linux-desktop]] |

## 摘要正文

Hotline Computer  v0.11.0 guides  install Hotline Computer A Linux desktop for your coding agent, in a rootless container on your machine. Any MCP client drives it with eight tools. You watch from your browser and take the mouse when it needs you. An illustration open in Pinta. The observer shows a completed Nix preparation job. Reading Wikipedia in Chromium. btop running in a full-height terminal on the left. Exploring San Francisco in OpenStreetMap. Claude serving a site on its own computer, every job it ran logged on the right. 1920 by 1080. Install  Copy $ export TOKEN=$(openssl rand -hex 24)  $ docker run -d --name computer \  --cap-drop=ALL --security-opt no-new-privileges \  --pids-limit 1024 --memory 4g --shm-size 1g \  -p 127.0.0.1:8787:8787 -e HOTLINE_COMPUTER_TOKEN= "$TOKEN" \  -v computer-home:/home/agent \  ghcr.io/1broseidon/hotline-computer:0.11.0 For your agent  Copy Install Hotline Computer for me and connect it to this client. 1. Check that Docker, Podman or Apple container is running. 2. Generate a token with `openssl rand -hex 24` and start  ghcr.io/1broseidon/hotline-computer:0.11.0 with the run command at  https://computer.hotline.dev/#install, published on 12…
