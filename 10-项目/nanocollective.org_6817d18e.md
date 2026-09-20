---
type: "project"
title: "Show HN: Prompt-scrub – local-first PII redaction for LLM prompts and responses"
project_url: "https://nanocollective.org/blog/prompt-scrub-v100-a-local-first-scrubber-for-prompts-and-their-responses-76"
first_seen: "2026-09-21T03:11:05+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_mrspence
  - story_49124405
  - show_hn
lang: "en"
---

# Show HN: Prompt-scrub – local-first PII redaction for LLM prompts and responses

> [!info] 一句话导读
> Nano Collective Build Blog Docs Contributors Sponsor

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://nanocollective.org/blog/prompt-scrub-v100-a-local-first-scrubber-for-prompts-and-their-responses-76>
> 首次收录：2026-09-21T03:11:05+08:00
> 来源渠道：HN Show HN
> 标签：author_mrspence, story_49124405, show_hn
> 最新指标：点赞=4 · 评论=2 · engagement_velocity=4

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-09-21T01:31:46+08:00 | HN Show HN | 点赞=4 · 评论=2 · engagement_velocity=4 | [[20-语料/posts/hn_show/2026-09-21/d6ecf81eaa289a34_Show-HN-Prompt-scrub-–-local-first-PII-redaction-f]] |
| 2026-09-21T02:54:50+08:00 | HN Show HN | 点赞=4 · 评论=2 · engagement_velocity=4 | [[20-语料/posts/hn_show/2026-09-21/d6ecf81eaa289a34_Show-HN-Prompt-scrub-–-local-first-PII-redaction-f]] |
| 2026-09-21T03:11:05+08:00 | HN Show HN | 点赞=4 · 评论=2 · engagement_velocity=4 | [[20-语料/posts/hn_show/2026-09-21/d6ecf81eaa289a34_Show-HN-Prompt-scrub-–-local-first-PII-redaction-f]] |

## 摘要正文

Nano Collective Build Blog Docs Contributors Sponsor Build Blog Docs Contributors Sponsor < Back to Blogs  [ Package ] [ New Concept ] [ Released ]  prompt-scrub v1.0.0: a local-first scrubber for prompts and their responses  July 15, 2026  |  @ LottieOxford |  0 comments Built by the Nano Collective , a community collective building AI tooling not for profit, but for the community. This is the first public release of prompt-scrub , a small Node.js utility that runs entirely on your machine. It detects identifying content inside a prompt (emails, paths, secrets, phone numbers, URLs, postal addresses, and a couple of opt-in categories), replaces each finding with a stable placeholder like Email_1 or Path_2 , and lets you rehydrate the model's response back to the original values locally after it comes back. The motivation is simple: most accidental identifier leakage to a cloud LLM lives in the text of the prompt and the text of its response. Stripping it there, deterministically, before the prompt leaves your machine is a useful layer in a privacy posture, and one that does not need a network round-trip, a new account, or a hosted service to work. What it actually does The package …
