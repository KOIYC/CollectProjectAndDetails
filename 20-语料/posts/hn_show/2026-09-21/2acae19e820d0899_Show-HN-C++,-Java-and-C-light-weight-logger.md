---
type: "corpus"
item_id: "2acae19e820d0899"
title: "Show HN: C++, Java and C# light-weight-logger"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=48732953"
project_url: "https://github.com/PenguineDavid/light-weight-logger"
author: "PenguineDavid"
published_at: "2026-06-30T14:07:42Z"
captured_at: "2026-09-21T02:53:04+08:00"
lang: "en"
kind: "post"
topic: "未分类"
shard: "2026-09-21"
pub_day: "2026-06-30"
tags:
  - 语料
  - hn_show
  - author_PenguineDavid
  - story_48732953
  - show_hn
metrics: {"points": 12, "comments": 0, "engagement_velocity": 12}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:113d"
---

# Show HN: C++, Java and C# light-weight-logger

> [!info] 一句话导读
> PenguineDavid/light-weight-logger

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=48732953>
> 指标：点赞=12 · 评论=0 · engagement_velocity=12
> 作者：PenguineDavid　|　发布：2026-06-30T14:07:42Z
> 项目链接：<https://github.com/PenguineDavid/light-weight-logger>
> 采集：2026-09-21T02:53:04+08:00　|　id：`2acae19e820d0899`

## 正文

# PenguineDavid/light-weight-logger

A custom console logging library made for Java, C++ & C#.

- Stars: 4
- Forks: 0
- Watchers: 4
- Open issues: 0
- License: GNU Lesser General Public License v2.1
- Default branch: main
- Created: 2026-06-15T03:42:26Z

## Languages

- C#
- C++
- Java

## Top Contributors

- PenguineDavid (11 contributions)

---

## README

# Light-Weight-Logger

Format-string driven terminal logging library for C++, C# and Java.

> Licensed under the GNU Lesser General Public License v2.1
> | Source: github.com/PenguineDavid/light-weight-logger

---

## Table of Contents

- Overview
- Format Specifier Reference
- Preset Format Styles
- C++ Implementation
- C# Implementation
- Java Implementation
- License

---

## Overview

Logger is a lightweight, zero-dependency terminal logging library. Instead of a fixed set of log levels with hard-coded output, it gives you a format-string mini-language. You register named levels at runtime, attach a format string and an ANSI colour to each, and call `log()` / `Log()` with a level name and message. The parser walks the format string one character at a time, expanding percent-encoded specifiers into live metadata at call time.

**Key properties:**

- No third-party dependencies in any port
- Single-file drop-in for C++ (`Logger.hpp`), two-file for C# and Java
- ANSI colour output via the `Colour` constants shipped with each port
- Dynamic `%S` padding keeps level names column-aligned automatically as you register more levels
- Source-location capture (`%F`, `%L`, `%f`) available in all three ports
- Date format switchable between AU (`DD/MM/YYYY`) and US (`MM/DD/YYYY`) at runtime

---

## Format Specifier Reference

Every format string is a plain string in which any two-character sequence starting with `%` is treated as a specifier. All other characters are emitted verbatim. Specifiers are expanded left-to-right in a single pass at call time.

### Colour Specifiers

| Specifier | Description |
|-----------|-------------|
| `%C` | Emit the ANSI colour code registered for this level. Use at the start of coloured regions. |
| `%G` | Emit ANSI grey (`\033[90m`). Typically used for metadata/secondary information. |
| `%c` | Emit ANSI reset (`\033[0m`). Required to close any colour region. |

### Layout Specifiers

| Specifier | Description |
|-----------|-------------|
| `%S` | Emit trailing spaces to align the level name column with the longest registered name. Recalculated automatically when new levels are added. |
| `%%` | Literal percent sign. |

### Metadata Specifiers

| Specifier | Description |
|-----------|-------------|
| `%N` | Level name (the string you passed to `add_format` / `AddFormat` / `addFormat`). |
| `%M` | The log message passed to `log()` / `Log()`. |
| `%T` | Current wall-clock time: `HH:MM:SS`. |
| `%D` | Current date: `DD/MM/YYYY` (AU) or `MM/DD/YYYY` (US). Controlled by `change_date_format`. |
| `%ms` | Current milliseconds component (`000`-`999`). Three-character sequence: `%`, `m`, `s`. |
| `%Z` | System timezone name or abbreviation (e.g. `AEST`, `PST`, `UTC`). |
| `%t` | Current thread ID. `std::this_thread::get_id()` in C++, `ManagedThreadId` in C#, `threadId()` in Java. |

