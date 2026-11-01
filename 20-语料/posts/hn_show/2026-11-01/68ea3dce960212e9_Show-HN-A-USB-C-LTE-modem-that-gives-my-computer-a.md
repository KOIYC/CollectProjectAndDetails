---
type: "corpus"
item_id: "68ea3dce960212e9"
title: "Show HN: A USB-C LTE modem that gives my computer a phone line"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50317331"
project_url: "https://github.com/Koppar-AI/koppar-lte-modem"
author: "abijahkaj"
published_at: "2026-10-31T15:56:41Z"
captured_at: "2026-11-01T09:38:09+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-11-01"
pub_day: "2026-10-31"
tags:
  - 语料
  - hn_show
  - author_abijahkaj
  - story_50317331
  - show_hn
metrics: {"points": 44, "comments": 32, "engagement_velocity": 44}
comments_count: 32
comments_total: 32
discovered_via: "hn:show_hn:3d"
---

# Show HN: A USB-C LTE modem that gives my computer a phone line

> [!info] 一句话导读
> GitHub - Koppar-AI/koppar-lte-modem: A phone line over USB-C: LTE data, SMS and voice calls with the call audio on USB. A 4-layer KiCad board designed by Koppar…

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50317331>
> 指标：点赞=44 · 评论=32 · engagement_velocity=44
> 作者：abijahkaj　|　发布：2026-10-31T15:56:41Z
> 项目链接：<https://github.com/Koppar-AI/koppar-lte-modem>
> 采集：2026-11-01T09:38:09+08:00　|　id：`68ea3dce960212e9`

## 正文

GitHub - Koppar-AI/koppar-lte-modem: A phone line over USB-C: LTE data, SMS and voice calls with the call audio on USB. A 4-layer KiCad board designed by Koppar from a one-page spec. · GitHub

A phone line over USB-C: LTE data, SMS and voice calls with the call audio on USB. A 4-layer KiCad board designed by Koppar from a one-page spec.

## Folders and files

| Name | Name | Last commit message | Last commit date |
| --- | --- | --- | --- |
| board | board | | |
| firmware | firmware | | |
| images | images | | |
| .gitignore | .gitignore | | |
| LICENSE | LICENSE | | |
| README.md | README.md | | |
| REVIEW.md | REVIEW.md | | |
| spec.txt | spec.txt | | |
| View all files | | | |

# Koppar LTE modem: a phone line over USB-C

A 4-layer board that gives a computer its own phone line: LTE data, SMS and voice calls, with the call audio on USB. Plug in a nano-SIM and one USB-C cable, and the computer can answer a call through your headset, hand it to a script or an AI agent, or send a text.

The board was designed by Koppar from a one-page spec (`spec.txt`), then reviewed part by part against the datasheets.

## What it does

One USB-C cable, and the computer sees three ordinary devices through the on-board USB hub:

| Device | From | For |
| --- | --- | --- |
| Network adapter | Quectel EC25-EUX (U8) | LTE data, with 3G and 2G fallback (European bands) |
| Serial ports | EC25-EUX | AT commands: caller ID (`+CLIP`), texts (`AT+CMGS`), answer (`ATA`) |
| USB sound card | RP2040 (U5) | Call audio: the module's 1.8 V PCM interface, level-shifted, as a USB microphone and speaker |

There is no battery, screen or speaker. Three LEDs show NET (green), RING (amber) and CALL (blue). Power is 5 V from USB-C, a 3.8 V / 3 A buck for the module's 2 A transmit bursts, and 3.3 V for the hub, the RP2040 and its flash.

| Top | Back |
| --- | --- |
| | |

The schematic is also in PDF.

## What is here

| Path | What it is |
| --- | --- |
| `spec.txt` | The spec the board was designed from. |
| `board/` | KiCad 10 project: schematic, board, rules, the module footprint, symbol and 3D model. |
| `board/fab/` | Gerbers and drill files (`gerbers.zip`), IPC-2581, schematic PDF. |
| `board/fab/jlc/` | JLCPCB assembly BOM and placement files, with the part choices checked by hand. |
| `REVIEW.md` | The design review: what passed, what changed and why, ordering notes, what is still open. |
| `firmware/` | The RP2040 sound-card firmware (after bring-up). |

