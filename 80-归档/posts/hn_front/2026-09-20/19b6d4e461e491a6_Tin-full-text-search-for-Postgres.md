---
type: "corpus"
item_id: "19b6d4e461e491a6"
title: "Tin: full-text search for Postgres"
source: "hn_front"
source_name: "HN 首页（非 Show HN）"
url: "https://news.ycombinator.com/item?id=49766611"
project_url: "https://planetscale.com/blog/introducing-tin"
author: "ksec"
published_at: "2026-09-19T13:52:06Z"
captured_at: "2026-09-20T03:41:55+08:00"
lang: "en"
kind: "post"
tags:
  - 语料
  - hn_front
  - author_ksec
  - story_49766611
  - front_page
metrics: {"points": 134, "comments": 59, "engagement_velocity": 134}
comments_count: 59
comments_total: 59
discovered_via: "hn:front_page:2d"
archived: true
archived_at: "2026-09-20T09:16:59+08:00"
archive_reason: "排除:无主题词"
---

# Tin: full-text search for Postgres

- **来源**：HN 首页（非 Show HN）　|　**kind**：post
- **原帖**：https://news.ycombinator.com/item?id=49766611
- **指标**：点赞=134 · 评论=59 · engagement_velocity=134
- **作者**：ksec　|　**发布**：2026-09-19T13:52:06Z
- **项目链接**：https://planetscale.com/blog/introducing-tin
- **采集**：2026-09-20T03:41:55+08:00　|　**id**：`19b6d4e461e491a6`

## 正文

Neki, sharded Postgres, is now available. Get started

Blog| Engineering| PostgreSQL

Table of contents «Close »

#### Table of contents

- What TIN is for
- TIN performance and benchmarking Workloads and corpus Test environment Index build time and size Mixed queries, top-10 ranked Conjunction and phrase queries, top-10 ranked Disjunction queries with concurrent writes When the index fits in memory Full results
- Why TIN is fast Document identification 48-bit identifiers are crazy Work elision and vectorization Solving MVCC Segments and merging
- Summary

PlanetScale, the fastest cloud Postgres, from $5/month.

Start now

Get the RSS feed

# Introducing TIN: full-text search for Postgres

Eric Ridge, Patrick Reynolds | September 16, 2026

One of the Postgres features our customers ask us for the most is full-text search. Today, we are excited to announce TIN: a fast, full-featured, reliable full-text search extension for Postgres. TIN stands for "Text INdex," and that is what it does.

TIN is available immediately as a GA release for all Postgres and Neki databases. Check it out:

```
CREATE EXTENSION tin;
CREATE INDEX an_index_name ON table_name USING tin(text_column_name);
SELECT * FROM table_name
  WHERE text_column_name ==> 'some words';

```

We built TIN because we believe a good text index should support:

- Boolean expressions, phrase queries, and span queries
- Fuzzy, wildcard, and regular-expression matching for terms
- Case and accent folding
- `COUNT(*)` queries and BM25-scored top-k queries

A good text index in Postgres must support all of those things while also handling joins, complicated `WHERE` clauses across full-text and other column types, continuous updates, replication, backups, and correct transaction visibility.

Although there are at least three existing text-search indexes for Postgres already, none of them met all of those requirements. TIN does. TIN is also really, mind-blowingly fast.

## What TIN is for

Application developers use text indexes to build a variety of search features. An e-commerce platform might need to search for the top ten products containing all keywords in the search:

```
SELECT * FROM products
  WHERE description ==> 'stretch denim jeans'
  ORDER BY tin.score(ctid) DESC
  LIMIT 10

```

A legal discovery platform might be required to return every document containing one or more of a set of keywords, but not care at all about ranking:

```
SELECT * FROM emails
  WHERE body ==> '[insider trading conspiracy]'

```

A photo tagging platform might show an exact count of photographs with a particular tag:

```
SELECT COUNT(*) FROM photos
  WHERE tags ==> '"san francisco"';

```

Most applications also need to insert, update, and delete documents, even while continuing to query the index. Search queries must return matches based on new or changed rows as soon as they've been committed.

## TIN performance and benchmarking

We ran benchmarks to assess performance for all the above use cases and more. We tried workloads:

