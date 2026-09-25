---
type: "project"
title: "Show HN: I measured my tmux statusbar at 15% of a core and replaced the forks"
project_url: "https://yogesh.lonkar.org/posts/ten-years-of-tmux"
first_seen: "2026-09-24T23:57:22+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_yogeshlor
  - story_49829597
  - show_hn
lang: "en"
---

# Show HN: I measured my tmux statusbar at 15% of a core and replaced the forks

> [!info] 一句话导读
> tmux status-interval 1 had six #() programs for statusbar, on battery that was 15.4% of a core.After digging found fork+exec through sh -c is ~14.6 ms and compu…

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://yogesh.lonkar.org/posts/ten-years-of-tmux>
> 首次收录：2026-09-24T23:57:22+08:00
> 来源渠道：HN Show HN
> 标签：author_yogeshlor, story_49829597, show_hn
> 最新指标：点赞=3 · 评论=1 · engagement_velocity=3

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-09-24T23:57:22+08:00 | HN Show HN | 点赞=3 · 评论=1 · engagement_velocity=3 | [[20-语料/posts/hn_show/2026-09-24/eb435cc37fc87f22_Show-HN-I-measured-my-tmux-statusbar-at-15%-of-a-c]] |

## 摘要正文

tmux status-interval 1 had six #() programs for statusbar, on battery that was 15.4% of a core.After digging found fork+exec through sh -c is ~14.6 ms and computing the actual segments was 2.6 ms on my device.Plus had ~1.5k lines of zsh scripts.Now one deamon process, caches in memory, unix socket and one #() for the whole right side. From 153.77 ms/s → 18.43 ms/s.Made that into a tmux plugin. You can try it without installing/configuring:docker run --rm -it lonkarorg/tmux-companion:playground
