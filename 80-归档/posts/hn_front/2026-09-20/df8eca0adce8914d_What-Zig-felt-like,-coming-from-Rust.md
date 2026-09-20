---
type: "corpus"
item_id: "df8eca0adce8914d"
title: "What Zig felt like, coming from Rust"
source: "hn_front"
source_name: "HN 首页（非 Show HN）"
url: "https://news.ycombinator.com/item?id=49766637"
project_url: "https://besok.github.io/posts/what-zig-felt-like-coming-from-rust"
author: "ksec"
published_at: "2026-09-19T13:55:18Z"
captured_at: "2026-09-20T09:20:18+08:00"
lang: "en"
kind: "post"
tags:
  - 语料
  - hn_front
  - author_ksec
  - story_49766637
  - front_page
metrics: {"points": 142, "comments": 166, "engagement_velocity": 142}
comments_count: 165
comments_total: 165
discovered_via: "hn:front_page:2d"
archived: true
archived_at: "2026-09-20T09:21:31+08:00"
archive_reason: "渠道停用"
---

# What Zig felt like, coming from Rust

- **来源**：HN 首页（非 Show HN）　|　**kind**：post
- **原帖**：https://news.ycombinator.com/item?id=49766637
- **指标**：点赞=142 · 评论=166 · engagement_velocity=142
- **作者**：ksec　|　**发布**：2026-09-19T13:55:18Z
- **项目链接**：https://besok.github.io/posts/what-zig-felt-like-coming-from-rust
- **采集**：2026-09-20T09:20:18+08:00　|　**id**：`df8eca0adce8914d`

## 正文

What Zig felt like, coming from Rust | besok

## Intro

I’ve spent the last 7 years as a Rust developer, working mostly on open source projects, and I’d like to think I’ve built a solid feel for the language and its ecosystem along the way. I gravitate toward the functional side of Rust like clean functions, expressive types, that sort of thing. But I’m always curious about other languages, and Zig has been on my radar for a while as a candidate C successor: lower-level, lighter-weight, and steadily earning its place among the languages people take seriously. I spent time with C earlier in my career, so the comparison always felt like it would be interesting to make.

One caveat worth stating up front: my experience with Zig begins with this project. Some of the observations will look naive and obvious for the people who work with Zig on daily basis and some of the decisions I made along the way were almost certainly not the optimal ones, they were shaped more by habits carried over from Rust than by deep Zig idiom. That’s fine, everyone has to start somewhere, and in the meantime I’m leaning on whatever cross-language intuition I’ve built up over the years, for better or worse.

To make the comparison fair, I decided to reimplement something I’d already built in Rust, not a toy, but not a sprawling project either, and ideally something the community could actually use. I settled on JSONPath: a query language for JSON, specified in RFC 9535. The Rust version already existed (jsonpath-rust), and the goal was to bring the same thing to Zig: zig-jsonpath.

## IDE support

The first thing that caught me off guard — and honestly, who would’ve expected this to be the memorable part — was IDE support, or the near-total lack of it. I’d been using RustRover for Rust and various JetBrains flavors for other languages, and Zig, by comparison, offered little beyond syntax highlighting and basic autocompletion. It wasn’t exactly surprising, but it did force me back to basics: learning to work with the language largely from the command line. What started as a drawback turned into one of the more interesting parts of the experience. It turns out I’d simply forgotten how straightforward it can be to rely on bare CLI tooling.

The first real lesson here was `build.zig`, which handles this with surprising ease. I eventually settled on this setup:

```shell
zig build test                                              # run all tests
zig build test -Dfilter="filter match function basic"       # run one test
zig build test -Ddebug-query=true                           # all tests with debug
zig build compliance                                        # compliance suite
zig build check                                             # unit tests + compliance

```

Once you accept the terms, it’s genuinely refreshing to work with.

I have Zig to thank, in a roundabout way, for kicking off a bigger chain reaction, namely my move away from a full IDE toward a helix + alacritty + zellij setup.

## Flat structure

With Rust, and most other languages, I’ve always spent a fair amount of time (going back and forth) trying to find the right balance between file size and folder depth. You’re free to fragment files and grow the folder hierarchy as deep as you like. Zig, it turned out, is fine with this too, but somehow doesn’t really encourage it (like C, which is no surprise for a low-level systems language). You can nest files and folders if you want, but doing so brings a bit of import friction, and the real question becomes: why bother? What do you actually gain in readability by splitting everything across more files and folders? In theory, better readability. In practice, when you collapse related things into one larger file, you can just slice it and navigate section by section instead and there’s a real benefit to having everything in one place. Mostly, Zig nudges you toward flat. If something needs a companion for a model, I just create a `model_ ` file next to it and move on.

I don’t think this scales to large projects, meaning at some point you need a real hierarchy but the threshold for needing one turned out to be much higher in Zig than I expected. In Rust, I tend to reach for folder structure early, almost by default. In Zig, I kept deferring it, and by the end of this project, I never needed it at all.

That contrast was useful beyond just Zig, because it made me reconsider, even in other languages, whether I’m organizing files because the project genuinely needs it, or out of habit. It’s also a pretty honest way to gauge how big a project actually is: if you can’t resist reaching for folders on day one,maybe it’s smaller than it feels.

Here’s the actual difference, side by side:

Rust (`src/`):

```shell
src/
├── lib.rs
├── parser.rs
├── parser/
│   ├── errors.rs
│   ├── macros.rs
│   ├── model.rs
│   ├── tests.rs
│   └── grammar/
│       └── json_path_9535.pest
├── query.rs
└── query/
    ├── atom.rs
    ├── comparable.rs
    ├── comparison.rs
    ├── filter.rs
    ├── jp_query.rs
    ├── queryable.rs
    ├── segment.rs
    ├── selector.rs
    ├── state.rs
    ├── test.rs
    └── test_function.rs

```

Zig (`src/`):

```shell
src/
├── root.zig
├── parser.zig
├── model.zig
├── model_query.zig
└── query.zig

```

## Tests

Setting the rfc9535 compliance suite aside for now and focusing purely on the language itself:

In Rust, I tend to stick with two approaches to testing:

- Inline unit tests, living in the same file or same folder as the code they cover. This is the convenient default always there, no extra setup.
- Integration tests, in an independent folder (like `tests`) outside the main source tree. This is the exception not the default, and sometimes absent altogether.

I expected roughly the same split from Zig. On paper, it looks similar: you can write tests directly inside the same file. The problem, at least for me, was verbosity. Given the flat structure I’d already settled into, I was left with two options, either a separate `model_test` file per model, or tests inlined directly into the model file itself. Both approaches ended up cluttering things: either the individual files or the main folder as a whole.

I went with the second option, which meant configuring it explicitly in `build.zig`. Once that was wired up, though, it worked well and stayed clean.

So overall: writing and managing tests feels easier to me in Rust. But in Zig’s case, much of that extra friction is language-specific, it comes down to Zig’s manual memory management rather than testing infrastructure itself.

## No functional paradigm

Rust is technically an imperative language, but it draws heavily on functional concepts: zero-cost iterators, lazy evaluation, ADTs, pattern matching, monadic types, traits, closures, and so on. Having also spent time with Haskell and Erlang, I’ve become fairly inclined toward the functional style, and it shows in this library. It leans heavily on FP idioms:

- Monadic error control via combinators like `Queryable` and related types
- Monadic-style data types like `Data ` with `map`, `flat_map`, `reduce`, and friends
- Pure, immutable transformations
- Combinators over iterators instead of loops
- Closures for local abstraction
- Declarative macros as a small embedded DSL
- Sum types and product types

I knew going in that I wouldn’t be able to bring all of this to Zig, but I hoped I could at least preserve the core concepts. In practice, where Rust leans on immutability and combinators, Zig pushed me toward in-place mutation and the pattern most native to the imperative world.

Where the two stay close: sum types.

Pure and direct in Rust:

```rust
pub trait Query {
    fn process<'a, T: Queryable>(&self, state: State<'a, T>) -> State<'a, T>;
}

impl Query for Segment {
    fn process<'a, T: Queryable>(&self, step: State<'a, T>) -> State<'a, T> {
        match self {
            Segment::Descendant(segment) => segment.process(step.flat_map(process_descendant)),
            Segment::Selector(selector) => selector.process(step),
            Segment::Selectors(selectors) => process_selectors(step, selectors),
        }
    }
}

```

Duck-typed in Zig:

```zig
pub fn query(node: anytype, iteration: *JsonPathIter) !void {
    const T = switch (@typeInfo(@TypeOf(node))) {
        .pointer => |p| p.child,
        else => @TypeOf(node),
    };
    if (!@hasDecl(T, "query")) {
        return; // no compile-time trait; just checks the method exists
    }
    try node.query(iteration);
}

```

Recursion holds up on both sides too.

```rust
fn process_descendant<T: Queryable>(data: Pointer<T>) -> Data<T> {
    if let Some(array) = data.inner.as_array() {
        Data::Ref(data.clone()).reduce(
            Data::new_refs(/* children */).flat_map(process_descendant)
        )
    } else { Data::Nothing }
}

```

Zig:

```zig
fn collectDescendants(allocator, value: *std.json.Value, path, out) !void {
    try out.append(allocator, .{ .json = value, .path = try allocator.dupe(u8, path) });
    switch (value.*) {
        .array => |arr| for (arr.items) |*elem| try collectDescendants(allocator, elem, child_path, out),
        else => {},
    }
}

```

