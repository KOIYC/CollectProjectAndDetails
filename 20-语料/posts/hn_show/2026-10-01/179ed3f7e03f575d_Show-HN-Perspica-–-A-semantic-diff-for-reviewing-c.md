---
type: "corpus"
item_id: "179ed3f7e03f575d"
title: "Show HN: Perspica – A semantic diff for reviewing code"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49914005"
project_url: "https://github.com/sshah03/perspica"
author: "sshah03"
published_at: "2026-09-30T20:34:49Z"
captured_at: "2026-10-01T09:41:49+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-10-01"
pub_day: "2026-09-30"
tags:
  - 语料
  - hn_show
  - author_sshah03
  - story_49914005
  - show_hn
metrics: {"points": 6, "comments": 1, "engagement_velocity": 6}
comments_count: 1
comments_total: 1
discovered_via: "hn:show_hn:3d"
---

# Show HN: Perspica – A semantic diff for reviewing code

> [!info] 一句话导读
> I started using this a little over half a year ago to help me navigate through some large AI coded PRs people were submitting, because I felt like if I looked a…

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49914005>
> 指标：点赞=6 · 评论=1 · engagement_velocity=6
> 作者：sshah03　|　发布：2026-09-30T20:34:49Z
> 项目链接：<https://github.com/sshah03/perspica>
> 采集：2026-10-01T09:41:49+08:00　|　id：`179ed3f7e03f575d`

## 正文

I started using this a little over half a year ago to help me navigate through some large AI coded PRs people were submitting, because I felt like if I looked at the PR on Github I would just auto pass it through because I didn't want to deal with it. Thought I'd clean it up and share it in case this style of review was useful to anyone else.Obviously it relies on an LLM run to get true semantic groupings of what changes were done, and why, but can also be used without an LLM to get more mechanical groupings/group names of changes made, along with the right order to view them in. The manual tree-sitter parsed analysis is deliberately conservative for now, but if people want to avoid the LLM analysis I can spend more time on that.You can use it for other peoples PRs, or for your own when you've relied heavily on Claude Code or Codex for that particular PR. If the change came from your own Claude Code or Codex session, it reads your prompts and marks which changes you asked for and which the agent decided on its own as well to help you validate it before submitting for others to review.Demo video done on some public project PRs is in the repo; for a look at what it looks like when it pulls in information about your own claude/codex sessions you'll have to use it yourself for now, but I'll work on getting an example of that up soon so people can take a look before spending time to get this to work locally for themselves.I also added support for perforce style side by side diffing because I always kind of liked it, though it's not quite as slick yet.

## 评论（1/1）

> **sshah03** · 2026-09-30T23:38:23.000Z　
> If you're interested in using this, but your language of choice is presently unsupported, just leave a reply here with the language and I'll prioritize adding it. Also any other requests, or suggestions that would make this genuinely useful to you as well.

## 导航

- 项目页：[[10-项目/github.com_3d6a9f85]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
