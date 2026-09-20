---
type: "project"
title: "Show HN: Rampart on CoreML"
project_url: "https://github.com/narner/Rampart-CoreML"
first_seen: "2026-09-21T02:53:02+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_narner
  - story_48733651
  - show_hn
lang: "en"
---

# Show HN: Rampart on CoreML

> [!info] 一句话导读
> narner/Rampart-CoreML

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://github.com/narner/Rampart-CoreML>
> 首次收录：2026-09-21T02:53:02+08:00
> 来源渠道：HN Show HN
> 标签：author_narner, story_48733651, show_hn
> 最新指标：点赞=6 · 评论=2 · engagement_velocity=6

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-09-21T01:29:55+08:00 | HN Show HN | 点赞=6 · 评论=2 · engagement_velocity=6 | [[20-语料/posts/hn_show/2026-09-21/3ef5339edcc3dfef_Show-HN-Rampart-on-CoreML]] |
| 2026-09-21T01:44:24+08:00 | HN Show HN | 点赞=6 · 评论=2 · engagement_velocity=6 | [[20-语料/posts/hn_show/2026-09-21/3ef5339edcc3dfef_Show-HN-Rampart-on-CoreML]] |
| 2026-09-21T02:53:02+08:00 | HN Show HN | 点赞=6 · 评论=2 · engagement_velocity=6 | [[20-语料/posts/hn_show/2026-09-21/3ef5339edcc3dfef_Show-HN-Rampart-on-CoreML]] |

## 摘要正文

# narner/Rampart-CoreML  - Stars: 9 - Forks: 0 - Watchers: 9 - Open issues: 0 - License: Creative Commons Attribution 4.0 International - Default branch: main - Created: 2026-06-30T01:14:07Z  ## Languages  - Python - Shell - Swift  ## Top Contributors  - narner (1 contributions)  ---  ## README  # Rampart Core ML  Core ML conversion and Swift package for `nationaldesignstudio/rampart`, a local PII token-classification model.  License: CC BY 4.0. See NOTICE.md for upstream Rampart model attribution and a summary of local changes.  ## Demo  https://github.com/user-attachments/assets/4e7a2f9f-d8e6-4724-88f3-6030480bea7a  ## Model Artifacts  The model is published as a GitHub Release asset instead of committed to Git. Swift package users can let the package download and cache it on first use:  ```swift let classifier = try await RampartCoreMLClassifier.downloaded() ```  For repo-local workflows, download the same Core ML package, vocabulary, and config files before running the full test suite:  ```sh scripts/download_model.sh ```  This writes:  ```text artifacts/RampartTokenClassifier.mlpackage artifacts/rampart-hf/vocab.txt artifacts/rampart-hf/config.json ```  These files are ignored…
