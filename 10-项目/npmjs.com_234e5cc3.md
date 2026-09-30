---
type: "project"
title: "Show HN: Mdq (jq for Markdown) CLI to parse, extract, update Markdown files"
project_url: "https://npmjs.com/package/mdq-cli"
first_seen: "2026-09-30T18:57:07+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_davert
  - story_49901671
  - show_hn
lang: "en"
---

# Show HN: Mdq (jq for Markdown) CLI to parse, extract, update Markdown files

> [!info] 一句话导读
> Query and edit markdown with a selector language - jq, for markdown

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://npmjs.com/package/mdq-cli>
> 首次收录：2026-09-30T18:57:07+08:00
> 来源渠道：HN Show HN
> 标签：author_davert, story_49901671, show_hn
> 最新指标：点赞=2 · 评论=0 · engagement_velocity=2

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-09-30T18:28:30+08:00 | HN Show HN | 点赞=2 · 评论=0 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-09-30/9f49a3bcdfe6516f_Show-HN-Mdq-(jq-for-Markdown)-CLI-to-parse,-extrac]] |
| 2026-09-30T18:57:07+08:00 | HN Show HN | 点赞=2 · 评论=0 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-09-30/9f49a3bcdfe6516f_Show-HN-Mdq-(jq-for-Markdown)-CLI-to-parse,-extrac]] |

## 摘要正文

# mdq-cli  Query and edit markdown with a selector language - jq, for markdown  - Version: 0.1.2 - License: MIT - Homepage: https://github.com/testomatio/explorbot#readme - Repository: git+https://github.com/testomatio/explorbot.git - Weekly downloads: 115 - Dependents: 0 - Created: 2026-09-28T23:12:59.021Z - Updated: 2026-09-29T22:03:49.748Z  ## Keywords  - markdown - query - selector - cli - jq - frontmatter - marked - edit  ## Dependencies  | Package | Version | | --- | --- | | commander | ^14.0.1 | | marked | ^16.2.0 | | yaml | ^2.8.3 |  ## Version History  | Version | Published | Deps | | --- | --- | --- | | 0.1.0 | 2026-09-28T23:12:59.369Z | 3 | | 0.1.1 | 2026-09-29T00:40:19.765Z | 3 | | 0.1.2 | 2026-09-29T22:03:49.432Z | 3 |  ---  ## README  # mdq  Query, validate, extract, and update structured Markdown with a selector language. Like `jq` for Markdown.  ## Usage examples  ```bash npx mdq-cli 'section("Overview")' generated.md                                      # validate npx mdq-cli 'section("API") table' --json README.md                                 # extract npx mdq-cli 'section("Tasks") list' --add-item 'Review docs' --in-place plan.md      # update ```  ### Validat…
