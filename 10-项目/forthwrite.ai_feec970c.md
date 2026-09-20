---
type: "project"
title: "Show HN: ForthWrite – Email AI that learns your voice from every edit you send"
project_url: "https://forthwrite.ai/blog/how-forthwrite-learns-your-email-voice"
first_seen: "2026-09-21T03:11:02+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_curtisboortz
  - story_48725623
  - show_hn
lang: "en"
---

# Show HN: ForthWrite – Email AI that learns your voice from every edit you send

> [!info] 一句话导读
> All articles Voice Matching

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://forthwrite.ai/blog/how-forthwrite-learns-your-email-voice>
> 首次收录：2026-09-21T03:11:02+08:00
> 来源渠道：HN Show HN
> 标签：author_curtisboortz, story_48725623, show_hn
> 最新指标：点赞=4 · 评论=0 · engagement_velocity=4

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-09-21T01:29:55+08:00 | HN Show HN | 点赞=4 · 评论=0 · engagement_velocity=4 | [[20-语料/posts/hn_show/2026-09-21/4ebaa9c3e91eedeb_Show-HN-ForthWrite-–-Email-AI-that-learns-your-voi]] |
| 2026-09-21T03:11:02+08:00 | HN Show HN | 点赞=4 · 评论=0 · engagement_velocity=4 | [[20-语料/posts/hn_show/2026-09-21/4ebaa9c3e91eedeb_Show-HN-ForthWrite-–-Email-AI-that-learns-your-voi]] |

## 摘要正文

All articles Voice Matching  How ForthWrite Learns Your Email Voice  How ForthWrite learns your email voice: pgvector RAG with MMR re-ranking, edit-distance scoring against what you send, and a phrasing miner.  5 min read · June 24, 2026  I've been chasing a specific problem for about a year: email assistants write a professional email, not your email. The tool produces something correct, polished, and obviously not from you. You edit it. You send it. You edit the next one. Nothing improves. Most tools don't have a feedback loop, so the model has no way to learn from the edits you make. Here's how ForthWrite closes that gap. The core problem with "learns your voice" Every AI email tool claims to learn your voice. The claim describes very different things depending on the tool. Prompt engineering means you write a system prompt describing your style. "Direct tone. No em-dashes. Under 100 words." The model follows instructions but doesn't update. You hit the same ceiling on every draft. Fine-tuning actually updates model weights on your data. It could work, but it costs significant compute per user and doesn't update dynamically as your writing evolves, which makes it impractical at …