### Source Location Specifiers

These resolve at call time by inspecting the call stack. In C++ this uses `std::source_location` (C++20). In C# this uses `System.Diagnostics.StackFrame`. In Java this walks `Thread.currentThread().getStackTrace()`.

| Specifier | Description |
|-----------|-------------|
| `%F` | Source file of the call site. |
| `%L` | Line number of the `log()` call. |
| `%f` | Function or method name at the call site. |

> **Note:** `%F`, `%L` and `%f` add overhead on every log call because they walk the call stack. Omit them from format strings used on hot paths.

---

## Preset Format Styles

The three format strings below are demonstrated in the example files. They are ordinary strings -- copy, modify, or ignore them.

### Style 1: Modern Standard

```
%C[%N]%c%S %G[%D %T %Z]%c -> %M
```

---

### Style 2: Clean Pipe Minimalist

```
%C %N %c%S | %G%T %Z%c | %M
```

---

### Style 3: Cloud Engine (with source metadata)

```
%G%D %T.%ms %Z%c %C<%N>%c%S %M %G(%F:%L)%c
```

---

### Building Your Own Format

Any combination of specifiers and literal text is valid:

```
// Compact -- just level and message, no timestamp
%C[%N]%c%S %M

// ISO-style with milliseconds
%G[%D %T.%ms]%c %C%N%c%S %M

// Thread-tagged for concurrent applications
%G[%T]%c [thread:%t] %C%N%c%S %M

// Full debug dump with source location
%C%N%c%S %M %G@ %F:%L in %f%c
```

---

## C++ Implementation

**Standard:** C++20 | **File:** `Logger.hpp` | **Namespace:** `Colour` (ANSI constants)

### Setup

`Logger.hpp` is header-only. Drop it anywhere on your include path and include it directly -- no build system integration required.

```cpp
#include "Logger.hpp"

int main()
{
    Logger logger;

    std::string fmt = "%C[%N]%c%S %G[%D %T %Z]%c -> %M";
    logger.add_format("INFO",    fmt, Colour::CYAN);
    logger.add_format("SUCCESS", fmt, Colour::GREEN);
    logger.add_format("WARN",    fmt, Colour::YELLOW);
    logger.add_format("ERROR",   fmt, Colour::RED);

    logger.log("INFO",    "Initializing core subsystem components.");
    logger.log("SUCCESS", "Database connection established smoothly.");
    logger.log("WARN",    "High memory usage detected on node cluster.");
    logger.log("ERROR",   "Failed to write to write-ahead log!");
}
```

### Compile

```sh
# GCC / Clang
g++ -std=c++20 -o app main.cpp

# MSYS2 ucrt64 (Windows)
g++ -std=c++20 -o app.exe main.cpp
```

### API Reference

#### `void add_format(const std::string& name, const std::string& format_string, std::string_view level_colour = Colour::WHITE)`

Register a named log level. Calling again with the same `name` replaces the format string and colour. `max_name_length` is updated so `%S` padding stays consistent.

| Parameter | Description |
|-----------|-------------|
| `name` | Arbitrary string used as the level identifier. Passed back via `%N`. |
| `format_string` | Format string using the specifiers above. |
| `level_colour` | One of the `Colour::` constants. Defaults to `Colour::WHITE`. Emitted by `%C`. |

#### `void log(const std::string& format_name, const std::string& message, const std::source_location location = std::source_location::current())`

Emit a log line. If `format_name` does not match a registered level, outputs `[UNREGISTERED]` followed by the message. Do not pass `location` -- the compiler-supplied default captures the call site automatically.

| Parameter | Description |
|-----------|-------------|
| `format_name` | Must match a name passed to `add_format`. |
| `message` | Free-form string emitted by `%M`. |
| `location` | Do not pass. Default captures the call site. |

#### `void change_date_format(std::string type)`

Switch date formatting. Accepts `"au"` (DD/MM/YYYY, default) or `"us"` (MM/DD/YYYY). Any other value is silently ignored.

