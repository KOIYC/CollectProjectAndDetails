---
type: "corpus"
item_id: "82463f79ae7eee80"
title: "Show HN: SlideOps – slides from a repo that flag when they drift from the code"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49508735"
project_url: "https://github.com/glukicov/slideops"
author: "lukicov"
published_at: "2026-08-31T12:15:10Z"
captured_at: "2026-09-21T02:56:42+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-21"
pub_day: "2026-08-31"
tags:
  - 语料
  - hn_show
  - author_lukicov
  - story_49508735
  - show_hn
metrics: {"points": 23, "comments": 5, "engagement_velocity": 23}
comments_count: 5
comments_total: 5
discovered_via: "hn:show_hn:52d"
---

# Show HN: SlideOps – slides from a repo that flag when they drift from the code

> [!info] 一句话导读
> I kept generating slide decks about my codebases with an agent, and weeks later they would go stale. Updating them was quite costly (time & tokens), as the agen…

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49508735>
> 指标：点赞=23 · 评论=5 · engagement_velocity=23
> 作者：lukicov　|　发布：2026-08-31T12:15:10Z
> 项目链接：<https://github.com/glukicov/slideops>
> 采集：2026-09-21T02:56:42+08:00　|　id：`82463f79ae7eee80`

## 正文

I kept generating slide decks about my codebases with an agent, and weeks later they would go stale. Updating them was quite costly (time & tokens), as the agent would have to re-scan the whole repo to re-generate the slides. So I made the slide deck carry its own provenance: SlideOps skill turns a repo into a slide deck, with all references to files carrying exact line range and a hash.Checking is done with standard-library Python: no model calls, no network, and very fast. For example, it distinguishes MOVED (the code shifted) from CHANGED (the content differs). Updating the slides costs tokens, but now the checking part has already given the agent just the relevant context on what exactly needs to be repaired.SlideOps ships as a Claude Code plugin and runs as a plain agent skill in Codex, Copilot CLI and OpenCode.Longer write-up: https://medium.com/@lukicov/your-documentation-is-a-build-ar...GitHub repo: https://github.com/glukicov/slideops

## 评论（5/5）

> **brookst** · 2026-08-31T13:48:34.000Z　
> I love this. Thanks for sharing. Would be great to generalize to documentation in general, not just slides.My LLM workflow is documentation-heavy, and that works great for getting projects off the ground and managing very large projects. But just like human-driven development, more documentation = more likelihood of being stale. Unlike humans, LLMs don’t resent time spent updating docs.So, if you’re taking feature requests, I would love to see this head towards full lifecycle documentation management. The tricky part is figuring out whether the docs or code drifted. Sometimes misalignment means the code was built wrong, sometimes it means the docs are stale and changes are intentional. A HITL model should maybe help?

---

> **boxed** · 2026-08-31T14:08:58.000Z　
> I wrote a bunch of custom tooling for iommi, I have a write up of it here: https://kodare.net/2025/08/08/documentation-that-is-never-wr...

---

> **lukicov** · 2026-08-31T16:03:50.000Z　
> Great idea on generalising this beyond just slides - v1.1 is now out with Markdown support :)This invisible citation comment (<!-- slideops data-src="app/main.py:40-58"...) is added to Markdown documents to help with tracking changes and keeping them it sync with the codebase.On the topic of generlaising to documents, for a moment I wish I named the skills "DocOps", but that's already a thing: https://www.writethedocs.org/guide/doc-ops/

---

> **lukicov** · 2026-08-31T14:47:34.000Z　
> The framing that the test suite is the documentation stuck with me: executing the examples removes the duplication rather than tracking it. Taking ideas from this, thank you!

---

> **boxed** · 2026-08-31T15:41:03.000Z　
> We did it the other way around first, but it was a huge hassle and very hacky. Since we flipped it we've been much more satisfied with the system.It's somewhat inspired by literate programming, but a bit flipped.

## 关联链接

- https://medium.com/@lukicov/your-documentation-is-a-build-ar...GitHub

## 导航

- 项目页：[[10-项目/github.com_8df92436]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
