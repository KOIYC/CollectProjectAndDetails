---
type: "project"
title: "Show HN: Perspica – A semantic diff for reviewing code"
project_url: "https://github.com/sshah03/perspica"
first_seen: "2026-10-01T09:41:49+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_sshah03
  - story_49914005
  - show_hn
lang: "en"
---

# Show HN: Perspica – A semantic diff for reviewing code

> [!info] 一句话导读
> I started using this a little over half a year ago to help me navigate through some large AI coded PRs people were submitting, because I felt like if I looked a…

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://github.com/sshah03/perspica>
> 首次收录：2026-10-01T09:41:49+08:00
> 来源渠道：HN Show HN
> 标签：author_sshah03, story_49914005, show_hn
> 最新指标：点赞=6 · 评论=1 · engagement_velocity=6

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-10-01T09:41:49+08:00 | HN Show HN | 点赞=6 · 评论=1 · engagement_velocity=6 | [[20-语料/posts/hn_show/2026-10-01/179ed3f7e03f575d_Show-HN-Perspica-–-A-semantic-diff-for-reviewing-c]] |

## 摘要正文

I started using this a little over half a year ago to help me navigate through some large AI coded PRs people were submitting, because I felt like if I looked at the PR on Github I would just auto pass it through because I didn't want to deal with it. Thought I'd clean it up and share it in case this style of review was useful to anyone else.Obviously it relies on an LLM run to get true semantic groupings of what changes were done, and why, but can also be used without an LLM to get more mechanical groupings/group names of changes made, along with the right order to view them in. The manual tree-sitter parsed analysis is deliberately conservative for now, but if people want to avoid the LLM analysis I can spend more time on that.You can use it for other peoples PRs, or for your own when you've relied heavily on Claude Code or Codex for that particular PR. If the change came from your own Claude Code or Codex session, it reads your prompts and marks which changes you asked for and which the agent decided on its own as well to help you validate it before submitting for others to review.Demo video done on some public project PRs is in the repo; for a look at what it looks like when it…
