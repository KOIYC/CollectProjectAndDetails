---
type: "project"
title: "Show HN: Inkvec, Pareto frontier in-browser vectorizer (Open Source)"
project_url: "https://github.com/logolabs/inkvec"
first_seen: "2026-09-20T14:01:34+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_stefatorus
  - story_49761511
  - show_hn
lang: "en"
---

# Show HN: Inkvec, Pareto frontier in-browser vectorizer (Open Source)

> [!info] 一句话导读
> SoTA Vectorizer on the pareto frontier

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://github.com/logolabs/inkvec>
> 首次收录：2026-09-20T14:01:34+08:00
> 来源渠道：HN Show HN
> 标签：author_stefatorus, story_49761511, show_hn
> 最新指标：点赞=2 · 评论=3 · engagement_velocity=2

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-09-20T02:35:34+08:00 | HN Show HN | 点赞=2 · 评论=3 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-09-20/b298716af3cfd11c_Show-HN-Inkvec,-Pareto-frontier-in-browser-vectori]] |
| 2026-09-20T02:46:51+08:00 | HN Show HN | 点赞=2 · 评论=3 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-09-20/b298716af3cfd11c_Show-HN-Inkvec,-Pareto-frontier-in-browser-vectori]] |
| 2026-09-20T02:55:58+08:00 | HN Show HN | 点赞=2 · 评论=3 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-09-20/b298716af3cfd11c_Show-HN-Inkvec,-Pareto-frontier-in-browser-vectori]] |
| 2026-09-20T03:04:29+08:00 | HN Show HN | 点赞=2 · 评论=3 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-09-20/b298716af3cfd11c_Show-HN-Inkvec,-Pareto-frontier-in-browser-vectori]] |
| 2026-09-20T03:16:53+08:00 | HN Show HN | 点赞=2 · 评论=3 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-09-20/b298716af3cfd11c_Show-HN-Inkvec,-Pareto-frontier-in-browser-vectori]] |
| 2026-09-20T03:29:12+08:00 | HN Show HN | 点赞=2 · 评论=3 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-09-20/b298716af3cfd11c_Show-HN-Inkvec,-Pareto-frontier-in-browser-vectori]] |
| 2026-09-20T03:38:50+08:00 | HN Show HN | 点赞=2 · 评论=3 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-09-20/b298716af3cfd11c_Show-HN-Inkvec,-Pareto-frontier-in-browser-vectori]] |
| 2026-09-20T09:23:24+08:00 | HN Show HN | 点赞=2 · 评论=3 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-09-20/b298716af3cfd11c_Show-HN-Inkvec,-Pareto-frontier-in-browser-vectori]] |
| 2026-09-20T14:01:34+08:00 | HN Show HN | 点赞=2 · 评论=3 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-09-20/b298716af3cfd11c_Show-HN-Inkvec,-Pareto-frontier-in-browser-vectori]] |

## 摘要正文

# logolabs/inkvec  SoTA Vectorizer on the pareto frontier  - Stars: 2 - Forks: 0 - Watchers: 2 - Open issues: 2 - License: Apache License 2.0 - Default branch: main - Created: 2026-09-15T19:10:29Z  ## Languages  - HTML - JavaScript - Python - Rust - Shell  ## Top Contributors  - Stefatorus (1 contributions)  ---  ## README  Inkvec reads a PNG, JPEG, WebP, GIF, BMP or TIFF and writes an SVG whose geometry is decided by the evidence in the pixels:  - A boundary sits where the anti-aliasing says it is — within **~0.05 px** on analytic test circles (the level-set extraction's own resolution limit; `crates/inkvec-trace/src/coverage.rs`), which is a synthetic-input figure, not a corpus one. - A circle is written as ` `, not four cubics pretending to be one. - A smooth ramp becomes a **real gradient**, not coloured bands. - The number of coordinates is chosen by **minimum description length** — not a tolerance slider you have to guess at.  Most tracers spend points wherever their curve-fit tolerance lets them. Inkvec spends them where the artist would have: one path per region, a circle where there is a circle, shared edges between shapes that never drift apart.  ---  ## Results  Inkvec v…
