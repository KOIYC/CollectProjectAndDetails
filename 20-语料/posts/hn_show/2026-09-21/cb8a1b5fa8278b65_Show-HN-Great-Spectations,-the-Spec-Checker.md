---
type: "corpus"
item_id: "cb8a1b5fa8278b65"
title: "Show HN: Great Spectations, the Spec Checker"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49117854"
project_url: "https://greatspectations.org/"
author: "RustyRussell"
published_at: "2026-07-31T01:02:08Z"
captured_at: "2026-09-21T03:11:11+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-21"
pub_day: "2026-07-31"
tags:
  - 语料
  - hn_show
  - author_RustyRussell
  - story_49117854
  - show_hn
metrics: {"points": 5, "comments": 0, "engagement_velocity": 5}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:83d"
---

# Show HN: Great Spectations, the Spec Checker

> [!info] 一句话导读
> Faithful Spec Compliance

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49117854>
> 指标：点赞=5 · 评论=0 · engagement_velocity=5
> 作者：RustyRussell　|　发布：2026-07-31T01:02:08Z
> 项目链接：<https://greatspectations.org/>
> 采集：2026-09-21T03:11:11+08:00　|　id：`cb8a1b5fa8278b65`

## 正文

Great Spectations
What it catches
 Example
 Why it Matters
 Install
Faithful Spec Compliance
Great Spectations
Implementing or developing a spec? You need Great Spectations!
$
 pip install greatspectations
 Copy
$
 uv tool install greatspectations
 Copy
$
 greatspectate check --config specquotes.toml src/*.c
 Copy
§1
 Orphans and Convicts
You quote the spec as you implement. A comment marker names the source and section; the text after it is the quote.
Great Spectations checks the quote against the spec. Ignoring whitespace differences by default, or byte-exact if you prefer.
If the spec changes, it notices. And tells you exactly which comment is now quoting text that no longer exists.
A convenient format. ... wildcards, and a quote can pick up where the previous one left off: split one requirement list across multiple code chunks.
Coverage too. Ask which requirements in the spec no comment has quoted yet.
Any language, any spec. C, Python, Rust comment syntax all handled. Markdown specs, MediaWiki, old-school RFC-editor plaintext, and more.
§2
 The Period, in Two Languages
A real, runnable example: Python and Rust each quote different clauses of the same paragraph; one of them botches a quote, one clause never gets quoted at all. Generated straight from examples/generate.py running the actual tool — see examples/ in the repo.
Python
 Rust
 Coverage
"""Great Spectations demo: quoting Dickens instead of a protocol spec.
Nothing here is a real "requirement" -- it's just prose from a novel,
used to show that greatspectate checks any text source, not only specs.
"""
# DICKENS #1: it was the age of wisdom, it was the age of foolishness,
WISDOM = "the age of wisdom"
FOOLISHNESS = "the age of foolishness"
# DICKENS #1: it was the spring of hope, it was the winter of despair,
HOPE = "the spring of hope"
DESPAIR = "the winter of despair"
# DICKENS #1: we were all going direct to Heaven, we were all going
# direct the other way
HEAVEN = "direct to Heaven"
THE_OTHER_WAY = "direct the other way"
greatspectate check — all quotes match
$ greatspectate check --config specquotes.toml --coverage .coverage -v -k src/tale.py
 src/tale.py:7:Matched 'it was the age of wisdom, it was the age of foolishness,'
 src/tale.py:11:Matched 'it was the spring of hope, it was the winter of despair,'
 src/tale.py:15:Matched 'we were all going direct to Heaven, we were all going direct the other way'
// Great Spectations demo: quoting Dickens instead of a protocol spec.
//
// Nothing here is a real "requirement" -- it's just prose from a
// novel, used to show that greatspectate checks any text source, not
// only specs.
// DICKENS #1: It was the best of times, it was the blurst of times,
const BEST: &str = "the best of times";
const WORST: &str = "the blurst of times"; // "You stupid monkey!"
// DICKENS #1: we had everything before us, we had nothing before us,
const EVERYTHING: &str = "everything before us";
const NOTHING: &str = "nothing before us";
// DICKENS #1: in short, the period was so far like the present period,
// that some of its noisiest authorities insisted on its being received,
// for good or for evil, in the superlative degree of comparison only.
const VERDICT: &str = "the superlative degree of comparison only";
greatspectate check — one quote doesn't match
$ greatspectate check --config specquotes.toml --coverage .coverage -v -k --comment-start '// ' --comment-continue '//' src/tale.rs
 src/tale.rs:7:cannot find match
 01-the-period.md:10: note: closest match (94%): 'It was the best of times, it was the worst of times,'
 src/tale.rs:11:Matched 'we had everything before us, we had nothing before us,'
 src/tale.rs:15:Matched 'in short, the period was so far like the present period, that some of its noisiest authorities insisted on its being received, for good or for evil, in the superlative degree of comparison only.'
01-the-period.md:1:<!-- Public domain: Charles Dickens, "A Tale of Two Cities" (1859).
 01-the-period.md:2: Text from Project Gutenberg EBook #98 (https://www.gutenberg.org/ebooks/98).
 01-the-period.md:3: Line-wrapped one clause per line (Gutenberg's own wrapping runs
 01-the-period.md:4: several clauses together per line, which -- fittingly for a demo
 01-the-period.md:5: of coverage tooling -- makes individual clauses impossible to
 01-the-period.md:6: tell apart at line granularity). -->
 01-the-period.md:7:
 01-the-period.md:8:# Book the First -- Chapter I: The Period
 01-the-period.md:9:
 *** 01-the-period.md:10:It was the best of times, it was the worst of times,
 + 01-the-period.md:11:it was the age of wisdom, it was the age of foolishness,
 *** 01-the-period.md:12:it was the epoch of belief, it was the epoch of incredulity,
 *** 01-the-period.md:13:it was the season of Light, it was the season of Darkness,
 + 01-the-period.md:14:it was the spring of hope, it was the winter of despair,
 + 01-the-period.md:15:we had everything before us, we had nothing before us,
 + 01-the-period.md:16:we were all going direct to Heaven, we were all going direct the other way--
 + 01-the-period.md:17:in short, the period was so far like the present period, that some of
 + 01-the-period.md:18:its noisiest authorities insisted on its being received, for good or
 + 01-the-period.md:19:for evil, in the superlative degree of comparison only.
§3
 I say, Pip, old chap!
This is particularly useful when writing a specification and its implementation side by side: the spec becomes better because you use it to annotate the code, and can see whether it's sufficiently thorough, or logically laid out for other implementors.
Whoever implements your specification will thank you for it!
Copyright Rusty Russell 2026. BSD-MIT licensed.
bolt bip rfc markdown

## 关联链接

- https://www.gutenberg.org/ebooks/98

## 导航

- 项目页：[[10-项目/greatspectations.org_246c8559]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
