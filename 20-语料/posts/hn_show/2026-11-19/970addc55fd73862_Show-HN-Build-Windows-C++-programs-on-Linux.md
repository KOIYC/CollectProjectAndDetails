---
type: "corpus"
item_id: "970addc55fd73862"
title: "Show HN: Build Windows C++ programs on Linux"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50553490"
project_url: "https://github.com/abidanBrito/build-windows-on-linux"
author: "abidanbrito"
published_at: "2026-11-18T22:50:56Z"
captured_at: "2026-11-19T09:43:31+08:00"
lang: "en"
kind: "post"
topic: "开发者工具"
shard: "2026-11-19"
pub_day: "2026-11-18"
tags:
  - 语料
  - hn_show
  - author_abidanbrito
  - story_50553490
  - show_hn
metrics: {"points": 3, "comments": 0, "engagement_velocity": 3}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:3d"
---

# Show HN: Build Windows C++ programs on Linux

> [!info] 一句话导读
> abidanBrito/build-windows-on-linux

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50553490>
> 指标：点赞=3 · 评论=0 · engagement_velocity=3
> 作者：abidanbrito　|　发布：2026-11-18T22:50:56Z
> 项目链接：<https://github.com/abidanBrito/build-windows-on-linux>
> 采集：2026-11-19T09:43:31+08:00　|　id：`970addc55fd73862`

## 正文

# abidanBrito/build-windows-on-linux

Cross-compiling C++ Windows executables from Linux.

- Stars: 0
- Forks: 0
- Watchers: 0
- Open issues: 0
- License: MIT License
- Default branch: main
- Created: 2026-11-17T17:45:00Z

## Languages

- C++
- CMake

## Topics

- cross-compilation
- llvm-mingw
- mingw-w64
- wine
- xwin

## Top Contributors

- abidanBrito (22 contributions)

---

## README

# build-windows-on-linux

Build
C++23
CMake 3.25+
License: MIT

Cross-compiling C++ Windows programs from Linux with four different toolchains.

There are two sample programs, tested under Wine:

- `hello`: a console hello world, using `std::println`.
- `window`: a basic Win32 GUI window.

## Toolchains

| Preset | Compiler | C++ library | SDK / CRT | ABI |
|-----------------|------------|-------------|---------------------|-------|
| `mingw-clang` | host clang | libstdc++ | mingw-w64 (UCRT) | GNU |
| `mingw-gcc` | GCC | libstdc++ | mingw-w64 (UCRT) | GNU |
| `llvm-mingw` | clang | libc++ | mingw-w64 (UCRT) | GNU |
| `xwin-clang-cl` | clang-cl | MSVC STL | Microsoft SDK + CRT | MSVC |

All of them link statically, so that no extra DLLs (or `WINEPATH` shenanigans) are needed. In theory, `xwin-clang-cl` can also link libraries built with Visual Studio.

## Install

### Ubuntu

```sh
sudo apt install cmake ninja-build wine
```

Ubuntu's own `clang` and `g++-mingw-w64-x86-64` are too old for C++23 (` `, MSVC STL), so get them elsewhere:

- **Clang**: from apt.llvm.org, e.g. `wget https://apt.llvm.org/llvm.sh && sudo bash llvm.sh 23`
- **MinGW GCC**: from Homebrew, with `brew install mingw-w64`, then add `$(brew --prefix mingw-w64)/toolchain-x86_64/bin` to your `PATH`
- **llvm-mingw** and **xwin**: grab the release tarballs from llvm-mingw (extracted to `/opt/llvm-mingw/llvm-mingw-ucrt`) and xwin

See `build.yml` for the exact steps.

### Arch

```sh
sudo pacman -S cmake ninja clang lld llvm mingw-w64-gcc wine
yay -S llvm-mingw-w64-toolchain-ucrt-bin xwin
```

### Microsoft SDK & CRT

This is only needed for `xwin-clang-cl`:

```sh
sudo mkdir /opt/xwin && sudo chown $USER: /opt/xwin
xwin --accept-license splat --output /opt/xwin
```

## Build & run

```sh
cmake --preset mingw-clang
cmake --build --preset mingw-clang

wine build/mingw-clang/hello.exe
wine build/mingw-clang/window.exe
```

> [!TIP]
> `cmake --list-presets` and `cmake --build --list-presets` show all available CMake presets.

## Some notes

These are already accounted for, but they're worth knowing:

- With `libstdc++`, `std::print` needs to link `stdc++exp`, as it lives in `libstdc++`'s experimental library.
- Linking `libstdc++` statically also requires `winpthread`, linked after `stdc++`. Note that `g++` adds it automatically, but `clang` doesn't.
- `mingw` only uses `wWinMain` as the entry point when linking with `-municode`, whereas `MSVC` picks it up on its own.
- `xwin-clang-cl` needs a recent clang (19+), since MSVC STL refuses older versions.

# RailCall — 40-Trillion-Parameter Intelligence: Same or Better Quality Than Frontier Models, 90% Less Expensive

## 关联链接

- https://apt.llvm.org/llvm.sh

## 导航

- 项目页：[[10-项目/github.com_a71c7086]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`开发者工具`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
