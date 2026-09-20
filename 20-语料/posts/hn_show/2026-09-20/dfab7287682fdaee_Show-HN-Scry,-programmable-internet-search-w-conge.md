---
type: "corpus"
item_id: "dfab7287682fdaee"
title: "Show HN: Scry, programmable internet search w/ congestion pricing"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49748041"
project_url: "https://scry.io/"
author: "Xyra"
published_at: "2026-09-17T23:15:57Z"
captured_at: "2026-09-20T14:57:50+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-20"
pub_day: "2026-09-17"
tags:
  - 语料
  - hn_show
  - author_Xyra
  - story_49748041
  - show_hn
metrics: {"points": 59, "comments": 25, "engagement_velocity": 59}
comments_count: 25
comments_total: 25
discovered_via: "hn:show_hn:90d"
---

# Show HN: Scry, programmable internet search w/ congestion pricing

> [!info] 一句话导读
> Scry — Give your agent the internet hypercube

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49748041>
> 指标：点赞=59 · 评论=25 · engagement_velocity=59
> 作者：Xyra　|　发布：2026-09-17T23:15:57Z
> 项目链接：<https://scry.io/>
> 采集：2026-09-20T14:57:50+08:00　|　id：`dfab7287682fdaee`

## 正文

Scry — Give your agent the internet hypercube

# Give your agent the internet hypercube.

Effortlessly run programs over billions of documents for fun and profit. Reddit, Hacker News, LessWrong, arXiv, Stack Exchange, Wikipedia, prediction markets and more, with millions of new posts and comments a day — rows by the thousand, or the answer itself, computed over every document that matches.

Rows held

≈357,680,548,306 across 44 public sources, advancing at the measured rate

Landed, last 24 h

≈+465,139,083 323K/min over the day to 10:21 UTC — rows newly held, live capture and backfill alike

Three fast query trails turn along the angled city grid and jump across present and historical layers, leaving long-lived paths behind them.

## Run arbitrary programs over the internet.

People search for pages; agents can query the underlying records. The question an agent actually has is rarely ten links. It might need every page that mentions this compound but not that patent, grouped by domain, since March. Scry runs that as a query instead of assembling it from repeated searches and scraped results.

### One table live

`reddit.posts` is effectively all of Reddit: every submission from 2005-06-23 to 2026-09-12, one row each. Completeness is measured, not estimated — post ids are one global counter, so held-versus-allocated is exact per month.

| `id` | String | one global base36 counter |
| --- | --- | --- |
| `subreddit` | String | |
| `author` | String | |
| `created_utc` | DateTime | |
| `title` | String | |
| `selftext` | String | body of a text post; empty for link posts |
| `score` | Int32 | net upvotes |
| `num_comments` | Int32 | |
| `upvote_ratio` | Float32 | |
| `domain` | String | where a link post points |
| `url` | String | |
| `search_text_lc` | String | lower(title + selftext), token-indexed |

The comment tree is `reddit.comments`, joined on `link_id = concat('t3_', id)`. Every relation is documented like this — columns, indexes, extent, known holes — at `GET /v1/scry/schema`. Source catalog →

### One query

Which way has LessWrong drifted on alignment: reachable, or out of reach? Mint the two poles as parallel sentences, take the balanced axis between them, average every chunk’s projection by year, and center on the era mean.

```
SELECT year, lean - avg(lean) OVER () AS drift, posts
FROM (
  SELECT toYear(p.original_timestamp) AS year,
         avg(scry_cosine_similarity(e.embedding,
           scry_contrast_axis_balanced(@achievable, @unreachable)))
           AS lean,
         uniq(e.target_key) AS posts
  FROM embeddings.chunks AS e
  JOIN forums.posts AS p ON p.post_key = e.target_key
  WHERE e.source = 'forum_posts'
    AND e.model_name = 'voyage-4-lite'
    AND p.source = 'lesswrong'
    AND p.original_timestamp >= '2009-01-01'
  GROUP BY year)
ORDER BY year LIMIT 100;
```

year out of reach reachable drift

2009 −0.0078

2010 −0.0078

2011 −0.0002

2012 −0.0047

2013 −0.0034

2014 −0.0011

2015 −0.0018

2016 +0.0067

2017 +0.0038

2018 +0.0109

2019 +0.0075

2020 +0.0086

2021 +0.0024

2022 +0.0017

2023 −0.0039

2024 +0.0004

2025 −0.0051

2026 −0.0062

Measured 2026-09-07 · 12 s · 906,548 posts and comments. Zero is the eighteen-year mean; the pole sentences are printed below. Runs as written against the live schema.

Scry gives your agent an incredibly powerful query substrate: Turing-complete search programs over the public record. Your agent figures the program out from your natural-language question — and you get as much low-level control and inspectability as you want.

This paradigm can be incredibly computationally heavy — sometimes heavier than state-of-the-art servers can handle — so we solve the limited-resource problem with free-floating, congestion-based pricing.

## Add Scry to your assistant.

Scry is an MCP server at `https://mcp.scry.io`. Connecting it takes about two minutes in ChatGPT or Claude and requires no code. The sign-in page also lets you create an account.

### ⬢ ChatGPT

1. Open ChatGPT on the web and go to Settings.
2. Turn on Developer mode. ChatGPT asks you to accept the risks.
3. Open connectors, click +, and enter a name (`scry`), a description (`programmatic search`), and the server URL `https://mcp.scry.io`. Click Create.
4. Complete the sign-in flow when ChatGPT sends you through it.
5. Scry appears as a connector. Select it, or call it with `@scry` in any chat. One setup covers the web and the ChatGPT mobile app — the easiest way to query the corpus from your phone.

### ✳ Claude

