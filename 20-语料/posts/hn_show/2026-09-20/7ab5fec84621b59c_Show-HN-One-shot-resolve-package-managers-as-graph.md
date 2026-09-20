---
type: "corpus"
item_id: "7ab5fec84621b59c"
title: "Show HN: One-shot resolve: package managers as graph schedulers (2x faster)"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49740792"
project_url: "https://glu.run/blog/installing-homebrew-packages-faster"
author: "henrikklee"
published_at: "2026-09-17T13:53:50Z"
captured_at: "2026-09-20T09:36:52+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-20"
pub_day: "2026-09-17"
tags:
  - 语料
  - hn_show
  - author_henrikklee
  - story_49740792
  - show_hn
metrics: {"points": 2, "comments": 0, "engagement_velocity": 2}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:90d"
---

# Show HN: One-shot resolve: package managers as graph schedulers (2x faster)

> [!info] 一句话导读
> Published: 2026-09-14

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49740792>
> 指标：点赞=2 · 评论=0 · engagement_velocity=2
> 作者：henrikklee　|　发布：2026-09-17T13:53:50Z
> 项目链接：<https://glu.run/blog/installing-homebrew-packages-faster>
> 采集：2026-09-20T09:36:52+08:00　|　id：`7ab5fec84621b59c`

## 正文

Published: 2026-09-14
Author: Henrik Klee Published September 14, 2026

Installing Homebrew packages 2.3x faster — glu

# Installing Homebrew packages 2.3x faster

I wanted to know whether Homebrew's packages could be installed faster. So I built a new client for them.

Henrik Klee Published September 14, 2026

Installing a dev tool on macOS is usually just a`brew install` away. It is easy and convenient, but often doesn't feel very fast. A cold install with a large dependency graph can take minutes while logs scroll by.

After using Bun and uv, I kept wondering why installing native Mac packages could not feel just as fast.

"Why doesn't someone just rewrite Homebrew in Rust?"

Eventually I decided to find out. With the help of AI, one weekend should be enough, or so I thought.

Turns out I was very wrong. Weeks later, the weekend project had become glu, a Rust package manager that installs Homebrew's bottles through its own resolver and installer. In end-to-end cold-install benchmarks, it is more than twice as fast as Homebrew on larger package graphs. This is how I got there, and why the Rust rewrite was only one part of it.

Median end-to-end install times, including dependencies. Methodology and full results.

## First, you need packages

To build a package manager, you need a repository of packages to install from. That means sourcing prebuilt binaries for thousands of packages and all supported architectures, or building a system that compiles them. It is an extremely time-consuming and expensive endeavor, definitely too much for a weekend project.

What if I could take an existing package repository and put a modern UX and a fast client in front of it?

Homebrew provides more than 8,000 prebuilt packages, called bottles, for all architectures that I cared about. So I set out to build a first POC: could Homebrew's bottles be installed correctly and faster without running Homebrew itself?

## The Python prototype

The first prototype was a Python program called `coldbrew`. It parsed Homebrew's `formula.json`, looked up the requested package, downloaded and extracted its bottle, and copied it into a target directory.

Installing a bottle takes more than extracting it. Bottles can contain placeholders such as `@@HOMEBREW_PREFIX@@` for the final installation directory. Replacing those paths is called relocation, and modified Mach-O binaries have to be signed again. Packages also need to be linked into directories on `PATH`, except when Homebrew marks them as isolated or keg-only. Many packages have additional postinstall work after their files are linked.

I ported enough of Homebrew's relocation, linking, and structured postinstall behavior to install real packages. The implementation was still POC-shaped: extraction shelled out to `tar`, Mach-O changes used external tools, and signing called Apple's `/usr/bin/codesign`. I expected to implement all of this exhaustively in Rust if the experiment worked.

## Homebrew had already tried Rust

During these first experiments, I found `brew-rs`. Homebrew had already tried replacing parts of its Ruby frontend with Rust and had abandoned the project.

Their benchmarks found Rust faster for narrow bottle-fetch operations, especially with warm caches. Ruby was faster in their representative full-install comparisons. Homebrew concluded that the narrow wins did not justify maintaining a separate frontend and moved its performance work back to Ruby.

This was not encouraging, but it also made the experiment more interesting. If`coldbrew` became faster while it was still written in Python, the answer could not simply be the language. glu is not based on `brew-rs` and shares no code with it.

## Where does the time go?

With the basic behavior in place, I could run `coldbrew install node`. It worked, but the first version was still slow. Rust would reduce startup and process overhead later, but first I needed to know what was happening during an install.

