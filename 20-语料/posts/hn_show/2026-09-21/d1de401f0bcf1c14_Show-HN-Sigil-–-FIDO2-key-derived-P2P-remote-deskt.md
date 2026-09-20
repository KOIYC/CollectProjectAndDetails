---
type: "corpus"
item_id: "d1de401f0bcf1c14"
title: "Show HN: Sigil – FIDO2 key-derived P2P remote desktop (agentic workflow retro)"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=48731840"
project_url: "https://dami.zip/blog/sigil-agentic-retro"
author: "FelineStateMach"
published_at: "2026-06-30T12:35:36Z"
captured_at: "2026-09-21T02:53:08+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-21"
pub_day: "2026-06-30"
tags:
  - 语料
  - hn_show
  - author_FelineStateMach
  - story_48731840
  - show_hn
metrics: {"points": 2, "comments": 0, "engagement_velocity": 2}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:113d"
---

# Show HN: Sigil – FIDO2 key-derived P2P remote desktop (agentic workflow retro)

> [!info] 一句话导读
> Skip to content maneframe

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=48731840>
> 指标：点赞=2 · 评论=0 · engagement_velocity=2
> 作者：FelineStateMach　|　发布：2026-06-30T12:35:36Z
> 项目链接：<https://dami.zip/blog/sigil-agentic-retro>
> 采集：2026-09-21T02:53:08+08:00　|　id：`d1de401f0bcf1c14`

## 正文

Skip to content maneframe
Home
 Blog
 Projects
 About
⌂ ←
 Path ~/maneframe/blog/sigil-agentic-retro
 Sigil: Agentic Dev Workflow Retrospective
Published Jun 29, 2026 · Updated Jun 30, 2026
 rust
 tauri
 iroh
 fido2
 openspec
 remote-desktop
 Remote Desktop applications have always faced ergonomic issues managing connections. You need an IP address, credentials, a VPN, an open port, or a third party to manage everything in between. The machine you want to access is out there, but reaching it requires setting up and maintaining a separate infrastructure chain.
⚠ Spoiler: Boruto: Two Blue Vortex, Chapter 16
"[...] The idea to use symbols. Each metal object would be a distinct shape... and visualizing that unique symbol... would make it possible to accurately transport to your intended coordinates, even if they were far away." - Boruto TBV Ch. 16, p. 6
There’s a moment in Boruto: Two Blue Vortex , chapter 16, that resonated with me as I thought about this problem. Boruto discovers his version of the Flying Thunder God Technique: every metal object has a unique shape. You mark it. Visualizing that specific symbol lets you transport to it, regardless of distance. The mark is always there; you just need to have put it there.
What if the mark you left on a machine was your FIDO2 security key and the address came from it? Touch the key, get the same identity you registered on the host, and dial by key instead of IP. You marked the machine when you set it up. Tap it again to get back.
The product name is simple. Sigil is magic-themed and succinct. You leave one on your machine, tap your key, and you’re in.
The first name was Keyhome. Same idea, but too much of a wombo ( word + combo ).
Tech Solutions Looking for an Ergonomic Problem #
There were a handful of technologies I’d been watching and wanted to use: Iroh , FIDO2 WebAuthn’s hmac-secret extension, ffmpeg as a managed subprocess, and emerging standards like MOQ (Media over QUIC) and HTTP/3. Each addressed something real. The question was whether a single project could use all without forcing any of them.
Remote desktop turned out to be that project.
Iroh handles NAT traversal and P2P routing over QUIC without an account or static address. FIDO2 hmac-secret derives hardware-bound secrets that work identically across key vendors. ffmpeg covers every GPU encode backend across platforms via a single subprocess API. MOQ and HTTP/3 address the media streaming problem: QUIC’s stream multiplexing and zero-RTT are exactly what low-latency video needs. Iroh already runs on QUIC internally, and MOQ implementations weren’t mature enough to evaluate when the spikes started, so video currently runs over Iroh’s native streams. MOQ stays on the roadmap.
The fit between FIDO2 and Iroh specifically is what locked the architecture.
Iroh is built around one premise: dial keys, not IPs. Your node identity is an Ed25519 keypair. You connect to peers by their public key, not their network address. The relay handles NAT traversal and fallback. “Keys are created and controlled by you. They stay the same as your device moves.”
FIDO2’s hmac-secret extension: register a credential on a security key, provide a salt, and the key returns a deterministic 32-byte HMAC-SHA-256 output. Same key, same PIN, same salt, same 32 bytes every time. The secret never leaves the hardware. Yubico’s CTAP2 deep dive : “the PRF seed key never leaves the secure element. This is the root of trust.”
Iroh’s SecretKey::from_bytes takes exactly 32 bytes.
That fit is the entire architecture.
FIDO2 key
 + PIN + touch
 + salt: SHA-256("keyhome-iroh-identity-v1")
 → 32-byte HMAC-SHA-256
 → Iroh Ed25519 SecretKey
 → deterministic NodeId
 → your machine's address
 Both host and client tap the same key. Same identity, derived independently. They know each other’s addresses before any network call. No pairing ceremony. No account. Nothing to copy.
