---
type: "corpus"
item_id: "faa925af8698adbf"
title: "Show HN: hfmodem – open-source PACTOR-3 and VARA compatible waveform generator"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50234509"
project_url: "https://hfmodem.ssj.lol/"
author: "saulstj"
published_at: "2026-10-25T18:26:55Z"
captured_at: "2026-10-26T09:42:36+08:00"
lang: "en"
kind: "post"
topic: "开发者工具"
shard: "2026-10-26"
pub_day: "2026-10-25"
tags:
  - 语料
  - hn_show
  - author_saulstj
  - story_50234509
  - show_hn
metrics: {"points": 2, "comments": 0, "engagement_velocity": 2}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:3d"
---

# Show HN: hfmodem – open-source PACTOR-3 and VARA compatible waveform generator

> [!info] 一句话导读
> Skip to content hfmodem is an experimental prerelease for developers only. Do not rely on it for any purpose, especially emergency communications.

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50234509>
> 指标：点赞=2 · 评论=0 · engagement_velocity=2
> 作者：saulstj　|　发布：2026-10-25T18:26:55Z
> 项目链接：<https://hfmodem.ssj.lol/>
> 采集：2026-10-26T09:42:36+08:00　|　id：`faa925af8698adbf`

## 正文

Skip to content hfmodem is an experimental prerelease for developers only. Do not rely on it for any purpose, especially emergency communications.
 It has nevertheless demonstrated successful Winlink mail transfers using PACTOR-3 and full-speed VARA HF protocols.
hf modem
 Modes Results Winlink mail Monitor & call
W9SSJ / hfmodem
HF data modem
hfmodem supports PACTOR, VARA, ARDOP, Robust Packet, military data waveforms, ALE, selcall and text-mode monitoring, alongside experimental sabir. Its station tools share audio, rig control and host connections.
 Try Winlink
Experimental prerelease · developers only AGPL-3.0-only
01 / PACTOR-1 timing PACTOR-1 · 1.25 s per cycle
A PACTOR-1 exchange with KB5LZK on 40 m: 0.96 s data packets, 0.12 s control signals and a measured 78.6 ms turnaround. Each cycle includes time for switching and propagation.
Modes
 Supported modes
 PACTOR, VARA and ARDOP are alpha. All other modes are experimental. The guides describe implementation and evidence limits.
Mode comparison
 Carrier placement, timing and mode parameters
01 / shrike · alpha PACTOR
 PACTOR-1, PACTOR-2 and PACTOR-3 link entry, waveforms and control signals
 02 / kestrel · alpha VARA
 Connection frames, modulation and bandwidth selection
 03 / besra · alpha ARDOP
 Frame types, error correction and acknowledged transfers
 04 / sabir · experimental sabir
 An experimental mode using OFDM and adaptive coding; its protocol and wire format are subject to change.
 05 / brubru · experimental Robust Packet
 Eight-carrier modulation, coding and interleaving, AX.25 frames and the KISS host boundary.
 06 / bateleur · experimental Military waveforms, ALE and selcall
 Serial and multitone waveforms, training, constellations and interleavers; linking and host-layer boundaries.
 07 / lanner · experimental RTTY, SITOR-B and NAVTEX
 Two-tone geometry, start/stop framing, letters and figures, time diversity and bulletin parsing.
Results
 Observed results
 These are recorded results from this station: gateway mail transfers and remote beacon reception.
01 PACTOR
 shrike · alpha
 Mail sent and received over PACTOR-3
 Winlink mail sent and received through WS8EOC over hfmodem’s PACTOR-3. Four messages also received through KB5LZK over PACTOR-1, with a normal session close.
Evidence
 02 VARA
 kestrel · alpha
 Mail received and delivered
 Mail reception through K0SI at BW2300 and confirmed outbound delivery through KB8AY. Multiple deliveries confirmed by the operator. VARA supports high speed capable and speed limited links.
Evidence
 03 ARDOP
 besra · alpha
 Mail sent and received
 hfmodem received messages through WW2MI and W6IDS. An outbound message through WW2MI reached its destination. Codec checks against ardopcf cover all 59 frame types in both directions.
Evidence
 04 sabir
 experimental
 Beacon decoded at remote receivers
 The hfmodem decoder recovered 40 m beacons from recordings at public receivers 103 and 302 miles away. Two transmitted gears decoded at both receivers.
Evidence
Recorded exchanges
 Successful Winlink mail sends and receives
 A single data-loss incident cost the project significant development work and logbook material. Among the losses were the high-speed VARA receive recording and the original rig receive recordings for these ARDOP sessions. These examples use the recordings and session records that survived.
 VARA · send · 40 m NS0A
 2026-09-27 · 21:21 UTC. 1 sent · destination receipt confirmed. L9 acknowledged transmit.
