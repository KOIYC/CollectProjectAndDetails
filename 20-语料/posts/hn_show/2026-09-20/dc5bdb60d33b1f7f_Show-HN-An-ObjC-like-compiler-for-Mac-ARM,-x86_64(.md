---
type: "corpus"
item_id: "dc5bdb60d33b1f7f"
title: "Show HN: An ObjC-like compiler for Mac ARM, x86_64(Linux, Win), WASM, & others"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49730393"
project_url: "https://compile-xc.org/"
author: "spacedcowboy"
published_at: "2026-09-16T17:37:42Z"
captured_at: "2026-09-20T14:03:53+08:00"
lang: "en"
kind: "post"
topic: "开发者工具"
shard: "2026-09-20"
pub_day: "2026-09-16"
tags:
  - 语料
  - hn_show
  - author_spacedcowboy
  - story_49730393
  - show_hn
metrics: {"points": 2, "comments": 10, "engagement_velocity": 2}
comments_count: 10
comments_total: 10
discovered_via: "hn:show_hn:90d"
---

# Show HN: An ObjC-like compiler for Mac ARM, x86_64(Linux, Win), WASM, & others

> [!info] 一句话导读
> Show HN: An ObjC-like compiler for Mac ARM, x86_64(Linux, Win), WASM, & others

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49730393>
> 指标：点赞=2 · 评论=10 · engagement_velocity=2
> 作者：spacedcowboy　|　发布：2026-09-16T17:37:42Z
> 项目链接：<https://compile-xc.org/>
> 采集：2026-09-20T14:03:53+08:00　|　id：`dc5bdb60d33b1f7f`

## 正文

Show HN: An ObjC-like compiler for Mac ARM, x86_64(Linux, Win), WASM, & others | Hacker News

Show HN: An ObjC-like compiler for Mac ARM, x86_64(Linux, Win), WASM, & others

1 point by spacedcowboy 22 minutes ago | hide | past | favorite | discuss

Hi folks,

So this is my announcement of a compiler[1] I've been working on for about 6 months now (so yes, to get the obvious out of the way early, this was written with Claude code).

The compiler is called 'xc', stands for 'cross-C' or 'extended-C' or whatever you want, really. It's fairly similar to Objective-C in style (without the [] brackets), and in fact the first version of the language was written in ObjC.

It works on Mac M-series, Windows, and Linux - and any of these hosts can create binaries for any of {Mac M-series, Windows, Linux, Android, iOS, WASM, Arm9 (Zynq), m68k and even 6502}.

Building the compiler needs host-tools to bootstrap everything, either GNUStep on Linux, or a Mac with Xcode. Once built, however, the system is entirely self-contained, and you don't need any platform tools. I have a binary running on my iPhone which was compiled and signed on a Linux box... The suite ships with 5 host-specific assemblers, 10 object/executable writers, and a native Apple code-signer (we don't shell out to 'codesign') Downloads are available at [3] for all three hosts (xcc-osx-0.6.tar.bz2, xcc-linux-0.6.tar.bz2, xcc-win64-0.6.zip). Linux and Windows are larger because of static linking to make sure things are easy to run.

The documentation for the language is all at [2], it goes into the language details, but you get ARC (Automatic reference counting, which automatically goes atomic when you have threads), blocks, callbacks, Classes, and Protocols. It's an optimising compiler with a shared IR, deliberately not LLVM's IR because one of the original targets was the 6502, and LLVM likes register-rich architectures. The compiler runs Vectorize, LICM, LoopRotate, LoopUnroll (fixed and variable trip), StrengthReduce, Inline, TailRecursion, NarrowIV, PointerIV, RedundantLoadCSE, IdiomMemset, LoopReductionCollapse,...

One major inter-operability feature is the ability to say #import (or #use, which also promotes its statics into the bare-call space) and have the compiler read libGEM.so, parse its DWARF, and expose the functions, types and enum constants inside. Xc uses the platform's native structure packing, so binding a C library is mostly just pointing -L at it.

The Licence for the compiler is GPL3, for the standard library there's the "standard" library exception, since that code is bundled into most apps. Bottom line, you are free to create any applications you like, open or closed, without any licensing issues. If you make a fix to the compiler, I would appreciate the bug report/patch.