1. Open claude.ai and go to Settings → Connectors.
2. Click Add custom connector.
3. Name it `Scry`, set the URL to `https://mcp.scry.io`, and add it.
4. Complete the sign-in flow when Claude sends you through it.
5. Enable Scry from the tools menu in any chat. One setup covers Claude.ai, Desktop, and mobile.

### $ For developers

Claude Code, Codex, Cursor, or any MCP client connects with the same URL. Agents without an MCP client use the HTTP API with your key. Per-client steps live on the connect page.

Claude Code — one command, then /mcp to approve claude mcp add --transport http scry https://mcp.scry.io content_copy any other agent — paste this prompt Connect Scry content_copy

read the prompt text first

```
Scry: programmatic search over the public web, for agents.

Connect over MCP (preferred). Scry is an MCP server at https://mcp.scry.io. One URL, OAuth on first use, approve at scry.io.

- Claude Code:  claude mcp add --transport http scry https://mcp.scry.io   then run /mcp inside a session and approve.
- Codex:        codex mcp add scry --url https://mcp.scry.io && codex mcp login scry
- Claude.ai, Claude Desktop, ChatGPT (developer mode), Cursor, any MCP client: add a custom connector with that URL and approve the scry.io consent.
- No browser (CI, headless): Claude Code adds --header "Authorization: Bearer $SCRY_API_KEY"; Codex adds --bearer-token-env-var SCRY_API_KEY. Keys live in the dashboard at https://scry.io/dashboard.
- Tools: schema, sql, embed, feedback. Call schema once before writing SQL; its contract block carries the product contract and starter guidance, and each relation carries its stats. For "what does the fresh web say since my cutoff": embeddings.crawl_pages is a rolling fresh crawl of allowlisted high-information hosts whose page_ts is crawl-observation time — mint an @handle with embed, rank it with the vector helper, and add `WHERE page_ts > toDateTime('<your cutoff>')`; hydrate verbatim text from crawl.pages by url.

HTTP API (when MCP is not available). Base https://api.scry.io; send `Authorization: Bearer $SCRY_API_KEY` (load it from `~/.config/scry/env`). No key: stop and send the user to https://scry.io/dashboard.

- GET /v1/scry/context?mode=agent — the live contract.
- GET /v1/scry/schema — the only discovery authority. The default document carries full contracts for the start-here relations plus a compact index of the rest; `?relation=<name>[,<name>]` fetches more full contracts; `?mode=index` lists the whole catalog. Schema discovery is also one SQL call: `scry.relations` and `scry.columns` are the same catalog served as relations you can filter and join, e.g. SELECT relation FROM scry.columns WHERE name = 'author_id' LIMIT 100. Never guess column names; a wrong-column error returns the real roster.
- POST /v1/scry/query with `Content-Type: text/plain` — one read-only statement in the ClickHouse dialect, always with LIMIT (start at 20). Synchronous; long queries may stream whitespace before the JSON body. `WITH RECURSIVE` is served (`anchor UNION ALL step`, the CTE read only in the step's FROM/JOIN; a 111-iteration branch-on-state loop returns in ~50 ms) — each iteration rescans what the step joins, so declare `x-scry-max-seconds` on corpus-scale joins. A JSON body `{"program": {...}}` on the same route runs fixpoint graph walks that read only the frontier: citation, reply/quote, and thread-tree edges, in-walk filters, stratified negation, zero-egress per-depth counts. Docs: https://scry.io/docs/turing-complete-search; the calculus it implements: https://scry.io/docs/calculus-of-search.
- POST /v1/scry/rerank — order documents you already hold by an instruction.

Working rules

- Token filters run at the speed of their rarest token: include one distinctive token (a name, an identifier, an unusual word). All-common-word sets scan for 30-60s. For broad topics use the embedding helpers the schema advertises.
- To sort rows by an attribute you can describe, send `x-scry-rerank: <directive>` on POST /v1/scry/query (MCP: the rerank argument on sql). Runs on local models, $0; the response's rerank block says what applied.
- To see what a statement would touch before paying for it, send `x-scry-explain: 1` on POST /v1/scry/query (MCP: explain=true on sql): the response is ClickHouse's index analysis — parts and granules selected per index — plus the referenced relations, and the statement does not run.
- Use only relations and helpers the live schema returns; an omitted name is unavailable, and there is no fallback database.
- Use is governed by https://scry.io/legal/terms: no bulk redistribution of results, no reconstruction of a substantial portion of a corpus, no building a competing corpus, index, or dataset product from what the service returns.
- Keep source timestamp, observation time, load time, processing status, and quality fields distinct. A recent load is not a recent source event; an absent row is not source absence. Say which fields support each claim.
- Report the exact SQL, relations, row count, duration, truncation state, and accounting fields returned.

Example

claude mcp add --transport http scry https://mcp.scry.io

curl -s https://api.scry.io/v1/scry/query \
  -H "Authorization: Bearer $SCRY_API_KEY" \
  -H "Content-Type: text/plain" \
  --data "SELECT hn_id, title, original_author, original_timestamp, uri FROM hackernews.items WHERE title != '' ORDER BY hn_id DESC LIMIT 20"

```

A pasted prompt is instructions for your agent. Read prompts before you run them, whether they come from us or anyone else. Scry's is plain text, shown in full above.

Then ask it the highest-leverage question you can think of.

What do I install?

Only the MCP server: `https://mcp.scry.io`, in ChatGPT, Claude, Claude Code, Codex, Cursor, or any MCP client. The sign-in creates your account. Nothing runs on your machine.

When does my agent use Scry?

When the answer is a set of records, not a page: every comment naming a compound since March, every thread an author started, how a stance shifted over five years. Once connected, your agent sees Scry beside its web search and picks per question; you can also just tell it to use Scry.

How it works