VARA · receive · 20 m N5TW
 2026-09-23 · 18:10 UTC. 2 received · 1 sent. L4 receive · speed-limited.
PACTOR-3 · send · 40 m VE1YZ
 2026-09-24 · 04:10 UTC. 1 sent · 2 received. SL6 acknowledged transmit.
PACTOR-3 · receive · 80 m WS8EOC
 2026-10-03 · 05:00 UTC. 1 received. SL3 receive.
ARDOP · send · 40 m WW2MI
 2026-08-23 · 03:11 UTC. 1 sent · destination receipt confirmed. 200 Hz session. Subsequent receive failed; END was not confirmed.
ARDOP · receive · 40 m W6IDS
 2026-08-26 · 15:24 UTC. 3 received · normal link close. 500 Hz session. Peer 4PSK.200.100 data.
Curated static logbook → · Recordings and their evidence →
 These are retained recordings at their actual speeds: VARA receive is L4 and PACTOR-3 receive is SL3. ARDOP audio is retained from remote KiwiSDR witnesses; the WW2MI send completed, but its subsequent receive attempt failed.
Winlink mail
 Install hfmodem and exchange email
 Follow the guided setup to send and receive Winlink email through a radio gateway. Use Python 3.13 on macOS or Linux. Connect the FTDX10's USB CAT and audio, or the FT-891's CAT connection and an external audio interface.
Open Terminal and paste this block Copy
 python3.13 -m venv ~/hfmodem-env
. ~/hfmodem-env/bin/activate
python3 -m pip install --pre hfmodem
hfmodem winlink The first run guides radio, callsign, licence and audio setup, saving configuration only. Grid is optional; press Enter to skip it. Choose PACTOR-3 or VARA HF and a band your antenna is ready for, then a gateway channel. Choose to receive mail or send a text message; sending asks for a recipient, subject and message. Review the final Start this mail call? prompt. Receiving mail is the default; the hidden Winlink password is kept for this session only.
 Guided calls set and check Yaesu DATA USB, the data audio route, RTS PTT and saved RF power (initially 20 W). Read the startup summary; the radio settings persist. Set CAT speed to 38400 baud and watch ALC during transmission while adjusting the provisional audio drive.
 In each new Terminal, run . ~/hfmodem-env/bin/activate first. Then use hfmodem winlink pactor or hfmodem winlink vara . Add --refresh for a new gateway list. With setup saved, --dry-run previews without opening radio hardware. Ctrl-C stops the call; read its transfer and teardown results. Read saved messages offline with hfmodem winlink --inbox .
Operator guides
 Install, set up and receive mail ↗ Station operation ↗ Configuration ↗ Documentation index ↗ Live operation uses Hamlib, the flac recording helper and nc ; Linux also needs the PortAudio system library. Setup checks the command-line tools and can offer to install missing tools through Homebrew or apt with your consent.
 Gateway choices are filtered by your configured licence and UTC hours, then ranked by distance when you provide a grid. The FT-891 needs an external audio interface; its USB CAT cable does not carry audio.
 Downloads, system dependencies and RF conditions determine how long installation and a contact take. For a recording-only preview, explore the curated logbook .
Monitor & call
 Monitor signals and make radio contacts
 Once installed, use the operator console for passive decoding, ALE and selcall contacts, and the station logbook. Start with a single passive decoder at the current dial, or tune once to a frequency or saved peer. You can then retune the radio itself while monitoring.
Terminal / passive reception
 hfmodem console pactor monitor
hfmodem console rtty monitor --freq 14080
hfmodem console stanag4285 monitor --mode 1200L
hfmodem console monitor --list-modes Frequencies are USB dial kHz in these examples. Set the radio's sideband and receive filter before starting; a wide 4 kHz voice passband is supported.
Operator guides
 Console setup and logbook ↗ All passive monitors ↗ HFLINK, ALE and selcall ↗ The HFLINK console supports automatic ALE scanning and optional sounding, manual calls, native ALE text and held-channel selcall pages. Preview the channel plan with --dry-run ; execution requires your configured station and transmit authorization.
hf modem © 2026 Saul St John (W9SSJ) · Code: AGPL-3.0-only · Documentation, images and site: CC BY 4.0
 hfmodem@ssj.lol · Accessibility · Source ↗ · Issues ↗ · Security ↗ Keyboard preferences Allow letter-key shortcuts Shortcut sequence Run shortcut

## 导航

- 项目页：[[10-项目/hfmodem.ssj.lol_ae774ef6]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`开发者工具`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