A utility in the tools/ section is c2xc. This takes almost all C code (I used it on Kundert's Sparse 1.4 — sparse.sourceforge.net) and converts it to valid XC. It might not be the best XC possible, but it will compile, and if you're trying to produce WASM code and can't just #use a dynamic library, this is the important part :)

There's also the beginnings of a cross-platform UI toolkit and Interface-Builder, though these are very early days.

There are 568 fixtures, 608 unit-tests, two simulators (6502 and 68k) and ~50 differential scripts to check output vs clang / binutils. The compiler is written in its own language, forming a "reference" ObjC compiler and the "shipped" written-in-xc compiler (all 120k lines of it), meaning it has two chances to find obscure bugs. Other real-world tests have been:

- transpiling Kundert's Sparse 1.4 to xc and diffing its test program's output against a clang build of the same library

- a circuit simulator built on it, checked against ngspice-47 and against an independent numpy MNA implementation

- writing a "test in anger" application, a server that listens for incoming web requests, parses them, uses them to query a DB and then sends the results out to a web-client (written in XC, and compiled to WASM)

Enjoy :)

1: https://github.com/ThrudTheBarbarian/xc

2: https://compile-xc.org/

# lucastononro/cc-subway

## 评论（10/10）

> **Rochus** · 2026-09-16T22:12:35.000Z　
> Wow, this is huge. Is the goal really to have a new language better than Objective-C, and to actually use it in projects, or mainly to demonstrate what an AI can do? As far as I understand, there is a non-trivial optimiser, assumingly also generated by AI, including the associated IR and lowerings. Are there comparisons of the resulting machine code quality and performance compared to e.g. GCC? Did you design and specify the xc language, and did the AI implement the frontend based on your specification, or was it a "full package" AI approach? (sorry if some questions were already answered on the web sites and the code, but it was too much to quickly get the answers)

---

