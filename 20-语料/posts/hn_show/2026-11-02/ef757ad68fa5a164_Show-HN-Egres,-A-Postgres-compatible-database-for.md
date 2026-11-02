---
type: "corpus"
item_id: "ef757ad68fa5a164"
title: "Show HN: Egres, A Postgres-compatible database for heavy, multi-tenant workloads"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50325296"
project_url: "https://manishrjain.com/egres"
author: "mrjn"
published_at: "2026-11-01T13:07:16Z"
captured_at: "2026-11-02T09:37:22+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-11-02"
pub_day: "2026-11-01"
tags:
  - 语料
  - hn_show
  - author_mrjn
  - story_50325296
  - show_hn
metrics: {"points": 5, "comments": 1, "engagement_velocity": 5}
comments_count: 1
comments_total: 1
discovered_via: "hn:show_hn:3d"
---

# Show HN: Egres, A Postgres-compatible database for heavy, multi-tenant workloads

> [!info] 一句话导读
> Manish R Jain About Brisk Calculator Docovia Feed

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50325296>
> 指标：点赞=5 · 评论=1 · engagement_velocity=5
> 作者：mrjn　|　发布：2026-11-01T13:07:16Z
> 项目链接：<https://manishrjain.com/egres>
> 采集：2026-11-02T09:37:22+08:00　|　id：`ef757ad68fa5a164`

## 正文

Manish R Jain About Brisk Calculator Docovia Feed
October 27, 2026 egres postgres zig 30 min read
 Egres: A Postgres-compatible database for heavy, multi-tenant workloads
 manishrjain.com/egres
 On this page ▾ Egres
 Benchmarks
 Who am I
 Why Egres
 Postgres Issues
 Why not a fork, extension or storage engine underneath
 The Design
 Thousands of Tenants in one Process
 Half the Disk, local or remote
 Read your Writes from any replica
 No VACUUM. No Repack.
 100x Faster Multi-Index Lookups
 Instant Branching of a database or a table
 Transactions: Repeatable Read, Pessimistic Locking
 Try it out
 More posts ↓ Docovia: The Land for Your Docs
 Theme Light Dark
 I love Postgres. It is an incredible database. But, its design is also 30 years
old and most of what people fight in production comes from decisions made long
time ago: VACUUM, transaction id wraparound, bloat, a process per connection,
MVCC. So, I’ve been wondering about this question for a while,
“What would Postgres look like if it were to be designed today?”
For the past year, I’ve been quietly working on answering that question. Today,
I’m excited to announce Egres to the world.
Egres is not a fork or a port of Postgres. It is a new database, designed from
first principles, that speaks Postgres. Apart from libpg_query , it uses no
Postgres code. This post walks through what Egres can do, the benchmark numbers,
why I built it, and then the design that makes those features and numbers
possible.
Egres is open source under Apache 2.0, and the code is on GitHub .
Egres
Speaks the Postgres protocol. psql, drivers and ORM connect unchanged.
Can run thousands of tenants on one process. Queries run on a custom coroutine
(fiber) system, with CPU ticks, memory and disk IOPS metered per
query and per tenant.
Uses a new storage engine, called zdb, which is an LSM forest (tree of LSM
trees) for storage, with block compression, checksums,
multi-version concurrency control and garbage collection.
Runs on local disk or object storage. With S3, Egres servers are stateless,
with an optional local NVMe disk cache.
Provides Raft based replication, with read-your-write guarantees across any
replica.
Provides instant database and table branching with zero copy and without doing
copy-on-write.
This release runs as a single node. The multi-node code is in but not enabled
yet; that’d land in the next release. Most of the work in this version went into
storage, replication, resource metering and fiber based query execution. The
 query features are basic for now, equality-only and no joins, and
will grow with each release.
You can install and get started with Egres by following this quickstart
guide .
Benchmarks
On 600M row (580 GiB data) benchmarks against Postgres v18, on a 16-core Ryzen 5950X
with each server capped at 64 GiB of memory ( link ):
Postgres 18
 Egres
 Why
Disk at the end of the load
 693 GiB
 376 GiB , 46% less
 SSTable block compression
Bytes written over the run
(write amplification)
 3.0 TiB (5.2×)
 2.3 TiB (4.0×) , 23% less
 No full-page writes to the WAL