The first addition was a structured trace format. It recorded what ran when, which worker picked up each job, and how much time went into downloads, relocation, code signing, disk writes, linking, and postinstall.

On small installs, the bottleneck was often startup overhead or network speed. Larger graphs behaved very differently. `vips`, for example, pulls in around 96 dependencies. A large package could start downloading too late. Many relocations could saturate the CPU. Too many concurrent writes could congest the disk. A cache refresh could take 20 seconds on its own.

A recorded `vips` install. Open the image to inspect the full trace.

It was obvious at this point that Homebrew was not slow simply because it was written in Ruby.

Package installation is a graph problem. The key to making it fast is optimizing the installation graph end to end.

## Optimizing the installation graph

`coldbrew` downloaded packages concurrently from the beginning. After benchmarking different limits, I settled on HTTP/2 multiplexing with up to 16 concurrent downloads.

Next I overlaid the package-local work. As soon as a package finished downloading, a worker could extract it, relocate it, and sign it while the remaining downloads continued. This made a large difference on relocation-heavy graphs such as`gcc`.

The design used multiple prepare workers, 16 download workers, and a serial commit lane for linking and postinstall. That lane stayed dependency-ordered so a package had all of its dependencies available when its own postinstall ran. Before any download or installation work started, `coldbrew` computed the complete installation DAG.

```
resolve
   ├── download A ── prepare A ─────────────── commit A
   ├── download B ───────── prepare B ─────── commit B
   └── download C ── prepare C ── commit C ── shared postinstall
```

Once downloads and preparation ran concurrently, download order started to matter. There were more packages waiting than available download slots, and picking the wrong package could leave the rest of the pipeline waiting later. That required a scheduler that chose which package to download next based on its effect on the full install.

The first scheduler used a score based on artifact size and graph criticalness. Size was an estimate of how long the download would take. Graph criticalness represented how much other work was waiting behind that package. This gave large downloads an early start without pushing small dependencies that unlocked long chains of work to the end.

To compute that score, I needed the artifact sizes. `formula.json` does not include them, so I wrote a script that downloaded all bottle manifests from GHCR up front. Those manifests contained the sizes needed for scheduling.

Different install graphs kept exposing problems with the scoring model. Even with a good starting order, a large package could still become the tail of the install. A small dependency arriving too late could leave the commit lane idle. One slow CDN connection could hold up everything. Finding these cases led to many iterations of the scheduler.

The current version estimates how each download affects the completion time of the full install. Large artifacts are split into smaller parts, allowing the most critical download to use more of the available bandwidth. Slow connections can launch bounded rescue requests. Known expensive preparation and postinstall operations also affect download priority.

Some packages request the same expensive postinstall steps. Often these are cache refreshes. Running the same refresh after every package can add 20 seconds or more. `coldbrew` coalesced these requests and ran the refresh once after all contributing packages were installed. Depending on the graph, shared work can start while other packages are still downloading.

More work went into avoiding redundant directory walks and repeated file reads. Shared limits for writers, CPU-heavy work, and memory stopped one part of the installer from overwhelming the others.

At this point, `coldbrew` was already much faster than Homebrew on many of the graphs I had tested. Its behavior was still POC-shaped, but I considered the main performance problem solved. The Rust port, exhaustive correctness work, and the rest of the package manager commands still remained.

## Getting the full graph in one request

Efficient scheduling depends on knowing the full graph and every artifact size before the downloads start. The POC got its package data from `formula.json` and used the bottle manifests I had downloaded separately. That worked for the experiment. A real client would otherwise have to keep all of this metadata updated locally or request formula and bottle data while walking the graph. Both options add work before the scheduler can make useful decisions.

A small registry with a `/resolve` endpoint would do this work in one shot. The registry loads Homebrew's formula data and all bottle manifests into memory before it serves requests. When the client sends the requested package roots and target platform, the registry builds the full graph from that in-memory data and returns one complete install manifest.

The manifest includes the required packages, versions, dependency edges, download URLs, checksums, file sizes, linking metadata, and postinstall steps. After receiving it, the client reconciles the graph with the packages already installed locally and can start scheduling downloads after one server round trip. There is no separate local metadata refresh and no cascade of formula and manifest requests during resolution.

The first registry implementation used SQLite. Later, I rewrote it around in-memory maps. Large graphs now resolve in milliseconds.

## Porting it to Rust

The Python POC had already shown that the architecture worked. At that point, the Rust port looked mostly like a matter of implementing the same design properly, closing the remaining correctness gaps, and adding the commands needed for a complete package manager.

