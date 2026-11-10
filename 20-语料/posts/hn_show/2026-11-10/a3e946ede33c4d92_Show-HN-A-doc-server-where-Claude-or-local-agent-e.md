---
type: "corpus"
item_id: "a3e946ede33c4d92"
title: "Show HN: A doc server where Claude or local agent edits based on added comments"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50428595"
project_url: "https://smarchone.github.io/docs"
author: "smarch27"
published_at: "2026-11-09T17:26:13Z"
captured_at: "2026-11-10T09:49:42+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-11-10"
pub_day: "2026-11-09"
tags:
  - 语料
  - hn_show
  - author_smarch27
  - story_50428595
  - show_hn
metrics: {"points": 2, "comments": 1, "engagement_velocity": 2}
comments_count: 1
comments_total: 1
discovered_via: "hn:show_hn:3d"
---

# Show HN: A doc server where Claude or local agent edits based on added comments

> [!info] 一句话导读
> Comment on your docs.

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50428595>
> 指标：点赞=2 · 评论=1 · engagement_velocity=2
> 作者：smarch27　|　发布：2026-11-09T17:26:13Z
> 项目链接：<https://smarchone.github.io/docs>
> 采集：2026-11-10T09:49:42+08:00　|　id：`a3e946ede33c4d92`

## 正文

~/ smarchone/docs
Star on GitHub
Comment on your docs.
 Claude makes the edits.
tl;dr Comment on your repo's Markdown docs in the browser. Claude Code, or any local agent, edits the file and replies.
The problem
Editing a doc from the terminal means describing where the problem is: "second section, the bullet about retries…"
Then you scroll a diff to check it got the right spot.
That's a lot of attention for a one-line fix, and you lose your place in the doc.
How it works
One small daemon on your machine. Each repo's agent connects to it with a skill and a polling script.
Browser
 The editor
One tab for every repo. You read, highlight and comment. Changes stream in live.
⇄ comments
edits
Daemon
 docs serve · localhost:3459
Owns the workspaces. Stores each doc's comment threads and version history, and queues threads as jobs for that repo's agent.
repo-a/.docs threads · history · job queue
repo-b/.docs threads · history · job queue
⇄ jobs
replies
Agent, per repo
 Skill + poll.sh
Claude Code with the /collab-docs skill, or any local agent. It edits the Markdown file directly and posts replies.
The skill registers the current repo as a workspace. docs serve "$PWD" starts the daemon if needed.
The polling script waits on the daemon in the background. It's a long-poll, so an idle agent uses no tokens.
When you comment, the daemon hands the page's threads to that repo's agent and locks the page. The agent edits the file, replies, and the page unlocks.
GitHub →
See it work
Two comments on a spec. One asks for an edit, the other asks a question. You never leave the page.
Docs — specs/retries.md
skip ⏭
Claude is listening
Retries
.docs/specs/retries.md
When a request to the upstream API fails, the client should, in most cases and depending on the type of error that was returned, consider trying the request again a number of times before eventually giving up.
Backoff
Waits double after each attempt, starting at 200 ms, with a little jitter so clients don't retry in lockstep.
We give up after 5 attempts. Errors after that go to the dead-letter queue.
Comments
Get started in 1 minute
npm i -g @smarchone/docs Node 22+ copy
npx skills add smarchone/docs --skill collab-docs -g copy
/collab-docs in Claude Code, in any repo copy
Then open http://127.0.0.1:3459 and leave your first comment. Or skip the global install: npx @smarchone/docs serve
space to skip · runs on your machine, nothing leaves it

## 评论（1/1）

> **hb-dbx** · 2026-11-09T18:29:44.000Z　
> sounds pretty cool lol. feel slike it'll be useful

## 关联链接

- http://127.0.0.1:3459

## 导航

- 项目页：[[10-项目/smarchone.github.io_424409c9]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
