---
type: "project"
title: "Show HN: Detect and mask PII, payment data and secrets in logs for Go"
project_url: "https://github.com/nao1215/embargo"
first_seen: "2026-11-20T09:45:52+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_nchika
  - story_50560084
  - show_hn
lang: "en"
---

# Show HN: Detect and mask PII, payment data and secrets in logs for Go

> [!info] 一句话导读
> Detect and mask personal data, payment data and secrets in text and logs for Go. Zero dependencies, cross-platform.

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://github.com/nao1215/embargo>
> 首次收录：2026-11-20T09:45:52+08:00
> 来源渠道：HN Show HN
> 标签：author_nchika, story_50560084, show_hn
> 最新指标：点赞=2 · 评论=1 · engagement_velocity=2

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-11-20T09:45:52+08:00 | HN Show HN | 点赞=2 · 评论=1 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-11-20/40e67faed9597c5c_Show-HN-Detect-and-mask-PII,-payment-data-and-secr]] |

## 摘要正文

# nao1215/embargo  Detect and mask personal data, payment data and secrets in text and logs for Go. Zero dependencies, cross-platform.  - Stars: 2 - Forks: 0 - Watchers: 2 - Open issues: 0 - License: MIT License - Default branch: main - Created: 2026-02-08T03:32:46Z  ## Languages  - Go - Makefile - Python  ## Topics  - data-masking - go - golang - logging - pii - redaction - secrets - security - sensitive-data - zero-dependency  ## Top Contributors  - nao1215 (65 contributions) - dependabot[bot] (4 contributions)  ---  ## README  # embargo  All Contributors  Go Reference MultiPlatformUnitTest reviewdog Gosec Trivy Coverage OpenSSF Scorecard  embargo detects and masks sensitive text in Go programs, logs and test output.  - Mask card numbers and emails before logs leave your service. - Check in tests that an HTTP handler or child process never writes a secret. - Scan support messages and imported files for personal data. - Detect Japanese phone numbers and My Number, including full-width digits.  ## Quick start  These examples use the unreleased API on main (Go 1.26.11 or later).  ```sh go get github.com/nao1215/embargo@main ```  ```go package main  import ( 	"fmt"  	"github.com/nao1…