> **spacedcowboy** · 2026-09-17T08:07:31.000Z　
> Hi, thanks for the kind words and interest :)It is indeed the goal to have a language better than (or at least fixing some of the pain points of) ObjC, and to make it truly cross-platform and just as easy to grok. Coming from C, I think ObjC was pretty much at the sweet-spot for complexity vs flexibility - there’s only a few things you have to learn over and above C and you get so much from that little extra.I’m already using it in one big project - and now this mentioned on HN has utterly failed [grin] I can put a link to https://blewit.net/ - the site isn’t really ready yet, another 6-8 weeks before launch, but if you want to see some of the WASM results, click on the sandbox link :)On the server side of blewit, everything is in xc, no apache, no scripting, and it uses the same classes there as it does in the WASM client. Plenty of C libraries compiled in with #use and then just linked: TLS, redis, Postgres libpq, …The compiler is mainly written with AI, but with a lot of supervision - those 6 months have been pretty much non-stop, with me being retired, and since I used to work for Apple for a couple of decades I have opinions on what the compiler should do (or not do) :)It started off as a project to write a new language for the 6502, if you look at https://atari-xt.com/ you’ll see a striking similarity in the website style... I knew I’d want more than one back end (st and xl) so from the start there was this idea of an IR that was flexible enough to handle register-rich and register-poor architectures, then I thought it’d be kind of useful to be able to write and test code on the Mac without loading it into the FPGA, so it was scaling from 8-bit to 64-bit pretty much immediately, with different executable formats; once that ground was laid it wasn’t too hard to extend it to the current multiple platforms.The optimiser is pretty thorough in terms of the classical operations. Where it still lacks is automatic vectorisation, clang vectorises code in lots of places you wouldn’t expect, but it also has a huge head-start over xc. Right now we’re sometimes on a par with a clang-compiled C program, but otherwise between 1.1x and 1.8x slower. There has been the occasional micro-benchmark where xc comes out faster :) I don’t actually have a benchmark suite, this is more informal testing during developmentof the optimiser and that’s something I should fix, not least because it’ll show where the next “bang for the buck” will be.It’s worth mentioning that most of my optimisation tests have been pretty low-level, so the clang version is written in C to make it easier to understand the assembly for this mere human, and xc has a bit more overhead with its automatic reference counting code, so a better future test might be to compare vs ObjC.Originally, I wrote up a 300 (or so) line spec for the language, and another spec for the IR, because it had to include automatic and transparent banked-memory use on the 6502 (so pointers were 3-bytes {bank, hi, lo}). Coming from using modern ObjC, I wanted ARC from the start, so that was built in, but it was only extended to blocks and callbacks (a callback is a ound function, an {object,method} or {nil,function} tuple) when we got onto the serious architecture support. It’s been “interesting” supporting a machine that doesn’t even support ‘mul’ alongside one that has vector simd :)Overall, I’d say the AI has done maybe 80% of the work, possibly 85% if I’m being generous. There have certainly been times I’m in the code changing things because it’s easier to express the difference between what it first came up with, and what I actually want, in actual code rather than English. On the other hand, I’d never even have attempted such a large project on my own. I see the AI as a massive force-multiplier on what can be done. It doesn’t get tired, it prevaricates (“I don’t want to make such a large change without ”) a lot less than humans, and it has alot of knowledge to draw on.One other thing I guess I should mention is that there is also the beginnings of a cross-platform UI framework, which uses an AppKit-like binding (you get things like TableView, CollectionView, OutlineView etc, with datasource protocols and delegates) but binds to the native widgets to provide a native look/feel/interaction from the same AppKit-like source. The docs go through it in more detail.This is only about 50% done, there’s a lot to finish off here. It helps that String in xc is native UTF8, but the binding part takes time. The fallback default is to draw the widget if there’s no binding, and until you pretty much 100% cover the native UI for a platform, it can look a bit jarring.Alongside that, there’s a tool ‘RoCkS’ which is even younger (maybe 10% there) which is intended to be the equivalent of Interface Builder. RoCkS is spelt that way because of the original atari origins... the GUI designer for GEM was "RCS" - Resource Construction Kit :) You design your UI with drag/drop and springs/struts, then bind UI objects in various layouts {desktop, tablet, phone} in {portrait, landscape} to the same core codebase. All with drag/drop, just like in Interface builder. Then the same application code can use a ‘phone’ UI layout when you compile the iOS/Android version, and use a ‘desktop’ layout when you compile a Windows/Linux/Mac version etc.At that point, I might re-announce on HN, because free and open-source cross-platform (and easy multi-platform) UI isn’t that common :)Again, thanks for the interest :) At least I got 1 comment :)

---

> **Rochus** · 2026-09-17T10:14:53.000Z　
> Interesting, thanks for the detailed explanations.Objective-C has indeed some impressive features, but also some inefficiencies and it got a bit out of favour over the years. Coming from the Wirth school I also understand the virtue and challenge of writing a compiler in his own language, but in practice it is often rather an obstacle than a benefit, and if a language is useful, there should never be a lack of representative projects. I thus write my own compilers always in a conservative C++98 subset or even in C so bootstrapping is never an issue and there is no second compiler necessary.Is your blewit, which sounds yet like another big code base, also AI generated/assisted? If I understand you correctly, you indeed have the engineering expertise to write compilers and to understand its architecture and complexities; so the project is not "vibe coded", but rather "augmented engineering"; I didn't manage to have a detailed look at the large code base yet, but in that case I would expect that it rather looks like a human engineered code base than the often strange looking architecture and code which I already have seen in Claude projects where the AI is just left alone for a few weeks.A performance within 1.1 to 1.8 on average of optimized Clang is a very good start for such a project.As I understand, the AI has implemented the frontend and lowering after your spec, which is amazing and demonstrates that it is able to work not only in and for the languages it was trained on. How was the AI able to demonstrate that your spec has been completely and correctly implemented? Is the language and IR spec somewhere on the web? What formalism did you use for the spec?I well remember GEM and also wrote software for Atari ST many years ago ;-)

---

