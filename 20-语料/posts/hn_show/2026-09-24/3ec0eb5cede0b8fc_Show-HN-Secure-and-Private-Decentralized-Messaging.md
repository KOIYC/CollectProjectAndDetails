---
type: "corpus"
item_id: "3ec0eb5cede0b8fc"
title: "Show HN: Secure and Private Decentralized Messaging over Git and WebRTC"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49830569"
project_url: "https://glitr.io/docs/technical/roadmap"
author: "Screen8774"
published_at: "2026-09-24T13:50:37Z"
captured_at: "2026-09-24T23:57:22+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-24"
pub_day: "2026-09-24"
tags:
  - 语料
  - hn_show
  - author_Screen8774
  - story_49830569
  - show_hn
metrics: {"points": 2, "comments": 0, "engagement_velocity": 2}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:3d"
---

# Show HN: Secure and Private Decentralized Messaging over Git and WebRTC

> [!info] 一句话导读
> Skip to main content

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49830569>
> 指标：点赞=2 · 评论=0 · engagement_velocity=2
> 作者：Screen8774　|　发布：2026-09-24T13:50:37Z
> 项目链接：<https://glitr.io/docs/technical/roadmap>
> 采集：2026-09-24T23:57:22+08:00　|　id：`3ec0eb5cede0b8fc`

## 正文

Skip to main content
Glitr How-tos How it works Technical Try Glitr
 Open Glitr
Documentation
 Get started
 What Glitr is
 Install
 Talk now
 First conversation
How-tos
 Connect your repository
 Git remotes
 Add a contact
 Send and receive
 Live vs offline
 Another device
 Git hosts
 Troubleshooting
How it works
Technical
 Architecture
 Data structures
 Roadmap
Try Glitr
Legal
Technical
 Roadmap
 On this page
 Glitr Roadmap
This document is a work in progress and not in sync with the implementation and capabilities demonstrated by the live app.
Important disclaimer
 Glitr is ambitious, and the architecture is different from a typical messenger: a git mailbox you own, plus live WebRTC when both people are online. If it lands, it should look and behave like a mainstream messaging app.
 It is not finished. The messenger is closed-source and unaudited, so you cannot review the product the way you would an open project. This site and the app are shared for testing, feedback, and demo only. If you are unsure, this app is not for you. Reach out for clarity on any detail instead of treating the documentation as an audit. Please use responsibly.
 The goal is messaging without a Glitr account or a required install: you host your own data. User mistakes are a real risk in that model. Outside-the-box thinking is not a reason to trust it. Please use responsibly.
No messaging system is completely secure. Rather than score Glitr against another app, this page lists the features and practices that would make a messenger as strong as it can be, then shows how close this project is.
Draft requirements
 This is the initial draft: a list detailed enough to turn into a plan. Nothing here claims to be better than every other solution. The useful question is what people actually need, and how close Glitr can get.
 Feel free to reach out to have items added, removed, or updated.
