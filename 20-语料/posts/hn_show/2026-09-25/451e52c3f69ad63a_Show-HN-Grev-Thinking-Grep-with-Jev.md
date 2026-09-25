---
type: "corpus"
item_id: "451e52c3f69ad63a"
title: "Show HN: Grev - Thinking Grep with Jev"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49837132"
project_url: "https://github.com/aurorainfra/grev"
author: "devttyeu"
published_at: "2026-09-24T21:46:21Z"
captured_at: "2026-09-25T13:42:25+08:00"
lang: "en"
kind: "post"
topic: SaaS/B2B
shard: "2026-09-25"
pub_day: "2026-09-24"
tags:
  - 语料
  - hn_show
  - author_devttyeu
  - story_49837132
  - show_hn
metrics: {"points": 2, "comments": 1, "engagement_velocity": 2}
comments_count: 1
comments_total: 1
discovered_via: "hn:show_hn:3d"
---

# Show HN: Grev - Thinking Grep with Jev

> [!info] 一句话导读
> License: Apache License 2.0

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49837132>
> 指标：点赞=2 · 评论=1 · engagement_velocity=2
> 作者：devttyeu　|　发布：2026-09-24T21:46:21Z
> 项目链接：<https://github.com/aurorainfra/grev>
> 采集：2026-09-25T13:42:25+08:00　|　id：`451e52c3f69ad63a`

## 正文

# aurorainfra/grev

Thinking coreutils

- Stars: 3
- Forks: 0
- Watchers: 3
- Open issues: 0
- License: Apache License 2.0
- Default branch: main
- Created: 2026-09-24T21:12:11Z

## Languages

- Go
- Makefile
- Shell

## Top Contributors

- magik6k (10 contributions)

---

## README

# grev

Unix filters that ask questions instead of matching patterns.

```console
$ cat examples/menu.txt
chicken tikka masala
fresh fruit salad
spaghetti carbonara
tofu stir fry with rice

$ grev 'is a vegan meal' examples/menu.txt
fresh fruit salad
tofu stir fry with rice
```

The tools run on TypeSafe's Jev models, which answer typed questions with
calibrated probabilities instead of generating text. That's why these tools behave like `grep`,
`sort` or `cut`: **output is always your input**. Labels and scores appear only as explicit
columns. A few thousand lines cost fractions of a cent and take seconds.

## Examples

```sh
# Search logs by meaning
grev --about 'nginx error log' 'says the upstream server timed out' examples/nginx-error.log
journalctl -fu myapp | grev --line-buffered --about 'application log' 'shows the process crashed'
git log --oneline | grev --about 'commit messages' 'fixes a bug'

# Guard a commit: exit 0 means yes
git diff --cached | isv 'adds a secret or credential' && echo 'refusing to commit' && exit 1

# Label, route, rank
tagv billing technical feature-request other < examples/tickets.txt
tagv --split tickets/ billing technical other < examples/tickets.txt
rank -s -m3 -L 'not urgent|soon|urgent|critical' 'How urgent is the ticket {}?' examples/tickets.txt
sortv 'chronologically, earliest first' examples/sortv-events.txt

# Find, cut, dedupe, reflow
man tar | pickv 'how do I list the contents of an archive?'
cutv 'email address' 'phone number' < examples/users.csv
uniqv -c 'Are {1} and {2} the same company?' examples/companies.txt
unwrap examples/memo.txt
seek --verify 'the spend ledger' .

# Bisect by meaning: the first health check that reports a failure (3 requests for 600 lines)
lookv -n --about 'health checks, one per minute' 'reports a failing dependency' examples/lookv-health.log

# Edit by meaning: quote marks but not apostrophes; St. → Saint or Street by context
trv "'" '"' 'is used as a quotation mark, not an apostrophe' < examples/trv-story.txt
trv -e '\bSt\.' -o 'Saint|Street' 'what St. abbreviates here' < examples/trv-addresses.txt

# Probabilities as columns, for awk
probev -H -q 'refund: asks for money back' -q 'angry: the writer is angry' < examples/tickets.txt
```

