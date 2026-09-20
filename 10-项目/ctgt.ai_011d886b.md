---
type: "project"
title: "Show HN: Distilling DeepSeek into GPT-OSS doesn't transfer censorship. Try it"
project_url: "https://ctgt.ai/research/distillation-censorship-transfer"
first_seen: "2026-09-21T02:55:38+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_cgorlla
  - story_49113599
  - show_hn
lang: "en"
---

# Show HN: Distilling DeepSeek into GPT-OSS doesn't transfer censorship. Try it

> [!info] 一句话导读
> We recently used DeepSeek V4 Flash as a teacher for finance tasks with GPT-OSS-120B. Distillation works well on this problem. At a constrained 8k token budget, …

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://ctgt.ai/research/distillation-censorship-transfer>
> 首次收录：2026-09-21T02:55:38+08:00
> 来源渠道：HN Show HN
> 标签：author_cgorlla, story_49113599, show_hn
> 最新指标：点赞=170 · 评论=73 · engagement_velocity=170

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-09-21T01:31:46+08:00 | HN Show HN | 点赞=170 · 评论=73 · engagement_velocity=170 | [[20-语料/posts/hn_show/2026-09-21/3a54db8694cfde34_Show-HN-Distilling-DeepSeek-into-GPT-OSS-doesn't-t]] |
| 2026-09-21T02:55:38+08:00 | HN Show HN | 点赞=170 · 评论=73 · engagement_velocity=170 | [[20-语料/posts/hn_show/2026-09-21/3a54db8694cfde34_Show-HN-Distilling-DeepSeek-into-GPT-OSS-doesn't-t]] |

## 摘要正文

We recently used DeepSeek V4 Flash as a teacher for finance tasks with GPT-OSS-120B. Distillation works well on this problem. At a constrained 8k token budget, our self-distilled 120B scores 83.61% on FinanceReasoning, above Kimi K3 (81.93%) and Inkling (65.13%). We released the 20B open weights. With V4 as the teacher though, we realized it would be timely to measure if the censorship characteristic of it transferred to the distilled version of the base model. tl;dr it didn't, the teacher answered politically sensitive questions 7 SDs differently than expected, but the distilled model's behavior remained the same as its American base. You can try a couple queries yourself with no auth here: http://playground.ctgt.ai/I will now dive in to the motivation, methodology and detailed results for those interested. The hard part of measuring this phenomena is isolating whether a model is reluctant to talk about sensitive things generally vs. a particular country's sensitive things. So we made 152 matched pairs where one prompt asked about a Chinese concept, and the other asked about a non-Chinese version of that concept. For example, the Great Leap Forward vs. the Holodomor. These were sc…