Homebrew's relocation, linking, signing, and postinstall behavior was ported very carefully this time. Compatibility-sensitive functions carry provenance comments with the upstream commit, file, and line. Before an install changes anything, glu validates the complete manifest and checks that every required transformation and postinstall step can be executed.

The Rust implementation also replaced the external tools used by `coldbrew`. Checksum validation, extraction, relocation, Mach-O changes, and signing moved into the process. Keeping these operations together avoided subprocess launches, repeated directory walks, and unnecessary full-file writes.

The orchestrator and download scheduler were rewritten several more times. From then on, every unusually slow benchmark run sent me back to its trace. Often I ended up changing the scheduler again. Some fixes helped one graph and hurt another. Correctness fixes also introduced performance regressions, which meant finding a way to keep the fix without adding time to the critical path.

Once the main implementation worked, I ran repeated code reviews with Fable and GPT. These reviews went deep into correctness, security, filesystem safety, and failure handling. Working through the findings often led to another round of implementation and testing. Some hardening changes added work to the install path, so I used the traces to recover the performance without undoing the safety improvement.

## From installer to package manager

A package manager is not very useful with only an install command. For installed state, I wanted something simple to reason about, similar to npm's `package.json`. That led to `glu.json`, which records the packages the user actually asked for. glu installs those packages and their dependencies, then removes dependencies that are no longer needed.

Then came commands for updating, removing, inspecting, recovering, and cleaning packages. The terminal output became short and phase-oriented instead of printing every internal operation. Every failed install points to its trace.

## A CLI for agents

Today, agent experience is as important as user experience. I had my coding agent use glu and noticed that ordinary CLI help leaves too much room for guessing. An agent managing system packages needs to know which commands mutate state, what they can change, whether they may prompt, and how failures are reported.

Every glu command therefore has a `CommandSpec` from which the human help, machine-readable command description, and JSON schemas are derived. Mutating commands support `--plan`, and JSON mode returns strict success and error envelopes without progress output mixed in. An agent can inspect the entire contract with`glu help --json --schemas`, preview a change, and only then approve it with `--yes`.

## Correctness

Speed does not matter if the installed package is wrong. To verify the result, I built a correctness harness that installs packages with Homebrew and glu, normalizes the expected differences, and compares the results. It checks files, links, permissions, Mach-O metadata, signatures, and package-specific command output.

This uncovered some Homebrew quirks and missing edge cases in glu. I have not tested every package on every platform, but glu now installs and manages most, if not all, packages correctly.

## Then I found nanobrew

When glu was almost finished, I discovered nanobrew. Its homepage called it the fastest macOS package manager. For a moment, I thought I had spent all this time building something that already existed.

Looking closer, nanobrew's largest speed claims focused on warm reinstalls from its content-addressed store and operations where nothing had to change. Its published charts also include cold installs, but the headline numbers such as a 39ms warm install and 0.1ms no-ops measure a different workload from the one I had optimized glu for.

My benchmark measures the full cold install: resolution, downloads, dependencies, relocation, linking, and postinstall. I added nanobrew to the benchmark runner and tested all three package managers under the same conditions.

## Benchmarks

For benchmarking, I built a runner that can measure cold installs of any set of packages, including their dependencies and postinstall work. For the published benchmark, I used `jq`, `node`, and`vips`. The runner executes each package manager in an interleaved order, restores a clean state and download cache before every attempt, and validates the installed package with package-specific probes.

Across six real network environments, glu was more than twice as fast as Homebrew on the larger `node` and`vips` graphs, and also faster on the smaller`jq` graph. Every glu install passed its validation probes. The benchmark page contains the complete dataset, failures, network breakdowns, and methodology.

### Update: Homebrew 7

Since I started writing this post, Homebrew 7 was released with more concurrency across downloads, preparation, and installation, along with fewer subprocesses and earlier use of API bottle metadata. I ran fresh benchmark sessions against v7. glu remained faster on `jq` and more than twice as fast on `node` and `vips`.

## So, was it the Rust rewrite?

Most of the important performance work had already happened in Python. Rust reduced the overhead of the binary and allowed extraction, relocation, Mach-O changes, and signing to happen in one process. The larger improvement came from computing the full graph up front, overlapping work, prioritizing the packages that determine wall time, controlling shared resources, and avoiding repeated postinstall work.

So the answer to "why doesn't someone just rewrite Homebrew in Rust?" is that rewriting it in Rust is not enough. You have to optimize the installation graph end to end.

glu is now fast enough that a package installation usually feels like one operation instead of a sequence of waits. If you encounter a bug or a slow install, let me know.

# Smart Mouth Billy Bass

## 导航

- 项目页：[[10-项目/glu.run_e2dd714f]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
