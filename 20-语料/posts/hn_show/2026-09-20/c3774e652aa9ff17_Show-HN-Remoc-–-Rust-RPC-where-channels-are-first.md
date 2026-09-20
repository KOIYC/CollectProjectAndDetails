---
type: "corpus"
item_id: "c3774e652aa9ff17"
title: "Show HN: Remoc – Rust RPC where channels are first-class values"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49713330"
project_url: "https://remoc.rs/"
author: "surban"
published_at: "2026-09-15T14:44:19Z"
captured_at: "2026-09-20T09:37:14+08:00"
lang: "en"
kind: "post"
topic: "开发者工具"
shard: "2026-09-20"
pub_day: "2026-09-15"
tags:
  - 语料
  - hn_show
  - author_surban
  - story_49713330
  - show_hn
metrics: {"points": 2, "comments": 0, "engagement_velocity": 2}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:90d"
---

# Show HN: Remoc – Rust RPC where channels are first-class values

> [!info] 一句话导读
> Remoc: Rust RPC with remote channels and objects

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49713330>
> 指标：点赞=2 · 评论=0 · engagement_velocity=2
> 作者：surban　|　发布：2026-09-15T14:44:19Z
> 项目链接：<https://remoc.rs/>
> 采集：2026-09-20T09:37:14+08:00　|　id：`c3774e652aa9ff17`

## 正文

Remoc: Rust RPC with remote channels and objects

# Remoc

Rust RPC with remote channels and objects over one connection.

 Remoc turns Rust traits marked with `#[rtc::remote]` into remotely callable interfaces, generating their clients and servers. Unlike conventional RPC, arguments and return values can contain Tokio-style remote channels and remote objects that remain usable after the call.

 A channel endpoint is an ordinary value that can travel inside a message, creating a new communication path wherever it arrives, without opening a port, looking up a name or registering anything. RPC calls, channels and remote objects are multiplexed over one TCP, TLS, WebSocket, pipe or other transport connection, each with independent flow control.

 $ `cargo add remoc` Copy the command

## One connection, many channels

 A single transport connection carries any number of independent, typed channels in either direction.

 Each channel keeps its own type and its own direction; the connection carries them all, in chunks, so a large message on one does not hold up the others. Back pressure is per channel too: a receiver that stops reading slows only its own sender.

## Channels are cheap, sendable values

 Channel endpoints can be sent inside messages, creating new communication paths without another transport connection. Here, the client asks the server to count and sends a channel for returning the numbers.

 Any channel can carry another. Here an RPC call hands over the sender of a new mpsc channel; there is no port to open, no name to look up and nothing to register or await.

Shared request

```
use remoc::prelude::*;

#[derive(Serialize, Deserialize)]
struct CountReq {
    up_to: u32,
    // A sender, on its way to the peer.
    seq_tx: rch::mpsc::Sender<u32>,
}
```

Server

```
while let Some(req) = rx.recv().await? {
    for i in 0..req.up_to {
        req.seq_tx.send(i).await?;
    }
}
```

Client

```
let (seq_tx, mut seq_rx) = rch::mpsc::channel(1);
tx.send(CountReq { up_to: 4, seq_tx }).await?;

// The channel is live now, nothing to set up.
while let Some(i) = seq_rx.recv().await? {
    println!("{i}");
}
```

### Complete runnable examples

 The excerpts above assume an existing connection. The examples here include every source file and the complete connection setup.

 Remote channels Send channel endpoints inside messages and use them from the other peer. View example → Trait-based RPC Generate a client and server from an async Rust trait. View example → Distributed tracing See remote calls as spans in the caller's trace via OpenTelemetry. View example → Web browser Connect Rust compiled to WebAssembly to a Rust server over WebSocket. View example →

## Multiple RPC calls, one round trip

 A call that hands out another object normally costs a round trip before that object can be used. Mark the method `#[pipelinable]` and the caller creates the client itself, then calls it while the request that opens it is still on its way.

 The counter is requested by the caller and calls to be performed with it are sent along with the initial request. They are run the moment the server attaches the counter to it. Only the final request is waited for, so the counter creation and the three calls that depend on it share a single round trip.

The remote trait

