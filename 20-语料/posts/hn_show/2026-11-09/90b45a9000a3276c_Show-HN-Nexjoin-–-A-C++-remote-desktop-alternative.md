---
type: "corpus"
item_id: "90b45a9000a3276c"
title: "Show HN: Nexjoin – A C++ remote desktop alternative (Windows XP+, macOS 10.13)"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50415946"
project_url: "https://nexjoin.io/README.html"
author: "szigand"
published_at: "2026-11-08T18:57:22Z"
captured_at: "2026-11-09T09:39:29+08:00"
lang: "en"
kind: "post"
topic: "开发者工具"
shard: "2026-11-09"
pub_day: "2026-11-08"
tags:
  - 语料
  - hn_show
  - author_szigand
  - story_50415946
  - show_hn
metrics: {"points": 2, "comments": 1, "engagement_velocity": 2}
comments_count: 1
comments_total: 1
discovered_via: "hn:show_hn:3d"
---

# Show HN: Nexjoin – A C++ remote desktop alternative (Windows XP+, macOS 10.13)

> [!info] 一句话导读
> Rethinking Remote Desktop

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50415946>
> 指标：点赞=2 · 评论=1 · engagement_velocity=2
> 作者：szigand　|　发布：2026-11-08T18:57:22Z
> 项目链接：<https://nexjoin.io/README.html>
> 采集：2026-11-09T09:39:29+08:00　|　id：`90b45a9000a3276c`

## 正文

Rethinking Remote Desktop
 The Engine and Platforms
Display and Control
System and Network
Security, Personal Data, Privacy
Current State
Source Code Audit
Code Signing
Support
Open Source
Usage
Current Servers
Uninstallation
Contact
Download
Screenshots
Blog | LinkedIn | Contact | Download    [ English | Hungarian ]
Rethinking Remote Desktop
 Many years ago, as a former LogMeIn developer, starting my own remote desktop system from scratch seemed like an interesting idea and a good challenge, especially since there were more and more complaints about the existing ones. I saw no point in developing yet another identical system, but rethinking what I could, putting in new ideas, and polishing every detail with proper implementation - while respecting future users' time, nerves, and private data - seemed like a good task. It should just do its job simply, cleanly, and unnoticed as it should: removing distance, making remote work easier and a better experience, and simplifying connections while taking care of security. For now, this is what came out of it. This is just a first incarnation of the engine; many kinds of products can be born from this.
 Try it out, and if you like this direction, let's keep it alive together!
 The Engine and Platforms
 Modular, multi-platform, native C++ engine for developing all kinds of remote desktop software
x86, x64, ARM, Apple Silicon
Windows XP SP3/Vista/7/8/8.1/10/11 and their server versions
From macOS 10.13 (not tested on macOS 27 yet)
Linux and Windows ARM32/64 are planned
~300,000 lines, ~1,400 source files of custom code
Display and Control
 Per-window control: when you don't need the entire remote desktop
 Run any number of windows from one or more remote machines as if they were running directly on your local desktop
Resize windows locally
Use the remote macOS menu bar, displayed right above the local window
Pop-up windows extending beyond the main window are also rendered and properly clipped
Keyboard handling:
 Unicode: Type using your local keyboard layout, even if it is not installed on the remote machine
Physical: Use the remote layout if it fits better, or if the remote application does not handle Unicode characters properly
Switch between local and remote input languages locally
Clipboard management:
 Beyond plain text, supports multiple formats (rich text, HTML, images, vector graphics, audio) as permitted between the respective operating systems
Synchronizes large clipboard contents, even many megabytes in size
Copy and paste multiple gigabytes of files - including subdirectories - directly between file managers across different operating systems (between local and remote, or even between multiple remote machines)
Monitors bandwidth and the other machine's CPU load during transfers, preventing the system from becoming unresponsive when handling large payloads
Mouse handling: Server-side mouse cursor movement takes priority
Multi-monitor handling
Retina resolution support, with the option to turn it off
Remote screen blanking on supported operating systems (Windows 10/11, macOS)
Accessing Windows Terminal Session desktops:
 no RDP client, firewall configuration, or VPN needed
on Windows 8.1+, logging into a disconnected session (using the FreeRDP library through localhost)
Parallel access to macOS Fast User Switching desktops if multiple users have logged-in desktops on one machine
Screen locking (Windows 8.1+, macOS): switch to a virtual session while the remote machine's physical display returns to the login screen, hiding your activity. On Windows, you can freely toggle back and forth between the physical and virtual views.
Desktop panic button: kicks all remote clients off the machine
System and Network
 Linux servers:
 Minimal C++ code in a single binary for security and performance
