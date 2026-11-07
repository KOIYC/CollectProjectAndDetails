---
type: "project"
title: "Show HN: Ru-Jev – an open model that scores caller-supplied options on CPU (MIT)"
project_url: "https://huggingface.co/besktech/ru-jev"
first_seen: "2026-11-07T09:43:25+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_vladimirbesk
  - story_50395242
  - show_hn
lang: "en"
---

# Show HN: Ru-Jev – an open model that scores caller-supplied options on CPU (MIT)

> [!info] 一句话导读
> Ру-Жев (Ru-Jev) v1.3

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://huggingface.co/besktech/ru-jev>
> 首次收录：2026-11-07T09:43:25+08:00
> 来源渠道：HN Show HN
> 标签：author_vladimirbesk, story_50395242, show_hn
> 最新指标：点赞=5 · 评论=0 · engagement_velocity=5

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-11-07T09:43:25+08:00 | HN Show HN | 点赞=5 · 评论=0 · engagement_velocity=5 | [[20-语料/posts/hn_show/2026-11-07/b8dc839799967d23_Show-HN-Ru-Jev-–-an-open-model-that-scores-caller]] |

## 摘要正文

# Ру-Жев (Ru-Jev) v1.3  Do not use the standard zero-shot pipeline. The call `pipeline("zero-shot-classification", model="besktech/ru-jev")` neither fails nor works: it returns numbers drawn from a randomly initialized head, and they change on every load. Load the model with the snippet below.  Open, Russian-first typed-decision model. It does not generate text. Given a context and a set of candidate options, it returns a calibrated probability over the options and picks one. It covers three decision shapes: yes/no, choice from options, and ordinal scale. It is a compact encoder (mmBERT-base, 307M), so it runs on CPU and can be deployed inside a closed perimeter.  - Project page: https://ru-jev.besk.tech - Demo with precomputed examples: https://huggingface.co/spaces/besktech/ru-jev-demo - Training and evaluation code: https://github.com/beskvladimir-create/ru-jev  Earlier releases are kept on branches: `v1.1` and `v1`. Load one with `revision="v1.1"` if you depend on its exact behaviour.  The inference widget is switched off on purpose, and the stock pipelines do not work either. This is a backbone plus a separate scoring head, not a standard sequence-classification checkpoint. Ev…
