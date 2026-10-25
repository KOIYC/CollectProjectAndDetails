---
type: "project"
title: "Show HN: Find overlapping Rust tests with mutation testing"
project_url: "https://github.com/yasuyuky/cargo-test-prune"
first_seen: "2026-10-25T23:24:35+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_yasuyuky
  - story_50230702
  - show_hn
lang: "en"
---

# Show HN: Find overlapping Rust tests with mutation testing

> [!info] 一句话导读
> To tackle the ever-increasing number of tests, I built cargo-test-prune.The idea behind it is to use cargo-mutants to generate mutants, and then solve the set c…

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://github.com/yasuyuky/cargo-test-prune>
> 首次收录：2026-10-25T23:24:35+08:00
> 来源渠道：HN Show HN
> 标签：author_yasuyuky, story_50230702, show_hn
> 最新指标：点赞=5 · 评论=0 · engagement_velocity=5

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-10-25T23:24:35+08:00 | HN Show HN | 点赞=5 · 评论=0 · engagement_velocity=5 | [[20-语料/posts/hn_show/2026-10-25/a0fc58e3aee97676_Show-HN-Find-overlapping-Rust-tests-with-mutation]] |

## 摘要正文

To tackle the ever-increasing number of tests, I built cargo-test-prune.The idea behind it is to use cargo-mutants to generate mutants, and then solve the set cover problem for those mutants to suggest which tests can be eliminated. (use a greedy algorithm to cover the detected mutants with fewer tests)I came up with this as a countermeasure against the monotonically increasing tests that tend to accumulate, especially when coding with AI.In fact, this very repository was also written using AI.I ran this tool on a previous revision of this repository. There were 11 tests and 108 generated mutants: 73 were caught by the tests, 23 survived, and 12 failed to compile. I removed the 5 tests suggested by the tool and re-ran the same 108 mutants. The remaining 6 tests caught the exact same 73 mutants.Tests partly serve as documentation, so simply applying this isn't necessarily recommended, but since writing less code still holds value in the AI era, I think this tool could be quite useful.
