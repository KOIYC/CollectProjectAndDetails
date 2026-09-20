---
type: "corpus"
item_id: "3ea90c193883baf3"
title: "Show HN: Pico, a small register-based scripting language I wrote in C"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=48344259"
project_url: "https://github.com/the0cp/pico"
author: "vaergawdd"
published_at: "2026-05-31T09:31:01Z"
captured_at: "2026-09-21T02:52:47+08:00"
lang: "en"
kind: "post"
topic: "开发者工具"
shard: "2026-09-21"
pub_day: "2026-05-31"
tags:
  - 语料
  - hn_show
  - author_vaergawdd
  - story_48344259
  - show_hn
metrics: {"points": 2, "comments": 1, "engagement_velocity": 2}
comments_count: 1
comments_total: 1
discovered_via: "hn:show_hn:144d"
---

# Show HN: Pico, a small register-based scripting language I wrote in C

> [!info] 一句话导读
> A small, compact, register-based scripting language and virtual machine implemented in C. Inspired by clox.

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=48344259>
> 指标：点赞=2 · 评论=1 · engagement_velocity=2
> 作者：vaergawdd　|　发布：2026-05-31T09:31:01Z
> 项目链接：<https://github.com/the0cp/pico>
> 采集：2026-09-21T02:52:47+08:00　|　id：`3ea90c193883baf3`

## 正文

# the0cp/pico

A small, compact, register-based scripting language and virtual machine implemented in C. Inspired by clox.

- Stars: 6
- Forks: 0
- Watchers: 6
- Open issues: 0
- License: GNU General Public License v3.0
- Default branch: master
- Created: 2025-07-16T12:05:39Z

## Languages

- C
- CMake
- Shell

## Topics

- c
- compiler
- compiler-design
- gcc
- interpreter
- language
- programming-language
- scripting-language
- virtual-machine

## Top Contributors

- the0cp (154 contributions)

---

## README

# PiCo

A small, compact scripting language and virtual machine implemented in C. pico includes a compiler, virtual machine, REPL, and a set of core modules for working with values, objects, and I/O.

## Features

- Register-based bytecode VM
- REPL
- Functions and closures
- Classes and methods
- Modules
- Lists, maps, strings, and slicing
- Small standard library
- Manual / automatic GC modes

See the included `manual.md` for a detailed language reference and usage examples: https://github.com/the0cp/pico/blob/master/manual.md

## What it looks like

```javascript
# A tiny PiCo demo: 

func slug(s) {
    return s.trim().lower().replace(" ", "-");
}

func badge(s) {
    return "[" + s + "]";
}

func makeCounter(prefix) {
    var n = 0;

    return func(name) {
        n++;
        return "${prefix}-${n}: ${name}";
    };
}

var next = makeCounter("demo");
var topics = [" Register VM ", " Pipe Operator ", " Path Join "];

for (var topic : topics) {
    var name = topic |> slug |> badge;
    print next(name);
}

print "path: ${"examples" / "data" / "sample.txt"}";
print "slice: ${"register-vm"[0:8]}, reverse: ${"PiCo"[::-1]}";

$> echo hello from the host shell
print "shell exit code = ${_exit_code}";
```

## Examples

More examples are available in `examples/`.

Try more examples:

```sh
./build/debug/pico examples/tour.pcs
./build/debug/pico examples/file_indexer.pcs
./build/debug/pico examples/modules/main.pcs
# ...
```

## Building

Requirements: gcc and CMake. The code uses GCC-specific techniques such as computed goto / dispatch table, so GCC is required. On Windows, GCC can be installed through MinGW-w64, Chocolatey, or MSYS2.

Clone the repo:

```sh
git clone --recursive https://github.com/the0cp/pico.git
```

Configure and build a debug version:

```sh
cmake --preset debug
cmake --build --preset debug
```

Configure and build a release version:

```sh
cmake --preset release
cmake --build --preset release
```

On Windows:

```sh
cmake --preset release-windows
cmake --build --preset release-windows
```

The executable is generated under the corresponding build directory, for example:

```text
build/debug/pico
build/release/pico
build/release-windows/pico.exe
```

## Installing

Install PiCo to your local user prefix:

```sh
cmake --preset release
cmake --build --preset release
cmake --install build/release --prefix ~/.local
```

Make sure `~/.local/bin` is in your PATH:

```sh
export PATH="$HOME/.local/bin:$PATH"
```

Then run PiCo from anywhere.

To install system-wide:

```sh
sudo cmake --install build/release
```

## Testing

Run the test suite with *CTest*:

```sh
ctest --preset debug --output-on-failure
```

or for release:

```sh
ctest --preset release --output-on-failure
```

## Usage

Run the interactive REPL:

```sh
pico
```

Run a script:

```sh
pico path/to/script.pcs
```

Pico scripts can also be executed directly with a Unix shebang:

```sh
#!/usr/bin/env pico

print("hello from Shebang");
```

Make it executable and run it:

```sh
chmod +x hello.pcs
./hello.pcs
```

Check `manual.md` for language syntax, built-in functions, and examples.

## License

This project is distributed under the GNU GPL v3. See `gpl-3.0.txt` for details.

## 评论（1/1）

> **vaergawdd** · 2026-05-31T09:35:20.000Z　
> Hi HN,
> I wrote this PiCo, a small register-based scripting language and virtual machine in C.
> This is a learning project. In the early stage I read Crafting Interpreters and learned a lot. Then I gradually changed the design toward register-based VM, module system, standard library, GC controls and etc.
> It is a small toy language, not a production-ready tool. I am making it complete enough that someone can play with it.
> I’d be happy to hear feedback.

## 关联链接

- https://github.com/the0cp/pico.git
- https://github.com/the0cp/pico/blob/master/manual.md

## 导航

- 项目页：[[10-项目/github.com_75f16477]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`开发者工具`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
