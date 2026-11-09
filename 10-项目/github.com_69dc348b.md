---
type: "project"
title: "Show HN: Record, branch, and compare command runs in stdlib-only Python"
project_url: "https://github.com/Protention/ocura-oss"
first_seen: "2026-11-09T09:39:29+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_protention
  - story_50417782
  - show_hn
lang: "en"
---

# Show HN: Record, branch, and compare command runs in stdlib-only Python

> [!info] 一句话导读
> Hi, this is a package I developed for keeping track of short toy-model development cycles and explaining what changed between runs.The core idea: commands run t…

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://github.com/Protention/ocura-oss>
> 首次收录：2026-11-09T09:39:29+08:00
> 来源渠道：HN Show HN
> 标签：author_protention, story_50417782, show_hn
> 最新指标：点赞=3 · 评论=0 · engagement_velocity=3

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-11-09T09:39:29+08:00 | HN Show HN | 点赞=3 · 评论=0 · engagement_velocity=3 | [[20-语料/posts/hn_show/2026-11-09/c2d72a5c8b312d5d_Show-HN-Record,-branch,-and-compare-command-runs-i]] |

## 摘要正文

Hi, this is a package I developed for keeping track of short toy-model development cycles and explaining what changed between runs.The core idea: commands run through the package, and their declared parameters (or injected parameters with --substitute) and outcomes go into a dependency-free ledger stored in the project. Because that ledger lives in the project directory, it has worked well for passing context between different agents. I’ve also found some use for it in CI work.
