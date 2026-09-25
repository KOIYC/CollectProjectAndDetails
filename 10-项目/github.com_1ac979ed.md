---
type: "project"
title: "Show HN: Grev - Thinking Grep with Jev"
project_url: "https://github.com/aurorainfra/grev"
first_seen: "2026-09-25T13:42:25+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_devttyeu
  - story_49837132
  - show_hn
lang: "en"
---

# Show HN: Grev - Thinking Grep with Jev

> [!info] 一句话导读
> License: Apache License 2.0

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://github.com/aurorainfra/grev>
> 首次收录：2026-09-25T13:42:25+08:00
> 来源渠道：HN Show HN
> 标签：author_devttyeu, story_49837132, show_hn
> 最新指标：点赞=2 · 评论=1 · engagement_velocity=2

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-09-25T13:42:25+08:00 | HN Show HN | 点赞=2 · 评论=1 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-09-25/451e52c3f69ad63a_Show-HN-Grev-Thinking-Grep-with-Jev]] |

## 摘要正文

# aurorainfra/grev  Thinking coreutils  - Stars: 3 - Forks: 0 - Watchers: 3 - Open issues: 0 - License: Apache License 2.0 - Default branch: main - Created: 2026-09-24T21:12:11Z  ## Languages  - Go - Makefile - Shell  ## Top Contributors  - magik6k (10 contributions)  ---  ## README  # grev  Unix filters that ask questions instead of matching patterns.  ```console $ cat examples/menu.txt chicken tikka masala fresh fruit salad spaghetti carbonara tofu stir fry with rice  $ grev 'is a vegan meal' examples/menu.txt fresh fruit salad tofu stir fry with rice ```  The tools run on TypeSafe's Jev models, which answer typed questions with calibrated probabilities instead of generating text. That's why these tools behave like `grep`, `sort` or `cut`: **output is always your input**. Labels and scores appear only as explicit columns. A few thousand lines cost fractions of a cent and take seconds.  ## Examples  ```sh # Search logs by meaning grev --about 'nginx error log' 'says the upstream server timed out' examples/nginx-error.log journalctl -fu myapp | grev --line-buffered --about 'application log' 'shows the process crashed' git log --oneline | grev --about 'commit messages' 'fixes a bug'…
