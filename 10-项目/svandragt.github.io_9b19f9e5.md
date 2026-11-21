---
type: "project"
title: "Show HN: Park – save and recall work context across repos and machines"
project_url: "https://svandragt.github.io/park"
first_seen: "2026-11-21T14:45:01+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_pacifika
  - story_50583988
  - show_hn
lang: "en"
---

# Show HN: Park – save and recall work context across repos and machines

> [!info] 一句话导读
> Getting started with park

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://svandragt.github.io/park>
> 首次收录：2026-11-21T14:45:01+08:00
> 来源渠道：HN Show HN
> 标签：author_pacifika, story_50583988, show_hn
> 最新指标：点赞=4 · 评论=3 · engagement_velocity=4

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-11-21T14:45:01+08:00 | HN Show HN | 点赞=4 · 评论=3 · engagement_velocity=4 | [[20-语料/posts/hn_show/2026-11-21/d2c7ea537d04e03b_Show-HN-Park-–-save-and-recall-work-context-across]] |

## 摘要正文

P Getting started with park Save where you were, so you or your agent can pick it up later. Source on GitHub Progress 0 of 7 Step 1 · About 2 minutes Install park park is one Go binary. It keeps your parked items in a local SQLite database. Terminal Copy  $ go install github.com/svandragt/park@latest  $ command -v park  $ park version Check that command -v park points into $(go env GOPATH)/bin or your GOBIN . If another park comes earlier on your PATH , that one runs instead. Where your items live The database is at ~/.local/share/park/park.db , or under $XDG_DATA_HOME when that is set. Set PARK_DB to use another file. Trying park in a throwaway database? Unset PARK_SYNC_DIR as well as changing PARK_DB . While PARK_SYNC_DIR is set, every database you point park at reads and writes the same sync log, so test items reach your real items. Terminal Copy  $ env -u PARK_SYNC_DIR PARK_DB=/tmp/park-test.db park list Step 2 · About 3 minutes Park your first item Park the thing you are in the middle of. Write it for the person who picks it up next, who may be you in a week or an agent with no memory of today. Run this inside a git repository: Terminal Copy  $ park add --name "Fix login redir…