Mean latency, three queries (geomean)
 3.5 ms
 1.3 ms , 2.8× faster
The fourth query, two indexes, p95
 490 ms
 3.9 ms , 126× faster
 Bitmap intersection, no composite indexes
Reader txns/s at the end of the settle
 99
 3,739
 Better latency under a closed loop
Load rate
 101,654 rows/s
 88,259 rows/s, 13% slower
 Compaction pushback
In general, Postgres does better when data fits comfortably in RAM; it achieves
higher txn/s in the first 15 mins of the benchmark. As data starts growing,
Egres does much better.
After the load (settle phase), Egres has lower p50 latency across all four
queries, by a factor (2.9x - 226x). The tails are more mixed for select and
 customer queries. When the blocks are in RAM, Egres wins (p50). When they have
to be fetched from disk, Egres pays the extra cost of decompressing bigger
blocks, 16 KiB for Egres in this run, vs 8 KiB for Postgres. On select , it’s
practically a tie. On customer , which has 75 rows scattered across the table,
it costs Egres 6 to 8ms at p95 and p99 extra, making Postgres 33% faster
(something for Egres to improve in future versions).
On the other two queries, sku_day and customer_day_count , Egres wins by a
factor, ranging from 4.6x to 226x. Postgres was given the same four
single-column indexes as Egres, without any composite index on (sku, day) or
 (customer_id, day) . With those, Postgres would surely do better than the
~500ms p95 it reached for sku_day .
But the point is, native bitmap indexes in Egres avoid the need to
predict which columns will be queried together, and perform really well even
without composite indexes. The same query runs in <4ms p95 in Egres.
Benchmarks are easy to get wrong, so I’ve put together this benchmarks
page which explains the methodology, the schema, the Postgres
configuration, the queries, and how to reproduce the numbers.
Who am I
If you don’t know me and are wondering why should you trust me with databases, a
bit of my background would help. I was the founder of Dgraph Labs, author of
 Dgraph - a distributed transactional graph database, and author of
 Badger - an embeddable key-value database written in Go. I
also worked in Google’s web search and Uber’s database groups. You can read more
 about me here.
Why Egres
While at Uber, I ran up against one of the largest MySQL fleets anywhere. What
had to be built around the database made the shortcomings of the database clear.
Raft based consensus on top of it, because it had none.
Reading your writes meant sending traffic to the leader always.
Losing a node was painful because of stateful nature of the deployments,
causing terabytes of data transfer to setup a new replacement node.
Elaborate systems built and rebuilt to throttle or drop
lower-priority queries when the database slowed down. Every version had to
guess what a query cost, because the database doesn’t say. One version used
rows returned as proxy for CPU usage, which put a full table scan returning
one row at the same cost as point lookup.
Postgres Issues
And that was MySQL, very heavily productionized database across the industry.
Postgres adds its own issues on top. In fact, Uber famously moved
off Postgres due to these limitations.
Engine
Every connection is a process. Trouble starts as you hit hundreds of active
connections and the standard answer is it put PgBouncer , which you then have
to tune.
No per-query accounting of CPU, memory or I/O, and no way to cap a tenant, so
one bad query can get OOM-killed and take the entire instance down with it.
Because transaction ids are 32 bits, falling far enough behind ends with the
database refusing writes, which is how Sentry lost most of a day
in 2015 and Mandrill lost a weekend in 2019.
Storage
Every row update writes a new tuple at a new
physical location, changing its ID. So, every index on the table has to point at this new ID to stay relevant.
Changing one, even unindexed column on a table with a dozen indexes updates all twelve
(unless the update qualifies as HOT). On a table with
twenty indexes, one regular update is twenty-one block changes .
Dead tuples stay in the heap until VACUUM removes them. A vacuum skips
heap pages it knows are clean, but it walks every index on the table in
full, and when it falls behind, the table bloats until you schedule
pg_repack. Andy Pavlo’s group called this MVCC design the part of PostgreSQL
they hate the most .
Tables and indexes are stored uncompressed, which as the benchmarks show
result in twice the disk used. TOAST compresses one value at a time and only
when the value is over about 2 KB, so a table of ordinary rows never
compresses at all . The answers are a compressing
filesystem underneath, or a columnar extension on top.
Write Ahead Log
The WAL carries a full copy of every page the first time it is touched
after a checkpoint, and checkpoints write the dirty pages again. One 1 KB
insert into a table with five indexes can produce
 around 48 KB of WAL .
