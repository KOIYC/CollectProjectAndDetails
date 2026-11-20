---
type: "corpus"
item_id: "eff112c26c267741"
title: "Show HN: Dayfile.app – Append-only log for your scripts and agents"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50561824"
project_url: "https://github.com/dayfile/dayfile"
author: "gilad"
published_at: "2026-11-19T16:00:33Z"
captured_at: "2026-11-20T09:45:52+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-11-20"
pub_day: "2026-11-19"
tags:
  - 语料
  - hn_show
  - author_gilad
  - story_50561824
  - show_hn
metrics: {"points": 4, "comments": 2, "engagement_velocity": 4}
comments_count: 2
comments_total: 2
discovered_via: "hn:show_hn:3d"
---

# Show HN: Dayfile.app – Append-only log for your scripts and agents

> [!info] 一句话导读
> Hi HN, I'm Gilad.dayfile.app is a "git log for scripts and agents", with ordered history, append-only logging as foundational characteristics. The service is cu…

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50561824>
> 指标：点赞=4 · 评论=2 · engagement_velocity=4
> 作者：gilad　|　发布：2026-11-19T16:00:33Z
> 项目链接：<https://github.com/dayfile/dayfile>
> 采集：2026-11-20T09:45:52+08:00　|　id：`eff112c26c267741`

## 正文

Hi HN, I'm Gilad.dayfile.app is a "git log for scripts and agents", with ordered history, append-only logging as foundational characteristics. The service is currently in beta, AGPL-licensed.As I was looking at various ways to record and retrieve a day's to-dos, automation and operational outputs (update successes and failures), the idea of a running event log. dayfile.app's primary use case is DevOps tracking and event logging. Building this, I've emphasized simplifying posting - one HTTP request with a title and optional tags (used for filtering when reading the log), AI access via MCP server (an assistant can read, post or close to-dos) and self-hosting as a first-class citizen (`pip install dayfile`, SQLite database is local in this mode).A demo is available at https://dayfile.app/demo. If using the cloud service and after generating a write token on the site, an example of posting an entry would be: curl -X POST https://USERNAME.dayfile.cloud/events \
 -H "Authorization: Bearer WRITE_TOKEN" \
 -H "content-type: application/json" \
 -d '{"title":"Nightly backup finished","tags":["backup"]}'

To read back (filtering using tag): curl -H "Authorization: Bearer READ_TOKEN" \
 "https://USERNAME.dayfile.cloud/events?tag=backup&within=7d"

or paste https://USERNAME.dayfile.cloud/t/READ_TOKEN/f/backup.atom into a feed reader (you need to create a feed called `backup`).What a local file can't do is notice something didn't happen - this is the heartbeat. dayfile.app can be configured to create an event if no associated event arrives. Imagine a backup which didn't run. A to-do event is created if no evidence of a successful backup shows up within a certain period. When the backup reports again, dayfile closes the associated to-do.Current limits: logs are not end-to-end encrypted, sign-in is via GitHub only, the free beta allows 50,000 events and log size of 25MB. Pricing will be sorted out after this launch and as user feedback rolls in.I'd love to hear in the comments on how you'd use it, what would prevent you from doing so, feature requests and suggestions. Bug reports can be submitted as issues on GitHub.

## 评论（2/2）

> **toomuchtodo** · 2026-11-19T16:04:26.000Z　
> Interesting idea! I use Graylog community edition for something similar, where everything technology I operate emits a logging event and Graylog is the append only log. Did you consider a traditional logging solution for this use case? If so, what differentiates this from such an approach?https://graylog.org/free/

---

> **gilad** · 2026-11-19T17:41:12.000Z　
> Thanks for the supportive comment. Graylog is a mature tool, with many more capabilities than dayfile offers. I'd emphasize Graylog's ability to handle volume, variety of sources - storage, search and response to events. dayfile's total volume, ingest and response is smaller, but more targeted - informative, yet limited events ("backup finished", "TODO xyz" + open/close feature). The tradeoff is size and complexity of the application itself. Graylog packages multiple Java applications - its server, OpenSearch for search, and MongoDB. dayfile is a single Python-based application and a single SQLite file you can export at any time. dayfile uses token-based access controls - a read token can be limited to an audience, and a feed can be filtered by tag and made public. One log can serve multiple audiences and views without exposing all of it.I can imagine these working together, processing + HTTP notifications from Graylog, into a post-processed, actionable event using dayfile.From your comment I assume you operate multiple systems; which events would you want in a short daily record, as opposed to the full log?

## 关联链接

- https://USERNAME.dayfile.cloud/events
- https://USERNAME.dayfile.cloud/events?tag=backup&within=7d
- https://USERNAME.dayfile.cloud/t/READ_TOKEN/f/backup.atom
- https://dayfile.app/demo.

## 导航

- 项目页：[[10-项目/github.com_271a4c20]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
