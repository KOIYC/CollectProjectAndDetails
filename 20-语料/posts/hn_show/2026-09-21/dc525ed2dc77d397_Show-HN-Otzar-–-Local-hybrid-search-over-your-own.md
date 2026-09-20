---
type: "corpus"
item_id: "dc525ed2dc77d397"
title: "Show HN: Otzar – Local hybrid search over your own files"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49113718"
project_url: "https://github.com/danielfleischer/otzar"
author: "yruthewaythatur"
published_at: "2026-07-30T18:22:59Z"
captured_at: "2026-09-21T03:11:14+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-21"
pub_day: "2026-07-30"
tags:
  - 语料
  - hn_show
  - author_yruthewaythatur
  - story_49113718
  - show_hn
metrics: {"points": 2, "comments": 0, "engagement_velocity": 2}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:83d"
---

# Show HN: Otzar – Local hybrid search over your own files

> [!info] 一句话导读
> danielfleischer/otzar

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49113718>
> 指标：点赞=2 · 评论=0 · engagement_velocity=2
> 作者：yruthewaythatur　|　发布：2026-07-30T18:22:59Z
> 项目链接：<https://github.com/danielfleischer/otzar>
> 采集：2026-09-21T03:11:14+08:00　|　id：`dc525ed2dc77d397`

## 正文

# danielfleischer/otzar

Local hybrid search over your own files — dense vectors, BM25, and metadata filters in one query. The same binary is an MCP server, so agents can search your notes.

- Stars: 1
- Forks: 0
- Watchers: 1
- Open issues: 0
- License: GNU General Public License v3.0
- Default branch: main
- Created: 2026-07-29T18:41:59Z

## Languages

- Clojure
- Go
- Makefile

## Topics

- clojure
- embeddings
- full-text-search
- golang
- lucene
- model-context-protocol
- ollama
- personal-knowledge-management
- semantic-search
- vector-search

## Top Contributors

- danielfleischer (81 contributions)

---

## README

# otzar

**Hybrid search over your own files** — dense vector similarity, BM25 keyword
matching, and metadata filters in a single query, running entirely on your
machine. A Clojure/Lucene server holds the index; a Go CLI is the UX; the same
binary speaks **MCP**, so Claude Code and friends can search your notes as a tool.

*otzar* (אוֹצָר) is Hebrew for **treasure** — and, fittingly, *thesaurus*.

```sh
otzar index -r ~/notes
otzar query "what did I decide about chunk overlap?"
```

```
#  score  path                     snippet
1  0.055  ~/notes/rag.md:42-47     Sentences are packed into windows of six, with two of…
2  0.031  ~/papers/rag.pdf p.4     Overlapping windows keep a claim and its evidence in…
```

## Install

Two files: the `otzar` client binary and `otzar-server.jar` — the whole server
packaged with its dependencies. Grab one of each from the
latest release; the jar is the same on every platform.

```sh
mkdir -p ~/.local/bin ~/.local/share/otzar
tar -xzf otzar_*_darwin_arm64.tar.gz -C ~/.local/bin
mv otzar-server.jar ~/.local/share/otzar/
```

You also need:

- **A JDK, 21 or newer**, to run the jar. `brew install openjdk` or any Temurin
 build will do.
- **Ollama** for embeddings: `ollama pull bge-m3`. It's the
 default for its multilingual coverage — notably Hebrew, which most small
 English-first embedding models handle poorly. Override with `OTZAR_EMBED_MODEL`.

otzar finds both on its own. The jar: `$OTZAR_SERVER_JAR`, the directory holding
the binary, `$XDG_DATA_HOME/otzar`, `~/.local/share/otzar`, then
` /share|lib/otzar` for a binary in ` /bin` — so one directory with
both files works, and so does a `/usr/local`-style split. The JVM: `$OTZAR_JAVA`,
`$JAVA_HOME`, `/usr/libexec/java_home`, Homebrew's keg-only `openjdk`, then
`PATH` — probing each by *running* it, since macOS ships a `/usr/bin/java` stub
that exists and fails. `otzar server status` prints what it resolved, which is the
quickest way to check an install.

Building from source: see `CONTRIBUTING.md`.

## Give it to Claude

The same binary is an MCP server, so an LLM host can search your index instead of
guessing. To register it with Claude Code:

```sh
claude mcp add notes -s user -- otzar mcp   # absolute path if otzar isn't on the host's PATH
```

It exposes three read-only tools — `search`, `get_document`, `list_indexed_paths`
— and starts the backing server itself, leaving it running when the host
disconnects. Writes stay on the CLI: an LLM should be able to *find* things, not
silently mutate the index.

