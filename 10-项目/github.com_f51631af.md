---
type: "project"
title: "Show HN: Nv – workspace orchestrator for jj built for parallel agent workflows"
project_url: "https://github.com/eersnington/jj-navi"
first_seen: "2026-09-21T02:52:31+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_Sreenington
  - story_47955188
  - show_hn
lang: "en"
---

# Show HN: Nv – workspace orchestrator for jj built for parallel agent workflows

> [!info] 一句话导读
> jj-navi is workspace orchestrator for Jujutsu (jj), built for parallel human and AI agentic workflows

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://github.com/eersnington/jj-navi>
> 首次收录：2026-09-21T02:52:31+08:00
> 来源渠道：HN Show HN
> 标签：author_Sreenington, story_47955188, show_hn
> 最新指标：点赞=2 · 评论=0 · engagement_velocity=2

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-09-21T01:09:14+08:00 | HN Show HN | 点赞=2 · 评论=0 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-09-21/97f23b1258d85ead_Show-HN-Nv-–-workspace-orchestrator-for-jj-built-f]] |
| 2026-09-21T01:13:42+08:00 | HN Show HN | 点赞=2 · 评论=0 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-09-21/97f23b1258d85ead_Show-HN-Nv-–-workspace-orchestrator-for-jj-built-f]] |
| 2026-09-21T02:52:31+08:00 | HN Show HN | 点赞=2 · 评论=0 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-09-21/97f23b1258d85ead_Show-HN-Nv-–-workspace-orchestrator-for-jj-built-f]] |

## 摘要正文

# eersnington/jj-navi  jj-navi is workspace orchestrator for Jujutsu (jj), built for parallel human and AI agentic workflows  - Stars: 24 - Forks: 2 - Watchers: 24 - Open issues: 3 - License: MIT License - Homepage: https://git.new/jj-navi - Default branch: main - Created: 2026-03-09T22:12:42Z  ## Languages  - JavaScript - Rust  ## Top Contributors  - eersnington (107 contributions) - github-actions[bot] (7 contributions)  ---  ## README  # jj-navi  Workspace management for Jujutsu, built for parallel human and AI agent workflows.  ## The problem  jj workspaces are great for parallel work, but the workflow around it is quite cumbersome:  - **Paths are unmanaged.** `jj workspace add ../name` works, but paths are arbitrary and easy to forget. - **Cross-workspace visibility is stale.** jj snapshots the current workspace when you run a command, but not the others. So `jj log` from one workspace can show outdated commits for the rest — files on disk exist, but jj hasn't recorded them yet. - **Cleanup is awkward.** Forgetting a workspace does not delete its directory, and deleting a directory does not forget the workspace. There is also no guard against removing the one you are currently…
