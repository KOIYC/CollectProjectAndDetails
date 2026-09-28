---
type: "project"
title: "Show HN: Jev-Like Model Learns to Cook"
project_url: "https://rlafuente.com/posts/2026-9-26-training-a-small-decision-model-to-cook"
first_seen: "2026-09-28T09:47:28+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_andes314
  - story_49870984
  - show_hn
lang: "en"
---

# Show HN: Jev-Like Model Learns to Cook

> [!info] 一句话导读
> Teaching a Decision Model to Cook and Cooperate

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://rlafuente.com/posts/2026-9-26-training-a-small-decision-model-to-cook>
> 首次收录：2026-09-28T09:47:28+08:00
> 来源渠道：HN Show HN
> 标签：author_andes314, story_49870984, show_hn
> 最新指标：点赞=2 · 评论=0 · engagement_velocity=2

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-09-28T09:47:28+08:00 | HN Show HN | 点赞=2 · 评论=0 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-09-28/2daaafd171a6ece1_Show-HN-Jev-Like-Model-Learns-to-Cook]] |

## 摘要正文

home |  writing |  post Teaching a Decision Model to Cook and Cooperate Published 2026-9-26 Your browser does not support embedded video. Two independently acting copies of the same decision model serve six soups in 512 ticks. Every move is a native game control. I trained a decision model to play cooperative Overcooked on one RTX 5080. Two independently acting copies learned to serve six soups in 512 ticks using only native controls. The policy is OpenJev , which applies the idea behind Jev : describe a situation, supply possible answers, and receive probabilities for them. OpenJev uses natural language inference to score whether each proposed answer follows from the context. Expressing actions as text lets the same classifier choose among different action spaces, making it a promising interface for learning through interaction. I’ve released the code and trained model . Figure 1. Greedy evaluations across the initial attempt, exploration restart, and two-chef continuation. Time starts at zero for each stage. Checkpoint 220 serves six soups. Learning from native controls Recent game demos show how much that interface can leave to the surrounding software. TypeSafe's Doom demo uses…