A replica applies the physical WAL byte for byte, and a replica query that
holds an old snapshot blocks replay, so after a timeout Postgres kills the
query, as Uber found . The alternative is to let the primary
bloat.
Lots of companies and developers are pouring resources into fixing what can be
fixed in Postgres. But these issues are not bugs that can be fixed. They follow
from decisions made decades ago, and changing them now would require a major
rewrite or a new on-disk format, a cost very few teams running Postgres in
production can reasonably absorb.
Why not a fork, extension or storage engine underneath
My first iteration of Egres swapped out the storage engine of Postgres with an
 LSM tree . The way MyRocks did with MySQL. Facebook cut its
instance size by 62% moving its user database to MyRocks, and
 Uber saved more than 30% moving Docstore and Schemaless to it.
Compute Storage Separation
Neon, AlloyDB and Aurora also swap out the storage engine, but for a different
goal. Their approach has been to serve Postgres pages via remote storage, so the
compute is stateless and can be started and stopped at will.
But it comes with a lot of machinery. Neon puts a Paxos quorum of Safekeepers
and fleet of Pageservers under every compute, and even then a
replica is eventually consistent, so read-your-writes have to be served from the
leader.
 AlloyDB reads its pages straight out of Colossus
(distributed, low-latency filesystem used across Google) and spins up a
read-only Postgres in a microVM for every agent that asks, with “sub-second
freshness”. That is the same asynchronous replication, with a better network and
faster storage.
Separating Storage doesn’t solve everything
Moving the pages to remote storage still doesn’t touch the rest of the list: a
process per connection, a row update causing write amplification across indexes,
VACUUM scans and pg_repack to deal with dead tuples, 32-bit transaction ids,
write amplification in physically replicated WAL, lack of native compression,
etc.
A stateless compute seems to help with multi-tenancy, because it lets you bring
up a Postgres instance per tenant without moving data. But having an instance
per tenant is expensive. A microVM makes it cheaper, but it comes with caveats.
You still have to preallocate minimum resources for that tenant, tear them down
after a period of inactivity to avoid billing for idle
resources, and every restart begins with empty cache. All these show up in
higher query latency.
A better way is resource pooling. Housing thousands of tenants on the same
server, charging them for what they used, throttling them when they use
resources beyond a cap. Nothing is reserved, or torn down, so no cold starts.
The server can be sized based on collective usage across all tenants, and get
much better resource utilization. If that sounds too far-fetched, note that
every web service already works this way: one process, thousands of users, each
billed for what they use.
Postgres cannot do this, because it cannot tell you what a query costs in CPU,
memory or disk IOPS. Nor does it make it safe to run these tenants together: as
mentioned earlier, one runaway query that gets OOM-killed brings
down the entire instance.
Egres From Scratch
Given all these, I gave up my earlier attempt at a “MyRocks for Postgres” and
decided to take the longer, more ambitious path to write Egres from scratch,
while ensuring Postgres wire protocol and SQL so existing tools would keep
working.
Egres is written in Zig. It allows using C libraries whenever relevant and it
gives explicit control over every allocation, which is what a per-query metering
needs. Most importantly, an allocation request can be rejected with an error,
instead of causing a process level panic or abort.
Egres is not trying to be a distributed, sharded database like CockroachDB,
Yugabyte or Multigres. Nor is it trying to replace Postgres everywhere. It is
designed for the workloads Postgres does not handle well: tables with many
indexes, terabytes on disk, or thousands of tenants sharing one node.
The Design
Thousands of Tenants in one Process
Status: Mechanisms are built. Cap enforcement mid-query in future release.
Egres is a single process, using a custom designed coroutine system called
 zfiber . zfiber spawns as many threads as the number of logical cores, and
