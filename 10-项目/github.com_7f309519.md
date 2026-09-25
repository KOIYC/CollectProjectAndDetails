---
type: "project"
title: "jaredpalmer/kev"
project_url: "https://github.com/jaredpalmer/kev"
first_seen: "2026-09-25T13:44:10+08:00"
sources:
  - github_new
tags:
  - 项目
  - github_new
  - Python
  - created:>2026-09-11
lang: "en"
---

# jaredpalmer/kev

> [!info] 一句话导读
> Small Jev-like decision models you can train and run yourself.

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://github.com/jaredpalmer/kev>
> 首次收录：2026-09-25T13:44:10+08:00
> 来源渠道：GitHub 新星仓库
> 标签：Python, created:>2026-09-11
> 最新指标：stars=6796 · forks=396 · open_issues=39

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-09-24T23:59:53+08:00 | GitHub 新星仓库 | stars=6636 · forks=377 · open_issues=34 | [[20-语料/posts/github_new/2026-09-24/7f309519de9eb862_jaredpalmer-kev]] |
| 2026-09-25T13:44:10+08:00 | GitHub 新星仓库 | stars=6796 · forks=396 · open_issues=39 | [[20-语料/posts/github_new/2026-09-24/7f309519de9eb862_jaredpalmer-kev]] |

## 摘要正文

# Kev  Small Jev-like decision models you can train and run yourself.  Kev is a family of small decision models built on Qwen3.5 and Qwen3.8 and based on the architecture described in [Jev's Architecture Unmasked](https://archerhume.com/posts/jevs-architecture-unmasked). You can use the pretrained weights or train your own. The API matches TypeSafe's [System One](https://docs.typesafe.ai/api), so you can point their Python SDK at your local server.  ## Highlights  - Yes/no (`noul`), multiple-choice (`choice`) and rating (`score`) questions in one request. The questions share the text but can't read each other. - Calibrated probabilities by default: each checkpoint ships with a temperature fitted on held-out data. - Drop-in for Jev: the TypeSafe Python SDK works against a Kev server unchanged. - Four sizes, from a 0.8B that runs on a laptop to a 27B for a single data-centre GPU. - Fine-tune on your own labelled examples. A coding-agent skill runs the whole loop on Modal, from finding your questions to serving the result. - Deploy your own HTTPS endpoint with one command. It scales to zero when idle. - Try it in the browser first: [huggingface.co/spaces/jaredpalmer/kev](https://huggi…
