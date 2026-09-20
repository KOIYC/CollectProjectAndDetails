---
type: "corpus"
item_id: "c9991863f5486f11"
title: "Show HN: Texio, reliable Markdown operations for shell scripts and AI agents"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49736484"
project_url: "https://github.com/Allra-Fintech/texio"
author: "yuzong"
published_at: "2026-09-17T04:39:42Z"
captured_at: "2026-09-20T09:36:55+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-20"
pub_day: "2026-09-17"
tags:
  - 语料
  - hn_show
  - author_yuzong
  - story_49736484
  - show_hn
metrics: {"points": 2, "comments": 0, "engagement_velocity": 2}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:90d"
---

# Show HN: Texio, reliable Markdown operations for shell scripts and AI agents

> [!info] 一句话导读
> Reliable Markdown operations for shell scripts and AI agents

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49736484>
> 指标：点赞=2 · 评论=0 · engagement_velocity=2
> 作者：yuzong　|　发布：2026-09-17T04:39:42Z
> 项目链接：<https://github.com/Allra-Fintech/texio>
> 采集：2026-09-20T09:36:55+08:00　|　id：`c9991863f5486f11`

## 正文

# Allra-Fintech/texio

Reliable Markdown operations for shell scripts and AI agents

- Stars: 2
- Forks: 0
- Watchers: 2
- Open issues: 6
- License: MIT License
- Default branch: develop
- Created: 2026-09-03T06:53:29Z

## Languages

- Python
- Rust
- Shell

## Topics

- ai-agents
- cli
- coding-agents
- commonmark
- document-automation
- github-flavored-markdown
- markdown
- rust

## Top Contributors

- JonghunYu (37 contributions)

---

## README

# Texio

Reliable Markdown operations for shell scripts and AI agents.

Texio extracts and surgically edits Markdown by document structure. Use it when
regular expressions are unsafe and rewriting the complete file would create
unnecessary changes.

> `grep` finds text. `sed` changes text. Texio understands Markdown.

## Extract a Markdown section

Install from crates.io with a current stable
Rust toolchain, or use the platform-specific binary instructions.

```sh
cargo install texio-cli --locked
texio --version
```

Create a small document and inspect its structure:

```sh
printf '# Demo\n\n## Installation\nold command\n\n## Usage\nkeep this\n' > demo.md
texio headings demo.md --json
texio section demo.md Installation
```

Preview one section change, then apply the same change after checking the diff:

```sh
texio replace demo.md --section Installation --text 'cargo install texio-cli --locked' --dry-run
texio replace demo.md --section Installation --text 'cargo install texio-cli --locked' --write
texio section demo.md Installation
```

The preview leaves the file unchanged; the write preserves the Usage section.
Copy the agent policy for future edits. Missing or
duplicate headings cause an error rather than selecting a guessed target.

The four-fixture benchmark measured 82.8% fewer
context-proxy tokens versus an idealized whole-file rewrite. This is not a
model-token or billing measurement. A source build can take longer than five
minutes; use a binary archive for the fastest first edit.

## Replace one section safely

Preview the proposed change:

```sh
texio replace README.md \
  --section "Installation" \
  --from installation.md \
  --dry-run
```

Apply it by replacing `--dry-run` with the explicit `--write` flag. Texio
preserves content outside the selected section and refuses ambiguous heading
matches.

## List headings for an agent

```sh
texio headings README.md --json
```

```json
[{"level":1,"title":"Texio"},{"level":2,"title":"Installation"}]
```

## Installation

Install the published crate with a current stable Rust toolchain:

```sh
cargo install texio-cli --locked
texio --version
```

From a checkout, use `cargo install --path . --locked`.

For Linux x86-64, Windows x86-64, Intel macOS, and Apple Silicon macOS,
follow the binary installation and checksum instructions.
The same page documents the organization Homebrew tap and platform limits.

## Status

Texio is an early preview. The initial contract focuses on section extraction,
heading discovery, and surgical replacement. CommonMark and GitHub Flavored
Markdown compatibility work is ongoing.

Current parsing is powered by `pulldown-cmark` and supports ATX and Setext
headings while ignoring heading-like text inside fenced code blocks. Replacement
is atomic and preserves the target file's permissions.

See Markdown support for dialect coverage, editing
guarantees, and current limitations.
See the CLI contract for stdin/stdout behavior, JSON
schemas, safety modes, compatibility policy, and exit codes.

## Why Texio?

AI agents frequently rewrite entire Markdown files to change one section. That
uses unnecessary context and can alter unrelated content. Texio provides a
small, deterministic operation that is easier to review and automate.

- Try ten tested agent recipes.
- Copy the agent instructions.
- Install the agent skill and review its
 automatic-selection evidence.
- Read Stop letting agents rewrite your entire README.
- Inspect and reproduce the public benchmark.

## Agent token benchmark

Across four Markdown fixtures, Texio used **45 context-proxy tokens instead of
261** for an idealized whole-file rewrite: **82.8% fewer tokens**. Texio also
passed 4/4 cases, compared with 3/4 for the whole-file baseline and 2/4 for the
regex baseline.

The same result is provided below as stable, agent-readable data:

```yaml
benchmark: markdown-agent-editing-v0.1.1
cases: 4
metric: unicode-word-and-punctuation-proxy
texio:
  input_tokens: 32
  output_tokens: 13
  total_tokens: 45
  passed: 4
whole_file:
  input_tokens: 175
  output_tokens: 86
  total_tokens: 261
  passed: 3
savings_vs_whole_file:
  input_percent: 81.7
  output_percent: 84.9
  total_percent: 82.8
regex:
  total_tokens: 45
  passed: 2
source: benchmarks/results/v0.1.1.json
caveat: deterministic context proxy; not model tokenizer or billing tokens
```

These numbers measure the checked-in fixtures and CLI traffic, not every token
an agent may consume while reasoning. See the methodology
and raw result to reproduce or audit them.

## License

MIT

# Text Expander & Autofill - Slash Commands Anywhere - Chrome Web Store

## 导航

- 项目页：[[10-项目/github.com_2e51762e]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
