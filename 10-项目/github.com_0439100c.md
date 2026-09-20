---
type: "project"
title: "Your prompt system has no tests, and that is why you cannot tell it is broken"
project_url: "https://github.com/Latifox/find-me-saas"
first_seen: "2026-09-20T14:17:39+08:00"
sources:
  - devto
tags:
  - 项目
  - devto
  - ai
  - claude
  - saas
  - indiehackers
lang: "en"
---

# Your prompt system has no tests, and that is why you cannot tell it is broken

> [!info] 一句话导读
> Tags:** `ai`, `python`, `testing`, `showdev`

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://github.com/Latifox/find-me-saas>
> 首次收录：2026-09-20T14:17:39+08:00
> 来源渠道：dev.to
> 标签：ai, claude, saas, indiehackers
> 最新指标：reactions=7 · 评论=6 · reading_time=5

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-09-20T02:36:45+08:00 | dev.to | reactions=7 · 评论=6 · reading_time=5 | [[20-语料/posts/devto/2026-09-20/3e5342740e2e60b0_Your-prompt-system-has-no-tests,-and-that-is-why-y]] |
| 2026-09-20T02:41:46+08:00 | dev.to | reactions=7 · 评论=6 · reading_time=5 | [[20-语料/posts/devto/2026-09-20/3e5342740e2e60b0_Your-prompt-system-has-no-tests,-and-that-is-why-y]] |
| 2026-09-20T02:58:10+08:00 | dev.to | reactions=7 · 评论=6 · reading_time=5 | [[20-语料/posts/devto/2026-09-20/3e5342740e2e60b0_Your-prompt-system-has-no-tests,-and-that-is-why-y]] |
| 2026-09-20T03:07:27+08:00 | dev.to | reactions=7 · 评论=6 · reading_time=5 | [[20-语料/posts/devto/2026-09-20/3e5342740e2e60b0_Your-prompt-system-has-no-tests,-and-that-is-why-y]] |
| 2026-09-20T03:19:58+08:00 | dev.to | reactions=7 · 评论=6 · reading_time=5 | [[20-语料/posts/devto/2026-09-20/3e5342740e2e60b0_Your-prompt-system-has-no-tests,-and-that-is-why-y]] |
| 2026-09-20T03:31:43+08:00 | dev.to | reactions=7 · 评论=6 · reading_time=5 | [[20-语料/posts/devto/2026-09-20/3e5342740e2e60b0_Your-prompt-system-has-no-tests,-and-that-is-why-y]] |
| 2026-09-20T03:38:15+08:00 | dev.to | reactions=7 · 评论=6 · reading_time=5 | [[20-语料/posts/devto/2026-09-20/3e5342740e2e60b0_Your-prompt-system-has-no-tests,-and-that-is-why-y]] |
| 2026-09-20T03:41:18+08:00 | dev.to | reactions=7 · 评论=6 · reading_time=5 | [[20-语料/posts/devto/2026-09-20/3e5342740e2e60b0_Your-prompt-system-has-no-tests,-and-that-is-why-y]] |
| 2026-09-20T09:50:00+08:00 | dev.to | reactions=7 · 评论=6 · reading_time=5 | [[20-语料/posts/devto/2026-09-20/3e5342740e2e60b0_Your-prompt-system-has-no-tests,-and-that-is-why-y]] |
| 2026-09-20T14:17:39+08:00 | dev.to | reactions=7 · 评论=6 · reading_time=5 | [[20-语料/posts/devto/2026-09-20/3e5342740e2e60b0_Your-prompt-system-has-no-tests,-and-that-is-why-y]] |

## 摘要正文

**Tags:** `ai`, `python`, `testing`, `showdev`  ---  Code fails loudly. A prompt system fails in silence, and it fails while still producing something that looks completely fine.  ![Image description](https://dev-to-uploads.s3.us-east-2.amazonaws.com/uploads/articles/merhvzz69gsfuk3nxx4m.png)  I found this out the slow way. I had built a multi-skill agent system: 15 skills, nine commands, each one writing structured JSON that the next one reads. It worked for weeks. Then it did not, and I could not tell you when it stopped, because nothing ever threw. A skill quietly stopped writing one field. The next skill read a null and carried on. The final score came out a few points off, in a document that read exactly as convincing as it had the week before.  Plausible output is the one thing these models are never bad at. That is precisely the problem.  ## What a test even means here  You cannot assert on the prose. Run the same prompt twice and you get different words, and that is fine, because the words are not the contract. Something else is.  Three things turned out to be testable, and together they catch nearly everything:  **The arithmetic.** My system scores six weighted dimensions …
