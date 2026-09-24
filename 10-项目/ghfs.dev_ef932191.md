---
type: "project"
title: "Show HN: ghfs – A read-only FUSE filesystem that keeps GitHub issues on disk"
project_url: "https://ghfs.dev/"
first_seen: "2026-09-22T12:53:31+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_ghfs_dev
  - story_49796385
  - show_hn
lang: "en"
---

# Show HN: ghfs – A read-only FUSE filesystem that keeps GitHub issues on disk

> [!info] 一句话导读
> already has the issue.

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://ghfs.dev/>
> 首次收录：2026-09-22T12:53:31+08:00
> 来源渠道：HN Show HN
> 标签：author_ghfs_dev, story_49796385, show_hn
> 最新指标：点赞=2 · 评论=0 · engagement_velocity=2

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-09-22T12:53:31+08:00 | HN Show HN | 点赞=2 · 评论=0 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-09-22/57a62205c18ea861_Show-HN-ghfs-–-A-read-only-FUSE-filesystem-that-ke]] |

## 摘要正文

gh fs Story Benchmarks Download Releases Developer Tool Your coding agent already has the issue. ghfs keeps your GitHub Issues on disk as read-only files, fetched before the agent starts.  No tool call in the middle of a task, no copy-paste,  no guessing at gh flags. macOS / Linux Windows (WSL 2) Windows (Native) Copy $ curl -fsSL https://ghfs.dev/install.sh | sh Run inside your WSL 2 terminal: $ curl -fsSL https://ghfs.dev/install.sh | sh Native Windows support is on the  roadmap .  Use WSL 2 to get started today. Install free Watch the 30-second demo macOS (Apple Silicon, 26 or later, with macFUSE 5.4.0) and Linux. Free for one repository. Demo ghfs, in 30 seconds An illustration of the workflow, not a screen recording. The file layout and format are what ghfs writes. Before / After The fetch moves out of the task. Before You start a task. The agent reaches for gh issue view , gets a flag wrong, retries, and finally pastes the whole issue into the conversation. Later in the same task it needs the comments again, and fetches them again. After The issue is already at .ghfs/github/issues/open/42.md . The agent opens it the way it opens any other file, greps across the open ones, and…
