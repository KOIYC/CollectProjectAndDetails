---
type: "project"
title: "Show HN: I have trained 15 blood glucose forecasting models on my own data"
project_url: "https://github.com/0xdeadf1sh/T1DMAI"
first_seen: "2026-11-11T13:37:17+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_0xdeadf1sh
  - story_50444761
  - show_hn
lang: "en"
---

# Show HN: I have trained 15 blood glucose forecasting models on my own data

> [!info] 一句话导读
> A model zoo of blood glucose forecasters trained & tested on my own data

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://github.com/0xdeadf1sh/T1DMAI>
> 首次收录：2026-11-11T13:37:17+08:00
> 来源渠道：HN Show HN
> 标签：author_0xdeadf1sh, story_50444761, show_hn
> 最新指标：点赞=15 · 评论=3 · engagement_velocity=15

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-11-11T13:37:17+08:00 | HN Show HN | 点赞=15 · 评论=3 · engagement_velocity=15 | [[20-语料/posts/hn_show/2026-11-11/186608be2c7b11ea_Show-HN-I-have-trained-15-blood-glucose-forecastin]] |

## 摘要正文

# 0xdeadf1sh/T1DMAI  A model zoo of blood glucose forecasters trained & tested on my own data  - Stars: 17 - Forks: 2 - Watchers: 17 - Open issues: 0 - License: MIT License - Default branch: main - Created: 2026-07-29T05:07:53Z  ## Languages  - Python - Rust - Shell  ## Topics  - blood-glucose - blood-glucose-forecasting - blood-glucose-prediction - deep-learning - diabetes - t1dm - time-series - transformers - type-1-diabetes - xgboost  ## Top Contributors  - 0xdeadf1sh (216 contributions)  ---  ## README  # T1DMAI  > [!NOTE] > Most of the code in this repo was written by AI. If you don't like that, feel free to leave.  This repo is a zoo. Here I train & test many blood glucose forecasting models (including my own) on both my own data and metabonet (public).  My model is a small transformer that forecasts blood glucose 2 hours ahead. I've made two variants: D16 DILATE and D16 MSE which use DILATE and MSE loss for training, respectively. D16 refers to the width of the model (16). They are both trained on synthetic traces, and then a LoRA adapter is added for light fine-tuning, but I also test them without the adapter.  Feast thine eyes on some of their forecasts (these have been tr…