## Build one

Board. Upload `board/fab/gerbers.zip` to JLCPCB: 4 layers, 1.6 mm, stackup JLC04161H-3313 (the antenna feeds are 49 Ω on it). Every via is 0.45 / 0.2 mm and none sits in a pad, so pick Min via hole size 0.2mm/(0.3/0.35mm) and Via covering: Plugged: no via-in-pad, no extra options.

Assembly. Use `board/fab/jlc/BOM-JLCPCB.csv` and `CPL-JLCPCB.csv`. Glance at the placement preview before confirming, especially the LEDs and the SIM socket (the card slot is at the board edge). `REVIEW.md` lists the parts the files correct.

Parts you source yourself. These are not on JLCPCB's assembly line, or are not on the board at all:

| Part | What to get | Where |
| --- | --- | --- |
| U8, the LTE module | Quectel EC25-EUX, ordering code EC25EUXGR-128-SGNS (EC25EUXGA-128-SGNS is end-of-life; same LGA-144 footprint). It must be the EUX: the North American data-only variants have no voice. | Techship, DigiKey, Octopart (stock changes, check the suffix). Deselect U8 at assembly and solder it with hot air or a stencil, or consign it. |
| 2 antennas | LTE, 698 to 2690 MHz, U.FL (I-PEX MHF I), 50 Ω: one on MAIN (J3), one on DIV (J4) | e.g. Taoglas FXUB63 or Taoglas FXUB62.07.0150C |
| SIM | A nano-SIM with a voice plan | Your carrier |
| Cable and port | USB-C on both ends, from a port that offers 3 A at 5 V | The 5.1 kΩ CC resistors make the board a sink; they negotiate nothing, so a USB-A port or a 1.5 A source will brown out in a 2G burst |

## Open it in KiCad

Open `board/koppar-lte-modem.kicad_pro` in KiCad 10. The module's footprint, symbol and 3D model are in the project (`board/footprints`, `board/custom_syms`, `board/models`), wired in by the project's library tables.

KiCad's library has no 3D model for two of the footprints, so the 3D viewer shows them without a body:

| Part | Footprint | 3D model |
| --- | --- | --- |
| J1, USB-C receptacle | `Connector_USB:USB_C_Receptacle_HRO_TYPE-C-31-M-12` | LCSC C165948 (EasyEDA model) |
| J2, nano-SIM socket | `Connector_JAE:JAE_SIM_Card_SF72S006` | LCSC C2977286 (EasyEDA model) |

easyeda2kicad converts either one to a `.wrl` you can attach to the footprint. The renders above use them.

## Bring-up and recovery

There is no BOOTSEL button. A blank RP2040 boots into its USB bootloader anyway, and the back has three labelled pad groups for the rest:

- BOOT + GND: short them while plugging in and the RP2040 comes up as a USB drive for a new `.uf2`, even after a firmware that crashes before USB starts.
- SWD (CLK, DIO, GND): a Pico Debug Probe or any CMSIS-DAP probe.
- USB_BOOT + 1V8: short them while plugging in and the EC25 starts in emergency download mode, for a modem update that went wrong.

The modem does not switch itself on: the RP2040 drives its PWRKEY (GPIO22) and RESET_N (GPIO23). Until the firmware runs, the computer sees only the hub and the RP2040.

## The design review

The first version (rev A) had an antenna feed at 35 Ω that hopped layers, a buck 60 mm from its inductor, and a SIM socket facing the wrong way. All three are fixed here, along with the parts list and the assembly rotations. `REVIEW.md` has every finding with its numbers.

## Status

| Board | Rev B: 0 DRC errors, 0 unconnected, KiCad 10. Being ordered. |
| --- | --- |
| Next | Once the boards are built: bring-up, AT commands, the sound-card firmware, the first call and text. |

