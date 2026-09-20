---
type: "project"
title: "Show HN: GLM-5.3 744B at 4 tok/s on a MacBook Pro, experts streamed from 4 SSDs"
project_url: "https://github.com/argonautlabsai/argodrive"
first_seen: "2026-09-20T09:36:54+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_Argonautlabs
  - story_49738954
  - show_hn
lang: "en"
---

# Show HN: GLM-5.3 744B at 4 tok/s on a MacBook Pro, experts streamed from 4 SSDs

> [!info] 一句话导读
> argonautlabsai/argodrive

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://github.com/argonautlabsai/argodrive>
> 首次收录：2026-09-20T09:36:54+08:00
> 来源渠道：HN Show HN
> 标签：author_Argonautlabs, story_49738954, show_hn
> 最新指标：点赞=2 · 评论=0 · engagement_velocity=2

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-09-20T09:23:24+08:00 | HN Show HN | 点赞=2 · 评论=0 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-09-20/95ab375d815b5aec_Show-HN-GLM-5.3-744B-at-4-tok-s-on-a-MacBook-Pro,]] |
| 2026-09-20T09:36:54+08:00 | HN Show HN | 点赞=2 · 评论=0 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-09-20/95ab375d815b5aec_Show-HN-GLM-5.3-744B-at-4-tok-s-on-a-MacBook-Pro,]] |

## 摘要正文

# argonautlabsai/argodrive  Layout, balancer and instruments for running mixture-of-experts models from SSDs. Three models, two engines.  - Stars: 4 - Forks: 1 - Watchers: 4 - Open issues: 0 - License: MIT License - Default branch: main - Created: 2026-09-08T19:50:45Z  ## Languages  - C - HTML - Python - Shell  ## Topics  - apple-silicon - inference - llm - metal - mixture-of-experts - nvme - ssd  ## Top Contributors  - konstantinnikol (28 contributions)  ---  ## README  # ARGODRIVE  **Layout, balancer and instruments for running mixture-of-experts models from SSDs.** Models of 518 GB to 1.44 TB on a 128 GB laptop: every token waits on disk, so what matters is not how much bandwidth you own but how long the slowest required read takes.  Three models, three forks, one method: the trunk stays in memory, the routed experts stream from NVMe, and every expert read is split across byte-identical replicas on however many drives are attached. Kimi K3 (2.78T) goes from 0.55 to 0.96 tok/s, GLM-5.3 (744B) from 2.02 to 3.70, DeepSeek V4.1-Flash from 14.38 to 18.45, with the same output at every rung.  ## What it has done  | model | engine | baseline | best measured | gain | |---|---|---|---|--…
