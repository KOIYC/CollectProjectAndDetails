---
type: "corpus"
item_id: "03608bc561fc2139"
title: "Show HN: Are My ETFs Overvalued? Daily ETF insights and comparisons tool"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49831744"
project_url: "https://etf-copilot.com/"
author: "iv777"
published_at: "2026-09-24T15:13:12Z"
captured_at: "2026-09-24T23:57:22+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-24"
pub_day: "2026-09-24"
tags:
  - 语料
  - hn_show
  - author_iv777
  - story_49831744
  - show_hn
metrics: {"points": 2, "comments": 0, "engagement_velocity": 2}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:3d"
---

# Show HN: Are My ETFs Overvalued? Daily ETF insights and comparisons tool

> [!info] 一句话导读
> I built ETF Copilot (https://etf-copilot.com/go/show-hn) as analytical support for my own investing. It answers what financial screeners and platforms do not: w…

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49831744>
> 指标：点赞=2 · 评论=0 · engagement_velocity=2
> 作者：iv777　|　发布：2026-09-24T15:13:12Z
> 项目链接：<https://etf-copilot.com/>
> 采集：2026-09-24T23:57:22+08:00　|　id：`03608bc561fc2139`

## 正文

I built ETF Copilot (https://etf-copilot.com/go/show-hn) as analytical support for my own investing. It answers what financial screeners and platforms do not: which valuation, growth, quality and risk metrics matter for each ETF, and how do they compare to own history and peers. It covers 1,000+ US-listed equity ETFs and updates every night with fresh data.Free version without signup offers 5 fund views. Overlap, concentration, and theme pages are unlimited. Pro $20/month tier adds unlimited views, full rankings, watchlists, alerts, and twice a week ETF market newsletter. For Show HN I opened a broader access showing most functionality for free.> > > Background:
About a year ago I became much more interested in investing in ETFs. I have been in Finance for many years and saw many systems and tools from Yahoo Finance to expensive enterprise solutions. They all gave plenty of data, but getting to ETF-level conclusion still took hours.> > > How it grew into a system:
I started building a small tool for myself. Rolling up stock level analysis to an ETF level was a key requirement, which enabled answering questions like “Is this ETF expensive” or “How profitable are companies in this ETF”. I automated it to run daily for US-listed equity ETF universe, which enabled ETF rankings based on valuation, growth, quality, and risk. I added features people were asking about on forums and social media: multi-fund comparison, overlap and concentration. Over time it evolved into an app.> > > Technical problems solved:
1) Mapping ETFs to stocks. ETFs hold many companies listed on international exchanges, reporting in different currencies, having different classes of securities. Tickers, ISIN, FIGI and company names can vary or be missing. I ended up building a fairly long set of rules to resolve the inconsistencies and map the data, as mapping quality directly influenced metrics downstream.2) Metrics aggregation and rankings. Negative P/E, missing data, abrupt changes in some metrics caused wild swings in early versions, and a straightforward weighted average approach worked in some cases but broke in others. Developing a system of calculation and coverage rules was an integral part to raise quality of outputs. For rankings, “Gate first, weight second” filtering to remove poor performers proved to be a much more effective and stable approach than a seemingly logical weighted average across all.3) LLM explanations grounded in facts and without hallucinations. I wanted to provide short daily explanations on each ETF and the market, instead of pushing the user to analyze dozens of metrics. I ran data analysis deterministically and built compact “factpacks” on each ETF and sector, as the only data LLM sees. Then fed those to LLM to write explanations and put a deterministic validator checking numerical claims against the source data, as well as a separate semantic LLM validator checking unclear or misleading wording.> > > Questions:
1. Can you quickly get the needed data in app to tell “what sets ETF X apart from similar funds”?
2. What would you improve to make it more actionable and useful for individual ETF investors?
3. Which steps and data points do you use, when you consider investing in ETFs?> > > Website: https://etf-copilot.com/go/show-hn

## 关联链接

- https://etf-copilot.com/go/show-hn

## 导航

- 项目页：[[10-项目/etf-copilot.com_76a08ba7]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