VoLTE is optional on the EC25-EUX. Where 2G and 3G are switched off, calls need a module firmware with VoLTE and a carrier that allows it; ask the seller.

## Design your own

This board started as a page of text. Koppar takes a spec like `spec.txt` to a schematic, a routed board, a BOM at live prices and Gerbers. It also takes a KiCad board you already have, or works from your own agent over MCP.

## Licence

CERN Open Hardware Licence Version 2, Permissive (`LICENSE`).

## About

A phone line over USB-C: LTE data, SMS and voice calls with the call audio on USB. A 4-layer KiCad board designed by Koppar from a one-page spec.

# nicorobinreal/molehill

## 评论（32/32）

> **abijahkaj** · 2026-10-31T15:58:12.000Z　
> I wanted a real phone line on my computer: calls and texts on a physical SIM, answered through my headset at my desk, or by a script or an AI agent when I'm away. Cloud numbers get treated as VoIP, and old Android phones give you no clean way to get call audio in and out over USB.So this is a 4-layer USB-C board around a Quectel EC25-EUX. Behind a USB hub, the computer sees an LTE network adapter, the modem's AT serial ports (caller ID, SMS, answer), and an RP2040 acting as a USB sound card. The RP2040 bridges the modem's 1.8 V PCM audio through a level shifter. There's a 3.8 V buck sized for the 2 A GSM bursts, and no battery.I wrote the spec as one page of text, and Koppar, the tool I'm building, generated the schematic and the board. Then I reviewed it against the datasheets. The review found a 35 Ω antenna feed that hopped layers, a buck 60 mm from its inductor, and a SIM socket facing into the board. The parts matching would have bought an 18 µH inductor for a 4.7 µH slot. REVIEW.md in the repo has all of it with the numbers.Status: the boards aren't built yet. The repo is the design as I'm ordering it: KiCad 10 project, Gerbers, JLCPCB BOM and placement files. Bring-up and the sound-card firmware come next.Happy to answer anything about the audio path or the power design, and I'd like to hear what you'd change before the first bring-up.

---

> **mycall** · 2026-10-31T18:25:40.000Z　
> Will LTE continue to work when 6G rolls out in 3 years?

---

> **Vaushite** · 2026-10-31T20:04:29.000Z　
> Obviously AI vibed, which means the project probably has never been built and wouldn't work if you built it.

---

> **mcculley** · 2026-10-31T20:42:06.000Z　
> This is great. Apple needs to figure out how to fit one into a 16" MacBook Pro.

---

> **efren6** · 2026-10-31T21:06:43.000Z　
> Er

---

> **gruez** · 2026-10-31T21:20:09.000Z　
> >Where 2G and 3G are switched off, calls need a module firmware with VoLTE and a carrier that allows it; ask the seller.This is a huge caveat. OP, does your setup even support VoLTE? Otherwise this might become a brick in a few years as your carrier shuts down 2G/3G, as many carriers around the world have already done

---

> **whalesalad** · 2026-10-31T21:56:29.000Z　
> I’d love one of these as a framework module

---

> **j45** · 2026-10-31T20:05:17.000Z　
> I believe there are VOIP phones that are sim card based. Imagine a country that doesn't have land lines but folks want a home phone.

---

> **j45** · 2026-10-31T20:04:22.000Z　
> Probably for a while - lots of IoT uses it, especially with the push away from 3G.

---

> **wolrah** · 2026-10-31T20:22:41.000Z　
> > Will LTE continue to work when 6G rolls out in 3 years?A significant change that came with LTE is the use of OFDM as the base of the air interface, which means that cellular providers no longer need to allocate large segments of spectrum to one protocol or another. Towers that were upgraded from 4G to 5G didn't need to disable 4G or consistently split their spectrum between the two they way they did when upgrading from 2G to 3G or 3G to 4G, they can dynamically allocate subchannels in each mode based on the immediate needs of their users.It seems unlikely that whatever technologies come in the future will regress in this way, so there shouldn't be a need for a hard cutoff at any point and I'd expect LTE devices to keep working for many generations to come.

