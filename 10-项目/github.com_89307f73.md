---
type: "project"
title: "Show HN: OmniDiff – Opensource, super fast, content aware Git difftool, in Rust"
project_url: "https://github.com/ivankovic/omnidiff"
first_seen: "2026-11-02T09:51:51+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_FabCH
  - story_50325253
  - show_hn
  - front_page
lang: "en"
---

# Show HN: OmniDiff – Opensource, super fast, content aware Git difftool, in Rust

> [!info] 一句话导读
> I have been researching what the ultimate diff tool would look like, based on actual diffs in open source repositories.OmniDiff can diff: code (25 languages), c…

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://github.com/ivankovic/omnidiff>
> 首次收录：2026-11-02T09:51:51+08:00
> 来源渠道：HN Show HN
> 标签：author_FabCH, story_50325253, show_hn, front_page
> 最新指标：点赞=157 · 评论=41 · engagement_velocity=157

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-11-02T09:37:22+08:00 | HN Show HN | 点赞=157 · 评论=41 · engagement_velocity=157 | [[20-语料/posts/hn_show/2026-11-02/747d6d027235ec4e_Show-HN-OmniDiff-–-Opensource,-super-fast,-content]] |
| 2026-11-02T09:51:51+08:00 | HN Show HN | 点赞=157 · 评论=41 · engagement_velocity=157 | [[20-语料/posts/hn_show/2026-11-02/747d6d027235ec4e_Show-HN-OmniDiff-–-Opensource,-super-fast,-content]] |

## 摘要正文

I have been researching what the ultimate diff tool would look like, based on actual diffs in open source repositories.OmniDiff can diff: code (25 languages), config, images, PDFs, archives, cursors, fonts...It's fast. It can diff C++ files of tens of thousands of lines in under 100ms, on a 2023 ThinkPad T14s.It's open source. AGPLv3.It's based on real diffs. I looked at the 7400 repositories that are listed in Gentoo packages, sampled 2000 diffs and solved them manually to get a good understanding of what is needed, before putting together the diff pipelines for each content type. Incidentally, this also forms the basis of the CI pipeline, so the robustness of the codebase is quite high.I'm still developing it. It's v0.3.0 at this time. But I have been using it daily as my git difftool for months now, and it works well.AI Disclosure: Yes, I do use AI. No, I do not vibecode.
