---
type: "project"
title: "Show HN: Paper-docx – agent-native Python-docx fork with 78% fewer DOCX failures"
project_url: "https://github.com/paper-instruments/paper-docx"
first_seen: "2026-09-26T09:41:08+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_i_rush_carriers
  - story_49848598
  - show_hn
lang: "en"
---

# Show HN: Paper-docx – agent-native Python-docx fork with 78% fewer DOCX failures

> [!info] 一句话导读
> paper-instruments/paper-docx

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://github.com/paper-instruments/paper-docx>
> 首次收录：2026-09-26T09:41:08+08:00
> 来源渠道：HN Show HN
> 标签：author_i_rush_carriers, story_49848598, show_hn
> 最新指标：点赞=5 · 评论=0 · engagement_velocity=5

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-09-26T09:41:08+08:00 | HN Show HN | 点赞=5 · 评论=0 · engagement_velocity=5 | [[20-语料/posts/hn_show/2026-09-26/af65826b8911b22b_Show-HN-Paper-docx-–-agent-native-Python-docx-fork]] |

## 摘要正文

# paper-instruments/paper-docx  - Stars: 12 - Forks: 0 - Watchers: 12 - Open issues: 1 - License: Other - Default branch: main - Created: 2026-07-07T20:12:03Z  ## Languages  - Gherkin - Makefile - Python  ## Top Contributors  - scanny (193 contributions) - DKWoods (23 contributions) - ondrej-111 (13 contributions) - revossen-asml (7 contributions) - apteryks (6 contributions) - onlyjus (6 contributions) - mavwolverine (4 contributions) - eupharis (3 contributions) - musicinmybrain (2 contributions) - brnstz (1 contributions)  ---  ## README  # paper-docx  `paper-docx` is an agent-first Python library for safely inspecting, editing, reviewing, and composing existing Microsoft Word (`.docx`) documents. It is a strict-superset hard fork of `python-docx` and a drop-in replacement. The distribution is renamed; the import name stays `docx`, so existing code keeps working unchanged.  ```python import docx                       # the import name is unchanged doc = docx.Document("contract.docx") ```  ## Why it exists  `python-docx` is excellent at *creating* documents. Its lossless package layer, disciplined XML mapping, and years of absorbed edge cases are why this fork builds on it.  The …
