---
type: "corpus"
item_id: "da9eca531b10032a"
title: "Show HN: VAX/VMS 5.5 now runs in browser"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49124202"
project_url: "https://vax.3dl.network/machines/dec/vax/ka655"
author: "baron3dl"
published_at: "2026-07-31T15:16:22Z"
captured_at: "2026-09-21T03:11:05+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-21"
pub_day: "2026-07-31"
tags:
  - 语料
  - hn_show
  - author_baron3dl
  - story_49124202
  - show_hn
metrics: {"points": 3, "comments": 4, "engagement_velocity": 3}
comments_count: 4
comments_total: 4
discovered_via: "hn:show_hn:83d"
---

# Show HN: VAX/VMS 5.5 now runs in browser

> [!info] 一句话导读
> Home of the original IBM PC emulator for browsers.

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49124202>
> 指标：点赞=3 · 评论=4 · engagement_velocity=3
> 作者：baron3dl　|　发布：2026-07-31T15:16:22Z
> 项目链接：<https://vax.3dl.network/machines/dec/vax/ka655>
> 采集：2026-09-21T03:11:05+08:00　|　id：`da9eca531b10032a`

## 正文

PCjs Machines
Home of the original IBM PC emulator for browsers.
About
Blog
Explorer
Repository
Tools
DEC MicroVAX 3900 (KA655) with OpenVMS VAX
Log in with SYSTEM / QUOKKA1953
The machine boots itself: the KA655’s self-tests first, then OpenVMS, about a minute to the
 Username: prompt. Click the terminal before typing.
The machine below is a DEC MicroVAX 3900 , the Q22-bus VAX built around the KA655 CPU module:
a CVAX 78034 at 3.125 MHz with the CFPA floating-point accelerator, the CMCTL memory controller, the
CQBIC Qbus interface, and the KA655 console/diagnostic ROM at physical 0x20040000 .
Attached devices:
RQDX3 MSCP Disk Controller , with an OpenVMS VAX V5.5 system disk
auto-mounted on DUA0:
The console serial line on OPA0: , as a glass TTY — DCL and the boot stream render correctly, but
screen programs (EDT, EVE, NOTES) do not paint
The disk image is fetched read-only; writes go to an in-memory copy-on-write overlay that vanishes
when you close the tab. Set autoBoot="false" on the  element of
 machine.xml if you would rather stop at the KA655’s >>> prompt and boot by hand.
[PCjs Machine "vax3900"]
Waiting for machine "vax3900" to load....
The port, the media it loads, and how to run it locally are described on the
 DEC VAX page.
Source
The VAX emulator is JavaScript, and all of it is readable:
machines/dec/vax/ — the port
modules/v2/ — the
machine itself: cpu.js
and decode.js
for instruction execution, mmu.js
for memory management, cqbic.js
for the Qbus, rqdx3.js
and rq.js for
the MSCP disk controller that DUA0: is attached to
tests/ — how it is
graded. Most of these are differentials : they run the same instruction stream through this
emulator and through Open SIMH and compare state register by register, rather than asserting
against numbers somebody typed in.
browser/ — the Web
Worker the machine runs in, and the disk provider that fetches the volume over HTTP
It is ported site-for-site from Open SIMH ’s VAX/ sources
(MIT, © 1998–2019 Robert M Supnik), so a function here generally has a C original with the same
name, and the comments say which one.
[ GitHub Source ]
PCjs Explorer
Expand All
Collapse All
Surprise Me
Hardware
 All PCs
