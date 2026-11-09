---
type: "project"
title: "Show HN: My first project, an AI-powered financial news analyzer"
project_url: "https://github.com/lamarcol/NotBot"
first_seen: "2026-11-09T09:39:29+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_lamarcol
  - story_50418158
  - show_hn
lang: "en"
---

# Show HN: My first project, an AI-powered financial news analyzer

> [!info] 一句话导读
> I'm 17, and I started NotBot a few months ago to see whether I could turn an idea into a working project. My main interest is economics, not becoming a programm…

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://github.com/lamarcol/NotBot>
> 首次收录：2026-11-09T09:39:29+08:00
> 来源渠道：HN Show HN
> 标签：author_lamarcol, story_50418158, show_hn
> 最新指标：点赞=2 · 评论=0 · engagement_velocity=2

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-11-09T09:39:29+08:00 | HN Show HN | 点赞=2 · 评论=0 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-11-09/dc9556849dc2747f_Show-HN-My-first-project,-an-AI-powered-financial]] |

## 摘要正文

I'm 17, and I started NotBot a few months ago to see whether I could turn an idea into a working project. My main interest is economics, not becoming a programmer, but I enjoy experimenting with code.A few months ago, I had the idea of creating a program that would analyze the most recent news about a specific stock and calculate a weighted average of their polarity to create a sort of sentiment indicator.While researching, I found a YouTube video about creating a simple GitHub repository that did, in a simplified and imprecise way, what I had in mind. At first glance, I realized it was a very simple program: feedparser retrieved news from Google News, beautifulsoup4 extracted the content, the sentiment was analyzed with FinBERT, running through Transformers and PyTorch.From there, I started modifying it with the free versions of Gemini. I had to solve a lot of problems, for example fixing the extraction of articles from Google News, I managed to solve it with a new library (googlenewsdecoder).Then I had to replace FinBERT, because it classified sentiment based on the context of the words but didn't take into account the actual impact of the event using external sources.I experimen…
