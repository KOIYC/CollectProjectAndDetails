---
type: "corpus"
item_id: "ba1d84ed199d789e"
title: "Show HN: profiler-md converts performance profiles to Markdown"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50507976"
project_url: "https://github.com/TomerAberbach/profiler-md"
author: "tomeraberbach"
published_at: "2026-11-15T16:04:51Z"
captured_at: "2026-11-16T10:00:05+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-11-16"
pub_day: "2026-11-15"
tags:
  - 语料
  - hn_show
  - author_tomeraberbach
  - story_50507976
  - show_hn
metrics: {"points": 4, "comments": 0, "engagement_velocity": 4}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:3d"
---

# Show HN: profiler-md converts performance profiles to Markdown

> [!info] 一句话导读
> Hi HN!profiler-md is a CLI and JS library that converts performance profiles to Markdown across 17 formats (e.g. pprof), 29 profilers (e.g. py-spy), 22 language…

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50507976>
> 指标：点赞=4 · 评论=0 · engagement_velocity=4
> 作者：tomeraberbach　|　发布：2026-11-15T16:04:51Z
> 项目链接：<https://github.com/TomerAberbach/profiler-md>
> 采集：2026-11-16T10:00:05+08:00　|　id：`ba1d84ed199d789e`

## 正文

Hi HN!profiler-md is a CLI and JS library that converts performance profiles to Markdown across 17 formats (e.g. pprof), 29 profilers (e.g. py-spy), 22 languages (e.g. Rust), and 4 profile types (call stack profiles, call graphs, heap snapshots, and traces).Earlier this year I tried using AI agents for performance optimization. They weren't very effective because they frequently:- Speculated about why something was slow from just reading the code- Made changes, measured the wall time before vs after, and struggled to distinguish real improvements from noise- Analyzed raw profiles using one-off scripts, which were often subtly incorrectThe issue was that the agents couldn't read a flamegraph like I could. In a flamegraph, I could see what was slow, and when I made changes, I could see whether the targeted work was eliminated. The agents needed a feedback loop like that.So I wrote a small converter from Node CPU profiles to Markdown. The agents were much more effective when using it, and I realized I also liked reading the Markdown myself!I felt this had potential, and I use many different programming languages at work, so I decided to build profiler-md. I also wrote an agent skill [1], which I've successfully used to optimize profiler-md itself and its pprof-format dependency (a 78x speedup on a large pprof file [2] and a 3.3x speedup more broadly [3]).I got to solve some fun problems for this project:- Making it so that adding a new format, profiler, or profile type is as simple as implementing an interface and adding to a registry. I also have project skills for this!- Resolving weirdly differing profiler semantics (e.g. around what line numbers mean [4] [5] [6] [7]) by setting up the right interface boundaries.- Matching functions across profiles for the Markdown diff output. A profile doesn't contain the full code, so this required some heuristics. I evaluated the algorithm by measuring recall (99.9%) and precision (99.7%) on diffs from real version upgrades.- Designing a call tree renderer that maximizes metrics such as how many of the hottest functions it shows and how much of the profile's self value it covers [8].I'd love to hear what you think. Try it out and let me know if you have any feedback or questions!Full disclosure: I work at Anthropic, but this personal project is unrelated to my employer.[1] https://github.com/TomerAberbach/profiler-md/#skill[2] https://github.com/DataDog/pprof-format/pull/77[3] https://github.com/DataDog/pprof-format/pull/107[4] https://github.com/rbspy/rbspy/issues/409[5] https://github.com/oven-sh/bun/issues/29240[6] https://github.com/google/pprof-nodejs/issues/361[7] https://github.com/NixOS/nix/blob/16fa212a96192479593620e9b9...[8] https://github.com/TomerAberbach/profiler-md/blob/a1ee95e4b5...

## 关联链接

- https://github.com/DataDog/pprof-format/pull/107[4
- https://github.com/DataDog/pprof-format/pull/77[3
- https://github.com/NixOS/nix/blob/16fa212a96192479593620e9b9...[8
- https://github.com/TomerAberbach/profiler-md/#skill[2
- https://github.com/TomerAberbach/profiler-md/blob/a1ee95e4b5...
- https://github.com/google/pprof-nodejs/issues/361[7
- https://github.com/oven-sh/bun/issues/29240[6
- https://github.com/rbspy/rbspy/issues/409[5

## 导航

- 项目页：[[10-项目/github.com_c20215b2]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
