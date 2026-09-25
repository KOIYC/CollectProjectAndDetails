---
type: "project"
title: "Show HN: Canary (YC) – Independent verification for AI code"
project_url: "https://runcanary.ai/"
first_seen: "2026-09-25T13:42:25+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_Visweshyc
  - story_49836632
  - show_hn
lang: "en"
---

# Show HN: Canary (YC) – Independent verification for AI code

> [!info] 一句话导读
> Hey HN, we are Aakash and Viswesh and we are building Canary (https://www.runcanary.ai/) - independent verification for AI code. Claude/Codex calls Canary with …

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://runcanary.ai/>
> 首次收录：2026-09-25T13:42:25+08:00
> 来源渠道：HN Show HN
> 标签：author_Visweshyc, story_49836632, show_hn
> 最新指标：点赞=5 · 评论=0 · engagement_velocity=5

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-09-25T13:42:25+08:00 | HN Show HN | 点赞=5 · 评论=0 · engagement_velocity=5 | [[20-语料/posts/hn_show/2026-09-25/e329c8bb9108b2a5_Show-HN-Canary-(YC)-–-Independent-verification-for]] |

## 摘要正文

Hey HN, we are Aakash and Viswesh and we are building Canary (https://www.runcanary.ai/) - independent verification for AI code. Claude/Codex calls Canary with the changesets, intended behaviour and team knowledge. Canary then deploys agent swarms to investigate potential failures and test suspected runtime bugs in remote sandboxes.To try it on your repository, paste this into your coding agent: Install the Canary CLI with npm i -g @runcanary/cli,  then run canary skills and follow its instructions  to onboard this repository.  Verification starts with what software is supposed to do and most importantly what it must never allow. This means investigating how inputs, permissions, state, timing, dependencies etc interact with each other. Intent is not always fully declared as well but many expectations are clear: private files should stay private, credentials should not leak, and retries should not create unintended duplicate effects.We believe the future is a unified and independent verification system that starts with all those expectations and then chooses how to investigate each suspected failure. Source-only code reviews catches static issues in the implementation but even a cle…