Non-blocking I/O socket handling (libevent)
SQL database for the Login/Contact servers
Peer-to-peer:
 IPv4/IPv6
UPnP, NAT-PMP, SIP ALG, H.323 ALG port opening on the router (can be disabled)
UDP (QUIC) and TCP connections
System Tray/Menu Bar menu: for practical, quick access to remote machines/desktops/windows
Join Code sharing: sharing your own machine, desktop, or window with someone else using a 9-digit code
Local network: optionally, you can turn on finding and accessing local machines without servers ( Settings->Network->Find Nexjoin devices on the local network, Settings->Sharing->Visible on local network )
Security, Personal Data, Privacy
 Cryptography:
 OpenSSL 3.5.9 LTS
RSA-2048 TLS 1.3 peer-to-peer connections
RSA-4096 based server certificates
Ed25519 based client certificates
Argon2 password-hash, recovery-code-hash
AES-256-CTR Randomized IV client-side encryption
Server-side zero-knowledge:
 Login servers:
 all personal data (password, name, profile icon, key) is encrypted on the client side, only the account name is unencrypted (minimum GDPR)
they send clients on to the Contact servers with a signed UserId/DeviceId, without personal data
Contact servers:
 only work with UserId/DeviceId, they know nothing about the clients
all personal data that remote desktop clients might need (machine name, OS version, icon, key, Join Code sharing) is encrypted on the client side (AES-256-CTR)
Relay servers:
 don't even know the UserId/DeviceId of the clients
hand out ticket pairs at the request of Contact servers to pair up incoming clients at the start of a remote connection
Replaceable Login servers: independent from Contact/Relay servers, later they can even be connected to local company systems (e.g. Active Directory, LDAP)
Certificate verification: on both client and server sides, issuing temporary certificates when redirecting clients between servers. Completely closed system.
End-to-end encryption:
 TLS connection with the Relay server until client ticket check
after pairing the clients, the Relay switches back to a plain socket, and the clients create a new TLS connection between each other over the forwarded connection, mutually checking each other's peer-to-peer certificate
the Relay server cannot inspect the data stream either, it just forwards it
in parallel with the live Relay server connection, clients also try to create a direct connection between each other, and switch to it if successful (this can be turned off)
IPC encryption: communication between processes is also encrypted with TLS 1.3
Transparency: data communication can be checked by turning on debug logging
Saved remote passwords: double encryption, encrypted by both the remote machine and the client side with their own keys, cannot be decrypted on either side without the other
Two-factor authentication: using Google Authenticator or other TOTP programs
Forgotten Nexjoin password: Recovery Codes to get your account back
Current State
 This is closed-source code developed the classic way over many years, in early beta state, from a single developer. It is not completely finished, but what is done is already works well in practice right now. Minor inaccuracies can of course still happen. What is still planned:
 Audio
