---
type: "corpus"
item_id: "607516b36e162aea"
title: "Show HN: A Kotlin compiler written in Go, 10x faster than kotlinc"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50315577"
project_url: "https://github.com/barteo/kotlin-compiler-go"
author: "barteo"
published_at: "2026-10-31T12:32:28Z"
captured_at: "2026-11-01T09:38:09+08:00"
lang: "en"
kind: "post"
topic: "开发者工具"
shard: "2026-11-01"
pub_day: "2026-10-31"
tags:
  - 语料
  - hn_show
  - author_barteo
  - story_50315577
  - show_hn
metrics: {"points": 3, "comments": 2, "engagement_velocity": 3}
comments_count: 2
comments_total: 2
discovered_via: "hn:show_hn:3d"
---

# Show HN: A Kotlin compiler written in Go, 10x faster than kotlinc

> [!info] 一句话导读
> barteo/kotlin-compiler-go

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50315577>
> 指标：点赞=3 · 评论=2 · engagement_velocity=3
> 作者：barteo　|　发布：2026-10-31T12:32:28Z
> 项目链接：<https://github.com/barteo/kotlin-compiler-go>
> 采集：2026-11-01T09:38:09+08:00　|　id：`607516b36e162aea`

## 正文

# barteo/kotlin-compiler-go

A Kotlin compiler for the JVM in Go, 10x faster than kotlinc

- Stars: 0
- Forks: 0
- Watchers: 0
- Open issues: 0
- License: Apache License 2.0
- Default branch: main
- Created: 2026-10-31T11:02:08Z

## Languages

- Go
- Java
- Python
- Shell

## Topics

- compiler
- go
- jvm
- kotlin

## Top Contributors

- barteo (1 contributions)

---

## README

# kotlin-compiler-go: a Kotlin compiler in Go

`kc` is a Kotlin compiler for the JVM, written in Go. On real libraries
it compiles 10x faster or more than `kotlinc` running in a warm JVM, and uses
about a tenth of the memory. The libraries it builds pass their own test
suites (Survey of real code), and it passes 95% of
`kotlinc`'s box tests (Conformance).

