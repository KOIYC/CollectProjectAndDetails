---
type: "project"
title: "Show HN: Token compression CLI to save Codex/Astra costs"
project_url: "https://github.com/spenmcke/compress"
first_seen: "2026-10-01T09:41:49+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_yolandac
  - story_49911910
  - show_hn
lang: "en"
---

# Show HN: Token compression CLI to save Codex/Astra costs

> [!info] 一句话导读
> Hey HN! Yolanda and Spencer here - wanted to share a token compression tool that we’ve built for ourselves to save 30% costs on codex!After maxing out sub and b…

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://github.com/spenmcke/compress>
> 首次收录：2026-10-01T09:41:49+08:00
> 来源渠道：HN Show HN
> 标签：author_yolandac, story_49911910, show_hn
> 最新指标：点赞=8 · 评论=4 · engagement_velocity=8

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-09-30T18:28:30+08:00 | HN Show HN | 点赞=3 · 评论=1 · engagement_velocity=3 | [[20-语料/posts/hn_show/2026-09-30/d010214e5e0cad1e_Show-HN-Free-token-compression-CLI,-saves-codex-bi]] |
| 2026-09-30T18:57:07+08:00 | HN Show HN | 点赞=3 · 评论=1 · engagement_velocity=3 | [[20-语料/posts/hn_show/2026-09-30/d010214e5e0cad1e_Show-HN-Free-token-compression-CLI,-saves-codex-bi]] |
| 2026-09-30T18:57:42+08:00 | HN Show HN | 点赞=3 · 评论=1 · engagement_velocity=3 | [[20-语料/posts/hn_show/2026-09-30/d010214e5e0cad1e_Show-HN-Free-token-compression-CLI,-saves-codex-bi]] |
| 2026-10-01T09:41:49+08:00 | HN Show HN | 点赞=8 · 评论=4 · engagement_velocity=8 | [[20-语料/posts/hn_show/2026-10-01/963b0d4913aa2e10_Show-HN-Token-compression-CLI-to-save-Codex-Astra]] |

## 摘要正文

Hey HN! Yolanda and Spencer here - wanted to share a token compression tool that we’ve built for ourselves to save 30% costs on codex!After maxing out sub and burning $700/day per person on api, we fine tuned a compression model to trim codex's tool call output to reduce input token + cache. It cut down tokens by 29.6% and now I just leave it on by default in Codex.To avoid messing up w/ cache, we use proxy + fine tuned qwen model trained on preserving agent trajectory to remove tool call results before they go back to the model, leaving kv cache untouched.The cli is free for everyone to use (https://github.com/spenmcke/compress). Just lmk ur feedback and hacks to shave even more costs on astra! If you want to integrate it into your product to offer the best models at low cost, I can set you up with an sdk and api keysPS: It’s built for coding agents, not conversational agents. I optimized it for file retrieval accuracy, trajectory preservation, and quality to get up to 30% cost reduction depending on how context-heavy the task is.On security and privacy side, it's a proxy wrapping your local codex and ZDR so it doesn't retain any queries. It’s on by default in codex and when you d…