```
#[rtc::remote]
trait Directory {
    // Existing callers remain unchanged.
    #[pipelinable]
    async fn open_counter(&self, name: String) -> Result<CounterClient, OpenError>;
}
```

Sequential caller

```
// Request counter client, one round trip.
let mut counter = dir.open_counter(name).await?;

// Two calls, two round trips.
counter.increase(20).await?;
counter.increase(45).await?;

// Final call, one round trip.
let value = counter.value().await?;

// Total: four round trips.

```

Pipelined caller

```
// Create the counter client up front, no round trip.
let (mut counter, counter_rx) = CounterClient::new();

// Four calls, one round trip.
let value = rtc::calls!(
    dir.open_counter_pipelined(name, counter_rx);
    counter.increase_call(20);
    counter.increase_call(45);
    counter.value_call()
);
// Total: one round trip.

```

 A pipelined call may hand out a further object in turn, so a chain of them is still one round trip. How pipelining works →

## Messages that evolve with your application

 Remoc uses Postbag to encode your data, allowing independently deployed versions to keep communicating as their message types change. Fields and enum variants can be added, removed, renamed or reordered, while recoverable fields can isolate an incompatible change instead of losing the entire enclosing message.

### Remote channels

 MPSC, oneshot, watch and broadcast, with the API you already know from Tokio. They all share one transport and messages are sent in chunks, so a big blob on one channel does not stall the others.

rch module →

### Remote trait calls (RPC)

 Putting `#[rtc::remote]` on a trait generates client and server implementations. Arguments and return values may contain channels, allowing a method to return a stream of updates instead of a single value. Calls can be traced across both endpoints with OpenTelemetry.

rtc module →

### Remote callbacks

 Send a closure over and let the other side call it, for example to report progress or to be told when something happens. The arguments travel one way, the result comes back.

rfn module →

### Observable collections

 Hash maps, B-tree maps, vectors and sets that publish their changes. A subscriber receives an initial snapshot followed by each change as it occurs.

robs module →

### Remote objects

 Locks and read/write locks accessible from another machine, plus lazy values that are fetched only when accessed.

robj module →

### Transport independence

 Remoc is transport-independent. It operates over an `AsyncRead` and `AsyncWrite` pair or a `Sink` and `Stream` of packets. Worked examples cover TCP, TLS, WebSockets and pipes.

transports →

### Independent back pressure

 Each channel, remote function and trait call has independent flow control. A receiver that stops reading stalls only its own sender. Buffering remains bounded without per-call configuration.

### Transport performance

 In the published benchmarks, Remoc remains within 2 % of a plain TCP implementation in most tested configurations and saturates a 1 Gbit/s link.

Benchmarks →

### Safe Rust and WebAssembly

 Remoc contains no `unsafe` code and is built on Tokio. It also targets `wasm32-unknown-unknown` and WASI, allowing a browser tab to be one endpoint of a connection.

## How does Remoc compare?

 See where Remoc, tarpc, gRPC and Cap'n Proto differ in their contracts, transferable capabilities, conversation patterns and deployment trade-offs.

Selected capabilities from the full RPC library comparison

| Capability | Remoc | tarpc | gRPC | Cap'n |
| --- | --- | --- | --- | --- |
| Rust trait contract | ✓ yes | ✓ yes | ✗ no | ✗ no |
| Typed channels as values | ✓ yes | ✗ no | ✗ no | ✗ no |
| Promise pipelining | ✓ yes | ✗ no | ✗ no | ✓ yes |
| Either peer can serve | ✓ yes | ✗ no | ✗ no | ✓ yes |

## Connection resilience with Aggligator

 Remoc sessions are stateful: channels and remote objects remain connected for as long as the session does. The Aggligator crate provides a transport that keeps Remoc's logical connection alive when underlying links fail, reconnecting automatically without requiring the session to start over. It can also combine the bandwidth of multiple links.

## Common uses

 More on channels, RPC and inter-process communication (IPC) across process and machine boundaries.

# Epistemic Physics 1: Bayesian Special Relativity · raispace

## 导航

- 项目页：[[10-项目/remoc.rs_85b95f0b]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`开发者工具`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
