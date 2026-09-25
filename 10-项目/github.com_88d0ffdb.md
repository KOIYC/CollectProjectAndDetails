---
type: "project"
title: "Show HN: Laya decision engine on AWS Lambda, backed by Lambda SnapStart"
project_url: "https://github.com/HQarroum/laymbda"
first_seen: "2026-09-25T00:12:57+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_hqm_
  - story_49794281
  - show_hn
lang: "en"
---

# Show HN: Laya decision engine on AWS Lambda, backed by Lambda SnapStart

> [!info] 一句话导读
> ⚡ Laya engine on AWS Lambda, backed by Lambda SnapStart.

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://github.com/HQarroum/laymbda>
> 首次收录：2026-09-25T00:12:57+08:00
> 来源渠道：HN Show HN
> 标签：author_hqm_, story_49794281, show_hn
> 最新指标：点赞=2 · 评论=0 · engagement_velocity=2

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-09-22T12:53:31+08:00 | HN Show HN | 点赞=2 · 评论=0 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-09-22/0b7afcfc2a0a426e_Show-HN-Laya-decision-engine-on-AWS-Lambda,-backed]] |
| 2026-09-25T00:12:57+08:00 | HN Show HN | 点赞=2 · 评论=0 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-09-22/0b7afcfc2a0a426e_Show-HN-Laya-decision-engine-on-AWS-Lambda,-backed]] |

## 摘要正文

# HQarroum/laymbda  ⚡ Laya engine on AWS Lambda, backed by Lambda SnapStart.  - Stars: 4 - Forks: 1 - Watchers: 4 - Open issues: 0 - License: MIT License - Default branch: master - Created: 2026-09-19T18:14:16Z  ## Languages  - Dockerfile - Python - TypeScript  ## Topics  - ai - classification - lambda - laya - ml  ## Top Contributors  - HQarroum (6 contributions)  ---  ## README   Laymbda  ⚡ The Laya engine running on AWS Lambda.  ## What's this ❓  Laymbda is an example of how to run the Laya System-1 decision model on AWS Lambda using a CPU-only, serverless architecture. It is backed by Lambda SnapStart for container functions, which caches and restores initialized Lambda states quickly.  This project uses the AWS Cloud Development Kit (CDK) as the Infrastructure-as-Code layer, and requires Node.js, Docker, npm, and AWS credentials configured for the target account and region.  > All credit goes to the Laya project.  ## Architecture  Laymbda has no long-running servers. CDK packages the runtime as an x86-64 container image, Lambda loads Laya during initialization, and SnapStart captures the initialized process when CDK publishes a version.  ### Architectural Trade-offs  Using AWS…
