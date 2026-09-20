---
type: "corpus"
item_id: "5b4bb4947b635b75"
title: "The scourge of x86 emulation"
source: "lobsters"
source_name: "Lobsters"
url: "https://lobste.rs/s/iq6w6l/scourge_x86_emulation"
project_url: "https://fex-emu.com/Scourge-of-emulation"
published_at: "2026-09-19T00:01:05.094-05:00"
captured_at: "2026-09-20T03:40:49+08:00"
lang: "en"
kind: "post"
tags:
  - 语料
  - lobsters
  - hardware
metrics: {"score": 52, "comments": 0}
comments_count: 0
comments_total: 0
discovered_via: "lobsters:hottest"
archived: true
archived_at: "2026-09-20T09:21:33+08:00"
archive_reason: "渠道停用"
---

# The scourge of x86 emulation

- **来源**：Lobsters　|　**kind**：post
- **原帖**：https://lobste.rs/s/iq6w6l/scourge_x86_emulation
- **指标**：得分=52 · 评论=0
- **作者**：—　|　**发布**：2026-09-19T00:01:05.094-05:00
- **项目链接**：https://fex-emu.com/Scourge-of-emulation
- **采集**：2026-09-20T03:40:49+08:00　|　**id**：`5b4bb4947b635b75`

## 正文

Author: FEX-Emu

The scourge of x86 emulation – FEX-Emu – A fast linux usermode x86 and x86-64 emulator

# The scourge of x86 emulation

Welcome to the first feature article on our site. We’re going to cover an ongoing problem with x86 emulation that affects every application that we emulate. This comes down to a single over-arching term that has wide-reaching ramifications; Emulating the x86 Total Store Ordering memory model (x86-TSO).

The problems with emulating this memory model on the weak ordering memory model that ARM defines is multi-faceted and covers multiple issues. We’re going to go over all the problems that we can encounter and the ways we solve (or in some cases can’t solve) in this article. Get yourself a snack and a warm drink to enjoy, this is going to be a long one.

- What exactly is x86-TSO?
- The humble beginnings of ARMv8.0-a
- I thought accessing memory was the easy bit?
- Oh no, what are these atomic instructions?
- What do you mean split-lock is mandatory?
- Wait, uncached memory needs to work?
- Looking towards a brighter future

What exactly is x86-TSO?

Before diving in to how we work around the x86 memory model problem, we need to first discuss exactly what it is. A memory model is a set of rules for how memory accesses in a system behave in relation to each other. The rules will dictate how loads and stores interact in a single-threaded or a multi-threaded environment. There’s a handful of popular memory memory models implemented in various forms of hardware, but the two we care about today is ARM’s relaxed (or weak) consistency model, and the x86 variant of Total-Store-Ordering consistency model. These two models are basically the two extremes of the spectrum; where ARM is the most relaxed, allowing significant hardware optimizations; and x86 is the most strict, enforcing a very strong coherency model that doesn’t allow a lot of room for optimization. One thing to be careful about when discussing memory models is the difference between consistency and atomicity. While these are related, they are not the same nor guaranteed in all cases.

The best way to explain how the differences in memory models work is to start with how x86 handles this. With TSO being very strict in how it operates, the programmer can assume that when a memory store occurs, that this will be coherently visible to all other processors in the system. This additionally means that when a memory load occurs, all stores before it “logically” will have been completed, or at least visible. This matches programmer expectations, you write to memory, it becomes visible as at the point of writing, as this is intuitive to think about when programming. The stores are effectively ordering the visibility of the loads, thus the name of the model. There’s a bit of nuance with how this operates but isn’t strictly necessary to understand.

