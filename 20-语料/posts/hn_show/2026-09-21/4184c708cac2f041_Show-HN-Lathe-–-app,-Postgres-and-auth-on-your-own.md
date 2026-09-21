---
type: "corpus"
item_id: "4184c708cac2f041"
title: "Show HN: Lathe – app, Postgres and auth on your own machine, from $15/mo"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49775468"
project_url: "https://lathe.live/"
author: "evgenileonti"
published_at: "2026-09-20T13:05:29Z"
captured_at: "2026-09-21T09:44:03+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-21"
pub_day: "2026-09-20"
tags:
  - 语料
  - hn_show
  - author_evgenileonti
  - story_49775468
  - show_hn
metrics: {"points": 3, "comments": 0, "engagement_velocity": 3}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:3d"
---

# Show HN: Lathe – app, Postgres and auth on your own machine, from $15/mo

> [!info] 一句话导读
> Classic System fonts, slate

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49775468>
> 指标：点赞=3 · 评论=0 · engagement_velocity=3
> 作者：evgenileonti　|　发布：2026-09-20T13:05:29Z
> 项目链接：<https://lathe.live/>
> 采集：2026-09-21T09:44:03+08:00　|　id：`4184c708cac2f041`

## 正文

Skip to content
lathe
Style
Classic System fonts, slate
 Developer Geist, mono interface
 Terminal Mono everywhere, phosphor
 Mode
System
 Light
 Dark
Apps
 Auth
 Pricing
 Docs
 Sign in
Style
Classic System fonts, slate
 Developer Geist, mono interface
 Terminal Mono everywhere, phosphor
 Mode
System
 Light
 Dark
One machine · yours alone · from $15 a month
Your whole app on one machine, run for you. From $15 a month.
Your app, its database and its sign-in on one dedicated machine. Deploy any container beside Postgres, Redis, CouchDB and NATS; we run the backups, TLS, monitoring and updates. One flat bill - nothing metered, no price per user.
Start free - 14 days, no card needed See how it works →
Billed monthly. Cancel any time. Mini starts with a 14-day free trial.
20 GB NVMe, not a network volume
20 TB traffic a month, unmetered
7 daily backups, restore-tested
90 s from checkout to live
Why a whole machine
 Managed sprawl or DIY operations. Lathe is the third way.
 Built for solo builders and small teams who want real infrastructure at a price they can explain, without becoming the person who runs it.
Managed platforms
 A slice of each of their clusters.
 The database from one vendor, the cache from another, the queue from a third, sign-in priced per user, and the app host on top, each metered on its own. The price on any one pricing page is never the price on the pile of invoices.
A bare VPS
 The whole box, cheap.
 Excellent hardware for very little. Then backups, TLS, credentials, upgrades, monitoring, deploys and the night something stops answering are all yours.
Lathe
 The whole box, ours to run.
 One dedicated machine with Postgres, Redis, CouchDB and NATS on it, your app and its sign-in beside them. We do the running: restore-tested backups, TLS everywhere, credentials, patching in a fixed window, monitoring, an API, an MCP server, webhooks. You get standard connection strings and a flat price.
Nothing metered: storage, traffic, connections, users and requests are in the plan.
 The app, the databases and the sign-in on the same machine, at the same price.
 Deploy from a GitHub push. Lathe deploys itself this way.
 Standard protocols and credentials; leave with a dump any time.
How it works
 From a push to a running product, on one machine.
 One workflow instead of a vendor pile: the app, its databases and its sign-in come up together and stay together, switched on from the same Engines settings, at the same price.
1. The machine
 Pick a plan, get a box.
 A dedicated machine, live about 90 seconds after checkout, with Postgres, Redis, CouchDB and NATS on it in any mix, each engine with a memory budget out of the plan's RAM. Mini starts with 14 free days, no card needed.
2. The app
 Push, and it deploys.
 Any image, any language, pulled from your registry with every engine's connection string already in its environment. Connect the GitHub repository that builds it and a green run deploys: the new version starts beside the old one and takes traffic once it answers its health path, on your domain with its certificate.
 The Apps engine →
3. The sign-in
 Users in your own Postgres.
 Email links and codes, OAuth with GitHub, Google and the rest, multi-factor and sessions, with every user in the auth schema of your own database, readable by your role. Built on the open-source Supabase Auth server, so supabase-js works unchanged. No price per user.
 The Auth engine →
lathe.live runs on Lathe: the site you are reading, the portal and the API are an app on a Lathe machine, deployed from a GitHub push the same way yours is, with its own database on a Lathe instance. When something here breaks, it breaks for us first. How the deploy works →
What the price includes
 Run properly, not just provisioned.
