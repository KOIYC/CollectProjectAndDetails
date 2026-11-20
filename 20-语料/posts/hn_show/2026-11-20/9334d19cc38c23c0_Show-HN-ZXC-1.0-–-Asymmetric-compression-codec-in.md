---
type: "corpus"
item_id: "9334d19cc38c23c0"
title: "Show HN: ZXC 1.0 – Asymmetric compression codec in C, now in ClickHouse beta"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50560067"
project_url: "https://github.com/hellobertrand/zxc/releases/tag/v1.0.0"
author: "pollop_"
published_at: "2026-11-19T13:48:22Z"
captured_at: "2026-11-20T09:45:52+08:00"
lang: "en"
kind: "post"
topic: "开发者工具"
shard: "2026-11-20"
pub_day: "2026-11-19"
tags:
  - 语料
  - hn_show
  - author_pollop_
  - story_50560067
  - show_hn
metrics: {"points": 4, "comments": 0, "engagement_velocity": 4}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:3d"
---

# Show HN: ZXC 1.0 – Asymmetric compression codec in C, now in ClickHouse beta

> [!info] 一句话导读
> ZXC v1.0.0 - Hydrogen

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50560067>
> 指标：点赞=4 · 评论=0 · engagement_velocity=4
> 作者：pollop_　|　发布：2026-11-19T13:48:22Z
> 项目链接：<https://github.com/hellobertrand/zxc/releases/tag/v1.0.0>
> 采集：2026-11-20T09:45:52+08:00　|　id：`9334d19cc38c23c0`

## 正文

# ZXC v1.0.0 - Hydrogen

- Tag: v1.0.0
- Repository: hellobertrand/zxc
- Published: 2026-11-11T08:01:51Z
- Author: hellobertrand

---

# Release Notes

v1.0.0 is a major release, and the stability release: the format is frozen, the C API is settled, and the compressed bytes do not change.

Its codename is **Hydrogen**, element 1. Each later major or minor releases will take their codenames from the next elements of Mendeleev's periodic table. Patch releases keep the codename of their series.

**Format v9 is frozen. Archives written by v0.15.0 decode as they are, and v1.0.0 writes byte-identical archives at levels 1 to 7. Any later format change is additive: newer readers keep reading older archives.**

What does change is the surface around those bytes. Settings move from option structs to parameters set on a context, which lets the API grow without breaking the ABI. The CLI now keeps its input files by default, and the bindings verify checksums by default when decoding.

> ⚠️ **Breaking change (API, ABI, CLI and bindings). No archive migration from v0.15.x.** The **soname moves to `libzxc.so.6`**, so programs linked against `libzxc.so.5` must be rebuilt, and C callers must update their source. Go users must update their imports: **the module moves to `github.com/hellobertrand/zxc/bindings/go`**. These behaviours change silently or at run time:
>
> - **`zxc_decompress()` no longer verifies checksums**, and neither do `zxc_decompress_inplace()`, `zxc_dstream_create(NULL)` and `zxc_stream_decompress(fin, fout, NULL)`. To keep the check, decode through a `zxc_dctx` with `ZXC_D_CHECKSUM` set.
> - **An out-of-range level is refused, no longer clamped.** `zxc_compress(..., 99)` returns `ZXC_ERROR_BAD_LEVEL`.
> - **`zxc` keeps its input files.** Scripts that relied on the old removal must add `--rm`.
> - **`zxc` no longer ignores file operands.** `zxc -z a b c` without `-m` now fails instead of overwriting `b`.
> - **The bindings change their checksum defaults.** Go, Python, Node.js and WASM now verify checksums when decoding, and Rust no longer writes them by default.
>
> Coming from v0.14.x or older, archives still need the one-time transcode, as format v9 only reads v9:
>
> ```sh 
> zxc-old -dc old.zxc | zxc-new -z -c > new.zxc 
> ```
>
> Full guide, with a call-by-call table for the C API: **docs/MIGRATION.md**.

## The format freeze

Format v9 keeps the wire layout of v0.15.0. From this release on, `docs/FORMAT.md`, the conformance vectors and the golden archives are the reference.