cooperatively schedules fibers across these threads. All work across the
database: connections, queries, WAL, compactions, disk and network I/O are run
using these fibers.
Cpu Ticks and zfiber
zfiber is custom-built to the needs of a database. It is different from Go’s
goroutines or Rust’s Tokio in that it allows certain fibers to have higher
priority than others. For example, the fibers running Raft loops get higher
priority and chosen over others if ready and waiting. zfiber also support
dedicated lanes (dedicated threads) that fibers can’t cross. So a
very heavy query workload would not spill into the threads serving the Raft fibers.
zfiber threads have local task queues and run task stealing so no
thread sits idle while another has a queue. While zfiber doesn’t natively evict
a running fiber, functions in Egres run a maybeYield call which can be used to
optionally yield a fiber. zfiber tracks CPU ticks spent per fiber so it can tell
how much CPU a query took.
Direct I/O
Egres does direct I/O, bypassing filesystem cache. It stores the blocks read in
an S3-FIFO cache to avoid relying on page cache. All storage I/O
activity goes through a virtual filesystem API, which can meter the traffic to
device and throttle disk IOPS as needed. In fact, Egres runs a quick calibration
on boot to figure out each device’s bandwidth, and calculates the cost of writes
as a factor of cost of reads, so it can charge reads and writes accordingly.
Any disk activity causes a fiber to park and wait for the I/O completion,
meanwhile other fibers can run on the threads. zfiber uses Mitchell Hashimoto’s
 libxev which provides io_uring on linux.
