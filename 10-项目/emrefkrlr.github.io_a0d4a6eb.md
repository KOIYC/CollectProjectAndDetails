---
type: "project"
title: "I built and launched a SaaS with zero budget – here's the exact stack (and the product)"
project_url: "https://emrefkrlr.github.io/gitpulse"
first_seen: "2026-09-21T01:27:56+08:00"
sources:
  - reddit
tags:
  - 项目
  - reddit
  - r/microsaas
lang: "en"
---

# I built and launched a SaaS with zero budget – here's the exact stack (and the product)

> [!info] 一句话导读
> I've been unemployed for a while. I decided to use the time to test

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://emrefkrlr.github.io/gitpulse>
> 首次收录：2026-09-21T01:27:56+08:00
> 来源渠道：Reddit 独立开发版块
> 标签：r/microsaas
> 最新指标：得分=3 · 评论=2 · 赞踩比=1

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-09-21T01:27:56+08:00 | Reddit 独立开发版块 | 得分=3 · 评论=2 · 赞踩比=1 | [[20-语料/posts/reddit/2026-09-21/0c8c21e17798dd47_I-built-and-launched-a-SaaS-with-zero-budget-–-her]] |

## 摘要正文

I've been unemployed for a while. I decided to use the time to test something I'd always believed: you can build and ship a real product with zero money.  Here's what I built, and exactly how I did it for free.  ---  **The product: GitPulse**  Writing changelogs always felt like unpaid overtime. You finish the work, then you have to sit down and translate commits into plain language for users.  GitPulse connects to your GitHub repo via webhook. Every git push → AI reads your commits → draft changelog created. You review, publish, done. Public URL + embed widget included.  → https://emrefkrlr.github.io/gitpulse  ---  **The $0 stack**  | What | Tool | Cost | |---|---|---| | Backend | FastAPI + Python | Free | | Frontend | HTMX + Jinja2 (no React) | Free | | Database | Supabase (free tier) | $0 | | Hosting | Render (free tier) | $0 | | Auth | GitHub OAuth | Free | | AI | Groq + DeepSeek (free/cheap tiers) | ~$0 | | Payments | Polar.sh | Free (% per transaction) | | Analytics | Google Analytics 4 | Free | | Domain/Landing | GitHub Pages | Free |  Total monthly cost: $0  ---  **The honest part**  This wasn't a smooth build. Render's free tier sleeps after inactivity — caused issues with…
