---
type: "corpus"
item_id: "5e6df9e7402f2975"
title: "Show HN: Presence.el Online status and simple messaging for Emacs"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49775425"
project_url: "https://git.andros.dev/andros/presence.el"
author: "andros"
published_at: "2026-09-20T13:00:26Z"
captured_at: "2026-09-21T09:44:03+08:00"
lang: "en"
kind: "post"
topic: "开发者工具"
shard: "2026-09-21"
pub_day: "2026-09-20"
tags:
  - 语料
  - hn_show
  - author_andros
  - story_49775425
  - show_hn
metrics: {"points": 2, "comments": 0, "engagement_velocity": 2}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:3d"
---

# Show HN: Presence.el Online status and simple messaging for Emacs

> [!info] 一句话导读
> andros / presence.el

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49775425>
> 指标：点赞=2 · 评论=0 · engagement_velocity=2
> 作者：andros　|　发布：2026-09-20T13:00:26Z
> 项目链接：<https://git.andros.dev/andros/presence.el>
> 采集：2026-09-21T09:44:03+08:00　|　id：`5e6df9e7402f2975`

## 正文

Explore
Help
Sign in
andros / presence.el
Watch
1
Star
0
Fork
You've already forked presence.el
0
Code
Issues
Pull requests
Projects
Releases
Packages
Wiki
Activity
Actions
See when your friends are online, away or offline, and send and read simple messages, right from Emacs.
24 commits
1 branch
0 tags
295 KiB
Emacs Lisp
100%
main
Find a file
HTTPS
Download ZIP
 Download TAR.GZ
 Download BUNDLE
Open with VS Code
Open with VSCodium
Open with Intellij IDEA
Cite this repository
BibTeX
Cancel
Exact
Exact
Union
RegExp
Andros Fenollosa
ce625c7b9c
Add presence-message-functions hook for incoming messages
2026-09-20 11:23:34 +02:00
images
Update
2026-09-20 10:59:26 +02:00
LICENSE
Add README, LICENSE and gitignore
2026-09-18 16:48:12 +02:00
presence.el
Add presence-message-functions hook for incoming messages
2026-09-20 11:23:34 +02:00
README.md
Add presence-message-functions hook for incoming messages
2026-09-20 11:23:34 +02:00
README.md
presence.el
See when your friends are online, away or offline, and send and read simple messages, right from Emacs.
The 🟢 3/4 on the right of the mode line means you are online and three
of your four friends are around. Legend: 🟢 online · ⛔ busy · 💤 away ·
 🔴 offline.
