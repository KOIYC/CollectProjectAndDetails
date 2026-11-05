---
type: "project"
title: "I built an AI cold email agent that pauses itself the second a prospect replies. Here’s the architecture problem that took longer than expected"
project_url: "https://www.reddit.com/r/microsaas/comments/1xf6yrl/i_built_an_ai_cold_email_agent_that_pauses_itself/"
first_seen: "2026-11-05T11:22:40+08:00"
sources:
  - reddit
tags:
  - 项目
  - reddit
  - r/microsaas
lang: "en"
---

# I built an AI cold email agent that pauses itself the second a prospect replies. Here’s the architecture problem that took longer than expected

> [!info] 一句话导读
> Been building an outreach tool called Agentra and wanted to share the part that actually turned out to be hard, because it’s not what I expected going in

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://www.reddit.com/r/microsaas/comments/1xf6yrl/i_built_an_ai_cold_email_agent_that_pauses_itself/>
> 首次收录：2026-11-05T11:22:40+08:00
> 来源渠道：Reddit 独立开发版块
> 标签：r/microsaas
> 最新指标：得分=3 · 评论=3 · 赞踩比=1

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-11-05T11:22:40+08:00 | Reddit 独立开发版块 | 得分=3 · 评论=3 · 赞踩比=1 | [[20-语料/posts/reddit/2026-11-05/fa80ae4819b36711_I-built-an-AI-cold-email-agent-that-pauses-itself]] |

## 摘要正文

Been building an outreach tool called Agentra and wanted to share the part that actually turned out to be hard, because it’s not what I expected going in  Everyone building an AI email tool focuses on generation quality, making the copy sound less robotic, personalizing it per prospect, picking the right tone. That part is genuinely the easy 80 percent now. Any decent model handles it fine with a reasonable prompt.  The hard part is the execution loop, specifically reply detection and sequence pausing. Here’s why this is more annoying than it sounds  You’re polling or watching a Gmail inbox for replies tied to a specific sequence you sent. Straightforward until you hit the edge cases. Auto-replies and out of office messages look like replies but aren’t, so if you pause on every message that lands in the thread, you end up pausing on vacation responders and your sequence just dies silently. You have to actually classify intent, not just detect activity.  Then there’s timing. If someone replies 10 minutes after step 2 goes out but step 3 is already queued and about to fire, you need a hard check immediately before send, not just a check at sequence creation time. I missed this early …
