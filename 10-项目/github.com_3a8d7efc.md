---
type: "project"
title: "Show HN: Gmessages-TUI, Google Messages (RCS and SMS) in the Terminal"
project_url: "https://github.com/louisrubet/gmessages-tui"
first_seen: "2026-11-11T13:37:17+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_louis_
  - story_50443847
  - show_hn
lang: "en"
---

# Show HN: Gmessages-TUI, Google Messages (RCS and SMS) in the Terminal

> [!info] 一句话导读
> As a big TUI fan I've been complaining for a long time about not being able to read my Google Messages in a terminal. I wrote a client. It pairs with the Androi…

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://github.com/louisrubet/gmessages-tui>
> 首次收录：2026-11-11T13:37:17+08:00
> 来源渠道：HN Show HN
> 标签：author_louis_, story_50443847, show_hn
> 最新指标：点赞=2 · 评论=0 · engagement_velocity=2

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-11-11T13:37:17+08:00 | HN Show HN | 点赞=2 · 评论=0 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-11-11/1753165285a5cfeb_Show-HN-Gmessages-TUI,-Google-Messages-(RCS-and-SM]] |

## 摘要正文

As a big TUI fan I've been complaining for a long time about not being able to read my Google Messages in a terminal. I wrote a client. It pairs with the Android phone, Google connection then emoji, the phone must remain on. The client manages SMS and RCS and groups, images (if you have a kitty compatible terminal), reactions, archives, spam, trash, searches, notifications...Google Messages having no public interface, I wrote a specification https://github.com/louisrubet/gmessages-tui/tree/main/doc/pr... from the protocol decoded by mautrix-gmessages https://github.com/mautrix/gmessages in libgm https://github.com/mautrix/gmessages/tree/main/pkg/libgm. Thanks to you guys! This allowed me to write gmessages-proto, a clean-room client crate in Rust and a separated interface https://github.com/louisrubet/chat-tui-core I am reusing for another messenger. Messages are stored in a local encrypted database, whose key is stored in the system keystore.Installation through cargo is `cargo install --locked gmessages-tui`.There are deb, rpm and pacman packages if you prefer.Tested on Linux only, please dare to install it on macOS or Windows, and open GitHub tickets!
