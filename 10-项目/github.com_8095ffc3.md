---
type: "project"
title: "Show HN: Yet another argument parser for Zig"
project_url: "https://github.com/gabor-boros/yaap"
first_seen: "2026-09-20T14:57:50+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_gabor-boros
  - story_49709062
  - show_hn
lang: "en"
---

# Show HN: Yet another argument parser for Zig

> [!info] 一句话导读
> Yet another argument parser for Zig

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://github.com/gabor-boros/yaap>
> 首次收录：2026-09-20T14:57:50+08:00
> 来源渠道：HN Show HN
> 标签：author_gabor-boros, story_49709062, show_hn
> 最新指标：点赞=2 · 评论=0 · engagement_velocity=2

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-09-20T09:23:24+08:00 | HN Show HN | 点赞=2 · 评论=0 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-09-20/a3fc2c860fa97709_Show-HN-Yet-another-argument-parser-for-Zig]] |
| 2026-09-20T14:57:50+08:00 | HN Show HN | 点赞=2 · 评论=0 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-09-20/a3fc2c860fa97709_Show-HN-Yet-another-argument-parser-for-Zig]] |

## 摘要正文

# gabor-boros/yaap  Yet another argument parser for Zig  - Stars: 2 - Forks: 0 - Watchers: 2 - Open issues: 9 - License: MIT License - Homepage: https://gabor-boros.github.io/yaap - Default branch: main - Created: 2026-09-14T21:54:32Z  ## Languages  - Zig  ## Topics  - argument-parser - cli - zig-library - zig-package - ziglang  ## Top Contributors  - gabor-boros (3 contributions) - github-actions[bot] (1 contributions)  ---  ## README  # YAAP  Yet Another Argument Parser.  YAAP is an argument parser inspired by Python's `argparse`. While it is giving the building blocks to make a CLI application, it is intentionally not bloated with features like autocompletion generation, colored outputs, etc.  Instead, it gives an argument parser with an optional `--help` flag to print the usage.  ## Features  - Positional arguments - Option default values - Long and short options (e.g., `-v`, `--verbose`) - Mixed positional arguments and options (`cmd -v arg1 --option`) - Subcommands (e.g., `cmd -v subcmd -a` ) - Clear errors on missing values - Optional `-h | --help` option  ## Installation  **1. Fetch the package**  ```shell zig fetch --save git+https://github.com/gabor-boros/yaap#v0.1.0 ``` …