But the language quickly forces you to diverge from the functional style, mostly because you’re now dealing with allocators directly, and a genuinely pure functional approach means constantly constructing new structures. That’s either expensive in memory or expensive in the manual bookkeeping needed to avoid it.

Mutation vs. immutable monad is the core difference.

Rust does a straightforward monadic transformation:

```rust
pub fn flat_map<F>(self, f: F) -> Data<'a, T> {
    match self {
        Data::Ref(data) => f(data),      // returns a *new* Data
        Data::Refs(v) => Data::Refs(v.into_iter().flat_map(...).collect()),
        _ => Data::Nothing,
    }
}

```

Zig switches to mutation:

```zig
pub fn queryName(name: []const u8, iteration: *q.JsonPathIter) !void {
    while (i < iteration.cursors.items.len) {
        if (obj.getPtr(name)) |val| {
            iteration.cursors.items[i] = .{ .json = val, .path = new_path }; // in-place overwrite
        } else iteration.remove(i);                                          // mutate list directly
    }
}

```

Reduce vs Fork.

```rust
selectors.iter().map(|s| s.process(step.clone())).reduce(State::reduce)

```

Zig:

```zig
var lhs_branch = try iter.fork();   // deep copy of cursor state
defer lhs_branch.deinit();          // then discarded

```

Combinators vs. loops.

```rust
items.iter().enumerate().filter(|(_, i)| cond(i)).map(|(idx, i)| Pointer::idx(i, path, idx)).collect()

```

Zig:

```zig
while (i < cursors.len) {
    if (actual_index < arr.items.len) { cursors[i] = .{...}; i += 1; }
    else iteration.remove(i);
}

```

All told, this reflects each language’s design goals and target domain, and it’s a reasonable trade-off but subjectively, I found the resulting Zig code less readable than its Rust counterpart.

## Allocators

Allocators are everywhere. Almost every function accepts one; every structure holds one. It’s explicit, and once you accept that as the cost of entry, it’s relatively straightforward to follow. This is more or less the language’s defining feature, so I can’t say I wasn’t warned.

In practice, though, the process is tedious. You have to meticulously follow the init/deinit convention, and that discipline gets shaky the moment your call stack grows long. It’s a clear improvement over a silent segfault or corrupted memory in C, but coming from Rust, you’re still the one enforcing the rule by hand: allocate something, handle the failure path, decide who’s responsible for deinit, every single time.

Fortunately, Zig’s `TestAllocator` comes to the rescue here. It won’t catch everything automatically, you still need to write the test cases that exercise the failure paths — but once you do, it’s fairly reliable. And that’s the trap: this all looks obvious on paper, right up until the code gets more complex, at which point these bugs tangle themselves up and hide.

Here are the cases that hit hardest, each compared against how Rust handles the same shape:

### Memory leak: forgotten deinit

```zig
var iter = q.JsonPathIter.init(&root, std.testing.allocator);
try iter.append(&root, "$['a']");
// BUG: no iter.deinit()

```

Caught by: `MemoryLeakDetected`, pointing at the `dupe` call inside `append`.

Fix: `defer iter.deinit();` right after init.

Rust: `Drop` runs automatically at scope end, so this specific bug simply doesn’t exist. Though technically, leaks are still possible in Rust like `Rc` reference cycles, or an explicit `Box::leak` so “never leaks” isn’t a hard guarantee, just something you’d have to go out of your way to trigger.

### Memory leak: deinit skipped on error path

```zig
fn build(json: *Value, a: Allocator) !q.JsonPathIter {
    var iter = q.JsonPathIter.init(json, a);
    try iter.append(json, "$['a']"); // ok
    try iter.append(json, "$['b']"); // fails -> iter leaked
    return iter;
}

```

Caught by: `FailingAllocator{ .fail_index = 1 }`, which forces the second append into `MemoryLeakDetected`.

Fix: `errdefer iter.deinit();` right after init.

Rust: truly eliminated. `Drop::drop` fires unconditionally on any scope exit, including early returns from `?`.

### Memory corruption: deinit called twice

```zig
fn runQuery(json: *Value, qstr: []const u8, a: Allocator) !q.JsonPathResult {
    var iter = q.JsonPathIter.init(json, a);
    errdefer iter.deinit();
    try q.query(qstr, &iter);
    return iter.toResult(parsed); // ownership moves to caller
}

fn cacheAndLog(json: *Value, qstr: []const u8, a: Allocator, cache: *std.ArrayList(q.JsonPathResult)) !void {
    var result = try runQuery(json, qstr, a);
    try cache.append(result);   // cache now holds a (shallow) copy of result's pointers
    defer result.deinit();      // BUG: frees the same heap data cache.items still points to
    printResults(&result);
}

fn processAll(json: *Value, queries: [][]const u8, a: Allocator) !void {
    var cache = std.ArrayList(q.JsonPathResult).init(a);
    defer {
        for (cache.items) |*r| r.deinit();  // frees the SAME memory Layer 2 already freed
        cache.deinit();
    }
    for (queries) |qs| try cacheAndLog(json, qs, a, &cache);
}

```

Caught by: running under `std.testing.allocator`, which fails on the second query’s `cache.items[0].deinit()` during `processAll`’s cleanup, `DoubleFree` pointing at both free sites, confirming this is a cross-function ownership bug, not a single-line typo.

Fix: only one layer may own the value. Since `cache` outlives `cacheAndLog`, ownership belongs to layer three; layer two must not `defer deinit` after handing it off:

```zig
fn cacheAndLog(json: *Value, qstr: []const u8, a: Allocator,
                cache: *std.ArrayList(q.JsonPathResult)) !void {
    var result = try runQuery(json, qstr, a);
    printResults(&result);      // use it first
    try cache.append(result);   // then hand off ownership — no defer after this
}

```

Rust: this exact shape can’t compile. `cache.push(result)` moves `result` — after that line, `result` no longer exists as a usable binding, so there’s no way to later call `drop(result)` by accident.

### Memory corruption: orphaned allocation when moving into a struct fails

```zig
pub fn appendBuggy(self: *Iter, v: *Value, path: []const u8) !void {
    const duped = try self.allocator.dupe(u8, path);
    // BUG: no errdefer
    try self.cursors.append(self.allocator, .{ .json = v, .path = duped });
}

```

Caught by: `FailingAllocator{ .fail_index = 1 }` failing the array’s growth (the second allocation), orphaning `duped` (the first allocation).

This leaks in a way distinct from case one: `iter.deinit()` runs fine, it just never sees this particular string.

```zig
const duped = try self.allocator.dupe(u8, path);
errdefer self.allocator.free(duped);   // only fires if append below fails
try self.cursors.append(self.allocator, .{ .json = v, .path = duped });

```

Rust: true by construction. `Vec::push(item)` moves `item` in and either succeeds or aborts on OOM and there’s no fallible push in the standard API that hands you back an “allocated but unlinked” value to accidentally lose. The gap that `errdefer` fills here simply doesn’t exist to begin with.

## Libraries and the core API

The ecosystem is still very young. There’s a real scarcity of libraries, and even something as basic as regex isn’t fully mature, for instance `mvzr`, the regex engine available in Zig, doesn’t support Unicode property escapes (`\p{...}`), which surfaced directly as a gap while implementing RFC 9535’s filter functions. On top of that, the language’s own standard library changes its API from version to version. None of this was surprising going in, but it’s worth noting for the record.

## Overall impression

The language is different from Rust (who could’ve thought that, yeah), but it left a genuinely good impression. It’s straightforward, modern, and blazingly fast. I believe it has real potential to become the true successor to C. On the other hand, it’s still young, and it shows: the shape of the language itself feels unfinished in places, and I suspect it’ll pick up more of the cooler quality-of-life features and syntax sugar as it matures.

As for me, I’d like to keep contributing to the ecosystem, and I will, whenever I come across a project worth building.

# Human brain is two separate organs, Stanford Medicine-led research finds

## 评论（165/165）

**gigatexal** · 2026-09-19T14:24:58.000Z：

“ The language is different from Rust (who could’ve thought that, yeah), but it left a genuinely good impression. It’s straightforward, modern, and blazingly fast. I believe it has real potential to become the true successor to C. On the other hand, it’s still young, and it shows: the shape of the language itself feels unfinished in places, and I suspect it’ll pick up more of the cooler quality-of-life features and syntax sugar as it matures.As for me, I’d like to keep contributing to the ecosystem, and I will, whenever I come across a project worth building.”Idk I don’t write either well enough to have a hand in this but losing out all of this for more
Imperative stuff seems like a step back.“ No functional paradigmRust is technically an imperative language, but it draws heavily on functional concepts: zero-cost iterators, lazy evaluation, ADTs, pattern matching, monadic types, traits, closures, and so on. Having also spent time with Haskell and Erlang, I’ve become fairly inclined toward the functional style, and it shows in this library. It leans heavily on FP idioms:Monadic error control via combinators like Queryable and related types
Monadic-style data types like Data<T> with map, flat_map, reduce, and friends
Pure, immutable transformations
Combinators over iterators instead of loops
Closures for local abstraction
Declarative macros as a small embedded DSL
Sum types and product types”

**diek** · 2026-09-19T14:37:20.000Z：

> One caveat worth stating up front> Here’s the actual difference, side by sideI realize the author put a disclaimer at the bottom that they used AI for styling, but having to wade through this stuff at work all day my brain now actively rejects Claude-isms in prose.

