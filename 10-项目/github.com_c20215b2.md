---
type: "project"
title: "Show HN: profiler-md converts performance profiles to Markdown"
project_url: "https://github.com/TomerAberbach/profiler-md"
first_seen: "2026-11-16T10:00:05+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_tomeraberbach
  - story_50507976
  - show_hn
lang: "en"
---

# Show HN: profiler-md converts performance profiles to Markdown

> [!info] 一句话导读
> Hi HN!profiler-md is a CLI and JS library that converts performance profiles to Markdown across 17 formats (e.g. pprof), 29 profilers (e.g. py-spy), 22 language…

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://github.com/TomerAberbach/profiler-md>
> 首次收录：2026-11-16T10:00:05+08:00
> 来源渠道：HN Show HN
> 标签：author_tomeraberbach, story_50507976, show_hn
> 最新指标：点赞=4 · 评论=0 · engagement_velocity=4

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-11-16T10:00:05+08:00 | HN Show HN | 点赞=4 · 评论=0 · engagement_velocity=4 | [[20-语料/posts/hn_show/2026-11-16/ba1d84ed199d789e_Show-HN-profiler-md-converts-performance-profiles]] |

## 摘要正文

Hi HN!profiler-md is a CLI and JS library that converts performance profiles to Markdown across 17 formats (e.g. pprof), 29 profilers (e.g. py-spy), 22 languages (e.g. Rust), and 4 profile types (call stack profiles, call graphs, heap snapshots, and traces).Earlier this year I tried using AI agents for performance optimization. They weren't very effective because they frequently:- Speculated about why something was slow from just reading the code- Made changes, measured the wall time before vs after, and struggled to distinguish real improvements from noise- Analyzed raw profiles using one-off scripts, which were often subtly incorrectThe issue was that the agents couldn't read a flamegraph like I could. In a flamegraph, I could see what was slow, and when I made changes, I could see whether the targeted work was eliminated. The agents needed a feedback loop like that.So I wrote a small converter from Node CPU profiles to Markdown. The agents were much more effective when using it, and I realized I also liked reading the Markdown myself!I felt this had potential, and I use many different programming languages at work, so I decided to build profiler-md. I also wrote an agent skill […