The Stack #
One constraint drove all tool choices: no vendor lock anywhere.
Tool Role
 Tauri Desktop shell. Rust backend, OS webview frontend, single binary.
 Iroh P2P transport. E2EE, relay-included, address-by-key.
 ctap-hid-fido2 FIDO2 CTAP client. Any key with hmac-secret support.
 ffmpeg Screen capture and encode. Every platform, every GPU backend.
Tauri’s architecture uses the OS’s native webview (WebKit on macOS/Linux, WebView2 on Windows) rather than bundling a browser engine. The Rust backend exposes typed commands; the frontend calls them over message passing. The whole thing ships as a single compiled binary under 10MB. This architecture matters for sigil: the Rust backend gets direct HID access for FIDO2, runs Iroh natively, and manages the ffmpeg subprocess lifecycle, while the frontend handles UI without needing to know any of that.
Tauri, Iroh, ffmpeg, and FIDO2 are all cross-platform and composable. Any piece can be replaced without touching the others.
Down-Air Documentation: Driving Your Proof of Concept Off-Stage #
Before any Tauri code existed, an OpenSpec change defined the problem: “the architecture is plausible but has four hard risks that must be tested before product build-out.” The risks were crate maturity, token mode assumptions, Iroh connectivity, and capture/input complexity. The spikes ran first, and the specs came from what the spikes found.
Each spike was tracked as an OpenSpec change in hermes-openspec , a Hermes Agent plugin adding a Kanban dashboard for browsing change proposals, spike findings, spec diffs, and task state across the repo. Findings were fed back into the dashboard after each run, scoping what came next.
hermes-openspec
The "Validate Tauri + YubiKey + Iroh MVP" Change is open in the hermes-openspec dashboard, Specs tab. Requirements R1 and R2 map directly to the evidence files produced by each spike.
Spike 001: Iroh native ping. Does Iroh compile and connect on the dev machine?
loopback_ping_rtt_reported_ms=4.140
 loopback_wall_time_ms=10.161
 Yes. One blocker: system Rust 1.75.0 was too old; Iroh 1.0 requires 1.91 . Fixed with rustup.
Spike 002: YubiKey HMAC-SHA1. The initial version of the plan used the challenge_response crate against a YubiKey OTP slot. Result: PARTIAL . Only a Google Titan on hand. The Titan is CTAP2-only and has no OTP slot. The research doc ranked CTAP2 third. Hardware changed the order.
Spike 003: FIDO2 CTAP via ctap-hid-fido2. The Titan supports CTAP2. Try that path.
Found 1 FIDO device(s):
 vid=0x18d1 pid=0x9470 "Titan Security Key v2"
 extensions: ["credProtect", "hmac-secret"]
 clientPin: true
 PIN retries: 8
 hmac-secret available. PIN-protected. Touch-protected. Design is no longer YubiKey-specific.
Spike 004: Derive Iroh identity from Titan hmac-secret. Does the HMAC output actually fit Iroh’s SecretKey?
[3/6] OK HMAC-Secret derived (32 bytes): 8da1f05bed0837d2...
 [4/6] OK Derived EndpointId: 5dff09ef28cdc7bfc04220645c1a775fef2a7fed3de54d665915c6f59dad1d9a
 [6/6] OK PING SUCCESSFUL! ping_rtt_reported_ms=6.536
 The question was whether we would need a transformation step, such as HKDF or truncation. We did not. The output of HMAC-SHA-256 is 32 bytes, and Ed25519 seeds are 32 bytes as well. SecretKey::from_bytes takes the output directly, without reshaping. The fit that proved convenient on paper worked well in code.
