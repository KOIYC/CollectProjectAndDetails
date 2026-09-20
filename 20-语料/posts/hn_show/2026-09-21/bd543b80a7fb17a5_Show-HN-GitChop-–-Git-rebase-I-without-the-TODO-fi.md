---
type: "corpus"
item_id: "bd543b80a7fb17a5"
title: "Show HN: GitChop – Git rebase -I without the TODO file"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=47949019"
project_url: "https://bendansby.com/apps/gitchop.html"
author: "webwielder2"
published_at: "2026-04-29T14:33:38Z"
captured_at: "2026-09-21T02:52:36+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-21"
pub_day: "2026-04-29"
tags:
  - 语料
  - hn_show
  - author_webwielder2
  - story_47949019
  - show_hn
metrics: {"points": 3, "comments": 1, "engagement_velocity": 3}
comments_count: 1
comments_total: 1
discovered_via: "hn:show_hn:174d"
---

# Show HN: GitChop – Git rebase -I without the TODO file

> [!info] 一句话导读
> git rebase -i that doesn't drop you into a terminal. Drag-reorder commits, split one commit into many by assigning hunks, reword in place. Native Mac, no server…

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=47949019>
> 指标：点赞=3 · 评论=1 · engagement_velocity=3
> 作者：webwielder2　|　发布：2026-04-29T14:33:38Z
> 项目链接：<https://bendansby.com/apps/gitchop.html>
> 采集：2026-09-21T02:52:36+08:00　|　id：`bd543b80a7fb17a5`

## 正文

All Apps
/
 GitChop
Docs
GitChop
git rebase -i that doesn't drop you into a terminal. Drag-reorder commits, split one commit into many by assigning hunks, reword in place. Native Mac, no servers.
Download — it’s free
Source on GitHub
See what it does
What it does
✂
Split a commit
The killer feature. Mark a commit edit , drag its hunks into named buckets, hit Apply. Each bucket becomes its own commit. The terminal-only edit → --continue dance, done as a UI.
↕
Drag to reorder
Pick up any commit, drop it where it should go. Squash and fixup attach to the row above and absorb count badges show how many follow-ups will fold in.
✎
Reword in place
Click the verb chip and pick Reword. A modal opens with the full message preloaded — edit subject and body, save. Applied during rebase via $GIT_EDITOR wiring; no editor pop-ups.
The verbs you know. pick , edit , squash , fixup , drop , reword — all visible as colored chips in the commit list. Click to change, drag to reorder.
Conflict pause that doesn't kick you out. When git stops on a conflict, GitChop stays open with a list of unmerged files. Open each in your editor, resolve, click Continue. Or Skip the commit, or Abort the whole rebase — all without leaving the app.
Backup ref every Apply. Before rewriting any history, GitChop writes refs/gitchop-backup/ pointing at the pre-rebase HEAD. Failed rebase rolls back automatically; manual recovery is one git update-ref away.
Custom rebase base. Right-click any commit → Use as base . Everything newer becomes the editable plan; the chosen commit is the foundation. Equivalent to git rebase -i  from the terminal.
Mid-rebase reorder. Paused on a conflict? The remaining commits still in the queue show up alongside — drag to reorder before clicking Continue, and git picks up the new sequence.
Real diff pane. Click any commit to see its full diff with structural color, word-wrap, and line numbers. Same shape as the diff git will see at apply time.
Multi-repo tabs. Open several repos at once; each gets its own tab with persistent state. ⌘O to add, ⌘W to close.
Sane defaults. Loads the last 12 commits by default; pick 25 / 50 / 100 / All from the count menu. Author and relative-age ( 3d , 2w ) per row so you can find the right slice quickly.
Native, fast, no services. Pure Swift. Shells out to your installed git for full upstream-fidelity behavior. Tiny binary, instant launch.
Screenshots
Get GitChop
Notarized, signed, and gatekeeper-friendly. No account, no telemetry.
Download — it’s free
Support
Questions, bug reports, or feature requests? Email
 ben.dansby@gmail.com
 and you’ll get a reply, usually within a day or two.
For how-to documentation, see the
 GitChop documentation .
Made on a Mac.
© 2026 Ben Dansby

## 评论（1/1）

> **immccc** · 2026-04-29T15:36:00.000Z　
> What's the main difference with other visual git tools or, for example, IDE integration like in any Jetbrains product?

## 导航

- 项目页：[[10-项目/bendansby.com_a0c69be7]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
