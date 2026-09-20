---
type: "corpus"
item_id: "a64d7468c1cf422e"
title: "SDCC – Small Device C Compiler"
source: "hn_front"
source_name: "HN 首页（非 Show HN）"
url: "https://news.ycombinator.com/item?id=49762744"
project_url: "https://sdcc.sourceforge.net/"
author: "lioeters"
published_at: "2026-09-19T02:32:36Z"
captured_at: "2026-09-20T03:32:45+08:00"
lang: "en"
kind: "post"
tags:
  - 语料
  - hn_front
  - author_lioeters
  - story_49762744
  - front_page
metrics: {"points": 118, "comments": 28, "engagement_velocity": 118}
comments_count: 28
comments_total: 28
discovered_via: "hn:front_page:2d"
archived: true
archived_at: "2026-09-20T09:16:59+08:00"
archive_reason: "排除:无主题词"
---

# SDCC – Small Device C Compiler

- **来源**：HN 首页（非 Show HN）　|　**kind**：post
- **原帖**：https://news.ycombinator.com/item?id=49762744
- **指标**：点赞=118 · 评论=28 · engagement_velocity=118
- **作者**：lioeters　|　**发布**：2026-09-19T02:32:36Z
- **项目链接**：https://sdcc.sourceforge.net/
- **采集**：2026-09-20T03:32:45+08:00　|　**id**：`a64d7468c1cf422e`

## 正文

SDCC - Small Device C Compiler

# SDCC - Small Device C Compiler

## What is SDCC?

SDCC is a retargettable, optimizing Standard C (ANSI C89, ISO C99, ISO C11, ISO C23) compiler suite that targets the Intel MCS51 based microprocessors (8031, 8032, 8051, 8052, etc.), Maxim (formerly Dallas) DS80C390 variants, Freescale (formerly Motorola) HC08 based (hc08, s08), Zilog Z80 based MCUs (Z80, Z80N, Z180, SM83, Rabbit 2000, 2000A, 3000A, SM83, TLCS-90, eZ80, R800), Padauk (pdk14, pdk15), STMicroelectronics STM8, MOS 6502 and WDC 65C02. Work is in progress on supporting the Rabbit 4000, 5000, 6000, Padauk pdk13 and the f8 and f8l targets; Microchip PIC16 and PIC18 targets are unmaintained. SDCC can be retargeted for other microprocessors.

SDCC suite is a collection of several components derived from different sources with different FOSS licenses. SDCC compiler suite include:

sdcc C compiler, originally written by Sandeep Dutta; (GPL). Some of the features include:

- extensive MCU specific language extensions, allowing effective use of the underlying hardware.
- a host of standard optimizations such as global subexpression elimination, loop optimizations (loop invariant, strength reduction of induction variables and loop reversing), constant folding and propagation, copy propagation, dead code elimination and jump tables for 'switch' statements.
- MCU specific optimizations, including a global register allocator.
- adaptable MCU specific backend that should be well suited for other 8 bit MCUs
- independent rule based peep hole optimizer.
- a full range of data types: char (8 bits, 1 byte), short (16 bits, 2 bytes), int (16 bits, 2 bytes), long (32 bit, 4 bytes), long long (64 bit, 8 bytes), float (4 byte IEEE), _Bool/bool and _BitInt.
- the ability to add inline assembler code anywhere in a function.
- the ability to report on the complexity of a function to help decide what should be re-written in assembler.
- a good selection of automated regression tests.

SDCC was originally written by Sandeep Dutta and released under a GPL license. Since its initial release there have been numerous bug fixes and improvements. As of December 1999, the code was moved to SourceForge where all the "users turned developers" can access the same source tree. SDCC is constantly being updated with all the users' and developers' input.

## News

2025-10-15: SDCC got funding.

SDCC is primarily developed by unpaid volunteer work; though once in a while there was some outside support, in particular by university employees being allowed to work on SDCC a bit during paid time, and SDCC developers receiving hardware samples from microcontroller vendors. However, sometimes the limitations of this are felt. In particular when I've had a few free hours to work on SDCC, started working on a feature or bug, but was not able to finish the work during the time I had, or simply was not able to even fully track down the cause of the bug. And when it took a long time until I could work again on that feature or bug, it took extra time or effort to get into it again. Sometimes I would instead start work on another aspect of SDCC instead. Having funding available for working on SDCC is IMO really helpful in these situations - instead of having to stop work on SDCC to go back to other paid work, I can just keep working on the feature or bug, since this then is paid work. SDCC developers have been applying for funding for SDCC projects, and we are happy to announce that two important such applications succeeded recently.

