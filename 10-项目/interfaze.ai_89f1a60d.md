---
type: "project"
title: "Show HN: A new benchmark for testing LLMs for deterministic outputs"
project_url: "https://interfaze.ai/blog/introducing-structured-output-benchmark"
first_seen: "2026-09-21T01:41:43+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_khurdula
  - story_47950283
  - show_hn
lang: "en"
---

# Show HN: A new benchmark for testing LLMs for deterministic outputs

> [!info] 一句话导读
> When building workflows that rely on LLMs, we commonly use structured output for programmatic use cases like converting an invoice into rows or meeting transcri…

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://interfaze.ai/blog/introducing-structured-output-benchmark>
> 首次收录：2026-09-21T01:41:43+08:00
> 来源渠道：HN Show HN
> 标签：author_khurdula, story_47950283, show_hn
> 最新指标：点赞=60 · 评论=30 · engagement_velocity=60

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-09-21T01:09:14+08:00 | HN Show HN | 点赞=60 · 评论=30 · engagement_velocity=60 | [[20-语料/posts/hn_show/2026-09-21/5059e747dd53b092_Show-HN-A-new-benchmark-for-testing-LLMs-for-deter]] |
| 2026-09-21T01:13:42+08:00 | HN Show HN | 点赞=60 · 评论=30 · engagement_velocity=60 | [[20-语料/posts/hn_show/2026-09-21/5059e747dd53b092_Show-HN-A-new-benchmark-for-testing-LLMs-for-deter]] |
| 2026-09-21T01:41:43+08:00 | HN Show HN | 点赞=60 · 评论=30 · engagement_velocity=60 | [[20-语料/posts/hn_show/2026-09-21/5059e747dd53b092_Show-HN-A-new-benchmark-for-testing-LLMs-for-deter]] |

## 摘要正文

When building workflows that rely on LLMs, we commonly use structured output for programmatic use cases like converting an invoice into rows or meeting transcripts into tickets or even complex PDFs into database entries.The model may return the schema you want, but with hallucinated values like `invoice_date` being off by 2 months or the transcript array ordered wrongly. The JSON is valid, but the values are not.Structured output today is a big part of using LLMs, especially when building deterministic workflows.Current structured output benchmarks (e.g., JSONSchemaBench) only validate the pass rate for JSON schema and types, and not the actual values within the produced JSON.So we designed the Structured Output Benchmark (SOB) that fixes this by measuring both the JSON schema pass rate, types, and the value accuracy across all three modalities, text, image, and audio.For our test set, every record is paired with a JSON Schema and a ground-truth answer that was verified against the source context manually by a human and an LLM cross-check, so a missing or hallucinated value will be considered to be wrong.Open source is doing pretty well with GLM 4.7 coming in number 2 right after G…
