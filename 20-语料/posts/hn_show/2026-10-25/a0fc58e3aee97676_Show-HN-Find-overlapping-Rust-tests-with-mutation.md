---
type: "corpus"
item_id: "a0fc58e3aee97676"
title: "Show HN: Find overlapping Rust tests with mutation testing"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50230702"
project_url: "https://github.com/yasuyuky/cargo-test-prune"
author: "yasuyuky"
published_at: "2026-10-25T12:02:00Z"
captured_at: "2026-10-25T23:24:35+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-10-25"
pub_day: "2026-10-25"
tags:
  - 语料
  - hn_show
  - author_yasuyuky
  - story_50230702
  - show_hn
metrics: {"points": 5, "comments": 0, "engagement_velocity": 5}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:3d"
---

# Show HN: Find overlapping Rust tests with mutation testing

> [!info] 一句话导读
> To tackle the ever-increasing number of tests, I built cargo-test-prune.The idea behind it is to use cargo-mutants to generate mutants, and then solve the set c…

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50230702>
> 指标：点赞=5 · 评论=0 · engagement_velocity=5
> 作者：yasuyuky　|　发布：2026-10-25T12:02:00Z
> 项目链接：<https://github.com/yasuyuky/cargo-test-prune>
> 采集：2026-10-25T23:24:35+08:00　|　id：`a0fc58e3aee97676`

## 正文

To tackle the ever-increasing number of tests, I built cargo-test-prune.The idea behind it is to use cargo-mutants to generate mutants, and then solve the set cover problem for those mutants to suggest which tests can be eliminated.
(use a greedy algorithm to cover the detected mutants with fewer tests)I came up with this as a countermeasure against the monotonically increasing tests that tend to accumulate, especially when coding with AI.In fact, this very repository was also written using AI.I ran this tool on a previous revision of this repository. There were 11 tests and 108 generated mutants: 73 were caught by the tests, 23 survived, and 12 failed to compile.
I removed the 5 tests suggested by the tool and re-ran the same 108 mutants. The remaining 6 tests caught the exact same 73 mutants.Tests partly serve as documentation, so simply applying this isn't necessarily recommended, but since writing less code still holds value in the AI era, I think this tool could be quite useful.

## 导航

- 项目页：[[10-项目/github.com_f1bc11a6]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
