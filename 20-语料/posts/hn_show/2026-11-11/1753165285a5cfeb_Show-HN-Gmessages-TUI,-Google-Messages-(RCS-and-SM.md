---
type: "corpus"
item_id: "1753165285a5cfeb"
title: "Show HN: Gmessages-TUI, Google Messages (RCS and SMS) in the Terminal"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50443847"
project_url: "https://github.com/louisrubet/gmessages-tui"
author: "louis_"
published_at: "2026-11-10T18:03:28Z"
captured_at: "2026-11-11T13:37:17+08:00"
lang: "en"
kind: "post"
topic: "开发者工具"
shard: "2026-11-11"
pub_day: "2026-11-10"
tags:
  - 语料
  - hn_show
  - author_louis_
  - story_50443847
  - show_hn
metrics: {"points": 2, "comments": 0, "engagement_velocity": 2}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:3d"
---

# Show HN: Gmessages-TUI, Google Messages (RCS and SMS) in the Terminal

> [!info] 一句话导读
> As a big TUI fan I've been complaining for a long time about not being able to read my Google Messages in a terminal. I wrote a client. It pairs with the Androi…

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50443847>
> 指标：点赞=2 · 评论=0 · engagement_velocity=2
> 作者：louis_　|　发布：2026-11-10T18:03:28Z
> 项目链接：<https://github.com/louisrubet/gmessages-tui>
> 采集：2026-11-11T13:37:17+08:00　|　id：`1753165285a5cfeb`

## 正文

As a big TUI fan I've been complaining for a long time about not being able to read my Google Messages in a terminal. I wrote a client. It pairs with the Android phone, Google connection then emoji, the phone must remain on. The client manages SMS and RCS and groups, images (if you have a kitty compatible terminal), reactions, archives, spam, trash, searches, notifications...Google Messages having no public interface, I wrote a specification https://github.com/louisrubet/gmessages-tui/tree/main/doc/pr... from the protocol decoded by mautrix-gmessages https://github.com/mautrix/gmessages in libgm https://github.com/mautrix/gmessages/tree/main/pkg/libgm. Thanks to you guys! This allowed me to write gmessages-proto, a clean-room client crate in Rust and a separated interface https://github.com/louisrubet/chat-tui-core I am reusing for another messenger. Messages are stored in a local encrypted database, whose key is stored in the system keystore.Installation through cargo is `cargo install --locked gmessages-tui`.There are deb, rpm and pacman packages if you prefer.Tested on Linux only, please dare to install it on macOS or Windows, and open GitHub tickets!

## 关联链接

- https://github.com/louisrubet/chat-tui-core
- https://github.com/louisrubet/gmessages-tui/tree/main/doc/pr...
- https://github.com/mautrix/gmessages
- https://github.com/mautrix/gmessages/tree/main/pkg/libgm.

## 导航

- 项目页：[[10-项目/github.com_3a8d7efc]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`开发者工具`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