Disk operations are throttled based on priority (and tenancy in future).
Inspired by the SILK paper , disk operations carry one of 3 priorities:
P0 is for queries, P1 and P2 for compactions. Knowing the full bandwidth of the
disk, lower priorities get the bandwidth the higher ones leave unused. Thus,
background compactions don’t interfere with queries and ensure query latencies
stay low even with many compactors running at the same time. The same mechanisms
could be applied to object storage, based on number of pending requests in
addition to bandwidth.
Memory
Furthermore, all memory is allocated via custom allocator, a thin wrapper over
jemalloc, which Zig’s allocator interface makes easy to do.
A memory governor tracks live memory against the total memory
allocated to the process. Every 100ms it sizes the block cache up and down to
make room for queries and background tasks, keeping the process under its
specified memory cap.
As of this release, only the total memory used by the process is being tracked.
Future releases will track memory per query and per tenant. An allocation could
then park the fiber waiting for some duration for more memory to become
available, or, if over the cap, fail with an error propagated back to the user
instead of an OOM kill.
One Process: Thousands of Tenants
Given these mechanisms, Egres would be able to accurately meter and throttle the
CPU ticks spent, the memory used, and the disk IOPS per query, per tenant. That
allows thousands of tenants to share resources, without any noisy neighbor
problem, and without running a VM per tenant.
MicroVMs
Beyond resource management, Neon and AlloyDB wrap each Postgres in a microVM for
two reasons, which don’t directly apply to Egres.
The first reason is best phrased by AlloyDB : “shared allocations
mean shared fate”. Postgres’s memory cannot be capped from outside, so a cgroup
limit means the OOM killer takes the postmaster down and every
tenant with it. In Egres, running out of a resource is a function error, which
can be treated like every other error and returned all the way back to the user.
Tenants share the resources but do not share the fate.
The second is security. Postgres has no boundary inside the process: extensions
are C running with the engine’s full power, and a memory-safety bug in that
code, reached through one tenant’s input, reaches every tenant’s data. A VM per
tenant puts a kernel between them.
Egres is one process too, so what it does instead is shrink the attack surface.
A client can send only SQL, a session is bound to one database at connection
time (auth coming in future release), and no tenant native code runs in the
process. Extensions will be compiled into the engine rather than loaded at
runtime, and user-defined functions, likely WebAssembly, will run in a sandbox
metered like any other fiber. That is the bet every multi-tenant web service
makes: a small surface instead of a kernel per customer.
Half the Disk, local or remote
Status: available in the current release.
ZDB: LSM Forest
Egres runs on top of a new storage engine I built, called zdb . While zdb
bootstrapped as a port of Badger from Go to Zig, it quickly went way beyond
Badger. zdb is a tree of LSM trees , aka an LSM forest, integrates
heavily with Raft consensus and reuses Raft write-ahead log instead of
having its own.
zdb mirrors the Postgres hierarchy. It has namespaces, which map to Postgres
databases. Each namespace owns many zdb tables. Each SQL table, and each of its
indexes, gets its own zdb table. Every zdb table is one or more LSM trees. The
benefit of this hierarchy is that zdb can branch or drop a namespace, table or
index instantly (see section about branching below). Moreover, heavy writes to
one table do not cause compaction pressure in another.
Shared Memtables
As you can imagine, an Egres instance which has hundreds of tables would have
hundreds of LSM trees. A typical LSM tree would have in-memory tables, called
memtables, and having memtables per tree would cause excessive memory usage.
To avoid that, zdb shares the same memtables across all namespaces, with keys
prefixed with (ns, table id) . SSTables are owned by the tree; the (ns, table id) can be inferred, so SSTables don’t store that prefix. The SSTable iterator
sets the (ns, table id) prefix to the keys it outputs during iteration, thus
allowing accurate key comparisons across tables and namespaces.
Tree Splits
Each table starts with one LSM tree, but as tree size grows (> 10 GiB), zdb can
split it in half to keep the compactions running predictably. Because each
tree’s size is bounded, zdb only uses 4 levels (Level 0 to Level 3) per tree.
Thus, each table can own many trees. Both the size and levels per tree are
configurable.
Tree splits don’t cause any data movement. zdb finds a median key which would
split the sizes as equally as possible based on the files in the last level, and
assigns SSTable files to each side. The files which overlap are assigned to
both. Later compactions only iterate over each tree’s assigned key range. Once
split, trees can run compactions independently and concurrently. Moreover, a
tree whose key range doesn’t get updates can avoid compactions entirely.
Compression and Checksum
zdb does block level compression, using the faster lz4 compression for L0 and L1
files, and the slightly slower but more powerful zstd for L2 and L3. On the
benchmark above, Egres took about half the disk Postgres did, the same kind of
saving that MyRocks brought to MySQL. Of course, savings from
compression depends a lot of the kind of data that’s being stored, so YMMV.
Every block carries a checksum, which is verified on every read, so a corrupt
block is caught before it’s served. In the future, these blocks can also be
encrypted to provide encryption at rest.
Local Disk Or Object Storage
zdb runs on local disk, or on object storage using S3 APIs. This allows Egres to
achieve a blazing fast NVMe experience with local storage. Or, a serverless
experience with remote object storage providing compute storage separation. When
using object storage, zdb uses a disk cache to store fixed-size file chunks on
local disk (if available), reducing S3 API calls and the associated latency.
This disk cache is in addition to the in-memory cache that zdb already uses to
store SSTable blocks across both storage mediums.
In fact, zdb internally uses a simple interface for file access, which can be
extended to other technologies like Azure Blob Store or Google Cloud Storage
APIs, or HDFS, etc.
Remote Data, Local WAL
Even when SSTables live on object storage, the WAL stays on local disk. A
write is deemed committed when its WAL entry is durable, so WAL latency dictates
commit latency. Low latency writes are only possible with local disk, not with
S3. Moreover, the WAL only needs a few gigabytes, which is cheap to allocate on
local NVMe, so Egres keeps WAL local.
The cost is that an Egres node is not fully stateless: a replacement node gets
the WAL from its Raft peers. That is fine here. One Egres node serves thousands
of tenants and doesn’t need to scale to zero when some of them go idle. So,
there’s no need to move the WAL off the node to make compute disposable.
Read your Writes from any replica
Status: Raft and the hybrid logical clock are already present. Multi-node setup
would be tested and made available in the next release.
Egres uses Raft for replication, for scaling out reads and to survive
node failures with automatic failover. Each entry in the Raft log stores a
hybrid logical clock (HLC) timestamp assigned by the leader, so timestamps
increase monotonically. As a replica applies the log, it advances its own clock
to the entry’s timestamp. That clock tells the replica how far behind the leader
it is, and which queries it can safely serve.
In a multi-node cluster (next release), the node you connect to would own the
session. A write arriving at a follower would forward it to the leader, who
would commit it through Raft, and return the commit timestamp back to the
follower to store it in the session. Any future reads can then be served
directly from the follower. The follower would block the read until it has
applied the log corresponding to the commit timestamp (typically milliseconds),
thus achieving read your write guarantee.
Replicated Compactions For Object Storage
As mentioned earlier, zdb reuses Raft WAL and integrates heavily with Raft. In
fact, it does something that’s harder to find in open-source: replicated
compactions. With files on object storage, a compaction is broken into 2
stages. First stage runs the compaction, generates the files, uploads them to
S3, and emits a manifest update for the leader to propose.
That update is optionally announced to the cluster first, so other nodes can
fetch chunks of the new files directly from S3 and warm them up before they are
needed. The leader then proposes the manifest update through Raft. The manifest
update is a delta: namespace id, tree id, minus these file ids at one level,
plus these file ids at the next. It does not contain the file data. Memtable
flushes go through the same process, so the log holds every change to zdb.
In the second stage: As the Raft log is applied, the manifest update is applied
to zdb in the same order, resulting in an identical zdb forest across all
replicas. Even the replicas which didn’t run the compaction get the compacted
forest.
This removes the need for every replica to run its own background compactions,
saving CPU and disk I/O. It also means the data lives once on S3, shared by
every replica, instead of each replica holding its own slightly different
version, N times for N replicas. The leader can also hand compaction work to any
node in the cluster to spread the load, savings its own resources, which are
the most precious in the cluster.
Replicated compactions also make bringing up a new replica on object storage
cheap and fast. The manifest is rebuilt from the WAL: fetch the last snapshot
manifest, apply the manifest updates since, then replay only the writes still in
memtables and not yet flushed, recreating the memtables. This yields an
identical zdb forest as all others; which also makes query latencies
predictable.
No VACUUM. No Repack.
Status: available in the current release.
zdb stores updates to the same row as versions. Each version carries its 64-bit
commit HLC timestamp, and a read at a timestamp returns the newest version at or
below it. Every read is a fixed snapshot over the entire database.
zdb does one interesting thing here. Other LSM trees write (key, version ts)
composite as the key, with one entry per version. zdb encodes the versions in
the value itself, keeping only one key per row. This reduces the number of keys
in the system by a factor, results in smaller SSTable block indexes and faster
key lookups.
Garbage Collection
Every Egres node tracks the minimum read timestamp of transactions currently
running in the system, as T low . It is bound by a configurable maximum
transaction age so an idle transaction cannot pin it forever. When followers
reply to the leader’s heartbeats, they include their T low .
When creating and proposing a snapshot, leader picks a raft index in the past,
which is either past a certain age min_age , or leaves certain WAL size
 min_bytes while ensuring it is picking all writes still in
