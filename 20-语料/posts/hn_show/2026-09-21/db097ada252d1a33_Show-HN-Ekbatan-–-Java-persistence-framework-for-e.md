---
type: "corpus"
item_id: "db097ada252d1a33"
title: "Show HN: Ekbatan – Java persistence framework for event-driven systems"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=48731373"
project_url: "https://zyraz-io.github.io/ekbatan"
author: "unikzforce"
published_at: "2026-06-30T11:52:13Z"
captured_at: "2026-09-21T02:53:10+08:00"
lang: "en"
kind: "post"
topic: "开发者工具"
shard: "2026-09-21"
pub_day: "2026-06-30"
tags:
  - 语料
  - hn_show
  - author_unikzforce
  - story_48731373
  - show_hn
metrics: {"points": 3, "comments": 0, "engagement_velocity": 3}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:113d"
---

# Show HN: Ekbatan – Java persistence framework for event-driven systems

> [!info] 一句话导读
> Ekbatan — Event-driven Java Persistence Framework

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=48731373>
> 指标：点赞=3 · 评论=0 · engagement_velocity=3
> 作者：unikzforce　|　发布：2026-06-30T11:52:13Z
> 项目链接：<https://zyraz-io.github.io/ekbatan>
> 采集：2026-09-21T02:53:10+08:00　|　id：`db097ada252d1a33`

## 正文

Ekbatan — Event-driven Java Persistence Framework

# Ekbatan event-driven java persistence framework.

v1.0.0-RC1 · Apache 2.0 · Java 25+

Ekbatan is a Java persistence framework for event-driven systems. One database transaction commits your data and the domain events; the persisted events can then be drained from the events outbox table to Kafka or any event broker.

A replacement for Hibernate, Spring Data, or hand-rolled JDBC. Drops into Spring Boot, Quarkus, or Micronaut — or plain java.

## Two writes. Two systems. One silent drift.

Your service inserts a row into the database, then publishes an event to Kafka. Two independent operations across two systems. If the second fails — Kafka outage, network blip, service crash — the row is committed but the event is lost. Your database and your event stream silently disagree.

### Two writes

✗ broken

app db State saved kafka Publish failed consumer No events

Crash between writes ⇒ DB and Kafka disagree.

The solution is a known pattern: the Transactional Outbox. Write the row AND the event into the same database transaction — both commit or both roll back. A separate process (a CDC tool like Debezium, a background job, or similar) drains the outbox table to Kafka, retrying until delivery succeeds.

Ekbatan makes adopting this pattern hassle-free. No boilerplate, no glue code, no outbox plumbing to maintain. The publish step stays decoupled by design — pair it with Debezium or any CDC tool of your choice.

### One write + outbox

✓ Ekbatan

database (one tx)

state events

Kafka

consumer

CDC tails the outbox — events ship later, always in sync.

Read the full explanation →

### MODEL is Immutable. Attaches its own events upon change.

A domain object that emits events when it mutates. `deposit(amount)` returns a new `Wallet` with a `WalletMoneyDepositedEvent` attached inside the same builder call. State and event coupled at the source — never two writes. Don't need events for a table? Extend `Entity` instead — same persistence surface, no event emission.

 Wallet.java

 1 @ AutoBuilder

 2 public final class Wallet extends Model< Wallet, …> {

 3 public final BigDecimal balance;

 4 // …

 5

 6 public Wallet deposit(BigDecimal amount) {

 7 return copy()

 8 . withEvent(new WalletMoneyDepositedEvent(id, amount))

 9 . balance(balance. add(amount))

 10 . build();

 11 }

 12 }

### ACTION Reads, mutates, PLAN the changes. ActionExecutor will persist the PLANNED changes.

A unit of business work. `perform()` reads from a repository, mutates the model, stages the new version on `plan()`. No transaction handling, no direct writes. Once `perform()` returns, `ActionExecutor` opens one database transaction and persists everything atomically — domain rows AND the matching events in the outbox table. All of it commits, or all of it rolls back.

 WalletDepositAction.java

 1 @ EkbatanAction

 2 public class WalletDepositAction extends Action< Params, Wallet> {

 3

 4 protected Wallet perform(Principal p, Params params) {

 5 var wallet = walletRepository. getById(params. walletId());

 6 return plan(). update(wallet. deposit(params. amount()));

 7 }

 8 // …

 9 }

### ACTION EXECUTOR runs the action. Wherever you call it from.

The framework's single entry point. Inject it via DI and call `execute(SomeAction.class, params)` from anywhere — a Spring `@RestController` (shown), a Quarkus resource, a scheduled job, a CLI command. The executor handles discovery, `perform()`, the transaction, and the atomic commit.

 2 @ RequestMapping("/wallets")

 3 public class WalletController {

 4

 5 private final ActionExecutor executor;

 6 // …

 7

 8 @ PostMapping("/{id}/deposit")

 9 public Wallet deposit(@ PathVariable UUID id, @ RequestBody Body body) throws Exception {

 10 return executor. execute(() -> "rest-user", WalletDepositAction.class,

 11 new Params(Id. of(Wallet.class, id), body. amount()));

 12 }

 13 }

### jOOQ-backed. Thin extension.

A short subclass of `ModelRepository`. Inherits `getById` / `add` / `update`; custom queries written in the typed jOOQ DSL when you need them — no JPA, no annotations soup.

 1 @ EkbatanRepository

 2 public class WalletRepository extends ModelRepository< Wallet, …> {

 3

 4 public List< Wallet> findAllByOwnerId(UUID ownerId) {

 5 return readonlyDb()

 6 . selectFrom(WALLETS)

 7 . where(WALLETS.OWNER_ID. eq(ownerId))

 8 . fetch(this:: fromRecord);

 9 }

 10 // …

 11 }

ATOMIC★ OUTBOX-NATIVE★ JAVA 25★ JOOQ★ VIRTUAL THREADS★ MULTI-DATABASE★ SHARDED★ SPRING · QUARKUS · MICRONAUT · PLAIN JAVA★ POSTGRES · MARIADB · MYSQL★

ATOMIC★ OUTBOX-NATIVE★ JAVA 25★ JOOQ★ VIRTUAL THREADS★ MULTI-DATABASE★ SHARDED★ SPRING · QUARKUS · MICRONAUT · PLAIN JAVA★ POSTGRES · MARIADB · MYSQL★

### Learn

A progressive path through the framework: why it exists, how Actions commit state and events, how to consume events, how sharding and sagas fit, then the complete project setup when you're ready.

## 导航

- 项目页：[[10-项目/zyraz-io.github.io_fb14223a]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`开发者工具`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