Your agent reads the live schema (`/v1/scry/schema`), picks an enabled source-native relation and listed vector helpers, then writes one bounded query for phrase matching, time windows, joins, or vector composition. Result rows keep the source-native identifiers and provenance fields the relation provides.

Research agents check hundreds of sources instead of skimming five. Standing queries watch the web for any condition you can write down. Derived tables can be computed over the public web without building a crawler. Agents can send source requests or feedback through the feedback endpoint (authenticated `POST https://api.scry.io/v1/feedback`).

How fresh is the data?

For account holders, `/v1/scry/schema` states current query coverage and relation freshness per source. But sources like arXiv refresh every day, and Hacker News and LessWrong in under 15 minutes.

Mission

Scry is public-benefit infrastructure, subsidized for independent noncommercial research and carried by commercial engagements: search over public evidence, every result traceable to its source.

Commitments

Scry should make it easy for conscientious, prosocial forces to run wildly world-unflattening programs. Scry is not supposed to suck! We want to metabolize pain points fast. And Scry remains affordable to people who need it.

Scry is in open alpha: corpus, indexes, and interfaces move quickly. Accounts are self-serve, with free credit to start.

Who is it for?

Anyone with a question the public record can answer. Individual accounts are self-serve. For commercial use, large evaluations, custom source builds, or dataset engagements, write to [email protected].

Special access

The public corpus is the open tier. We hold vastly larger social archives under special access, granted person by person. Write to [email protected] with who you are, what you want to study, and five 10-minute time slots when you could take a video call — we talk first, then decide.

## 44 sources, counted every five minutes.

357,680,548,306 rows held · +460M landed this day · 24 of 42 sources moving

measured 10:21 UTC · `GET /v1/stats/wire`

### Social

| source | description | held ≈ | this day | rate | 48 h | 30 d |
| --- | --- | --- | --- | --- | --- | --- |
| Reddit comments | Near-complete Reddit comment archive, 2005 to present, from the Arctic Shift mirror: comments removed before capture are absent, bulk dumps land with lag, and the live tail captures a fraction of current volume, so a zero here is absence in landed data, not at the source. Temporal coverage is published on this schema entry: extent (computed from landed data, with computed_at) and known_holes (declared gaps with provenance). | 27,027,571,180 | +5.24M | 3.64K/min | | |
| Mastodon | Deduped Mastodon status surface from dump and live public-timeline landing. | 227,889,452 | +4.42M | 3.07K/min | | |
| Bluesky | Source-native Bluesky posts (app.bsky.feed.post), ~2.2B rows (measured 2026-09-10): the archived firehose capture (through 2026-06-23) unioned with the live Jetstream tail (from 2026-07-25; the interval between is a declared known hole). at_uri is the primary key, author_did carries identity (author_handle resolves on only ~41M rows, none after 2026-02-19), payload is the post text; embeddings.bluesky_posts is the ANN companion via at_uri. Temporal coverage is published on this schema entry: extent (computed from landed data, with computed_at) and known_holes (declared gaps with provenance). | 2,393,388,394 | +3.43M | 2.38K/min | | |
| Reddit posts | Near-complete Reddit submission (post) archive, 2005 to present, from the Arctic Shift mirror: title, selftext, score, comment count, and outbound domain/url per post; a post's comment tree lives in reddit.comments via link_id = concat('t3_', id). Posts removed before capture are absent, bulk dumps land with lag, and the live tail captures a fraction of current volume, so a zero here is absence in landed data, not at the source. Temporal coverage is published on this schema entry: extent (computed from landed data, with computed_at) and known_holes (declared gaps with provenance). | 3,739,565,015 | +920K | 639/min | | |
| Forums | Primary forum corpus: ~36M source-native posts and comments across ~4,300 forum sites (measured 2026-08-26; LessWrong, DataSecretsLox, DEV, EA Forum, 4chan boards, crypto governance, plus a long crawl-discovered tail). site_key is the community identity: the source column names only the curated lanes, and the majority of rows (~54%) carry source = 'manual', so enumerate site_key — not source alone — before scoping a community question. Archived base refreshed in place by live source-native forum tails. | 44,804,341 | +549K | 381/min | | |
| Hacker News | Source-native Hacker News PostgreSQL export. upvotes and comment_count are snapshots taken at first fetch — minutes after creation on the live tail — and are never refreshed; do not rank recent windows by engagement. Temporal coverage is published on this schema entry: extent (computed from landed data, with computed_at) and known_holes (declared gaps with provenance). | 45,358,375 | +13.6K | 9/min | | |
| LessWrong · in Forums | Primary forum corpus: ~36M source-native posts and comments across ~4,300 forum sites (measured 2026-08-26; LessWrong, DataSecretsLox, DEV, EA Forum, 4chan boards, crypto governance, plus a long crawl-discovered tail). site_key is the community identity: the source column names only the curated lanes, and the majority of rows (~54%) carry source = 'manual', so enumerate site_key — not source alone — before scoping a community question. Archived base refreshed in place by live source-native forum tails. | 924,530 | +218 | 9/h | | |
| EA Forum · in Forums | Primary forum corpus: ~36M source-native posts and comments across ~4,300 forum sites (measured 2026-08-26; LessWrong, DataSecretsLox, DEV, EA Forum, 4chan boards, crypto governance, plus a long crawl-discovered tail). site_key is the community identity: the source column names only the curated lanes, and the majority of rows (~54%) carry source = 'manual', so enumerate site_key — not source alone — before scoping a community question. Archived base refreshed in place by live source-native forum tails. | 192,677 | +60 | 3/h | | |
| Stack Exchange | Stack Exchange network: questions and answers across every landed site — dump-backed base plus a quota-bounded API tail. Temporal coverage is published on this schema entry, never assumed from this prose: extent (computed from landed data, with computed_at) and known_holes (declared gaps with provenance). | 83,477,246 | — | | | |