The output in the log ( 5dff09ef... ) is the actual NodeId , not a test value or placeholder. The ping at step 6 is the real confirmation. It shows a derived key that Iroh accepts as a valid endpoint and can route through. That completes the full chain from key hardware to the P2P network in a single spike.
It is the same FIDO2 key, PIN, and salt. This means we get the same EndpointId every time. That determinism is key. The address comes from the key, not a registration step. The spike ran again later with a YubiKey and produced a different NodeId , as expected given the different key, but maintained the same stability: the same inputs always yield the same output. We have confirmed vendor independence.
Spikes 005 through 007 connected frame streaming, input injection, and Titan-derived identity into the Tauri app. OpenSpec tasks were closed.
Early PoC: Spec-Driven, Agentic #
Out of that spike work, three specs emerged which defined what alignment looked like before any product code got written:
yubikey-identity : The security key is the hardware authority. It gates every session. Pairing material only becomes available after verification succeeds. No software fallback when the key is absent.
iroh-session : Native Iroh endpoint in the Rust backend, not in the browser. Authenticated host dialing from token-derived material. Protocol streams separated: auth, control, frames, diagnostics.
remote-control : Frame stream from host to client. Input forwarding from client to host only during an active session. A local disconnect that the user controls.
These three specs defined the boundary between “we’re building something real” and “we’re still exploring.” The OpenSpec workflow in hermes-openspec kept these live on the Kanban board, with each spike’s findings feeding back into what the next iteration needed to prove.
Cool Kid’s Agentic Workflow: Loops #
The pattern that held through all of it:
OpenSpec change
 define the risk, the success criteria, and the scope
 |
 v
 Numbered spike
 smallest test that answers one question
 |
 v
 evidence file
 commands run, platform, output, blockers
 |
 v
 Review in hermes-openspec dashboard
 Kanban view, change board, spec diffs
 |
 v
 Next change scoped from findings.
 Each spike was small enough to verify by hand. The spec was the handoff between what was found and what got built next. The FIDO2-generic pivot came from spike 002’s partial result. The xcap-to-ffmpeg switch came from measuring after the WebCodecs revert. Both were scope changes driven by evidence rather than planning.
