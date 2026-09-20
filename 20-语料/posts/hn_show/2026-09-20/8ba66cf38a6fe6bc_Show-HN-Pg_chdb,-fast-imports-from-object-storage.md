---
type: "corpus"
item_id: "8ba66cf38a6fe6bc"
title: "Show HN: Pg_chdb, fast imports from object storage to Postgres using COPY"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49768601"
project_url: "https://clickhouse.com/blog/introducing-chdb-postgres"
author: "saisrirampur"
published_at: "2026-09-19T17:42:09Z"
captured_at: "2026-09-20T09:48:16+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-20"
pub_day: "2026-09-19"
tags:
  - 语料
  - hn_show
  - author_saisrirampur
  - story_49768601
  - show_hn
metrics: {"points": 3, "comments": 0, "engagement_velocity": 3}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:3d"
---

# Show HN: Pg_chdb, fast imports from object storage to Postgres using COPY

> [!info] 一句话导读
> Collapse the terminal

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49768601>
> 指标：点赞=3 · 评论=0 · engagement_velocity=3
> 作者：saisrirampur　|　发布：2026-09-19T17:42:09Z
> 项目链接：<https://clickhouse.com/blog/introducing-chdb-postgres>
> 采集：2026-09-20T09:48:16+08:00　|　id：`8ba66cf38a6fe6bc`

## 正文

Skip to content

Collapse the terminal

->Scroll to top

<-Back

- Blog
- /
- Product

Copy pageCopied!More actions

- View as Markdown Open this page in Markdown
- Open in ChatGPT Ask questions about this page
- Open in Claude Ask questions about this page
- Open in v0 Ask questions about this page

# Introducing chdb Postgres extension: High-performance imports from cloud storage

David Wheeler

Sep 8, 2026 · 11 minutes read

We're happy to announce a new Postgres extension: chdb. This extension expands Postgres import and export features via the chDB library, an in-process ClickHouse engine, providing efficient, flexible conversion to and from a wide array of data formats living on your favorite cloud storage systems.

## Benchmark

And boy howdy do we mean efficient! We compared chdb's performance importing the NYC Taxi dataset (1m rows, wide table) in a number of data formats to three other Postgres extensions, all reading from a regionally-colocated AWS S3 bucket. To the chart!

> In order to minimize differences and to optimize for measurement of extension performance rather than infrastructure, the chdb, pg_lake, and pg_duckdb benchmarks ran on `r8id.xlarge` ClickHouse Managed Postgres services with 4 vCPUs and 32 GB RAM; the aws_s3 benchmark ran on a `db.r8g.xlarge` AWS RDS host, also with 4 vCPUs and 32 GB RAM. Results average three runs for each import. See the benchmark source code for details.

Of the four extensions, chdb exhibits the most consistent performance. pg_duckdb and pg_lake, both backed by DuckDB, take around 2-3x as long to import data from CSV, JSON, and Parquet. Only aws_s3 approaches chdb's performance, but it supports a much more limited array of data formats.

## Data formats

Did we mention data formats? The chdb extension can read and write a slew of data formats --- all those that ClickHouse itself supports. This table summarizes the supported data formats and compression algorithms of the extensions we compared; note that this chdb list of formats is but a subset of the formats it supports:

| Extension | Compression | Data Formats |
| --- | --- | --- |
| aws_s3 | none | Text (TSV), CSV, Postgres Binary |
| pg_lake | gzip, zstd, snappy (Parquet only) | CSV, JSON, Parquet |
| pg_duckdb | gzip, zstd, snappy (Parquet only) | CSV, JSON, Parquet |
| chdb | gzip, zstd, lz4, bz2, snappy, brotli | TSV, CSV, JSON, BSON, Prometheus, Protobuf, Avro, Parquet, Arrow, XML, CapnProto, Markdown, MsgPack, ORC, and more! |

As ClickHouse and the chDB library add more, the chdb extension will get them for free!

We benchmarked chdb performance loading the NYC Taxi dataset for a number of these formats, where it demonstrated quite consistent performance:

We used the JSONCompact format for compatibility with the other extensions. Other JSON formats, such as JSONCompactEachRow, will more closely approximate the performance of the other formats.

## Usage

The chdb package ships with two extensions: a CREATE EXTENSION extension named chdb and a hook module named chdb_hook.

### chdb extension

The chdb extension (docs) provides the `chdb_query()` function, which executes a single chDB query. For example, this query:

```sql
1SELECT * FROM chdb_query($$
2  SELECT * FROM s3('s3://datasets-documentation/my-test-bucket-768/some_prefix/some_file_1.csv');
3$$) AS (id int, months int, days int);

```

Copy command

Outputs:

```bash
1id | months | days
2----+--------+------
3  1 |      2 |    3
4  3 |      2 |    1
5  4 |      5 |    6
6(3 rows)

```