> **spacedcowboy** · 2026-09-17T15:24:22.000Z　
> I'd already written a lot of it in ObjC, thinking it would be "just for me" before I moved to wanting it running on the FPGA. Three options- Port the ObjC runtime to my little OS on the FPGA ?- Rewrite everything in C so the native FPGA tools could compile it- Make it compile itself and treat the ObjC version as a bootstrap.#3 seemed the best option :)Blewit is a reasonably-sized project, but it's not on the same order as the compiler. It did shake out a few bugs in the compiler that the unit-tests etc. didn't find. At least, when you own the compiler, you don't submit a bug report to the developers and wait for a patch :)Yep, I'm happy with the optimisation - and I think most of the areas left are actually vectorisation - clang is very eager to vectorise (for good reason, it makes a difference)As for the spec, the original one is https://github.com/ThrudTheBarbarian/xc/blob/main/compiler/d... but that's now quite out of date (despite claiming to be the reference :) I'll update it, and also add a readable version to the website..We've really only added things that haven't broken fundamentals recently. The main recent additions were the block type (and since I agree with the thinking that spawned "http://goshdarnblocksyntax.com", we use 'block' not some convoluted ^ notation). Similarly a callback is a 'callback', the types were added and obey the usual grammar rules.The GEM desktop lives on: https://0x0000ff.co.uk/mov/xt/xtos-aug-11.mov :)- if you look at the bottom you'll see 2 icons (ST, XE) and clicking on that launches the emulation in a window, but since the actual desktop also uses GEM, you can run a GEM app (actually on either the ST or the XL) and open windows, drag them around etc.- There's a lot to do to get this desktop to be as useful as Magic! or Thing, but for various reasons it's on hold atm - mainly that I'm waiting on a physical garage to be built, which (today!) got rafters put on. Once that's in place, I'll have all the electronics stuff set up, and I can debug the motherboard that the FPGA plugs into.

---

> **Rochus** · 2026-09-17T16:06:48.000Z　
> Cool. Amazing to see what AI (Claude Code?) can do when the operator is an expert. It's like working as a lead engineer with a team. I never touched Claude code so far and am hesitant to give this tool direct access to my machine. I made some good experience with Google AiStudio when implementing my compilers and oberon system migration this year (see e.g. https://github.com/rochus-keller/oberonsystem3native/); it's fascinating that you can give it a bunch of sources with an error description and there is a very good chance that it points to the bug.

---

> **spacedcowboy** · 2026-09-17T16:41:14.000Z　
> It is actually pretty amazing what it can do, though sometimes it feels like herding cats. As I said, now and then I just dip into the code, rewrite something and tell it to adopt that pattern going forward.It takes a lot of the grunt-work out of writing something, and it actually is very much like running a team of junior engineers. I tend to run multiple threads at once (compiler, blewit, docs, framework), and often overnight I just give them a bunch of tasks to do, with files (/tmp/compiler, /tmp/blewit, …) to shout on, if they need input from, or have found relevant bugs for, another thread. I come down in the morning and spend the first hour or so just reviewing code.Or sometimes I come down and discover that one of them has proclaimed “it’s 3am (it wasn’t) and I’m not going to make a change at this hour”. Like, what ? You’re a machine! You don’t get sleepy…

---

> **Rochus** · 2026-09-17T18:31:49.000Z　
> I see, thanks; but what about the cost? Is this just a fixed subscription? If so, what level is necessary for such kinds of large projects? Can you just let it run ad infinitum, or are there daily or weekly limits, or do you even have to spend money by effort?

---

> **spacedcowboy** · 2026-09-17T21:30:58.000Z　
> I run Claude code (though I’m told open code runs better, I’m used to Claude) through deepseek, which costs me about £45 per month. That’s fine for me, though I realise everyone has their own limits.

---

> **Rochus** · 2026-09-18T01:46:42.000Z　
> Wow, that's far from expensive; actually incredible to get a full language with compiler and optimzier and a bunch of targets for just a few hundered dollars. That makes me feel like a movie theater pianist back when sound films first came out.

---

> **spacedcowboy** · 2026-09-19T08:40:30.000Z　
> Yeah, it was kind of eye-opening for me too. I honestly can’t see myself going back to “normal” programming.I’ve been around a while, was there when “the web” was a paradigm-shift (when I set up my first website, you had to email CERN to get put on a list of websites in the world), and this very much feels like another.But the only way to adapt to change on that level is to embrace it, revel in it, and seize it. At least IMHO :)

## 关联链接

- https://github.com/ThrudTheBarbarian/xc

## 导航

- 项目页：[[10-项目/compile-xc.org_45a8ddb3]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`开发者工具`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