- With conjunction (must contain all words), disjunction (must contain any word), and phrase (must contain all words in sequence) queries and a mix of all three.
- That count documents or that ask for the top k by BM25 score.
- With and without clients writing new data to the index concurrently with the benchmark query workload.

### Workloads and corpus

We have measured TIN against a variety of text corpora: all of Wikipedia, a collection of Reddit comments totaling 2.3 TB, and a mixed workload we call simply "pile" with 797 GB of open-access research papers, legal documents, public domain books, and Enron emails. The benchmark results we share in this article are from an export of questions and answers from Stack Exchange: an 85 GB corpus with 150 million documents. Because the corpus has no standard query trace, we generated a synthetic one by sampling substrings ranging from 2 to 15 terms. We interpreted each substring three ways: as a conjunction, as a disjunction, and as a phrase query, for a total of 1,719 queries.

### Test environment

We ran our benchmarks on an AWS i7i.8xlarge EC2 instance with local NVMe storage and a modern, AVX-512-capable CPU. For each text-search extension, we set up Postgres 18.6 in an isolated container limited to 8 vCPUs and 32 GB of RAM. That's small enough to show how each index system performs when the index doesn't just fit in Postgres buffers. The benchmark phases ran sequentially, so the engines did not compete for resources. We chose a standalone EC2 instance to minimize the impact of operational overhead and replication and to ensure that anyone who wants to reproduce our benchmarks of competing text-search indexes can do so using the same instance type and container limits.

To drive the search traffic against the Postgres containers, we used the ParadeDB Benchmarker. We have a forked version that pre-warms before beginning measurement and adds metrics for bytes read and WAL bytes written. We left all Postgres parameters at the defaults that the Benchmarker supplies, except for three: we set `max_parallel_workers` to 8 (from 40), `shared_buffers` to 24 GB (from 128 MB), and `maintenance_work_mem` to 24 GB (from 64 MB), to best match the resources of the container. We ran the Benchmarker on the same EC2 instance as the target Postgres server, to ensure that network latency did not impact the measurements.

For each scenario, we measured the performance of TIN v1.0.2 against all the other Postgres text-search indexes that were capable of running the workload at all: ParadeDB v0.25.2, pg_textsearch v1.4.0, and the GIN index built into Postgres v18.6. Aside from TIN, only ParadeDB was able to complete all of the benchmarks.

### Index build time and size

Indexes range from 33% to 61% of the size of the corpus, and they took from 8 to 129 minutes to prepare, build, and finalize. The three engines other than TIN failed with the container's configured 32 GB limit, so for index builds only, we increased the available RAM as shown in the table. Before running queries, we set the container back to 32 GB of RAM for everyone.

| | Total time | Index size | Required RAM |
| --- | --- | --- | --- |
| TIN | 8m10s | 50.7 GB | 32 GB |
| ParadeDB | 19m20s | 52.1 GB | 64 GB |
| pg_textsearch | 26m49s | 41.5 GB | 128 GB |
| Postgres GIN | 2h09m04s | 28.0 GB | 64 GB |

### Mixed queries, top-10 ranked

Our first benchmark compares TIN against ParadeDB, for a workload with mixed (conjunction, disjunction, and phrase) queries, top-10 results by BM25 score, with no concurrent writes to the index. TIN handles 25× as many queries per second as ParadeDB does, with p99 latencies 26× lower. GIN can't complete this benchmark, because it runs out of memory performing the disjunction searches. pg_textsearch can't complete the benchmark because it handles only disjunction searches.

### Conjunction and phrase queries, top-10 ranked

Our next benchmark compares TIN against ParadeDB and Postgres GIN, for top-10 conjunction and phrase queries, with no concurrent writes. TIN and ParadeDB rank using BM25, while GIN ranks using `ts_rank_cd`. TIN handles 10× as many queries as ParadeDB and 541× as many as GIN, with p99 latencies 6× and 1,356× lower, respectively. pg_textsearch is again absent because it handles only disjunction queries.

### Disjunction queries with concurrent writes

Our third result compares TIN against both ParadeDB and pg_textsearch, for a workload with disjunction queries, top-10 results by BM25 score, and a concurrent client targeting 1,000 `UPDATE` queries per second. TIN handles 36× as many queries as pg_textsearch and 57× as many queries as ParadeDB, with p99 latencies 24× and 36× lower, respectively. Over the course of a ten-minute run, TIN completes 270,279 updates, while ParadeDB completes 185,584, and pg_textsearch completes only 735.