memtable. For that Raft entry, it finds its HLC timestamp = T index .
Then leader calculates the minimum across all of these, with T snap =
MIN(T index , T low for each node ). When creating and proposing a
snapshot, leader sets this T snap . Once applied, every node in the
cluster rejects reads below T snap . Note that because every replica’s
open readers already counted towards the T snap , a replica doesn’t
have to kill a running query to keep up (except one beyond its max age).
All compactions can then drop unneeded versions below T snap , hence
garbage collecting them and freeing up space.
Simple, Effective GC
Both Egres and Postgres keep old versions for as long as the slowest reader
needs them. Egres does cap how long a transaction can stay open, so one
forgotten session cannot pin versions forever. The difference is what happens
afterwards.
In Postgres the dead tuples become holes in heap and index pages: VACUUM marks
the space reusable, but the table stays at its high-water mark, with live rows
spread thin across pages, until VACUUM FULL or pg_repack rewrites it. Moreover,
Postgres has to vacuum even a table nobody writes to, to freeze its transaction
ids before the 32-bit counter does.
In Egres, when T snap moves forward, the dead versions vanish at the
next compaction of their files, and the live ones are rewritten into dense new
files with no holes. Garbage collection piggybacks on compactions, which are
much lighter than a VACUUM scan. Each compaction operates on a few files at a
time, releasing disk space as it goes. Timestamps are 64-bit, so there’s no
counter to wrap.
100x Faster Multi-Index Lookups
Status: available in the current release.
Every row in an Egres table is keyed by a monotonically increasing 64-bit
integer id per table, called egid. In zdb, the rows are stored with keys
generated from these egids (big-endian order, 8-bytes per id) and map to the row
tuple. Each new commit for the same row adds a value version under the same key,
so egid assigned to a row never changes.
The user defined PRIMARY KEY is a unique secondary index from the encoded key to
the egid. This means a primary-key point lookup would read via 2 hops, first
from primary key to egid, then egid to row. In exchange, every index has the
same shape, index key -> egid(s), which are 64-bit ints and can be efficiently
encoded.
Egres exposes egid SQLite style. SELECT egid, col1, col2 FROM table . ... WHERE egid = N would avoid the index key -> rowid lookup, though that’s an
optimization. In the benchmarks , point reads via select queries,
which use primary index, Egres still came out ahead at p50 – 0.18ms Egres vs
0.52ms Postgres. The primary key to egid is a seek into SSTable blocks that are
already cached, and most likely to stay cached because of frequency of such
lookups.
Roaring Bitmaps Integration
Unsatisfied by the traditional roaring bitmaps implementations, I wrote
one in Zig called zroar . It stores containers in one serialized byte array,
instead of an adaptive radix tree with an allocation per container used by
others. Its in-memory form is the same as its on-disk form, so it avoids the
need for a deserialization step to run bitmap operations. Against CRoaring ,
it is 2x to 9x faster.
zdb understands that the values in an index table are 64-bit integers. A write
that touches an index produces a delta under the index key: plus row ids, minus
row ids. zdb stores these deltas as versions for the index key. As
compactions run, zdb folds these deltas into roaring bitmaps using zroar,
fetching the previous fold from lower levels if needed.
On index key lookup getBitmap(index_key, read_ts) , zdb fetches only the
versions (<= read_ts) up until the first fold it finds, loads the bitmap,
applies the delta versions in order and returns a zroar bitmap valid as of the
read timestamp.
This native support for indexes results in efficient index operations. What
would be a bitmap index scan in Postgres ( WHERE col1 = x ) is a single index
key lookup returning pre-generated bitmaps in Egres. Where this shows up most is
a query across two indexes with no composite index: WHERE col1 = x AND col2 = y . Two seeks, one intersection resulting in row ids.
AND, OR and NOT across indexes become bitmap operations: the planner, admittedly
simplistic as of this release, turns the index conditions into a tree of bitmap
nodes: Each leaf is an index read yielding a zroar, AND nodes intersect, OR
nodes union, and the bitmap at the root picks the rows to fetch.
As mentioned in Benchmarks section, this is what makes sku_day query 126x
faster at p95: 490 ms in Postgres against 3.9 ms in Egres. On
 customer_day_count , the other two-index query, Postgres p95 took 15.1 ms