It is a prototype: it compiles most of Kotlin but not all of it, and it
checks less than `kotlinc` does (What it doesn't do).

## Results

`kc` against `kotlinc` 2.4.21 on an Apple M2 MacBook Air (8 cores, 16 GB),
JDK 21. `kotlinc` runs in a warm JVM, as it does in the Gradle daemon:
the median of repeated compilations in one JVM, after the JIT has warmed
up. `kc` uses all cores, as it does by default.

| Project | Files | Lines | `kotlinc` | `kc` | Speedup |
|:---|---:|---:|---:|---:|---:|
| kotlinpoet 2.4.0 | 39 | 8.7k | 1.23 s | 97 ms | **13x** |
| Ktor 3.6.0 (`ktor-io`, `ktor-utils`, `ktor-http`) | 236 | 24k | 2.32 s | 226 ms | **10x** |
| kotlinx-coroutines-core 1.11.0 | 169 | 34k | 2.50 s | 159 ms | **16x** |

- **On one core** (`kc -j 1`) `kc` is still 6.6–8.8x faster than warm
 `kotlinc`: 143 ms, 350 ms and 285 ms.
- **Cold**, with a new JVM per build as on the command line or in CI,
 `kotlinc` takes 6.9 s, 19.2 s and 10.9 s, 69–85x slower than `kc`.
- **Memory:** `kc` peaks at 85–118 MB, and cold `kotlinc`, with an 8 GB
 heap limit, at 1.0–1.1 GB.

How each number is measured, and the full tables with CPU time, are in
Benchmark.

## What it doesn't do

`kc` doesn't do all the work `kotlinc` does. It leaves out:

- **Some of the language.** A few features aren't supported, and
 visibility isn't checked. Unsupported Kotlin
 lists them all.
- **Most of `kotlinc`'s checks.** `kotlinc` runs 290 checkers for
 warnings and errors after type checking. `kc` has no separate
 checkers: it reports the errors that type checking finds, which is why
 it agrees with `kotlinc` on only 79% of the diagnostics tests.
- **Anything but the JVM.** There is no Kotlin/Native, JS or Wasm, and no
 language versions.
- **Incremental compilation, a Gradle plugin and IDE support.**
- **Identical output.** The class files work the same, but differ in
 places. For example, `kc` shares the objects of inline functions where
 `kotlinc` copies them, so it writes 790 classes for
 kotlinx-coroutines-core and `kotlinc` writes 850.
 Differences from kotlinc
 lists them.

The checkers don't explain the speedup. In a profile of both compilers
on one thread, `kc` is faster at each phase that both of them run:

| Work | `kotlinc` | `kc -j 1` | Ratio |
|:---|---:|---:|---:|
| Parsing | 4.7 s | 0.27 s | ~18x |
| Resolution and type checking | 8.8 s | 0.92 s | ~10x |
| Checkers (warnings and errors) | 5.4 s | none | |
| Reading the class path | 0.4 s | 0.01 s | |
| Backend, with inlining and writing | 19.1 s | 1.32 s | ~14x |
| **Total** | **38.4 s** | **2.51 s** | **15x** |

Even without its checkers, `kotlinc` would take 33 s, 13x as long as
`kc`. This profile is of 500 generated files (202k lines) in a warm JVM
(Where kotlinc's time goes).

## Why it's faster

- **No JVM.** `kc` starts in milliseconds; a cold `kotlinc` spends
 seconds starting the JVM and warming up the JIT.
- **Parallelism.** `kc` parses, checks bodies and generates class files
 on all cores; `kotlinc`'s frontend uses one.
- **Fewer passes.** `kotlinc`'s time is spread over 88 IR lowerings and
 290 checkers, none above about 2%. `kc` generates code in one pass
 over the checked AST.
- **Lazy inputs.** `kc` indexes the class path in about 5 ms while
 parsing, and decodes a class only when it's first used.

Design describes the pipeline.

## Try it

Requires Go 1.27.2+ and a JDK. The tests and benchmarks also need
`kotlinc` and `hyperfine` (`brew install go openjdk@21 kotlin hyperfine`).

```sh
go build -o bin/kc ./cmd/kc
bin/kc -d out testdata/run/fizzBuzz.kt
java -cp out FizzBuzzKt
```

`kc` doesn't add the standard library by itself. Put `kotlin-stdlib.jar`,
and any other libraries the program uses, on the class path to compile
and run it. For example, with kotlinx.coroutines, which ships with
`kotlinc`:

```sh
L=$(brew --prefix kotlin)/libexec/lib
CP=$L/kotlin-stdlib.jar:$L/kotlinx-coroutines-core-jvm.jar
bin/kc -cp $CP -d out testdata/run/stdlibCoroutinesBasics.kt
java -cp out:$CP StdlibCoroutinesBasicsKt
```

Arguments can be files or directories. Flags:

| Flag | Meaning |
|---|---|
| `-d` | output directory (default `.`) |
| `-cp`, `-classpath` | jars and directories to compile against |
| `-jdk-home` | JDK whose classes to use (default: `$JAVA_HOME`, or the JDK of `java` on `PATH`) |
| `-no-jdk` | don't use JDK classes |
| `-module-name` | module name, as in `kotlinc` (default `main`) |
| `-friend-paths` | class path entries whose internal declarations are visible (`kotlinc`'s `-Xfriend-paths`) |
| `-parcelize`, `-serialization`, `-compose` | apply the parcelize, kotlinx.serialization and Compose plugins |
| `-jvm-default` | how interface bodies compile, as in `kotlinc` (default `no-compatibility`) |
| `-Xdebug` | keep dead variables in suspend functions for debuggers, as in `kotlinc` |
| `-j` | parallel workers (default: all CPUs) |
| `-time` | print per-phase timings |
| `-features` | print each error with its unsupported feature, tab-separated |

There is no Gradle plugin. To try `kc` in a Gradle build, a Gradle init
script can replace a module's Kotlin compile task with a call to `kc`.
bench/kotlinpoet/kc.init.gradle.kts
does this for kotlinpoet.

### Repeat the benchmark

```sh
git clone --depth 1 --branch 1.11.0 https://github.com/Kotlin/kotlinx.coroutines.git \
  "${TMPDIR:-/tmp}/kc-survey/kotlinx-coroutines-1.11.0"
RUNS=5 WARM_RUNS=20 bench/coroutines-time.sh
```

`bench/coroutines-time.sh` builds `kc`, downloads the library's
dependencies from Maven Central, compiles it with both compilers using
its Gradle build's options, and writes the table to
bench/results/time-coroutines.md.
It expects `kotlinc` and the JDK where Homebrew installs them; set
`KOTLIN_HOME` and `JAVA_HOME` otherwise. `bench/kotlinpoet-time.sh` and
`bench/ktor-time.sh` time the other two libraries
(Benchmark).
## Documentation

- Unsupported Kotlin: what `kc` doesn't support, and
 where its output differs from `kotlinc`'s
- Design: the pipeline, type checking, class file
 generation, the inliner, coroutines and compiler plugins
- Benchmark: how `kc` is measured against `kotlinc`,
 and the results
- Survey of real code: which features real libraries use,
 and libraries built with `kc` and tested end to end
- Conformance: `kotlinc`'s own box and diagnostics
 tests run against `kc`

## Tests

```sh
go test ./...
```

Tests use the JDK in `$JAVA_HOME`, or the JDK of `java` on `PATH`. On macOS
`/usr/bin/java` is only a launcher, so set `JAVA_HOME`, for example
`export JAVA_HOME=$(/usr/libexec/java_home -v 21)`. Without a JDK, tests fail
with unresolved references to Java classes such as `HashMap`.

Tests that need the standard library find `kotlin-stdlib.jar` in
`$KOTLIN_HOME/lib` or next to `kotlinc` on `PATH`, and are skipped without
it. Tests that compare with `kotlinc` are skipped if it isn't on `PATH`. The
kotlinx.serialization 1.9.0 and Compose runtime 1.9.2 tests use jars from
Gradle's cache, or from `KC_SERIALIZATION_CP` and `KC_COMPOSE_CP`, and are
skipped without them.

- `testdata/run/`: programs compiled with `kc` and run under
 `java -Xverify:all`. Output must match `*.out`, which
 `testdata/gen_expected.sh` generates with `kotlinc`. A directory is a
 multi-file program with `main` in `main.kt`.
- `testdata/lib/`: a library compiled by `kc` and a program compiled
 against it by `kc` and by `kotlinc`. Both must produce `X.out`.
- `testdata/errors/`: each `// ERROR ` comment marks a line that must
 produce a diagnostic containing that text.
- `TestCoroutineShapes`: compares `kc`'s and `kotlinc`'s coroutine classes;
 differences must be listed in `testdata/coroutine-shapes.golden`.
- Package tests in `internal/` cover the parser, Kotlin metadata, class
 file frames and methods, the inliner and class path loading.

## License

Apache License 2.0, the same as `kotlinc`. See LICENSE.

Error fetching https://puzzle.io27.com/: CRAWL_EMPTY_CONTENT

## 评论（2/2）

> **barteo** · 2026-10-31T12:42:22.000Z　
> Hi HN, kc is a Kotlin compiler for the JVM, written in Go.Why I built it: most Kotlin tools, like linters, KSP and the language server, are built on kotlinc's frontend, so they're only as fast as it is. A fast frontend could make room for:- Linters that run in milliseconds instead of seconds- A fast language server- Much faster KSP annotation processing- Quicker builds in CI, where every run starts a cold JVM- Fast feedback for coding agents, which compile and fix code in a loop many times per taskI measured big gains in both speed and memory against kotlinc 2.4.21, running warm as in the Gradle daemon:- kotlinx-coroutines-core: 2.50 s → 159 ms (16x)- Ktor core modules: 2.32 s → 226 ms (10x)- kotlinpoet: 1.23 s → 97 ms (13x)- Memory: ~1 GB → ~100 MBWhat it doesn't do yet:- A few language features aren't supported- No warnings, and only the errors that type checking finds, so some invalid code compiles- JVM only, no Gradle plugin or IDE support- Passes 95% of kotlinc's box testsIt's a prototype, but I plan to keep working on it until it's useful for a wide range of real projects.Benchmark details and how to repeat them: https://github.com/barteo/kotlin-compiler-go/blob/main/docs/...

---

> **Rochus** · 2026-10-31T13:25:47.000Z　
> This is amazing, particularly the much smaller memory use, which I assumes comes because structured types can be used by value in Go (vs. the all heap approach of Java), isn't it? I assume the parallelization of the front-end is explicit in the source code (haven't looked at the source so far); what Go concepts did you use for it?You could even consider re-using the Go compiler IR and backend for native, statically linked binaries, instead of generating JVM IR.

## 关联链接

- https://github.com/Kotlin/kotlinx.coroutines.git
- https://puzzle.io27.com/:

## 导航

- 项目页：[[10-项目/github.com_b7af218e]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`开发者工具`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