### Video & audio

held

1,266,931,613

this day

+87.2M

of the estate

0.4%

sources

1 · 1 moving

YouTube: metadata for 4.52 billion public videos, 1.12 billion caption transcripts over 824 million videos in 301 languages, and 1.22 billion comments. TikTok's public catalogue with captions where creators enabled them. Twitch chat across half a million channels, captured live.

| source | description | held ≈ | this day | rate | 48 h | 30 d |
| --- | --- | --- | --- | --- | --- | --- |
| Podcast episodes | Podcast episodes, one row per episode. | 1,266,931,613 | +87.2M | 60.6K/min | | |

### Writing & web

held

33,437,730,787

this day

+52.9M

of the estate

9.3%

sources

11 · 6 moving

811 million messages across 132,000 public lists and newsgroups — the Linux kernel list, netdev, Fedora, extropians, SL4, and the long tail — threaded by reply and root, queryable by list, author, date, and text.

A bibliographic catalog across OCLC/WorldCat, OpenLibrary, ISBNdb, and Google Books; public-domain full text in passages behind special access, granted person by person; FanFiction.net 1998 to 2015; Wikipedia, embedded for vector ranking. A live crawl of the web, and the cleaned reading layer of Common Crawl — articles, forums, and lists chosen by link-graph centrality, boilerplate stripped, every row keeping its WARC triple.

| source | description | held ≈ | this day | rate | 48 h | 30 d |
| --- | --- | --- | --- | --- | --- | --- |
| Web crawl artifacts | The crawl's stored captures: the fetched bytes behind each page, kept in segment packs. | 538,619,472 | +33.5M | 23.2K/min | | |
| Web crawl pages | Promoted text extractions of crawled web pages across every crawled host — the live crawl corpus. (The /search crawled_url family still reads the earlier static crawl in internet.documents; this relation is the fresh one.) | 557,238,420 | +18.0M | 12.5K/min | | |
| Substack comments | Comments beneath the Substack posts above. | 80,856,406 | +1.06M | 737/min | | |
| Substack posts | Substack posts, swept across a roster of publications that grows in place, custom domains included. | 28,458,014 | +353K | 245/min | | |
| Mailing lists | Public mailing-list and Usenet archive messages (extropians, SL4, and ~34k more lists); payload is the message text, threaded by parent/root keys. | 795,119,640 | +46.9K | 33/min | | |
| Wikipedia | English Wikipedia articles: one row per main-namespace page with title, full article text (payload), word count, categories (JSON), and quality flags — the full 6.2M-page set landed 2026-03 plus new articles from the recentchanges feed. embeddings.wikipedia_articles is its semantic companion (page_id). | 6,323,509 | +1.79K | 1/min | | |
| Common Crawl index | The Common Crawl per-capture URL index (CDX): one row per WARC capture — full URL decomposition, fetch status, MIME, CLD2 languages, content SHA-1 digest, and the exact WARC (filename, offset, length) provenance triple that re-derives the raw record from CC's public hosting. The existence-and-provenance layer: what the web had at a URL or domain, without text cost; content_digest joins duplicate content across captures. | 24,541,359,343 | — | | | |
| Common Crawl pages | Full plain text of the web as Common Crawl saw it: every WET capture of each held crawl (~2B pages per crawl, measured 2026-09-10). Whole-page extracted text — boilerplate (nav, cookie banners, footers) included; the same URL recurs across crawls by design (one row per capture). The recall layer: for indexed clean text grep commoncrawl.distillate or internet.text first and hydrate here. | 6,246,409,973 | — | | | |
| Wikidata | Wikidata items and claims from the weekly entity snapshot (CC0). | 373,834,895 | — | | | |
| Internet documents | Internet text documents across 85 source families (source keys e.g. crawled_url, lesswrong, mailing_list): one row per document, with content_text, uri, source, and quality fields. A frozen federated snapshot (nothing after ~2026-04) — contents overlap but do not match the live per-source tables; the live-forum sources' current rows land in forums.posts beside this archive. A record_ref ': ' resolves here by id (non-UUID refs resolve in forums.posts). The crawled_url family is the earlier static crawl; the live crawl corpus is crawl.pages. | 204,516,642 | — | | | |
| Common Crawl distillate | The cleaned reading layer of Common Crawl: genre-classified pages (article / forum / mailing_list) selected by link-graph centrality and URL-shape predicates, with boilerplate-free extracted text (~4.3KB avg vs ~8.2KB raw WET). Tier A rows also carry raw html, tier B text only, tier C provenance only — every row keeps the WARC triple to re-derive the original from CC hosting. Token-indexed (hasToken over lower(text)) and a branch of internet.text. | 64,994,473 | — | | | |

### Scholarship

held

6,011,491,657

this day

+63.3K

of the estate

1.7%

sources

9 · 4 moving

508 million OpenAlex works with the citation graph, 316 million carrying a DOI. arXiv, PubMed, PMC, Europe PMC with bioRxiv and medRxiv, INSPIRE-HEP, and a DOI-keyed journal full-text corpus, folded into one catalog that states which corpora hold each paper and whether its full text is on hand. Every ClinicalTrials.gov study.

