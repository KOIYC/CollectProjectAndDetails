---
type: "corpus"
item_id: "916ec5f34791cb5a"
title: "What I learned building wfreq"
source: "devto"
source_name: "dev.to"
url: "https://dev.to/yashksaini/what-i-learned-building-wfreq-52f5"
project_url: "https://crates.io/crates/thiserror"
author: "Yash Kumar Saini"
published_at: "2026-10-28T15:10:42Z"
captured_at: "2026-10-29T20:47:20+08:00"
lang: "en"
kind: "post"
topic: "开发者工具"
shard: "2026-10-29"
pub_day: "2026-10-28"
tags:
  - 语料
  - devto
  - rust
  - cli
  - buildinpublic
  - discuss
metrics: {"reactions": 12, "comments": 3, "reading_time": 5}
comments_count: 3
comments_total: 3
discovered_via: "devto:buildinpublic"
---

# What I learned building wfreq

> [!info] 一句话导读
> How a word-frequency tool taught me to wrap errors instead of replacing them: from .expect() to thiserror, #[source] and per-file warnings.

> [!meta]- 语料信息（点开展开）
> 来源：dev.to（post）
> 原帖：<https://dev.to/yashksaini/what-i-learned-building-wfreq-52f5>
> 指标：reactions=12 · 评论=3 · reading_time=5
> 作者：Yash Kumar Saini　|　发布：2026-10-28T15:10:42Z
> 项目链接：<https://crates.io/crates/thiserror>
> 采集：2026-10-29T20:47:20+08:00　|　id：`916ec5f34791cb5a`

## 正文

## TL;DR

How a word-frequency tool taught me to wrap errors instead of replacing them: from .expect() to thiserror, #[source] and per-file warnings.

---

