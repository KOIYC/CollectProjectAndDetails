---
type: "project"
title: "开源一个 Agent 长期记忆系统：262k 多跳 48.3%，高于 CAR 论文报告的 41%"
project_url: "https://arxiv.org/abs/2507.05257"
first_seen: "2026-11-21T14:55:12+08:00"
sources:
  - v2ex
tags:
  - 项目
  - v2ex
  - 17
lang: "zh"
---

# 开源一个 Agent 长期记忆系统：262k 多跳 48.3%，高于 CAR 论文报告的 41%

> [!info] 一句话导读
> 项目地址：https://github.com/jing-ying-dev/whale-ying-memory

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://arxiv.org/abs/2507.05257>
> 首次收录：2026-11-21T14:55:12+08:00
> 来源渠道：V2EX
> 标签：17
> 最新指标：回复=0

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-11-21T14:55:12+08:00 | V2EX | 回复=0 | [[20-语料/posts/v2ex/2026-11-21/5968c0b6d0cdf9e8_开源一个-Agent-长期记忆系统-262k-多跳-48.3%,高于-CAR-论文报告的-41%]] |

## 摘要正文

项目地址：https://github.com/jing-ying-dev/whale-ying-memory  大家好，我今年 21 岁，是一本中医学大三学生，没有计算机或 AI 专业背景。2026 年 10 月 14 日开始研究 API，10 月 22 日转向 Agent 长期记忆，11 月 18–19 日跑出了现在这组结果。  项目叫 WhaleYing Memory，Apache-2.0 开源。Whale 一方面来自 DeepSeek 的鲸鱼形象，一方面是“深海记忆”的意象；Ying 是我的名字。  我想解决的不是单纯“从文本块里搜相似内容”，而是三个更具体的问题：  同一事实出现多个版本时，Agent 能不能知道哪个已经被取代；  长上下文里，能不能避免检索到旧值；  一个答案需要串联多个事实时，能不能逐跳找齐证据再回答。  全部开发、抽取、检索和测评都在一台无独显轻薄本上完成：Windows 11、i5-13420H、16GB 内存。  先放结果  指标是 MemoryAgentBench · Conflict_Resolution 的 substring exact match，不是 LLM judge；这些 MemoryAgentBench 跑次的作答 temperature 为 0.7。  单跳（FactConsolidation-SH）   - 262k：**93.2%**（gpt-4o-mini，5 次均值）——论文基线 GPT-4o 60 · BM25 56 · gpt-4o-mini 45 - 262k：**93.0%**（DeepSeek，关思考，单次） - 262k：**92.0%**（本地 Qwen2.5-Coder 7B，单次） - 6k：**98%**（DeepSeek，关思考，单次）  多跳（FactConsolidation-MH）   - 262k：**48.3%**（DeepSeek，关思考，3 次均值）——CAR 对照 BM25 3 · HippoRAG-v2 5 · Mem0 2 · MemGPT 3 · CAR(gpt-4o) 41 - 262k：**25.3%**（gpt-4o-mini，3 次均值）——CAR(gpt-4o-mini) 27 - 6k：**66% substring / 65% exact**（DeepSeek，关思考，单次）  这里最值得注意的是：单跳换三个作答模型都在 92%–93%，但多跳换作答模型会从 25.3% 变成 48.3%。我的判断是，单跳的主要瓶颈在“记忆有没有找对”，多跳还额外依赖作答模型组合证据的能力。  和直接读全文对照  同为 262k：  单跳：DeepSeek 直接读全文 64%…