**bbg2401** · 2026-09-19T14:39:48.000Z：

I don’t see the point of letting an LLM generate an article when the topic is your personal, subjective experience which only you, a human, would be able to express.

**spider-mario** · 2026-09-19T14:42:08.000Z：

> The first thing that caught me off guard — and honestly, who would’ve expected this to be the memorable part — was IDE support, or the near-total lack of it.I would have completely expected that.

**tialaramex** · 2026-09-19T14:50:21.000Z：

I think when we're looking back on the 2020s we'll be struck by the Allocator obsessionAll of the Handmade "C successor" languages seem to have this obsession, including not only Zig but Odin, C3 and Jai.For some toy problems you can do clever allocator tricks and get a huge perf win. For example Jai and Odin both seem to really want you to write code which can throw away a "per-frame" arena periodically so they're not paying to track allocations in the arena because they're all thrown away at the same time.But a lot of real world software just isn't that simple. This doesn't make such features worthless, it just means they're one of a thousand tools the experienced developer could want in their toolkit, not really deserving headline status.

**karmakurtisaani** · 2026-09-19T14:56:27.000Z：

Off topic, but I remember fondly the pre-LLM days when I used to love reading about programming languages. I never got a chance to professionally work with Rust, but made some cool hobby projects with it. Would have eventually tried out zig too.Now it all feels so pointless though. Like memorizing rules to do mental arithmetic. Sure, there is still use for language expertise, but not enough to get excited over new concepts and ideas.

**ozgrakkurt** · 2026-09-19T14:56:57.000Z：

Would recommend learning how to use arena allocation. You would have patterns like:fn run_query(alloc) { arena = init_arena(alloc);

 defer arena.deinit();

}

**weinzierl** · 2026-09-19T15:11:49.000Z：

Two additional points:1. Tooling (as an extension to the mentioned IDE support point). Zig and Rust are both praised for their tooling and I think rightfully so. The C/C++ interop story and the cross-compiling story in Zig are great. From the standpoint of a working practitioner though I think Rust is way ahead. Not surprising given that Zig is much younger, but something to keep in mind.2. Compile Time Stuff: Here Zig is praised and Rust not so much. I think this is undeserved. Rust has much higher aspirations for their compile time features, namely that outcome must be identical regardless when the code runs. This is a very useful property but makes the task much harder and fundamentally incomparable with Zig comptime.

**truth_seeker** · 2026-09-19T15:15:25.000Z：

Detailed in depth look at Zig Vs Rust (also ... Vs Go)https://gist.github.com/corporatepiyush/5382d79192be9737cf3b...

**hn_submit** · 2026-09-19T15:26:45.000Z：

There will never be a true successor to C since C is "high level assembly." The lack of pointer checking, unsafe casts and non-existent bounds checking aren't an oversight but by design! Assembly doesn't have them so neither does C! There's no reason to whine about it.The real problem is that people are using C for the wrong reasons. C is for the development of operating systems and low-level code, not applications.Zig is more modern but anything that does even one iota more of hand-holding or has anything that looks like a guardrail fails the test.If you want to write applications use Pascal, Java, C#, Swift or Go.

**Syzygies** · 2026-09-19T15:32:51.000Z：

For various purposes I work on a language comparison project that includes C and candidate successors such as Go, Zig. One question is the language to use for an archival port of a 1980's computer algebra system written in 32-bit K&R C. While Zig is a great debugging compiler, it's not yet stable enough to be the best target language for archival purposes.https://github.com/Syzygies/CompareSo you're in a restaurant where you don't speak the language, you can't read the menu, but you see three price points for set meals featuring the house specialty. (Say, "Crossing the Bridge" noodles in Yunnan.) Which do you choose? My tour guide, the author Fuchsia Dunlop, later agreed with me this is obvious: The middle choice.So you're choosing between Go and C23 as candidate successors to K&R C. They both have "royal blood". One got the name. Knowing nothing more, which do you choose?The answer is equally obvious. The one that got the name also got the warts.

**csense** · 2026-09-19T15:43:23.000Z：

One of the section headings says "Mutation vs. immutable monad is the core difference" but this is not true.The code in that section is clear in its purpose and broad outline: "Give me a function and data; if the data is bare apply the function to it; if the data is a container apply the function to each item inside it."You can absolutely do that with immutable data structures in Zig. You just have to pass an allocator to the function (i.e. instead of calling data.flat_map(f), you call data.flat_map(a, f) where a is your allocator).That the Zig version of the code does mutation is a matter of programmer choice, not something imposed by the language.(Also, what do monads have to do with it?)

**plqbfbv** · 2026-09-19T15:48:31.000Z：

Maybe I'm not that deep into programming, but I don't understand the hype about Zig?I programmed in rust a bit and can't say I'm an expert, but in my view rust mostly-solved the memory management problem at compile time and without a GC, and it works very well. The biggest con and cost I've always seen repeated so far is that "it's slow to compile", and I get that, if you're past 250 crates the final --release link tends to become noticeable, but there were improvements to incremental compilation.On the other hand - looking at the syntax from this post - Zig feels a blend of javascript, python and golang syntax that still requires memory management. So a nicer-written C that inherits all the issues from C? From the post: no functional programming, data mutation, memory leak, double-free, memory corruption.Personally I'd rather trade a couple minutes of final link every time when this is the other option.

**gslepak** · 2026-09-19T17:37:22.000Z：

I'm honestly baffled why people are writing Zig or Rust and avoiding V. V (and now Bend) seems like the future to me.

**AlienRobot** · 2026-09-19T17:42:24.000Z：

In the example of Rust: items.iter().enumerate().filter(|(_, i)| cond(i)).map(|(idx, i)| Pointer::idx(i, path, idx)).collect()

vs. Zig: while (i < cursors.len) {
 if (actual_index < arr.items.len) { cursors[i] = .{...}; i += 1; }
 else iteration.remove(i);
 }

I think you have to be a special kind of person to call Rust "more readable."The thing about Rust is that if you can appreciate zero-cost abstractions on iterators then the language feels like the only right way to program. But many programmers either don't use this sort of programming at all, or don't care if it has a cost in languages like JS, Python, Java, etc.Personally I like Zig a lot because it feels like you're doing low-level programming but without having to program C which is... well, https://xkcd.com/918/

**myko** · 2026-09-19T17:53:17.000Z：

> One caveat worth stating up frontIt would be nice if people would note that their posts are AI generated, and put that in the title here to make it easier to ignore

**jauco** · 2026-09-19T19:19:04.000Z：

Given that the author mentions both using helix and zig encouraging larger files with more content I’d be curious to know how they navigate these files in helix. The thing that keeps me from using it is lack of code folding, which I notice I use a lot when navigating larger files to zoom out.

**elendilm** · 2026-09-19T19:33:21.000Z：

> It turns out I’d simply forgotten how straightforward it can be to rely on bare CLI tooling.Happy for you.CLI tooling counter intuitively makes for very less friction especially when you are moving very fast.

**api** · 2026-09-19T14:30:10.000Z：

I would say Rust is a functional language that has been hammered into the shape of C++. It also draws heavily on ML.I get why, and it makes it a better fit for its obvious “C++ reimagined, cleaner, and better” niche.

**pjmlp** · 2026-09-19T14:36:01.000Z：

Modern and blazing fast, what we lost leaving behind languages like Modula-2 and Object Pascal, having newer generations to think C and C++ were the only compiled languages alternatives to scripting languages.

**cosmic_cheese** · 2026-09-19T14:44:35.000Z：

I’m more than a bit out of my depth discussing the topic, but I’m not sure than imperative-dominant languages will ever really go away or that functional-dominant languages will ever become as popular as C and C++. Ugly as they may be, imperative languages seem to be grokked by humans more readily and are more often than not “good enough” for the most part so it’s difficult to see them losing substantial momentum.

**metaltyphoon** · 2026-09-19T14:41:09.000Z：

So anything that has em dashes is now considered LLM generated? What made you think this is generated?

**ivanjermakov** · 2026-09-19T17:08:13.000Z：

"Having a blog is cool these days"

**pton_xd** · 2026-09-19T15:05:41.000Z：

AAA games use allocators extensively, and they are more complex pieces of software with higher performance requirements than nearly anything else out there. So I'm not sure what toy problems you're talking about.Allocators have been in wide use long before the 2020s but I agree there does seem to be a resurgent interest lately. Although I would argue it's part of a more broad trend of focusing data driven design. Which makes sense because accessing main memory is one of the slowest things your program can do.

**convolvatron** · 2026-09-19T16:13:59.000Z：

actually large programs that are persistent is where you really care. kernels and databases often use explicit allocators because there is so much policy wrapped up in allocation.this goes back decades, its not just a feature of the 2020s. as a systems programmer I always want this, and the idea that allocator state should be completely hidden and implicit is shortsighted.but yes, it is a bit onerous to pass around allocator(s). the real complaint that I have is that if 'malloc' is global and a compiler primitive, then we can do things like coalesce allocations and have compiler managed lifetimes when appropriate.explicit allocators are an important lever, its not clear to me that we could never find a way to make them possible without the minor downsides.

**slopinthebag** · 2026-09-19T16:18:24.000Z：

yes i've noticed this as well. they all stem from a heterodoxical corner of the programming community who are obsessed about performance. this isn't a bad thing, considering how slow modern software is! but this group believes performance is a memory issue, which is true for some software but not all. i think these languages can be really useful for realtime applications like gaming where allocation has a real cost, but the so-called "pointer jungles" are probably not the reason why microsoft teams takes a trillion cpu instructions to boot.