| source | description | held ≈ | this day | rate | 48 h | 30 d |
| --- | --- | --- | --- | --- | --- | --- |
| arXiv | arXiv's bibliographic feed, with the TeX source and full text on hand where arXiv supplies it. | 6,840,539 | +45.0K | 31/min | | |
| PubMed | NCBI's annual PubMed baseline plus every daily update file, revisions and deletions settled in order. | 42,832,557 | +17.8K | 12/min | | |
| Paper extractions | Every academic-paper extraction attempt, revision, error, and provenance field. | 396,087,554 | +271 | 11/h | | |
| Academic papers (full text) | Exactly one deterministic successful text revision per source paper. quality_label states text fidelity: 'good' (93.8% of rows, measured 2026-09-10) is faithful full text; 'abstract' (0.5%, measured 2026-09-10) holds the abstract alone — no full text on hand, so a full-text census excludes it; 'zero_text' and 'short_per_page' mark scan-residue sources whose PDFs carry little or no text layer; 'low_text_ratio' marks image-heavy PDFs (large PDF relative to extracted text) — ~70% of these carry a healthy, usable text layer alongside figures/scans, so include them when recall matters; 'symbol_heavy' marks glyph/encoding damage; 'very_short' marks complete but tiny documents. Filter quality_label = 'good' for the strictly faithful core. Rows whose quality_flags contain 'tex_pandoc' or 'tex_clean' (extractor_version arxiv-texmd-v2) carry 'good' by construction, not by measurement; in 'tex_pandoc' rows LaTeX macros pandoc could not expand are dropped silently, and 'tex_clean' rows keep raw unexpanded TeX, so counts and other macro-valued numbers may be missing — verify against another rendering. pdf_bytes > 0 marks a PDF-backed row (the source PDF's size); extractor_version and converter name the route the text took (PDF text layer, OCR, arXiv TeX or ar5iv HTML, PMC XML, a preprint abstract); artifact_path is the extraction artifact — a text shard or the upstream page — never the PDF itself. How many rows, papers, PDF-backed or TeX-derived texts, and tokens are on hand is served measured on this entry's corpus_status (with computed_at), never quoted here. | 91,217,841 | +271 | 11/h | | |
| OpenAlex citations | Reverse citation edges of the OpenAlex graph: one row per (cited work, citing work) with the citing work's publication date — who cites this paper, newest first, in milliseconds. The keyed complement of openalex.works.referenced_works (3.09B edges, measured 2026-09-10; the equivalent has(referenced_works, id) scan over works takes 2-8 s). Walk references forward through works.referenced_works, walk citations backward here; hydrate either end via openalex.works. | 3,086,374,182 | — | | | |
| Library catalog records | Bibliographic catalog records across OCLC/WorldCat, OpenLibrary, ISBNdb, and Google Books. | 1,527,812,492 | — | | | |
| OpenAlex works | OpenAlex scholarly-work metadata snapshot: title, venue, year, DOI, authorships (author id, name, ORCID, institutions, corresponding flag), topics, concepts, keywords, funders, open-access locations, citation counts, and the citation graph (referenced_works). 508.1M unique works over ~510.4M physical ReplacingMergeTree rows (measured 2026-09-10; count with uniq(id), an estimate within about 1%); 316.1M carry a DOI, 266.9M an abstract_inverted_index, 460.6M authorships. doi_norm (lowercase bare DOI) joins academic.papers full text via doi_norm = decodeURLComponent(paper_key); paper_key keeps the first slash literal (10.48550/arxiv.2211.09527) and percent-encodes later ones (10.18653/v1%2f2024.acl-long.331). | 510,372,821 | — | | | |
| Crossref | The Crossref public data file (March 2026): one row per registered DOI work. | 179,535,192 | — | | | |
| Patents | Patent publications from the Google Patents public dataset. | 170,418,479 | — | | | |

### Markets

held

1,939,537,723

this day

+23.3M

of the estate

0.5%

sources

5 · 4 moving

Kalshi (188 million markets), Polymarket, Manifold, and Metaculus: markets, comments, and resolution context, plus all 23 million Manifold bets, each carrying the market probability before and after it.

| source | description | held ≈ | this day | rate | 48 h | 30 d |
| --- | --- | --- | --- | --- | --- | --- |
| Kalshi markets | Every Kalshi market as the public API shows it, swept continuously: status, settlement, and probability observations, append-only. | 491,735,680 | +11.2M | 7.76K/min | | |
| Kalshi trades | Public Kalshi executions: realized price and liquidity history, landed within minutes of the trade. | 513,697,123 | +10.8M | 7.47K/min | | |
| Polymarket trades | Public Polymarket trades, one row per execution. | 297,375,048 | +1.35M | 935/min | | |
| Polymarket markets | Polymarket markets: title, category, status, resolution, open/close/settle times, volume, liquidity, probability. | 4,755,034 | +64.3K | 45/min | | |
| Market trades (unified) | One unified trade stream across Kalshi, Polymarket, and Manifold, each trade carrying the market probability before and after it. | 631,974,838 | — | | | |

### Records

held

1,228,644,106

this day

+2.55K

of the estate

0.3%

sources

3 · 1 moving

59 million SEC EDGAR filing documents in full text — annual and quarterly reports, current reports, insider filings. The DOJ Epstein releases as a queryable artifact index. Grant and funding records from public releases.

| source | description | held ≈ | this day | rate | 48 h | 30 d |
| --- | --- | --- | --- | --- | --- | --- |
| SEC filings | SEC EDGAR filings — annual and quarterly reports, current reports, insider filings — in full text, plus the quarterly financial-statement numbers. | 234,032,005 | +2.55K | 2/min | | |
| Google Trends | Google Trends top and rising search terms, daily and hourly. | 560,148,251 | — | | | |
| FEC transactions | FEC campaign-finance transactions by committee and candidate, from the FEC bulk files. | 434,463,850 | — | | | |

### Code

held

43,891,265,580

this day

+1.82M

of the estate

12%

sources

5 · 1 moving

408 million GitHub repositories as Software Heritage observed them — including the ones since deleted, renamed, or taken private; one owner lookup returns a person's entire public footprint. The package registries as one catalog: npm, Go, PyPI, NuGet, Packagist, crates.io, and about thirty more.

| source | description | held ≈ | this day | rate | 48 h | 30 d |
| --- | --- | --- | --- | --- | --- | --- |
| GitHub archive events | The GH Archive event stream, hour by hour: every public push, issue, pull request, star, and fork on GitHub. | 11,167,384,567 | +1.82M | 1.26K/min | | |
| deps.dev graph | The deps.dev dependency graph: package-to-package edges across open ecosystems, from the public snapshot. | 25,192,519,296 | — | | | |
| Software Heritage revisions | Commits from the Software Heritage graph export — the history layer over every archived forge origin. | 5,940,997,207 | — | | | |
| Package registries | Package-to-repository links across npm, Go, PyPI, NuGet, Packagist, crates.io, and about thirty more registries, as one catalog. | 1,152,917,663 | — | | | |
| Software Heritage origins | The forge origins Software Heritage has archived, with visit history — including the ones since deleted, renamed, or taken private. | 437,446,847 | — | | | |

### Undisclosed

held

236,342,892,837

this day

+280M

of the estate

66%

sources

1 · 1 moving

Vastly larger social archives sit behind special access, granted person by person.

| source | description | held ≈ | this day | rate | 48 h | 30 d |
| --- | --- | --- | --- | --- | --- | --- |
| 22 undisclosed sources | Vastly larger social archives sit behind special access, granted person by person. | 236,342,892,837 | +280M | 195K/min | | |

* how the count is kept

* counted since the census began. Landed means newly held: a row the census counted for the first time, whether captured live or backfilled from an archive — the estate’s intake, not the internet’s own pace. A count that fell — crawls retired to cold storage, duplicates merged away — reads trimmed and is not a landing.

Held and missing are published, never rounded away. Reddit numbers its comments with one global counter, so the 6% not held is an exact subtraction, and every relation carries its computed extent and declared holes on its schema entry — an empty result inside a measured extent means absence, not a gap.

## Embedding vectors are, in fact, algebraically compositional.

This means:

- the difference between two embeddings is itself a direction with a meaning;
- the mean of several is a concept;
- projecting one onto another keeps or removes one component of what a text is about.

Most systems hide embeddings behind a similarity API and throw that structure away. In Scry a vector is a first-class value:

- mint one from any text;
- add, subtract, and project them in a query;
- rank a whole corpus along the result.

Text search speaks a full operator grammar — exact phrases, exclusion, OR, regex, fuzzy, proximity — and `scry_lex` carries that whole grammar into the query as one predicate, compiled server-side to each relation’s own text indexes. Everything below runs as written against the live schema.

scry_centroid([@metric, @school, @reward]) — three descriptions averaged into one concept, a direction to rank a corpus by.

scry_contrast_axis_balanced(@achievable, @unreachable) — two sentences’ difference is a direction; a document’s cosine to it is where it lands, everything orthogonal set aside.

The same axis over every corpus with Voyage-4 vectors, on-topic documents only (cosine ≥ 0.5 to the poles’ centroid): 10–90% run, middle half, median. The Congressional Record and Kalshi hold nothing on topic. Measured 2026-09-11, 13–67 s per corpus.

### Can you find the failure mode without knowing its name?

Describe Goodhart’s law three ways — metrics, classrooms, reward hacking — average the three vectors into one, and rank every embedded LessWrong post by it while excluding every post that contains the word. The top five are specification gaming, test-score gaming, and fitness-seeking AIs: 51,890 posts ranked in 9 s, measured 2026-09-07.

```
POST /v1/scry/embed  {"name": "metric", "text": "Once a measure becomes a target, people improve the reported number instead of the outcome it was supposed to measure. The metric rises while the underlying objective gets worse."}
POST /v1/scry/embed  {"name": "school", "text": "A school is rewarded for its students test scores. Teachers teach to the test and exclude weak students, improving the ranking without improving education."}
POST /v1/scry/embed  {"name": "reward", "text": "An agent discovers a way to maximize its reward signal without doing the task its designer intended. Optimizing the proxy breaks its relationship with the real goal."}
POST /v1/scry/embed  {"name": "proxy", "expression": "scry_centroid([@metric, @school, @reward])"}

SELECT uri, any(title) AS title, max(similarity) AS score
FROM (
  SELECT p.uri, p.title,
         scry_cosine_similarity(e.embedding, @proxy) AS similarity
  FROM embeddings.chunks AS e
  JOIN forums.posts AS p ON p.post_key = e.target_key
  WHERE e.source = 'forum_posts' AND e.model_name = 'voyage-4-lite'
    AND e.chunk_index = 0 AND p.source = 'lesswrong' AND p.kind = 'post'
    AND NOT hasToken(lower(p.payload), 'goodhart'))
GROUP BY uri
ORDER BY score DESC, uri
LIMIT 5;

→ Specification gaming: the flip side of AI ingenuity  0.701
  Improving Teaching Effectiveness: Final Report          0.687
  Risk from fitness-seeking AIs: mechanisms and mitigations  0.683
```

### Which way has LessWrong drifted on alignment: reachable, or out of reach?

Mint the two poles as parallel sentences that differ only in stance, take the balanced axis between them, and average every chunk’s projection quarter by quarter, joined to real post timestamps. The window function centers each quarter on the era mean, because the zero of a contrast axis only means equidistant from the two sentences. One query returns the trajectory of a community.

```
POST /v1/scry/embed  {"name": "achievable", "text": "Robust alignment seems achievable by defense in depth: iterative training, scalable supervision, interpretability, red-teaming, corrigible tool use, formal checks where possible, and institutions that prevent single-point failure. No one technique must be perfect if several imperfect safeguards compose well."}
POST /v1/scry/embed  {"name": "unreachable", "text": "Robust alignment seems unreachable by defense in depth: training optimizes proxies, supervision fails once systems surpass us, deception can hide until deployment, interpretability is incomplete, and institutions face racing pressure. Combining several imperfect safeguards still leaves correlated catastrophic failure modes."}

SELECT quarter, lean - avg(lean) OVER () AS drift, posts
FROM (
  SELECT toStartOfQuarter(p.original_timestamp) AS quarter,
         avg(scry_cosine_similarity(e.embedding,
             scry_contrast_axis_balanced(@achievable, @unreachable))) AS lean,
         uniq(e.target_key) AS posts
  FROM embeddings.chunks AS e
  JOIN forums.posts AS p ON p.post_key = e.target_key
  WHERE e.source = 'forum_posts' AND e.model_name = 'voyage-4-lite'
    AND p.source = 'lesswrong' AND p.original_timestamp >= '2009-01-01'
  GROUP BY quarter)
ORDER BY quarter
LIMIT 100;
```

### How fast did “vibe coding” catch on?

The search grammar rides inside the query as one predicate — here as an aggregate operand, with the month’s whole item count as its denominator. Hacker News: zero through January 2025, 34 mentions in February (the first item, 2025-02-03, links Karpathy’s tweet), 494 in March, 590 in April; 4 s, measured 2026-09-07.

```
SELECT toStartOfMonth(original_timestamp) AS month, count() AS items,
       countIf(scry_lex('"vibe coding"')) AS mentions,
       round(100000.0 * mentions / items, 1) AS per_100k
FROM hackernews.items
WHERE original_timestamp >= '2024-12-01'
GROUP BY month
ORDER BY month
LIMIT 36;

→ 2025-01      0     0.0 per 100k
  2025-02     34    11.9
  2025-03    494   169.4
  2025-04    590   212.6
```

### What does a community actually call the thing?

The token index prunes three months of Reddit comments to the ones carrying `gpt`; the regex then extracts every model name they mention and groups the occurrences — a vocabulary census over every matching comment, not a sample. Measured 2026-09-07: 378 million rows read, 17 s.

```
SELECT arrayJoin(extractAll(lower(body), 'gpt-[0-9]{1,2}(?:\.[0-9])?[a-z]*')) AS model,
       count() AS hits
FROM reddit.comments
WHERE scry_lex('gpt')
  AND created_utc >= now() - INTERVAL 90 DAY
GROUP BY model
ORDER BY hits DESC
LIMIT 10;
```

### Which papers cite both Scaling Laws and Chinchilla?

Citation edges are native keys, so “related work” becomes a set intersection: every OpenAlex work that cites both Scaling Laws for Neural Language Models and Training Compute-Optimal Large Language Models, ranked by its own citation count. 195 shared citers, 0.1 s, measured 2026-09-07 against the 2026-06-26 OpenAlex snapshot.

```
SELECT id, title, publication_year, cited_by_count
FROM openalex.works
WHERE id IN (
  SELECT citing_work_id FROM openalex.cited_by
  WHERE cited_work_id IN ('https://openalex.org/W3001279689',   -- Scaling Laws, 2020
                        'https://openalex.org/W4225591000')   -- Chinchilla, 2022
  GROUP BY citing_work_id HAVING uniqExact(cited_work_id) = 2)
ORDER BY cited_by_count DESC
LIMIT 10;

→ Large language models encode clinical knowledge   2023  3,194
  Can LLMs Transform Computational Social Science?   2023    429
  ProGen2: boundaries of protein language models      2023    426
```

### Which corners of the archive even talk about it?

One call compiles the same line against every relation with a text plane — 49 of them — and returns each relation's own index-native predicate in 0.2 s, before you spend a single scan. Add `counts: true` and the sweep also counts every relation that answers inside its budget; the largest archives report a `count_error` instead of a number.

```
POST /v1/scry/compile
{"q": "\"scaling laws\" -crypto", "relation": "*", "counts": true}

→ 49 relations compiled, 0.2 s. Counted (2026-09-07, 62 s):
  openalex.works 6,522 · academic.catalog 3,394 · x_open.tweets 2,087
  · forums.posts 1,387 · hackernews.items 983 · github.documents 679 · …
```

### Which single bets moved the GPT-5 market most?

Every Manifold bet carries the market probability before and after it, so the biggest moves in a question’s life are one ORDER BY away. On 2024-07-20 one bet of 20,701 mana took “Will GPT-5 be released before 2025?” from 48.9% to 83.2%; 6,040 bets ranked in 0.4 s, measured 2026-09-07, new bets landing within minutes.

```
SELECT created_at_source, prob_before, prob_after,
       round(100 * (prob_after - prob_before), 1) AS move_pp, amount, outcome
FROM manifold.bets
WHERE contract_id = 'RxR5grRyVrDm0wtzhAuM'  -- Will GPT-5 be released before 2025?
  AND is_redemption = 0
ORDER BY abs(prob_after - prob_before) DESC
LIMIT 10;

→ 2024-07-20 10:46  0.489 → 0.832  +34.3 pp  20,701  YES
  2024-10-26 07:36  0.250 → 0.500  +25.0 pp   5,000  YES
  2024-09-12 18:46  0.253 → 0.048  −20.5 pp  −2,238  YES
```

### Text

`scry_lex('"exact phrase" -noise /regex/')` the whole search grammar as one predicate

`a NEAR/50 b · "phrase"~3 · w

## 评论（25/25）

> **MrDrMcCoy** · 2026-09-18T16:52:45.000Z　
> This is a very good thing, thanks! Have you talked with any of the smaller search engines like Kagi, Qwant, Brave, Mwmbl, DDG, etc to have this supplement the quality of their results? This seems like a big step towards breaking Google and Bing's dominance in search.

---

> **neilellis** · 2026-09-18T17:10:54.000Z　
> Please have a 'readable version' option so I don't have to exhaust myself parsing the sites layout. I get that it's unique but most of us just want to work out what you're offering in 5-10 seconds of our time.

---

> **DylanMerigaud** · 2026-09-18T18:18:37.000Z　
> Congestion pricing for queries sounds innovative.

---

> **vova_hn2** · 2026-09-18T18:36:25.000Z　
> Pricing model is hard to understand at a glance. It uses a term "second of query time" which is not a conventional term and not defined anywhere. Also, all pricing related pages seem to be LLM-generated and are hard to read for a human.Please, just explain in your own words, how the pricing works, without using made up terms invented by an LLM.

---

> **podgorniy** · 2026-09-18T18:58:24.000Z　
> It's beautiful <3

---

> **ashkankiani** · 2026-09-18T19:32:20.000Z　
> Cool idea. The pricing model reminds me of my time working in algorithmic trading, haha. I'll try this out for some queries I wanted to run.I suppose the scraping you're doing is a huge part of your value proposition, but I would like to gently nudge you in the direction of making the datasets available via p2p (e.g. a torrent) like how Wikipedia distributes its snapshots in the spirit of democratizing access to data that is becoming increasingly walled off. Also, I think another potential benefit that kind of bulk sharing would have is relieving the congestion from those doing the equivalent operation to extract data via the querying interface.

---

> **ares623** · 2026-09-18T19:41:29.000Z　
> > Furthermore, search companies aren't even pursuing text-to-SQL anymore (several have talked to me)... they made up their minds during the traumatic 2024 text-to-sql days. They were just too early.Can you expand on this? Is text-to-sql a deadend? (I personally think it is, having worked on a project at $work. But curious to hear about others experience.)

---

> **segatti** · 2026-09-18T19:56:10.000Z　
> this is cool

---

> **letmevoteplease** · 2026-09-18T20:34:45.000Z　
> Cool but please rewrite the text. Ctrl + F "land" gives 29 matches.

---

> **mrbluecoat** · 2026-09-18T20:35:43.000Z　
> Scry, keyword action that allows a player to look at a specific number of cards from the top of their library and then arrange those cards in any order, placing any number of them on the bottom of the library and the rest on top.

---

> **codexon** · 2026-09-18T20:44:17.000Z　
> How did you scrape reddit comments? Doesn't this require expensive licensing from reddit? How do you handle comments that were deleted by users?

---

> **arboles** · 2026-09-18T22:28:17.000Z　
> I'm out of my depth, search is just really cool. If Scry beats the current DeepSearchQA leaderboard why isn't it in the leaderboard?Will it be added? Are you forced to use a traditional search engine to make it in the leaderboard?https://scry.io/deepsearchqahttps://www.kaggle.com/benchmarks/google/dsqa

---

> **antoniojtorres** · 2026-09-19T02:20:03.000Z　
> Fascinating stuff. Curious how you handle the ingestion of data from so many sources cost effectively

---

> **Xyra** · 2026-09-18T18:44:34.000Z　
> that's a good idea. it's very doable

---

> **JLO64** · 2026-09-18T17:38:21.000Z　
> I strongly second this, although I must admit it loaded surprisingly fast for me as I'm on a mobile hotspot in the back of a car.

---

> **hmartin** · 2026-09-18T19:00:27.000Z　
> HN: This site looks like all the other slop, awful to read.Also HN: This site is doesn't look like other sites, awful to read.

---

> **Xyra** · 2026-09-18T22:35:54.000Z　
> Hi, yes. New users right now get free credit. When the server isn't burdened, queries are currently ~free (under $.01 per second, when most are well under a second). We're just trying to learn here how to use this thing productively together.As load increases, the price goes up. There's also exponential egress pricing because Scry is a place where computation happens, not a metaphorical torrent. I'm still tweaking things, balancing between multi-user server load, giving normal active human users lots of priority and no fear in using it hard and deliberately, and fair pricing for agents and automated heavy workflows people set up in the background.

---

> **Xyra** · 2026-09-19T07:08:49.000Z　
> thank you!

---

> **Xyra** · 2026-09-19T00:50:19.000Z　
> let me know if it was faster and more compositionally expressive than you expected

---

> **Xyra** · 2026-09-19T00:01:31.000Z　
> thanks, I try

---

> **Xyra** · 2026-09-19T00:00:51.000Z　
> Good point, fixed

---

> **saturatedfat** · 2026-09-18T21:02:05.000Z　
> pushshift baby

---

> **Xyra** · 2026-09-19T20:45:24.000Z　
> good idea, I emailed them. And no search engine, only Scry or direct web fetch of an URL in a Scry result or from the agent's memory.

---

> **ai-inquisitor** · 2026-09-18T19:40:50.000Z　
> I'd bet that no one, not even the site's [human] creators, has ever read that homepage end to end. At best, it might have been handed over to a swarm of reviewer agents.

---

> **codexon** · 2026-09-19T19:44:25.000Z　
> How hasn't reddit sued them offline yet?

## 关联链接

- https://api.scry.io/v1/feedback`
- https://api.scry.io/v1/scry/query
- https://api.scry.io;
- https://mcp.scry.io
- https://mcp.scry.io.
- https://mcp.scry.io`,
- https://mcp.scry.io`.
- https://openalex.org/W3001279689
- https://openalex.org/W4225591000
- https://scry.io/dashboard.
- https://scry.io/docs/calculus-of-search.
- https://scry.io/docs/turing-complete-search;
- https://scry.io/legal/terms:

## 导航

- 项目页：[[10-项目/scry.io_8fe8acea]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