Copy command

### chdb_hook module

The `chdb_hook` module (docs) hooks into the COPY command to copy data to or from an AWS S3, Google Cloud Storage, Azure Blob Storage, file, or http URL. This example loads records from a CSV file on S3:

```sql
1CREATE TABLE times (
2    id     INT NOT NULL,
3    months INT NOT NULL,
4    days   INT NOT NULL
5);
6
7LOAD 'chdb_hook';
8COPY times FROM 's3://datasets-documentation/my-test-bucket-768/some_prefix/some_file_1.csv';

```

Copy command

After which the `times` table contains the records from the file:

```bash
1# SELECT * FROM times;
2 id | months | days
3----+--------+------
4  1 |      2 |    3
5  3 |      2 |    1
6  4 |      5 |    6
7(3 rows)

```

Copy command

A CREATE TABLE command may also derive its columns, and load its rows, from such a URL. Try this one (all the URLs in this piece point to legit data files):

```sql
1CREATE TABLE reviews () WITH (
2    copy_from = 's3://datasets-documentation/amazon_reviews/amazon_reviews_2015.snappy.parquet'
3);

```

Copy command

The resulting, fully-loaded table has this structure:

| Column | Type |
| --- | --- |
| review_date | integer |
| marketplace | text |
| customer_id | numeric(20,0) |
| review_id | text |
| product_id | text |
| product_parent | numeric(20,0) |
| product_title | text |
| product_category | text |
| star_rating | smallint |
| helpful_votes | bigint |
| total_votes | bigint |
| vine | boolean |
| verified_purchase | boolean |
| review_headline | text |
| review_body | text |

## Data types

Like pg_clickhouse, chdb relies on the pg-clickhouse-c headers-only library to convert values from ClickHouse to Postgres, including its type mapping, as in the `CREATE TABLE` example above. The current release maps nearly all of the ClickHouse types to Postgres types and vice versa. These mappings work most of the time; when they don't, use the `structure` option to tell chdb what type to use.

For example, pg-clickhouse-c maps a Postgres JSON value to ClickHouse String, because ClickHouse JSON currently recognizes only JSON objects, while Postgres JSON supports objects, arrays, and JSON scalar values. But perhaps you're confident your JSON columns contain only objects, thanks to a check constraint:

```sql
1CREATE TABLE projects (
2    name   TEXT PRIMARY KEY,
3    meta   JSON NOT NULL CHECK (json_typeof(meta) = 'object')
4);
5
6INSERT INTO projects
7VALUES ( 'chdb',   '{"status": "release"}' ),
8       ( 'walrus', '{"status": "revise"}'  );

```

Copy command

To benefit from the increased flexibility and storage for object-aware storage formats such as Parquet JSON, use the `structure` option to map it to ClickHouse JSON:

```sql
1COPY projects to 'file:///tmp/projects.parquet' (
2    structure 'name String, meta JSON'
3);

```

Copy command

## Cloud storage URLs

The chdb_hook extension reads and writes to all your favorite storage platforms. It determines the appropriate protocol from the URL scheme.

| Schemes | Target |
| --- | --- |
| file | Absolute path on the Postgres server |
| http, https | HTTP URL |
| s3 | AWS S3 |
| gs, gcs, oss | Google Cloud Storage |
| az, azure, abfss, abfs | Azure Blob Storage or Azure ABFS |
| hdfs | Hadoop Distributed File System |

URLs may also use a number of wildcards to concurrently fetch multiple files. Revisiting the `CREATE TABLE` example above, this command finds and imports six files from S3:

```sql
1CREATE TABLE times () WITH (
2    copy_from = 's3://datasets-documentation/my-test-bucket-768/{some,another}_prefix/some_file_{1..3}.csv'
3);

```

Copy command

After which the `times` table contains the records from each file it loaded:

```bash
1SELECT * FROM times;
2 c1 | c2 | c3 
3----+----+----
4  1 |  2 |  3
5  3 |  2 |  1
6  4 |  5 |  6
7  1 |  2 |  3
8  3 |  2 |  1
9  4 |  5 |  6
10  1 |  2 |  3
11  3 |  2 |  1
12  4 |  5 |  6
13  1 |  2 |  3
14  3 |  2 |  1
15  4 |  5 |  6
16  1 |  2 |  3
17  3 |  2 |  1
18  4 |  5 |  6
19  1 |  2 |  3
20  3 |  2 |  1
21  4 |  5 |  6
22 (18 rows)

```

Copy command

## Architecture

Support for such a vast array of data formats and cloud platforms demands a panoply of dependencies. We avoid managing those dependencies by delegating the problem to the chDB library. But loading that library into a Postgres backend would be excessive, especially for typically occasional or periodic tasks such as loading from a data source once a day.

Data loading extensions thus take a variety of approaches to managing the size and complexity of such a library by a variety of means:

