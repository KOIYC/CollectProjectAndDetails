---
type: "corpus"
item_id: "4fe889b1c5b41526"
title: "Show HN: Built end-to-end encrypted messenger – public source"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49877983"
project_url: "https://chat.markero.eu/"
author: "bugas"
published_at: "2026-09-28T13:52:50Z"
captured_at: "2026-09-29T09:42:56+08:00"
lang: "en"
kind: "post"
topic: "开发者工具"
shard: "2026-09-29"
pub_day: "2026-09-28"
tags:
  - 语料
  - hn_show
  - author_bugas
  - story_49877983
  - show_hn
metrics: {"points": 2, "comments": 1, "engagement_velocity": 2}
comments_count: 1
comments_total: 1
discovered_via: "hn:show_hn:3d"
---

# Show HN: Built end-to-end encrypted messenger – public source

> [!info] 一句话导读
> without the trust issues.

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49877983>
> 指标：点赞=2 · 评论=1 · engagement_velocity=2
> 作者：bugas　|　发布：2026-09-28T13:52:50Z
> 项目链接：<https://chat.markero.eu/>
> 采集：2026-09-29T09:42:56+08:00　|　id：`4fe889b1c5b41526`

## 正文

Markero
Features
 Security
 Blog
 Status
 Log in
 Create account
Private messaging,
without the trust issues.
End-to-end encrypted chat with no email and no phone number . Messages are encrypted in your browser before they reach our servers — we can't read them, and neither can anyone else. Just pick a username.
Create your account — free
 Android app
 How it works
No email · No phone number · Takes about 2 minutes · Open source (AGPL)
PGP Curve25519
 Encryption standard
2FA always on
 TOTP required for every account
Zero access
 We store ciphertext, nothing else
EU hosted
 Servers in the European Union
How it works
Everything sensitive happens on your device. The server is a courier that can't open the envelopes it carries.
Keys stay with you
When you sign up, your browser generates a PGP keypair using Curve25519. Your private key is encrypted with your TOTP secret, which itself is encrypted with your password. It never touches our servers unencrypted.
Logging in needs two factors
Every account requires TOTP two-factor authentication. Your key only unlocks with your password and your authenticator app. Recovery codes are provided as a backup.
Media and files, same rules
Photos, voice messages and documents up to 10 MB are encrypted before upload and decrypted only on the recipient's device. Nothing is ever stored in plaintext.
Open source
The source code is publicly available on our own Git instance, so the encryption can be independently reviewed. Zero claims you have to take on faith.
# What we store
username
argon2(password)
public_key
ciphertext(messages, files)
# What we don't
password (plaintext)
private_key (plaintext)
message contents
email address
phone number
IP logs
Why end-to-end encryption matters
Most messaging apps are "encrypted in transit" — the message is protected while travelling, but readable by the company that runs the server. End-to-end encryption is different.
🔐
Encrypted before upload
Messages are locked on your device with a key only you and the recipient have. The server only ever sees ciphertext — scrambled data it cannot decrypt.
🙅
We can't read it, even if asked
Because we hold no plaintext and no decryption keys, there is nothing we could hand over to a government or an attacker. Zero-access isn't a promise, it's a technical property.
🪪
No email, no phone number
Most messengers tie your account to your phone number, which is linked to your identity. Markero only asks for a username, so your conversations can't be tied to your real-world identity.
Markero vs other messengers
How Markero compares on the things that matter for privacy.
Markero
 WhatsApp
 Signal
 Telegram
End-to-end encrypted by default
 Yes
 Yes
 Yes
 No (opt-in)
Requires email or phone number
 No
 Phone
 Phone
 Phone