against Egres 2 ms.
Batched Execution
Postgres pulls one row at a time through its tree of operators. Every row pays a
function call per operator and the CPU never sees enough work at once to pipeline
any of it. Egres does batched execution instead: the executor moves a batch
of rows through the operators, so the operator overhead is paid once per batch
rather than per row, and the rows an operator touches are already in cache. To
avoid copies, each operator updates a bit set marking which rows are still
selected.
Instant Branching of a database or a table
Status: available in the current release.
Egres supports instant branching for both databases and tables (with indexes).
It reuses the Postgres syntax: CREATE DATABASE dst TEMPLATE src branches a
 src database. CREATE TABLE dst AS TABLE src branches a table. In Postgres,
the table gets copied, but indexes are skipped. In Egres, the indexes are cloned
as well.
No actual data is ever copied though. Egres branches database (namespace) via a
single manifest update, which creates a new dst namespace, with new tables and LSM
trees, referencing the same SSTables from src .
The table and index schemas live in reserved tables within the namespace, so
they are cloned automatically. Unflushed writes sitting in memtables are copied
under the new namespace so no writes are lost.
A table branch works the same way for the table and indexes, plus a few extra
writes to copy their schemas in the reserved tables.
No Copy On Write
In fact, this system is better than the page level copy-on-write, where if 1000
pages get small updates, all those 1000 pages would have to be copied over and
rewritten. In zdb, the new writes land at the top of the corresponding LSM
trees, so the amount of data written is proportional to the new writes in the
system, not the data they overlap with.
Transactions: Repeatable Read, Pessimistic Locking
Status: available in the current release.
Egres provides Snapshot Isolation, the same as Postgres’ repeatable read
isolation. Serializable isolation is planned for future releases.
In Egres, write transactions run on the leader. At BEGIN, the transaction
assigns leader’s last applied timestamp as the read timestamp,
T read . From then on, every read gets a fixed snapshot of the
database as of T read . Reads do not block and do not acquire any locks,
unless FOR UPDATE .
Deadlock Detection
Writes use pessimistic locking. A write statement first gathers all the rows it
would change, then locks them in key order to avoid cycles. Locking is done via
 SemaphoreMap which exists only in leader’s memory. In addition to holding