- aws_s3 simply downloads files to the local file system and passes control to COPY; hence its limitation to AWS S3 sources and the formats that Postgres COPY supports
- pg_duckdb embeds the DuckDB engine in the Postgres backend, overkill for occasional COPY needs
- pg_lake runs a separate DuckDB-powered service and communicates with it via the libpq protocol, which permanently consumes resources on the Postgres host

The chdb extension adopts its own distinctive architecture: It embeds the chDB library into a separate helper application. Neither the extension nor chdb_hook link chDB. Instead, they start the helper app on demand and communicate with it via an efficient, in-memory channel: file descriptors (`STDIN`, `STDOUT`, and `STDERR`, plus another for configuration information).

This design prevents the chDB library from consuming any more resources than necessary to carry out a single command. It also isolates the PostgreSQL cluster itself from out of memory issues that using shared memory with a background worker would suffer.

When the helper app finishes executing a command and has passed all its results to the backend (in ClickHouse Native format, straight from the source), it simply cleans up and exits, leaving the server resources to the service that most matters: PostgreSQL.

```bash
1+-------------+
2                  |   helper    |
3+----------+      |    app      |      +------+
4| Postgres |      | +---------+ |      | chDB |
5| Backend  |<---->| |  chDB   | |<---->| Data |
6+----------+      | | Library | |      +------+
7                  | +---------+ |
8                  +-------------+

```

Copy command

## What's next?

We plan to continue making chdb better. Potential roadmap items include:

- Complete type mapping. We're gradually filling in the gap between Postgres and ClickHouse data types, to the benefit of both chdb and pg_clickhouse.
- Access control to object storage via credential chain. Currently credentials required to read and write object stores must be passed explicitly in each chdb call. We'd like to allow transparent, server-configured credentialing to work as well.
- Support for `COPY (query) TO`
- Support for a `WHERE` condition on COPY
- Support for all of the existing COPY options
- Support for the Iceberg format
- Query files directly from storage

## Give it a try

Find the chdb extension in all the usual places, including GitHub and PGXN. We also provide it as part of the broader pg_clickhouse package on ClickHouse Managed Postgres; ask your support contact to add `chdb_hook` to your default configuration, or just connect to a superuser account via `psql` or your favorite client, run `CREATE EXTENSION chdb;` or `LOAD 'chdb_hook';` and get started!

### Get started with ClickHouse Managed Postgres today

Interested in seeing how ClickHouse Managed Postgres works on your data? Get started with ClickHouse Cloud in minutes and receive $300 in free credits.

Sign up

### Get started today

Interested in seeing how ClickHouse works on your data? Get started with ClickHouse Cloud in minutes and receive $300 in free credits.

Sign up

---

Share this post

- Copy URL

### Subscribe to our newsletter

Stay informed on feature releases, product roadmap, support, and cloud offerings!

## Recent posts

View all Blogs

Engineering

### Measuring real-time performance per dollar under continuous load: CostBench’s first end-to-end results

Tom Schreiber and Lionel Palacin · Sep 8, 2026

Product

### How MCP Toolbox turns agent text into ClickHouse vectors

Pete Hampton · Sep 7, 2026

Product

### ClickHouse as a streaming HTTP API

Mark Needham · Sep 5, 2026

Engineering

### Build a real-time market data app with ClickHouse and Massive

Lionel Palacin · Sep 4, 2026

View all Blogs

```json
[{"@context":"https://schema.org","@type":"BlogPosting","headline":"Introducing chdb Postgres extension: High-performance imports from cloud storage","description":"The chdb Postgres extension brings fast imports and exports across cloud storage platforms and data formats, powered by the embedded ClickHouse engine.","image":"/uploads/Blog_Banner_CHDB_Extension_1_ebdf65f0e4.png","publisher":{"@type":"Organization","name":"ClickHouse","url":"https://clickhouse.com/","logo":{"@type":"ImageObject","url":"https://clickhouse.com/_next/static/immutable/media/icon1.3b4swr1c2xvk2.png"}},"datePublished":"2026-09-08T15:42:52.505Z","dateModified":"2026-09-08T15:42:52.403Z","author":{"@context":"https://schema.org","@type":"Person","name":"David Wheeler","url":"https://clickhouse.com/authors/david-wheeler","@id":"https://clickhouse.com/authors/david-wheeler#person","image":"/uploads/Image_512x512_1_8bc569c360.png"}}]

```

# Aaronmike481/BreachScanner

## 关联链接

- https://clickhouse.com/
- https://clickhouse.com/_next/static/immutable/media/icon1.3b4swr1c2xvk2.png
- https://clickhouse.com/authors/david-wheeler
- https://clickhouse.com/authors/david-wheeler#person
- https://schema.org

## 导航

- 项目页：[[10-项目/clickhouse.com_e3771084]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