**jcranmer** · 2026-09-19T16:18:32.000Z：

I'd word it slightly differently, as something like the Allocator Effect System obsession. It's not so much that allocator tricks don't have a role in modern software--all of the large applications I've worked on rely on things like arena allocation at least some of the time--but rather that things like making container types generic over allocators seems to be more trouble than it's worth. I've never seen anyone use anything other than the default allocator for STL types, for example.

**boomlinde** · 2026-09-19T16:33:53.000Z：

> But a lot of real world software just isn't that simple.Zig doesn't force or even tends to prefer one way or another. If I want unassuming heap allocations that can be reclaimed in any order, there's an allocator for that. If I want an arena to discard at the end of something like a request or a video frame, there's an allocator for that. If I want to use a fixed backing buffer for the allocations, there's an allocator for that.The point is that the standard library doesn't assume one or the other, which seems good if the problem is that "real world software just isn't that simple" in the more general sense that there's no one-size-fits-all allocation strategy.

**jmull** · 2026-09-19T18:02:03.000Z：

Allocation happens. You can leave it to the compiler, the runtime, or let the code control it.The automatic solutions are usually pretty good and usually the right place to start. But if performance is a priority, you want options.BTW, “per-frame arena” is part of a general pattern of a repeated interval of work doing significant allocation. This is really common in software of all kinds… servers that process requests (like web servers and database servers) and typical command line tools.

**philippta** · 2026-09-19T18:05:27.000Z：

> For example Jai and Odin both seem to really want you to write code which can throw away a "per-frame" arena periodicallyYou can generalize this far beyond per-frame semantics. Think per-http-request, per-pubsub-message.Per each, you can create a new virtual.Arena, set it as your context.temp_allocator and use it for the entirety of the request or message. Afterwards, throw it away.

**pixelesque** · 2026-09-19T18:33:29.000Z：

Some of this surely stems from Rust not originally supporting allocators at the standard API level until later. You can manually create your own, and create/modify your own containers, but until GlobalAlloc came around it sometimes involved doing things like passing through Arc<Allocator> through to things if you wanted multiple things to use a single one.Sometimes using a global one isn't the best thing (it's often a good idea to specialise base on allocation size, reuse and lifetimes), but I've used them quite a bit in C++ over the past 16 years doing HPC for graphics, rendering and simulation, so calling them only useful for "toy problems" likely shows you just haven't found a need for them in what you've been doing.

**sortoflog** · 2026-09-19T18:40:27.000Z：

I’m not so sure the usefulness of custom allocators really relates to the complexity of the problem. Take the scratch arena example: ifaik it’s just free performance (& simplicity) whenever you need dynamic allocations with lifetimes that begin and end on a critical path. Presumably this is why Jai/Odin focus on this situation so much since it applies to per-frame stuff in videogames, but generally I’d expect this to come up more often in nontrivial problems.

**ratorx** · 2026-09-19T14:59:48.000Z：

I think (for now), it is still relevant. A language is an abstraction, and a good abstraction, like a good LLM harness, can be quite valuable.Let’s say I’m writing some concurrent code with an LLM. I’d probably feel much safer having it write Rust, rather than C. So even in a post-LLM world, languages will continue to evolve as long as abstractions can be improved.

**echelon** · 2026-09-19T15:02:03.000Z：

I used Rust extensively pre-LLM, and I'm much happier to serialize my thoughts to Rust than any other language.I prefer to prototype in Golang since it compiles fast and makes for quick iteration, but at the end I ask the LLM to port the Golang to Rust.Nice Rust enums for APIs are the chef's kiss.I absolutely will not write anything in Python or scripting languages anymore. They're too brittle and don't have great devex or deployment stories. Especially when you can just as easily build in a typesafe language with good error handling that compiles down to a single static binary.

**eddythompson80** · 2026-09-19T15:14:03.000Z：

I was thinking about that too recently. We have a new service that we’re trying to publish an SDK for. I don’t like the SDK that was created and kept nitpicking about how verbose certain things are and how “unergonomic” it feels (long tedious type names, annoying redundant constructs, etc) But then I was wondering if for a brand new service/SDK if anyone cares anymore and how much fuss i should be making about that.

**alembic_fumes** · 2026-09-19T15:25:47.000Z：

I relate to this.For years I used Rust as my hobby-programming language and loved it greatly. I never managed to land a job working with it full-time, because either the work was too niche or it didn't pay enough, or I was simply too comfortable where I was to change. And now that I finally have enough discretion over my technology choices to run a "proper" project using whatever tools and languages I want, it is not me but the AI that writes all of the code.There's a part of me that feels a quite sad about all this. It's almost as if there actually all along existed a real final deadline on finding that "dream job". And I missed it. And while I expect this one miss to be just a small piece in the grand picture of things that we're going to lose or have already lost to the zeitgeist of agentic SWE, it feels big to me. It was my professional dream, while I still had professional dreams.

**rgoulter** · 2026-09-19T15:27:32.000Z：

> Sure, there is still use for language expertise, but not enough to get excited over new concepts and ideas.Programming and learning new things can still be fun in the era of agentic coding.With LLMs, I get to quicky ask: what would this look like? Why do it that way? If you suspect that the LLM isn't doing it the right way, you can still investigate that yourself.e.g. the other day, https://rhombus-lang.org/ was mentioned on HN. With LLMs, the cost for trying this out is practically much lower.

**wannabe44** · 2026-09-19T15:30:28.000Z：

> Sure, there is still use for language expertise, but not enough to get excited over new concepts and ideas.In 5-10 years, the people who have paid attention to these will be needed to bail us out of the mess that the rest of the slop-addled monke brains have created.

**layer8** · 2026-09-19T16:08:42.000Z：

> I remember fondly the pre-LLM days when I used to love reading about programming languages.First I thought you were going to comment about the grating LLM-isms in the article, which made me end up not enjoying reading it.

**bigstrat2003** · 2026-09-19T17:47:31.000Z：

It isn't like LLMs are actually good at programming, so there's no reason to give up on your interest in it. The hype around LLMs is not sustainable, the quality simply is not there.

**simonask** · 2026-09-19T15:36:22.000Z：

Step zero of using arena allocation is to build realistic benchmarks so you can measure if it's worth the trouble in the first place. Standard allocators are incredibly good these days, and even plugging in mimalloc or jemalloc will be much less work, and much less error prone.

**LoganDark** · 2026-09-19T15:13:43.000Z：

Zig comptime feels easier and more effective in practice. I've had some fun const evaluating some stuff in Rust, but I needed to use a bunch of annoying imperative hacks because so much of the functional stuff wasn't supported in const context back then. It's probably a bit better these days.For one of my crates I needed to have a build script make a bunch of lookup tables as separate files for me to `include_bytes!` because at the time I couldn't generate a bunch of floating point conversions in const.

**chaz72** · 2026-09-19T15:14:49.000Z：

Are you saying that you think that Zig does not produce identical outcomes for comptime code regardless of when the code runs? What do you mean?

**monocasa** · 2026-09-19T15:52:53.000Z：

Except Rust is actively being used in kernel space and low level embedded systems as well.

**PaulDavisThe1st** · 2026-09-19T16:33:13.000Z：

Is a digital audio workstation or a "AAA" game, with their timing constraints, unbounded computational loads and general demanding performance requirements closer to "an application" or "operating systems and low level code" ?

**slopinthebag** · 2026-09-19T16:38:36.000Z：

i dunno, people are using rust effectively to build applications too. and apple has started using swift in the kernal.i do agree that applications are probably best built in fast garbage collected language. but it also seems like go, java, C#, etc have other downsides that push people towards things like zig or rust even for apps. it also depends on what you mean by "apps". is a server an app? what about an actual native cross-platform desktop application? does go, c#, or java have a good paradigm for that? what if you want to use an oss language not tied to a big tech company? you start running out of suitable languages pretty dang fast.you could name any application type and i could probably give you reasons why you might want to build it in a "systems" language instead of a high level one.

**pjmlp** · 2026-09-19T16:11:19.000Z：

Despite my usual rants, naturally C23.Minimal rewrite due to the breaking changes introduced in C23 versus K&R C, while the others are a complete rewrite.Even if the syntax is a bit of a kludge there are now ways to indicate bounds on function arguments.

**d0mine** · 2026-09-19T16:16:32.000Z：

Middle may be wrong (it is a marketing trick to add 3rd outragesly expensive option, to make 2nd option look reasonable). The correct answer is “it depends” (even how long you should spend on choosing may depend on context too).For example, write in whatever language you know best, then translate to a more appropriate language using LLMs once the desired behavior can be checked automatically. It is a tactic that works in some cases.

**bunderbunder** · 2026-09-19T15:57:42.000Z：

Further up he discusses that using a functional paradigm is possible, but concludes that it doesn’t feel like a practical choice because of how Zig does memory management:> But the language quickly forces you to diverge from the functional style, mostly because you’re now dealing with allocators directly, and a genuinely pure functional approach means constantly constructing new structures. That’s either expensive in memory or expensive in the manual bookkeeping needed to avoid it.So I don’t think he’s trying to say that it’s literally impossible. It felt more like the result of a good faith attempt to understand how Zig itself actually wants to be used, and to compare that to how he’s used to using Rust.I actually liked that he did it. So many other comparisons want to evaluate one language against the other language’s values. But I don’t want to know how well Zig can do Rust; I want to know how well Zig accomplishes its own goals, and what those goals are.

