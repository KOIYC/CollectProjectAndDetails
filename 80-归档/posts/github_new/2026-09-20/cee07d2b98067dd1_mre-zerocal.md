---
type: "corpus"
item_id: "cee07d2b98067dd1"
title: "mre/zerocal"
source: "github_new"
source_name: "GitHub 新星仓库"
url: "https://github.com/mre/zerocal"
project_url: "https://zerocal.shuttleapp.rs/"
author: "mre"
published_at: "2022-09-21T16:54:02Z"
captured_at: "2026-09-20T03:28:00+08:00"
lang: "en"
kind: "post"
tags:
  - 语料
  - github_new
  - Rust
  - topic:microsaas
metrics: {"stars": 170, "forks": 17, "open_issues": 10}
comments_count: 0
comments_total: 0
discovered_via: "github:14d"
archived: true
archived_at: "2026-09-20T09:16:59+08:00"
archive_reason: "排除:无主题词"
---

# mre/zerocal

- **来源**：GitHub 新星仓库　|　**kind**：post
- **原帖**：https://github.com/mre/zerocal
- **指标**：stars=170 · forks=17 · open_issues=10
- **作者**：mre　|　**发布**：2022-09-21T16:54:02Z
- **项目链接**：https://zerocal.shuttleapp.rs/
- **采集**：2026-09-20T03:28:00+08:00　|　**id**：`cee07d2b98067dd1`

## 正文

# zerocal 🚫📆

Welcome to zerocal, the _serverless calendar_.  
It allows you to create calendar invites from the convenience of your terminal!  
🔗 Here's my [blog post about the project](https://endler.dev/2022/zerocal/).

## Usage

```sh
curl https://zerocal.shuttleapp.rs?start=2022-11-04+20:00&duration=3h&title=Birthday&des
cription=paaarty > party.ics
open party.ics
```

## Web UI

You can also use the web UI at https://zerocal.shuttleapp.rs

![web ui](assets/ui.png)

## Self-hosting

You can also self-host zerocal.
To do so, compile the binary with `cargo build --release --features local` and
run it with `./target/release/zerocal`.
The server will listen on port 8000 by default.

## Contributing

Please check the issue tracker for contribution ideas. Any pull request is welcome. ❤️

To run a local development version install [cargo-watch](https://crates.io/crates/cargo-watch)
and then run

```
make local
```

You can also run a dev version on shuttle.rs with

```
make dev
```

## Derivatives

Was your project inspired by zerocal? Add it here!

- [kiwical](https://github.com/maheshsundaram/kiwi) - Kiwi Calendar built with Typescript on Deno Deploy.

## Credits

This app was built with the help of 🚀 [shuttle.rs](https://www.shuttle.rs/),
the web application platform for Rust.

## 关联链接

- https://zerocal.shuttleapp.rs