![wfreq running in the terminal](https://dev-to-uploads.s3.us-east-2.amazonaws.com/uploads/articles/34vxm5jgef1gx024558g.gif)

I built `wfreq`, a small Rust CLI that prints the most common words in `.txt`, `.md`, `.pdf` and `.docx` files. The counting took an afternoon. The error messages took the rest of the project.

This post is about the hardest part: making the tool tell the truth when something goes wrong.

## Version 1: `.expect()` and a crash

The first `main` read the file like this:

```rust
let content = std::fs::read_to_string(&args.file).expect("File can not read");
```

I pointed it at a PDF and got:

```plaintext
thread 'main' panicked at src/main.rs:30:57:
File can not read: Error { kind: InvalidData, message: "stream did not contain valid UTF-8" }
```

Two problems. A panic is a crash with a backtrace hint, not a message for a user. And `read_to_string` only accepts valid UTF-8, so every PDF "can not be read", even though the file is right there.

## Version 2: `?` and an error message nobody asked for

The textbook fix is to return `Result` from `main` and use `?`. I added a custom error enum with [thiserror](https://crates.io/crates/thiserror) and nice messages:

```rust
#[derive(Debug, Error)]
pub enum CliError {
    #[error("File not found or cannot read: {0}")]
    FileReadError(PathBuf),
    // ...
}

fn main() -> Result<(), Box<dyn Error>> {
    let content = parser::extract_text(&args.file)?;
    // ...
}
```

Then I ran it on a missing file:

```console
$ wfreq nope.txt
Error: FileReadError("nope.txt")
```

My message was nowhere. When `main` returns `Err`, Rust prints the error with **`Debug`**, not `Display`, so all the `#[error("...")]` text is ignored.

The fix is small: keep `?` everywhere, but handle the error once, at the top.

```rust
fn main() {
    if let Err(e) = run() {
        eprintln!("error: {e}");   // Display: the #[error] text
        std::process::exit(1);
    }
}

fn run() -> Result<(), Box<dyn Error>> {
    // all the real work, using ? freely
}
```

`exit(1)` lives in `main`, after `run()` has returned and dropped everything, so nothing is skipped. And `eprintln!` sends the message to stderr, so `wfreq notes.txt > top.txt` never puts an error into the output file.

## Version 3: the lie

Now errors looked nice:

```console
$ wfreq nope.txt
error: File not found or cannot read: nope.txt
```

Then I tried a file that **did** exist but was not valid UTF-8. Same message: "File not found or cannot read". The file was right there. The real reason, invalid UTF-8, was gone.

The culprit was one character in the conversion:

```rust
std::fs::read_to_string(path)
    .map_err(|_| CliError::FileReadError(path.to_path_buf()))
```

`|_|` throws the `io::Error` away. "Not found", "permission denied", "is a directory" and "not UTF-8" all became the same vague sentence.

The rule I took from this: **when you convert an error, wrap it, don't replace it.** Your error adds the context (which file), and the original error keeps the cause (why).

```rust
#[derive(Debug, Error)]
pub enum CliError {
    #[error("cannot read {}: {source}", .path.display())]
    FileRead {
        path: PathBuf,
        #[source]
        source: std::io::Error,
    },
    // ...
}

std::fs::read_to_string(path).map_err(|source| CliError::FileRead {
    path: path.to_path_buf(),
    source,
})
```

Two details worth knowing:

- `PathBuf` has no `Display`, because a path is not guaranteed to be valid text. So the message uses `{}` with `.path.display()` as an extra argument. The leading `.` refers to the variant's field.
- `#[source]` makes thiserror implement `Error::source()`, so tools that print error chains can follow it to the `io::Error`.

Now the same file says what is actually wrong:

```plaintext
error: cannot read bad.txt: stream did not contain valid UTF-8
error: cannot read nope.txt: No such file or directory (os error 2)
```

## Version 4: the bug that compiled

When I added PDF and DOCX support, the parser picked a function by file extension. One version looked like this:

```rust
match ext.as_str() {
    "txt" | "md" => {
        txt::parse(file_path);
        Ok("Parser success".to_string())
    }
    "docx" => docx::parse(file_path),
    // ...
}
```

This type-checks (once a missing `use std::fs;` was added). Every arm returns `Result<String, CliError>`. But the `;` after `txt::parse(file_path)` throws away the parsed text **and** any error. Every `.txt` file now "contained" the two words `parser` and `success`, and a broken file reported success.

The compiler can't catch this: the types are right, the values are wrong. A test can:

```rust
#[test]
fn reads_text_from_stdin() {
    let out = run_with_stdin(&["-", "-n", "1"], "to be or not to be");
    assert_eq!(stdout(&out), "Path: -\n 1. be              2\n");
}
```

Each arm should just be the parser call, so its result (text or error) is returned as-is:

```rust
"txt" | "md" => txt::parse(file_path),
"pdf" => pdf::parse(file_path),
"docx" => docx::parse(file_path),
```

## Version 5: one bad file in a folder

Then the tool learned to read folders. A folder can hold a broken PDF next to twenty good text files. Should one bad file stop the whole run?

I decided:

- **One file given:** any problem is an error, exit code 1.
- **Several files or a folder:** a bad file is a warning on stderr and is skipped.
- **Every file failed:** that is an error too, because there is nothing to count.

```rust
for path in &files {
    match parser::extract_text(path) {
        Ok(text) => merge_counts(&mut counts, count_words(&text, args.case_sensitive)),
        Err(e) if files.len() > 1 => eprintln!("warning: {e} (skipped)"),
        Err(e) => return Err(e.into()),
    }
}
```

This only works because of version 3. The warning is useful because the error already carries the file and the reason:

```plaintext
warning: cannot parse docs/old.pdf: PDF error: couldn't parse input: invalid file header (skipped)
```

Without the path in the error, that line would say "cannot parse: invalid file header", and you would have to guess which of the twenty files it means.

## What I'd tell myself at the start

1. `.expect()` is for "this cannot happen", not for user input.
2. Returning `Result` from `main` prints `Debug`. Use a `run()` function and print the error yourself.
3. `map_err(|_| ...)` deletes information you can't get back. Wrap the error with `#[source]` instead.
4. Put the file path in the error, not in the caller. You will need it as soon as there is more than one file.
5. A `match` arm with a `;` and a hard-coded `Ok(...)` compiles fine. Write an end-to-end test that checks real output.

The integration tests in `tests/integration.rs` check every error message mentioned here, so none of these bugs can come back quietly.

full crash → crates.io story: https://medium.com/@yash_k_saini/from-a-crash-to-crates-io-shipping-a-rust-cli-tool-f6ed59c16a9f
repo: https://github.com/yashksaini-coder/wfreq
crate: https://crates.io/crates/wfreq

## 评论（3/3）

> **Sina Rezaei** · 2026-10-28T17:03:15Z　
> The per-file warning approach is a good call. I’d be curious how you’d handle this if wfreq were running in CI over thousands of documents: say one PDF is corrupted halfway through the batch, but the rest are valid. Keeping the original error chain makes debugging much easier, but I’d also want the final exit status to distinguish “some files were skipped” from “the whole run failed.” Otherwise, a pipeline could publish incomplete frequency data and still report success. That’s where error handling starts becoming part of the CLI’s contract, not just nicer error messages.

---

> **Yash Kumar Saini** · 2026-10-29T04:21:21Z　
> That is a serious concern and that's why I'm looking for contributors, if you have any feasible solutions please raise a pr I would like to see how you would approach that problem

---

> **Sina Rezaei** · 2026-10-29T05:13:12Z　
> I'd probably separate processing from publishing the results. Say a CI job scans 4,000 PDFs and one fails halfway through. wfreq could keep processing the remaining files, collect the failed paths and their error chains, then return a non-zero exit code if anything was skipped. I'd also write the frequency data to a temporary file and only replace the final output once the batch is clean. Otherwise, a failed run could leave behind a perfectly valid-looking but incomplete dataset. A --keep-going flag plus a clear batch summary would make this much easier to use in CI.

## 关联链接

- https://crates.io/crates/wfreq
- https://dev-to-uploads.s3.us-east-2.amazonaws.com/uploads/articles/34vxm5jgef1gx024558g.gif
- https://github.com/yashksaini-coder/wfreq
- https://medium.com/@yash_k_saini/from-a-crash-to-crates-io-shipping-a-rust-cli-tool-f6ed59c16a9f

## 导航

- 项目页：[[10-项目/crates.io_b608986c]]
- 渠道页：[[50-渠道/devto]]
- 赛道：`开发者工具`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
