---
type: "corpus"
item_id: "e4cac036b28a648c"
title: "Show HN: License Detector – the fastest, most accurate license detection tool"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49510297"
project_url: "https://github.com/licensedetector/cli"
author: "eggbrain"
published_at: "2026-08-31T14:35:46Z"
captured_at: "2026-09-21T03:11:21+08:00"
lang: "en"
kind: "post"
topic: "开发者工具"
shard: "2026-09-21"
pub_day: "2026-08-31"
tags:
  - 语料
  - hn_show
  - author_eggbrain
  - story_49510297
  - show_hn
metrics: {"points": 4, "comments": 0, "engagement_velocity": 4}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:52d"
---

# Show HN: License Detector – the fastest, most accurate license detection tool

> [!info] 一句话导读
> The License Detector engine & CLI (Elastic License 2.0) — resolve lockfiles across 20+ ecosystems and reconcile each package's declared license against the text…

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49510297>
> 指标：点赞=4 · 评论=0 · engagement_velocity=4
> 作者：eggbrain　|　发布：2026-08-31T14:35:46Z
> 项目链接：<https://github.com/licensedetector/cli>
> 采集：2026-09-21T03:11:21+08:00　|　id：`e4cac036b28a648c`

## 正文

# licensedetector/cli

The License Detector engine & CLI (Elastic License 2.0) — resolve lockfiles across 20+ ecosystems and reconcile each package's declared license against the text it actually ships.

- Stars: 0
- Forks: 0
- Watchers: 0
- Open issues: 0
- License: Other
- Homepage: https://licensedetector.com/
- Default branch: main
- Created: 2026-08-24T23:38:31Z

## Languages

- Go
- Go Template
- Shell

## Topics

- c2pa
- copyright
- copyright-scan
- license-checker
- license-checking
- license-compliance
- license-detection
- licensing
- open-source-licensing
- oss-compliance
- sbom
- spdx-licenses

## Top Contributors

- scouttyg (2 contributions)

---

## README

# License Detector

**The license your dependencies actually ship — reconciled against what they claim.**

License Detector resolves a repository's dependency lockfiles, determines each
package's license by reading the **license text the package actually ships** and
reconciling it against the **declared** metadata, evaluates the result against a
policy you control, and reports a **pass / needs-review / blocked** verdict.

Most scanners report the label a package declares. License Detector reads the fine
print — so it catches the gap (the classic "declares MIT but ships ISC"), modified
license text, and dual/`OR` licensing that label-only tools miss.

This repository is the **open-source engine + CLI** (Elastic License 2.0). The hosted
GitHub App — PR checks, a dashboard, and media/asset-rights scanning on every pull
request — lives at **licensedetector.com**.

---

## Install

```sh
go install go.licensedetector.com/cmd/license-detector@latest
```

Requires **Go 1.26+**. The CLI is a single static binary with an embedded license
corpus — no service, no database, and it works offline against its on-disk cache.

## Quick start

```sh
# Scan the current repo against the built-in zero-config policy
license-detector scan .

# Explain one package's verdict, with the evidence behind it
license-detector explain npm/left-pad@1.3.0

# Identify a single local license file (what is it? has the text been modified?)
license-detector identify LICENSE

# Write a starter policy.yaml you can customize
license-detector init

# Policy-free inventory (never gates) — every dependency + its license
license-detector list .
```

`scan` discovers a `.license-detector.yaml` / `policy.yaml` by walking up from the
target path; pass `--policy ` to point at one explicitly, or `-` to read it from
stdin.

## Output formats

`scan` renders to `--format `:

| Format | Use |
|---|---|
| `text` (default) | human-readable verdict table |
| `json` | machine-readable results |
| `csv` | spreadsheet / inventory |
| `spdx`, `cyclonedx` | SBOM export |
| `sarif`, `github` | CI code-scanning surfaces |
| `markdown`, `html`, `notice`, `obligations`, `table`, `yaml` | docs, notices, attribution |

```sh
license-detector scan . --format cyclonedx -o sbom.json
license-detector scan . --format sarif -o results.sarif
```

## Using it in CI

`scan` sets its exit code so it can gate a build:

| Exit | Meaning |
|---|---|
| `0` | no blocked dependencies (and no configured `--strict`/`--fail-on` gate tripped) |
| `1` | a blocked dependency (or a configured gate tripped) |
| `2` | usage error (bad flags/args/policy, unreadable repo) |
| `3` | runtime failure (scan pipeline, render, or `--output` write failed) |

```sh
# Fail the job on any blocked dependency
license-detector scan . || exit 1
```

For a hosted, zero-config experience — a Check Run + self-updating comment on every
PR — install the GitHub App.

## Full reference & shell integration

The CLI can emit its own complete reference — every command and flag — so you never
have to guess:

```sh
license-detector docs -o cli-reference.html   # self-contained HTML reference of the whole CLI
license-detector man > license-detector.1     # man page (roff), for packaging
license-detector help                         # top-level help; add --help to any subcommand
license-detector scan --help                  # full flag reference for a command
```

Shell completion for `bash`, `zsh`, or `fish`:

```sh
license-detector completion zsh > _license-detector   # then put it on your $fpath
```

For a single package's evidence as machine-readable JSON:

```sh
license-detector explain npm/left-pad@1.3.0 --format json
```

## Ecosystems

21 ecosystems, discovered anywhere in the tree (monorepos included):

Cargo · CocoaPods · Composer · Conan · Conda · Go modules · Gradle · Hackage · Hex ·
Julia · Maven · npm · NuGet · opam · pip / PyPI · pub (Dart) · renv (CRAN) · RubyGems ·
shards (Crystal) · Swift · Unity

## Offline & caching

```sh
license-detector scan . --offline        # resolve from the disk cache only, no network
license-detector scan . --cache-dir ./x  # override the cache location
```

`--offline` degrades uncached dependencies to needs-review; pair it with
`--fail-on partial` to fail on anything unresolved.

## Deep scan (assets)

A deep scan additionally reads the **rights baked into media you ship** — stock and
press-agency credits, rights-managed markers, and C2PA content credentials (including
AI-generation provenance) across images, video, audio, and 3D models:

```sh
license-detector scan . --deep
```

## License

**Elastic License 2.0** — see `LICENSE`. Free to use, copy, modify, and
redistribute, with the ELv2 limitations (no providing the software as a hosted/managed
service to third parties, no circumventing the license key, no removing notices).

Copyright © 2026 Solid Gradient LLC (Scott Goci).

## Contact

- General & support: **scott@licensedetector.com** · licensedetector.com
- Security: **security@licensedetector.com** (see `CONTRIBUTING.md`)

## Contributing & this mirror

This repo is a **one-way mirror** of the `oss/` module from a private monorepo — see
`CONTRIBUTING.md` for how issues and changes flow. The hosted
product and its source (the server, billing, dashboard) are separate and proprietary.

# mQuark Actionful App

## 关联链接

- https://licensedetector.com/

## 导航

- 项目页：[[10-项目/github.com_a3201053]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`开发者工具`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
