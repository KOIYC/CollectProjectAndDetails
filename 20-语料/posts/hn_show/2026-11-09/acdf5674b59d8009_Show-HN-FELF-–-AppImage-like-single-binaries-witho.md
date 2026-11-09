---
type: "corpus"
item_id: "acdf5674b59d8009"
title: "Show HN: FELF – AppImage-like single binaries without FUSE, root, or a runtime"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50415219"
project_url: "https://github.com/Rucadi/FELF"
author: "Rucadi"
published_at: "2026-11-08T17:26:45Z"
captured_at: "2026-11-09T09:39:29+08:00"
lang: "en"
kind: "post"
topic: "开发者工具"
shard: "2026-11-09"
pub_day: "2026-11-08"
tags:
  - 语料
  - hn_show
  - author_Rucadi
  - story_50415219
  - show_hn
metrics: {"points": 3, "comments": 1, "engagement_velocity": 3}
comments_count: 1
comments_total: 1
discovered_via: "hn:show_hn:3d"
---

# Show HN: FELF – AppImage-like single binaries without FUSE, root, or a runtime

> [!info] 一句话导读
> Hello HN!I've always had a bad time redistributing programs that use shared libraries, AppImage in my opinion does too much, and a container is an overkill - no…

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50415219>
> 指标：点赞=3 · 评论=1 · engagement_velocity=3
> 作者：Rucadi　|　发布：2026-11-08T17:26:45Z
> 项目链接：<https://github.com/Rucadi/FELF>
> 采集：2026-11-09T09:39:29+08:00　|　id：`acdf5674b59d8009`

## 正文

Hello HN!I've always had a bad time redistributing programs that use shared libraries, AppImage in my opinion does too much, and a container is an overkill - not always integrates smoothly.I've moved to nix since long ago, but redistributing between nix and other distros or vice versa it's still a pain in the ass, more so if you want to run an alien app in nix or a nix app without the package manger in any other distro.For that, with the help of Claude, I've implemented a format that deduces at pack-time all the shared libraries a program needs, puts them, together with its own glibc and a patched dynamic linker into a single executable.This means that you don't actually need a runtime nor any special capability, it can run inside a FROM SCRATCH docker, alpine linux etc... And it also supports coreutils-like multiple programs accessible via symlinks, so it is a good fit for that purpose.You can just use:> felf pack $(which git) --output git.felfand you'll have already a git binary that works everywhere, no matter which distro you are building this from. This only packs the binary and their dependencies.Essentially, the effect is similar as if you LD_PRELOAD's all the libraries that it requires.In the end, we have been fighting these demons since long long ago, chroots/docker/appimage/flatpack/nix etc...So this xkcd applies: https://xkcd.com/927/I'm happy to share the project, I hope it inspires new discoveries/tools in this regard!

## 评论（1/1）

> **Imustaskforhelp** · 2026-11-08T19:26:23.000Z　
> This is really beautiful from first glance.I had built appseed[0] inspired by zapps.app (curious what you think about that)and although, I could get some apps like bun and others to work statically using that. I struggled to make it work on things like OBS studio and it certainly had a lot of limitations with how it worked.It had a different approach of working where instead of pushing everything into a single binary, you had the .so file outside in an external filesystem of binary, could something like this work within FELF as well theoretically (for de-duplication purposes perhaps)?It seems that your experiment can work for almost every app including OBS and other complicated applications. I am rather really impressed by it and I will try to try it!I wonder if games can now be FELF'd as well and we can have containerized games into single binaries maybe, where I can just "run" games.What do you personally think could be the largest benefits of this approach and if there are any further things that you are pursuing in this area?This is really impressive work and thank you for releasing it! Have a nice day :-D[0]: https://github.com/serJaimeLannister/appseed

## 关联链接

- https://xkcd.com/927/I

## 导航

- 项目页：[[10-项目/github.com_d4938088]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`开发者工具`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