The weak memory model that ARM has is a bit less intuitive about how it operates. By default the regular memory loads and stores that ARM uses aren’t strictly coherent across processors in your system, allowing the CPU to operate more efficiently most of the time. When a store instruction executes, that piece of memory (the cacheline) isn’t immediately visible to other processors in the system. Saving on precious power and efficiency because it’s expensive in hardware to invalidate other core’s cachelines, or allow them to snoop another processor’s caches. Relatedly if a processor is loading data from memory that another processor has written to, it’s not guaranteed that this load will even see this updated memory. This sounds like it would cause some significant problems in a multi-threaded application right? Older versions of ARM (ARMv7 and older) used a memory barrier instruction to ensure ordering, which had significant performance implications.

To get around this limitation of consistency, ARM also introduced load-acquire, and store-release memory instructions. In C++ parlance this maps to std::atomic’s memory_order_acquire and memory_order_release definitions respectively. In ARM’s terminology, these instructions also aren’t technically considered to be atomic operations, but programmers conflate the two. FEX has used the terms atomic-load and atomic-store to mean the same thing! The distinction usually doesn’t matter, but when discussing these topics it may be better to be pedantic about it.

The primary use case for these instructions is to force memory ordering between these class of instructions. ARM calls this the “Release Consistency sequentially consistent (RCsc)” model. Without getting too far in to the weeds about how this model operates, the basic gist is that the load-acquire instructions must be observed sequentially without reordering, and the store-release instructions must as well while fulfilling “barrier-ordered-before” semantics. Removing the costly memory barrier instruction required in older ARM architecture versions.

The humble beginnings of ARMv8.0-a

This is the premise of where we start in ARMv8.0-a when we’re emulating the x86-TSO memory model. We make all x86 memory loads turn in to ARM’s load-acquire instructions, and x86 memory stores turn in to store-release instructions. This gives FEX effectively the same memory semantics as x86, although we are actually being more strict than what is necessary. This is because we had no middle-ground which exactly matches behaviour. As one might think, it is exceedingly costly to emulate TSO wth this instructions and we have microbenchmarks that can show this. As ARM CPUs weren’t designed to have these relatively rare acquire/release instructions suddenly become the vast majority of instructions executed.

First let’s start with something easy and use a microbenchmark that is fairly nice to the hardware. No tricky edge-cases, just accessing memory in in the common case. This gives us some baseline numbers for what the best-case situation should be.

Let’s break down this graph as it tells us a few interesting stories. The Load and Store columns of each machine is representing our baseline performance number that our hardware should be attempting to achieve. These aren’t trying to max out the memory bandwidth of each system, but do the same amount of work for each type of operation. If we turn our attention to the acquire-load results, we can see that out of the five CPUs tests, three of them have their performance hindered quite a bit by using acquire-loads! Additionally we can see that the AmpereOne CPU has release-store instructions that are strikingly low compared to the other results, and the M1 Acquire/LRCPC load instructions are quite a bit lower than the baseline as well.

The AmpereOne results in particular showcase how bad this legacy path can get. These instructions were never designed to be used this way. Using acquire-release semantics for every load for x86 emulation actually imposes some really strict limitations on ARM CPUs in that the load instructions can no longer be ordered around each other at all. So when you have millions of them in flight per second, the performance isn’t really expected to be good. But because these are the only instructions we had with ARMv8.0-a, it’s what we had to use. While Cortex-X4 and Cortex-X925 have amazing performance for these, you can see how the Oryon-3 has deprioritized their importance.

## Where do we go from here?

Let’s take a closer look at the LRCPC-load instructions, which is mandatory since ARMv8.3. This extension adds a bunch of new load instructions to the ARM ISA and adds a new memory model on top of ARM’s RCsc model from before. This new “Release Consistency processor consistent (RCpc)” memory model is what we’ve been wanting! This extension is designed around the requirements that x86 emulation requires, and is expected to get utilized heavily on hardware that implements it. As you can see from the graph, almost all of the platforms have their LRCPC-loads matching their regular loads in performance.

With th

# “The Secret Life of Circuits” is here - lcamtuf’s thing

## 关联链接

- https://fex-emu.com/Scourge-of-emulation/