**kccqzy** · 2026-09-19T15:59:28.000Z：

Monads are where flat_map came from. A monadic programming style is where flat_map is used pervasively eschewing other APIs.

**slopinthebag** · 2026-09-19T16:03:21.000Z：

yeah to me zig exists as a counter-reaction to rust. which means avoiding both the good and bad things rust does. and rust does a lot of things right, so...

**pjmlp** · 2026-09-19T16:04:57.000Z：

Basically you pick the type safety that Modula-2 or Mesa already offered in the late 1970's, repackage it with comptime and more C like syntax, and have a whole legion of new devs jumping into it.Note that AT&T, where UNIX and C were born, the language they were researching as C replacement was Cyclone, not something that is not much different.

**bunderbunder** · 2026-09-19T16:18:04.000Z：

Zig is aiming to be lower level than Rust. As the project homepage prominently advertises, it has no hidden memory allocation or control flow. It also gives more control over how memory is allocated, which is potentially useful in applications with particularly tight performance requirements.Kelley first created Zig when hr was working on a digital audio workstation and found most existing languages to be awkward for working with particularly hard real time requirements, but still wanted something more modern than C. Im speculating here, but I believe its advantage over Rust for that specific application is that you have tighter control over exactly when memory is allocated and deallocated, and how data is laid out in it. Rust wants to tie allocation lifetimes to scope in a very fine grained way that I would guess is beneficial the vast majority of the time, but does still make it harder to reason about when you’re about to stall out the CPU while the allocator does its thing.

**hinkley** · 2026-09-19T16:31:53.000Z：

Rust could not work in a world where compilation was a single threaded affair. I think it exists now instead of in the 90’s and 00’s in good part because of this.I don’t think it’s an accident that it has succeeded as multicore took over. We are now well past a point that a task that can be split with 70% efficiency into multiple parallel tasks is 5-10x faster than the optimal sequential solution. Expensive multicore machines existed when Rust was a baby but it didn’t really catch on until 4 core was common in consumer hardware. And now I have an ancient laptop with 16 cores.But Rust is also good for producing correct code to run on those systems. So it benefits twice.

**kllrnohj** · 2026-09-19T16:34:31.000Z：

Zig is exciting to people that still actually like C. Is that a rationale choice? Not very often. Is it a wrong choice? Also again not very often. At least, not for anything in scope of a solo dev.The industry where it seems strongest positioned is embedded. Will it actually break into that domain? No idea.

**pron** · 2026-09-19T16:42:56.000Z：

