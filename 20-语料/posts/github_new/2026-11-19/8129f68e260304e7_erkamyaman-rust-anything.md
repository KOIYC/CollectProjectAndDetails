---
type: "corpus"
item_id: "8129f68e260304e7"
title: "erkamyaman/rust-anything"
source: "github_new"
source_name: "GitHub 新星仓库"
url: "https://github.com/erkamyaman/rust-anything"
project_url: "https://npmjs.com/package/rust-anything"
author: "erkamyaman"
published_at: "2026-11-16T12:10:36Z"
captured_at: "2026-11-21T15:06:21+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-11-19"
pub_day: "2026-11-16"
tags:
  - 语料
  - github_new
  - Rust
  - created:>2026-11-07
metrics: {"stars": 6845, "forks": 542, "open_issues": 2}
comments_count: 0
comments_total: 0
discovered_via: "github:14d"
---

# erkamyaman/rust-anything

> [!info] 一句话导读
> <img src="docs/assets/logo.png" width="160" height="160" alt="The rust-anything crab">

> [!meta]- 语料信息（点开展开）
> 来源：GitHub 新星仓库（post）
> 原帖：<https://github.com/erkamyaman/rust-anything>
> 指标：stars=6845 · forks=542 · open_issues=2
> 作者：erkamyaman　|　发布：2026-11-16T12:10:36Z
> 项目链接：<https://npmjs.com/package/rust-anything>
> 采集：2026-11-21T15:06:21+08:00　|　id：`8129f68e260304e7`

## 正文

rust-anything

English · Türkçe · Українська · 简体中文 · 繁體中文 · Deutsch · Français · Русский · 日本語 · 한국어 · Azərbaycanca · Oʻzbekcha · Қазақша · Кыргызча · Türkmençe · Татарча · ئۇيغۇرچە · Português · Tiếng Việt

Rewrite your app in Rust, and prove it still behaves the same.
Point it at your app: it records what the original does, your coding agent writes the Rust one piece at a time,
and every piece is checked against that recording before it moves on. It doesn't translate code; it proves the rewrite.

Install · Releases · Claude Code plugin · MCP Registry · Real-world ports · FAQ
Languages · How it works · Whole apps · Sponsors · MIT
Made in Türkiye 🇹🇷 by erKam Yaman · ❤️ Sponsor me · Sponsored by  CodeRabbit

New in 2.0: Prettier, ported to Rust. 19x faster · 15,837 of 17,224 recorded runs fully in Rust · every run byte-identical

  Prettier against its Rust port on 59 real files from ms, Fuse.js and json-server (Apple M4). Same output, byte for byte. How it was measured.

PHP and C#: record, replay and the front door today; unit ports come next.

      Record
      record runs the original on generated edge cases, semantic traps and your own inputs, and saves what it returns or throws.

      Port
      bridge generates the Rust crate and a wrapper, so callers keep the original API. You or your agent write the Rust.

      Check
      diff replays every recorded case against the Rust, and nothing ships until they all match and gate passes.

      Lift
      When replay passes with no fallback and every unit passes gate, app lift makes it a pure Rust app. The original is never touched.

