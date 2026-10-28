---
type: "corpus"
item_id: "6da82e76b06bc777"
title: "Show HN: Aqueous Archive Format"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50267373"
project_url: "https://github.com/lifthrasiir/aqueous"
author: "lifthrasiir"
published_at: "2026-10-27T23:31:52Z"
captured_at: "2026-10-28T09:39:16+08:00"
lang: "en"
kind: "post"
topic: "开发者工具"
shard: "2026-10-28"
pub_day: "2026-10-27"
tags:
  - 语料
  - hn_show
  - author_lifthrasiir
  - story_50267373
  - show_hn
metrics: {"points": 3, "comments": 0, "engagement_velocity": 3}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:3d"
---

# Show HN: Aqueous Archive Format

> [!info] 一句话导读
> Aqueous Archive Format

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50267373>
> 指标：点赞=3 · 评论=0 · engagement_velocity=3
> 作者：lifthrasiir　|　发布：2026-10-27T23:31:52Z
> 项目链接：<https://github.com/lifthrasiir/aqueous>
> 采集：2026-10-28T09:39:16+08:00　|　id：`6da82e76b06bc777`

## 正文

# lifthrasiir/aqueous

Aqueous Archive Format

- Stars: 1
- Forks: 0
- Watchers: 1
- Open issues: 0
- License: Other
- Homepage: https://lifthrasiir.github.io/aqueous/spec/
- Default branch: main
- Created: 2026-10-13T21:30:16Z

## Languages

- Batchfile
- Bikeshed
- C
- C++
- JavaScript
- Makefile
- Python
- Rust
- Shell

## Topics

- backup
- compression
- compressor
- data-compression
- decompression
- decompressor

## Top Contributors

- lifthrasiir (490 contributions)

---

## README

# 💧 Aqueous

Aqueous is an archive format and an archiver, `aqr`, built around lossless recompression.
Most files people keep are already compressed, by encoders far weaker than what a modern
machine can afford: JPEG's and MP3's Huffman codes, deflate in PNG, ZIP, PDF and gzip, LZ4 and
Snappy in browser profiles and databases. Aqueous undoes that compression, codes the contents
with stronger models, and rebuilds the original files bit for bit on extraction.

- **Recompressors** for about twenty format families: images (PNG, JPEG, PSD, BMP and PNM,
 BCn textures in DDS), audio (MP3, FLAC, WAV, AIFF), documents and data (PDF, SQLite, text,
 FASTA, Wavefront OBJ), containers and general-purpose compression (gzip and zlib, ZIP, LZ4,
 LZO, LZMA, Snappy, tar, ar and cpio, git checkouts) and executables (PE and Mach-O). Each
 lives in its own `aqr-*` crate, with a `FORMAT.md` describing what it stores.
- **Self-describing archives.** A file's content is a *formula*, a small stack-machine program
 over stored blocks, which applies WebAssembly modules to undo what the compressor did. A
 decompressor needs no knowledge of the formats inside; known modules run natively, unknown
 ones in a sandbox.
- **Random access.** A file is extracted by reading little more than its own blocks, which the
 formula indexes. Archives can be extended by appending, and overlay archives describe a tree
 as changes to another.

The format is specified in `spec/index.bs` (an Editor's Draft, not yet
fixed). Aqueous is dedicated to the public domain, or under MIT-0 where that is not possible
(`LICENSE.txt`); see `CREDITS.md` for the projects its ideas
come from.

## Sneak peek

Matt Mahoney's 10 GB benchmark (79,431 files, 10.00 GB), on an Apple M4 (10 cores),
2026-10-27, at commit `d84deff`:

| method | size | compression | decompression |
|---|---|---|---|
| `tar \| zstd -3 -T10` | 4.68 GB | 33 s | |
| `tar \| zstd -3 -T10 --long=31` | 4.17 GB | 36 s | |
| zpaq 7.15 | 3.70 GB | | |
| **`aqr`** (level `mid`) | **2.630 GB** | 136 s (73 MB/s) | 19.2 s (521 MB/s, 2.84 GB peak) |

Compression includes the round-trip check of every file. Some formats alone, as
`archive / input` against `zstd -3` of the same files:

| format | aqr | zstd -3 |
|---|---|---|
| JPEG | 0.785 | 0.913 |
| PNG | 0.802 | 0.997 |
| MP3 | 0.853 ~ 0.890 | 0.971 |
| PE executables | 0.326 | 0.381 |
| SQLite | 0.227 | 0.366 |
| text (enwik9) | 0.253 | 0.312 |
| FASTA (hg19) | 0.218 | 0.309 |

The 10 GB archive includes its decoder modules. The figures by format are tentative: they were
measured before the modules were embedded in archives. How they were measured, and the
formats taken or not yet taken, are in
`docs/file-formats.md`.

## Building

```sh
cargo build -r -p aqr
target/release/aqr -c -o out.aqr some/directory   # compress
target/release/aqr -t out.aqr                     # test
target/release/aqr -d out.aqr                     # extract
```

The workspace's tests are slow in debug builds; run them with `cargo test -r`.

# chen-985211/cleancode

## 关联链接

- https://lifthrasiir.github.io/aqueous/spec/

## 导航

- 项目页：[[10-项目/github.com_dcc46e2d]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`开发者工具`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