The NGI0 Commons Fund donates to improve SDCC support for various target hardware, as well as implement machine-independent improvements to make SDCC more competitive vs. non-free compilers. Hardware-specific improvements planned include improving support for Padauk's popular low-cost microcontrollers, improving support for the Rabbit microcontrollers common in older IoT devices, and improving support for Toshiba TLCS microcontrollers. The focus for machine-independent improvements will be in enhancing support for recent ISO C standards, an optimization to reduce memory usage for local variables, and implementing a link-time optimization to optimize out unused functions and objects. The latter is the one feature most-requested by SDCC users in recent years. This project in done jointly by five SDCC developers.

The Sovereign Tech Fund comissioned work on improving SDCC for safety and security of embedded firmware. We will improve support for aspects of modern C standards and dialects relevant to safety and security, get SDCC ready for post-quantum cryptography, work on mitigations for potential side-channel attacks and improve the reliability of SDCC via extended testing also covering less-commonly used command-line parameter combinations. This project is done by one SDCC developer.

We can imagine all this coming together e.g. when writing firmware for an IoT device based on an eZ80 or Rabbit 4000 SoC. The SDCC user writing this firmware will benefit from the improved support for the target architecture, modern C features for efficiency and convenience, general high level optimizations (all part of the NGI0 Commons project), modern C features relevant for safety and security, to help avoid bugs in the user-written code, efficient side-channel-free code generated for modern cryptography algorithms (all part of the STF project). And thanks to improved testing and fixed compiler bugs, the firmware will compile and work very reliably (depending on the details part of the STF or the NGI0 project).

January 28th, 2025: SDCC 4.5.0 released.

