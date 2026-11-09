---
type: "corpus"
item_id: "dc9556849dc2747f"
title: "Show HN: My first project, an AI-powered financial news analyzer"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50418158"
project_url: "https://github.com/lamarcol/NotBot"
author: "lamarcol"
published_at: "2026-11-08T22:34:06Z"
captured_at: "2026-11-09T09:39:29+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-11-09"
pub_day: "2026-11-08"
tags:
  - 语料
  - hn_show
  - author_lamarcol
  - story_50418158
  - show_hn
metrics: {"points": 2, "comments": 0, "engagement_velocity": 2}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:3d"
---

# Show HN: My first project, an AI-powered financial news analyzer

> [!info] 一句话导读
> I'm 17, and I started NotBot a few months ago to see whether I could turn an idea into a working project. My main interest is economics, not becoming a programm…

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50418158>
> 指标：点赞=2 · 评论=0 · engagement_velocity=2
> 作者：lamarcol　|　发布：2026-11-08T22:34:06Z
> 项目链接：<https://github.com/lamarcol/NotBot>
> 采集：2026-11-09T09:39:29+08:00　|　id：`dc9556849dc2747f`

## 正文

I'm 17, and I started NotBot a few months ago to see whether I could turn an idea into a working project. My main interest is economics, not becoming a programmer, but I enjoy experimenting with code.A few months ago, I had the idea of creating a program that would analyze the most recent news about a specific stock and calculate a weighted average of their polarity to create a sort of sentiment indicator.While researching, I found a YouTube video about creating a simple GitHub repository that did, in a simplified and imprecise way, what I had in mind. At first glance, I realized it was a very simple program: feedparser retrieved news from Google News, beautifulsoup4 extracted the content, the sentiment was analyzed with FinBERT, running through Transformers and PyTorch.From there, I started modifying it with the free versions of Gemini. I had to solve a lot of problems, for example fixing the extraction of articles from Google News, I managed to solve it with a new library (googlenewsdecoder).Then I had to replace FinBERT, because it classified sentiment based on the context of the words but didn't take into account the actual impact of the event using external sources.I experimented with an LLM that allowed me to specify the evaluation criteria more precisely through a prompt. I found a free one with rather strict TPM and RPM limits (it was called openai/gpt-oss-120b).I also created two coefficients: one that adjusted the reliability of the news based on its source, and another that adjusted its impact based on how recent it was (all selected news articles had been published within the last 24 hours). Each article was divided into title, description, and content, and each of these three sections had a different weight based on predefined values (title 35%, description 25%, and text 40%). If the content had fewer than 100 characters, the text was not assigned any weight, and the title accounted for 60% while the description accounted for 40%.After these modifications, I took a break of about a month because of school commitments, during which I discovered Codex (OpenAI's agent).I changed the main LLM and implemented Gemini (3.1 Flash-Lite) because the TPM limits of the LLM I was using were too restrictive.Even though I started using Gemini, I didn't discard Groq. In fact, I used it as a fallback in case Gemini returned some kind of error.Another important modification was the addition of asynchronous article downloading through aiohttp and the processing of multiple articles simultaneously through asyncio. Later, I decided to start using Groq again for article analysis. In fact, I had both LLMs analyze the longer articles and then calculated the average of their two polarity scores.The first was Finnhub, which allowed me to search for many more news articles about a specific stock (by entering its name and ticker).At that point, I had to split up the code because the script had become very long.The last modification I made concerned news selection: I implemented a filter that prevented similar news articles from being selected, to avoid excessively distorting the polarity in an incorrect way.First of all, I'd like to know, from an expert, how well the project is built from a structural point of view and how it could be improved. For future projects, what parameters should I take into consideration to understand whether a project is well built?Secondly, I'd like to know how I can determine whether a program like this can actually work, or at least how it could be useful (even with some modifications).The third and final point is: which aspects of the pipeline might require more attention or could be optimized? Does it make sense to continue working on the project (also with the idea of turning it into a product), or am I approaching a structural limit?

## 导航

- 项目页：[[10-项目/github.com_14bf5e0f]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
