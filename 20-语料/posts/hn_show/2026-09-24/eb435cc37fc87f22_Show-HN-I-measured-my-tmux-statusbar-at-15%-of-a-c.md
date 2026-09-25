---
type: "corpus"
item_id: "eb435cc37fc87f22"
title: "Show HN: I measured my tmux statusbar at 15% of a core and replaced the forks"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49829597"
project_url: "https://yogesh.lonkar.org/posts/ten-years-of-tmux"
author: "yogeshlor"
published_at: "2026-09-24T12:18:19Z"
captured_at: "2026-09-24T23:57:22+08:00"
lang: "en"
kind: "post"
topic: "开发者工具"
shard: "2026-09-24"
pub_day: "2026-09-24"
tags:
  - 语料
  - hn_show
  - author_yogeshlor
  - story_49829597
  - show_hn
metrics: {"points": 3, "comments": 1, "engagement_velocity": 3}
comments_count: 1
comments_total: 1
discovered_via: "hn:show_hn:3d"
---

# Show HN: I measured my tmux statusbar at 15% of a core and replaced the forks

> [!info] 一句话导读
> tmux status-interval 1 had six #() programs for statusbar, on battery that was 15.4% of a core.After digging found fork+exec through sh -c is ~14.6 ms and compu…

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49829597>
> 指标：点赞=3 · 评论=1 · engagement_velocity=3
> 作者：yogeshlor　|　发布：2026-09-24T12:18:19Z
> 项目链接：<https://yogesh.lonkar.org/posts/ten-years-of-tmux>
> 采集：2026-09-24T23:57:22+08:00　|　id：`eb435cc37fc87f22`

## 正文

tmux status-interval 1 had six #() programs for statusbar, on battery that was 15.4% of a core.After digging found fork+exec through sh -c is ~14.6 ms and computing the actual segments was 2.6 ms on my device.Plus had ~1.5k lines of zsh scripts.Now one deamon process, caches in memory, unix socket and one #() for the whole right side. From 153.77 ms/s → 18.43 ms/s.Made that into a tmux plugin. You can try it without installing/configuring:docker run --rm -it lonkarorg/tmux-companion:playground

## 评论（1/1）

> **yogeshlor** · 2026-09-24T12:26:49.000Z　
> Recording of the tmux-companion: https://asciinema.org/a/1266213

## 导航

- 项目页：[[10-项目/yogesh.lonkar.org_47fd66c7]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`开发者工具`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
