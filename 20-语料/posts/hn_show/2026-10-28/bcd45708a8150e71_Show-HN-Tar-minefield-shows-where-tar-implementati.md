---
type: "corpus"
item_id: "bcd45708a8150e71"
title: "Show HN: Tar-minefield shows where tar implementations disagree"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50264374"
project_url: "https://stoppels.ch/tar"
author: "stabbles"
published_at: "2026-10-27T19:21:25Z"
captured_at: "2026-10-28T09:39:16+08:00"
lang: "en"
kind: "post"
topic: "开发者工具"
shard: "2026-10-28"
pub_day: "2026-10-27"
tags:
  - 语料
  - hn_show
  - author_stabbles
  - story_50264374
  - show_hn
metrics: {"points": 3, "comments": 2, "engagement_velocity": 3}
comments_count: 2
comments_total: 2
discovered_via: "hn:show_hn:3d"
---

# Show HN: Tar-minefield shows where tar implementations disagree

> [!info] 一句话导读
> tar-minefield F17 pax-global-comment ›

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50264374>
> 指标：点赞=3 · 评论=2 · engagement_velocity=3
> 作者：stabbles　|　发布：2026-10-27T19:21:25Z
> 项目链接：<https://stoppels.ch/tar>
> 采集：2026-10-28T09:39:16+08:00　|　id：`bcd45708a8150e71`

## 正文

Working draft
 tar-minefield F17 pax-global-comment ›
 Tar file extraction test suite
This project provides an extensive test suite and documentation for tar file extraction, with the goal of ensuring that implementations extract tar archives the same way.
There are many implementations of tar, from command line tools to libraries for programming languages. Because the tar file format leaves room for interpretation, different implementations can extract certain crafted tar files in different ways.
This is a security concern for file exchange: for example, when a security scanner and the extractor use different tar implementations, the scanner could inspect other files than the ones that end up on disk.
By assigning identifiers to these ambiguities, and providing test cases and usage data, this project aims for tar implementations to converge on strict parsing and identical behavior.
This project proposes a default policy that rejects the vast majority of ambiguities in tar files that could make implementations extract different files, while ensuring that nearly every source tarball already published can still be extracted. Of the 82,586 source tarballs of Spack, nixpkgs, Guix and live-bootstrap, and samples of PyPI, crates.io and RubyGems, it accepts 99.77% .
Comparison of different tar implementations ¶
This table shows how different tar implementations behave on each test case. A green ✓ is the
strict behavior that the default policy asks for; click a row for details
about the case.
Each case has a permanent identifier, such as F15, whose letter is its category:
F framing: which members an archive has.
N names: what path each member has.
K kinds: the kind of each member: file, directory or link.
S order and state: how members combine into a directory tree.
A case's page shows its archive block by block, what every implementation makes of it, and how
common it is in release tarballs. An implementation's page, linked from its name above the matrix,
lists the cases where it does not do as the policy says.
Policy ¶
This section defines a working draft of the
 default policy 1 , which accepts, tolerates or rejects