locks, the map maintains a wait-for graph and detects any deadlocks at the time
of lock acquisition. In case it finds a deadlock cycle, the transaction is
immediately aborted and all held locks are released. There are no lock timeouts.
Conflict Detection
The leader also keeps an in-memory Oracle : a map from row hash to its
latest commit timestamp. After locks are acquired, their hashes are checked
against the Oracle to find the max commit timestamp among them,
T max_commit . If T max_commit is at or below
T read , nobody else changed them and the statement proceeds.
If T max_commit is higher than T read , the rows are stale.
Egres bumps up the T read to T max_commit and re-runs the
single statement; already acquired locks stay held.
A multi-statement transaction first checks if the earlier statements’ row hashes
have T max_commit above T read . If not, it executes the same
way as above, updating T read to T max_commit and re-running
the current statement. Otherwise, it fails the transaction with 40001, the same
serialization failure Postgres returns.
All of transaction’s row and index writes go into a memtable owned by that
transaction. When reading, this memtable is overlaid on zdb, so the transaction
can see its own pending writes. Nothing touches storage or the Raft log until
COMMIT, which proposes the entire write set, applied atomically on every
replica. There is no validation phase at commit, because every conflict was
settled by the above described locking process before the statement wrote
anything.
I chose pessimistic locking over optimistic on purpose. Dgraph had optimistic
locking which caused abort storms under high contention. N transactions would
race for a hot key, one wins, and N-1 waste all their work and have to re-do it.
Pessimistic locking turns that contention into a queue, while disjoint
transactions still run in parallel. Locks are taken on rows and unique index
keys only. Non-unique index updates to the same index key run concurrently.
Try it out
Egres is one binary. On Linux x86_64 or an Apple silicon Mac, easiest way to get
started is by running this command:
curl -fsSL https://egresql.io/install.sh | sh
 egres
 Then, with the psql you already have:
psql -h localhost -p 3210 -d egres
 The quickstart takes it from there: create a table, load some rows, and
branch the database. To build from source instead, you need Zig 0.16 :
git clone https://github.com/manishrjain/egres
 cd egres
 zig build -Doptimize=ReleaseFast
 zig-out/bin/egres
 This release is single node and the query features are basic, so
expect rough edges. Try it, and tell me what you find. Open an issue
for anything wrong, slow or missing, or for a feature you want. Star the
 repo to follow the progress. If you want to talk about Egres, you can
also hit me up on LinkedIn or email me at manishrjain+egres [at] gmail [dot] com . Thanks for reading.
© 2026 Manish Rai Jain Twitter · LinkedIn · GitHub · RSS

## 评论（1/1）

> **mrjn** · 2026-11-01T13:10:44.000Z　
> Author here. Egres is a Postgres-compatible database designed to tackle heavy workloads and run thousands of tenants on the same server. It works with psql and drivers unchanged. The post goes into details about the what, why and how; which I hope you'd find interesting.Before Egres, I was the founder of Dgraph -- author of Dgraph and Badger. ex-Google, ex-Uber. So, been working on databases for a while now. The idea for Egres all started with a question: "“What would Postgres look like if it were to be designed today?” After years of pondering and a year of work, the result is Egres.For Egres, I built a new storage engine called zdb, which is pioneering LSM forest concept -- a tree of LSM trees. zdb can run on local disk or object storage, has native roaring bitmaps integration, can do instant zero-copy branches for database or table.All of this runs on a custom co-routine system I built called zfiber, so all queries execute on that. Egres meters CPU ticks, disk IOPS and memory used per query, per tenant, so it can run thousands of tenants on the same server without noisy neighbor problem.This release is single node and the query ability is limited to equality (no joins) queries only. Raft replication is already baked in, future releases would allow multi-node clusters.Egres is open source under Apache 2.0, the GitHub repo is here: https://github.com/manishrjain/egres.Would love to know your thoughts, and which features to prioritize getting into next release.

## 关联链接

- https://egresql.io/install.sh
- https://github.com/manishrjain/egres

## 导航

- 项目页：[[10-项目/manishrjain.com_ad7697ca]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
