---
type: "project"
title: "Show HN: Respawn – an undo button for AI agents (Rust, local-first, no cloud)"
project_url: "https://github.com/savageAZfck/respawn"
first_seen: "2026-09-20T09:36:44+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_savag3AZfckk
  - story_49747632
  - show_hn
lang: "en"
---

# Show HN: Respawn – an undo button for AI agents (Rust, local-first, no cloud)

> [!info] 一句话导读
> Default branch: main

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://github.com/savageAZfck/respawn>
> 首次收录：2026-09-20T09:36:44+08:00
> 来源渠道：HN Show HN
> 标签：author_savag3AZfckk, story_49747632, show_hn
> 最新指标：点赞=2 · 评论=0 · engagement_velocity=2

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-09-20T09:23:24+08:00 | HN Show HN | 点赞=2 · 评论=0 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-09-20/ac073067a9c74f0a_Show-HN-Respawn-–-an-undo-button-for-AI-agents-(Ru]] |
| 2026-09-20T09:36:44+08:00 | HN Show HN | 点赞=2 · 评论=0 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-09-20/ac073067a9c74f0a_Show-HN-Respawn-–-an-undo-button-for-AI-agents-(Ru]] |

## 摘要正文

# savageAZfck/respawn  - Stars: 2 - Forks: 0 - Watchers: 2 - Open issues: 0 - License: Other - Default branch: main - Created: 2026-09-15T02:25:16Z  ## Languages  - Rust  ## Top Contributors  - savageAZfck (10 contributions)  ---  ## README  # respawn  > **Status: beta.** Format and CLI may change between minor versions. The > integrity guarantees below are implemented and tested; there has been no > external security audit.  **Undo as infrastructure.** respawn versions the state of a directory tree as a content-addressed snapshot graph — every file's content lives in the store (content-defined chunks via FastCDC), so any snapshot can be materialized back exactly. Reverting is a HEAD pointer swap plus atomic per-file writes. Drift is a manifest diff. Machines replicate snapshots over the LAN — plaintext or Noise-encrypted — with no server.  Built for the agent era: snapshot the world before an autonomous process touches it, revert when it goes wrong, and prove afterward what changed.  ``` respawn init            # create .respawn/ in the worktree respawn snap -m "v1"    # content-addressed snapshot respawn snap --apfs     # point-in-time cut via APFS (macOS ≤15, root or --ask-admin…
