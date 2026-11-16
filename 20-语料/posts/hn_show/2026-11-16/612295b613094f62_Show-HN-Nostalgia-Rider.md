---
type: "corpus"
item_id: "612295b613094f62"
title: "Show HN: Nostalgia Rider"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50507891"
project_url: "https://nostalgiarider.com/"
author: "qvq"
published_at: "2026-11-15T15:57:07Z"
captured_at: "2026-11-16T10:00:05+08:00"
lang: "en"
kind: "post"
topic: "开发者工具"
shard: "2026-11-16"
pub_day: "2026-11-15"
tags:
  - 语料
  - hn_show
  - author_qvq
  - story_50507891
  - show_hn
metrics: {"points": 3, "comments": 1, "engagement_velocity": 3}
comments_count: 1
comments_total: 1
discovered_via: "hn:show_hn:3d"
---

# Show HN: Nostalgia Rider

> [!info] 一句话导读
> Nostalgia-Rider is a browser toy that mashes up Line Rider [1] and Ski Stunt Simulator [2]. I loved to play both back when they were popular and thought it woul…

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50507891>
> 指标：点赞=3 · 评论=1 · engagement_velocity=3
> 作者：qvq　|　发布：2026-11-15T15:57:07Z
> 项目链接：<https://nostalgiarider.com/>
> 采集：2026-11-16T10:00:05+08:00　|　id：`612295b613094f62`

## 正文

Nostalgia-Rider is a browser toy that mashes up Line Rider [1] and Ski Stunt Simulator [2]. I loved to play both back when they were popular and thought it would be fun to create this.No accounts or ads. It's a pure static site.[1] https://www.linerider.com
[2] https://www.cs.ubc.ca/~van/sssjava/javademo.html

## 评论（1/1）

> **qvq** · 2026-11-15T16:11:56.000Z　
> Technical details:I did pay attention to performance, even if it's overkill. Uses Zig compiled to WASM for the game state. Rendering is done in JS and WebGL reading from SharedArrayBuffer. I didn't think a single language was worth the boundary trampolining and extra tooling.I tried to get muti-threading to work but that seems to require multiple web workers running instances of the WASM binary. It started to make other things more complicated (probably because I couldn't find the right level of abstraction) so I gave up. Running WASM in a single worker, off the main thread, is good enough for now.

## 关联链接

- https://www.cs.ubc.ca/~van/sssjava/javademo.html
- https://www.linerider.com

## 导航

- 项目页：[[10-项目/nostalgiarider.com_51dafee8]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`开发者工具`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
