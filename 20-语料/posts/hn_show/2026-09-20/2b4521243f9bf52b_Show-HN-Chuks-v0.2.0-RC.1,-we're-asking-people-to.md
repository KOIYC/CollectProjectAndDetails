---
type: "corpus"
item_id: "2b4521243f9bf52b"
title: "Show HN: Chuks v0.2.0-RC.1, we're asking people to try to break it"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49764179"
project_url: "https://chuks.org/blog/chuks-v020-rc1-the-release-candidate"
author: "princeLex"
published_at: "2026-09-19T07:20:22Z"
captured_at: "2026-09-20T09:48:16+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-20"
pub_day: "2026-09-19"
tags:
  - 语料
  - hn_show
  - author_princeLex
  - story_49764179
  - show_hn
metrics: {"points": 2, "comments": 0, "engagement_velocity": 2}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:3d"
---

# Show HN: Chuks v0.2.0-RC.1, we're asking people to try to break it

> [!info] 一句话导读
> Published: 2026-09-18

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49764179>
> 指标：点赞=2 · 评论=0 · engagement_velocity=2
> 作者：princeLex　|　发布：2026-09-19T07:20:22Z
> 项目链接：<https://chuks.org/blog/chuks-v020-rc1-the-release-candidate>
> 采集：2026-09-20T09:48:16+08:00　|　id：`2b4521243f9bf52b`

## 正文

Published: 2026-09-18
Author: Chuks Team   Language Design & Engineering

Chuks v0.2.0-rc.1: The Release Candidate | Chuks Programming Language

# Chuks v0.2.0-rc.1: The Release Candidate

 Sep 18, 2026

v0.2.0-rc.1 is a release candidate, not the stable release. Opt in:

Terminal window

# Already have Chuks installed

chuks upgrade --prerelease

# First-time install

curl -fsSL https://chuks.org/install.sh | bash && chuks upgrade --prerelease

A plain `chuks upgrade` stays on v0.1.2 until v0.2.0 ships. On an rc build it says so rather than moving you back.

Chuks v0.2.0-rc.1 is the build we believe is 0.2.0. Everything in it went through the same gate as a release: the golden suite on both backends, the fuzzed differential between the bytecode VM and the native binary, twenty-four differential suites, cross-compilation for five targets, and two consumer test suites that must print byte-identical output both ways. What that gate cannot supply is a program it has never seen. Most of what is fixed below was found not by a test but by building real programs in Chuks; the rest of the way to 0.2.0 is other people’s programs, which is what a release candidate is for.

`chuks --version` prints `0.2.0-rc.1`. A fix found during the candidate ships as `rc.2`, `rc.3` and so on, each picked up by `chuks upgrade --prerelease`; the build that survives is republished as plain `v0.2.0`, which `chuks upgrade` then offers everyone.

## What we are asking for

Build something with it, or point your existing program at it, in both execution modes:

Terminal window

chuks run main.chuks # the bytecode VM

chuks build main.chuks # the native binary

The two must agree, byte for byte, on everything a program prints. Where they do not, or where either of them is wrong, that is a bug we want. Report it at https://github.com/chuks-programming-language/releases/issues/new?template=bug_report.yml with the output of `chuks --version` and the smallest file that shows it. A message that begins “Internal compiler error” is always ours; report it as it stands.

## Breaking changes

Programs written for v0.1.2 may need these edits. Each is a correction to something that was either undefined or different between the two execution modes; the checker reports the first three at compile time.

- A loop binds anew on every pass, and an `if` branch is a scope. A `const` or `var` declared inside a loop body used to be one slot for the whole function, so every closure made in the loop read the last iteration’s value, on the VM and the native binary alike. Now each pass gets its own binding: loop bodies, the `for` counter, `for...of` and `for...in` elements, `while` bodies and `catch` variables. A variable declared outside the loop is still one variable, shared with its closures. Code that relied on the old behaviour, typically a helper parameter used to freeze a loop value, can drop the helper.
- An async function is a function that returns a task.`async function f(): Task ` is assignable wherever `function(...): Task ` is expected and the other way round; the `async` keyword is no longer part of the function type. A `Task ` body no longer warns about a missing return, and reading a member of the awaited value through the `Task` itself (`f().x` without `await`) is now an error.
- A call or `spawn` standing alone as a statement drops its task, and a dropped task’s failure is reported. Before, a task nobody awaited could fail silently. A command-line program reports it at exit; an embedding host is told the moment it happens. If a background task is meant to be left alone, catch inside it.
- `await` and `spawn` bind to the call, not to the rest of the expression.`"[" + await f() + "]"` awaits `f()` and joins the brackets; it used to parse as `await (f() + "]")`, which the VM printed as “Task(pending)” and the native binary as “0”. The checker also rejects a `Task` used where a value is concatenated.
- String positions are bytes, and no accessor cuts a character.`length`, `indexOf`, `slice`, `at`, `charAt` and `substring` all count the same unit now, the byte, on both backends (the VM used to count characters for some of them). A position inside a multi-byte character snaps to the character: `at`, `charAt` and `s[i]` return the whole character containing the byte, `slice` and `substring` return the whole characters inside the range, and `padStart` / `padEnd` count characters because padding is about width. Use `for (var c of s)` or `s.split("")` to walk characters and `runeCount()` to count them. The optional second argument of `indexOf`, `lastIndexOf`, `includes`, `startsWith`, `endsWith` and `split` is honoured on both backends (the native binary dropped it), and `match` / `matchAll` return the matches as a `[]string`. `std/strings` is the string methods under module names and can no longer answer differently from them; `strings.replace` deliberately replaces every occurrence where `s.replace` replaces the first.
- A caught error is its message.`string(e)` in a `catch` is the bare message on both backends; the file, line and trace belong to the report of an error nobody caught. Code that parsed a location out of a caught error’s text should stop.
- `var` is not how a `dataType` field is declared.`dataType R { var x: string }` was silently accepted by dropping the `var`; it is now an error naming the fix.
- Assigning to an imported name has been an error since v0.1.1 and stays one.

