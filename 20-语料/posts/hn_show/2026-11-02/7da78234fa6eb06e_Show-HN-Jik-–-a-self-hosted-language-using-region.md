---
type: "corpus"
item_id: "7da78234fa6eb06e"
title: "Show HN: Jik – a self-hosted language using region-based memory management"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50329086"
project_url: "https://github.com/jik-lang/jik"
author: "scorched_soy"
published_at: "2026-11-01T19:51:54Z"
captured_at: "2026-11-02T09:37:22+08:00"
lang: "en"
kind: "post"
topic: "开发者工具"
shard: "2026-11-02"
pub_day: "2026-11-01"
tags:
  - 语料
  - hn_show
  - author_scorched_soy
  - story_50329086
  - show_hn
metrics: {"points": 3, "comments": 0, "engagement_velocity": 3}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:3d"
---

# Show HN: Jik – a self-hosted language using region-based memory management

> [!info] 一句话导读
> Compiler for the Jik programming language.

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50329086>
> 指标：点赞=3 · 评论=0 · engagement_velocity=3
> 作者：scorched_soy　|　发布：2026-11-01T19:51:54Z
> 项目链接：<https://github.com/jik-lang/jik>
> 采集：2026-11-02T09:37:22+08:00　|　id：`7da78234fa6eb06e`

## 正文

# jik-lang/jik

Compiler for the Jik programming language.

- Stars: 6
- Forks: 0
- Watchers: 6
- Open issues: 1
- License: MIT License
- Homepage: https://jik-lang.org
- Default branch: main
- Created: 2026-04-25T11:13:36Z

## Languages

- Batchfile
- C
- JavaScript
- Makefile

## Topics

- c
- compiler
- jik
- jik-lang
- language-design
- programming-language
- region-based-memory
- statically-typed
- transpiler

## Top Contributors

- radovanhorvat (79 contributions)

---

## README

# Jik

_A readable language with region-based memory management that compiles to C._

## Try Jik in GitHub Codespaces
_Open a ready-to-use Jik development environment._

---

## What is Jik?

Jik is a statically typed programming language designed to be readable and easy to learn. It uses a straightforward source-to-C compilation model, region-based memory management
and avoids garbage collection.

Jik provides practical language features such as type inference, optional type annotations, vectors, dictionaries, options, variants, and more, together with a small standard library. The
result is a language that keeps common code concise and expressive, while still compiling to readable and predictable C.

Jik's memory model is one of its defining ideas. Instead of garbage collection or manual heap allocation, composite values are allocated into explicit regions that determine their lifetime, with language rules that prevent invalid cross-region use.

## Examples

These examples provide a quick tour of common Jik features.

 Parsing a config

```jik
use "jik/string"

func main():
    text := "host = localhost\nport = 8080\nmode = dev\n"
    settings: Dict[String]

    for line in string::split(text, "\n", _):
        if line == "":
            continue
        end
        parts := string::split(line, "=", _)
        if len(parts) == 2:
            key := string::trim(parts[0], _)
            value := string::trim(parts[1], _)
            settings[key] = value
        end
    end

    host := settings["host"]
    port := settings["port"]
    if host is Some and port is Some:
        println("connecting to ", host?, ":", must string::to_int(port?))
    end
end
```

 Error handling

```jik
throws func safe_div(x, y):
    if y == 0.0:
        fail("division by zero")
    end
    return x / y
end

func show_div(x, y):
    try value := safe_div(x, y):
        println(x, " / ", y, " = ", value)
    except:
        println("cannot divide ", x, " by ", y, ": ", error_msg())
    end
end

func main():
    show_div(12.0, 3.0)
    show_div(7.0, 0.0)
    println("forced result: ", must safe_div(8.0, 2.0))
end
```

 Working with variants

