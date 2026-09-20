---
type: "corpus"
item_id: "cd027f9f6d5c331d"
title: "We gave away the data layer (registry data) a competitor charges SIX FIGURES / year"
source: "reddit"
source_name: "Reddit 独立开发版块"
url: "https://www.reddit.com/r/microsaas/comments/1vbt4v2/we_gave_away_the_data_layer_registry_data_a/"
project_url: "https://registry-lookup.com/"
author: "OkHeat6599"
published_at: "2026-07-31T22:51:29+08:00"
captured_at: "2026-09-21T01:32:17+08:00"
lang: "en"
kind: "post"
topic: "开发者工具"
shard: "2026-09-21"
pub_day: "2026-07-31"
tags:
  - 语料
  - reddit
  - r/microsaas
metrics: {"score": 5, "comments": 2, "upvote_ratio": 1}
comments_count: 0
comments_total: 0
discovered_via: "reddit:83d+settle3"
---

# We gave away the data layer (registry data) a competitor charges SIX FIGURES / year

> [!info] 一句话导读
> Not a success story post per se, but the decision was unusual enough that it might be useful to someone.

> [!meta]- 语料信息（点开展开）
> 来源：Reddit 独立开发版块（post）
> 原帖：<https://www.reddit.com/r/microsaas/comments/1vbt4v2/we_gave_away_the_data_layer_registry_data_a/>
> 指标：得分=5 · 评论=2 · 赞踩比=1
> 作者：OkHeat6599　|　发布：2026-07-31T22:51:29+08:00
> 项目链接：<https://registry-lookup.com/>
> 采集：2026-09-21T01:32:17+08:00　|　id：`cd027f9f6d5c331d`

## 正文

Not a success story post per se, but the decision was unusual enough that it might be useful to someone.

Background: we're Veridion, we sell company data to enterprise customers. Registry data (legal names, registration numbers, incorporation dates, addresses) is the foundation layer under that product.

**What started it**

A lead mentioned, almost in passing, that they pay a registry data provider six figures a year. For legal names, identifiers and registered addresses. We already had that data running in production.

The realisation was that the price had nothing to do with the cost. Registry data is public record, governments publish it deliberately. What the layer between charges reflects switching costs, not collection costs.

The case against was obvious: we'd be giving away something a competitor monetises, and possibly training customers to expect it free.

The case for was that we don't win deals on registry data. Nobody picks a supply chain risk platform because it can tell you a company's legal name. Our differentiation sits above that layer. So charging for the foundation was never actually the business, it was just what everyone did.

**What it does**

Search by company name and jurisdiction, get back registry number, status (active/inactive), incorporation date, legal form, tax ID, registered address.

**Why it's useful** 

Company names are messy and unreliable. People type brand names, misspell things, use abbreviations, and the same company shows up three ways in your database. Registry data gives you the actual legal entity behind the name, plus whether it still exists and is trading. So you can catch junk signups, spot accounts that quietly dissolved, and clean up duplicates that fuzzy name matching won't catch.

**The build**

Genuinely fast, because the hard part was already done. The pipelines had been running for years. We built a search frontend and a public REST API on top and shipped in a few days.

The one interesting technical thing: normalisation is the whole problem in this space. Every registry has its own legal forms, its own status vocabulary, its own numbering. "Dissolved" in one country is "struck off" in another and "cancelled" in a third. Getting 309 jurisdictions into one schema was years of accumulated work, and it's the reason this isn't easy to replicate even though the underlying data is public.

Result: [registry-lookup.com](http://registry-lookup.com)

521M legal entities, 309 jurisdictions, 244 countries. Free to search, no account. 5,000 API calls a month free.

If you've run a free tier on top of an enterprise product, I'd like to know which way it went for you.

## 关联链接

- http://registry-lookup.com

## 导航

- 项目页：[[10-项目/registry-lookup.com_b06796d6]]
- 渠道页：[[50-渠道/reddit]]
- 赛道：`开发者工具`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
