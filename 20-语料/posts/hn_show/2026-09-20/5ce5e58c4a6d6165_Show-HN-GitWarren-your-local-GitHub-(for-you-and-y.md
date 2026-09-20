---
type: "corpus"
item_id: "5ce5e58c4a6d6165"
title: "Show HN: GitWarren - your local GitHub (for you and your agents)"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49711890"
project_url: "https://gitwarren.com/"
author: "xfor"
published_at: "2026-09-15T13:00:21Z"
captured_at: "2026-09-20T14:06:40+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-20"
pub_day: "2026-09-15"
tags:
  - 语料
  - hn_show
  - author_xfor
  - story_49711890
  - show_hn
metrics: {"points": 4, "comments": 2, "engagement_velocity": 4}
comments_count: 2
comments_total: 2
discovered_via: "hn:show_hn:90d"
---

# Show HN: GitWarren - your local GitHub (for you and your agents)

> [!info] 一句话导读
> GitWarren — review what your agents wrote, before GitHub ever sees it

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49711890>
> 指标：点赞=4 · 评论=2 · engagement_velocity=4
> 作者：xfor　|　发布：2026-09-15T13:00:21Z
> 项目链接：<https://gitwarren.com/>
> 采集：2026-09-20T14:06:40+08:00　|　id：`5ce5e58c4a6d6165`

## 正文

GitWarren — review what your agents wrote, before GitHub ever sees it

# Review what your agents wrote, before GitHub ever sees it.

An agent finishes a task and leaves you a worktree full of changes that aren't committed yet. Every other review tool waits for a pull request. GitWarren reads the worktree directly — staged, unstaged and untracked — so you read the diff on your own machine first.

v0.1.5 · Apple silicon and Intel · Windows and Linux too

or `brew install --cask klarluft/tap/gitwarren`

## An agent's output isn't a commit. It's a dirty worktree.

That is the gap. By the time work has been committed, pushed and opened as a pull request, you have already accepted its shape — and the moment when a correction was cheap has passed. GitWarren finds the worktree where the branch is checked out, wherever it happens to live on disk, and folds its staged, unstaged and untracked files into one diff you can read and comment on.

A file the agent created and never added to git — reviewed, and commented on, before it was ever a commit.

## Your agents take part in the review — they aren't just the subject of it.

GitWarren ships an MCP server over stdio. Point Claude Code, Codex or any MCP client at it and it gets the same seventeen tools the app itself uses: open a review, read the whole discussion, reply in a thread, leave a comment on a line, resolve one. Ask an agent to explain its own diff, or to answer the question you left on line 40 — in the review, where the answer stays.

An agent’s comment and the reply, in one thread — attributed, and never mistakable for a person.

### Always attributed

A machine-written comment is always marked as one, and the tool's name comes from the MCP handshake rather than from whatever the model decides to call itself that day.

### Two agents stay two

Each MCP session is given its own id, so two agents working at the same time are told apart in the thread without either having to cooperate.

### Yours to edit

You can edit or delete anything in a review. An agent is held to its own messages — it can fix its own typo, not quietly rewrite yours.

### No account

Nothing to sign up for and nothing to sign in to. GitWarren is one person's app, on one machine, with no notion of anybody else.

### Nothing cached

Every branch name, commit and diff on screen is read from git at the moment it is shown — so nothing can quietly go stale behind your back.

### One SQLite file

Your reviews and comments live in a single file in your application-data directory. Delete it and GitWarren is gone. Your repositories are untouched.

# VectisPDF — Editor PDF Premium, 100% Privado y Sin Servidores

## 评论（2/2）

> **xfor** · 2026-09-15T13:00:21.000Z　
> If you ever felt like you want to have a GitHub code review experience without pushing the code to GitHub you may want to look at GitWarren.More and more of my work is leveraged by agents orchestrated on my computers and when working for companies where I can't just push unreviewed agent's work to GitHub, I was really looking for a way to nicely iterate on the PR locally (I'm freelance programmer for corporations of all sizes). I checked existing solutions and they were missing some things, so I built my own app that has:- threads of comments (not just a single comment)- support for images (both in git diff and in comments so your agents can push and pull images/screenshots)- general discussion on the PR- agents can discuss changes between themselves (maybe you ask one agent to review other agent's work)- you can comment files not related to the change- you can see uncommitted changes so you can make a review before anything gets committed- there's mcp/desktop app/cli and webUI so you can choose what you like- it works with tailnet and ssh (GitWarren talks to other instances on your machines)- you can make a review on your phoneand the most important- you can really feel like on GitHub without pushing to GitHubAll this is free and open source. Take a look and leave your feedback - I'm currently pushing an update every day, as I discover more things each day I work with it as my personal code review tool.

---

> **melezhik** · 2026-09-19T18:22:07.000Z　
> > I can't just push unreviewed agent's work to GitHubStill not sure why is that? If you push to some PRs branch, not main branch. The very idea of PR - is one may review the one before merge. Why should I take another review before push to PR branch ?

## 导航

- 项目页：[[10-项目/gitwarren.com_d7a73e91]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
