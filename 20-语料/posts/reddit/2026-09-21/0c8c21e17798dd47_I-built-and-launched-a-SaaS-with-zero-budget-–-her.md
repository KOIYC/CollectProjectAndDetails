---
type: "corpus"
item_id: "0c8c21e17798dd47"
title: "I built and launched a SaaS with zero budget – here's the exact stack (and the product)"
source: "reddit"
source_name: "Reddit 独立开发版块"
url: "https://www.reddit.com/r/microsaas/comments/1tsv54w/i_built_and_launched_a_saas_with_zero_budget/"
project_url: "https://emrefkrlr.github.io/gitpulse"
author: "Secure-Musician384"
published_at: "2026-05-31T21:17:46+08:00"
captured_at: "2026-09-21T01:27:56+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-21"
pub_day: "2026-05-31"
tags:
  - 语料
  - reddit
  - r/microsaas
metrics: {"score": 3, "comments": 2, "upvote_ratio": 1}
comments_count: 0
comments_total: 0
discovered_via: "reddit:144d+settle3"
---

# I built and launched a SaaS with zero budget – here's the exact stack (and the product)

> [!info] 一句话导读
> I've been unemployed for a while. I decided to use the time to test

> [!meta]- 语料信息（点开展开）
> 来源：Reddit 独立开发版块（post）
> 原帖：<https://www.reddit.com/r/microsaas/comments/1tsv54w/i_built_and_launched_a_saas_with_zero_budget/>
> 指标：得分=3 · 评论=2 · 赞踩比=1
> 作者：Secure-Musician384　|　发布：2026-05-31T21:17:46+08:00
> 项目链接：<https://emrefkrlr.github.io/gitpulse>
> 采集：2026-09-21T01:27:56+08:00　|　id：`0c8c21e17798dd47`

## 正文

I've been unemployed for a while. I decided to use the time to test
something I'd always believed: you can build and ship a real product
with zero money.

Here's what I built, and exactly how I did it for free.

---

**The product: GitPulse**

Writing changelogs always felt like unpaid overtime. You finish the
work, then you have to sit down and translate commits into plain
language for users.

GitPulse connects to your GitHub repo via webhook. Every git push →
AI reads your commits → draft changelog created. You review, publish,
done. Public URL + embed widget included.

→ https://emrefkrlr.github.io/gitpulse

---

**The $0 stack**

| What | Tool | Cost |
|---|---|---|
| Backend | FastAPI + Python | Free |
| Frontend | HTMX + Jinja2 (no React) | Free |
| Database | Supabase (free tier) | $0 |
| Hosting | Render (free tier) | $0 |
| Auth | GitHub OAuth | Free |
| AI | Groq + DeepSeek (free/cheap tiers) | ~$0 |
| Payments | Polar.sh | Free (% per transaction) |
| Analytics | Google Analytics 4 | Free |
| Domain/Landing | GitHub Pages | Free |

Total monthly cost: $0

---

**The honest part**

This wasn't a smooth build. Render's free tier sleeps after
inactivity — caused issues with third-party URL validators.
Supabase's connection pooler required a specific asyncpg fix
(statement_cache_size=0). Polar.sh needed GitHub Pages as the
product URL because Render's cold start made their bot time out.

None of these were hard problems. They just took time to debug.

---

**What I learned**

The $0 constraint is actually useful. It forces you to pick boring,
proven tools instead of chasing shiny stacks. FastAPI + HTMX is
genuinely underrated for this kind of app.

The hard part wasn't the tech. It was shipping something real enough
to show people.

---

Pricing: Free (3/month) → $7/month → $19/month

If you've built something similar or have feedback on the product
itself, I'd genuinely like to hear it.

## 导航

- 项目页：[[10-项目/emrefkrlr.github.io_a0d4a6eb]]
- 渠道页：[[50-渠道/reddit]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