### Colour Constants

```cpp
Colour::RESET    // \033[0m
Colour::BLACK    // \033[30m
Colour::RED      // \033[31m
Colour::GREEN    // \033[32m
Colour::YELLOW   // \033[33m
Colour::BLUE     // \033[34m
Colour::MAGENTA  // \033[35m
Colour::CYAN     // \033[36m
Colour::WHITE    // \033[37m
Colour::GREY     // \033[90m
```

All constants are `constexpr std::string_view` defined in namespace `Colour`.

### Dependencies

All standard library:

| Header | Used for |
|--------|----------|
| ` `, ` `, `<unordered_map>` | Core I/O and storage |
| ` `, ` ` | Timestamp formatting |
| `<source_location>` | C++20. Required for `%F`, `%L`, `%f` |
| ` ` | `%t` (thread ID) |
| ` ` | `std::max` for `max_name_length` |

---

## C# Implementation

**Runtime:** .NET 8+ | **Files:** `Logger.cs` + `Colour.cs` | **Namespace:** `include`

### Setup

Add both files to your project. No NuGet packages required.

```csharp
using include;

Logger logger = new Logger();

string fmt = "%C[%N]%c%S %G[%D %T %Z]%c -> %M";
logger.AddFormat("INFO",    fmt, Colour.CYAN);
logger.AddFormat("SUCCESS", fmt, Colour.GREEN);
logger.AddFormat("WARN",    fmt, Colour.YELLOW);
logger.AddFormat("ERROR",   fmt, Colour.RED);

logger.Log("INFO",    "Initializing core subsystem components.");
logger.Log("SUCCESS", "Database connection established smoothly.");
logger.Log("WARN",    "High memory usage detected on node cluster.");
logger.Log("ERROR",   "Failed to write to write-ahead log!");
```

### Project File

```xml
<Project Sdk="Microsoft.NET.Sdk">
  <PropertyGroup>
    <OutputType>Exe</OutputType>
    <TargetFramework>net8.0</TargetFramework>
    <Nullable>enable</Nullable>
    <ImplicitUsings>enable</ImplicitUsings>
  </PropertyGroup>
</Project>
```

### API Reference

#### `void AddFormat(string name, string formatString, string levelColour)`

Register a named log level. `Formats` and `FormatColours` are `static Dictionary` instances shared across all `Logger` instances, so formats registered on one instance are visible to all others. Calling again with the same `name` replaces the entry and recalculates `_maxNameLength`.

| Parameter | Description |
|-----------|-------------|
| `name` | Level identifier. Passed back via `%N`. |
| `formatString` | Format string using the specifiers above. |
| `levelColour` | One of the `Colour.` constants. Emitted by `%C`. |

#### `void AddFormat(string name, string formatString)`

Overload that defaults `levelColour` to `Colour.WHITE`.

#### `void Log(string formatName, string message)`

Emit a log line. Source location is resolved via `new StackTrace(true)` -- frame index 1 is always the direct caller of `Log()`. Requires PDB symbols or source-linked builds for `%F` and `%L` to resolve correctly.

> **Note:** In Release builds without PDBs, `%F` and `%L` may return `null` or `0`. Either ship PDBs alongside the binary or restrict source-location specifiers to Debug configurations.

#### `void ChangeDateFormat(string format)`

Accepts `"au"` (DD/MM/YYYY) or `"us"` (MM/DD/YYYY). Any other value is silently ignored.

### Colour Constants

```csharp
Colour.RESET    // \x1B[0m
Colour.BLACK    // \x1B[30m
Colour.RED      // \x1B[31m
Colour.GREEN    // \x1B[32m
Colour.YELLOW   // \x1B[33m
Colour.BLUE     // \x1B[34m
Colour.MAGENTA  // \x1B[35m
Colour.CYAN     // \x1B[36m
Colour.WHITE    // \x1B[37m
Colour.GREY     // \x1B[90m
```

All constants are `public static readonly string` on the `Colour` class in namespace `include`.

### Threading Notes

`Formats` and `FormatColours` are static dictionaries. `AddFormat` is not thread-safe and must be called during initialisation before spawning threads. `Log()` only reads from those dictionaries after setup, which is safe for concurrent readers.

---

## Java Implementation