ParadeDB's approach to accepting writes sacrifices read throughput and latency. pg_textsearch maintains the same 3.5

# Laya — 33ms Multilingual System 1 Decision Engine with Calibrated Probabilities

## 评论（59/59）

**Tiberium** · 2026-09-19T14:22:48.000Z：

If anyone's curious - https://planetscale.com/docs/postgres/search/get-started#loc...:They're not providing a local extension with the same performance at the time - it's only offered on their cloud services.The local version https://github.com/planetscale/lead is mainly just for testing the syntax, it doesn't have the same perf characteristics.

**bob1029** · 2026-09-19T14:32:04.000Z：

I struggle with FTS inside SQL (SQLite and MSSQL). There is often a fairly significant impedance mismatch between the relational concerns and how the documents need to be stored.I've always preferred to use SQL as the system of record and then build/maintain an external Lucene index. Do we think these integral FTS capabilities are at the point where a hybrid architecture doesn't make sense anymore? How much customization exists in this provider?

**andrenotgiant** · 2026-09-19T15:32:46.000Z：

I think what we're seeing with every database company providing new full-text search capabilities is an example of AI coding productivity showing up in the real world.It started with paradeDB and pg_search https://www.paradedb.com/blog/introducing-searchTimescale has pg_textsearch https://github.com/timescale/pg_textsearchNeon and Databricks have Lakebase Search https://docs.databricks.com/aws/en/oltp/projects/lakebase-se...Now PlanetScale.AFAIK all of these are implementations of the BM25 algorithm. You can just tell an agent to read about BM25 and implement it in your system of choice. Cool to see. Seems like there's still a lot of juice to be squeezed out of how it's architected and integrated into each system, but you can't help but wonder if this will lead to aggressive commodification

**alexnewman** · 2026-09-19T15:52:47.000Z：

What’s funny is I worked with a company with planet in the name
Who could really use a full text search that was great in the Postgres

**usernametaken29** · 2026-09-19T16:04:46.000Z：

Interestingly enough SQLites FTS supports Lucene queries out of the box with great performance characteristics. IIRC only writes become pretty slow after a while.
I’ve always wondered what exactly would prevent PostgreSQL from strapping that implementation into its own database. My experience with ts_query hasn’t been particularly rosy. It can be better than LIKE but only marginally so and at the cost of insane index sizes…
If this extension becomes open source and we can test it out in the real world I’m sure there’s a sweet spot

**sick_of_slop** · 2026-09-19T16:19:56.000Z：

What are the advantages of Tin over using ts_vector with gin and gist indexes?

**adityapatadia** · 2026-09-19T16:29:54.000Z：

It’s just me or there are others who keep seeing these updates and think mongodb had all of this years ago?Seriously so happy to be running our production stack on mongo.

**aroman** · 2026-09-19T16:35:10.000Z：

I want to try Planetscale... but we're addicted to (and totally dependent on) Neon's branching model. They really got us hooked on that!

**downsplat** · 2026-09-19T16:35:19.000Z：

I suppose it all depends on the scale of your project, but I've had pretty good luck using both MySQL's and SQLite's FTS capabilities. Surprised to hear that Open Source champion Postgres didn't have up-to-snuff FTS up to now...?

**groundzeros2015** · 2026-09-19T16:36:31.000Z：

Please read the Postgres manual. It has incredible built-in search capability.

**znpy** · 2026-09-19T16:58:15.000Z：

This was already posted and ignored at https://news.ycombinator.com/item?id=49751888 so i’ll ask the same question: again:I don’t see any github link, is this 21st century embrace, extend, extinguish ?

**tannhaeuser** · 2026-09-19T16:58:52.000Z：

Postgres does have pg_fts (tsvector/tsquery/tsrank) which is a quite sophisticated full text search package integrated with functional indexing and query optimization. Why would I use something vibecoded that isn't part of core Postgres instead?

**immmmmm** · 2026-09-19T17:35:41.000Z：

Please note possible name collision with PostGIS Triangulated Irregular Network (TIN) data type.

**dorianmariecom** · 2026-09-19T18:03:20.000Z：

it does what it says on the TIN