Overview
This package brings a lightweight presence indicator into Emacs. It keeps a WebSocket connection open to a presence server and reports your own status while listening for the status of the friends you follow.
Each participant registers once and receives a stable ID. You share that ID with the people you want to stay in touch with, add their IDs to your friends list, and Emacs shows who is around without leaving the editor.
Registration
Before configuring the package you need an ID. Run M-x presence-register once: it contacts the server and returns your presence-user-id , also copying it to the kill ring so you can paste it straight into your configuration as shown below. This is a one time step; afterwards you only need the connection commands.
Configuration
The :vc keyword installs the package straight from the repository (Emacs 29+).
( use-package presence
 :vc ( :url "https://git.andros.dev/andros/presence.el" )
 :custom
 ( presence-server-url "wss://presence.andros.dev/ws" )
 ;; Your ID, assigned by the server on registration.
 ( presence-user-id "3f9a1c7e5b2d8a40" )
 ;; Friends: every ID must be paired with a local alias.
 ;; Aliases live only here, they are never sent over the network.
 ( presence-friends
 ' (( "6150ac2c57030a6a" . "Andros" ))) ; it's me
 ;; Automatic status.
 ( presence-away-after 600 )
 ;; Optional: always report online, ignoring the idle timer.
 ( presence-always-online nil )
 ;; Seconds to wait before reconnecting after a dropped connection.
 ( presence-reconnect-interval 5 )
 :config
 ;; Enable the global mode on startup so you connect right away.
 ( presence-mode 1 ))
 Usage
presence-mode is a global minor mode: enable it once with M-x presence-mode and it applies to your whole Emacs session, across every buffer. It connects to the server and starts broadcasting your status. Your friends appear under the local alias you gave each ID in presence-friends . When you stay idle longer than presence-away-after seconds you are marked as away, and you return to online as soon as you resume activity. Disable the mode to disconnect.
Set presence-always-online to t when you want to appear online at all times: the idle timer is ignored and you are never marked as away automatically.
Command
 Description
M-x presence-register
 Register with the server and return your presence-user-id (run once, before configuring)
M-x presence-mode
 Connect to the server and broadcast your status
M-x presence-list-friends
 Open a buffer listing your friends and their current status
M-x presence-set-status
 Pick your status manually: online, busy or away
M-x presence-send-message
 Send a short message to one of your friends
M-x presence-broadcast
 Send a short message to every friend at once
presence-set-status overrides the automatic state until you change it again or reconnect.
Incoming messages are shown in the echo area and appended to the *presence* buffer, so you can read back the conversation.
If the connection drops, Presence reconnects on its own after presence-reconnect-interval seconds, for as long as the mode stays enabled.
Mode line
While presence-mode is active it shows a compact indicator in the mode line: an emoji for your current state followed by how many friends are around (online, busy or away) out of the total.
🟢2/3
 Your state maps to an emoji:
Emoji
 State
🟢
 online
⛔
 busy
💤
 away
🔴
 offline
So ⛔2/3 means you are busy and two of your three friends are around. The default format begins with a space so the indicator does not stick to other mode-line segments. Customize the template with presence-mode-line-format , or set it to nil to hide the indicator entirely:
;; Just your state emoji, without the friends counter.
 ( setq presence-mode-line-format ' ( presence-state-indicator ))
;; Or hide it completely.
 ( setq presence-mode-line-format nil )
 Recipes
Because statuses and messages are just function calls, you can wire them into anything Emacs already knows about. presence-broadcast sends a message to every friend at once, and the rest build on it.
Native desktop notifications for incoming messages
Every incoming message runs presence-message-functions with the sender's alias, the message body and the sender's id, so you can surface it as a native notification:
( add-hook 'presence-message-functions
 ( lambda ( alias body _id )
 ( cond
 ;; Linux / BSD via D-Bus.
 (( fboundp 'notifications-notify )
 ( notifications-notify :title alias :body body ))
 ;; macOS via terminal-notifier.
 (( executable-find "terminal-notifier" )
 ( call-process "terminal-notifier" nil 0 nil
 "-title" alias "-message" body )))))
 Invite everyone to a virtual coffee
( defun my/presence-coffee ()
 "Invite all your friends to a virtual coffee break."
 ( interactive )
 ( presence-broadcast "☕ virtual coffee in 5 minutes?" ))
 Announce your Magit pushes
( add-hook 'magit-post-push-hook
 ( lambda () ( presence-broadcast "just pushed 🚀" )))
 Share the song you are listening to
;; `my/now-playing` returns the current track as a string
 ;; (via EMMS, mpris, or `osascript` on macOS).
 ;; Broadcast only when the track changes, to avoid flooding your friends.
 ( defvar my/presence-last-track nil )
( run-with-timer 0 30
 ( lambda ()
 ( when-let (( track ( my/now-playing )))
 ( unless ( equal track my/presence-last-track )
 ( setq my/presence-last-track track )
 ( presence-broadcast ( format "🎧 %s" track ))))))
 Show what you are hacking on
( add-hook 'find-file-hook
 ( lambda ()
 ( when-let (( p ( project-current )))
 ( presence-broadcast
 ( format "hacking on %s" ( project-name p ))))))
 Go busy during a focus session
( add-hook 'org-pomodoro-started-hook
 ( lambda () ( presence-set-status 'busy )))
 ( add-hook 'org-pomodoro-finished-hook
 ( lambda () ( presence-set-status 'online )))
 Development
The reference backend lives at presence-server .
This section documents the wire protocol so you can build a compatible server. Every frame is a single JSON object with a type field. The transport is a plain WebSocket at presence-server-url .
Registering
Before connecting for the first time, presence-register asks the server for an ID:
--> { "type" : "register" }
 <-- { "type" : "registered" , "id" : "3f9a1c7e5b2d8a40" }
 The returned id is stored as presence-user-id . Aliases are never part of the protocol: each client maps every ID to a local alias in presence-friends , so the server only ever deals with IDs.
Connecting
On presence-mode the client opens the socket and greets the server with its ID and the friends it wants to follow:
--> { "type" : "hello" , "id" : "3f9a1c7e5b2d8a40" ,
 "subscribe" : [ "a17c44e09b3f5d21" , "c0ffee42deadbeef" ]}
 The server answers with a snapshot of the subscribed friends:
<-- { "type" : "roster" ,
 "friends" : [
 { "id" : "a17c44e09b3f5d21" , "state" : "online" },
 { "id" : "c0ffee42deadbeef" , "state" : "away" }
 ]}
 Sending your status
When your state changes (manually or through the idle timer) the client pushes:
--> { "type" : "status" , "state" : "busy" }
 state is one of online , busy , away or offline . That is the whole payload: a status carries no free text note.
Receiving updates
The server broadcasts a friend's change to every subscriber:
<-- { "type" : "status" , "from" : "c0ffee42deadbeef" , "state" : "online" }
 Messages
To send a short message to a friend:
--> { "type" : "message" , "to" : "c0ffee42deadbeef" , "body" : "☕ virtual coffee in 5 minutes?" }
 Incoming messages arrive the same way, identified only by the sender ID (the client resolves the alias locally):
<-- { "type" : "message" , "from" : "a17c44e09b3f5d21" , "body" : "on my way" }
 Keepalive
The client answers server ping frames to keep the connection alive:
<-- { "type" : "ping" }
 --> { "type" : "pong" }
 Disconnection
There is no disconnect frame. Disconnection is signaled by the WebSocket close: when a client's socket closes, or it stops answering ping , the server marks it offline and broadcasts that status to its subscribers. On the client side, a dropped socket triggers an automatic reconnect after presence-reconnect-interval seconds.
Unknown type values should be ignored so the protocol can grow.
Contributing
Contributions are welcome! Please see the contribution guidelines for instructions on how to submit issues or pull requests.
License
GNU General Public License v3.0 or later
Powered by Forgejo
Version:
10.0.3
Page: 66ms
 Template: 16ms
English
Bahasa Indonesia
Deutsch
English
Español
Esperanto
Filipino
Français
Italiano
Latviešu
Magyar nyelv
Nederlands
Plattdüütsch
Polski
Português de Portugal
Português do Brasil
Slovenščina
Suomi
Svenska
Türkçe
Čeština
Ελληνικά
Български
Русский
Українська
فارسی
日本語
简体中文
繁體中文（台灣）
繁體中文（香港）
한국어
Licenses
 API

## 导航

- 项目页：[[10-项目/git.andros.dev_63440684]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`开发者工具`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