Theo from T3.gg put the more comprehensive version of this well in “It’s time to go bigger” : “If you’re not pushing yourself past what made sense before, you’re not really using these tools to their capacity.” The agent handles exploration. The spec keeps the exploration from becoming a rewrite that goes nowhere.
Agentic development, homelabbing, and container sandboxes have created a new class of machine: environments that are deliberately isolated, that you still need to occasionally reach into. Each one needs remote access at some point. The options today all have a catch.
SSH is terminal-only. VNC works, but it is unencrypted and needs port forwarding. Tailscale and ZeroTier are good but require an account, meaning you are trusting a third party as a permanent fixture in your network topology. RDP is Windows-shaped. Cloudflare Tunnel requires an account and a domain. Every option with a GUI either requires exposing a port or requires account-based coordination through someone else’s infrastructure.
Sigil’s model: no accounts, no port forwarding, no third party in the auth path. The FIDO2 key is the only credential. Iroh relay handles NAT traversal without knowing who you are. The machine is dark to the internet until the key touches it.
Three years ago, building that end-to-end on your own and shipping it as a native cross-platform binary with hardware video encoding would have been a product-sized effort. FIDO2 integration across platforms, a custom P2P protocol, a video pipeline that handles GPU backends per OS, and a UI that ships on Linux, macOS, and Windows. You would need people. Now it is a spike series with numbered evidence files. That is what Theo means. The cost floor changed. The question is whether you update the scope of what you attempt.
1-2 FPS #
Then the video problem.
First frame path: JPEG over the Iroh channel. Worked. Stuck at 1-2fps. Replaced JPEG with H.264 via openh264 . Still 1-2fps. Implemented WebCodecs decode on the client side for hardware-accelerated H.264 in the browser. Hit a wall: WebCodecs is not available in Tauri’s WebView. Reverted.
The natural next move is a different codec or a better decoder. That was the wrong diagnosis. The codec was never the bottleneck.
Measuring the host pipeline revealed the problem was xcap , the Rust screen-capture crate. Its video recording is flagged as WIP in the README. It was producing raw frames slowly regardless of the downstream encoder. Switching codecs rearranged the queue.
The fix was replacing xcap with an ffmpeg subprocess. ffmpeg handles capture and encoding in a single pipeline with GPU acceleration: NVENC on Nvidia, VAAPI on Linux, VideoToolbox on macOS, AMF on AMD, and software fallback otherwise. The reasons to reach for ffmpeg over another Rust capture crate are: it combines capture, encoding, and format conversion in a single tool; its hardware backend coverage is broader than that of any single Rust crate; and it’s available on every platform sigil targets.
After the ffmpeg switch, xcap’s 90ms capture + 80–150ms per-frame encode became ~5ms total with NVENC. Hardware-accelerated, up to 60fps, reliable.
That answered “is it fast?” but not “is the hardware path actually firing?” or “is the client keeping up?” The next push was observability.
Host side. The backend emits a host-encode-stats event per frame: encode_ms , capture_ms , size_bytes , fps . The info panel picks this up in a # performance section with a 60-sample sparkline (rolling window, auto-scaling y-axis) — so you can see encode time history at a glance. A separate # encoder section shows the resolved encoder name ( h264_nvenc , h264_videotoolbox , libx264 , etc.), codec, bitrate, framerate, and GOP. If hardware encoding silently fell back to software, it shows up there.
Config. Every host entry point now routes through a config overlay before starting: codec (H.264 / H.265 / AV1), backend (auto / nvenc / vaapi / qsv / amf / videotoolbox / software), bitrate, framerate, GOP. detect_available_encoders probes the system and populates the available options so you’re only shown what’s actually installed. Daemon auto-host skips it.
Client side. The wire protocol header grew from 13 to 14 bytes (a codec byte added per frame) (0=h264, 1=h265, 2=av1). The client reads the codec from the wire rather than a separate event, which means it works correctly regardless of which frontend is open. The # stream section in the client panel shows codec received, total frames, and dropped frame count split by cause: decoder not ready vs. decode exception. When something breaks, you know which side of the pipe and why.
Shipping an Idea as v0.1 #
The PoC worked. The loop had run enough times to close the spec. What was left was the gap between “this works on my machine” and “this is shippable.”
The biggest structural problem was commands.rs (1645 lines in a single file). Everything the Rust backend did lived there: auth, input forwarding, streaming, state management, network. Agentic development moves fast and doesn’t always clean up after itself. The refactor split it into commands/{auth, input, streaming, network, state}.rs before anything else. That made the real bugs visible.
The frontend had the same problem. index.html was 1557 lines: markup, styles, codec handling, and all UI logic in one file. It split into main.js (UI and Tauri event wiring), codecs.js (WebCodecs decode pipeline and stream stats), and style.css . index.html became what it should have been from the start: markup only.
Some of those bugs only show up under use:
AV1 keyframe detection was wrong; every frame was being treated as a keyframe by checking the first byte instead of walking OBUs for OBU_SEQUENCE_HEADER . Fixed in the module split.
MouseMove events were being forwarded at capture rate, not throttled. Added a ~60fps cap and a bounded sync_channel(64) with try_send on the enigo input channel to prevent backpressure from piling up.
FIDO spawn_blocking calls had no timeout. On a slow key tap or a detached key, the backend would hang. Added a 30s timeout.
Encoder config wasn’t persisted. Every restart needed reconfiguring. Fixed with app data dir persistence and a setup hook restore.
Hardcoded relay URL was swapped out for presets::N0 relay map for geographic routing and fallback.
After that, the rename. Keyhome explained the mechanism. Sigil describes the feeling. Branding covered everything: Cargo.toml, tauri.conf.json, source files, README, AGENTS.md, and the UI.
The current state is v0.1: the core loop is reliable and used daily. It is not well tested beyond one developer’s setup and has not been hardened for multi-user/multi-host scenarios or a production pairing flow. For personal server management, it is complete. For anything broader, it is a solid foundation.
cargo install --git https://args.io/cat/sigil sigil
 Requires Rust 1.85+, ffmpeg, and a FIDO2 key with hmac-secret support. Full setup at github.com/FelineStateMachine/sigil .
Sources
Boruto: Two Blue Vortex, Chapter 16 (Viz)
Iroh 1.0: Dial Keys, not IPs
CTAP2 HMAC Secret Deep Dive (Yubico)
Tauri Architecture
It’s time to go bigger (Theo, T3.gg)
xcap on GitHub
© 2026 maneframe RSS | GitHub

## 关联链接

- https://args.io/cat/sigil

## 导航

- 项目页：[[10-项目/dami.zip_0a8b6490]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