Storage on NVMe Local NVMe, not a network volume - lower latency on every write. Sized with the plan, never metered.
Daily backups, 7 kept Restore any of the last 7 in place; your connection string does not change. Every restore is preceded by a snapshot, so it can be undone for 7 days. The latest backup is restored to a temporary server and checked every month, so it is one we have seen work.
Traffic, 20 TB a month 20 TB of outbound traffic a month, included and unmetered. Above that we contact you first; overages are discussed, not charged.
Connection pooling and TLS PgBouncer (transaction mode) on 6432 , direct Postgres on 5432 , TLS and SCRAM-SHA-256 on both. Optional IP allowlist.
Engines, composed per instance Choose the engines at creation and change them later; each gets a memory budget from the plan's RAM, TLS and credentials of its own, and the same price: none. The data engines are the unmodified upstream builds.
 Postgres 17 - Relational SQL database. Standard, rock-solid; pgvector and the usual extensions.
 Redis 8 - Cache and real-time. In-memory speed; append-only log for durability.
 CouchDB 3 - NoSQL document store. Erlang engine; tiny idle footprint; sync-friendly.
 NATS 2 - Messaging and streams. Go single binary; queues and event streams.
 Apps - Your web apps. One image each, deployed from a push, the machine's engines a loopback away.
 Auth - Sign-in and users. No per-user price; supabase-js and the Supabase auth clients work unchanged.
A machine of your own Your instance is the only thing on it: a dedicated machine where your queries have the full memory and disk.
Postgres 17 and the usual extensions pgvector , pg_stat_statements , pg_trgm and pgcrypto enabled from the start. Minor updates for every engine and OS security updates in a fixed weekly window (Sundays 03:00 UTC), announced in advance.
Self-serve operations Create, restore, reset, rotate credentials, allowlist, resize, delete; per engine, its settings, restart and reset; inside the engines, databases and extensions, a Redis console, CouchDB's Fauxton, JetStream streams. From the portal, the REST API or the MCP server, instantly.
Support and the trial Email support with a reply within 24 hours on business days; we watch the alerts. Mini starts with 14 free days, no card needed: add one before the end to keep it, or let it go and nothing is ever charged.
What $29 a month buys
 One Starter box, fully allocated.
 Not a share of a pool. This is the whole 4 GB of Starter with every engine switched on - the split you get if you do not choose your own, drawn to scale. Mini holds any mix that fits its 1740 MB for engines; every engine at once starts at Starter.
0 MB 2048 MB 4096 MB
Postgres 17
 1437 MB 35.1%
Redis 8
 479 MB 11.7%
CouchDB 3
 479 MB 11.7%
NATS 2
 479 MB 11.7%
Apps
 479 MB 11.7%
Auth
 128 MB 3.1%
System headroom
 615 MB 15.0%
Headroom is the kernel, the pooler, the exporters and the backup scripts - 15% of the machine, kept back so the engines never fight it. Change the mix any time: an engine you switch off stops with its data kept and its memory goes back into the budget, and automatic reallocation moves memory between the ones that are on from what each holds.
Connect
 Standard protocols. Real credentials.
 pg_dump , redis-cli , CouchDB replication and NATS tooling work exactly as they do anywhere. Every connection is standard; learn once, use everywhere.
psql "postgres://app:••••@db-7f3a.lathe.computer:6432/app?sslmode=require"
rediss://default:••••@db-7f3a.lathe.computer:6379
https://admin:••••@db-7f3a.lathe.computer:6984/
tls://app:••••@db-7f3a.lathe.computer:4222
Plans
 Four plans. The same product on each.
 Pick by how much you store and how much memory the engines need. Everything below is in every plan, including 20 TB of outbound traffic a month.
Plan vCPU RAM Storage Traffic Price Best for Choose a plan
Mini 14-day free trial 1 2 GB 20 GB 20 TB $15/mo A small app with its database Try Mini free - no card needed →
Starter The full stack 2 4 GB 40 GB 20 TB $29/mo The whole stack at once: app, data, sign-in Choose Starter →
Plus 4 8 GB 80 GB 20 TB $49/mo A busier app, a bigger store Choose Plus →
Pro 8 16 GB 160 GB 20 TB $89/mo A heavy database with the stack beside it Choose Pro →
Billed monthly in USD, in advance. Everything is included: usage, traffic, connections and every engine. Upgrades at any time: more storage means the next plan. Mini starts with a 14-day free trial, no card needed; the other plans are paid at creation.
Questions
 The ones people actually ask.
