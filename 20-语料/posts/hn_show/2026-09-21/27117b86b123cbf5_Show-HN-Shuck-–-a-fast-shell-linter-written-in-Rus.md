---
type: "corpus"
item_id: "27117b86b123cbf5"
title: "Show HN: Shuck – a fast shell linter written in Rust"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=47963760"
project_url: "https://github.com/ewhauser/shuck"
author: "ewhauser421"
published_at: "2026-04-30T15:13:08Z"
captured_at: "2026-09-21T01:40:53+08:00"
lang: "en"
kind: "post"
topic: "开发者工具"
shard: "2026-09-21"
pub_day: "2026-04-30"
tags:
  - 语料
  - hn_show
  - author_ewhauser421
  - story_47963760
  - show_hn
metrics: {"points": 8, "comments": 1, "engagement_velocity": 8}
comments_count: 1
comments_total: 1
discovered_via: "hn:show_hn:174d"
---

# Show HN: Shuck – a fast shell linter written in Rust

> [!info] 一句话导读
> I’ve been working on shuck, a shell script linter written in Rust.ShellCheck is excellent project and set the bar for this space. However, it's very slow and ta…

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=47963760>
> 指标：点赞=8 · 评论=1 · engagement_velocity=8
> 作者：ewhauser421　|　发布：2026-04-30T15:13:08Z
> 项目链接：<https://github.com/ewhauser/shuck>
> 采集：2026-09-21T01:40:53+08:00　|　id：`27117b86b123cbf5`

## 正文

I’ve been working on shuck, a shell script linter written in Rust.ShellCheck is excellent project and set the bar for this space. However, it's very slow and take up a far amount of resources. shuck is conservatively 20x faster than shellcheck and uses a fraction of the resources. shuck currently supports sh, bash, dash, ksh, mksh, and zsh.shuck should mostly be a drop in replacement for shellcheck but it is not a port since shellcheck is GPL. It is s clean-room implementation with its own parser and analysis engine, so behavior may differ in some cases. shuck is tested against shellcheck on a large number of open source projects with a lot of shell scripts and has very few variations.That said, I’ve tried to make migration easy: 1) shuck supports ShellCheck-style suppression 2) you can run shuck in shellcheck compatibility mode where it has all the same CLI args and output.This is still early, and I’d especially love feedback from people who maintain large monorepos, CI-heavy projects, or lots of shell scripts. I’m interested in places where ShellCheck compatibility matters, places where it does not, and which classes of shell bugs people most want lint/fix support for next.

## 评论（1/1）

> **bbor** · 2026-05-01T08:25:30.000Z　
> Looks great, and I love the `zsh` support! Took a note to whip up a Sublime plugin for this when I get a chance. Congrats on shipping something, seriously.Out of curiosity: how in the name of the good lord above did you end up with 1,163 commits on this repo in the span of 3 weeks, all by yourself? I was assuming Claude commits given the `./.claude/skills` dir, but doesn't Claude usually sign it's own commits as a collaborator?

## 导航

- 项目页：[[10-项目/github.com_e7a3499e]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`开发者工具`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
