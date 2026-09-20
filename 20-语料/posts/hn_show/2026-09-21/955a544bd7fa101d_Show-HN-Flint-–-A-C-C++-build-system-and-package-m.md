---
type: "corpus"
item_id: "955a544bd7fa101d"
title: "Show HN: Flint – A C/C++ build system and package manager written in pure C"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49500884"
project_url: "https://github.com/mainak55512/flint"
author: "mbhatt99"
published_at: "2026-08-30T17:38:30Z"
captured_at: "2026-09-21T03:11:29+08:00"
lang: "en"
kind: "post"
topic: "开发者工具"
shard: "2026-09-21"
pub_day: "2026-08-30"
tags:
  - 语料
  - hn_show
  - author_mbhatt99
  - story_49500884
  - show_hn
metrics: {"points": 2, "comments": 0, "engagement_velocity": 2}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:52d"
---

# Show HN: Flint – A C/C++ build system and package manager written in pure C

> [!info] 一句话导读
> Simple light-weight package manager and build system written in C for c/c++ projects

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49500884>
> 指标：点赞=2 · 评论=0 · engagement_velocity=2
> 作者：mbhatt99　|　发布：2026-08-30T17:38:30Z
> 项目链接：<https://github.com/mainak55512/flint>
> 采集：2026-09-21T03:11:29+08:00　|　id：`955a544bd7fa101d`

## 正文

# mainak55512/flint

Simple light-weight package manager and build system written in C for c/c++ projects

- Stars: 3
- Forks: 1
- Watchers: 3
- Open issues: 1
- Default branch: main
- Created: 2026-01-11T18:20:00Z

## Languages

- C
- Shell

## Topics

- build
- build-system
- build-tool
- c-package-manager
- package-manager
- project-management

## Top Contributors

- mainak55512 (46 contributions)

---

## README

# Flint

**Disclaimer: This project is in BETA stage and only available for Linux, use with caution.**

Flint is an experimental build system and package manager for C/C++ projects. It aims to simplify the development workflow by managing dependencies directly through Git and automating the compilation process via a single JSON configuration file.
Flint is compatible with GCC & Clang compilers.

**NOTE:**

CLI Docs available here: Flint

Compositions of the Cherts(dependencies) are/will be updated here: Flint Cherts

## Installation
**Prerequisits:**

- GCC/Clang compiler chain
- GIT

Run the following command in terminal:

```bash
curl -fsSL -H "Accept: application/vnd.github.v3.raw" https://api.github.com/repos/mainak55512/flint/contents/build.sh | bash
```

## Project Structure

Flint expects a specific directory layout to function correctly:

* **src/**: All local project source files (.c, .cpp).
* **include/**: Local header files (.h, .hpp).
* **deps/**: External libraries (managed by Flint).
* **static/**: Contains all the static library (.a) files.
* **shared/**: Contains all the dynamic/shared (.so) libraries.
* **composition.json**: The project manifest.

## How it Works

Currently, Flint uses a "manifest-first" approach:

1. **Git Integration**: When a library is added, flint clones the repository into the `deps/` directory.
2. **Strict Manifest Requirement**: For a dependency to be compatible, it **must** contain its own `composition.json` file. Flint reads this file to understand which directories to include and compile. EDIT: Libraries can be added through chert compositions now (check Flint Cherts).
3. **Compilation**: The tool aggregates all source files and include paths from the main project and all dependencies to trigger the local compiler.

## composition.json Structure

```json
{
    "project_name": "example_project",
    "project_language": "c",
    "version": "0.1.0",
    "compiler_path": "/usr/bin/gcc",
    "executable": true,
    "flags": [],
    "lib_links": [],
    "include_paths": ["include"],
    "src": ["src"],
    "dependencies": {
        "example_lib": {
            "version": "1.0.0",
            "remote": "https://github.com/user/example_lib"
        }
    }
}

```

## Current Limitations

As this is an early development prototype, please be aware of the following:

* ~~**No Build Flags**: Custom compiler flags (e.g., -O3, -Wall) are not yet supported.~~
* **Naming Conflicts**: There is currently no resolution logic for dependencies that share the same directory or project names.
* ~~**Strict Compatibility**: Only repositories containing a `composition.json` file can be added as dependencies at this time.~~
* ~~**No Incremental Builds**: The system currently performs full builds.~~

## Usage

### Initialize a Project

```bash
flint init

```

### Add a Dependency

(The remote repository must contain a `composition.json` file)

```bash
flint add <git_remote_url>

```
or
Add the cherts composition in the `dependencies` section in composition.json and run
```bash
flint sync
```
**N.B.** compositions are/will be available in Flint Cherts

### Build

```bash
flint build

```
or directly run with
```bash
flint run
```

# AbracadaNames

## 关联链接

- https://api.github.com/repos/mainak55512/flint/contents/build.sh
- https://github.com/user/example_lib

## 导航

- 项目页：[[10-项目/github.com_e3e5d724]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`开发者工具`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
