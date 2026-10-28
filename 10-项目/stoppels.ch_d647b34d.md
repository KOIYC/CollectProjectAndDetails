---
type: "project"
title: "Show HN: Tar-minefield shows where tar implementations disagree"
project_url: "https://stoppels.ch/tar"
first_seen: "2026-10-28T09:39:16+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_stabbles
  - story_50264374
  - show_hn
lang: "en"
---

# Show HN: Tar-minefield shows where tar implementations disagree

> [!info] 一句话导读
> tar-minefield F17 pax-global-comment ›

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://stoppels.ch/tar>
> 首次收录：2026-10-28T09:39:16+08:00
> 来源渠道：HN Show HN
> 标签：author_stabbles, story_50264374, show_hn
> 最新指标：点赞=3 · 评论=2 · engagement_velocity=3

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-10-28T09:39:16+08:00 | HN Show HN | 点赞=3 · 评论=2 · engagement_velocity=3 | [[20-语料/posts/hn_show/2026-10-28/bcd45708a8150e71_Show-HN-Tar-minefield-shows-where-tar-implementati]] |

## 摘要正文

Working draft  tar-minefield F17 pax-global-comment ›  Tar file extraction test suite This project provides an extensive test suite and documentation for tar file extraction, with the goal of ensuring that implementations extract tar archives the same way. There are many implementations of tar, from command line tools to libraries for programming languages. Because the tar file format leaves room for interpretation, different implementations can extract certain crafted tar files in different ways. This is a security concern for file exchange: for example, when a security scanner and the extractor use different tar implementations, the scanner could inspect other files than the ones that end up on disk. By assigning identifiers to these ambiguities, and providing test cases and usage data, this project aims for tar implementations to converge on strict parsing and identical behavior. This project proposes a default policy that rejects the vast majority of ambiguities in tar files that could make implementations extract different files, while ensuring that nearly every source tarball already published can still be extracted. Of the 82,586 source tarballs of Spack, nixpkgs, Guix and l…
