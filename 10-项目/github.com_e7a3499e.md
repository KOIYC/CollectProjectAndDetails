---
type: "project"
title: "Show HN: Shuck – a fast shell linter written in Rust"
project_url: "https://github.com/ewhauser/shuck"
first_seen: "2026-09-21T01:40:53+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_ewhauser421
  - story_47963760
  - show_hn
lang: "en"
---

# Show HN: Shuck – a fast shell linter written in Rust

> [!info] 一句话导读
> I’ve been working on shuck, a shell script linter written in Rust.ShellCheck is excellent project and set the bar for this space. However, it's very slow and ta…

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://github.com/ewhauser/shuck>
> 首次收录：2026-09-21T01:40:53+08:00
> 来源渠道：HN Show HN
> 标签：author_ewhauser421, story_47963760, show_hn
> 最新指标：点赞=8 · 评论=1 · engagement_velocity=8

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-09-21T01:09:14+08:00 | HN Show HN | 点赞=8 · 评论=1 · engagement_velocity=8 | [[20-语料/posts/hn_show/2026-09-21/27117b86b123cbf5_Show-HN-Shuck-–-a-fast-shell-linter-written-in-Rus]] |
| 2026-09-21T01:13:42+08:00 | HN Show HN | 点赞=8 · 评论=1 · engagement_velocity=8 | [[20-语料/posts/hn_show/2026-09-21/27117b86b123cbf5_Show-HN-Shuck-–-a-fast-shell-linter-written-in-Rus]] |
| 2026-09-21T01:40:53+08:00 | HN Show HN | 点赞=8 · 评论=1 · engagement_velocity=8 | [[20-语料/posts/hn_show/2026-09-21/27117b86b123cbf5_Show-HN-Shuck-–-a-fast-shell-linter-written-in-Rus]] |

## 摘要正文

I’ve been working on shuck, a shell script linter written in Rust.ShellCheck is excellent project and set the bar for this space. However, it's very slow and take up a far amount of resources. shuck is conservatively 20x faster than shellcheck and uses a fraction of the resources. shuck currently supports sh, bash, dash, ksh, mksh, and zsh.shuck should mostly be a drop in replacement for shellcheck but it is not a port since shellcheck is GPL. It is s clean-room implementation with its own parser and analysis engine, so behavior may differ in some cases. shuck is tested against shellcheck on a large number of open source projects with a lot of shell scripts and has very few variations.That said, I’ve tried to make migration easy: 1) shuck supports ShellCheck-style suppression 2) you can run shuck in shellcheck compatibility mode where it has all the same CLI args and output.This is still early, and I’d especially love feedback from people who maintain large monorepos, CI-heavy projects, or lots of shell scripts. I’m interested in places where ShellCheck compatibility matters, places where it does not, and which classes of shell bugs people most want lint/fix support for next.