**noir_lord** · 2026-09-19T14:32:04.000Z：

Becoming more the norm for them, Neki is the same.Immediately rules out ever using them (though I don't currently have any problems that would benefit from that level of scale currently, have in the past though).Postgres's license allows this but for me (personally) it leaves a bad taste.Also it's not really "full-text search for Postgres" it's "full-text search for our hosted version of Postgres" so the title is a little misleading.

**pqdbr** · 2026-09-19T15:44:22.000Z：

The problem is that they don’t support bare metal. I’d love to use PlanetScale in our bare metal servers.

**zombodb** · 2026-09-19T15:32:40.000Z：

I’m one of TIN’s developers and if you google my username you’ll see I’ve been in this space for a long time.The answer to your first question is simply: yesAs far as your second question, what customization do you need that you believe TIN or PlanetScale doesn’t provide? These are things we can do, with alacrity.

**gfody** · 2026-09-19T15:35:34.000Z：

in my experience it’s pretty common to find big inverted indexes for text directly in the database - not necessarily large docs but certainly free text records in volume. using bm25 and unicode’s breakiterator is a very good way to build it. like putting lucene in the database basically - makes a lot of sense when the database is already large. places that bend over backwards to move search out of the db are usually trying to avoid having a very large db (and often end up with one anyway, getting the worst of both worlds)

**CodesInChaos** · 2026-09-19T15:42:04.000Z：

ParadeDB's implementation builds on the Tantivy crate, which predates AI coding.

**samwillis** · 2026-09-19T15:50:37.000Z：

There is a lot of truth to this, but it's also very much down to domain experts being able to do this to move faster.Planetscale (assuming they used a agentic development practice) will have pulled this off, to the level of performance that they have, because they have a team of very highly experienced Postgres developers. Their knowlage of Postgres internals will have given them the insights needed to steer the models to a plan that used the architecture as described in the post. That's not something a model can do on its own*World experts + LLMs = moving mountains.(* we're obviously seeing something a little different from inside the research teams in the labs. They are showing that the models, when you burn the level of tokens only they can, are able to do novel things from the models own insights.)

**ceuk** · 2026-09-19T18:23:26.000Z：

I don't completely disagree with your hypotheses but it feels like the hard part of his TIN stuff isn't BM25 (which has been around for donkeys years) it's all the hardcore storage engine work around it. And is an LLM particularly good at e.g. segment merging under a thousand updates a second? I've had a few situations where I've been told "we've hit the perf floor" by Claude only to have persisted myself and shaved substantial amounts off still.More damning for the theory might be that I think paradedb's pg_search predates the agentic coding by a few years?

**xcc3641** · 2026-09-19T16:22:35.000Z：

SQLite FTS relies on shadow B-trees under single-writer locks. Postgres index access methods must map postings directly to physical ctid tuples, surviving MVCC visibility checks and heap tuple churn.

**dragonwriter** · 2026-09-19T17:04:04.000Z：

From the benchmarks deep in the document, TIN is much faster than built in text search (tested against GIN, which is itself much faster than GiST for text search.)

**stickfigure** · 2026-09-19T16:32:34.000Z：

Poe's Law strikes again.

**groundzeros2015** · 2026-09-19T16:35:53.000Z：

Is this an ad? Postgres has had search for more than a decade.

**dragonwriter** · 2026-09-19T16:57:39.000Z：

It has FTS built in and has had it for a VERY long time.

**paulddraper** · 2026-09-19T16:49:28.000Z：

It has it.Incredible? No.

**dragonwriter** · 2026-09-19T16:56:50.000Z：

If you read deep into this, they claim much better performance than the built in search; they also imply that the built-in search is missing features they provide but don’t make clear which ones (I think it is just support in the same index for queries covering other conditions on other columns, because every other feature they claim seems to line up with the built in search features, which have been around for about 20 years.)

**Boxxed** · 2026-09-19T17:32:10.000Z：

The built in search can't do any scoring mechanism that involves corpus-wide stats, so things like tfidf and bm25 are right out. If you don't need that then great, but in my experience the results are much worse.

**rs_rs_rs_rs_rs** · 2026-09-19T17:20:24.000Z：

>is this 21st century embrace, extend, extinguishI assume here you're talking about Amazon's modus operandi?

**samlambert** · 2026-09-19T15:28:06.000Z：

why?

**dbbk** · 2026-09-19T15:31:38.000Z：

Why would you need super fast search for local testing?

**zombodb** · 2026-09-19T15:50:42.000Z：

Why don’t you like Postgres’ license? It’s as permissive as a license gets.

**Cyph0n** · 2026-09-19T18:29:20.000Z：

> Becoming more the norm for them, Neki is the same.Uh, isn’t this becoming the norm everywhere ever since LLMs have been trained on OSS without credit or attribution? Why wouldn’t you want to hide your stuff going forward?In my view, OSS is only going to move more and more towards one of two models: open core + proprietary functionality (e.g. MongoDB) OR open source + private tests (e.g. SQLite).

**samlambert** · 2026-09-19T16:17:25.000Z：

we support bare metal inside AWS, GCP, and very soon Azure

**zombodb** · 2026-09-19T15:44:15.000Z：

They also end up with all the infrastructure and processes necessary to keep the external search system in sync, resync/reindex, pkey shipping back to their source of truth in queries, application-side joins and enrichment between both sources. It’s brutal.Having everything in one place eliminates entire classes of development and especially operational problems.

**cjonas** · 2026-09-19T16:35:25.000Z：

Seems like a lot of this knowledge was encoded into the blog post. I wonder if given this post and access to a planet scale instance to compare with, how close an agentic agent could get.

**geraneum** · 2026-09-19T16:41:30.000Z：

I think we can frame it as LLMs materializing existing potential. It seems like there needs to be an underlying potential to tap into, without which, the results could be slop.

**nozzlegear** · 2026-09-19T18:06:54.000Z：

> There is a lot of truth to this, but it's also very much down to domain experts being able to do this to move faster.Yeah, I don't think I could tell Qwen3.8 (my LLM of choice) to study up on bm25 and then implement full text search in the couchdb instances I maintain without studying both bm25 and couchdb internals myself.

**bddicken** · 2026-09-19T18:45:03.000Z：

THIS++

**dragonwriter** · 2026-09-19T17:02:05.000Z：

> Postgres has had search for more than a decade.More than two decades (it moved to core from contrib in version 8.3 in 2008, but it was available in contrib since 7.4 in 2003.)

**groundzeros2015** · 2026-09-19T16:54:36.000Z：

I think it’s fantastic.You want to use this thing instead?

**zombodb** · 2026-09-19T17:49:01.000Z：

Over Postgres' FTS, TIN provides at least: - superior performance
 - superior operational overhead
 - no second copy of data in tsvector form
 - BM25 scoring support with optimized top-k output
 - runtime configurable scoring knobs
 - expression-attached score boosting
 - sophisticated span query support -- this is proximity search on steroids (https://github.com/planetscale/lead/tree/main/tinql/docs)
 - lossless term positions
 - index-answerable negative expressions (find all docs that don't contain a word)
 - full document hit highlighting
 - optimized exact `count(\*)`
 - term expansion via any of fuzzy matching, wildcards, regular expressions, and dictionary ranges
 - intentionally smaller user-facing SQL API surface

There's a lot we didn't cover in the announcement blog. I'm sure we'll do more as time goes on.As an aside, something I personally think is cool, and I suppose you can do this with Postgres' built-in `@@` too, is that you can use TIN's full query language (linked above) against any text datum. This is a valid query: SELECT pid, query 
 FROM pg_stat_activity 
 WHERE query ==> 'select OR copy'

in other words, you don't need an index at all to use TIN's full query language against any text field in any query.

**Onavo** · 2026-09-19T15:45:28.000Z：

To avoid vendor lock-in.

**noir_lord** · 2026-09-19T16:09:48.000Z：

Building non-open extensions on top of it, it's not the license I don't like, the bad taste is that they use something open extend it and keep part of it closed.The license allows it but on the flip side it's vendor lock-in predicated on using something open as the base.Fully proprietary no issue with that, full open, no issue with that, building proprietary on top of open is where the bad taste comes in.For completeness, it's not them specifically either, the other cloud companies do similar things and I suspect in part the reason they don't open these extensions up is because the others will but then they are doing the same thing themselves.

**sroussey** · 2026-09-19T17:53:19.000Z：

what do you call bare metal in my office?

**awesome_dude** · 2026-09-19T19:40:55.000Z：

The easiest way to find that out is to TIAS

**rs_rs_rs_rs_rs** · 2026-09-19T17:18:06.000Z：

...yes, obviously?

**dbbk** · 2026-09-19T15:57:14.000Z：

It's Postgres search any coding agent can switch you to something else in 5 minutes

**zombodb** · 2026-09-19T16:24:49.000Z：

When one develops using open-source software they have an obligation to follow the licenses. They also have a moral obligation to be respectful of the work upon which they’re building. And they have a social obligation to help improve that software where they can.Those that develop on top of open-source have no obligation to give you their work for free.You’d be surprised as to the amount of open-source contributions TIN drove towards Postgres, LLVM, and pgrx. And you’d be speechless at the amount of upstream work across all sorts of open-source PlanetScale does. Postgres 18.6, for example, is better for you today, in part, because of TIN. You’re welcome.

**collinmcnulty** · 2026-09-19T19:21:56.000Z：

I find this attitude self-defeating because the lure of being able to provide some amount of proprietary software on top of open is what draws in the corporate investment in open software. And in the system we live in, it’s hard to imagine there’d be nearly as much open software as there is without that corporate investment. As a big fan of open software, this seems like a great trade to me.(Disclosure: I work for a company with this business model, in part because I like working on open software)

**noir_lord** · 2026-09-19T16:32:22.000Z：

> You’re welcome.I didn't say thank you and don't presume I would, Planetscale acting in their own self interest by improving postgres upstream isn't deserving of thanks, any more than Intel upstreaming a bunch of Linux kernel work is or myriad other examples.Corporations acting in their self interest isn't worth giving thanks for, neither is the work of the people paid to do work on their behalf.I don't expect my employer to thank me, I expect them to pay me, I don't expect users of software I was paid to write to thank me because I did it for the money not out of altruism towards those users.

**xyzzy_plugh** · 2026-09-19T16:42:28.000Z：

Everything else aside> Those that develop on top of open-source have no obligation to give you their work for free.This is a pretty narrow view of open source.Just as a simple example, GPLv3 and AGPLv3 are both considered Open Source and, depending on how you hold them, may obligate releasing work to customers essentially for free.

**aarondf** · 2026-09-19T18:01:08.000Z：

> When one develops using open-source software they have an obligation to follow the licenses.Agreed!> They also have a moral obligation to be respectful of the work upon which they’re building.Respectfully, completely disagree!Open source is a license, not a moral framework. Your only duty is to abide by the license. If you want to enforce that everything built on top of a particular open source package also be open source, that belongs in the license.

**zombodb** · 2026-09-19T16:42:04.000Z：

It’s clear that we’re on opposite ends of open-source ideology.Good luck out there! 2026 is wild times!!

**zombodb** · 2026-09-19T16:54:23.000Z：

I thought I was clear:> When one develops using open-source software they have an obligation to follow the licenses.Obviously what follows from one of those licenses is what you say.I’m glad we agree!

**jamienk** · 2026-09-19T17:40:48.000Z：

"...are both considered Open Source" << Free Software (GPL) is the O.G. - it's like saying "George Washington is considered to be an American President" or "The Beatles are considered to be a pop/rock band" or "water is considered to be..."I remember so well when "Open Source" branding started with Bruce Perens - all the business arguments. When you need a database, someone ELSE'S business decisions (how THEY are going to make money) never end up helping YOU. If you use proprietary extensions and become dependent on them, you inevitably will get BURNED when their business needs diverge from your needs.
- They close shop
- They refuse to interop with something you need
- They demand that you obey their arcane rules
- They rug-pull
- They get hacked as only they can
- They lie to you
- They stab you in the back

**zombodb** · 2026-09-19T18:32:55.000Z：

> Your only duty is to abide by the license.We live in a society. I don’t see any harm in believing we ought to be respectful of the work. That’s all I’m saying. You don’t have to be, but it’s a better world if you are.> If you want to enforce that everything built on top of a particular open source package also be open source, that belongs in the license.Yes! I fully agree. The one that creates the thing is the one that gets to choose its license.Having opened-sourced some bit of work myself, that’s a very difficult decision.

**noir_lord** · 2026-09-19T16:46:37.000Z：

You as well, and yes it's very "may you live in interesting times" at the moment everywhere.