A new release of SDCC, the portable optimizing compiler for STM8, MCS-51, DS390, HC08, S08, Z80, Z180, Rabbit, R800, SM83, eZ80 in Z80 mode, Z80N, TLCS-90, MOS 6502, WDC 65C02, Padauk and PIC microprocessors is now available. (http://sdcc.sourceforge.net). Sources, documentation and binaries for GNU/Linux amd64, Windows x86 and amd64, macOS amd64 are available.

SDCC 4.5.0 New Feature List:

- Full atomic_flag support for msc51 and ds390 ports
- Experimental f8 port
- ISO C2y case range expressions
- ISO C2y _Generic selection expression with a type operand
- K&R-style function syntax (preliminarily with the semantics of non-K&R ISO-style functions)
- ISO C23 enums with user-specified underlying type
- struct / union in initializers

## What Platforms are Supported?

GNU/Linux on amd64, GNU/Linux on x86, Microsoft Windows on amd64, and macOS on amd64 are the primary, so called "officially supported" platforms.

SDCC compiles natively on GNU/Linux and macOS using gcc. Windows release and snapshot builds are made by cross compiling to mingw32 on a Linux host.

SDCC is known to also work on at least GNU/Linux on aarch64, GNU/Linux on ppc64, FreeBSD on aarch64.

Windows users can also try Cygwin (https://www.cygwin.com/) or may try the unsupported Microsoft Visual C++ build scripts.

## Downloading SDCC

See the Sourceforge download page for the last released version including source and binary packages for Linux - amd64, Microsoft Windows - x86, Microsoft Windows - amd64 and Mac OS X - ppc and amd64.

Major Linux distributions take care of SDCC installation packages themselves and you will find SDCC in their repositories. Unfortunately SDCC packages included in Linux disributions are often outdated. In this case users are encouraged to compile the latest official SDCC release or a recent snapshot build by themselves or download the pre-compiled binaries from Sourceforge download page.

In addition, SDCC should compile on any modern Unix-like OS; the following are included in automated regression testing, like the release packages:

- Linux - x86
- FreeBSD - aarch64

SDCC is always under active development. Please consider downloading one of the snapshot builds if you have run across a bug, or if the above release is more than two months old.

The latest development source code can be accessed using Subversion. The following will fetch the latest so

Error fetching https://oppslist.com/: CRAWL_LIVECRAWL_TIMEOUT
Error fetching https://liqi.io/creators: CRAWL_NOT_FOUND

## 评论（28/28）

**fiatpandas** · 2026-09-19T03:23:03.000Z：

TIL about Dallas Semiconductor from this page.Love Silicon Prairie lore.

**dmitrygr** · 2026-09-19T03:24:41.000Z：

SDCC has the best OSS 8051 compiler. It is buggy as hell, but it is free. Sometimes that is good enough.

**MobiusHorizons** · 2026-09-19T04:14:42.000Z：

Has worked well enough for me on 8051 and stm8

**blackfawn** · 2026-09-19T04:34:24.000Z：

SDCC has been a nice resource for a variety of MCUs. I wish it had support for some of the 8-bit PIC chips like the PIC10 and PIC12... maybe one day!

**woadwarrior01** · 2026-09-19T09:01:17.000Z：

I have fond memories of using it for PIC16 as a teenager, ~25 years ago. It was a huge step up from writing assembly. My parents bought me a Microchip PICSTART Plus, but refused to pay for a Hitech-C compiler license. :)

**andrewstuart** · 2026-09-19T10:10:39.000Z：

I use SDCC for 8051.I have started to notice that programming with an LLM it seems to make little difference if I get it to write the entire program in assembly language rather than c.

**jrmg** · 2026-09-19T15:02:28.000Z：

I wonder if this is the most active (or last?...) still-under-development project on SourceForge?

**sehugg** · 2026-09-19T16:12:14.000Z：

I initially added the MOS 6502 support by hacking the HC08 backend. It was awful, someone else (Gabriele Gorla) cleaned it up and got it merged to the mainline. There are other options these days for optimized 6502, like llvm-mos or Oscar64.

**hacker_homie** · 2026-09-19T04:11:54.000Z：

I used it for some toy projects never ran into "bugs" as in this is just broken, but it's quirky for sure.

**Jyaif** · 2026-09-19T06:01:17.000Z：

What a coincidence, just yesterday I asked an LLM to generate a C compiler for the 8051 because SDCC's output was not optimized.
Within an 1.5 hour it was correctly compiling my project at 60% of the size of what SDCC generates.
One or 2 quota refreshes later it passed the SDCC test suite and optimized soft floats.https://github.com/jyaif/cc51

**nickcw** · 2026-09-19T08:27:15.000Z：

I used sdcc for an 8051 based commercial project a while back. I seem to remember spending more time reading the assembly to figure out workarounds for the compiler than actually writing C code!Whereas sdcc works brilliantly for z80 lineage processors. I wrote quite a lot of C for Gameboy recently and didn't find a single compiler bug in sdcc which revised my opinion of it upwards greatly.

**rurban** · 2026-09-19T19:04:53.000Z：

stm8 array access is suboptimal.

**pjmlp** · 2026-09-19T05:06:17.000Z：

If it has not to be SDCC, Mikroe compilers have support for them across C, BASIC and Pascal compilers, if I am not mistaken.

**megous** · 2026-09-19T11:13:56.000Z：

Microchip XC compiler has support for those. They recently dropped the licensing requirement, so while it's not FOSS, it's freeware now, without limits.

**khrbtxyz** · 2026-09-19T17:26:46.000Z：

There are probably several other projects. I remember coming across OpenOCD recently https://openocd.org/pages/repos.html

**jdboyd** · 2026-09-19T19:07:44.000Z：

qBittorrent is still on SF and seems to be more popular in terms of downloads over the prior week, and also looks after with a release earlier this month.Skipping past two projects that consist of repackaging existing projects, or a corporate project that I suspect uses SF only for distribution, the next large community project is CrystalDiskInfo, with a release earlier this summer.Apache OpenOffice is still popular, but doesn't look particularly active.Then we have KePass followed by Ventoy.Even when they are active projects, and maybe not even all that old, they feel like they have a vintage feel to them. Part of me wonders if it is using SF that makes it feel that way, but when I look at the home pages for some of these projects that have their home page off SF, they still have that vintage/old school feel.

**dmitrygr** · 2026-09-19T04:34:16.000Z：

when you have large code, bugs will find you. for example two uint16 vars globally declared one after another. adding them together to each other will produce an access to garbage memory after 5-6 additions. dumb code but a simple repro. i ran into its bug when working on eInk price tags a while back.

**megous** · 2026-09-19T11:18:35.000Z：

Slightly larger switch() statement and you'll run into peephole optimizer just eating away at jump target instructions without telling the jumper to adapt the destination address for the case. Of course the result is completely random code execution. Things like that. :)But I wrote non-trivial code with sdcc regardless. My favorite 8051 targets are FX2LP USB boards from aliexpress. :)

**oasisaimlessly** · 2026-09-19T06:18:43.000Z：

I assume you're running that test suite using a 3rd party 8051 emulator to avoid the potential for common-mode errors in both your compiler and emulator resulting in false confidence the compiler's correctness?> two simulators used for testing, sim51 (a plain 8051) and minitel_simNarrator: No, he was not.

**Joel_Mckay** · 2026-09-19T05:24:49.000Z：

The PIC compiler options were never standards compliant up until around when Microchip purchased AVR. There are great chips now that have free gcc support, reasonable power draw, and 32bit float support (ATSAM3X8E current prices are not worth it in many cases.)PIC does still have a few key use-cases, but most people will hit the stack depth limits pretty quickly in C. A pic12 Assembly project is fun, but the limitations cut deep these days.STM32/ESP32/RP2350 or nRF for low power stuff are far less effort these days, and give much better value. =3

**raphman** · 2026-09-19T04:48:40.000Z：

As a student, 20 years ago, I felt like I was going crazy when using SDCC for pic16. Being new to microcontrollers and C, SDCC seemed cursed - even simple 'blink LED' test cases pseudo-randomly worked or didn't. It turned out that the compiler optimized away some 'empty' loops a little bit too aggressively without realizing that these loops were setting output pins. These bugs have long been fixed but still live on in my long-term memory.

**Jyaif** · 2026-09-19T06:50:39.000Z：

"it runs on my device" is my criteria of success here

**dragontamer** · 2026-09-19T14:04:57.000Z：

ESP32 and RP2350 have pretty crap or nearly non-existent analog. I don't think they even come with a comparator, let alone rarer analog parts like a DAC.If you need a DAC, Comparator, ADC, and a couple of logic gates, its hard to beat an AVR DD (4x arbitrary gates called CCL. 1x DAC. Differential SAC ADC. I believe 2x Comparators and multiple "internal DACs" so you don' have to spend your 1x external DAC on internal parts). Also 1.8V to 5.5V support, as well as dual-power supply support (PortC is run off a 2nd power supply, but all the logic is compatible. This means PortC can run at 5V while everything else runs at 1.8V, or vice versa, making the AVR DD also a built-in level shifter)