```jik
variant Packet:
    ID: int
    TEXT: String
    BYTES: Vec[int]
end

func inspect(pkt):
    if pkt is Packet.ID:
        pkt[Packet.ID] = pkt[Packet.ID] + 1
        println("next id: ", pkt[Packet.ID])
    end

    match pkt:
        case Packet.ID{id}:
            println("id packet: ", id)
        case Packet.TEXT{text}:
            println("text packet: ", text)
        case Packet.BYTES{bytes}:
            println("bytes packet, len = ", len(bytes), ", first = ", bytes[0])
    end
end

func main():
    pkt := Packet.ID{41}
    println("raw id: ", pkt[Packet.ID])
    inspect(pkt)

    inspect(Packet.TEXT{"hello"})
    inspect(Packet.BYTES{[10, 20, 30]})
end
```

 Newton method

```jik
use "jik/math"

struct NewtonResult:
    root: double
    converged: bool
    xs: Vec[double]
end

func solve(x0: double, tol: double, max_steps: int, r: Region) -> NewtonResult:
    xs := [0 of 0.0][r]
    x := x0
    push(xs, x)

    for step = 0, max_steps:
        fx := math::cos(x) - x
        if math::abs(fx) <= tol:
            return NewtonResult{root = x, converged = true, xs = xs}[r]
        end
        x = x - fx / (-math::sin(x) - 1.0)
        push(xs, x)
    end

    return NewtonResult{root = x, converged = false, xs = xs}[r]
end

func main():
    res := solve(1.0, 1e-12, 20, _)
    println("root: ", res.root)
    println("steps: ", len(res.xs) - 1)
    println("converged: ", res.converged)
end
```

For more examples, look in the examples directory or inside the Jik test suite.

## Showcase

- Play Missile Defence — a Jik game using the Raylib 6.0 wrapper.
 - Source code
 - Note: the browser demo is a separate WebAssembly build

## Quick start

To start programming in Jik:

- download the latest release for your platform
- extract the release archive
- from the extracted directory, run `jik help` to confirm the executable works
- (optional) add the extracted directory to `PATH`
- if you plan to use `jik run` or `jik build`, either pass the compiler name with `--cc` or set `JIK_CC`, for example to `clang` or `gcc`
 - Windows: For a simple GCC setup, download from WinLibs, and add its `bin` directory to `PATH`
- create a file `hello.jik`:

```jik
func main():
    println("Hello, Jik!")
end
```

- run it: `jik run hello.jik`
- generate C output: `jik tran hello.jik`
- build an executable: `jik build hello.jik`

Only `clang` and `gcc` host compilers were tested. MSVC was not tested.

## Building Jik from source

To build Jik from source, you will need `make` and a C compiler:

- download the Jik repository and navigate to the root
- run `make`

Additionally, to run the Jik test suite:

- run `make test`

Note that MSVC was not tested and is not the default build path in this repository

## Further reading

- Documentation
- Language overview
- Region-based memory management
- CLI reference
- Standard library documentation
- Jik packages
- Official Jik website

---

### Repository layout

- `src/` - compiler source
- `jiklib/` - Jik standard library modules
- `support/` - Jik support library
- `test/` - test suite
- `docs/` - design notes and language documentation
- `examples/` - examples of Jik code
- `assets/` - assets (logo, etc)
- `scripts/` - dev scripts
- `tools/` - tools (syntax highlighting, etc)

### Roadmap

- **0.1.x - Implementation stabilisation**
 - keep the language syntax stable (intended to be frozen)
 - find and fix bugs in the compiler and in the support library (`core.h`)
 - extend the standard library as needed
 - expand the test suite
 - write real programs in Jik to validate the implementation

- **Later**
 - bootstrapping: rewrite Jik in Jik
 - concurrency support (may be implemented either in the C implementation or during bootstrapping)

# Supremath — Suprematism Art Generator

## 关联链接

- https://jik-lang.org

## 导航

- 项目页：[[10-项目/github.com_14c3bd56]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`开发者工具`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
