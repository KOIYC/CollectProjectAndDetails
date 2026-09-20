---
type: "corpus"
item_id: "9dbef4d7a15ab32e"
title: "Show HN: Go Implementation of Systemd Time"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49758918"
project_url: "https://gitlab.com/allddd/go-systemd-time"
author: "allddd"
published_at: "2026-09-18T19:18:11Z"
captured_at: "2026-09-20T09:23:24+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-20"
pub_day: "2026-09-18"
tags:
  - 语料
  - hn_show
  - author_allddd
  - story_49758918
  - show_hn
metrics: {"points": 4, "comments": 0, "engagement_velocity": 4}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:90d"
---

# Show HN: Go Implementation of Systemd Time

> [!info] 一句话导读
> allddd / go-systemd-time

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49758918>
> 指标：点赞=4 · 评论=0 · engagement_velocity=4
> 作者：allddd　|　发布：2026-09-18T19:18:11Z
> 项目链接：<https://gitlab.com/allddd/go-systemd-time>
> 采集：2026-09-20T09:23:24+08:00　|　id：`9dbef4d7a15ab32e`

## 正文

allddd / go-systemd-time · GitLab

master

Select Git revision

Selected

- master default protected

Branches 1

- development

Tags 3

- v0.2.1 protected
- v0.2.0 protected
- v0.1.0 protected

5 results

Find file

Code

Clone with SSH

Clone with HTTPS

Open with

Visual Studio Code

IntelliJ IDEA

Download source code

Your workspaces

A workspace is a virtual sandbox environment for your code in GitLab.

No agents available to create workspaces. Please consult Workspaces documentation for troubleshooting.

Actions

docs: add better examples and a short desc of functions to readme

Most recent commit.

allddd authored 4 months ago

Verified

0d244223

0d244223 4 months ago

| Name | Last commit | Last update |
| --- | --- | --- |
| .gitlab-ci.yml | ci: add pipeline config | 4 months ago |
| .golangci.yml | chore: disable mnd linter | 4 months ago |
| LICENSE | initial commit | 4 months ago |
| README.md | docs: add better examples and a short desc of functions to readme | 4 months ago |
| go.mod | initial commit | 4 months ago |
| systemdtime.go | style: improve code and comment consistency | 4 months ago |
| systemdtime_test.go | feat(timestamp): add function for parsing timestamps | 4 months ago |

# go-systemd-time

Go implementation of systemd time.

Note

Calendar events are not yet supported.

I don't like maintaining docs in two places, so below are just a few examples and the rest is on pkg.go.dev.

## Time spans

`ParseTimespan` parses a time span string and returns a`time.Duration`. It supports units from nanoseconds to years (and their abbreviations), decimal values, combinations, bare numbers, etc. See the full docs for more info.

```go
package main

import (
	"fmt"
	"log"

	systemdtime "gitlab.com/allddd/go-systemd-time"
)

func main() {
	timespans := []string{
		"1.5days",
		"100ns",
		"1y 12month",
		"2h30min",
		"500 ms",
		"55s500ms",
		"60",
	}
	for _, ts := range timespans {
		d, err := systemdtime.ParseTimespan(ts)
		if err != nil {
			log.Fatal(err)
		}
		fmt.Printf("There are %.0f seconds in %q.\n", d.Seconds(), ts)
	}
}
```

## Timestamps

`ParseTimestamp` parses a timestamp string and returns a`time.Time`. It supports many more formats/variations than shown below, see the full docs.

```go
package main

import (
	"fmt"
	"log"

	systemdtime "gitlab.com/allddd/go-systemd-time"
)

func main() {
	timestamps := []string{
		"today",
		"+13h30min",
		"10h11min ago",
		"2009-11-10 18:15:22.654321 UTC",
		"@1395716396",
		"Tue 2009-11-10T18:15:22+01:00",
		"tomorrow Asia/Tokyo",
	}
	for _, ts := range timestamps {
		t, err := systemdtime.ParseTimestamp(ts)
		if err != nil {
			log.Fatal(err)
		}
		fmt.Printf("%q is a %s.\n", ts, t.Weekday())
	}
}
```

This project is licensed under the BSD 2-Clause License. See LICENSE for more details.

# Yello — Connect your agent with other people’s agents

## 导航

- 项目页：[[10-项目/gitlab.com_49229eb5]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