each case below, based on data from the 82,586 distinct release
tarballs of Spack, nixpkgs, Guix and live-bootstrap, and samples of PyPI, crates.io and RubyGems.
The prevalence column is the share of these tarballs that have a case: a first-order
approximation of how common it is in general.
1 A policy can be stricter and also reject the tolerated
cases, at the cost of rejecting more published tarballs: some tolerated cases are common, such as
numbers padded with spaces (F01), and others rare. That suits special-purpose tools,
such as an extractor for a single ecosystem, where it can be checked against every tarball ever
published there.
To accept ¶
identifier name what it is prevalence
F17 pax-global-comment The global pax header with only a comment , as git archive writes it. not measured
F31 pax-xattr-not-utf8 An xattr in a pax header whose value is not UTF-8, as libarchive and star write them. 0.04%
N01 gnu-long-name A name over 100 bytes, in a GNU long name. not measured
N02 name-fills-field A name of exactly 100 bytes, which fills the name field without a NUL. 9.53%
N03 pax-long-name A name over 100 bytes, in a pax path . not measured
N04 ustar-prefix A long name split between the ustar prefix and name fields. 7.65%
S01 tree-dir-after-contents A directory after its contents. 1.22%
S02 tree-duplicate-dir The same directory twice, as tar cf x.tar d d/sub writes. 0.19%
Tolerated ¶
identifier name what it is prevalence
F01 number-leading-space Numeric fields padded with spaces rather than zeros, as old tars wrote them. 0.99%
F02 end-data-after Data after the end-of-archive marker that is not a header, which is ignored. 0.03%
F05 magic-version-nuls The POSIX magic with NULs for its version, ustar\0\0\0 , as some Java archivers write. 0.07%
F14 pax-size-disagrees A pax size that disagrees with the header's, so that a reader of the header's misses a member. none
F18 pax-global-comment-after-members A global pax header with only a comment , after the first member. 0.10%
F32 checksum-leading-space A checksum padded with spaces rather than zeros, as Perl's Archive::Tar writes it. 0.99%
N05 name-dot A member named ./ , the root of the tree, as tar cf x.tar . writes first. 0.08%
N06 name-leading-dot-slash The name ./a , which is the path a . 0.30%
N07 symlink-absolute A symlink to an absolute path, created as it is. 0.11%
N15 name-control-character A control character in a name, here a newline, created as it is. 0.01%
To reject: framing ¶
identifier name what it is prevalence
F03 end-lone-zero-block An end-of-archive marker of one zero block, not two. <0.01%
F04 end-missing No end-of-archive marker: the archive ends after a complete member. 0.03%
F06 checksum-signed A checksum that only matches as the signed sum of the header. none
F07 end-archive-after Another archive after the end-of-archive marker. <0.01%
F08 end-truncated-in-member An archive that ends inside the data of a member. not measured
F09 end-zero-block-then-member A zero block, then another member: the end of the archive, or not? <0.01%
F10 extended-pax-size-before-gnu-long A pax size followed by a GNU long name: which of them does the size apply to? none
F11 magic-odd-version The POSIX magic with a version that is neither 00 nor NULs. none
F12 number-size-gap A size with a space among its digits, which reads as two sizes. none
F13 pax-newline-in-path A newline in a pax path , which split on lines is another record. none
F15 pax-size-on-dir A pax size on a directory, which takes the next header for its data. 0.01%
F16 type-unknown An unknown typeflag with a size: data, or no data? none
F19 pax-global-between-extended-and-member A global pax header between an extended header and its member. none
F20 pax-global-size A global pax header with a size , which frames every member after it, or none. none
F21 pax-size-empty An empty pax size , which in POSIX removes the size rather than giving one. none
F22 pax-size-negative A negative pax size , which a member cannot have. none
F23 pax-size-plus A pax size with a plus sign, +512 , which conversions of strings to numbers accept. none
F24 pax-size-leading-space A pax size with a leading space, 512 , which conversions of strings to numbers skip. none
F25 pax-size-not-ascii-digits A pax size in Arabic-Indic digits, ٥١٢ , which some conversions of strings read as 512. none
F26 pax-size-leading-zero A pax size with a leading zero, 0777 : 777 in decimal, as POSIX says, or 511 in octal. none
F27 pax-size-too-large A pax size of 2^64 + 512, which wraps around to 512 in 64 bits. none
F28 pax-newline-in-comment A newline in a pax comment , which split on lines leaves a size record. none
F29 number-size-base256-negative A negative base-256 size in the header, -512, which a member cannot have. none
F30 number-size-base256-too-large A base-256 size of 2^64 + 512 in the header, which wraps around to 512 in 64 bits. none
F33 size-on-dir A size in the header of a directory, which takes the next header for its data. none
F34 size-on-hardlink A size in the header of a hard link, in a pax archive, which takes the next header for its data. none
F35 pax-size-on-hardlink A pax size on a hard link, which takes the next header for its data. none
F36 pax-record-length-short A pax record whose length is one byte short, so that it ends just before its newline. none
To reject: names ¶
identifier name what it is prevalence
N08 extended-pax-path-and-gnu-long-name A pax path and a GNU long name for one member, and a third name in its header. none
N09 extended-two-pax-headers Two pax extended headers for one member, with different paths. none
N10 format-star A ustar prefix whose end reads as star's times, with star's tar\0 at offset 508. <0.01%
N11 gnu-prefix-field The prefix field of a header with GNU magic, which GNU tar uses for times in incremental archives. none
N12 name-absolute An absolute name, which points outside the directory the archive is extracted to. <0.01%
N13 name-backslash A backslash in a name: a character on Unix, a separator on Windows. <0.01%
N14 name-bytes-after-nul Bytes after the NUL that ends a name. none
N16 name-dotdot A name with .. , which climbs out of the directory the archive is extracted to. <0.01%
N17 name-empty A member with an empty name. none
N18 name-not-utf8 A name that is not UTF-8. <0.01%
N19 pax-nul-in-path A NUL inside a pax path . none
N20 pax-repeated-key One pax key twice in one extended header. <0.01%
N21 pax-global-path A global pax header with a path . none
N22 pax-path-empty An empty pax path , which in POSIX removes the path rather than giving one. none
N23 extended-gnu-long-then-pax A GNU long name, then a pax header, then the member: which of them does the long name apply to? none
N24 pax-hdrcharset-binary hdrcharset=BINARY , which declares a pax path that is not UTF-8 as bytes. none
N25 symlink-empty-target A symlink with an empty target. none
N26 pax-global-path-then-empty A global path , then a global header that removes it with an empty value. none
To reject: kinds ¶
identifier name what it is prevalence
K01 kind-trailing-slash-file A regular file whose name ends in a slash: a file, or a directory? <0.01%
K02 linkname-on-file A regular file with a link target. <0.01%
K03 symlink-trailing-slash A symlink whose name ends in a slash. none
To reject: order and state ¶
identifier name what it is prevalence
S03 hardlink-missing-target A hardlink to a member that is not in the archive. none
S04 hardlink-to-itself A hardlink to itself. 0.03%
S05 hardlink-to-later-member A hardlink to a member that comes later. none
S06 hardlink-to-symlink A hardlink to a symlink: a link to the symlink, or to its target? <0.01%
S07 tree-duplicate-file-differs The same file twice, with different contents: the first copy, or the last? not measured
S08 tree-duplicate-file-dir A file, then a directory of the same name. none
S09 tree-duplicate-file-identical The same file twice, with the same contents. 0.11%
S10 tree-symlink-then-file A symlink, then a file of the same name: replace the link, or write through it? none
S11 tree-through-symlink A member written through a symlink, which points out of the destination. none
S12 tree-under-file A member under a file. <0.01%
S13 hardlink-empty-target A hardlink with an empty target. none
Data to support the default policy ¶
The default policy accepts 99.77% of the 82,586 distinct release tarballs of Spack, nixpkgs, Guix and live-bootstrap, and samples of PyPI, crates.io and RubyGems. See the list of the 192 it rejects , and why.
ecosystem tarballs rejected share
Spack 37,553 70 0.19%
nixpkgs 18,990 78 0.41%
Guix 10,168 34 0.33%
PyPI 10,000 19 0.19%
crates.io 5,000 0 none
RubyGems 5,000 6 0.12%
live-bootstrap 171 0 none
total (distinct) 82,586 192 0.23%
The tarballs by the median mtime of their members, a rough check that the data spans enough years, leaving out the 14,361 whose mtimes are fixed for reproducibility or missing:
Motivating examples ¶
case the archive what implementations make of it
N09 two pax headers for one file, with path=first and path=second GNU tar, BusyBox, 7-Zip, node-tar, tar-fs, Go, R and Julia extract second ; Python and Java extract first ; PHP, RubyGems, Perl and live-bootstrap extract header-name , the name in the ustar header; bsdtar, Rust, .NET and Haskell reject it
S10 a symlink a to target , then a file a most replace the link with the file; Python's tarfile and live-bootstrap write through the link, to target ; 7-Zip, .NET and Haskell reject it
K01 a regular file named a/ GNU tar, bsdtar, BusyBox, 7-Zip, node-tar, Java, Perl and live-bootstrap create a directory a ; Python, Go, Rust's tar and astral-tokio-tar, PHP's PharData , RubyGems and R an empty file a ; tar-fs, .NET, Haskell, Julia and tar-codec reject it
F12 a size field of 000000 1000 , with a space GNU tar, BusyBox, 7-Zip, node-tar, tar-fs, Perl, Haskell, Julia and live-bootstrap read 0, and find a second file smuggled in the data; R reads 512, and extracts it as the data of a ; bsdtar, Python, Go, Rust, Java, .NET, PHP and RubyGems reject it
Contributing ¶
This project is looking for contributions from people who work on package managers, registries and tar implementations, in the form of discussions in issues or pull requests on GitHub or by email to harmen at stoppels dot ch, so that the working draft of the default policy can become a reference.
You can also contribute by testing other implementations, or by crafting a tarball that is particularly hard to parse. A case that shows a vulnerability that is not yet disclosed is reported privately first: see SECURITY.md .
Contributors:
Harmen Stoppels
William Woodruff
haampie/tar-minefield on GitHub · Last updated 2026-10-27 · DOI 10.5281/zenodo.23617964

## 评论（2/2）

> **genxy** · 2026-10-27T19:27:56.000Z　
> Really excellent report, both in the content and the presentation.My solution is to use gnu tar everywhere.

---

> **due-rr** · 2026-10-27T19:40:48.000Z　
> Agreed! Unfortunately the choice is not always in your hands.

## 导航

- 项目页：[[10-项目/stoppels.ch_d647b34d]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`开发者工具`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
