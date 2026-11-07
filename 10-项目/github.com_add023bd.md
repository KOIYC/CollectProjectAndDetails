---
type: "project"
title: "Show HN: Agents infer Lego mechanisms from sources, then animate them"
project_url: "https://github.com/anteloc/ldraw-mecha/tree/v0.5.0"
first_seen: "2026-11-07T09:43:25+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_antelocnova
  - story_50397325
  - show_hn
lang: "en"
---

# Show HN: Agents infer Lego mechanisms from sources, then animate them

> [!info] 一句话导读
> Hi there :)Around a month ago, I released LDraw Nova, an agentic toolset for assembling LEGO CAD models by generating LDraw source code files.For more details, …

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://github.com/anteloc/ldraw-mecha/tree/v0.5.0>
> 首次收录：2026-11-07T09:43:25+08:00
> 来源渠道：HN Show HN
> 标签：author_antelocnova, story_50397325, show_hn
> 最新指标：点赞=24 · 评论=1 · engagement_velocity=24

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-11-07T09:43:25+08:00 | HN Show HN | 点赞=24 · 评论=1 · engagement_velocity=24 | [[20-语料/posts/hn_show/2026-11-07/8f75952edf213518_Show-HN-Agents-infer-Lego-mechanisms-from-sources,]] |

## 摘要正文

Hi there :)Around a month ago, I released LDraw Nova, an agentic toolset for assembling LEGO CAD models by generating LDraw source code files.For more details, here's the Show HN post:https://news.ycombinator.com/item?id=49937916From the comments, I got the impression that there was quite an interest in seeing not only AI-generated LEGO models, but also AI-animated LEGO ones.I took a look at results from past experiments, and found it feasible to use agentic LLMs for:- analyzing the LDraw source code for LEGO models - reverse-engineer! the mechanisms present by reading the descriptions and sequence for the parts there - and then, animate them via Blender!This new project I'm presenting, LDraw Mecha, is the end result and proof that can be done:- Read specially annotated LDraw LEGO models .mpd source files - Infer the model structure in terms of submodels - Select from those the ones that are mechanisms - Plan animations - Execute them in BlenderIn summary, from an initial .mpd source file, get a rigged and animated version for the model as a Blender (.blend) file.See the results here:- Repo (v0.5.0): https://github.com/anteloc/ldraw-mecha/tree/v0.5.0 - Gallery: https://github.com/a…