---

> **abijahkaj** · 2026-10-31T20:15:11.000Z　
> I mentioned in the top comment that Koppar generated the board and that the first batch is about to be ordered, so no detective work needed there.I'm just as skeptical of blind AI hardware output as you are, which is why I audited every net against the datasheets and put all the flaws in REVIEW.md in the repo before ordering:
> - The 0.33 mm RF trace came out to ~35 Ω instead of 50 Ω and hopped layers through vias (I included Pi-matching pads to tune it on the bench).
> - The 3.8 V buck converter was placed too far from its inductor, and the 1.37 mm power trace is narrower than Quectel's 2 mm recommendation (~100 mV drop at 3 A). - The SIM socket (J2) is oriented inward, which is annoying mechanically.5 bare boards + 2 PCBA units are currently being ordered at JLCPCB, and I'll order the EC25-EUX modules separately to hand-solder onto U8 since JLC was out of stock.Since the KiCad files are in the repo, if you spot a specific net or pinout error that will brick bring-up, let me know so I can bodge-wire it next week.

---

> **wlesieutre** · 2026-10-31T21:03:08.000Z　
> They could if they wanted to, I’m a bit surprised that they didn’t add it with this big new MBP generation.Especially now that they have their own modem and wouldn’t need to pay whatever royalties Qualcomm would demand, which I’ve read are based on the device price and would get very high on a premium laptop.

---

> **DaiPlusPlus** · 2026-10-31T22:00:26.000Z　
> They don’t want to: it helps deuce demand for the iPhone via the macOS/iPhone tethering integration, and for calls taken via FaceTime.

---

> **sellmesoap** · 2026-11-01T00:03:19.000Z　
> If they can hack one into a hardware crypto wallet why not a MacBook https://news.ycombinator.com/item?id=50054092

---

> **abijahkaj** · 2026-10-31T21:53:16.000Z　
> Yes, the Quectel EC25-EUX supports VoLTE natively on the modem baseband, and from the board's perspective the audio path is identical: the modem handles the IMS/SIP registration and AMR codec internally and outputs standard 1.8V PCM digital audio to the RP2040 whether the call is over VoLTE or 2G/3G fallback.I put that caveat in the README because VoLTE support in practice depends on carrier whitelisting and having the right carrier MBN profile loaded on the Quectel module (AT+QMBNCFG), not on the rest of the PCB. Here in Europe, 2G/3G is still up for a few more years, and major carriers have MBN profiles in the standard EC25-EUX firmware, so testing both VoLTE registration and CSFB fallback will be part of bring-up when the board lands.

---

> **wolrah** · 2026-10-31T20:27:03.000Z　
> There are SIP to cellular gateways which have historically been very popular in regions where landline to mobile calls cost money but mobile to mobile do not, but they mostly don't exist in the US market other than high-density devices mostly used by SMS spammers.The only actual VoIP phone with a SIM card I'm aware of is the Yealink T74LTE which for a long time was exclusive to Verizon's business phone service but has recently become available for general purchase, those can support both SIM over LTE data and VoLTE (which is also basically SIP but over a prioritized channel).

---

> **retatop** · 2026-10-31T20:53:57.000Z　
> I don't think your conclusion is correct. 4G -> 5G will result in 5G networks completely consuming the 4G ones. T-Mobile has already been talking about shutting down LTE in a few years. The reason afaik that 4G and 5G are seemingly compatible right now is that most networks are in 5G NSA mode (non standalone) which means that LTE is actually used for negotiation and orchestration stuff, with 5G only used for the actual data pipe. I have been told that most of the benefit of 5G comes with 5G SA (standalone), but that requires not supporting the LTE stuff

---

> **gruez** · 2026-10-31T20:54:03.000Z　
> It's not just spectrum, though. The core network is totally different than 5G SA or whatever 6G has. Maintaining all of that will eventually be considered not worth the trouble, and it'll be decommissioned. If anything decommissioning will be faster for LTE because unlike 2G/3G (which were needed because VoLTE support was flakely and had device whitelists) there isn't much point in keeping LTE around for legacy reasons.

