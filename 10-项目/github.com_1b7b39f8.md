---
type: "project"
title: "Show HN: Live, system-wide USB transfer sniffer in eBPF"
project_url: "https://github.com/yeet-src/usbsnoop"
first_seen: "2026-09-21T02:52:49+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_r3tr0
  - story_48342821
  - show_hn
lang: "en"
---

# Show HN: Live, system-wide USB transfer sniffer in eBPF

> [!info] 一句话导读
> Live, system-wide USB transfer sniffer in eBPF — decodes USB traffic inline (control SETUP, SCSI, HID) from two universal URB hooks. No usbmon, no hardware snif…

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://github.com/yeet-src/usbsnoop>
> 首次收录：2026-09-21T02:52:49+08:00
> 来源渠道：HN Show HN
> 标签：author_r3tr0, story_48342821, show_hn
> 最新指标：点赞=9 · 评论=0 · engagement_velocity=9

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-09-21T01:27:24+08:00 | HN Show HN | 点赞=9 · 评论=0 · engagement_velocity=9 | [[20-语料/posts/hn_show/2026-09-21/e869b08dbfa37cbe_Show-HN-Live,-system-wide-USB-transfer-sniffer-in]] |
| 2026-09-21T02:52:49+08:00 | HN Show HN | 点赞=9 · 评论=0 · engagement_velocity=9 | [[20-语料/posts/hn_show/2026-09-21/e869b08dbfa37cbe_Show-HN-Live,-system-wide-USB-transfer-sniffer-in]] |

## 摘要正文

# yeet-src/usbsnoop  Live, system-wide USB transfer sniffer in eBPF — decodes USB traffic inline (control SETUP, SCSI, HID) from two universal URB hooks. No usbmon, no hardware sniffer. CO-RE portable.  - Stars: 85 - Forks: 4 - Watchers: 85 - Open issues: 0 - Homepage: https://yeet.cx - Default branch: master - Created: 2026-05-30T00:53:55Z  ## Languages  - C - JavaScript - Makefile  ## Topics  - bpf - co-re - ebpf - libbpf - linux - observability - reverse-engineering - showcase - tracing - usb - usb-sniffer - yeet  ## Top Contributors  - julian-goldstein (4 contributions)  ---  ## README  # usbsnoop — live USB transfer sniffer from two fentry hooks  usbsnoop demo  A real-time, colorized feed of USB traffic **system-wide** — built on the two universal URB chokepoints every host-controller driver funnels through, so it works on xHCI/EHCI/OHCI/dwc alike with no per-controller tracepoints and no `usbmon`. Fully CO-RE portable.  | fentry hook | what it tells us | | ------------------------ | ------------------------------------------------------- | | `usb_submit_urb` | a transfer was queued (device, endpoint, type, payload) | | `usb_hcd_giveback_urb` | it completed (status, bytes move…
