---
type: "project"
title: "Show HN: Free GitHub Action that scans PR diffs for malicious code, not quality"
project_url: "https://github.com/marketplace/actions/vigil-pr-scanner"
first_seen: "2026-09-20T09:36:43+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_arsalsajjad
  - story_49749862
  - show_hn
lang: "en"
---

# Show HN: Free GitHub Action that scans PR diffs for malicious code, not quality

> [!info] 一句话导读
> Vigil PR Scanner · Actions · GitHub Marketplace

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://github.com/marketplace/actions/vigil-pr-scanner>
> 首次收录：2026-09-20T09:36:43+08:00
> 来源渠道：HN Show HN
> 标签：author_arsalsajjad, story_49749862, show_hn
> 最新指标：点赞=2 · 评论=0 · engagement_velocity=2

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-09-20T09:23:24+08:00 | HN Show HN | 点赞=2 · 评论=0 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-09-20/97028291bc9e448c_Show-HN-Free-GitHub-Action-that-scans-PR-diffs-for]] |
| 2026-09-20T09:36:43+08:00 | HN Show HN | 点赞=2 · 评论=0 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-09-20/97028291bc9e448c_Show-HN-Free-GitHub-Action-that-scans-PR-diffs-for]] |

## 摘要正文

Vigil PR Scanner · Actions · GitHub Marketplace · GitHub  By arsallls  # Vigil  Scans PR diffs for malicious capability, not code quality. No style notes, no refactor suggestions, no "consider extracting a helper". One question only:  > Did this PR gain the ability to run commands, phone home, or read credentials — and does the file it landed in have any business doing that?  See example output ↓ — Vigil flagging a real PR alongside an LLM reviewer.  ## Two ways to run it  - GitHub Action — two workflow files, zero infrastructure. Start here. - Self-hosted — you run a small webhook server; code never leaves your network and a PR structurally cannot tamper with the scanner. See SELFHOST.md.  ## Install  No secrets. No account. No configuration. Two small files, both on your default branch. `GITHUB_TOKEN` is minted automatically by Actions — there is nothing to set up.  `.github/workflows/vigil-scan.yml`:  ``` name: vigil-scan on:   pull_request:     types: [opened, synchronize, reopened] jobs:   scan:     uses: arsallls/Vigil-Public/.github/workflows/reusable-scan.yml@v1 ```  `.github/workflows/vigil-report.yml`:  ``` name: vigil-report on:   workflow_run:     workflows: [vigil-scan…