Zero-access (server can't read)
 Yes
 No
 No
 No
Mandatory two-factor auth
 Yes
 Optional
 Optional
 Optional
EU hosted (GDPR)
 Yes
 US
 US
 Various
Free forever
 Yes
 Yes
 Yes
 Yes
Open source
 Yes
 No
 Yes
 No
Who Markero is for
If any of these sound like you, Markero was built with you in mind.
Journalists & sources
Communicate with sources without a phone number connecting the thread to you. Your private key never leaves your device.
Privacy-conscious families
Share photos, voice notes and everyday messages knowing the service provider can't read them — even by accident.
Teams that need confidentiality
Group chats with end-to-end encryption, message requests to stop spam, and full session control across devices.
Get started in a minute
You don't need to be technical to use Markero. The encryption happens automatically.
Step 1
Create an account
Pick a username and a password. No email, no phone number. Your browser generates your encryption keypair on the spot.
Step 2
Scan the QR code
Add your account to an authenticator app for mandatory two-factor authentication. It takes about 30 seconds.
Step 3
Start messaging
Message anyone on Markero or create a group. Everything is encrypted automatically — no settings to configure, no keys to manage.
What you'll need: an authenticator app — Google Authenticator, Aegis, 1Password or similar. They're free and take a minute to set up.
Create your account
 Read the threat model
Frequently asked questions
The honest answers about how Markero protects your messages.
Is Markero really end-to-end encrypted?
Yes. Messages are encrypted in your browser with a PGP keypair before they reach our servers. We store only ciphertext and cannot read your messages — and neither can anyone who compromises the server.
Do I need an email or phone number to sign up?
No. Markero only asks for a username and a password. No email address, no phone number — which means no way to link your account to your identity.
Do I need to install an app?
No. Markero runs in your browser — create an account and start chatting without installing anything. There's also an Android app if you prefer, with native push notifications.
How does Markero keep my account secure?
Two-factor authentication (TOTP) is mandatory for every account. Your private key only unlocks with your password and your authenticator app. Recovery codes are provided as a backup if you lose your device.
What encryption does Markero use?
Markero uses PGP with a Curve25519 keypair. Passwords are stored as argon2 hashes. Your private key is never transmitted, and messages are encrypted before they leave your device.
Can I use Markero on Android?
Yes. Markero has a native Android app as well as a browser-based web client. Both use the same end-to-end encryption, and you can sign in on multiple devices.
What makes Markero different from WhatsApp or Telegram?
Markero is zero-access: we store only encrypted ciphertext and cannot read your messages. It does not require an email or phone number, encryption keys never touch our servers, and two-factor authentication is mandatory for every account.
Is Markero free?
Yes. Markero is free forever, with end-to-end encrypted chats, group messaging, voice calls, and file sharing included. There are no premium tiers and no ads.
Where are Markero servers hosted?
Markero servers are hosted in the European Union, which means your data is covered by GDPR protections.
Create your account in two minutes.
No email, no phone number. Works in your browser and on Android. Free forever.
Create your account
 Open source (AGPL-3.0) — review the code
© 2026 Markero
Features
 Security
 Blog
 Changelog
 Privacy
 Status
 Android app
 Source

## 评论（1/1）

> **bugas** · 2026-09-28T13:52:50.000Z　
> Hey guys,I built as title says E2EE chat platform chat.markero.eu and its public source sits at https://git.markero.eu/main/markero-chat - feel free to fork it, clone it, break it, send PRs.- Project took 4 months to mature with breaks. It includes android AAB project files if you wish to submit it to Play store. Firebase is integrated.- Not going to lie - On AI: I used it as coding assistant. Every change was reviewed and tested - there are 84 backend + 13 WebSocket + 6 crypto tests in the repo (./tests/run-all.sh).- What I'm looking for:Holes in the threat model: chat.markero.eu/security - what's misleading, missing?Code review - especially the key-wrapping and message-encryption paths.UX/UI feedback from actually using it.- We will not beat Telegram or Signal but we can stand aside it.- Let me know what you think, not looking for promotion but as independent project looking for holes and how to solve them, criticism accepted, but would rather want a comment on how to improve it.
> - Where I'm not claiming victory - Signal is excellent. I'm not trying to beat it, the trade off is different.- If you find a vulnerability, please report it privately, or make PR request.Thank you guys and girls for reading this! It means a lot!P.S- It will probably get a lot of hate, but I'm ready to improve it. People can host it themselves and have secure chats with they guys, we are not beating Telegram/Signal we are standing belong them. Thanks again!

## 导航

- 项目页：[[10-项目/chat.markero.eu_ec7a5cc6]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`开发者工具`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
