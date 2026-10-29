---
type: "project"
title: "What I learned building wfreq"
project_url: "https://crates.io/crates/thiserror"
first_seen: "2026-10-29T20:47:20+08:00"
sources:
  - devto
tags:
  - 项目
  - devto
  - rust
  - cli
  - buildinpublic
  - discuss
lang: "en"
---

# What I learned building wfreq

> [!info] 一句话导读
> How a word-frequency tool taught me to wrap errors instead of replacing them: from .expect() to thiserror, #[source] and per-file warnings.

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://crates.io/crates/thiserror>
> 首次收录：2026-10-29T20:47:20+08:00
> 来源渠道：dev.to
> 标签：rust, cli, buildinpublic, discuss
> 最新指标：reactions=12 · 评论=3 · reading_time=5

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-10-29T20:47:20+08:00 | dev.to | reactions=12 · 评论=3 · reading_time=5 | [[20-语料/posts/devto/2026-10-29/916ec5f34791cb5a_What-I-learned-building-wfreq]] |

## 摘要正文

## TL;DR  How a word-frequency tool taught me to wrap errors instead of replacing them: from .expect() to thiserror, #[source] and per-file warnings.  ---  ![wfreq running in the terminal](https://dev-to-uploads.s3.us-east-2.amazonaws.com/uploads/articles/34vxm5jgef1gx024558g.gif)  I built `wfreq`, a small Rust CLI that prints the most common words in `.txt`, `.md`, `.pdf` and `.docx` files. The counting took an afternoon. The error messages took the rest of the project.  This post is about the hardest part: making the tool tell the truth when something goes wrong.  ## Version 1: `.expect()` and a crash  The first `main` read the file like this:  ```rust let content = std::fs::read_to_string(&args.file).expect("File can not read"); ```  I pointed it at a PDF and got:  ```plaintext thread 'main' panicked at src/main.rs:30:57: File can not read: Error { kind: InvalidData, message: "stream did not contain valid UTF-8" } ```  Two problems. A panic is a crash with a backtrace hint, not a message for a user. And `read_to_string` only accepts valid UTF-8, so every PDF "can not be read", even though the file is right there.  ## Version 2: `?` and an error message nobody asked for  The text…
