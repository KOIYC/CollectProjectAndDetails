---
type: "corpus"
item_id: "a1845b3cf112b660"
title: "Show HN: Rheo 0.4.0"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=48730169"
project_url: "https://github.com/freecomputinglab/rheo"
author: "breezykermo"
published_at: "2026-06-30T09:01:13Z"
captured_at: "2026-09-21T02:53:12+08:00"
lang: "en"
kind: "post"
topic: "开发者工具"
shard: "2026-09-21"
pub_day: "2026-06-30"
tags:
  - 语料
  - hn_show
  - author_breezykermo
  - story_48730169
  - show_hn
metrics: {"points": 3, "comments": 0, "engagement_velocity": 3}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:113d"
---

# Show HN: Rheo 0.4.0

> [!info] 一句话导读
> freecomputinglab/rheo

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=48730169>
> 指标：点赞=3 · 评论=0 · engagement_velocity=3
> 作者：breezykermo　|　发布：2026-06-30T09:01:13Z
> 项目链接：<https://github.com/freecomputinglab/rheo>
> 采集：2026-09-21T02:53:12+08:00　|　id：`a1845b3cf112b660`

## 正文

# freecomputinglab/rheo

Typesetting and static site engine based on Typst

- Stars: 185
- Forks: 4
- Watchers: 185
- Open issues: 8
- License: Apache License 2.0
- Homepage: https://rheo.ohrg.org
- Default branch: main
- Created: 2025-10-06T13:13:16Z

## Languages

- CSS
- JavaScript
- Just
- Nix
- Rust
- Shell
- TeX
- Typst

## Top Contributors

- breezykermo (178 contributions)
- willcrichton (9 contributions)

---

## README

Rheo is a typesetting and static site engine based on Typst.
It compiles folders of Typst to PDF, HTML, and EPUB simultaneously, and ships a
development server for rapid website iteration. Rheo is a project of the
Free Computing Lab and part of the document
infrastructure described in Document Infrastructure for Augmented Reading.

Full documentation lives at **rheo.ohrg.org**.

## Usage

Compile every `.typ` file in a directory to all formats, recompiling on change:

```bash
# Clone the examples repo first
git clone https://github.com/freecomputinglab/rheo-tests.git ../rheo-tests
rheo watch ../rheo-tests/examples/blog_site --open
```

`--open` starts a development server at `http://localhost:3000` with automatic
browser refresh. Use `compile` for a one-shot build, and `--pdf` / `--html` /
`--epub` to select formats:

```bash
rheo compile ../rheo-tests/examples/blog_site --html
```

See the documentation for the full set of commands,
flags, and `rheo.toml` configuration.

## Installation

### Using cargo binstall (recommended)

cargo-binstall downloads a
prebuilt binary from GitHub Releases — no compiling from source:

```bash
cargo binstall rheo
```

### Using cargo

Rheo requires Rust and Cargo (install from rustup.rs):

```bash
# Install from crates.io
cargo install --locked rheo

# Or build from source
git clone https://github.com/freecomputinglab/rheo
cd rheo
cargo install --path crates/cli
```

### Using Nix flakes

With Nix and
flakes enabled:

```bash
nix develop   # enter the development environment
nix build     # or build the package
```

## Features

- **Multi-format compilation** — one source tree to PDF, HTML, and EPUB at once.
- **Relative linking** — link between documents with Typst label syntax; rheo
 resolves each link per output format (see below).
- **Spines** — combine and order files into a single PDF or multi-chapter EPUB.
- **Watch mode + dev server** — live reload at `http://localhost:3000`.
- **`rheo.toml` configuration** — formats, spines, assets, fonts, and per-format
 options.

See the documentation for details on every feature.

### Relative linking

Rheo assigns each source file a *handle* derived from its path, and you link
between documents using standard Typst label syntax:

```typst
See the #link(<about>)[about page] for more information.
Visit #link("https://example.com")[our website].
```

Rheo resolves these per format — to `.html` anchors in HTML, and to internal
document links in PDF and EPUB. A link to a non-existent file is a compile error.

Root-level files get a bare handle (` `); nested files use `:` as the path
separator (` `). See the
relative linking docs for handle rules and migrating
projects from Rheo version `<0.4.0`.

## License

Licensed at your option under either:
- Apache License, Version 2.0 (LICENSE-APACHE)
- MIT license (LICENSE-MIT)

## Contribution

Unless you explicitly state otherwise, any contribution intentionally submitted
for inclusion in the work by you, as defined in the Apache-2.0 license, shall be
dual licensed as above, without any additional terms or conditions.

# Noysr

## 关联链接

- http://localhost:3000`
- http://localhost:3000`.
- https://example.com
- https://github.com/freecomputinglab/rheo-tests.git
- https://rheo.ohrg.org

## 导航

- 项目页：[[10-项目/github.com_3dd9d594]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`开发者工具`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