Requirements ​
Technical requirements ​
P2P — no central Glitr server for exchanging messages
End to end encryption — intercepted payloads should not be readable
Forward secrecy — a compromised key should not decrypt past messages
Key management — you hold your own keys; there is no central key authority
Encrypted storage — messages stay sealed on the device
Secure signaling — the first connection between peers is established securely
Anonymity — you can talk without revealing who you are
Deniable authentication — participants can still be confident a message is authentic
Keys per contact — each connection has its own keys
Onion style routing — origins stay hidden
User Experience requirements ​
Remove registration — no personal details required to start
Support multimedia — share animations and videos
Offline messaging — send encrypted messages while the other person is offline
Self-destructing messages — optional delete-after-time
Minimize metadata — hide who is talking to whom, and when
Optimistic requirements ​
Open source — so experts can audit the code and users can decide whether to trust it
Minimal infrastructure — fewer services to fail or attack
Regular security audits — find and fix issues promptly
Status ​
Glitr only.
done
in-progress
planned
n/a (this iteration dropped a prior approach)
Transport and architecture ​
 Item Description Status Notes
 P2P Live WebRTC is peer-to-peer. The git mailbox is push and poll through a host, not store-and-forward P2P. Live vs offline , live links
 PeerJS backend Not used. Signaling is git-brokered; live uses webrtc-core . Architecture
 Git backend The mailbox is a git repository you own. Git as your mailbox
 Minimal infrastructure No Glitr chat server. You still need a git host, ICE, and optionally a CORS proxy. Architecture
 Onion style routing Git mailbox traffic can go over Tor. Live WebRTC cannot. An optional live path is chaining distinct TURN servers — not a built-in onion network. Live links , git mailbox , WebRTC and onion routing
 Encryption and keys ​
 Item Description Status Notes
 End to end encryption Payloads are encrypted to a contact so a git host is not reading the thread. Signal and post-quantum
 Cascading cipher AES → Signal → PQXDH (inner), then RSA hybrid → ML-KEM (outer). Signal and post-quantum
 Forward secrecy Double Ratchet is documented. The product is unaudited. Signal and post-quantum
 Key management You hold the connect password, git tokens, and profile/protocol keys. There is no full key-management UX. Data structures
 Keys per contact One ProtocolSession (ratchet state) per contact. Data structures
 Encrypted storage Sealed collections use Argon2id then AES-GCM on flush. Architecture
 Secure signaling Inner SDP is cascaded to the contact. ICE/STUN still exist. Live links
 Deniable authentication Not claimed on product crypto pages. —
 Privacy ​
 Item Description Status Notes
 Anonymity Listed as a requirement. Product docs currently disclaim it. What Glitr is
 Minimize metadata Bodies are sealed. A host can still see activity, access, and IPs. Encryption visibility
 Remove registration No Glitr account and no phone-number directory. What Glitr is
 Remove installation Browser-first. PWA and desktop install are still documented. Install
 Messaging and UX ​
 Item Description Status Notes
 Offline messaging Git-URL contacts can send while the other person is offline. Pair now has no mailbox fallback. Live vs offline
 Support multimedia Live and git-path file attachments. Voice and video on an open live link. Live links
 Group messaging Fan-out groups: one mailbox per member, groupId on send/ingest. Data structures
 Self-destructing messages Not in the data model. —
 Trust and documentation ​
 Item Description Status Notes
 Open source The Signal handshake library is public. The rest of the messenger is not. Architecture , signal-protocol
 Threat model A one-line host-vs-content split exists. A dedicated draft is still WIP. Encryption visibility
 Formal verification Not claimed for the messenger. —
 Regular security audits Closed-source. No independent audit. —
 Developer documentation Architecture, records, and Try pages. App source is not published. Architecture , data structures
 User documentation Start, how-tos, and how-it-works. Documentation
How we got here ​
The feature matrix below compares three positive-intentions messengers. If you lined them up on one axis, the useful label would be code transparency — not a simple open vs closed split. Cybersecurity hides details by complexity even when the source is public.
positive-intentions/chat ​
The first iteration: an open-source, browser-only messenger with no registration and no required install. It is plain JavaScript, uses the browser's built-in crypto, and can run from index.html or a static host such as GitHub Pages. A hosted copy exists to help people start. This code predates AI-assisted slop — there was slop before that too. Explaining it while it was being built was hard because the subject is dense.
Research side-projects and proofs of concept branched from this work. They show up again in the feature matrix.
Key learnings:
Code quality and documentation needed to improve throughout.
Getting started had to be easier.
"Pure JavaScript" is not enough.
Branding was weak.
"Build it and they will come" does not work in cybersecurity.
More:
Chat project
Source
Enkrypted Chat ​
Feedback from the first iteration led to a second app, structured so pieces could be built and tested in isolation. It uses Webpack 5 module federation. The result is much more complex than iteration-1, and harder to explain.
That work also produced several micro-apps, compared in the feature matrix below.
Key learnings:
A browser-only JavaScript stack has real limits.
A self-authored security audit or formal verification does not count — especially if AI wrote it.
Open source is not sustainable at this stage.
Better UX earns more useful feedback than a demo, source, and docs alone.
More:
Getting started
Whitepaper
Glitr ​
This site is the third iteration: a different stack in the same direction. Glitr is a Rust implementation and replaces PeerJS with a git mailbox you own. It is the latest positive-intentions messenger, and it is still unfinished.
This iteration aims to be the strongest version of the idea so far. It is a work in progress.
More:
Documentation
Architecture
Feature Matrix ​
Glossary ​
The matrix compares three iterations of the same idea.
Iteration App
 iteration-1 positive-intentions/chat
 iteration-2 Enkrypted Chat
 iteration-3 Glitr