AT&T
AT&T 6300
Color Graphics
Documentation
CDP
CDP MPC 1600
Color Graphics
Documentation
COMPAQ
Portable
Monochrome Graphics
Documentation
DeskPro 286
Documentation
DeskPro 386
Color Graphics
Enhanced Graphics
VGA Display
Documentation
LTE/286
Documentation
IBM
PC (Model 5150)
Color Graphics
Monochrome Display
Dual Displays
VGA Display
Documentation
PC XT (Model 5160)
Color Graphics
Enhanced Graphics
Monochrome Display
VGA Display
Documentation
PC AT (Model 5170)
Color Graphics
Enhanced Graphics
Monochrome Display
VGA Display with CD-ROM
Documentation
PCJr (Model 4860)
Documentation
PC Hard Drives
Documentation
PC Video Adapters
Documentation
Zenith
Zenith Z-150
Color Graphics
Documentation
Arcade
Space Invaders
DEC
PDP-10
KA10
PDP-10 KA10 Test
Documentation
KL10
Documentation
Documentation
PDP-11
PDP-11/20
PDP-11/20 with BASIC
PDP-11/20 with Bootstrap Loader
PDP-11/20 with Boot Monitor
PDP-11/20 with Front Panel
PDP-11/45
PDP-11/45 with 256Kb
PDP-11/45 with VT100
PDP-11/70
PDP-11/70 with 4Mb
PDP-11/70 "Server Array"
PDP-11/70 with Boot Monitor
PDP-11/70 with Front Panel
PDP-11/70 with CPU Exerciser
PDP-11/70 with RSTS/E
PDP-11/70 with RT-11
PDP-11/70 with XXDP+
PDP-11/70 with VT100
Documentation
Documentation
ROMs
DEC PDP-11 ROMs
DEC VT100 ROMs
Other DEC ROMs
VAX
MicroVAX 3900 (KA655) with OpenVMS VAX
VT100
VT100 Terminal
Dual VT100 Terminals
VT100 connected to IBM PC AT
Intel
8080 Exerciser
LEDs
Game of Life
Lite-Brite
Text Scroller
OSI
Challenger 1P
Challenger 1P "Array"
Challenger 1P with Debugger
TI
TI-42 Calculator
TI-42
TI-42 with Diagnostics
TI-55 Calculator
TI-55
TI-55 with Diagnostics
TI-57 Calculator
TI-57
TI-57 with Diagnostics
TI-57 with Revised ROM
Software
DEC
PDP-10
Diagnostics
KA10
DAKAA
DAKAB
DAKAC
DAKAD
DAKAE
DAKAF
DAKAG
DAKAH
DAKAI
DAKAJ
DAKAK
DAKAL
DAKAM
DAKBA
Languages
MACRO-10
Tests
PDP-10 Mini-Assembler Tests
PDP-10 Opcode Tests
PDP-11
Disks
RK03
RT-11 4.0
Tapes
BASIC
BASIC (Single User)
Diagnostics
D0AA
D0BA
D0CA
D0DA
D0EA
D0FA
D0GA
D0HA
D0IA
D0JA
D0KA
D0LA
D0MA
D0NA
D0NB
D0NC
D0OA
DEQKC
IBM PC
Applications
IBM
BASIC
Programs from PC DOS 1.00
DONKEY.BAS from PC DOS 1.00
Karel the Robot
Karel the Robot 1.00
Multiplan
IBM Multiplan 1.00
Lotus
1-2-3
1-2-3 1A
1-2-3 1A*
Microsoft
Learning MS-DOS
Learning MS-DOS 1.00
Learning MS-DOS 1.01
Microsoft Chart
Microsoft Chart 2.02
Microsoft Excel
Microsoft Excel 2.0
Microsoft Excel 5.0a
Microsoft Multiplan
Microsoft Multiplan 1.06
Microsoft Multiplan 2.00
Microsoft Multiplan 2.01
Microsoft Multiplan 3.00
Microsoft Multiplan 4.00
Microsoft Multiplan 4.01
Microsoft Multiplan 4.20
Microsoft Word
Microsoft Word 1.10
Microsoft Word 1.15
Microsoft Word 2.00
Microsoft Word 3.00
Microsoft Word 3.10
Microsoft Word 5.00
Microsoft Word 5.0A
Word for Windows
Word for Windows 2.0c
Other
dBASE II
dBASE II 2.4
dBASE III
dBASE III 1.0
Mac Series
Mac Series 1.0
SuperCalc
SuperCalc 1.10
SuperCalc2
SuperCalc2 1.00
SuperCalc3
SuperCalc3 1.00
ThinkTank
ThinkTank (1987)
VisiCalc
VisiCalc (1981)
WordStar
Overview
WordStar 3.20
WordStar 3.24
WordStar 3.30
WordStar 4.00
WordStar for PCjr
Demos
IBM
Dealer Demos
IBM PC Dealer Demos
Exploring the IBM PC
Exploring the IBM PC (CGA)
Exploring the IBM PC (MDA)
Exploring the IBM PC AT 1.00
Exploring the IBM PC AT 2.00
IBM EGA Demos and Utilities
Fantasy Land
Devices
Mouse
Microsoft Mouse
MS Mouse 2.00
MS Mouse 2.50
MS Mouse 4.00
MS Mouse 5.00
MS Mouse 5.03
MS Mouse 6.xx
ROM
IBM PC ROMs
IBM PC BIOS Sources
IBM PC XT BIOS Sources
IBM PC AT BIOS Sources
IBM EGA BIOS Sources
Diagnostics
COMPAQ
COMPAQ DeskPro 386 (1986)
COMPAQ User Programs (1987)
COMPAQ User Programs (1989)
COMPAQ SystemPro
COMPAQ Diagnostics 5.02
COMPAQ Diagnostics 5.08
COMPAQ Diagnostics 6.12
IBM Diagnostics
IBM PC
IBM PC Diagnostics 1.00
IBM PC Diagnostics 1.02
IBM PC Diagnostics 1.02 (Adv)
IBM PC Diagnostics 2.02
IBM PC Diagnostics 2.05
IBM PC Diagnostics 2.05 (Adv)
IBM PC Diagnostics 2.07
IBM PC Diagnostics 2.20 (Adv)
IBM PC AT
IBM PC AT Diagnostics 1.01 (Adv)
IBM PC AT Diagnostics 1.02
IBM PC AT Diagnostics 2.00
IBM PC AT Diagnostics 2.07 (Adv)
IBM PS/2 Model P70
IBM PS/2 Model P70 Reference 1.01
Games
IBM
101 Monochrome Mazes (1983)
Id Software
Commander Keen (1991)
Wolfenstein 3D (1993)
Infocom
The Hitchhiker's Guide to the Galaxy
Leather Goddesses of Phobos
Planetfall
Zork I: The Great Underground Empire
Zork II: The Wizard of Frobozz
Zork III: The Dungeon Master
Microsoft
Microsoft Adventure
Flight Simulator (1984)
Other
Adventures in Math (1983)
Balance of Power (1985)
Castle Adventure (1985)
Dune II (1992)
Executive Suite (1982)
Eye of the Beholder (1991)
Hero's Quest I (1989)
Invaders Boot Sector (2019)
King's Quest (1985)
King's Quest (1987)
Lemmings (1991)
Life & Death II (1990)
Moria (1992)
Nine Princes in Amber (1985)
The Oregon Trail (1989)
The Oregon Trail (1990)
The Oregon Trail (1991)
Populous (1989)
Rogue (1985)
Trump Castle (1988)
Wizardry I (1984)
Languages
Borland
Turbo Pascal
Borland Turbo Pascal 2.00B
Borland Turbo Pascal 3.00B
Borland Turbo Pascal 3.01A
Borland Turbo Pascal 3.02A
Borland Turbo Pascal 4.00
Borland Turbo Pascal 5.00
Borland Turbo Pascal 5.50
Borland Turbo Pascal 6.00
Digital Research
Pascal/MT+
Pascal/MT+ 3.11
IBM
APL
IBM APL 1.00
LOGO
IBM LOGO 1.00
Assembler
IBM Macro Assembler 1.00
IBM Macro Assembler 2.00
BASIC
Compiler
IBM BASIC Compiler 1.00
IBM BASIC Compiler 2.00
COBOL
IBM COBOL Compiler 1.00
FORTRAN
IBM FORTRAN Compiler 1.00
Pascal
IBM Pascal Compiler 1.00
Logitech
Modula-2/86
Modula-2/86 1.00
Modula-2/86 1.10
Microsoft
Assembler
Macro Assembler 1.00-1981
Macro Assembler 1.00
Macro Assembler 1.06
Macro Assembler 1.10
Macro Assembler 1.12
Macro Assembler 1.25
Macro Assembler 2.04
Macro Assembler 3.00
Macro Assembler 3.01
Macro Assembler 4.00
Macro Assembler 5.00
Macro Assembler 5.10
Macro Assembler 5.10 (Feb 1988)
Macro Assembler 6.00
Macro Assembler 6.11
BASIC
Compiler
Microsoft BASIC Compiler 5.36
QBasic
QBasic 1.10
QuickBASIC
QuickBASIC 1.00
QuickBASIC 2.00
QuickBASIC 2.01
QuickBASIC 3.00
QuickBASIC 4.00
QuickBASIC 4.50
Visual Basic
Visual Basic 1.00
C
Microsoft C Compiler 1.03
Microsoft C Compiler 1.04
Microsoft C Compiler 2.03
Microsoft C Compiler 3.00
Microsoft C Compiler 4.00
Microsoft C Compiler 5.00
Microsoft C Compiler 5.10
Microsoft C Compiler for OS/2 5.10
Microsoft C Compiler 6.00a
Microsoft C Compiler 7.00
Microsoft QuickC for Windows 1.00
COBOL
Microsoft COBOL Compiler 1.12
FORTRAN
Compiler
Microsoft FORTRAN Compiler 5.00
PowerStation
Microsoft FORTRAN PowerStation 1.00
Pascal
Compiler
Microsoft Pascal Compiler 3.20
Microsoft Pascal Compiler 3.30
Microsoft Pascal Compiler 3.31
Microsoft Pascal Compiler 4.00
QuickPascal
QuickPascal 1.00
Other
RatBas
RatBas (1982)
SDKs
OS/2 SDKs
Microsoft
MS OS/2 SDK 1.02
Windows SDKs
Windows SDK 1.01
Windows SDK 1.03
Windows SDK 1.04
Windows SDK 3.00
Windows SDK 3.10
Shareware
Books
DOS Internals (1994)
Graphics for the IBM PC
Inside the IBM PC
Unauthorized Windows 95
Undocumented DOS
The Undocumented PC
Undocumented Windows
Magazines
Big Blue Disk
PC Disk Magazine
PC Magazine Diskettes
PC Tech Journal Diskettes
Miscellaneous
PC-SIG Diskette Library
BBS Collections
PC User Groups
Small Computer Book Club
Unprotect Collection
Systems
CP/M-86
CP/M-86 1.00
CP/M-86 1.1B
DOS
COMPAQ
COMPAQ MS-DOS 1.10
COMPAQ MS-DOS 1.11
COMPAQ MS-DOS 1.12
COMPAQ MS-DOS 2.11
COMPAQ MS-DOS 2.12
COMPAQ MS-DOS 3.00
COMPAQ MS-DOS 3.10
COMPAQ MS-DOS 3.20
COMPAQ MS-DOS 3.31
COMPAQ MS-DOS 4.01
COMPAQ MS-DOS 5.00
Digital Research
DR DOS 3.31
DR DOS 3.32
DR DOS 3.33
DR DOS 3.34
DR DOS 3.40
DR DOS 3.41
DR DOS 5.00
DR DOS 6.00
IBM
PC DOS 0.90
PC DOS 1.00
PC DOS 1.10
PC DOS 2.00
PC DOS 2.10
PC DOS 3.00
PC DOS 3.10
PC DOS 3.20
PC DOS 3.30
PC DOS 4.00
PC DOS 4.01
PC DOS 5.00
PC DOS 5.02
PC DOS 6.10
PC DOS 6.30
PC DOS 7.00
Microsoft
MS-DOS 2.00
MS-DOS 3.20
MS-DOS 3.21
MS-DOS 3.30
MS-DOS 3.31
MS-DOS 4.00
MS-DOS 4.01
MS-DOS 4.0M
MS-DOS 5.00
MS-DOS 6.00
MS-DOS 6.20
MS-DOS 6.22
DOS Extensions
IBM
TopView
TopView 1.00
TopView 1.01
TopView 1.10
Microsoft
MS-DOS Manager
MS-DOS Manager 1.00
Quarterdeck
DESQview
DESQview 1.02
QEMM-386
QEMM-386 4.10
QEMM-386 4.23
QEMM-386 5.13
QEMM-386 6.02
SoftLogic
Software Carousel
Software Carousel 2.0.3
Software Carousel 3.0.1
DoubleDOS
DoubleDOS 2.1
DoubleDOS 2.1F
DoubleDOS 2.1V
Disk Optimizer
Disk Optimizer 2.0.3
Other
Omniview 386
Omniview 386 4.30
HomeBase
HomeBase 1.04A
OS/2
IBM OS/2
IBM OS/2 1.0
IBM OS/2 1.1
IBM OS/2 1.2
IBM OS/2 1.3
MS OS/2
MS OS/2 1.0
OS/2 Prototype Disks
OS/2 CP-DOS (v7.68)
OS/2 SIZZLE (v7.68.18)
OS/2 FOOTBALL (v7.68.17)
OS/2 FOOTBALL (v4.41.00)
OS/2 1.0 Debugger (1988)
UCSD p-System
UCSD p-System with Fortran
UCSD p-System IV with Fortran
UCSD p-System with Pascal
UCSD p-System IV with Pascal
UNIX
IBM
PC/IX
PC/IX 1.0
XENIX
XENIX 1.0
XENIX 2.0
Microport
AT&T UNIX System V-AT
AT&T UNIX System V-AT 2.3
MINIX
MINIX 1.1
QNX
QNX 1.1
QNX 1.2
SCO
Xenix 8086
Xenix 8086 2.1.3
Xenix 286
Xenix 286 2.1.3
Xenix 286 2.2.1e
Xenix 286 2.2.3b
Xenix 286 2.3.2d
Xenix 386
Xenix 386 2.2.3b
Xenix 386 2.3.2f
Xenix 386 2.3.4h
Windows
Microsoft Windows 1.00
Microsoft Windows 1.01
Microsoft Windows 1.02
Microsoft Windows 1.03
Microsoft Windows 1.03a
Microsoft Windows 1.03b
Microsoft Windows 1.04
Microsoft Windows 2.03
Microsoft Windows/386 2.0x
Microsoft Windows/386 2.10
Microsoft Windows 2.11
Microsoft Windows 3.00
Microsoft Windows 3.10
Windows for Workgroups 3.11
Windows 95 (Build 121)
Windows 95 (Build 499)
Windows 95 (RTM) 4.00.950
Tests
PCx86 CPU Tests
PCx86 TestMonitor
VGA "Black Book" Tests
Utilities
Borland
Sidekick
Sidekick 1.11C
Sidekick 1.56
SideKick Plus
SideKick Plus 1.00A
IBM
IBM Professional Debug
IBM Professional Debug 1.00
Microsoft
Unfiled
MS Unfiled Utilities
Norton Utilities
Norton Utilities 2.00
Norton Utilities 2.01
Norton Utilities 3.00
Norton Utilities 3.10
Norton Utilities 4.00
Norton Utilities 4.00 (Adv)
Norton Utilities 4.50 (Adv)
Norton Utilities 5.00
Norton Utilities 6.01
Other
Enhanced DEBUG
Enhanced DEBUG 1.32b
FlickerFree
FlickerFree 1.0
OBJASM
OBJASM 2.0
PathMinder
PathMinder 2.11
PC Tools
PC Tools 1.03
PC Tools 4.30
PFM (Paul's File Manager)
PFM 3.14
Spacemaker
Spacemaker 1.06
SPY
SPY 0.1
UNP
UNP 4.11
OSI C1P
6502 Programs
PCjs
6502 Assembler (8K)
BASIC Extensions
LIFE
Processor Tests
BCD Tests
Overflow Tests
BASIC Programs
OSI
BASIC MATH
CHECKING
COUNTER
POKER
PRESIDENTS
STAR WARS
TRIG TUTOR
Other
SEAWOLFE
SPACEWAR
STAR TREK
TANK FOR TWO
PCjs
CHECKERS
HANGWOMAN
LIFE
OTHELLO
SOFORECAST
TUBELIST
PCjs
Tools
Software Archive
Documents
Books
Programming
Microsoft Programmer's Library
Datasheets
Intel
Motorola
National Semiconductor
Magazines
BYTE
DosGetNews()
Microsoft Languages
Microsoft Systems Journal
PC Disk Magazine
PC Tech Journal
Manuals
DEC
IBM
Intel
Microsoft
Motorola
Papers
Research
Electronic Computer Project
Tom Estelita
Photos
Lite-Brite
PCjs Archives
Library
Document Archive
Programming Notes
Specifications
DOS Protected Mode Interface
pcjs.org © 2012-2026 Jeff Parsons
PCjs is released under an MIT License

## 评论（4/4）

> **baron3dl** · 2026-07-31T15:16:22.000Z　
> When PCjs hit the front page a couple weeks back I noticed VAX was conspicuously missing and couldn't resist seeing VMS run in a web browser. Claude Code running Opus 5 meticulously ported the KA655 from SIMH to PCjs.It boots up to OpenVMS 7.3. I demo with 5.5 because its 1/10 the size and hits the nostalgia even harder.

---

> **mikewarot** · 2026-08-01T19:33:48.000Z　
> That's way cool, but it won't take an enter from my phone as a carriage return. I'll try it from home later.

---

> **alexkowalenko** · 2026-08-01T08:46:03.000Z　
> I wanted to look at the source code, it's not checked into the repo.

---

> **baron3dl** · 2026-08-01T19:05:07.000Z　
> Upstream hasn't replied to the issue I opened about how they want to take the fork back in. There are 3 open PRs. Seems like maybe he's not paying attention to it. Anyway, the code is all here in my fork: https://github.com/baron-3dl/pcjs/tree/master/machines/dec/v...

## 导航

- 项目页：[[10-项目/vax.3dl.network_4ff34a84]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
