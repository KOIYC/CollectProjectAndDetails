---
type: "corpus"
item_id: "a3fc2c860fa97709"
title: "Show HN: Yet another argument parser for Zig"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49709062"
project_url: "https://github.com/gabor-boros/yaap"
author: "gabor-boros"
published_at: "2026-09-15T07:36:44Z"
captured_at: "2026-09-20T14:57:50+08:00"
lang: "en"
kind: "post"
topic: "开发者工具"
shard: "2026-09-20"
pub_day: "2026-09-15"
tags:
  - 语料
  - hn_show
  - author_gabor-boros
  - story_49709062
  - show_hn
metrics: {"points": 2, "comments": 0, "engagement_velocity": 2}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:90d"
---

# Show HN: Yet another argument parser for Zig

> [!info] 一句话导读
> Yet another argument parser for Zig

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49709062>
> 指标：点赞=2 · 评论=0 · engagement_velocity=2
> 作者：gabor-boros　|　发布：2026-09-15T07:36:44Z
> 项目链接：<https://github.com/gabor-boros/yaap>
> 采集：2026-09-20T14:57:50+08:00　|　id：`a3fc2c860fa97709`

## 正文

# gabor-boros/yaap

Yet another argument parser for Zig

- Stars: 2
- Forks: 0
- Watchers: 2
- Open issues: 9
- License: MIT License
- Homepage: https://gabor-boros.github.io/yaap
- Default branch: main
- Created: 2026-09-14T21:54:32Z

## Languages

- Zig

## Topics

- argument-parser
- cli
- zig-library
- zig-package
- ziglang

## Top Contributors

- gabor-boros (3 contributions)
- github-actions[bot] (1 contributions)

---

## README

# YAAP

Yet Another Argument Parser.

YAAP is an argument parser inspired by Python's `argparse`. While it is giving
the building blocks to make a CLI application, it is intentionally not bloated
with features like autocompletion generation, colored outputs, etc.

Instead, it gives an argument parser with an optional `--help` flag to print
the usage.

## Features

- Positional arguments
- Option default values
- Long and short options (e.g., `-v`, `--verbose`)
- Mixed positional arguments and options (`cmd -v arg1 --option`)
- Subcommands (e.g., `cmd -v subcmd -a` )
- Clear errors on missing values
- Optional `-h | --help` option

## Installation

**1. Fetch the package**

```shell
zig fetch --save git+https://github.com/gabor-boros/yaap#v0.1.0
```

**2. Wire it in `build.zig`**

```zig
const yaap_dep = b.dependency("yaap", .{});
exe.root_module.addImport("yaap", yaap_dep.module("yaap"));
```

## Usage

Optional names and help text go in a spec. YAAP does not print or exit on its
own. Handling `parse` errors and help is the responsibility of the caller.

```zig
const std = @import("std");
const yaap = @import("yaap");

const Config = struct {
    input: []const u8 = "",
    output: []const u8 = "",
    verbose: bool = false,
};

pub fn main(init: std.process.Init) !void {
    var config = Config{};

    var parser = yaap.Parser.init(init.gpa, "prog", .{
        .description = "Process a file",
        .examples = &.{ "prog file.txt", "prog --help", "prog -o output.txt },
    });
    defer parser.deinit();

    try parser.addHelp(.{});
    try parser.addArg(&config.input, .{ .name = "input", .help = "File to process" });
    try parser.addFlag(&config.output, .{ .short = 'o', .default = "text.out", .help = "Output file" })

    var buf: [1024]u8 = undefined;
    var writer = std.Io.File.stderr().writer(init.io, &buf);
    const args = try init.minimal.args.toSlice(init.arena.allocator());

    parser.parse(args[1..]) catch |err| {
        try parser.writeError(&writer.interface, err);
        try writer.interface.flush();
        return;
    };

    if (parser.helpRequested()) {
        try parser.writeUsage(&writer.interface);
        try writer.interface.flush();
        return;
    }

    std.debug.print("input file: {s}\n", .{config.input});
}
```

## Subcommands

Each subcommand is its own `Parser`. Parent flags may appear before the command
name. Remaining tokens are parsed by the child. Calling `writeUsage` on the
**root** parser prints the usage of the parser that requested help. The usage
program line is built from the parent chain, so children do not need their own
program name.

```zig
var parser = yaap.Parser.init(init.gpa, "prog", .{});
defer parser.deinit();

var build = yaap.Parser.initCommand(init.gpa, .{});
defer build.deinit();

try build.addFlag(&config.release, .{ .short = 'r', .long = "release", .help = "Optimized build" });
try build.addHelp(.{});
try parser.addCommand(&build, .{ .name = "build", .help = "Build the project" });
try parser.addHelp(.{});

parser.parse(args[1..]) catch |err| {
    try parser.writeError(writer, err);
    return;
};

if (parser.helpRequested()) {
    try parser.writeUsage(writer);
    return;
}
```

The selected child is available as `parser.selected` (and `parser.command` for
the name). Parent positionals cannot be mixed with subcommands.

## Documentation

API docs are published at gabor-boros.github.io/yaap.
Generate them locally with:

```shell
zig build docs
```

Output is written to `zig-out/docs`.

## Development

Install pre-commit, then enable the hooks (requires
`zig` on `PATH`):

```shell
pre-commit install
```

CI runs the same hooks on every pull request.

## License

YAAP is licensed under the MIT license.

# GitHub - bassimeledath/karen: App feedback as easy as complaining. Point, speak, and give your coding agent the context. A development-only overlay for React apps. · GitHub

## 关联链接

- https://gabor-boros.github.io/yaap
- https://github.com/gabor-boros/yaap#v0.1.0

## 导航

- 项目页：[[10-项目/github.com_8095ffc3]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`开发者工具`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