**Minimum:** Java 21 | **Files:** `Logger.java` + `Colour.java` | **Package:** `include`

### Setup

Place both files under `src/include/`. Import them into any class that needs logging.

```java
import include.Logger;
import include.Colour;

public class main {
    public static void main(String[] args) {
        Logger logger = new Logger();

        String fmt = "%C[%N]%c%S %G[%D %T %Z]%c -> %M";
        logger.addFormat("INFO",    fmt, Colour.CYAN);
        logger.addFormat("SUCCESS", fmt, Colour.GREEN);
        logger.addFormat("WARN",    fmt, Colour.YELLOW);
        logger.addFormat("ERROR",   fmt, Colour.RED);

        logger.log("INFO",    "Initializing core subsystem components.");
        logger.log("SUCCESS", "Database connection established smoothly.");
        logger.log("WARN",    "High memory usage detected on node cluster.");
        logger.log("ERROR",   "Failed to write to write-ahead log!");
    }
}
```

### Compile and Run

```sh
# From the directory containing src/
javac -d out src/include/Colour.java src/include/Logger.java src/main.java
java -cp out main
```

### API Reference

#### `void addFormat(String name, String formatString, CharSequence levelColour)`

Register a named log level. `FORMATS` and `FORMAT_COLOURS` are `static HashMap` instances shared across all `Logger` instances. Calling again with the same `name` replaces the entry and recalculates `maxNameLength`.

| Parameter | Description |
|-----------|-------------|
| `name` | Level identifier. Passed back via `%N`. |
| `formatString` | Format string using the specifiers above. |
| `levelColour` | A `CharSequence` -- in practice one of the `Colour.*` string constants. Emitted by `%C`. |

#### `void addFormat(String name, String formatString)`

Overload that defaults `levelColour` to `Colour.WHITE`.

#### `void log(String formatName, String message)`

Emit a log line. Source location is resolved by calling `Thread.currentThread().getStackTrace()` and reading index 2 (0 = `getStackTrace`, 1 = `log()`, 2 = caller). The file name from `getFileName()` is the simple filename without path.

> **Note:** `Thread.currentThread().threadId()` requires Java 19+, stable in Java 21. If you need Java 17 support, replace `threadId()` with the deprecated `getId()`.

#### `void changeDateFormat(String type)`

Accepts `"au"` (DD/MM/YYYY) or `"us"` (MM/DD/YYYY). Uses `"au".equals(type)` null-safe comparison. Any other value is silently ignored.

### Colour Constants

```java
Colour.RESET    // \033[0m
Colour.BLACK    // \033[30m
Colour.RED      // \033[31m
Colour.GREEN    // \033[32m
Colour.YELLOW   // \033[33m
Colour.BLUE     // \033[34m
Colour.MAGENTA  // \033[35m
Colour.CYAN     // \033[36m
Colour.WHITE    // \033[37m
Colour.GREY     // \033[90m
```

All constants are `public static final String` on the `Colour` class in package `include`.

### Threading Notes

`FORMATS` and `FORMAT_COLOURS` are static `HashMap` instances. `addFormat` is not thread-safe and must not be called concurrently. `log()` is effectively read-only on those maps after setup and is safe to call from multiple threads, though walking the stack trace on every call carries overhead under high concurrency.

---

## License

This library is distributed under the GNU Lesser General Public License v2.1.

What LGPL v2.1 means in practice:

- You may use Light-Weight-Logger in a closed-source application without being required to open-source that application
- If you distribute a modified version of Light-Weight-Logger itself, those modifications must be released under LGPL v2.1
- You must provide a way for end users to re-link your application against a modified version of the library
- A copy of the licence text must accompany any distribution of the library

Copyright (C) 2026 David S

This library is free software: you can redistribute it and/or modify
it under the terms of the GNU Lesser General Public License as published by
the Free Software Foundation, either version 2.1 of the License, or
(at your option) any later version.

This library is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU Lesser General Public License for more details.

You should have received a copy of the GNU Lesser General Public License
along with this library. If not, see https://www.gnu.org/licenses/old-licenses/lgpl-2.1.html#SEC1.

## 关联链接

- https://www.gnu.org/licenses/old-licenses/lgpl-2.1.html#SEC1.

## 导航

- 项目页：[[10-项目/github.com_65444196]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`未分类`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
