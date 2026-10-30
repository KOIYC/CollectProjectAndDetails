---
type: "corpus"
item_id: "5687f481ecb9c2c8"
title: "Show HN: Sidekeys – Turn an iPhone into a Mac display and agent control deck"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50295597"
project_url: "https://sidekeysapp.com/"
author: "cmillstein"
published_at: "2026-10-29T20:42:21Z"
captured_at: "2026-10-30T09:46:09+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-10-30"
pub_day: "2026-10-29"
tags:
  - 语料
  - hn_show
  - author_cmillstein
  - story_50295597
  - show_hn
metrics: {"points": 2, "comments": 0, "engagement_velocity": 2}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:3d"
---

# Show HN: Sidekeys – Turn an iPhone into a Mac display and agent control deck

> [!info] 一句话导读
> Your iPhone, beside your Mac.

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50295597>
> 指标：点赞=2 · 评论=0 · engagement_velocity=2
> 作者：cmillstein　|　发布：2026-10-29T20:42:21Z
> 项目链接：<https://sidekeysapp.com/>
> 采集：2026-10-30T09:46:09+08:00　|　id：`5687f481ecb9c2c8`

## 正文

Skip to content
Sidekeys
Features
Pricing
FAQ
Join the beta
Your iPhone, beside your Mac.
Sidekeys turns your iPhone into a second screen for your Mac, and a control deck that knows what you're doing.
Email
Get the beta
I'd test on
 iPhone Duo
 iPhone
 iPad
The TestFlight beta is open. Enter your email and get the link instantly. Built for iPhone Duo, works with any iPhone or iPad.
Download the Mac app Free · Apple silicon · Setup guide
Xcode File Edit View Product Tue 9:41 AM
TaxCalculator.swift
Checkout
Cart.swift
LineItem.swift
TaxCalculator.swift
Receipt.swift
Tests
TaxCalculatorTests.swift
import Foundation
struct TaxCalculator {
 let rate: Decimal
/// Rounds half to even, like the receipt.
 func total ( for items: [ LineItem ]) -> Decimal {
 let subtotal = items. reduce ( 0 ) { $0 + $1.price }
 let tax = (subtotal * rate)
 . rounded (scale: 2 , .bankers)
 return subtotal + tax
 }
}
extension Decimal {
 func rounded (scale: Int ,
 _ mode: RoundingMode ) -> Decimal {
 var value = self , result = Decimal ()
 NSDecimalRound (&result, &value, scale, mode)
 return result
 }
}
Design review 12:04
MK Maya
JR Jordan
SL Sam
You You
Terminal Shell Edit View 9:41 AM
claude — ~/checkout
✻ Claude Code
> Fix the rounding bug in tax totals and add a test
⏺ Read( TaxCalculator.swift )
⏺ Update( TaxCalculator.swift )
⎿ - .rounded(.plain)
+ .rounded(scale: 2, .bankers)
⏺ Write( TaxCalculatorTests.swift )
⏺ Bash(npm test -- tax)
⎿ ✓ 12 tests passed
Design review 12:04
MK Maya
JR Jordan
SL Sam
You You
Meeting
Mute Muted
Camera
Share
Leave
Claude Code needs you
Wants to run: npm test
Approve Approved
One app, three jobs
More room. Fewer shortcuts to remember.
01 · Second screen
A second screen for your Mac.
Plug in your iPhone and your Mac gets a new display. Drag windows onto it, touch to click, scroll with two fingers, and type with the on-screen keyboard.
It's built for iPhone Duo's big inner screen, and it works on any iPhone or iPad.
Sharp Retina picture
Edge to edge, with your Mac's menu bar fully visible.
Low latency over USB‑C
One cable between your iPhone and your Mac.
Rotates with you
Rotate your phone and your Mac's display rotates with it.
Windows land where you are
New windows you open from the phone land on the phone.
Pinch to zoom
Zoom in on small text, right on the phone.
02 · A deck for every app
Keys that change with what you're doing.
Sidekeys shows keys for the app in front on your Mac: Xcode, Final Cut Pro, Figma, VS Code and more. One tap runs the shortcut you'd otherwise have to remember.
In a Zoom, Google Meet, Microsoft Teams or Slack call, the deck switches to big mute, camera and leave buttons that work even while the meeting window is buried behind your work.
Xcode
 Final Cut Pro
 Figma
 VS Code
 Meeting
