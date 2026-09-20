---
type: "corpus"
item_id: "9e71d16155233418"
title: "Show HN: An OSS Python dependency scanner for exploited, unmaintained packages"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49762076"
project_url: "https://github.com/binuka200/package-doctor"
author: "binukajayaweera"
published_at: "2026-09-19T00:27:26Z"
captured_at: "2026-09-20T14:01:26+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-20"
pub_day: "2026-09-19"
tags:
  - 语料
  - hn_show
  - author_binukajayaweera
  - story_49762076
  - show_hn
metrics: {"points": 3, "comments": 4, "engagement_velocity": 3}
comments_count: 5
comments_total: 5
discovered_via: "hn:show_hn:90d"
---

# Show HN: An OSS Python dependency scanner for exploited, unmaintained packages

> [!info] 一句话导读
> I built an open source python dependency scanner that will scan and flag packages with known exploit CVEs(CISA's Known Exploited list and FIRST EPSS) and unmain…

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49762076>
> 指标：点赞=3 · 评论=4 · engagement_velocity=3
> 作者：binukajayaweera　|　发布：2026-09-19T00:27:26Z
> 项目链接：<https://github.com/binuka200/package-doctor>
> 采集：2026-09-20T14:01:26+08:00　|　id：`9e71d16155233418`

## 正文

I built an open source python dependency scanner that will scan and flag packages with known exploit CVEs(CISA's Known Exploited list and FIRST EPSS) and unmaintained packages that have not had a release or commit in 2 years. Theres also claude hook that will make your AI agent not install these type of packages included in this repo. The full mechanism is in the readme of the project, this was just a brief summary.

## 评论（5/5）

> **binukajayaweera** · 2026-09-19T00:45:08.000Z　
> the packages get flagged or escalated if its at a trust boundary for example if it parses, decodes or authenticates data that an attacker can influence and have either a known CVE or is basically unmaintained. Non trust boundary packages also get reported but not escalated. I welcome contributions to the repo to make it more useful. More info can be found in the readme and docs attached to it.

---

> **zahlman** · 2026-09-19T09:52:44.000Z　
> Have you considered talking to PyPI staff about this?

---

> **binukajayaweera** · 2026-09-19T18:34:05.000Z　
> I dont know how I can reach them, I would love to get their feedback on this

---

> **zahlman** · 2026-09-19T23:24:42.000Z　
> There's a public Python packaging Discord https://discord.gg/pypa , or you can try emailing the Packaging Work Group (see info at https://wiki.python.org/psf/PackagingWG ), although the latter is probably deprecated. You can also try the Packaging section of the official Python forums: https://discuss.python.org/c/packaging/14

---

> **binukajayaweera** · 2026-09-20T01:23:04.000Z　
> joined the discord chat, thank you for suggesting this to me

## 导航

- 项目页：[[10-项目/github.com_5e012b78]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