Is there a free tier or a trial? A trial: Mini starts with 14 free days, no card needed, and the instance is yours at once. Buy the plan before the trial ends to keep it - the first month ($15) is charged when you do; without that it pauses and is deleted 7 days later. One trial per person. Other plans are paid at creation and the card is kept for renewals. There is no free tier: each instance is a dedicated machine with a real cost. Delete the instance at any time and billing stops; a final snapshot is kept 7 days. New accounts are limited to one instance until the first renewal.
What if something breaks, or I need help? Email us; a person replies within 24 hours on business days. Failed jobs, health checks and backup verifications alert us directly, and an instance that stops answering is restarted automatically. Each instance runs on one machine; availability depends on that machine.
How long until I have a connection string? About 90 seconds. Instances boot from pre-built images; nothing is installed at creation time.
What happens when my disk fills up? At 80% you receive an email and a banner on the instance page, with the upgrade a click away in Settings. At 95% Postgres stops accepting writes until you upgrade or free space. Redis, CouchDB and NATS stop accepting writes too, so for multi-engine instances the warning is your only guard.
Do you check that the backups actually restore? Yes, monthly and automatically. Each instance's latest backup is restored to a temporary server, checked engine by engine ( pg_amcheck and a row-count sample for Postgres), then destroyed. Failures alert us directly.
Is a disk snapshot a safe backup for a running Postgres? Yes. Postgres keeps a write-ahead log, so an image of a running machine is crash-consistent: on start it replays the log up to the last committed transaction, the same recovery it performs after a power cut. What makes a backup unsafe is never restoring it, which is why every instance's latest backup is restored and checked once a month.
How do I move an existing database in? Point pg_dump at your current database and restore it over the direct port (5432) on the new instance; the other engines take their own standard import and replication tools. Data stays in standard formats; your dump is yours unchanged. Tell us if the dump is large and we will help with the run.
Can I get my data out? Yes. You hold standard credentials; pg_dump , redis-cli , CouchDB replication and NATS tooling work at any time. Standard protocols and tools are used throughout.
What does a restore actually do? Backups run daily; 7 are kept. A restore snapshots the current disk, then rebuilds the instance from the backup you choose; the address is unchanged. Downtime depends on data size. The pre-restore snapshot is kept 7 days, so any restore can be undone.
Where does my data live, and who touches it? In the datacenter you choose - Finland or Germany - and it stays there. One infrastructure provider runs the machines and no one else has access, and we do not look at database contents except to handle a request you made.
Can I run one engine without the others? Yes, any combination, chosen at creation or changed later. A disabled engine is stopped with its data kept on disk and resumes when re-enabled. At least one engine must be on.
Which versions and licences? Postgres 17 (PostgreSQL); Redis 8 (AGPL-3.0); CouchDB 3 (Apache-2.0); NATS 2 (Apache-2.0). All upstream builds, unmodified; we add TLS, credentials and a memory budget.
Can I run my app on it too? Yes. The Apps engine runs your own container image on the same machine as its databases, with their connection strings already in its environment, served over https on a name of its own and on your domains. A deploy starts the new version beside the old one and moves traffic once it answers; connect a GitHub repository and a green run of your workflow deploys it. It is in the plan price. The Apps engine .
Is there sign-in for my app? Yes. The Auth engine runs sign-in beside your app: email links and codes, OAuth, multi-factor, sessions, with the users in the auth schema of your own Postgres. It is built on the open-source Supabase Auth server, so supabase-js works unchanged. In the plan price, with no price per user. The Auth engine .
Can I move up a plan later? Yes, at any time; storage grows with the plan and every engine's memory budget scales with it. Upgrades only, with a few minutes of downtime at a time you choose.
Can an AI agent do this for me? Yes. The MCP server at https://mcp.lathe.live exposes everything the portal does; Claude.ai connects with a sign-in, other clients with an API key. The plain-text page gives an agent the facts.
One dedicated machine, 20 GB, backed up daily, your app on it, for $15 a month.
Live about 90 seconds after checkout. Cancel any time; Mini starts with a 14-day free trial.
Start free - 14 days, no card needed
 Run in the open: live status , the latest backup of every instance restore-tested each month, support answered within 24 hours on business days, updates in a fixed weekly window (Sundays 03:00 UTC), your choice of datacenter (Finland or Germany). Operated by Lathe.
Lathe
Pricing
 Postgres
 Redis
 CouchDB
 NATS
 Apps
 Auth
 Guides
 For agents
 Terms
 Privacy
 Docs
 Status
support@lathe.live
Are you sure?
Type to confirm
Cancel Confirm

## 关联链接

- https://admin:••••@db-7f3a.lathe.computer:6984/
- https://mcp.lathe.live

## 导航

- 项目页：[[10-项目/lathe.live_1e9e0133]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
