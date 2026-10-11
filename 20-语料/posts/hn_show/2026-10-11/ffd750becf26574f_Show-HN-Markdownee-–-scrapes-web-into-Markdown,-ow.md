---
type: "corpus"
item_id: "ffd750becf26574f"
title: "Show HN: Markdownee – scrapes web into Markdown, own Trafilatura typescript port"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50038717"
project_url: "https://markdownee.com/"
author: "seky"
published_at: "2026-10-11T00:59:49Z"
captured_at: "2026-10-11T09:43:53+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-10-11"
pub_day: "2026-10-11"
tags:
  - 语料
  - hn_show
  - author_seky
  - story_50038717
  - show_hn
metrics: {"points": 3, "comments": 0, "engagement_velocity": 3}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:3d"
---

# Show HN: Markdownee – scrapes web into Markdown, own Trafilatura typescript port

> [!info] 一句话导读
> Skip to main content

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50038717>
> 指标：点赞=3 · 评论=0 · engagement_velocity=3
> 作者：seky　|　发布：2026-10-11T00:59:49Z
> 项目链接：<https://markdownee.com/>
> 采集：2026-10-11T09:43:53+08:00　|　id：`ffd750becf26574f`

## 正文

Skip to main content
 Markdownee: web scraper (websites into Markdown)
 Web content as Markdown or other formats — built on Trafilatura Core , free, open source.
Markdownee playground
 Preview extraction results, adjust extraction settings, and generate ready-to-run CLI commands, lib calls, or Apify actor API calls.
Crawl crawl & save Fetch single page Export storage → files Purge clear storage
 URL to extract
 Paste Clear Example
Output
 Output format Output format
Plain text
 Markdown
 HTML
 Minified HTML
 Original raw HTML
Output layout Output layout
Minimal
 Standard
 Enhanced
Extraction
Page & browser
Crawl scope
Session & proxy
Storage
What to do:
 Crawl URL Preview results
 npm CLI Generate commands
 npm library TypeScript code
 Python lib Library code
 Apify CLI Generate commands
 Apify API API call code
Reset Crawl URL
This playground previews one page only. Use the generated commands or code to crawl multiple pages.
Available as:
 npm package CLI & lib
Python library
Source code on GitHub
Apify Actor Apify gives you $5 of free usage monthly
Social:
 Star us on GitHub
Follow us on GitHub
Follow us on X
What is Markdownee?
 Markdownee is a web scraper that crawls websites and saves their content as Markdown , HTML or plain text for LLMs, retrieval pipelines, and research datasets.
Choose which links to follow, set page and depth limits, and select how much page content to keep. Control tables, links, images, and user comments separately.
Boilerplate removal uses Trafilatura Core , our open-source extraction engine based on Trafilatura , available in TypeScript and Python. Markdownee’s TypeScript and Python versions each use the matching Core implementation.
The Core in its name means it is reduced to one task : extracting main content by removing boilerplate. Other packages handle output conversion, including Markdown.
Core's TypeScript engine ports the original Python Trafilatura , with go-trafilatura as a DOM translation aid. Its native Python engine translates that port.
Compared with Mozilla Readability , Trafilatura and Trafilatura Core use layered structural and content heuristics with fallback and recall escalation, rather than centering extraction on the candidate scoring inherited from Arc90’s original readability.js article extractor; Trafilatura Core also offers configuration options for boilerplate removal.
Crawlee handles crawling and uses Playwright for browser rendering.
Two language versions — TypeScript and Python : self-host with the npm CLI , npm library , or Python library , or use the hosted Apify Actor . Source code is on GitHub .
Save image files with the optional image downloading mode
Learn more
Getting started
 Try Markdownee with one npx command — no browser install or API key is needed. Use Node.js 22.22.2+ on the 22.x line, 24.15.0+ on 24.x, or 26+:
npx --package=@markdownee/markdownee markdownee fetch \
 https://en.wikipedia.org/wiki/Web_scraping \
 --crawler-type cheerio --save markdown-file -o page.md
Open page.md to inspect the extracted article. --crawler-type cheerio fetches over plain HTTP. For a whole-site crawl or specific formats, use the playground to build a command visually, then copy it.
 Learn more
Home About Press kit Library Help Trafilatura GitHub X (Twitter) Terms Privacy

## 关联链接

- https://en.wikipedia.org/wiki/Web_scraping

## 导航

- 项目页：[[10-项目/markdownee.com_b5c054f0]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
