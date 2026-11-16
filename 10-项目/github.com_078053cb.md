---
type: "project"
title: "Show HN: Fix Gate – verifies security-fix PRs, incl. AI-written ones"
project_url: "https://github.com/IWEBai/fix-gate-action"
first_seen: "2026-11-11T13:37:17+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_mdzariflatif
  - story_50444188
  - show_hn
lang: "en"
---

# Show HN: Fix Gate – verifies security-fix PRs, incl. AI-written ones

> [!info] 一句话导读
> IWEBai/fix-gate-action

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://github.com/IWEBai/fix-gate-action>
> 首次收录：2026-11-11T13:37:17+08:00
> 来源渠道：HN Show HN
> 标签：author_mdzariflatif, story_50444188, show_hn
> 最新指标：点赞=2 · 评论=0 · engagement_velocity=2

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-11-11T13:37:17+08:00 | HN Show HN | 点赞=2 · 评论=0 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-11-11/30aaca7d455c0b9e_Show-HN-Fix-Gate-–-verifies-security-fix-PRs,-incl]] |

## 摘要正文

# IWEBai/fix-gate-action  Fix Gate: a free GitHub Action that checks any security-fix pull request. Finding gone, nothing new, files parse, tests not newly failed. Rule-based, runs on your runner.  - Stars: 0 - Forks: 0 - Watchers: 0 - Open issues: 0 - License: MIT License - Homepage: https://www.railo.dev/fix-gate - Default branch: main - Created: 2026-10-29T05:29:58Z  ## Topics  - code-review - code-security - devsecops - github-actions - pull-requests - sast - security - semgrep - vulnerability-remediation  ## Top Contributors  - zariffromlatif (10 contributions)  ---  ## README  # Fix Gate  **Was that security fix actually a fix?**  Fix Gate is a free GitHub Action that verifies a security-fix pull request, whoever or whatever wrote it: GitHub Copilot Autofix, Snyk Agent Fix, an editor assistant, or a person. It answers five questions and posts them as a check run named **Fix Gate**:  | Check | How | |---|---| | Targeted finding gone | Railo's rules run over the base and head versions of every changed file. The finding reported at base, inside the changed lines, must no longer match at head. | | Nothing new in the changed lines | A finding at head with no counterpart at base fa…