---

> **OJFord** · 2026-10-31T21:07:10.000Z　
> > they can dynamically allocate subchannels in each mode based on the immediate needs of their users.Right, so if I'm still rocking 4G only while 'everyone' else in the area is using 6G with some other stragglers on 5G, ...

---

> **ChocolateGod** · 2026-10-31T22:36:23.000Z　
> 6G will likely replace 5G rather than 4G.4G has become the new 2G when it comes to IoT etc.

---

> **drum55** · 2026-10-31T20:29:05.000Z　
> The PCB looks super weird, what is going on here?https://files.catbox.moe/nijoin.pnghttps://files.catbox.moe/suazr4.pngThey sort of look sensible until you look closer and then the whole board is fever dream autorouting.

---

> **drum55** · 2026-10-31T21:14:41.000Z　
> There was a prototype macbook pro on ebay from 20 years ago with a 3G modem in it, the retail MBP from the time even has the space for a SIM card near the battery door. Presumably they decided against it for a good reason.https://www.macrumors.com/2011/08/14/photos-of-a-prototype-m...

---

> **kotaKat** · 2026-10-31T22:41:29.000Z　
> They're not fully confident yet on the mmWave to go in the Macbook.There's a reason they carefully have been bringing their own modem in via "weird" devices. The C1 came in on the 16e, C1X was the Air (phone+iPad), and they're finally confident enough to bring C2 to the mainline iPhones, but it seems like maybe not ready until C3 comes around next fall.

---

> **Scoundreller** · 2026-10-31T21:17:15.000Z　
> I'd like this kind of setup because my VoIP provider charges a couple bucks a month for 9-1-1 while sending 9-1-1 over cellular would be free

---

> **j45** · 2026-10-31T22:20:00.000Z　
> I recall seeing some that were offered in Asia but might not be elsewhere.It looked like an office desk phone but instead of Ethernet, a SIM card goes only. Some came with a cordless handset with it too. seeing

---

> **cowlevel** · 2026-10-31T21:10:53.000Z　
> Ironic given that LTE, literally called Long-Term Evolution, was supposed to make future backwards incompatible changes unnecessary.

---

> **cowlevel** · 2026-10-31T21:12:54.000Z　
> What are the differences between 4G and 5G core networks?

---

> **cowlevel** · 2026-10-31T21:09:29.000Z　
> They're (mostly) the same channels shared by all of them. It's not like an ethernet address (where everyone on the network speaks the same protocol and just ignores packets not for it), it's a radio frequency timeslice that's allocated to you, and you and your nearby tower can speak any radio modulation they want in that timeslice, even ones that other phones or other towers don't support.However new technologies sometimes also bring new spectrum blocks like mmwave 5G.

---

> **cowlevel** · 2026-10-31T21:12:09.000Z　
> they answered with AI and got flagged for being AI. You can turn on showdead in settings to see it but there's nothing of value in their comment really.

---

> **abijahkaj** · 2026-10-31T21:20:56.000Z　
> yeah it's raw output from the router i'm coding without a trace smoothing pass yet, so it draws ugly jagged steps. looks bad to a human layout engineer, no argument there. either way it won't stop it from working, the electrons don't care how ugly the bend is at 2 MHz. just want to see if it boots when the jlcpcb parcel lands.edit: idk why my comments are being [flagged], i've written to hn but the issue is apparently still there

---

> **DaiPlusPlus** · 2026-10-31T22:10:53.000Z　
> > was supposed to make future backwards incompatible changes unnecessaryI struggle to think of any system/scheme/protocol/spec/etc that promised this to have actually delivered. One can never predict the future.

---

> **gruez** · 2026-10-31T21:16:37.000Z　
> https://en.wikipedia.org/wiki/5G#Core_network_architectureBig enough that most carriers can't even launch 5G with its associated core network ("5G standalone"), and had to use the kludge of 5G + 4G core network ("5G non-standalone)

## 导航

- 项目页：[[10-项目/github.com_2e58988f]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
