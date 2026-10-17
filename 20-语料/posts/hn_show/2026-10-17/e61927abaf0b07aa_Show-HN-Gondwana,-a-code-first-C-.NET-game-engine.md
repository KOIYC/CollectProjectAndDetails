---
type: "corpus"
item_id: "e61927abaf0b07aa"
title: "Show HN: Gondwana, a code-first C#/.NET game engine with WebGL"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50123777"
project_url: "https://github.com/Isthimius/Gondwana"
author: "isthimius"
published_at: "2026-10-16T20:01:59Z"
captured_at: "2026-10-17T13:35:15+08:00"
lang: "en"
kind: "post"
topic: "开发者工具"
shard: "2026-10-17"
pub_day: "2026-10-16"
tags:
  - 语料
  - hn_show
  - author_isthimius
  - story_50123777
  - show_hn
metrics: {"points": 4, "comments": 1, "engagement_velocity": 4}
comments_count: 1
comments_total: 1
discovered_via: "hn:show_hn:3d"
---

# Show HN: Gondwana, a code-first C#/.NET game engine with WebGL

> [!info] 一句话导读
> Gondwana is a 2D/2.5D game engine for C#/.NET 8 that I’ve been building over the past 16 months, using SkiaSharp for rendering. I've spent my career creating we…

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50123777>
> 指标：点赞=4 · 评论=1 · engagement_velocity=4
> 作者：isthimius　|　发布：2026-10-16T20:01:59Z
> 项目链接：<https://github.com/Isthimius/Gondwana>
> 采集：2026-10-17T13:35:15+08:00　|　id：`e61927abaf0b07aa`

## 正文

Gondwana is a 2D/2.5D game engine for C#/.NET 8 that I’ve been building over the past 16 months, using SkiaSharp for rendering. I've spent my career creating web and distributed apps and that has influenced the engine's development, so it will feel very familiar to anyone with a similar background. The engine is deliberately code-first in its implementation but still includes visual authoring tools and a custom CLI.I started creating Gondwana to host my own RTS and SNES-style games, to offload the game ideas percolating in my brain. I wanted to focus more on creating gameplay systems and was less concerned with 3D graphics. The predictability and transparency of the old Win32/GDI era were the ideal for what I was shooting for, but I also wanted something faster and more portable than GDI32. To that end, I am not trying to emulate the bigger engines.Spot! became my primary dogfooding project that I’ve since pushed up to itch.io. Getting a game to that point really helped burn away the cruft that accumulates from trying to create something like this. I was able to get Spot! to render at a consistent 120 fps on my dev machine. I experienced the absolute ecstasy of getting WebGL to cooperate with the engine cycle. And I discovered that even if Gondwana is code-first, you don’t want to hand-code platformer levels, so I added Gondwana Studio to the repository. Studio uses the same file formats that are understood by the core engine. Asset handling was beefed up, UI widgets were added for things like game HUD elements and engine diagnostics, and I fleshed out the CI/release pipeline to keep it organized.As it stands currently, Gondwana supports GPU-backed OpenGL rendering with WinForms and Avalonia hosts, and a dedicated WebGL path with Blazor. Recently a good bit of effort has been put into optimizing the rendering hot-path, reducing contention between simulation and presentation, and into making the visual tooling easy to use by people other than just me. I even was able to get itch.io deployment down to a single command in the custom CLI.The engine is still actively evolving feature-wise, but the core rendering is pretty solid right now. I expect Gondwana will remain 2D/2.5D with parallax support, so I am not trying to supplant Unity, Godot, et al. Also worth noting, Gondwana intentionally does not have an explicit ECS framework built in, although one could absolutely work well with the engine if desired.The project is MIT licensed, the source is hosted on GitHub, the packages are on NuGet, and Spot! is playable in the browser at itch.io. I will include several links in the first comment under this. I’d love to see what other hobbyists or indie game devs think of the project. Feedback on usability, as well as praise and/or criticism of the architecture would be awesome.

## 评论（1/1）

> **pikarde** · 2026-10-16T20:46:15.000Z　
> I’ve been following the repo for a while. I appreciate the effort and hard work that went into this project. Definitely worth checking out.

## 导航

- 项目页：[[10-项目/github.com_b612f0e6]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`开发者工具`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