## Names that used to be off limits

- A reserved word is an ordinary name wherever a name cannot be an expression: a `dataType` field, a map key, an interface or class member. `dataType Rec { from: string, in: string, class: string }` parses, because a payload’s fields are not the language’s to rename. A reserved word is still not a binding.
- A type parameter may not be named after a builtin type, or listed twice.
- A function or class may be named `Task`, `ChuksError`, `add`, `eq`, `Div` or anything else the native runtime uses internally; the runtime keeps out of the way.
- Two modules may each declare a private variable, type, function or class under one name; a name means what the module that uses it says it means, on every layer.
- `catch`, `finally`, `extends`, `implements`, `as`, `instanceof`, `in` and `of` may open a line; the statement they continue is the one above.

## Added

- `concat` on arrays.`a.concat(b)` returns a new array, on both backends.
- A literal takes its type from where it lands. A record literal nested in another (`{ state: { checked: true } }` against a `dataType` field), a literal initialising an annotated class field (`private session: Session = { ... }`), a typed map value, a typed list element, an assignment, an argument and a return are all checked against the declared type, with unknown keys, wrong values and missing fields reported inside.
- Generics across modules. A generic base class imported from another module can be extended (`class FeedStore extends Store `), a generic function called from a specialised class method gets its own typed copy, and a base-class method that reflects over `this` (`json.stringify(this)`, `this[k] = v`) sees the whole object, subclass fields included, in the native binary as on the VM. Nothing is widened to `any`.
- An imported base class links to the module it came from, under the name that module exported it as. Two packages exporting a `Store` no longer cross, and `import { Base as B }; class X extends B` works on both backends.
- Error messages name values as the program knows them. “string index must be an integer, got string”, never a runtime type name. A value that refuses an index, a lock or a slice reads the same on both backends.
- An awaited task’s failure reports from the throw through every await, on both backends: the trace reads from where it was thrown down through each coroutine that awaited it. A runaway recursion is a runtime error with a trace that elides the middle of the stack, not a crash.
- The native runtime, embedded. A host that embeds a Chuks program (`chuks build --c-archive`) can hand it its time zone (`chuks_set_timezone`), is told of a dropped task’s failure the moment it happens, and survives a call into the engine that fails: the engine recovers and unwinds instead of taking the process down.
- `chuks serve`: linked packages (a symlink in `chuks_packages/`) reload like the app’s own files; a restarted server resyncs a device that saw an earlier run; two devices never share a pack in flight. `chuks install` keeps a package’s `tests/` and `examples/` out of the consumer’s tree.
- `chuks upgrade` understands pre-release versions and never moves you to an older build unless you name it.

## Fixed in the native backend

Found by building real programs rather than fixtures; each has a golden fixture now and, where it fits, a differential cell:

- A method called through `any` that returns a slice or map came back empty in every program that imported `std/strings`.
- `this.x = null` on a nullable class field compiled to nothing.
- A type the runtime references lost its methods when hoisted between generated files.
- A failed HTTP request returned nothing instead of throwing its cause.
- A module whose only runtime use was `??` failed to build (`undefined: Nullish`).
- A dynamic field set through a generic or `any` holder dropped a slice; a map assigned where a record was declared did not become the record; `!=` between two functions crashed.

Performance: a literal passed to a `Record | []T` parameter is built as the record (no hydration per call), and a dynamic field read is a switch with a cached plan instead of a reflection scan.

## By the numbers

Since v0.1.2: 30 commits, 160 files, +8,612 / -1,616. Every change ran the twelve-stage release preflight: the golden suite on both backends, the VM-to-native differential fuzz, 24 differential suites, cross-compilation for five targets, the installed-package consumer build, and two consumer test suites byte-identical on both backends.

# Show HN: Nordstjernen Web Browser 1.0.24 | Hacker News

## 关联链接

- https://chuks.org/install.sh
- https://github.com/chuks-programming-language/releases/issues/new?template=bug_report.yml

## 导航

- 项目页：[[10-项目/chuks.org_87d03422]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