> I don't understand the hype about Zig?As a long-time low-level programmer, and as someone working on a popular mainstream language, I find Zig fascinating, and I also think it addresses a long-standing problem in low-level programming. I'll get to the problem later, but the fascinating part is its use of partial evaluation (comptime) as a single coherent mechanism that replaces a myriad of other partial-evaluation mechanisms (macros, templates/generics, constexprs). That one mechanism is the core of the language, like macros are in lisps, and that design - whether you like it or not - is revolutionary. It's never been done before (other languages have partial evaluation mechanisms that are almost as general, but they're offered in addition to, not as a replacement of, other features).> rust mostly-solved the memory management problem at compile time and without a GC"Mostly" does a lot of work here because 1., if you look at the implementation of very efficient, possibly specialised data structures - the very thing you reach for a low-level language for - they typically require unsafe, and 2., it still suffers from the problem C++ has had for decades, which is that over time, as program changes and evolves over years, things tend to drift toward the more general mechanisms that rely on malloc/free on an individual objects, and the program gets slower and slower (huge runtimes like TCMalloc help, but not enough, because they can't move pointers). This problem, of programs that start out fast, but after five or ten years of evolution need to spend a lot of effort to remain fast, is one of the things moving collectors were designed to solve, but they require moving pointers, which doesn't work in low-level languages that are not meant to have an FFI layer between them and the hardware.To compete with the performance of moving GCs, which allocate through bumping a pointer, like on the stack, and free memory in bulk, low-level languages need to rely on arenas (which work based on a similar principle), and Zig is the first language that makes arenas almost user-friendly and hopefully sufficiently composable to withstand program evolution. Of course, time will tell how well this works in practice.

**logicchains** · 2026-09-19T17:20:24.000Z：

If you're writing ultra low latency code you basically want everything allocated from an arena, with different arenas for different kinds of objects. Zig comes with this built in, while Rust makes it extremely unergonomic to do safely (due to the lifetime system).

**qudat** · 2026-09-19T17:34:59.000Z：

As someone who primarily writes in TS, Go, Python, I agree with your assessment: it looks like those languages. The reason I like Go is the reason I like Zig: the language is relatively simple and feels like C.The C interop is a huge win as someone who wants to do more posix/wayland projects.

**applfanboysbgon** · 2026-09-19T18:03:25.000Z：

> So a nicer-written C that inherits all the issues from C?And inherits all of the benefits of C. C is the foundation of the computing world. "C, but not built 50 years ago" is, by itself, a tremendous value add to a programming ecosystem that has largely abandoned attempts to write a truly performant language in favor of handicapping programmers with fully automated safety.Rust is a low-level language for people who don't write low-level code. Zig is for those who do.

**myko** · 2026-09-19T17:54:22.000Z：

I haven't heard of those, but I've used Zig and Rust for some projectsWhat's the pitch?

**altairprime** · 2026-09-19T18:56:05.000Z：

Such bafflement is often a medium-strength signal of the Bystander Effect. If someone wrote and submitted to HN your own blog post comparing the Zig/Rust examples from this article to ones from V, I’d read it in its entirety knowing nothing whatsoever about V. Perhaps it will be written by you!

**Hugsbox** · 2026-09-19T18:03:15.000Z：

I'm not exactly sure what you mean, that seems like a pretty phrase to me, is it considered an LLMism now? Kinda feels like the same thing with the em-dashes; I can't use em anymore because people will then assume I'm an LLM, even though just a few years ago it was a perfectly normal thing to do.It's entirely possible I'm just getting worse and worse at picking out LLM writing these days too, who knows.

**touisteur** · 2026-09-19T14:50:00.000Z：

I miss the years of writing CLI tools, web servers and clients, in Ada (and of course, real-time complex distributed system...). Felt so simple and right and fast and robust. The code is still readable today and maintaining it is a zero effort today. Clean Java without the enterprise BS was a close second in ease of programming - boilerplate be damned.I'm glad NVIDIA found a way to make GPUs programmable and got us out of the shaders tarpit, but did it have to be C++...

**jstimpfle** · 2026-09-19T15:01:25.000Z：

You repeating this weird strawman take a million times doesn't make it true. Why don't you finally just put out some genuinely interesting projects demonstrating how everybody was doing it wrong, so people can make up their own mind and finally be convinced. There must be some true magic in those languages and platforms you mention, that should offset the pain of writing in upper case and with super long KEYWORDs everywhere, and to offset the cost of switching to a culture that has way less mindshare and way less of a software ecosystem around it.FWIW I've actually worked for 6 months on a large old Delphi project. It was some performance work that, as almost always, mainly required getting the language crap out of the way. In the end I got the job done (100x-1000x speedup) but I wouldn't want to switch back to this ecosystem: Licensing costs, weird language warts there too. A slow moving ecosystem. Ultimately, I just need something that does what I tell it to do, reliably and fast, and that doesn't get in the way.

**pyrolistical** · 2026-09-19T14:54:15.000Z：

Until there is a machine that is natively functional, there is always going to an incentive to go lower level for more performance.Even hardware (GPUs) that functional language could trivially exploit, it’s still higher performance to write low level code and manages all the memory imperatively

**abound** · 2026-09-19T14:47:02.000Z：

Not OP, but I think the leading and trailing paragraphs were mostly human-written (and nice to read), but the memory leak example cases had a very different flavor of prose and code comments that smelled very Claude-y to me

**brilee** · 2026-09-19T14:49:54.000Z：

"It's young, and it shows""Holds up""not a toy, but not a sprawling project either, and ideally..""And that’s the trap"ctrl F "real" -> 6 usagesctrl F "genuine" -> 4 usages

**sampullman** · 2026-09-19T14:50:49.000Z：

It's unfortunate, but to come across as genuine now I think you have to actively avoid AI-isms.In this case it feels AI generated with human polish, or vice versa. A couple tells are "One caveat worth stating up front..." and of course, "...the shape of the language itself...".

**applfanboysbgon** · 2026-09-19T14:55:28.000Z：

> So anything that has em dashes is now considered LLM generated?Is that what they said? If that's not what they said, why are you putting words in their mouth in an attempt to weaken their statement into some completely ridiculous stupid strawman that is obviously not actually what they said?

**greenhat76** · 2026-09-19T14:55:46.000Z：

"And honestly"

**Svip** · 2026-09-19T14:59:47.000Z：

It kind of says so at the bottom:> Disclaimer: styling and error handling throughout this article were cleaned up with the help of AI.The implication seems to be "light editing", but the LLM styling really comes through, so I guess that tracks.

**kllrnohj** · 2026-09-19T15:10:58.000Z：

And those games do so in a language (C++) where allocators is not a headline feature, and is barely even supported at all in the standard library.The important part is a language where the standard library isn't special, and Rust has this property, too. So in domains where things like per-frame allocators are useful, you can still have them. That capability just isn't cluttering up the more common path where that isn't useful.

**simonask** · 2026-09-19T15:33:18.000Z：

> AAA games use allocators extensivelyThey do, but not necessarily together with generic, standard containers.When you find yourself wanting a nonstandard allocator, you usually want it because you want it to have some interesting property. It's not necessarily trivial to fit that into the interface of something like `std::vector`, or `std::unordered_map`, etc.Here's my take as a game developer: 99% of use cases for custom allocators are scratch allocators for doing stuff within a frame. 95% of those are much easier to serve by just amortizing allocations by storing things in an `std::vector` (or equivalent) that gets cleared every frame. You can use linear storage to back many interesting data structures, including queues, ring buffers, priority queues, binary heaps, etc., and that's more than enough for a large number of systems in a game.The overwhelming majority of the time, more complex data structures (like hash maps etc.) have a longer lifetime than the current frame, because the whole point of using them in the first place is to amortize lookup time across frames.

**NetMageSCW** · 2026-09-19T19:36:04.000Z：

Making allocators part of a type or scope instead of in every function call might be a start.

**NetMageSCW** · 2026-09-19T19:33:53.000Z：

But for how many software domains are allocators more specialized than a single built-in general purpose one so important it should be the focus of your language?

**bunderbunder** · 2026-09-19T18:47:40.000Z：

Way back in the aughties I saw an interesting analysis (on a now defunct blog) indicating that under typical usage C# implementations tend to outperform C++ implementations in long-running business applications. The supposed reason was that C#’s compacting GC keeps the cost of new allocations fairly constant. By contrast, in C++ under typical use every new allocation requires probing for a sufficiently large block of free memory in an increasingly fragmented heap.I haven’t tried to replicate this for myself. And, even assuming for the sake of argument that it was definitely true back then, a lot can happen in 20 years. But still, it does speak to wanting options when performance really is critical.

**karmakurtisaani** · 2026-09-19T15:02:49.000Z：

But do you still have enthusiasm for finding out about new language features or concepts? I'll do what it takes to get the job done, but the passion for it is totally gone.

**karmakurtisaani** · 2026-09-19T15:07:14.000Z：

Yep, my point tho is more sentimental than technical. Let the LLM figure out the language details and just manage the output and deployment. It's ... not fun

**boredatoms** · 2026-09-19T15:16:09.000Z：

It still boggles my mind that golang hasnt introduced rust-style enums

**karmakurtisaani** · 2026-09-19T15:19:14.000Z：

Exactly, hard to see why any of this matters anymore.

**skhameneh** · 2026-09-19T16:56:20.000Z：

This is a bit nuanced, because if there’s redundant constructs then that does impact maintainability and efficiency with both runtime and LLMs working with the code.I’d push this more towards personal preference of how code is expressed matters much less now than how maintainable it is.There is the aspect of long type names, they often don’t have much impact when tokenized. The character count of words is nearly negligible - they often become one or two tokens anyways. But, the choice of words may have a greater impact on how the word choice weights an LLMs contextual processing of that word (a human may be able to ignore an inaccuracy in naming a bit more flexibly than some LLMs).

**karmakurtisaani** · 2026-09-19T17:02:05.000Z：

Yeah, this is exactly it. Not earth-shattering, but personally depressing. My solution has been to start a career switch.

**karmakurtisaani** · 2026-09-19T15:52:53.000Z：

Yep, learning new things is amazing now. Just today I went through some really crappy slides, just dropped them to gemini and asked for elaboration. It saved me hours of figuring the shit out the old fashioned way.

**karmakurtisaani** · 2026-09-19T17:41:33.000Z：

I'm skeptical, most human written code was and still is garbage and survives without major rewrites.

**slopinthebag** · 2026-09-19T16:55:14.000Z：

i think the reason is more that arena's let you manage lifetimes in groups instead of pointer chasing. if you have to manually manage memory, it's eaiser to manage a small number of arena objects instead of a large number of individual objects.eg https://www.dgtlgrove.com/p/untangling-lifetimes-the-arena-a...that being said, it's even easier to not manage any lifetimes at all :)although i suppose some will say that you still manage lifetimes in rust, you just have full support from the compiler to make sure you do it right. that seems better to me than relying on simplification to ensure you don't make mistakes.

**boomlinde** · 2026-09-19T17:20:41.000Z：

I don't know about more error prone. Benchmarks completely aside, freeing a batch of stuff you've allocated in a single place makes it easier to manage memory. I think it should be preferred wherever it's an option for that reason most of all. The "killer app" is something like an arena allocator that lives for the duration of an HTTP request.

**ozgrakkurt** · 2026-09-19T18:30:57.000Z：

I meant to suggest using arena allocation for everything and not even using a malloc style allocator. Just getting memory via memmap at program start and then using arenas for everything after that.It makes it much easier to avoid lifetime mistakes in my experience.Using arena allocation also makes me think more about how much memory I am using and how much memory I should be using etc.It is hard to benchmark it against just using a global allocator because it is a structural change to the whole codebase.

**vlovich123** · 2026-09-19T15:29:00.000Z：

There’s a few comptime crates out there. Crabtime is iirc the most mature and popular

**tialaramex** · 2026-09-19T15:46:44.000Z：

Certainly every new Rust release tends to have either new things which were stabilized as const on day one, or things which already existed but now have stable const.The biggest constraint today on Rust's constant evaluation compared to where you'd expect is that trait implementations can't ever be constant, this obviously means you can't call SomeTrait::function in your constant, even if you can see the implementation of SomeTrait::function and if it were not a trait it'd obviously be constant -- but it also means sugar like Rust's for loop, which de-sugars into trait invocations, can never be constant today.I think we can expect that to get fixed in the relatively near future, but I'd have said that last year too so what do I know.If you have C++ experience you'd probably want a lot more. C++ is allowed to allocate inside constant evaluation, and I believe in C++ 26 it's now even allowed to persist the allocation to runtime rather than being required to always clean up during compilation, so that's a much bigger set of crazy things you can do at compile time.

**bruckie** · 2026-09-19T15:20:26.000Z：

I assumed that it meant that if you ran code at compile time or at runtime, the results should be exactly the same given the same inputs.

**weinzierl** · 2026-09-19T15:55:35.000Z：

Yes. For example in Rust it took a long time for floating point operations to be available at compile time and even now only a subset is. The reason is that a lot of energy and thought went into the issue of producing identical output (and what identical precisely means ) even when compilation is on a different processor than where the target runs.As far as I know this is not a concern for Zig comptime.

**hn_submit** · 2026-09-19T16:19:34.000Z：

It's useful, but systems programming languages shouldn't be used to create applications in the first place.We're trying to solve a problem that shouldn't be solved. We're continuing and even confirming the usage of systems programming languages for application development.

**IncreasePosts** · 2026-09-19T16:25:53.000Z：

Rust is for devs who think "if only c++ had a few more features, it would be perfect". Zig is for devs who think "if only C had fewer features, it would be perfect"

**packetlost** · 2026-09-19T16:26:29.000Z：

> it has no hidden memory allocation or control flowRust had like 3 allocating types total. If you aren't working with extremely deeply nested 3rd party types it's trivial to identify when allocations happen. Hell you could throw a lint rule together in like 5 minutes to warn on it if you're really worried. Besides Drop (excluding async) is there even any hidden control flow?> Im speculating here, but I believe its advantage over Rust for that specific application is that you have tighter control over exactly when memory is allocated and deallocated, and how data is laid out in it.Rust has almost exactly the same semantics for controlling allocations and deallocations, it just prevents you from screwing it up and not freeing something or using the allocation after freeing it. You still have to pass around your reference in your call stack until you no longer need it.> Rust wants to tie allocation lifetimes to scope in a very fine grained way that I would guess is beneficial the vast majority of the time, but does still make it harder to reason about when you’re about to stall out the CPU while the allocator does its thing.It's really not substantially different. You allocate ahead of time or don't allocate at all. The only real difference is you might want to use an Option instead of an uninitialized pointer because it's semantically more correct and harder to screw up.

**kllrnohj** · 2026-09-19T16:38:27.000Z：

> Zig is aiming to be lower level than Rust.Zig and Rust are equivalently "low level". Zig isn't any closer to the hardware than Rust is.> but I believe its advantage over Rust for that specific application is that you have tighter control over exactly when memory is allocated and deallocated, and how data is laid out in it.Rust gives you all this, too.Zig's primary (possibly only) advantage over Rust is that it has much faster compilation times.

**treyd** · 2026-09-19T17:34:36.000Z：

> the very thing you reach for a low-level language for - they typically require unsafeThere's a formal proof asserting that if you keep up the safety invariants within an unsafe region then that will not infect other code, even in the presence of arbitrary other correctly-written unsafe blocks.This means you can build abstractions on top of these low-level primitives to keep it contained, so consumer code never has to even think about or know there's unsafe blocks in it. The type system lets you build very powerful abstractions so these go a long way.There's a lot of woo-woo scare quoting around how much you actually have to use unsafe code in Rust. It's fairly uncommon to actually have to reach for them in practice. Most of my usage ends up being things like converting a &[u8] to a &str when I know it's already valid UTF-8 so I want to skip the linear-time validity check. Very rarely do I have to build data structures with complicated pointer juggling, because there's often a library that already does what I need!> which is that over time, as program changes and evolves over years, things tend to drift toward the more general mechanisms that rely on malloc/free on an individual objects, and the program gets slower and slowerWhat are you talking about? I've never encountered this and I've been using Rust for 10 years.

**kibwen** · 2026-09-19T18:15:14.000Z：

Arenas in Rust work very well with lifetimes. In fact arenas benefit greatly from lifetimes, because lifetimes allow them to uphold the usual Rust safety guarantees about preventing use-after-free. For example, here's the bumpalo crate in action: let mut arena = Bump::new(); // create arena
 
 let foo = arena.alloc(Foo { x: 42 }); // allocate item in arena
 
 bump.reset(); // clear arena
 
 foo.x += 1; // compiler error preventing use-after-free

**comex** · 2026-09-19T18:29:26.000Z：

It’s a very common tic of recent Claude models specifically. Don’t worry - for better or worse, the labs are trying to train away AI writing smells (for example, Anthropic talked about Fable 5.1 having more natural writing), so this particular tic will probably become outdated as an AI indicator relatively soon, as em dashes already have. And then people will forget about it.

**pjmlp** · 2026-09-19T15:10:22.000Z：

Also a good one.

**pjmlp** · 2026-09-19T15:09:08.000Z：

If you don't like, press PgDn.

**metaltyphoon** · 2026-09-19T14:54:23.000Z：

After going over that section again I can see it now.

**ifh-hn** · 2026-09-19T14:57:09.000Z：

Are these obvious signs of AI generation?

**junon** · 2026-09-19T15:18:18.000Z：

A number of "<assertion>: <followup>" patterns too which is pretty common of at least Claude.

**12_throw_away** · 2026-09-19T19:33:46.000Z：

> It's unfortunate, but to come across as genuine now I think you have to actively avoid AI-isms.I actually think this might be a good thing? I'm way more aware of cliches and filler in my writing these days, and it almost always reads better when I just remove them and plainly say the thing.

**metaltyphoon** · 2026-09-19T15:01:20.000Z：

That’s the first thing others point to being LLM-generated. If you see, right after the phrase you quote, there is a question as to what else OP thinks is LLM-generated. I didn’t put words into anyones mouth

**lefra** · 2026-09-19T15:47:25.000Z：

I never used it in practice, so maybe the support isn't that good, but I was under the impression that it was possible to pass custom allocators basically everywhere in the STL. See for example the definition of a vector here:https://en.cppreference.com/cpp/container/vector

**pixelesque** · 2026-09-19T18:22:02.000Z：

> and is barely even supported at all in the standard library.What does that mean?

**tonyhart7** · 2026-09-19T15:11:14.000Z：

nothing stopping you to code manually

**frje1400** · 2026-09-19T15:20:04.000Z：

Yes, as an example structured concurrency in Java (final release in Java 28 perhaps). I think that could totally change how we write concurrent code in that language.I just upgraded a less important service to Java 27, a few days after its release (several nice features). It's cool how easy it is to upgrade nowadays.That an agent writes most of the code doesn't mean anything to me here.My examples are Java because that is the main language where I work.

**za3faran** · 2026-09-19T15:28:10.000Z：

There's a couple of languages I follow their roadmap and I find exciting, including Java and C#. I don't feel there's proper justification of writing backend services in something like python or ruby anymore, for example.

**za3faran** · 2026-09-19T15:30:34.000Z：

After reading many comments from its original authors, it's not surprising.

**wannabe44** · 2026-09-19T18:00:17.000Z：

We will imprison these slop addicted monke brains and start new academic regime, only hand written OCaml code allowed.Jokes aside, have you watched 2001 - a space Odyssey?

**simonask** · 2026-09-19T19:25:25.000Z：

I respectfully disagree. The technique has its place, and I use it once in a while, but whether it makes a positive difference for performance is highly sensitive to a number of factors.For example, bump style allocators allocate very quickly, but at the cost of higher memory usage and therefore sometimes worse cache locality.The only way to know is to actually measure.

**simonask** · 2026-09-19T19:29:19.000Z：

If this works for the programs you write, that’s great. It does preclude you from using many great data structures with potentially better performance - especially hash maps. Rehashing is pretty detrimental to most arena allocators you can think of.

**LoganDark** · 2026-09-19T15:34:37.000Z：

I don't know if I would ever depend on something like that for a library crate. There's enough syn+proc_macro2 pollution in the ecosystem already.

**LoganDark** · 2026-09-19T15:53:13.000Z：

> it also means sugar like Rust's for loop, which de-sugars into trait invocations, can never be constant today.Yep, that was my annoyance.Const allocation is possible in Rust as an unstable feature. Not sure if you can persist it to runtime, though you can persist a reference which will become a static reference. I think it being unstable is why I needed `include_bytes!`.

**chaz72** · 2026-09-19T15:24:21.000Z：

And they believe Zig comptime wouldn’t do that? For the same inputs? I’d love an example.

**chaz72** · 2026-09-19T17:22:02.000Z：

Now I see this response, I responded to the other comment.

**nvme0n1p1** · 2026-09-19T19:30:19.000Z：

What's your source for this? Comptime Zig code can do pointer casts and whatnot, all emulated as if run on the target bitness/endianness/etc. And any operations that are undefined on the target platform result in a compile error. I've never had an issue cross-compiling.

**everforward** · 2026-09-19T16:42:39.000Z：

I don’t think this delineation is that clear, unless by “application” you mean the app tier of a 3 tier app.Postgres and Nginx make sense in system programming languages; they’re extremely performance sensitive and that granular level of control offers them features. Interpreters are sort of the same, they interact with the OS a ton, it makes sense to work in the same language as the OS.I do generally agree for the app tier of a web app. I wouldn’t build a CMS in Rust, but I also wouldn’t build a reverse proxy in Python.

**boomlinde** · 2026-09-19T17:01:57.000Z：

What are the requirements and design constraints of an application? Please give a general answer that applies to all applications.

**tcfhgj** · 2026-09-19T17:14:36.000Z：

why shouldn't they? humanity consumes more resources than is sustainable, and systems languages can help to reduce resource consumption.

**monocasa** · 2026-09-19T18:13:02.000Z：

Rust is also a great language for app code. I reach for it now in places I used to use python.

**slopinthebag** · 2026-09-19T16:30:59.000Z：

ironically rust has fewer features than c++ and zig has more than c

**sennalen** · 2026-09-19T16:32:12.000Z：

I wish people would stop inventing new languages for nostd when we have nostd

**bunderbunder** · 2026-09-19T18:27:20.000Z：

But here I feel like we’re at risk of heading down the same old doom spiral that plagues any conversation about programming languages when people try to treat it as a competition: getting pedantic about what’s technically possible in a language. It’s much more interesting to talk about how a language wants to be used.So, in the case of Zig, every function that wants to be able to allocate or deallocate heap memory needs an explicit reference to an allocator. That means that you can tell whether a function might allocate memory from its signature. It also means that changing a function so that it can allocate is explicitly a breaking change.That’s a really interesting design decision. And the reasons why someone would or would not want something like that baked directly into the language are so much more interesting than bickering about how technically with proper discipline you can have that kind of control in any non-GC language.

**pixelesque** · 2026-09-19T18:38:05.000Z：

> Rust had like 3 allocating types total.Seriously? Categories of types maybe, but literal types it's more than that.Even closures allocate if they need to capture their environment.

**maleldil** · 2026-09-19T18:03:07.000Z：

Comptime is a big one too. You can achieve similar things in Rust with generics and macros, but comptime makes certain things easier (and other things harder).

**pron** · 2026-09-19T17:50:09.000Z：

That's always been true in all the safe languages with unsafe escape hatches, except here these "primitives" are the main reason to reach for a low-level language in the first place - because they presumably require the control that low-level languages offer. Combining them in the same language might appeal to some and not to others who think that the high-level, safe parts are unnecessarily complicated because it needs to integrate with the low-level parts, and the low-level parts are unnecessarily complicated because they need to integrate with the safe parts. Anyway, some like this and some don't, but my point is that it's not "mostly solved".> What are you talking about? I've never encountered this and I've been using Rust for 10 years.Okay, but I've been doing low-level programming professionally for 25 years, and have encountered this over and over in large programs (over 500KLOC) as they evolve.

**jey** · 2026-09-19T18:16:28.000Z：

> > which is that over time, as program changes and evolves over years, things tend to drift toward the more general mechanisms that rely on malloc/free on an individual objects, and the program gets slower and slowerI think the idea is that a small program can organize its allocations and data structures to minimize number of calls to malloc, e.g. with preallocated workspace structs, or slab allocation, and similar approaches. But as a program gets bigger, there's a pressure to have looser coupling, to have subsystems with simple convenient APIs which leads to them doing on-demand malloc calls internally, rather than having consumers pre-allocate their needed workspace. Because that kind of workspace management results in more complex APIs and more burden on the consumer.That said, I don't really believe it either, at least for the kind of codebase where it would matter (scientific computing, in-memory DB server, etc). A codebase that places an emphasis on minimizing heap operations in hot codepaths can do so by consistently using workspaces and allocation-avoiding APIs. I don't think it's so difficult really, but it does take a conscious design decision to do so. But writing something like a web browser in this way could be annoying due to most data having wildly variable sizes, and zig's arena concept would be very handy -- but rust has crates like bumpalo for that purpose.My personal mantra: "Think in FORTRAN, code in Rust/Julia/C++". But I'm mostly working on HPC-style code where I don't have to do with wildly varying input or output sizes.

**AndrewDucker** · 2026-09-19T15:23:44.000Z：

People should reply on Hacker News. If you disagree with someone's opinion and you have reasons for doing so then the right thing to do is share them.

**tumdum_** · 2026-09-19T15:04:35.000Z：

Each one makes me update my estimate slightly in favour of AI. Also, pangram agrees.

**IshKebab** · 2026-09-19T15:18:38.000Z：

Yes.

**layer8** · 2026-09-19T16:11:28.000Z：

In aggregate, yes.And even if LLMs didn’t exist (or had different idiosyncrasies), the article would still be exhibiting a repeatedly weird and stilted writing style.

**12_throw_away** · 2026-09-19T19:36:50.000Z：

> [em-dashes are] the first thing others point to being LLM-generated [...] I didn’t put words into anyones mouthA) this isn't true and hasn't been true for a while, B) your first sentence directly contradicts the last one.

