---
type: "corpus"
item_id: "963b0d4913aa2e10"
title: "Show HN: Token compression CLI to save Codex/Astra costs"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49911910"
project_url: "https://github.com/spenmcke/compress"
author: "yolandac"
published_at: "2026-09-30T17:30:54Z"
captured_at: "2026-10-01T09:41:49+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-10-01"
pub_day: "2026-09-30"
tags:
  - 语料
  - hn_show
  - author_yolandac
  - story_49911910
  - show_hn
metrics: {"points": 8, "comments": 4, "engagement_velocity": 8}
comments_count: 4
comments_total: 4
discovered_via: "hn:show_hn:3d"
---

# Show HN: Token compression CLI to save Codex/Astra costs

> [!info] 一句话导读
> Hey HN! Yolanda and Spencer here - wanted to share a token compression tool that we’ve built for ourselves to save 30% costs on codex!After maxing out sub and b…

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49911910>
> 指标：点赞=8 · 评论=4 · engagement_velocity=8
> 作者：yolandac　|　发布：2026-09-30T17:30:54Z
> 项目链接：<https://github.com/spenmcke/compress>
> 采集：2026-10-01T09:41:49+08:00　|　id：`963b0d4913aa2e10`

## 正文

Hey HN! Yolanda and Spencer here - wanted to share a token compression tool that we’ve built for ourselves to save 30% costs on codex!After maxing out sub and burning $700/day per person on api, we fine tuned a compression model to trim codex's tool call output to reduce input token + cache. It cut down tokens by 29.6% and now I just leave it on by default in Codex.To avoid messing up w/ cache, we use proxy + fine tuned qwen model trained on preserving agent trajectory to remove tool call results before they go back to the model, leaving kv cache untouched.The cli is free for everyone to use (https://github.com/spenmcke/compress). Just lmk ur feedback and hacks to shave even more costs on astra! If you want to integrate it into your product to offer the best models at low cost, I can set you up with an sdk and api keysPS: It’s built for coding agents, not conversational agents. I optimized it for file retrieval accuracy, trajectory preservation, and quality to get up to 30% cost reduction depending on how context-heavy the task is.On security and privacy side, it's a proxy wrapping your local codex and ZDR so it doesn't retain any queries. It’s on by default in codex and when you don’t want compression, you can use `codex --uncompress` to disable it.Give it a try: code is in https://github.com/spenmcke/compressYou can install the cli using`curl -fsSL https://install.everestagi.com/install.sh | sh && source ~/.config/everest/shell.sh`Love to hear any feedback and learn your hacky ways to save token costs too!

## 评论（4/4）

> **stdl1b** · 2026-09-30T17:47:55.000Z　
> how did you measure it's 30% saving?

---

> **michaelastreiko** · 2026-09-30T17:50:55.000Z　
> Practical angle I like: a checkable token cut beats another flashy demo. For a small team, predictable spend on coding agents matters more than peak hype.

---

> **yolandac** · 2026-09-30T17:52:38.000Z　
> we're a proxy so could count the tokens using openai response.usage

---

> **yolandac** · 2026-09-30T17:56:01.000Z　
> it gets addictive to run the `savings` command to see tokens saved

## 关联链接

- https://github.com/spenmcke/compressYou
- https://install.everestagi.com/install.sh

## 导航

- 项目页：[[10-项目/github.com_cb151dfa]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