| tool | like | does |
|---|---|---|
| `grev` | grep | print the records the model says yes to |
| `isv` | test | answer a yes/no question about the whole input with the exit status |
| `oneof` | case | print which label fits the whole input |
| `tagv` | awk | label every record; `--split DIR` routes records into files |
| `sortv` | sort | sort in an order described in words, by pairwise comparison |
| `rank` | sort | sort records by how well they fit, or by ordered levels |
| `pickv` | grep -o | the one line or regex match that best answers a question |
| `uniqv` | uniq | collapse adjacent records that mean the same thing |
| `unwrap` | fmt | re-join hard-wrapped lines |
| `seg` | csplit | split a stream into topic segments |
| `cutv` | cut | cut the CSV/TSV columns that match a description |
| `seek` | find | walk a directory tree to what a description names |
| `trv` | tr, sed | translate, delete, squeeze or replace only where an instruction applies |
| `lookv` | look, git bisect | find where an ordered input's answer flips, in a few rounds |
| `probev` | awk | print per-record probability columns |
| `jev` | — | config, API key, spend, models, one-off and raw requests |

Every tool has `--help` and a man page. The common flags:

| flag | meaning |
|---|---|
| `-p` | progress, with live and projected cost |
| `-Q` | show the quote and ask first |
| `-J N` / `-Jmax` | parallelism |
| `--max-cost` | per-run budget |

## Install

- **Packages:** deb, rpm, apk, Arch packages and archives for Linux, macOS, FreeBSD and
 Windows are on the releases page.
 `packaging/arch/PKGBUILD` builds from source.
- **With Go:** `go install github.com/aurorainfra/grev/cmd/...@latest`
- **From source:** `make && sudo make install`, which also installs the man pages and bash/zsh/fish
 completions.

## Configure

Everything lives in one file, `~/.grevconfig`, in git-config style; the full reference is
`docs/CONFIG.md` (or `man grevconfig`). `jev key set` puts your
API key there with mode 0600:

```ini
[api]
	key = tsk-…                           ; written by `jev key set`
[defaults]
	progress = auto                       ; the -p overlay whenever stderr is a terminal
	jobs = max
	confirmAbove = 0.25                   ; ask before runs quoted above $0.25 (built-in: $1)
[limits]
	daily = 5                             ; spend caps in USD, across all tools
	monthly = 50
[tool "grev"]
	about = application logs              ; per-tool defaults for any long option,
	threshold = 0.7                       ; e.g. how sure the model must be to say yes
```

Thresholds are set per tool because `-t` means different things: P(yes) in `grev`, the minimum
confidence of a choice in `tagv`, a path score in `seek`.

Manage it with `jev config set limits.daily 5` or `jev config list --show-origin`, and check
your spend with `jev spend`. Command-line flags beat environment variables, which beat the
config. In CI, `TYPESAFE_API_KEY` supplies the key without any file.

## Cost and safety

Jev charges $0.042 per million input tokens, and output is free. Grepping a 4,000-line source
file costs about $0.008.

Nothing big runs by surprise:
- Any run quoted above `confirmAbove` ($1 unless configured) asks first. Without a terminal, it
 refuses.
- `--max-cost` and the daily/monthly caps stop a run before it goes over.
- Closing the output pipe (`| head`) stops the spending.

## More

- **`docs/DESIGN.md`:** how the tools phrase questions and why, the evals,
 flag conventions and the cost model.
- **`docs/CONFIG.md`:** configuration in depth.
- **Man pages:** `grev-tools(7)`, `grevconfig(5)`, and one per tool.

## License

Licensed under either of Apache License, Version 2.0 or
MIT license, at your option.

Unless you explicitly state otherwise, any contribution intentionally submitted for inclusion in
this work by you, as defined in the Apache-2.0 license, shall be dual licensed as above, without
any additional terms or conditions.

# On-Call Arena

## 评论（1/1）

> **devttyeu** · 2026-09-24T21:51:42.000Z　
> Thought it would be funny to build, but those have actually helped me with log-combing already

## 导航

- 项目页：[[10-项目/github.com_1ac979ed]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`SaaS/B2B`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