shipped as documented
partial, limited, or self-authored only
absent / not claimed
Matrix ​
 Transport and architecture ​
 iteration-1 (positive-intentions/chat) iteration-2 (Enkrypted Chat) iteration-3 (Glitr)
 Feature iteration-1 iteration-2 iteration-3
 P2P
 PeerJS backend
 Git backend
 Minimal infrastructure
 Onion style routing
 Encryption and keys ​
 iteration-1 (positive-intentions/chat) iteration-2 (Enkrypted Chat) iteration-3 (Glitr)
 Feature iteration-1 iteration-2 iteration-3
 End to end encryption
 Cascading cipher
 Forward secrecy
 Key management
 Keys per contact
 Encrypted storage
 Secure signaling
 Deniable authentication
 Privacy ​
 iteration-1 (positive-intentions/chat) iteration-2 (Enkrypted Chat) iteration-3 (Glitr)
 Feature iteration-1 iteration-2 iteration-3
 Anonymity
 Minimize metadata
 Remove registration
 Remove installation
 Messaging and UX ​
 iteration-1 (positive-intentions/chat) iteration-2 (Enkrypted Chat) iteration-3 (Glitr)
 Feature iteration-1 iteration-2 iteration-3
 Offline messaging
 Support multimedia
 Group messaging
 Self-destructing messages
 Trust and documentation ​
 iteration-1 (positive-intentions/chat) iteration-2 (Enkrypted Chat) iteration-3 (Glitr)
 Feature iteration-1 iteration-2 iteration-3
 Open source
 Threat model
 Formal verification
 Regular security audits
 Developer documentation
 User documentation
FAQ ​
Why git?
Self-hosting is a common recommendation for secure messaging. You do not have to run your own server: pick a git host (GitHub, GitLab, and similar) or host the remote yourself.
Serverless WebRTC?
A connection can be made without a backend, as described in this issue .
Demo
Ready for production?
No. The product aims at a secure experience, but it cannot be audited or reviewed. Shared for testing, feedback, and demo purposes only.
EU Chat Control?
There is no Glitr account, no central chat server, and cryptography runs on the client. This older post is about a previous iteration; the mechanics are still similar.
Threat model?
A dedicated draft is still a work in progress. Too much of the product is unfinished to publish one yet.
The messenger is closed-source and unaudited, so you should not have to take anyone's word for it. The app does not require sensitive details. Do not use any when you try it.
Open source?
Glitr is not open source yet. That goes against the usual cybersecurity advice, and it is a goal, not a current claim. Older iterations and the Signal handshake library are public. glitr.io itself is closed-source.
Where can I find out more?
https://positive-intentions.com/
https://www.reddit.com/r/positive_intentions
Reach out for clarity instead of treating the docs as an audit.
Previous
 Data structures
 Next
 Overview
Requirements Technical requirements
 User Experience requirements
 Optimistic requirements
Status Transport and architecture
 Encryption and keys
 Privacy
 Messaging and UX
 Trust and documentation
How we got here positive-intentions/chat
 Enkrypted Chat
 Glitr
Feature Matrix Glossary
 Matrix
FAQ
Product
 Open Glitr
 Get started
 How-tos
 Try Glitr
Learn
 How it works
 Architecture
 Data structures
 Encryption
 Signal Protocol
Legal
 Terms and privacy
 Mastodon
Copyright © 2026 Glitr, part of positive-intentions . Built with positivity. Research and development — subject to change.

## 关联链接

- https://positive-intentions.com/
- https://www.reddit.com/r/positive_intentions

## 导航

- 项目页：[[10-项目/glitr.io_9a237422]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
