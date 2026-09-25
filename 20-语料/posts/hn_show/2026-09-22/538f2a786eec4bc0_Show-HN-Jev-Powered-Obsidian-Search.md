---
type: "corpus"
item_id: "538f2a786eec4bc0"
title: "Show HN: Jev Powered Obsidian Search"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49795109"
project_url: "https://github.com/Emlembow/jev-graph-search"
author: "MikeLembo"
published_at: "2026-09-22T00:05:39Z"
captured_at: "2026-09-25T13:54:35+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-22"
pub_day: "2026-09-22"
tags:
  - 语料
  - hn_show
  - author_MikeLembo
  - story_49795109
  - show_hn
metrics: {"points": 3, "comments": 0, "engagement_velocity": 3}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:3d"
---

# Show HN: Jev Powered Obsidian Search

> [!info] 一句话导读
> Emlembow/jev-graph-search

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49795109>
> 指标：点赞=3 · 评论=0 · engagement_velocity=3
> 作者：MikeLembo　|　发布：2026-09-22T00:05:39Z
> 项目链接：<https://github.com/Emlembow/jev-graph-search>
> 采集：2026-09-25T13:54:35+08:00　|　id：`538f2a786eec4bc0`

## 正文

# Emlembow/jev-graph-search

Jev-assisted retrieval and evidence-preserving inspection for local Markdown, Obsidian vaults, and Logseq Markdown graphs.

- Stars: 8
- Forks: 1
- Watchers: 8
- Open issues: 0
- License: MIT License
- Homepage: https://www.skills.sh/emlembow/jev-graph-search/jev-graph-search
- Default branch: main
- Created: 2026-09-21T19:00:07Z

## Languages

- JavaScript

## Topics

- logseq
- markdown
- obsidian

## Top Contributors

- Emlembow (7 contributions)

---

## README

# Jev Graph Search

Jev Graph Search helps an AI agent find useful notes and passages in a local Obsidian vault or a folder of Logseq Markdown notes. It makes a shortlist on your machine, then uses Jev to rank those candidates against your question. The result includes the original passage and source reference, so the agent can point back to the note it used.

Run it from the terminal or install the agent skill. An optional JSON snapshot is supported as well. See Jev for the ranking service.

Get started · Obsidian and Logseq · Agent skill · Documentation

Tax-code benchmark: source recall without versus with Jev is 33.2% versus 73.2% at top 1, 53.5% versus 80.1% at top 3, and 63.9% versus 81.8% at top 5.

On one 8,851-node tax-code graph, Jev reranking raised top-five source recall from **63.9% to 81.8%**.

## Get started

You need **Node.js 20+** and npm. Git is needed for the example checkout and skill installation. The CLI has no runtime dependencies.

Run the exact npm release:

```sh
npx --yes --package=jev-graph-search@0.2.2 jev-graph-search setup
```

At setup, use **↑/↓ and Enter** to choose TypeSafe or OpenRouter, then paste your API key into the hidden prompt. Your key is saved in a private per-user configuration file, outside the graph.

Search a directory of Markdown files or an optional JSON graph snapshot:

```sh
npx --yes --package=jev-graph-search@0.2.2 jev-graph-search search "Why did we choose this database?" --input ./ObsidianVault
```

For a persistent `jev-graph-search` command:

```sh
npm install --global jev-graph-search@0.2.2
jev-graph-search --help
```

The release workflow publishes exact package versions with npm trusted publishing and provenance. Pin the package version in automation so upgrades are deliberate.

 Try the included example without a key

```sh
git clone --branch v0.2.2 --depth 1 https://github.com/Emlembow/jev-graph-search.git
cd jev-graph-search
node bin/jev-graph-search.js search "Why PostgreSQL?" --input examples/memory.json --offline
node bin/jev-graph-search.js audit --input examples/memory.json
```

`--offline` uses local lexical ranking. Remove it after setup to use Jev.

## Agent skill

```sh
npx skills add Emlembow/jev-graph-search --skill jev-graph-search
```