**kllrnohj** · 2026-09-19T16:09:37.000Z：

std::allocator was so painful to use it was almost always easier to just reimplement the container instead (especially for trivial ones like vector).I haven't used the relatively new C++17 polymorphic_allocator, though, maybe it fixes this.

**karmakurtisaani** · 2026-09-19T15:19:53.000Z：

Nothing stopping me from doing a lot of things. But is there any point to it?

**karmakurtisaani** · 2026-09-19T15:22:03.000Z：

Thanks for the perspective.

**karmakurtisaani** · 2026-09-19T15:55:05.000Z：

Yeah, I also try to follow what's new. But it's more like "Ok, that's good I guess." Rather than "Cool! Looking forward to applying this in my next project!"

**pjmlp** · 2026-09-19T16:12:41.000Z：

Never was really, at least if performance matters.

**tialaramex** · 2026-09-19T15:52:20.000Z：

It does seem like maybe a crate with convenience macros so you can get a `&'static [Foo; N/size(Foo)]` rather than `&'static [u8; N]` and maybe even a delicious compile time "Hey jerk, that's not a valid Foo, you screwed up" if appropriate from your pre-baked data files, would be nice regardless of having more constant eval.

**estebank** · 2026-09-19T19:20:00.000Z：

FWIW const traits are progressing quite nicely. It will also allow for Default to be used in const context, which is quite handy (and will integrate nicely with default field values, which only allows consts today in nightly).

