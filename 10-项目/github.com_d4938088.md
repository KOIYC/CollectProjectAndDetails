---
type: "project"
title: "Show HN: FELF – AppImage-like single binaries without FUSE, root, or a runtime"
project_url: "https://github.com/Rucadi/FELF"
first_seen: "2026-11-09T09:39:29+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_Rucadi
  - story_50415219
  - show_hn
lang: "en"
---

# Show HN: FELF – AppImage-like single binaries without FUSE, root, or a runtime

> [!info] 一句话导读
> Hello HN!I've always had a bad time redistributing programs that use shared libraries, AppImage in my opinion does too much, and a container is an overkill - no…

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://github.com/Rucadi/FELF>
> 首次收录：2026-11-09T09:39:29+08:00
> 来源渠道：HN Show HN
> 标签：author_Rucadi, story_50415219, show_hn
> 最新指标：点赞=3 · 评论=1 · engagement_velocity=3

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-11-09T09:39:29+08:00 | HN Show HN | 点赞=3 · 评论=1 · engagement_velocity=3 | [[20-语料/posts/hn_show/2026-11-09/acdf5674b59d8009_Show-HN-FELF-–-AppImage-like-single-binaries-witho]] |

## 摘要正文

Hello HN!I've always had a bad time redistributing programs that use shared libraries, AppImage in my opinion does too much, and a container is an overkill - not always integrates smoothly.I've moved to nix since long ago, but redistributing between nix and other distros or vice versa it's still a pain in the ass, more so if you want to run an alien app in nix or a nix app without the package manger in any other distro.For that, with the help of Claude, I've implemented a format that deduces at pack-time all the shared libraries a program needs, puts them, together with its own glibc and a patched dynamic linker into a single executable.This means that you don't actually need a runtime nor any special capability, it can run inside a FROM SCRATCH docker, alpine linux etc... And it also supports coreutils-like multiple programs accessible via symlinks, so it is a good fit for that purpose.You can just use:> felf pack $(which git) --output git.felfand you'll have already a git binary that works everywhere, no matter which distro you are building this from. This only packs the binary and their dependencies.Essentially, the effect is similar as if you LD_PRELOAD's all the libraries that…
