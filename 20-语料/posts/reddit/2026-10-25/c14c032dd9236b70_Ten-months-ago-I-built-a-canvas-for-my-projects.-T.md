---
type: "corpus"
item_id: "c14c032dd9236b70"
title: "Ten months ago I built a canvas for my projects. This week it started writing its own history, in Git"
source: "reddit"
source_name: "Reddit 独立开发版块"
url: "https://www.reddit.com/r/selfhosted/comments/1x6n34p/ten_months_ago_i_built_a_canvas_for_my_projects/"
project_url: "https://github.com/3xpyth0n/ideon"
author: "Constant-Drive9727"
published_at: "2026-10-15T22:26:28+08:00"
captured_at: "2026-10-25T23:28:44+08:00"
lang: "en"
kind: "post"
topic: AI 工具/Agent
shard: "2026-10-25"
pub_day: "2026-10-15"
tags:
  - 语料
  - reddit
  - r/selfhosted
  - Release (No AI)
metrics: {"score": 3, "comments": 11, "upvote_ratio": 0.5652173913043478}
comments_count: 11
comments_total: 11
discovered_via: "reddit:14d+settle10"
---

# Ten months ago I built a canvas for my projects. This week it started writing its own history, in Git

> [!info] 一句话导读
> For the ones who followed along: 640 stars now, up from 100 when I first posted here. Still the same messy solo side project, but v1.0 changed what it can do.

> [!meta]- 语料信息（点开展开）
> 来源：Reddit 独立开发版块（post）
> 原帖：<https://www.reddit.com/r/selfhosted/comments/1x6n34p/ten_months_ago_i_built_a_canvas_for_my_projects/>
> 指标：得分=3 · 评论=11 · 赞踩比=0.5652173913043478
> 作者：Constant-Drive9727　|　发布：2026-10-15T22:26:28+08:00
> 项目链接：<https://github.com/3xpyth0n/ideon>
> 采集：2026-10-25T23:28:44+08:00　|　id：`c14c032dd9236b70`

## 正文

Hi everyone,

For the ones who followed along: 640 stars now, up from 100 when I first posted here. Still the same messy solo side project, but v1.0 changed what it can do.

The short version of why it exists: I keep losing the thread when I walk away from a project. Notes in one app, configs in another, no big picture. So I built a canvas where all of it connects. That part you know.

What's new in v1.0 is the part I'm proudest of: the canvas is now a Git artifact. A project syncs to a repo, structure, notes and block positions version-controlled inside a .ideon/ directory with checksums. The rest of your repo stays untouched. You edit the canvas, you push, and the history sits in Git like code. Diffs, reviews, rollback. Not my cloud, your repo.

Also in 1.0: database block with typed columns, mermaid with live rendering, and a chained audit trail so every state change is traceable.

What's next: a plugin API so people can build their own block types, and a desktop app once the project grows enough to justify it.

The long-term idea is the canvas stopping being a map and becoming a system. A graph that remembers everything and eventually reacts on its own, (from just blocks to neurons 👀).

Still two containers, app + Postgres, one docker-compose up

Repo: [https://github.com/3xpyth0n/ideon](https://github.com/3xpyth0n/ideon)

Hope it's useful for your own labs :D

## 评论（11/11）

> **asimovs-auditor**（1 分） · 2026-10-15T22:26:37+08:00　
> Expand the replies to this comment to learn how AI was used in this post/project.

---

> **Constant-Drive9727**（2 分） · 2026-10-15T22:28:55+08:00　
> No AI was used, for the post or the project. I'm French, I wrote this in French and translated it myself. The code is hand-written.

---

> **Ok-Junket-4565**（-4 分） · 2026-10-16T01:32:45+08:00　
> i like how clean the dark ui looks with the mermaid block sitting right there not buried in a menu somewhere

---

> **fernandops**（1 分） · 2026-10-16T07:03:15+08:00　
> How does it handle two people editing the same canvas on separate branches? Moving a block and editing its note should ideally merge without making someone resolve a huge position diff. A small example PR with a conflict and its resolution would tell me more about the Git workflow than a clean push.

---

> **thatboyonabike**（2 分） · 2026-10-16T12:33:43+08:00　
> This is a bot.

---

> **Joncallim**（1 分） · 2026-10-16T15:27:22+08:00　
> Can you restore the canvas and attached files from the repo alone, or would you need a database backup too? A short restore example would be helpful.

---

> **Constant-Drive9727**（2 分） · 2026-10-16T15:32:09+08:00　
> You can restore the canvas from the repo, there are three options: Git wins, Ideon wins, or Manual where you check the diff yourself. If you want to restore, from the repo, you select the Git wins option and the repo state overwrites the current canvas state.

---

> **Constant-Drive9727**（2 分） · 2026-10-16T16:42:29+08:00　
> Ideon syncs to a single configured branch, not across arbitrary branches. Both users pull from and push to the same branch. Conflicts are resolved by the merge mode you pick (ideon-wins, git-wins, or manual). The "separate branches with a conflict PR" scenario isn't the intended workflow

---

> **Joncallim**（1 分） · 2026-10-21T09:07:28+08:00　
> Thanks, that clears up the canvas part. Are uploaded attachments included in the repo too, or do those still need a separate backup? Just checking what would be needed to restore onto a completely fresh instance.

---

> **Constant-Drive9727**（1 分） · 2026-10-21T15:05:04+08:00　
> Attachments are in the repo too, stored under \`.ideon/uploads/\`, and included in the bundle manifest (manifest.files). If you restore the repo, the canvas and all attached files come back. I’ve ensured that absolutely all data within a canvas can be tracked in Git.

---

> **Joncallim**（1 分） · 2026-10-24T10:16:21+08:00　
> Ah good, that was the missing bit. Thanks for following up. Having the attachments in the same restore makes this much easier to reason about.

## 导航

- 项目页：[[10-项目/github.com_81b7ebcf]]
- 渠道页：[[50-渠道/reddit]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