**weinzierl** · 2026-09-19T16:00:33.000Z：

sin(x) can produce different results at comptime and runtime. In Rust there is no sin(x) at comptime for precisely this reason.

**vlovich123** · 2026-09-19T16:04:46.000Z：

Traditional stuff in this space are:* floating point differences between the build machine and the target. By far the most common* endiannes - code assumes little median runs on big endianThere’s other more subtle issues that can crop up but those are the big two.Not saying I agree though - those can happen anyway when you run on two different machines anyway.

**hn_submit** · 2026-09-19T16:57:41.000Z：

Writing an operating system kernel in C is valid usage since there's a great deal of thought going into it and it almost never changes.EVERYTHING ELSE is invalid usage no matter how performance critical people claim their application is. These are just excuses for people to use a grossly unsafe language to get that last 2% of performance whilst costing the world trillions in lost productivity and security breaches.

**IncreasePosts** · 2026-09-19T17:54:45.000Z：

Give it a chance! Rust hasn't even had its bar mitzvah yet and C++ is already buying a Porsche during its midlife crisis.Yes, on paper zig has more features than C, but what zig has is explicitness. C has a big murky space of implicitness. For example, there might be 5 different zig features which can be used at various times you might use a void* in C, buy the conceptual space of void* fully contains(and then some) the spaces of those zig features.

**orf** · 2026-09-19T19:23:27.000Z：

I agree with you, but it’s not baked directly into the language? It’s just a convention and a shared trait?

**steveklabnik** · 2026-09-19T19:19:38.000Z：

It’s actually the opposite: the language has zero allocations in it. Allocation is entirely a library concern.When you want to have a closure allocate an environment, the closure itself does not: the Box you wrap it in, which is a stdlib type, does.

**treyd** · 2026-09-19T18:02:56.000Z：

That's just not an accurate description of how you write Rust in practice. There's no separate "high level" and "low level" parts/forms of the language any more than the software development process already is all about building abstractions. You should be doing this in Zig, too.It's just that sometimes some of the abstractions you need to build go outside what the ownership and borrowing system can model. And when you don't need to do that (which is 99% of the time) you also get all the benefits of the ownership/borrow system for free.

**pron** · 2026-09-19T18:40:58.000Z：

> but rust has crates like bumpalo for that purpose.Except that's not composable, the exact same issue we have in C++.> But I'm mostly working on HPC-style code where I don't have to do with wildly varying input or output sizes.There you have it. The problems arise more quickly in concurrent rather than parallel code, and when there are lots of features added over the years that touch the hot paths.> in-memory DB serverActually, here there can be big problems (as it's also about concurrency rather than parallelism). Last week a colleague of mine looked at Moka and saw that it could only offer half the throughput as Java's Caffeine at the same latency. When he looked into it, he saw that over 40% of the program's CPU was spent on the epoch-based reclamation.

**pjmlp** · 2026-09-19T15:58:38.000Z：

Sure, except there is a bit of history here, this isn't the first exchange, and I am not bothering to reply back as we aren't going to change opinion on C vs safer languages until we leave this realm.Thus we can keep filling HN with pointless comments or move on.

**layer8** · 2026-09-19T16:05:51.000Z：

Meaningfulness comes from what you care about. I wonder why you were interested in programming-language concepts before but now (apparently) stopped caring about the code. The code still remains the language that communicates the actual program logic.

**frje1400** · 2026-09-19T15:34:17.000Z：

You're welcome. I now feel inspired to try to change your mind, if you don't mind.I would argue that "concepts" actually are more important than ever. Let's take my structured concurrency example. It doesn't matter here exactly what is, but if it ends up being as important as I think it will be, I likely want to write most concurrent code that way going forward.However, it will likely be years until agents go to it unless deliberately steered in that direction. And if I want to make agents write it, I need to review it, and if I'm going to review, I need to understand it.I think this is why I'm not pessimistic about the profession, it still feels like what I'm doing and learning matters.

**chaz72** · 2026-09-19T17:18:26.000Z：

Interesting, I hadn’t run across that but that’s probably just my problem domain. I did find this bug that looks like it was resolved a year ago https://github.com/ziglang/zig/issues/24184 and I have also read they are doing some other work on floating point that will hopefully address other cross-platform inconsistencies.

**chaz72** · 2026-09-19T17:25:16.000Z：

I get it now. Important things but not things that I use often - hopefully addressed by 1.0.

**smj-edison** · 2026-09-19T19:09:47.000Z：

Doesn't comptime run under the target's float and endianness semantics? I need to check, but I believe they emulate the target when evaluating.

**pron** · 2026-09-19T18:34:41.000Z：

They're not separate forms but they are separate modes, and it is precisely because the language tries to fit both these modes into the same language that both suffer. I fully understand the goal of trying to unify these modes into the same language (C++ does the same thing), but there have always been very experienced people who like this approach and those who dislike it, hence it's not "solved". Something is solved when there's a broad consensus it's solved, and there isn't one here.I mean, someone can think it's solved for them, but if they're asking why others don't see it the same way and why many expert low-level programmers are at least intrigued by Zig, this is why.

**jstimpfle** · 2026-09-19T16:06:55.000Z：

There is plenty history of you repeating the same strawmans literally thousands of times. I've just never seen _anyone_ on HN (or elsewhere for that matter) make such claims?

**karmakurtisaani** · 2026-09-19T17:08:09.000Z：

I guess a large part of my motivation was that it makes me a more effective and skilled programmer. There are countless of interesting things out there, and the motivation to focus on one comes from what you do with it later on.

**weinzierl** · 2026-09-19T18:12:51.000Z：

I'm not sure there is something to be addressed. Zig has just a different approach and Zig people different expectations.In Rust we can expand what is possible at compile time without breaking existing code because we took a very careful approach only stabilizing what we are sure about. Some things will probably never be possible at compile time in Rust.Zig is much more powerful but that also means they cannot take stuff away without breaking existing code and making comptime more restricted. So it is unlikely Zig will ever become like Rust in that regard, but that is ok - just different approaches.

**pjmlp** · 2026-09-19T16:14:47.000Z：

Here goes again, better improve your Algolia search skills if you cannot find anyone else.

**chaz72** · 2026-09-19T18:34:35.000Z：

I hear you but I’m not sure it’s as dramatic as that, it’s also been quite predictable in my use over the last few years since I haven’t happened to use floating point or different endianness.

**vlovich123** · 2026-09-19T18:38:41.000Z：

I think the Rust approach is incorrect - if the runtime behavior can change based on the machine that the code gets run on, why is it so important the build time behavior has such a restrictive definition? Especially considering build.rs can be used to bypass that definition anyway. It feels like a weird cut to make that I can’t figure out the understanding for. It feels like it inherited the const philosophy of c++11 without reexamining if it’s actually a good idea.

**jstimpfle** · 2026-09-19T16:21:46.000Z：

I don't even have to search. Given the frequency of you repeating the same old tired stories, one is bound to stumble over your comments every other day.

**tcfhgj** · 2026-09-19T19:19:00.000Z：

reproducible builds

## 关联链接

- https://besok.github.io/posts/what-zig-felt-like-coming-from-rust/
