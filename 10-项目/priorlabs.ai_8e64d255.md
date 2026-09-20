---
type: "project"
title: "Show HN: TabPFN-3.5, a Tabular Foundation Model for messy real-world tables"
project_url: "https://priorlabs.ai/technical-reports/tabpfn-3-5"
first_seen: "2026-09-20T14:06:01+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_onasta
  - story_49715384
  - show_hn
lang: "en"
---

# Show HN: TabPFN-3.5, a Tabular Foundation Model for messy real-world tables

> [!info] 一句话导读
> Published: 2026-09-15

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://priorlabs.ai/technical-reports/tabpfn-3-5>
> 首次收录：2026-09-20T14:06:01+08:00
> 来源渠道：HN Show HN
> 标签：author_onasta, story_49715384, show_hn
> 最新指标：点赞=10 · 评论=1 · engagement_velocity=10

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-09-20T09:23:24+08:00 | HN Show HN | 点赞=10 · 评论=1 · engagement_velocity=10 | [[20-语料/posts/hn_show/2026-09-20/e85bac48e3fdfe87_Show-HN-TabPFN-3.5,-a-Tabular-Foundation-Model-for]] |
| 2026-09-20T09:37:10+08:00 | HN Show HN | 点赞=10 · 评论=1 · engagement_velocity=10 | [[20-语料/posts/hn_show/2026-09-20/e85bac48e3fdfe87_Show-HN-TabPFN-3.5,-a-Tabular-Foundation-Model-for]] |
| 2026-09-20T14:06:01+08:00 | HN Show HN | 点赞=10 · 评论=1 · engagement_velocity=10 | [[20-语料/posts/hn_show/2026-09-20/e85bac48e3fdfe87_Show-HN-TabPFN-3.5,-a-Tabular-Foundation-Model-for]] |

## 摘要正文

Published: 2026-09-15  Prior Labs  # TabPFN-3.5: Technical Report  September 15, 2026 • 5 min  Today, we are releasing TabPFN-3.5, which ranks first place on both TabArena and BeyondArena. We also update Thinking mode and Plus to make use of TabPFN-3.5. For latency-sensitive applications, we’re introducing TabPFN-3.5-Fast, available in alpha.  Most machine learning assumes rows are independent, features are clean and there is enough data to train a gradient boosting tree. In reality, business data rarely fits this assumption. An insurance data table combines the claim amount with reviewer conclusions. Transactions are connected to merchants and customers. Scientific and industrial sensors collect hundreds of measurements, and data differs by location or time period.  These cases so far required encoding, extensive feature engineering and model tuning. TabPFN-3.5 improves most in these harder data regimes, and it is the most accurate and scalable tabular foundation model available today. Read the full model report.  > Zero-shot inference surpassing my carefully tuned models, consistently taking the top rank in my backtests. TabPFN proved we could move to an inference-only foundation…
