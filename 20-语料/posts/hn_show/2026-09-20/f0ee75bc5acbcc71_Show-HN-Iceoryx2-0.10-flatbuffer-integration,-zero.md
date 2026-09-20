---
type: "corpus"
item_id: "f0ee75bc5acbcc71"
title: "Show HN: Iceoryx2 0.10: flatbuffer integration, zerocopy IPC with unbounded data"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49758211"
project_url: "https://ekxide.io/blog/iceoryx2-0.10-release"
author: "elfenpiff"
published_at: "2026-09-18T18:23:19Z"
captured_at: "2026-09-20T09:36:36+08:00"
lang: "en"
kind: "post"
topic: "开发者工具"
shard: "2026-09-20"
pub_day: "2026-09-18"
tags:
  - 语料
  - hn_show
  - author_elfenpiff
  - story_49758211
  - show_hn
metrics: {"points": 2, "comments": 0, "engagement_velocity": 2}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:90d"
---

# Show HN: Iceoryx2 0.10: flatbuffer integration, zerocopy IPC with unbounded data

> [!info] 一句话导读
> Published: 2026-09-19

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49758211>
> 指标：点赞=2 · 评论=0 · engagement_velocity=2
> 作者：elfenpiff　|　发布：2026-09-18T18:23:19Z
> 项目链接：<https://ekxide.io/blog/iceoryx2-0.10-release>
> 采集：2026-09-20T09:36:36+08:00　|　id：`f0ee75bc5acbcc71`

## 正文

Published: 2026-09-19
Author: Christian Eltzschig

Announcing iceoryx2 v0.10.0 - ekxide Blog | ekxide

# Announcing iceoryx2 v0.10.0

Christian Eltzschig - 19/09/2026

## What Is iceoryx2?

iceoryx2 is a communication library designed to build robust and efficient data-intensive systems. It enables ultra-low-latency communication between processes - comparable to Unix domain sockets or message queues, but significantly faster and easier to use.

The library provides language bindings for C, C++, Python, Rust, and C#, and runs on Linux, macOS, Windows, FreeBSD, and QNX, with experimental support for Android and VxWorks.

iceoryx2 supports multiple messaging patterns, including publish-subscribe, events, request-response streams, and the blackboard pattern, a key-value repository implemented directly in shared memory. Its architecture is fully decentralized and does not rely on a central broker, which improves robustness and scalability.

To get a better impression of the performance characteristics, check out the iceoryx2 benchmarks and try them on your own platform.

| |
| --- |

- Project iceoryx2 on GitHub
- iceoryx2 Book
- Project iceoryx2 RMW for ROS on GitHub
- Project on crates.io

## Release v0.10.0

With v0.10.0, we are landing something that both the community and we have wanted for years: support for dynamically growing, unbounded payloads in shared memory while preserving iceoryx2's zero-copy communication.

Another frequent request from the community was native integration of a serialization format such as FlatBuffers. Thanks to Gravis Robotics, who funded both features, these capabilities are now available in iceoryx2.

Take a look at the iceoryx2 v0.10.0 release notes for the complete list of changes.

Our predecessor, iceoryx classic, has entered maintenance mode. We will continue to fix important security issues on its main branch, but our development focus has now shifted completely to iceoryx2. If you are still using iceoryx classic, now is a good time to start looking into migration. And if you require support or miss a feature, we are happy to help.

At the end of this year, iceoryx classic will reach end of life, and support will only be available to customers.

The main highlights of iceoryx2 v0.10 are:

- FlatBuffers Support & Sending Unbounded Data
- Robust Event Messaging Pattern
- Gateway Improvements
- Developer Experience and Quality-of-Life Improvements

### FlatBuffers Support & Sending Unbounded Data

Until now, iceoryx2 required an upper bound for the payload size. Every endpoint needs to map the shared-memory segment into its process address space, which makes resizing that segment later practically impossible.

When we introduced dynamic data support based on slices, we took a first step toward overcoming this limitation. However, users still had to provide an upper bound for the payload size at runtime, and resizing an already-loaned sample was not possible.

With the FlatBuffers integration and the new FlatBuffers allocator, we are taking the next step. The allocator can reallocate data for an already-loaned sample, allowing dynamically growing FlatBuffers payloads to be sent via iceoryx2 without requiring a predefined upper bound.

FlatBuffers can also build serialized data directly in shared memory. On the receiving side, that data can be consumed directly from shared memory as well. This avoids additional copies around serialization and deserialization and makes FlatBuffers a natural fit for zero-copy communication.

Take a look at our FlatBuffers publish-subscribe and request-response examples.

### Robust Event Messaging Pattern

In the past, event notifications could be lost when the buffer of the underlying mechanism was exhausted. Depending on the platform and implementation, this could for example happen when a Unix domain socket buffer was full or a semaphore overflowed. For mission-critical systems, losing an event notification in this way is not acceptable.

We therefore refactored the event messaging pattern. With v0.10, iceoryx2 can guarantee that notifications are never lost.

When a listener waits for incoming notifications, iceoryx2 now provides both the event ID that woke it up and the number of times that event was sent.

### Gateway Improvements

The tunnel building blocks received several improvements in this release:

- Allocations were removed from the hot path to improve performance.
- Additional configuration options were added, including an allowlist.
- A reactive execution mode is now available.

These building blocks are also an important foundation for the generic gateway concept we are currently working on.

### Developer Experience and Quality-of-Life Improvements

- Per-Subscriber Configurable History: Subscriber ports within the same service can now use different history sizes. The service only defines the maximum supported history size.
- Port Names and Direct Connections: Consider a reactive client-server scenario where a server sends a notification as soon as a response has been sent. Previously, all listeners of the event service would have been woken up. Ports can now be assigned names, and notifications can be sent directly to a specific listener identified by its port name. This makes it possible to wake only the port that is actually waiting for the notification.
- Reduced bindgen Dependencies: Some users encountered problems with `bindgen` on specific platforms. To reduce this dependency, we ported our platform abstraction layer to `libc` wherever possible.
- Minimum Rust Version Set to 1.89

## Roadmap: What’s Next?

- ekxide Mission Control: Mission Control is planned for release on 26 September 2026.
- Generic Gateway Concept: We are working on reusable building blocks that will allow us to add gateways to different protocols quickly, with little to no configuration required for the default use case.
- ROS 2 to iceoryx2 Gateway: The first gateway implementation will connect ROS 2 with iceoryx2, allowing both ecosystems to work together while making it easier to move between them. On 29 September 2026, Gravis Robotics and Foxglove will showcase this in Zurich. If you have time, register for the event and join us.

## Thank You

Most of the features we develop are funded by our customers. With this release, we are able to name one of them, and we want to explicitly thank Gravis Robotics.

They funded the FlatBuffers integration and unbounded data support included in v0.10. They are also currently funding the development of our generic gateway concept and the first gateway implementation connecting iceoryx2 and ROS 2.

We also want to thank our community. Your ideas, discussions, bug reports, and contributions help shape iceoryx2 every day. Even frustrating bugs become a little less painful when they are tackled with humor and openness.

A big thank you also goes to the iceoryx team, who were relentless in implementing these features and improvements.

And finally, thank you to all our customers who help us keep the development pace high and share our vision:

To create an open-source zero-copy data plane for physical AI and mission-critical systems.

# Show HN: Open-source revenue recognition and analytics for Stripe and Metronome | Hacker News

## 导航

- 项目页：[[10-项目/ekxide.io_e73754f2]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`开发者工具`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
