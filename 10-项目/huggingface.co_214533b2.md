---
type: "project"
title: "Show HN: Swift-Qwen3.8-27B, -58.3% thinking, x1.95 speed, accuracy of xhigh"
project_url: "https://huggingface.co/ukisai/Swift-Qwen3.8-27b"
first_seen: "2026-09-20T14:04:11+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_kisjovan
  - story_49727511
  - show_hn
lang: "en"
---

# Show HN: Swift-Qwen3.8-27B, -58.3% thinking, x1.95 speed, accuracy of xhigh

> [!info] 一句话导读
> Swift-Qwen3.8-27B is UkisAI's reasoning-efficient derivative of Qwen3.8-27B, using 58.3% fewer thinking tokens while maintaining near-identical performance (<1%…

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://huggingface.co/ukisai/Swift-Qwen3.8-27b>
> 首次收录：2026-09-20T14:04:11+08:00
> 来源渠道：HN Show HN
> 标签：author_kisjovan, story_49727511, show_hn
> 最新指标：点赞=29 · 评论=17 · engagement_velocity=29

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-09-20T09:23:24+08:00 | HN Show HN | 点赞=29 · 评论=17 · engagement_velocity=29 | [[20-语料/posts/hn_show/2026-09-20/d8969a388d578536_Show-HN-Swift-Qwen3.8-27B,-58.3%-thinking,-x1.95-s]] |
| 2026-09-20T09:37:02+08:00 | HN Show HN | 点赞=29 · 评论=17 · engagement_velocity=29 | [[20-语料/posts/hn_show/2026-09-20/d8969a388d578536_Show-HN-Swift-Qwen3.8-27B,-58.3%-thinking,-x1.95-s]] |
| 2026-09-20T14:04:11+08:00 | HN Show HN | 点赞=29 · 评论=17 · engagement_velocity=29 | [[20-语料/posts/hn_show/2026-09-20/d8969a388d578536_Show-HN-Swift-Qwen3.8-27B,-58.3%-thinking,-x1.95-s]] |

## 摘要正文

# Swift-Qwen3.8-27B  Swift-Qwen3.8-27B is UkisAI's reasoning-efficient derivative of Qwen3.8-27B, using 58.3% fewer thinking tokens while maintaining near-identical performance (<1% loss) and as a result getting a x1.95 speed-up on several tasks.  The prompt is a sample from LiveCodeBench v6  ## Training approach  We built Swift by identifying reasoning-marker tokens that, in our analysis, trigger overthinking in Qwen’s reasoning rollouts. We then fine-tuned Qwen by penalizing usage of those tokens while it reasons.  Swift produces shorter reasoning traces. In our testing, we also observe fewer overthinking errors.  For maximum gains, Swift also includes a transfer component derived from BottleCap AI's ThinkingCap-Qwen3.6-27B.  ## Evaluation scope  > All results below compare the Qwen3.8-27B BF16 base with the same base plus the Swift adapter.  ## Benchmarks  | Benchmark | Score | | Mean tokens | | | Median tokens | | --- | --- | --- | --- | --- | --- | --- | | | Base | Swift | Base | Swift | Reduction | Reduction | | General reasoning | | | | | | | | GPQA-Diamond | 88.38% | 88.28% | 15,014 | 8,855 | ↓ 41.0% | ↓ 58.3% | | MMLU-Pro | 85.47% | 84.95% | 2,980 | 1,603 | ↓ 46.2% | ↓ 28.…