The skill tells an agent how to retrieve evidence from local Markdown graphs or JSON snapshots, inspect links, and suggest where to save a new note. It invokes the CLI above. Installing the skill does not configure API keys or read your files.

## Commands

With the CLI installed, try these operations:

```sh
# Retrieve source passages from an Obsidian vault
jev-graph-search search "What did we decide?" --input ./ObsidianVault

# Propose where a new memory belongs
jev-graph-search place "We chose PostgreSQL for transactions" --input ./ObsidianVault

# Audit explicit structure; add --semantic for Jev suggestions
jev-graph-search audit --input ./ObsidianVault

# Follow existing links in an optional JSON snapshot without a provider key
jev-graph-search traverse --input snapshot.json --from PAGE_A --to PAGE_B
```

Search starts with keyword matches and a limited set of linked notes, then sends selected titles, bounded aliases, and content excerpts to Jev for reranking. Results retain the exact source evidence. `place` and migration commands propose changes without writing to your graph. Use `jev-graph-search --help` for all commands.

## Obsidian and Logseq

Set `--input` to a local Markdown directory. Obsidian vaults are read recursively, including nested folders. Logseq graphs are supported through their Markdown `pages/` and `journals/` files; database and Org-mode formats are outside this interface. Hidden paths and symbolic links are skipped. Reading the graph does not create a backup or export.

Common page metadata works in either graph style:

```markdown
---
aliases: [Database decision, PostgreSQL decision]
tags: [architecture, storage]
---
# Database decision

## Related
- [[Transactions]]
See also Migration notes
```

Top-level YAML `aliases` and `tags` lists, plus unindented Logseq `alias::` and `tags::` page-property lines, are indexed as page-level metadata. Indented block-property lines remain page content. Wikilinks and relative Markdown links become explicit graph evidence.

```sh
# Obsidian
jev-graph-search search "database decision" --input ./ObsidianVault --offline

# Logseq Markdown graph
jev-graph-search audit --input ./logseq-graph --offline
```

## Configuration

- Interactive setup: `jev-graph-search setup`.
- Environment setup: export `TYPESAFE_API_KEY` or `OPENROUTER_API_KEY`, then run `jev-graph-search setup --from-env` to persist it.
- Diagnostics: `jev-graph-search config` and `jev-graph-search doctor` show redacted configuration.
- Cache: semantic scores are cached; `--no-cache` requests fresh scores.
- Local search: `--offline` explicitly selects lexical ranking.

Keys are never accepted as command-line arguments. Saved credentials use a `0600` file inside a `0700` directory. Storage and provider options →

## Documentation

- Local graph schema and Markdown inputs
- Provider setup and credential storage

Jev ranks only the shortlist it receives. It cannot recover missing candidates or show that the available evidence is sufficient. Model suggestions are not links that already exist in the graph, and a partial snapshot stays partial. The current default may still return results when the question has no answer in the graph.

## License

MIT © 2026 Emlembow.

Error fetching https://www.reddit.com/r/buildinpublic/comments/1wg3s6s/give_me_a_link_to_your_project_and_ill_roast_it/: CRAWL_LIVECRAWL_TIMEOUT
Error fetching https://www.reddit.com/r/IndieDev/comments/1wgr4nz/criação_de_personagem/: CRAWL_LIVECRAWL_TIMEOUT
Error fetching https://i.redd.it/lfkani353mph1.png: CRAWL_LIVECRAWL_TIMEOUT

## 关联链接

- https://github.com/Emlembow/jev-graph-search.git
- https://i.redd.it/lfkani353mph1.png:
- https://www.reddit.com/r/IndieDev/comments/1wgr4nz/criação_de_personagem/:
- https://www.reddit.com/r/buildinpublic/comments/1wg3s6s/give_me_a_link_to_your_project_and_ill_roast_it/:
- https://www.skills.sh/emlembow/jev-graph-search/jev-graph-search

## 导航

- 项目页：[[10-项目/github.com_095448be]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