Localization to as many languages as possible
Using TPM/Secure Enclave
Two-factor authentication when accessing remote machines too
Wake-on-Lan
Convenient switching between multiple monitors
Drawing on the remote screen (whiteboard)
Proper Windows HDR color conversion
Opening a new Windows Terminal Session
DirectX 9 Screen Capture (Windows Vista & Windows 7 DWM)
Hardware video encoding/decoding
Handling proxies
Remote Update
Mobile/tablet clients
Deployable servers for your own network
Optional PTSD mode: unexpected cancellation of the Free license, occasional nagging with popup windows, unexpected connection drops, filling out repentant confessions (for temporary management of withdrawal symptoms)
And whatever else comes... :) Even your ideas.
Source Code Audit
 So far I have done everything I can for security and privacy, but auditing the code with an outside expert is also planned.
 Code Signing
 The code is signed with my own name on both Windows and macOS (András Szigethy, https://www.linkedin.com/in/szigand/ ). On Windows, my Sectigo Individual Code Sign Certificate is still quite new, so Windows Defender SmartScreen might complain for a while on first start. You can step past that, and in theory it will calm down over time once enough people have done it.
 On Windows Server 2003, update KB3072630 is required for signature verification; without it, the program will not start.
 Support
 If you like the idea, want this software to be completed and kept running, and would use and rely on it in production in the not-too-distant future, please support it on Patreon , or if you prefer not to register just for this - or are contributing as a company and need a B2B invoice - you can also do so on Polar . I cannot continue without support, and I do not want to get deeply involved in the business world. I also welcome sponsors, including for server infrastructure. This is an experiment to see whether this project can be viable and grow organically in this form, while preserving its independence and common sense.
 Open Source
 The code relies on several very good, freely usable open-source libraries (Poco C++, wxWidgets, SDL, etc.). My firm goal is that if the project gets on a stable footing, I will regularly send 10% of the incoming money to them, since without their persistent work this couldn't have been created either, and couldn't really exist in the future, so I think they deserve this.
 Usage
 The program can also be used in STANDALONE MODE as a client, without installation, to access remote or local machines.
Sharing the screen requires installation because of the necessary system components needed to make remote access to desktops actually usable.
If you want to access your own remote machines, you can register a Nexjoin account and assign your machines to it one by one after installation.
You can assign icons to your machines ( .svg, .icns, .png, .gif, .jpg, .jpeg, .bmp, .tif, .tiff ), which are stored on the server after client-side encryption. You can even use a logo, emblem, or product photo copied straight from a website. ( macOS Windows XP/7 Windows Vista Windows 8/8.1/10 Windows 11 )
If you only want to occasionally share something from your machine with a Join Code, you don't need a Nexjoin account for that, but installation is required.
You can also share your machines one by one with other users so they can access them anytime. They can log into the desktops of these machines either with the password of the given desktop user, or by knocking if the user sitting at the machine lets them in. You can revoke the sharing anytime.
You can share a complete desktop, a whole screen, or even a currently open window with a Join Code, even remotely.
Join Code sharing requires the machines to be connected online to the Nexjoin server.
Changing machine names and icons requires the machines to be assigned to an account.
Current Servers
 Login/Contact servers (because of GDPR, currently):
 Budapest (HU)
Frankfurt (DE)
Amsterdam (NL)
Relay servers:
 Budapest (HU)
Frankfurt (DE)
Beauharnois (CA)
Hillsboro (US)
Singapore (SG)
Sydney (AU)
The servers use the downloaded DBIP IP to City Lite database so they can direct clients to the closest servers if needed.
 For now, there are only these few servers so the system can be tried out at all; live production use will obviously require more later.
 Uninstallation
 Windows: from the Control Panel, just like other programs.
macOS: drag the icon to the Trash, the Launch Daemon notices this and deletes itself along with the Launch Agent.
Contact
 You can find the project blog at https://blog.nexjoin.io/ , where I post news and updates. You can also subscribe to the email newsletter there.
My LinkedIn profile: https://www.linkedin.com/in/szigand/
Project email addresses:
 András Szigethy
admin@nexjoin.io
support@nexjoin.io
bugs@nexjoin.io
security@nexjoin.io
privacy@nexjoin.io
Download
 macOS 10.13+
 Intel/Apple Silicon: https://nexjoin.io/download/NexjoinMac_0.84.375.zip
Windows XP SP3 - 11
 32-bit (x86): https://nexjoin.io/download/NexjoinWin32_0.84.375.exe.zip
64-bit (x64): https://nexjoin.io/download/NexjoinWin64_0.84.375.exe.zip
Screenshots
❮
 ❯

## 评论（1/1）

> **szigand** · 2026-11-08T18:57:34.000Z　
> Many years ago, as a former LogMeIn developer, starting my own remote desktop system from scratch seemed like an interesting idea and a good challenge, especially since there were more and more complaints about the existing ones. I saw no point in developing yet another identical system, but rethinking what I could, putting in new ideas, and polishing every detail with proper implementation - while respecting future users' time, nerves, and private data - seemed like a good task. It should just do its job simply, cleanly, and unnoticed as it should: removing distance, making remote work easier and a better experience, and simplifying connections while taking care of security. For now, this is what came out of it. This is just a first incarnation of the engine; many kinds of products can be born from this.

## 关联链接

- https://blog.nexjoin.io/
- https://nexjoin.io/download/NexjoinMac_0.84.375.zip
- https://nexjoin.io/download/NexjoinWin32_0.84.375.exe.zip
- https://nexjoin.io/download/NexjoinWin64_0.84.375.exe.zip
- https://www.linkedin.com/in/szigand/

## 导航

- 项目页：[[10-项目/nexjoin.io_0f303c6e]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`开发者工具`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