**Rewrite your whole app in Rust, one piece at a time.** rust-anything records what your
Node.js (TypeScript/JavaScript), Python, C, Go, Ruby, Java or Kotlin app does today, then checks every piece of the
Rust rewrite against that recording before it moves on, until the app is pure Rust. CLIs, HTTP
servers and libraries; your coding agent (or you) writes the Rust. It is built on
[napi-rs](https://github.com/napi-rs/napi-rs), [PyO3](https://github.com/PyO3/pyo3) and
[wasm-bindgen](https://github.com/wasm-bindgen/wasm-bindgen), which carry the calls between your
language and Rust; rust-anything decides what to move and proves it matches. It can only catch what the
recording covers: see [What it can't catch](docs/how-it-works.md#what-it-cant-catch). Whole tools
and servers, or only the slow part, one hot path at a time:

| Real project, same output as the original | Original | With rust-anything |
| --- | ---: | ---: |
| [Prettier](docs/real-world.md#prettier) 3.6.2, 2,360 JS/TS files from the command line | 128.6 s | **6.9 s: 19x faster** |
| Prettier, 6,305 Markdown files from the command line | 352 s | **22.5 s: 15.6x faster** |
| [json-server](docs/real-world.md#json-server), a whole Node server: memory at idle | 74 MB | **3.5 MB**, one 5.3 MB binary |
| json-server, from start to first response | 79 to 85 ms | **8 to 10 ms** |
| [Fuse.js](docs/real-world.md#fusejs) search over 50,000 strings, per query | 91.2 ms | **2.8 ms: 32x faster** |

Prettier: 15,837 of 17,224 recorded runs format fully in Rust across 10 languages (JavaScript,
TypeScript, JSX, JSON, GraphQL, YAML, Markdown, CSS, SCSS, Less), and all 17,224 match Prettier
byte for byte, since anything not ported yet falls back to Prettier. json-server: 514/514
recorded HTTP cases match on a pure Rust binary. Measured on an Apple M4, two runs each, every
output compared before timing ([details](docs/real-world.md)). Calling Rust once per small
function is usually *slower* than a JIT; rust-anything finds the loop worth moving, and moves it. Against
C the win is safety, not speed: [ffmpeg's libavutil](docs/real-world.md#ffmpeg) ported to Rust
matches all 226,447 recorded calls and runs at about C's speed (18 of 42 benchmarks even, 8
faster, 16 slower by 3 to 40%).

  json-server, a whole Node server, lifted to a pure Rust binary (Apple M4). How it was measured.

> rust-anything is an independent project, not affiliated with or endorsed by the Rust Project
> or the Rust Foundation. "Rust" is a trademark of the Rust Foundation.

> [!WARNING]
> `record` and `app record` run your original code, calling each function (or the whole app) on
> many generated inputs, and `app record` runs every case twice. `diff`, `gate` and `app replay`
> run the same cases again, on the port or the original. Code that writes files, talks to a
> database or calls the network does that once per case. Run them on a copy of the project, with a
> test database and no production credentials in the environment.

## Quick start

Paste this into Claude Code, Codex, Cursor, Gemini CLI or OpenCode and let your agent install it:

```text
Install rust-anything: run `cargo install rust-anything`, then `rust-anything setup`.
Tell me when to restart you.
```

Or yourself:

```sh
cargo install rust-anything   # from crates.io
rust-anything setup           # registers it with Claude Code, Codex, Cursor, Gemini CLI and OpenCode
```

No Rust toolchain yet? Prebuilt binaries for macOS, Linux and Windows are attached to each
[GitHub release](https://github.com/erkamyaman/rust-anything/releases), and for JavaScript
projects `npm install -g rust-anything` installs the same binary.

In Claude Code you can also install it as a plugin (the MCP server and the skill; the CLI above
must be on your `PATH`):

```text
/plugin install rust-anything --marketplace erkamyaman/rust-anything
```

`setup` adds the MCP server to each agent it finds and installs the workflow skill where the agent
reads skills. It keeps your other settings, is safe to run again, and `--remove` undoes it.
Then ask your agent, for example:

- *"Rewrite this CLI in Rust with rust-anything, end to end, and prove it behaves the same."*
- *"This search feels slow. Profile it with rust-anything and move the hot loop to Rust."*
- *"Plan a migration of `src/parser/` to Rust with rust-anything; port the first unit and prove it."*
- *"Bench the Rust port in `rust/text-rs` against the original and tell me whether to ship it."*

### Works with

| Agent | `rust-anything setup` adds |
| --- | --- |
| Claude Code | MCP server in `~/.claude.json`, skill in `~/.claude/skills/` |
| Codex | MCP server in `~/.codex/config.toml`, skill in `~/.codex/skills/` |
| Cursor | MCP server in `~/.cursor/mcp.json` |
| Gemini CLI | MCP server in `~/.gemini/settings.json` |
| OpenCode | MCP server in `~/.config/opencode/opencode.json` (`mcp.servers`), skill in `~/.config/opencode/skills/` |
| Any other MCP client | add `rust-anything mcp` as a stdio server by hand (see [Install](docs/install.md#install)) |

Before changing a file that exists, `setup` saves a copy beside it (`<file>.rust-anything.bak`); `--no-backup` skips the copy.

To wire OpenCode up by hand, put the server in `~/.config/opencode/opencode.json` (`command` is
the whole argv) and copy [`skills/rust-anything/`](./skills/rust-anything) to
`~/.config/opencode/skills/rust-anything/`:

```json
{
  "mcp": {
    "servers": {
      "rust-anything": { "type": "local", "command": ["rust-anything", "mcp"] }
    }
  }
}
```

Or run the steps yourself:

```sh
rust-anything profile . -- node bench.mjs              # what is hot, and who calls it
rust-anything bridge . src/fuzzy.ts --batch fuzzyScore:text
# write src/port.rs (or let your agent), then:
rust-anything record rust/fuzzy-rs && rust-anything build rust/fuzzy-rs
rust-anything diff rust/fuzzy-rs                       # every recorded case must match
rust-anything fuzz rust/fuzzy-rs --time 60 --keep      # fresh inputs: what the recording missed
rust-anything bench rust/fuzzy-rs                      # faster? the verdict says
rust-anything gate rust/fuzzy-rs                       # done means this passes
```

rust-anything does not translate code: your coding agent (Claude Code, Codex, Cursor, OpenCode, ...) or you write
the Rust. rust-anything supplies what an agent cannot guess reliably: where the time goes, what to port
first and in which order, a bridge so the rest of the code calls the Rust with its API unchanged,
the exact behavior the port must match, a safe way to ship it, and a gate that says when a port is
done.

Same output is not enough. Record what the app sends too, and a rewrite that mails twice fails:

  A real run of app record --effects and app replay. See Side effects.

## Languages

| Language | Unit | Bridge | Recorded and replayed by |
| --- | --- | --- | --- |
| TypeScript/JavaScript | folder or file | napi-rs or wasm-bindgen with a generated binary wire; classes and async included | Node, running the `.ts` sources |
| Python | package or module | PyO3 (abi3), direct conversion, typed exceptions | Python, importing the original |
| C | `.c` file | `extern "C"` functions with the original names and a header | the original compiled to a shared library, called through ctypes, one fork per case |
| Go | package | typed cgo calls and a generated binary wire, in a package with the original API | a generated Go driver, built as its own module |
| Ruby | file or folder of module functions | a magnus extension under the original modules | a generated Ruby driver |
| Java | package of `public static` methods | typed JNI and a generated binary wire, in wrapper classes with the original methods | a generated reflection driver |
| Kotlin | Gradle module of top-level functions and `@JvmStatic` methods | the Java bridge: typed JNI in Java wrapper classes calling the compiled Kotlin statics | a generated reflection driver, with the Kotlin sources compiled by `kotlinc` |
| PHP | folder of functions and `public static` methods | coming next: PHP FFI over a C ABI | whole apps today: `app record`, `app replay` and the front door, for CLIs and servers (`php -S`) |
| C# | folder of `public static` methods | coming next: P/Invoke over a C ABI | whole apps today: `app record`, `app replay` and the front door, for CLIs and ASP.NET servers (`dotnet <app>.dll`) |

Every language except C also gets batch classes (`--batch`): the items cross once and stay in
Rust, and each call runs over all of them on all cores.

The language is detected from the repository (`go.mod`, `pom.xml`, `build.gradle`/`build.gradle.kts`,
a `.csproj` or `.sln`, `pyproject.toml`, `Gemfile`, `composer.json`, `package.json`, else the most
common source files); a Gradle module with `.kt` sources and no `.java` sources is Kotlin, mixed
modules stay Java. `--lang` overrides it. Types come from the source: TS types, Python hints, C, Go,
Java, Kotlin and C# signatures, Ruby YARD tags, PHP types and phpdoc; untyped parameters used as
numbers are inferred as numbers.

For Android, `rust-anything build <crate> --profile android` builds the same JNI library with the
NDK for `arm64-v8a`, `armeabi-v7a` and `x86_64` (or the `--abi` values you pass) and installs it
into `<crate>/jniLibs/<abi>/`; `--api` sets the API level (minimum 26, which the generated Java
runtime needs). It finds the NDK from `ANDROID_NDK_HOME`/`ANDROID_NDK_ROOT` or the SDK, needs the
Rust targets (`rustup target add aarch64-linux-android armv7-linux-androideabi
x86_64-linux-android`), links 64-bit libraries with 16 KB page alignment, and checks that every
JNI entry point is exported. Gradle looks in `src/main/jniLibs` by default, so pass
`--jni-libs app/src/main/jniLibs` or add `<crate>/jniLibs` to `sourceSets.main.jniLibs.srcDirs`.
`rust-anything record <crate> --profile android` runs the original Kotlin unit under ART on a
connected device (adb), dexes the generated driver with `d8` from the SDK's build-tools, and pulls
the results back as the same `cases.jsonl`; `diff <crate> --profile android` replays them against
the `.so` built for the device's ABI. Both need `adb`, a device, `kotlinc`, an SDK with build-tools
and a platform, and `--device <serial>` when more than one device is connected. The profile covers
logic units: Activity/Compose/XML UI, lifecycle and SDK-only classes stay in Kotlin, and each call
crosses JNI, so prefer the generated batch wrappers for hot loops. On a host, `record` and `diff`
keep using the desktop JVM.

For PHP, `analyze` plans a PHP app (Composer packages and PSR-4 autoloading, risks
such as loose comparison and integer overflow into floats, Composer packages mapped to crates),
and a PHP CLI or server can be recorded, replayed and put behind a Rust front door. Porting its
units into Rust through PHP's FFI is the next step ([issue #2](https://github.com/erkamyaman/rust-anything/issues/2)).

C# works the same way: `analyze` reads `.csproj` projects and their NuGet packages
(mapped to crates), resolves `using` directives to folders, and flags what C# does differently
(`decimal`, `dynamic`, LINQ's deferred queries, `Task`, `lock`, reflection). A C# CLI or ASP.NET
server can be recorded, replayed and put behind a Rust front door; porting units through P/Invoke
comes next.

## Learn more

- [How it works](docs/how-it-works.md): the loop, what `bridge` and `analyze` decide, hot paths, what it can't catch, what a real port takes, and keeping up with the original (`map`)
- [Ship a port as a package](docs/packaging.md): maturin wheels and napi-rs per-platform npm packages, with the CI that builds them
- [Port a whole app](docs/whole-apps.md): servers, CLIs and libraries, from the front door to `app lift`
- [Examples and case studies](docs/examples.md): x18n, and real code in six languages
- [Real-world ports](docs/real-world.md): json-server, Fuse.js, vercel/ms, with benchmarks
- [Install, update and develop](docs/install.md): every install method, Windows, and building from source
- [FAQ](docs/faq.md) · [Status](docs/STATUS.md) · [MCP tools](docs/tools.md)

## Sponsors

  rust-anything is free and open source. If it helps your work, please consider sponsoring it.
  Your support keeps development going.

## Contributing

Issues and pull requests are welcome; [CONTRIBUTING.md](./CONTRIBUTING.md) covers the setup, where
tests go, and how to add a language. Design choices and their reasons are in
[DECISIONS.md](./DECISIONS.md). Case studies of real ports are especially welcome. Please report
security problems privately ([SECURITY.md](./SECURITY.md)), and see the
[code of conduct](./CODE_OF_CONDUCT.md).

## License

[MIT](./LICENSE) © [Erkam Yaman](https://github.com/erkamyaman). Ports and generated code in your repository are yours.

## 关联链接

- https://awesome.re/mentioned-badge.svg
- https://buymeacoffee.com/erkamyaman
- https://coderabbit.link/erkamyaman
- https://crates.io/crates/rust-anything
- https://github.com/AIshihzong/awesome-reverse-engineer-anything
- https://github.com/PyO3/pyo3
- https://github.com/erkamyaman
- https://github.com/erkamyaman/rust-anything/discussions/127
- https://github.com/erkamyaman/rust-anything/issues/2
- https://github.com/erkamyaman/rust-anything/releases
- https://github.com/napi-rs/napi-rs
- https://github.com/rust-unofficial/awesome-rust#development-tools
- https://github.com/sponsors/erkamyaman
- https://github.com/wasm-bindgen/wasm-bindgen
- https://img.shields.io/badge/Become_a_sponsor-%E2%9D%A4-db61a2?style=for-the-badge&logo=githubsponsors&logoColor=white
- https://img.shields.io/badge/Buy_me_a_coffee-%E2%98%95-FFDD00?style=for-the-badge&logo=buymeacoffee&logoColor=black
- https://img.shields.io/badge/Featured%20in-Awesome%20REA-f0b429
- https://img.shields.io/badge/Join%20the%20discussion-6E40C9?style=for-the-badge&logo=github&logoColor=white
- https://img.shields.io/badge/license-MIT-555
- https://img.shields.io/badge/macOS%20·%20Linux%20·%20Windows-native-2563EB
- https://img.shields.io/coderabbit/prs/github/erkamyaman/rust-anything?labelColor=171717&color=FF570A&label=Reviewed+by+CodeRabbit
- https://img.shields.io/crates/v/rust-anything?color=E2862A&label=crates.io
- https://img.shields.io/github/languages/top/erkamyaman/rust-anything?logo=rust&label=Rust&color=CE422B
- https://img.shields.io/github/stars/erkamyaman/rust-anything?style=social
- https://img.shields.io/npm/v/rust-anything?color=E2862A&label=npm

## 导航

- 项目页：[[10-项目/npmjs.com_372733ea]]
- 渠道页：[[50-渠道/github_new]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