Frontmost: Xcode
Run ⌘R
Stop ⌘.
Build ⌘B
Test ⌘U
Clean ⇧⌘K
Console ⇧⌘C
Breakpoints ⌘Y
Device Hub
Frontmost: Final Cut Pro
Play Space
Mark In I
Mark Out O
Blade B
Undo ⌘Z
Export ⌘E
Full Screen ⇧⌘F
Scrub
Frontmost: Figma
Move V
Frame F
Text T
Comment C
Pen P
Zoom to Fit ⇧1
Hide UI ⌘\
Export ⇧⌘E
Frontmost: VS Code
Run F5
Stop ⇧F5
Terminal ⌃`
Commands ⇧⌘P
Format ⇧⌥F
Find in Files ⇧⌘F
Git ⌃⇧G
Explorer ⇧⌘E
In a call
Mute
Camera
Leave
Raise Hand
Share
Chat
Illustration. On your phone, the deck switches by itself.
03 · Your AI agents, at a glance
See which agent needs you.
Running coding agents in the terminal? Sidekeys shows each one as a card: what it's working on, what finished, and what's waiting on you.
Approve a request or jump to its window with one tap.
Built for iPhone Duo
Sidekeys uses the iPhone Duo's vertical toolbar, fills the inner screen edge to edge, and works on the outer screen too.
How it works
Set up in a minute.
Download the Mac app
Get the free Sidekeys app for Mac from sidekeysapp.com/mac , and Sidekeys for iPhone from TestFlight during the beta.
Plug in your iPhone
Connect your iPhone to your Mac with a USB-C cable and open Sidekeys.
That's it
Your iPhone is now a display and a deck.
Pricing
Pay once. Keep it.
$9.99 once
Try everything free for 7 days. After that, unlock Sidekeys once for $9.99.
No subscription
No account
Family Sharing included
Mac app is free
Get the beta
 Buy on the web
Buy here or in the app, same price. A web purchase gives you a code that unlocks up to 5 of your devices.
Questions
Which iPhones does it work with?
Sidekeys is built for iPhone Duo's big inner screen, and it works on any iPhone or iPad. On iPhone Duo it also works on the outer screen.
Can I use my iPhone as a second monitor for my Mac?
Yes. Apple's Sidecar only works with iPad, so Sidekeys fills the gap: install the free Mac app, plug in your iPhone, and your Mac gets a real extra display you can drag windows onto, with touch, scrolling and typing. It works on iPad too.
How is Sidekeys different from Sidecar and iPhone Mirroring?
Sidecar turns an iPad into a Mac display, but not an iPhone. iPhone Mirroring goes the other way, showing your iPhone on your Mac. Sidekeys puts your Mac's screen on your iPhone or iPad, and adds a control deck for the app you're using and a dashboard for AI coding agents.
Does it work with Claude Code?
Yes. In the Mac app's menu, choose Agents, then Connect Claude Code. Every Claude Code session appears as a card on your phone, and you can approve or deny permission requests with one tap, seeing the actual command. If your phone isn't connected, approvals fall back to the normal terminal prompt.
Cable or Wi-Fi?
Either. A USB-C cable gives the lowest delay; use one that carries data, not a charge-only one. Over Wi-Fi, pair once (plug in the cable once, or type the code your iPhone shows), and from then on your iPhone connects on its own whenever Sidekeys is open nearby. Wi-Fi connections are encrypted end to end between your two devices.
Which Macs are supported?
A Mac with Apple silicon running macOS 27 or later, with the free Sidekeys app for Mac installed. Download it here .
The Mac app isn't on the Mac App Store because it creates a virtual display, which the Mac App Store doesn't allow. It's notarized by Apple and downloads straight from this site.
Is it a subscription?
No. Try every feature free for 7 days, then unlock Sidekeys once for $9.99. No subscription, no account.
Can my family use it?
Yes. The unlock works with Family Sharing, so people in your Apple Family Sharing group can use it too.
What happens to my data?
Your screen, touches and typing never leave your own devices: they go directly between your iPhone and your Mac. The apps have no analytics, ads, tracking or accounts. If you buy on the web or join the beta list, we keep only your email and purchase. Read the privacy policy .
Give your Mac a sidekick.
The beta is open. Enter your email and you're in.
Email
Get the beta
I'd test on
 iPhone Duo
 iPhone
 iPad
Download the Mac app Free · Apple silicon · Setup guide
Sidekeys
Mac download
Support
Contact
Privacy
© 2026 Sidekeys

## 导航

- 项目页：[[10-项目/sidekeysapp.com_ee27b7c8]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
