---
type: "project"
title: "Show HN: Review agent changes locally before pushing"
project_url: "https://github.com/marcparadise/reviewer"
first_seen: "2026-09-20T09:37:07+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_GrinningFool
  - story_49721156
  - show_hn
lang: "en"
---

# Show HN: Review agent changes locally before pushing

> [!info] 一句话导读
> marcparadise/reviewer

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://github.com/marcparadise/reviewer>
> 首次收录：2026-09-20T09:37:07+08:00
> 来源渠道：HN Show HN
> 标签：author_GrinningFool, story_49721156, show_hn
> 最新指标：点赞=2 · 评论=0 · engagement_velocity=2

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-09-20T09:23:24+08:00 | HN Show HN | 点赞=2 · 评论=0 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-09-20/9b5c0ed172872385_Show-HN-Review-agent-changes-locally-before-pushin]] |
| 2026-09-20T09:37:07+08:00 | HN Show HN | 点赞=2 · 评论=0 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-09-20/9b5c0ed172872385_Show-HN-Review-agent-changes-locally-before-pushin]] |

## 摘要正文

# marcparadise/reviewer  - Stars: 2 - Forks: 0 - Watchers: 2 - Open issues: 0 - License: GNU Affero General Public License v3.0 - Default branch: main - Created: 2026-09-14T04:22:52Z  ## Languages  - CSS - Go - HTML - JavaScript  ## Top Contributors  - marcparadise (1 contributions)  ---  ## README  This document written and maintained by a human.  # reviewer  `reviewer` is a small self-hosted code review tool and light-weight workflow for reviewing agent-generated changes locally.  Somewhere around the thousandth time you give your agent permission to continue working, something slips through: an architectural choice that isn't what you meant, an object that's getting bloated, or some weird backwards-compatibility code gymnastics the agent applies to an internal-only implementation. Taking a step back to view the entirety of the changes -- instead of just as scroll-by approval blobs in the harness -- often makes it easier to catch issues.  This tool helps by allowing you to perform a local review (similar to GitHub PRs), and annotate the code with comments for your agents to address. Once you approve the changes, you or the agent can push the branch to your normal upstream such as…