**Name it after what you indexed, not after otzar.** The name becomes the tool
prefix the model sees: `notes` gives it `mcp__notes__search`, which reads like
something to reach for when you ask about your notes, where `mcp__otzar__search`
is a word that means nothing to a model. Pick `papers`, `research`, `journal` —
whatever your corpus actually is. Nothing depends on it; `claude mcp remove `
and add it again to change your mind.

For the same reason, tell your host what's in there. The tool descriptions
describe the *shape* of a corpus because they ship to everyone; only you know it
holds ten years of org-mode journals. Two lines in `CLAUDE.md` close the gap:

```markdown
My notes and reading live in an otzar index (~/Documents/Notes, org + markdown).
When I ask what I wrote, read, or think about something, search it before
answering rather than guessing.
```

Drop `-s user` to scope it to the current project, or use `-s project` to write a
`.mcp.json` that ships with the repo. `claude mcp list` shows what's registered
and whether it connects.

## Commands

```sh
otzar index notes.md report.pdf     # index individual files
otzar index -r ~/notes              # descend into a directory
otzar index -f ~/notes              # force re-embed even if unchanged
otzar index --now                   # re-scan everything already indexed

otzar query "vector database tradeoffs"           # hybrid (default)
otzar query -m keyword "exact phrase"             # BM25 only
otzar query -m vector "semantically similar"      # kNN only
otzar query -k 5 -e md,txt -p ~/notes/ "topic"    # top-5, filtered

otzar list                          # every indexed path, one per line (alias: ls)
otzar admin stats                   # documents and chunks in the index
otzar admin prune                   # drop indexed files that no longer exist
otzar admin clear                   # wipe the entire index
otzar admin reindex                 # re-embed everything

otzar server status                 # health, index stats, which server it resolved
otzar server restart                # picks up server changes
otzar server watch enable --interval 30m   # auto-reindex on a timer (off by default)

otzar completion fish | source      # also bash, zsh, powershell
```

A few things worth knowing:

- **You never have to start the server.** Anything that talks to the *index* —
 `index`, `query`, `list`, `admin *`, `otzar mcp` — boots it if it isn't running,
 with a one-line notice on stderr so piped output stays clean. The `server`
 commands stay explicit, since a `status` that started what you asked it to report
 on would be no use.
- **Re-indexing is cheap.** Unchanged files are skipped, so `otzar index -r ~/notes`
 is safe to re-run. `otzar index --now` re-scans every tree you've indexed —
 picking up what's new, changed, or deleted — and `server watch` does the same
 thing on an interval, without loading the model when nothing changed.
- `--mode` picks the retriever; `--ext`, `--path`, and `--after` filter any mode.
- `-j/--json` on any command gives machine-readable output — for `query`, that
 includes the hybrid score breakdown.

## What it indexes

Plain text, markdown, and source code (read as-is); **HTML** (tags stripped in
place, so line numbers still point at the file); **PDF** (via PDFBox — soft line
wraps rejoined into prose; no OCR, so a scanned PDF is skipped); and **docx**
(paragraphs from `word/document.xml`; the old binary `.doc` is not supported).
Anything else is ignored.

Each format declares what a hit can cite, because that differs — a line for text
and HTML, a page for a PDF, a paragraph for a docx:

```
~/notes/rag.md:42-47        ~/papers/rag.pdf p.4        ~/notes/report.docx ¶12
```

Formats live in one registry, `server/src/rag/index/extractor.clj`, if you want to
add one.

## How it works

Files are extracted, split into sentences with the JDK's `BreakIterator` (no
model file, and it handles Hebrew), packed into overlapping chunks, embedded via
Ollama, and written to a single Lucene index that holds the inverted index, the
doc values for filters, and the HNSW vector graph in the same segment. A query
runs BM25 and kNN with the same filters and fuses the two rankings with
Reciprocal Rank Fusion.

`docs/design.md` explains the choices and the alternatives that
were rejected; `docs/api.md` is the HTTP contract between the two
halves.

## Status

Working end to end and in daily use: hybrid retrieval, Ollama-backed embeddings,
metadata filters, live indexing progress, the MCP adapter, auto-reindex, and index
maintenance. Local-only, single-user, no auth — by design.

**Test coverage:** 150+ tests across the Clojure server and Go client, covering
filesystem safety, extraction, indexing, retrieval, lifecycle, and MCP boundaries.

Personal project, best-effort maintenance: issues and ideas welcome, pull requests
probably not. See `CONTRIBUTING.md` to build and hack on it.

## License

GPL-3.0 — see `LICENSE`.

# yashmahajan10/llm-differential-privacy-gateway

## 导航

- 项目页：[[10-项目/github.com_9be95eba]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