- **The bytes did not move.** The 13 golden archives and the 53 conformance files are identical to those of v0.15.0. Only their names and location changed (#538, #548).
- **Stricter decoders (#547).** File, block and `.zxd` headers with non-zero reserved bits or bytes are rejected as corrupt, closing a channel for smuggled metadata. v0.15.0 writes zeros there, so its archives and dictionaries are unaffected.
- **Block types get descriptive names (#538).** GLO becomes **SPL** (split streams) and GHI becomes **PAK** (packed sequences), in the code, the documentation and the test vectors. The on-disk bytes are unchanged.

## A C API built to last (#545, #546)

Option structs were part of the ABI, so adding a field changed their layout. Parameters are appendable identifiers, so new settings no longer break it.

```c
zxc_cctx* c = zxc_create_cctx();
zxc_cctx_set_param(c, ZXC_C_LEVEL, 5);
zxc_cctx_set_param(c, ZXC_C_CHECKSUM, 1);
zxc_compress_cctx(c, src, n, dst, cap);
zxc_free_cctx(c);
```

- **Parameters.** `zxc_cctx_set_param()` / `zxc_dctx_set_param()` and their getters, with bounds from `zxc_cparam_bounds()` / `zxc_dparam_bounds()`. `0` restores the default, and a new `ZXC_ERROR_BAD_PARAM` reports an invalid value or identifier.
- **One-shot calls.** `zxc_compress(src, n, dst, cap, level)` and `zxc_decompress(src, n, dst, cap)` take nothing else. Checksums and dictionaries need a context.
- **Dictionaries are copied on attach.** `zxc_cctx_set_dict()` / `zxc_dctx_set_dict()` leave the caller free to release its buffers as soon as they return.
- **One dictionary prefix.** `zxc_train_dict` -> `zxc_dict_train_content`, `zxc_train_dict_huf` -> `zxc_dict_train_huf`, `zxc_dict_id` -> `zxc_dict_compute_id`, `zxc_dict_get_id` -> `zxc_dict_read_id`.
- **Bound functions return `size_t`.** `zxc_compress_bound()`, `zxc_compress_block_bound()`, `zxc_decompress_block_bound()` and `zxc_estimate_cctx_size()` drop `uint64_t`. An input too large for the platform returns 0 instead of wrapping.
- **Run-time version.** `zxc_version_number()` and `zxc_version_codename()` report the loaded library (#545, #560).
- **Streams take a context.** `zxc_stream_compress()`, `zxc_stream_decompress()`, `zxc_cstream_create()` and `zxc_dstream_create()` read their parameters from a `const` context.

## Performance

**Single-threaded speed is unchanged from v0.15.0**: within 2 % on Neoverse-V2, Zen 5 and Zen 3 for both compression and decompression. The compressed sizes are identical.

Decompression lead over the codec with the nearest ratio, on Silesia (202 MB), single thread, lzbench 2.4.1. ZXC is also smaller in every pairing.

| Machine | `-1` vs `lz4 --fast` | `-3` vs `lz4` | `-6` vs `lz4hc -9` | `-7` vs `zstd -1` |
|:---|---:|---:|---:|---:|
| Apple M3 | **2.41x** | **2.14x** | **1.61x** | **2.95x** |
| Neoverse-V2 | **1.92x** | **1.54x** | **1.28x** | **2.16x** |
| EPYC Zen 5 | **2.20x** | **1.64x** | **1.22x** | **2.47x** |
| EPYC Zen 3 | **1.82x** | **1.35x** | **1.15x** | **2.35x** |

In absolute terms, level 1 decodes at **14.8 GB/s** on Apple M3 and **11.7 GB/s** on Zen 5, and level 3 at **11.0 GB/s** and **8.3 GB/s**. Full tables: README and WHITEPAPER.

*The reference client moves from Apple M2 to Apple M3, so the M3 figures cannot be compared with those published for v0.15.0. The benchmarks also move to `lzav` 5.20.*

### Seekable ranges (#562)

Single-threaded ranges decode directly into the caller's buffer when it is safe, as the one-shot API does. Multi-threaded workers claim batches of consecutive blocks by size, as the `FILE*` engine does. Silesia on Apple M3, 8 threads, against the previous code:

| Block size | Before | After | Gain |
|:---|---:|---:|---:|
| 4 KB | 15.72 GB/s | 28.80 GB/s | **+83.2 %** |
| 64 KB | 36.02 GB/s | 43.02 GB/s | **+19.4 %** |
| 512 KB | 37.84 GB/s | 46.17 GB/s | **+22.0 %** |

Single-threaded ranges gain 7 to 18 %.

### Thread counts (#561)

`-T N` and the thread parameters now always mean N encode or decode workers, with the reader and writer threads on top. Auto-detection uses the online processors minus one, unless the workers do their own reads.

## CLI

- **Input files are kept by default (#558).** `--rm` removes the input once its output is written. It is ignored with an explicit output, standard output, `-t` and `-l`, and `-k` takes precedence.
- **File metadata is preserved (#539).** Output files get the input's permission bits, access and modification times, group, and owner when run as root. `--no-preserve` turns this off.
- **Failed or interrupted runs no longer lose data (#578).** `-f` replaces the output only once the new one is complete, where a failed run used to destroy it. A fatal signal removes the partial output, except on Windows. A read error on the input fails instead of passing for the end of the input.
- **No file operand is dropped (#578).** More than two operands need `-m`, and `-o` takes one input. `-c` and `-t` treat every operand as an input, so `zxc -dc a.zxc b.zxc` writes both and `zxc -t a.zxc missing b.zxc` fails. `-t -j` over several files prints one JSON array.
- **An output that is the input under another name is refused (#555).** `zxc -f -o DATA.TXT data.txt` on a case-insensitive filesystem could destroy the input and still exit 0. The guard now compares file identity as well as paths, which also covers short names and links. Reported and fixed by @Vladexy88x (#550).
- **`--rm` on a symbolic link removes the link, not its target (#557).**
- **`-r` picks the right files (#558).** It skips `.zxc` files when compressing and selects only them when decompressing or testing. Links are ignored, including a link given as the starting path.
- **`-V` names the release and the build (#535, #559, #560):** `ZXC CLI v1.0.0 "Hydrogen" (build arm64 64-bit LE)`.
- On Windows, long options that take no argument now reject one, as they already did on Linux and macOS (#558). `--bench` logs its errors (#546).

## Bindings

- **`wrappers/` becomes `bindings/` (#581).** The Go module moves to `github.com/hellobertrand/zxc/bindings/go`, tagged `bindings/go/vX.Y.Z`, and versions up to v0.15.0 stay published under `wrappers/go`. It now carries the C sources, so `go get` needs cgo and a C compiler but no separate build of the library.
- **Checksums are verified by default on decode (#580).** Go, Python, Node.js and WASM now verify the checksums an archive carries, and an archive without checksums decodes either way. Opt out with `zxc.WithChecksum(false)`, `checksum=False` or `checksum: false`. The C one-shot `zxc_decompress()` stays the fast path and does not verify.
- **Rust writes no checksums by default (#580),** like the other bindings. Ask with `with_checksum()`; `without_checksum()` is deprecated. Decoding already verified by default.
- **Hardening (#580):** Go and Rust refuse an output that is the input in their file functions. `zxc.WithMaxOutputSize(n)` in Go and `maxOutputSize` in Node.js and WASM refuse a size declared by an untrusted footer before allocating it.
- **Node.js (#580):** the package now needs Node.js `^20.17.0` or `>=22.9.0`.
- **Rust, Go, Python, Node.js and WASM moved to context parameters (#546),** with the dictionary pinning dropped now that the library copies dictionaries. An out-of-range level is now an error in Go, Python, Node.js and WASM.
- **Rust (#545):** `compress_bound()`, `compress_block_bound()` and `decompress_block_bound()` return `usize` instead of `u64`, and `zxc-compress-sys` follows the C API.
- **Go (#533):** a handle dropped without `Close` no longer leaks native memory or a `FILE*`, and `OpenBytes` no longer crashes the process once the garbage collector finds it still pinned. `Close` remains required. Thanks to @Vladexy88x.
- **Go and Rust (#546):** a failed file operation leaves an existing output file intact.
- **Release codename (#560):** exposed in Go, Python, Rust and WASM.

## Portability & Build

- **Windows kernel-mode library (#513):** `contrib/windows-kernel` builds the buffer API as `zxc_km.lib` from the unmodified core sources, with a self-test driver and a CI job. It is the counterpart of `contrib/linux-kernel`. Contributed by @jeanga.
- **Wider CI coverage (#543, #556):** the Debian release architectures are required (armhf, ppc64le, s390x, riscv64, loong64), with ports such as hppa, m68k and sh4 in a non-required tier. New targets include Arch Linux, AlmaLinux 9, Amazon Linux 2023 on ARM64, FreeBSD 15.1, x86_64 APX and Clang 23.
- **Scalar fuzzing (#537):** fuzz targets also cover the scalar paths, for platforms without SIMD.
- **CMake defaults to `Release` (#529)** for top-level projects with no build type or optimization flag. Meson warns when built as an unoptimized subproject.
- **Ubuntu 26.04 and static analysis (#576):** CI follows the new `ubuntu-latest`, and the CLI keeps `errno` and removes the created file when `fdopen` fails.
- **Shared library file name:** it now starts with the soname number, as in `libzxc.so.6.0.0`, instead of carrying the release number. On macOS, the current version therefore no longer falls below the compatibility version. `pkg-config` still reports `1.0.0`.
- **Third-party notices (#587):** the rapidhash MIT notice moves from `LICENSE` to `THIRD_PARTY_NOTICES`, so `LICENSE` is BSD-3-Clause alone. The packages ship both.

## Reliability

- **Decompression tail pad (#564):** `ZXC_DECOMPRESS_TAIL_PAD` is recomputed from the real bounds of the decoder, 2084 bytes instead of 2112. `zxc_decompress_block_bound()` follows.
- **`FILE*` engine (#578):** a read error on the input now fails instead of ending the stream. After a corrupt block, the output is exactly the blocks before it, whatever order the threads finished in.

## Security

- Hardened dictionary training against size overflow, >4 GiB offset truncation, NULL samples and a resulting divide-by-zero. Compression and decompression are not affected. ([GHSA-6r4j-7r6c-xf94], #590). Reported by @ccsimplyspolit.

## Documentation

- **libzxc.org (#512):** a new website with documentation, benchmark comparisons per processor and the API reference, built from the published release.
- **Throughput over a link (#530)** replaces the effective throughput metric. It accounts for transfer and decoding overlapping, and shows where each codec leads as bandwidth grows.
- **WHITEPAPER and README rewritten and condensed (#540).**
- **MIGRATION:** the C API guide, with a call-by-call table and every behaviour change.

## Acknowledgements

Thanks to **@Vladexy88x** for finding and fixing the CLI data-loss bug (#550, #555) and the Go handle leaks (#533), to **@jeanga** for the Windows kernel-mode library (#513) and continued testing, and to **@GeekQAQ** for the context report (#532).

Thanks to **@chmike**, author of zxc-go, a native Go encoder and decoder that needs no cgo, and whose suggestion started the seekable in-place work (#562).

A 1.0 is also the moment to thank those it stands on: **@MarcinZukowski** for PivCo-Huffman, **@rygorous** for the breakdown of its merge operations, **@inikep** (lzbench) and **@powturbo** (TurboBench) for the independent benchmarks, and **@nuberchardzer1** for the Python binding.

## Changelog

- api: Honor -T as worker count (#561)
- api: Add zxc_version_codename() (#560)
- api: Move settings from option structs to context parameters (#546)
- api: Cleans up public API, soversion 6 (#545)
- api: Reject non-zero reserved header fields (#547)
- fix: Reject wrapped corpus sizes in dictionary training (#590)
- fix: Bindings - verify checksums by default on decode (#580)
- fix: Wrapper Go - release native resources of handles dropped without Close (#533)
- fix: Correct decompression tail pad to 2084 (#564)
- perf: Decodes seekable ranges in place and batches multi-threaded jobs by size (#562)
- cli: Keeps input files by default, adds --rm to remove them (#558)
- cli: Refuse an output that is the input under another name (#555)
- cli: Preserves file metadata and refines output handling (#539)
- cli: Stop losing data on failed or interrupted runs (#578)
- cli: Reorder -V banner, version before arch (#559)
- cli: Remove a symlink input, not its target (#557)
- cli: Include byte order and architecture in version output (#535)
- build: Exclude language-specific wrapper tests from Snyk analysis (#542)
- build: Fix CI failures on ubuntu-latest (26.04) (#576)
- build: Split third-party notices from LICENSE (#587)
- build: Rename wrappers to bindings (#581)
- build: Bump pytest from 9.1.1 to 9.2.0 in /wrappers/python (#571)
- build: Bump cibuildwheel from 4.3.1 to 4.3.5 in /wrappers/python (#573)
- build: Bump vitest from 5.0.3 to 5.0.5 in /wrappers/nodejs (#570)
- build: Bump cc from 1.7.0 to 1.10.0 in /wrappers/rust (#569)
- build: Bump libc from 0.2.190 to 0.2.191 in /wrappers/rust (#567)
- build: Bump filelock from 3.29.0 to 4.2.4 in /wrappers/python/requirements (#552)
- build: Bump setuptools from 84.0.0 to 84.1.0 in /wrappers/python/requirements (#551)
- build: Bump certifi in /wrappers/python/requirements (#544)
- build: Expand and reorganize platform coverage (#543)
- build: Use standard arm64 runners for pull request benchmarks (#536)
- build: Default to Release build type for top-level CMake projects (#529)
- build: Bump cibuildwheel from 4.2.1 to 4.3.1 in /wrappers/python (#519)
- build: Bump scikit-build-core from 1.1.0 to 1.1.1 in /wrappers/python (#522)
- build: Bump cc from 1.5.1 to 1.7.0 in /wrappers/rust (#518)
- build: Bump libc from 0.2.189 to 0.2.190 in /wrappers/rust (#517)
- build: Bump vitest from 5.0.2 to 5.0.3 in /wrappers/nodejs (#520)
- build: Update lzbench source to original upstream repository
- build: Add x86_64 APX tier and Clang 23 support (#556)
- portability: Windows kernel-mode library for drivers (zxc_km.lib) (#513)
- doc: Add AI tool usage policy (#596)
- doc: Add 1.0.0 upgrade section to MIGRATION
- doc: Condense and refine README and API documentation (#540)
- doc: Replace effective throughput metric with link throughput chart (#530)
- doc: Refresh benchmarks
- doc: Swap Go binding to zxc-go
- doc: Add hyperlinks to contributors in README
- doc: Rewrite and condense WHITEPAPER.md for clarity
- doc: Adds website with automated Cloudflare deployment (#512)
- misc: Raise go directive to 1.22, test 1.22 and stable (#594)
- misc: Adds release/X.Y maintenance branch workflow (#589)
- misc: Reorganize tests into subdirectories (#548)
- misc: Standardizes unsigned integer literal suffixes (#531)
- misc: Add scalar fallback fuzzing targets (#537)
- misc: Add GitHub star button, fix doc wording (#588)
- misc: Bump codecov/codecov-action from 7.0.0 to 7.1.1 (#586)
- misc: Bump github/codeql-action/upload-sarif (#585)
- misc: Bump msys2/setup-msys2 from 2.32.0 to 2.33.0 (#584)
- misc: Bump pypa/gh-action-pypi-publish from 1.14.2 to 1.14.3 (#583)
- misc: Bump actions/upload-artifact from 7.0.1 to 7.0.2 (#582)
- misc: Disable native arch for scan-build analysis (#579)
- misc: Bump github/codeql-action/analyze from 4.38.3 to 4.39.1 (#574)
- misc: Bump cross-platform-actions/action from 1.5.0 to 1.7.0 (#572)
- misc: Bump actions/attest-build-provenance from 4.1.1 to 4.2.2 (#568)
- misc: Bump actions/setup-python from 7.0.0 to 7.1.0 (#566)
- misc: Bump rust-lang/crates-io-auth-action from 1.0.5 to 1.0.6 (#565)
- misc: Bump marked from 18.1.0 to 18.1.2 in /site (#575)
- misc: Parallelize valgrind per test (#577)
- misc: Use BUILD_ONLY list (#563)
- misc: Run benchmarks on draft PRs
- misc: Replaces magic numbers with named constants (#554)
- misc: Rename GLO and GHI block types to SPL and PAK (#538)
- misc: Remove .github from export-ignore in .gitattributes
- misc: Restrict local preview server to localhost and rename cache key (#528)
- misc: Bump github/codeql-action/init from 4.38.2 to 4.38.3 (#524)
- misc: Bump oss-fuzz-base/base-builder in /.clusterfuzzlite (#516)
- misc: Bump marked from 18.0.14 to 18.1.0 in /site (#521)
- misc: Bump github/codeql-action/upload-sarif (#523)
- misc: Bump actions/download-artifact from 8.0.1 to 8.0.2 (#515)
- misc: Bump actions/setup-node from 6.4.0 to 7.1.0 (#514)
- misc: Bump ossf/scorecard-action from 2.4.3 to 2.5.0 (#525)

Full Changelog: v0.15.0...v1.0.0

## Assets

| Name | Size | Downloads |
| --- | --- | --- |
| checksums.sha256 | 733 B | 7 |
| checksums.sha256.minisig | 311 B | 3 |
| multiple.intoto.jsonl | 49.6 KB | 3 |
| zxc-1.0.0-linux-arm64.tar.gz | 315.6 KB | 7 |
| zxc-1.0.0-linux-x86_64.tar.gz | 642.6 KB | 12 |
| zxc-1.0.0-macos-arm64.tar.gz | 258.6 KB | 2 |
| zxc-1.0.0-sbom.spdx.json | 2.1 KB | 1 |
| zxc-1.0.0-windows-arm64.zip | 419.3 KB | 2 |
| zxc-1.0.0-windows-x86_64.zip | 995.5 KB | 17 |
| zxc-1.0.0.tar.gz | 866.1 KB | 9 |
| zxc-1.0.0.tar.zxc | 899.8 KB | 2 |

## 导航

- 项目页：[[10-项目/github.com_18ee826f]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`开发者工具`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
