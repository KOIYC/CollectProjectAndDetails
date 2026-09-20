---
type: "corpus"
item_id: "e85bac48e3fdfe87"
title: "Show HN: TabPFN-3.5, a Tabular Foundation Model for messy real-world tables"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49715384"
project_url: "https://priorlabs.ai/technical-reports/tabpfn-3-5"
author: "onasta"
published_at: "2026-09-15T16:56:55Z"
captured_at: "2026-09-20T14:06:01+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-20"
pub_day: "2026-09-15"
tags:
  - 语料
  - hn_show
  - author_onasta
  - story_49715384
  - show_hn
metrics: {"points": 10, "comments": 1, "engagement_velocity": 10}
comments_count: 1
comments_total: 1
discovered_via: "hn:show_hn:90d"
---

# Show HN: TabPFN-3.5, a Tabular Foundation Model for messy real-world tables

> [!info] 一句话导读
> Published: 2026-09-15

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49715384>
> 指标：点赞=10 · 评论=1 · engagement_velocity=10
> 作者：onasta　|　发布：2026-09-15T16:56:55Z
> 项目链接：<https://priorlabs.ai/technical-reports/tabpfn-3-5>
> 采集：2026-09-20T14:06:01+08:00　|　id：`e85bac48e3fdfe87`

## 正文

Published: 2026-09-15

Prior Labs

# TabPFN-3.5: Technical Report

September 15, 2026 • 5 min

Today, we are releasing TabPFN-3.5, which ranks first place on both TabArena and BeyondArena. We also update Thinking mode and Plus to make use of TabPFN-3.5. For latency-sensitive applications, we’re introducing TabPFN-3.5-Fast, available in alpha.

Most machine learning assumes rows are independent, features are clean and there is enough data to train a gradient boosting tree. In reality, business data rarely fits this assumption. An insurance data table combines the claim amount with reviewer conclusions. Transactions are connected to merchants and customers. Scientific and industrial sensors collect hundreds of measurements, and data differs by location or time period.

These cases so far required encoding, extensive feature engineering and model tuning. TabPFN-3.5 improves most in these harder data regimes, and it is the most accurate and scalable tabular foundation model available today. Read the full model report.

> Zero-shot inference surpassing my carefully tuned models, consistently taking the top rank in my backtests. TabPFN proved we could move to an inference-only foundation model. Jean Pablo Fuquen, AI Engineer, Scaleway

### Benchmark results

TabArena is a living IID benchmark with 51 curated datasets and more than 27 methods, including more than 10 tabular foundation models. BeyondArena goes broader than IID, with 142 datasets containing high-dimensional, grouped, temporal, high-cardinality and text-rich data that standard benchmarks often leave out.

On TabArena, TabPFN-3.5 outperforms the previous leader. On BeyondArena, it finishes about 150 Elo points ahead of the previous overall leader.

On BeyondArena’s non-large datasets, TabPFN-3.5 leads on text-rich, high-cardinality and high-dimensional data, with up to about 250 Elo points over the strongest previous baseline. It matches the strongest baseline on grouped data. This makes TabPFN-3.5 the strongest model on real-world prediction tasks, where the incoming ERP, CRM and production data isn’t clean.

Building on the base model, TabPFN-3.5-Plus adds enhanced processing to extract signal from text-rich datasets containing product descriptions, customer reviews or internal notes. It ranks second behind TabPFN-3.5-Thinking on STRABLE, a benchmark for predictions on 108 tabular datasets with messy strings.

> On par with my ML model built over a week, in a couple of clicks. Corentin Garet, Beside

TabPFN-3.5-Thinking, our most accurate offering for when compute matters less than the result, goes even further with 44 more Elo points on TabArena and about 20 more on BeyondArena, both compared with the base TabPFN-3.5 model.

Thinking also improves on temporal and grouped data - for example, a model trained on one store may need to predict sales for other locations, or use historic records to predict sales next month. Sales performance can be different between stores and over different seasons. Thinking handles these differences well, making it a tool of choice for business-critical predictions.

> TabPFN outperforms gradient boosting on real-life insurance datasets without any tuning. And you get prediction confidence intervals, which are super useful for risk applications. Kacper Wieczorek, Lead Data Scientist, Marshmallow

For the first time, we release an alpha model version for latency-sensitive applications - TabPFN-3.5-Fast runs up to six times faster than the base model.

We document the evaluation protocol, datasets, model configurations, runtime environment and complete results in our report.

### Availability

TabPFN-3.5 model family is available today via:

- Our API ships TabPFN-3.5 Plus, Fast and Thinking, and Prior Labs MCP now uses TabPFN-3.5 Plus as well. From 15 September until 29 September 2026, all API and MCP users get a 50% reduction from the standard TabPFN-3.5 token rates for the 3.5 family. Standard rates resume on 29 September.
- SAP customers can access TabPFN-3.5 Plus through SAP AI Core.
- TabPFN-3.5 Plus and Thinking are available on AWS Sagemaker. Availability on Microsoft Azure ML will follow shortly.
- Open-source `tabpfn` package ships the base model and Fast checkpoint.

# COLMAP browser workspace

## 评论（1/1）

> **onasta** · 2026-09-15T16:56:55.000Z　
> I'm excited to announce the release of our new Tabular Foundation Model TabPFN-3.5!It improves a lot on standard tabular prediction problems (rank 1 by far [TabArena](https://github.com/autogluon/tabarena) and much faster than the competing models, 98% win rate against a well tuned XGBoost). But most importantly it really improves on the messy real-world data we've seen across industries. Be it non-i.i.d. data with temporal or grouped splits, tables with strings, text and images, high-cardinality categorical features, or wide tables with many features, we're also state of the art. Inside our harness, it's also the best model to predict on relational data, outperforming specific graph-based models.Would love to hear how it performs on your own data!

## 导航

- 项目页：[[10-项目/priorlabs.ai_8e64d255]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