**technothrasher** · 2026-09-19T05:58:54.000Z：

I still run across this to this day with GCC and Cortex-M code. The optimizer will occasionally decide to blow away loops that are clearly doing something.

**lelanthran** · 2026-09-19T06:12:33.000Z：

> that the compiler optimized away some 'empty' loops a little bit too aggressively without realizing that these loops were setting output pins.Doesn't sounds like a bug in the compiler, sounds more like `volatile` was not used (unless, of course, `volatile` was not being honoured).

**Joel_Mckay** · 2026-09-19T17:35:53.000Z：

In general, most DAC and ADC colocated on/near a digital chip rail has a list of noise issues anyway, as even an external Vref chip may be unable to help repeatably hit the claimed bit resolution with oversampling. At $9.28/pc for a mcu chip that should cost under $2... runs out of excuses pretty quickly.It is not about whether something is "crap", because they are all mostly "crap" at analog in different scenarios. Just some vendors have chosen not to polish their "turd" in Marketing. These days many DAC are part of a Class D amplifier, as battery life took priority over the noise floors. These have also become less "crap" over the years.Best of luck =3

**uecker** · 2026-09-19T06:04:50.000Z：

Please file a bug report, if you haven't done so.

**raphman** · 2026-09-19T18:33:57.000Z：

Might be. There certainly were bugs in my understanding of micro-controllers and compilers at the time...EDIT: but SDCC indeed ignored 'volatile': https://sourceforge.net/p/sdcc/bugs/436/
