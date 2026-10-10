---
type: "corpus"
item_id: "58fd0a7ea2eb911c"
title: "Show HN: Axiom: The Functional Systems Langauge"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50028197"
project_url: "https://axiomlang.software/"
author: "chrispaig3"
published_at: "2026-10-10T00:18:58Z"
captured_at: "2026-10-10T09:53:50+08:00"
lang: "en"
kind: "post"
topic: "开发者工具"
shard: "2026-10-10"
pub_day: "2026-10-10"
tags:
  - 语料
  - hn_show
  - author_chrispaig3
  - story_50028197
  - show_hn
metrics: {"points": 2, "comments": 0, "engagement_velocity": 2}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:3d"
---

# Show HN: Axiom: The Functional Systems Langauge

> [!info] 一句话导读
> Skip to content 0.7.8 Why Axiom Tour Performance Status Docs Get started

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50028197>
> 指标：点赞=2 · 评论=0 · engagement_velocity=2
> 作者：chrispaig3　|　发布：2026-10-10T00:18:58Z
> 项目链接：<https://axiomlang.software/>
> 采集：2026-10-10T09:53:50+08:00　|　id：`58fd0a7ea2eb911c`

## 正文

Skip to content 0.7.8 Why Axiom Tour Performance Status Docs Get started
Axiom 0.7.8 / Open source. Built in Axiom. The functional systems language
 High-level thinking.
 Native-level control.
 Express your ideas with powerful types. Catch missing cases and check effects at compile time. Ship a native binary with no VM or garbage collector.
 Build with Axiom Explore the language ↗
 For people who care how their code reaches the machine.
AX / NATIVE COMPILATION 001
 SOURCE / .ax (fn (square x) (* x x))
 NATIVE EXECUTABLE Ideas in. Machine code out.
 Axiom LLVM IR Native
01 / Expressive by design Types that model your ideas. 02 / Explicit where it counts Effects the compiler checks. 03 / Native from the start LLVM. Straight to the machine.
 See it in action
 A small program. The whole picture.
Write it. Run it. Break it.
Watch the compiler catch what changed.
shapes.ax — from source to executable PAUSE
 shapes.ax 31 : 37
 1 ( import IO )
 2
 3 ( data Shape
 4 ( Circle { r : Float } )
 5 ( Rect { w : Float, h : Float } )
 6 ( Triangle { b : Float, h : Float } )
 7 ( Hexagon { side : Float } ) )
 8
 9 ( :: area ( -> Shape Float ) )
 10 ;@axiom:restrict(no-io)
 11 ( fn ( area s )
 12 ( match s
 13 ( ( Circle { r = r } ) ( * 3.14159 ( * r r ) ) )
 14 ( ( Rect { w = w, h = h } ) ( * w h ) )
 15 ( ( Triangle { b = b, h = h } ) ( / ( * b h ) 2.0 ) )
 16 ( ( Hexagon { side = a } ) ( * 2.598076 ( * a a ) ) ) ) )
 17
 18 ( :: report ( -> String Shape Int ) )
 19 ;@axiom:effect(io)
 20 ( fn ( report name s )
 21 ( let ( ( a ( area s ) ) )
 22 ( println " {name:<10} {a:>8.2} " ) ) )
 23
 24 ( :: main Int )
 25 ;@axiom:effect(io)
 26 ( fn ( main )
 27 {
 28 ( report "circle" ( Circle 2.0 ) )
 29 ( report "rect" ( Rect 3.0 4.5 ) )
 30 ( report "triangle" ( Triangle 4.0 3.0 ) )
 31 ( report "hexagon" ( Hexagon 2.0 ) )
 32 0
 33 } )
sh ~/demo
 ~/demo $ axiom run shapes.ax
 circle 12.57
rect 13.50
triangle 6.00 ~/demo $ axiom check shapes.ax
 error [AX3005] : non-exhaustive pattern match: missing Hexagon
 --> shapes.ax:12:10
 |
 12 | (match s
 | ^ this `match` does not cover: Hexagon
 |
 = help: add the missing arms, each a `todo` until it is written ~>
 ((Hexagon _) (todo "Hexagon"))
 = help: run `axiom explain AX3005` for a full explanation
compilation failed due to 1 previous error
 ~/demo $ axiom run shapes.ax
 circle 12.57
rect 13.50
triangle 6.00
hexagon 10.39 ~/demo $ axiom build shapes.ax -o shapes
 Build successful: shapes ~/demo $ ./shapes
 circle 12.57
rect 13.50
triangle 6.00
hexagon 10.39 ~/demo $
[ 5 / 5 ] A native executable, with its allocator and syscalls inside it.
 [axiom] 0 : write
 1 : run
 2 : break
 3 : fix
 4 : ship *
A recorded terminal session: A sum type: three shapes, each with named fields. area promises it performs no I/O. The compiler holds it to that. report prints, so it says so: effect(io). Compile and run in one step. No build file. $ axiom run shapes.ax Add a fourth shape, and nothing else. The match in area no longer covers every shape. The compiler names it, and the missing arm. $ axiom check shapes.ax Handle the hexagon, and report one. $ axiom run shapes.ax A native executable, with its allocator and syscalls inside it. $ axiom build shapes.ax -o shapes $ ./shapes
 Your next native binary starts here. Prebuilt for macOS & Linux arm64. Setup & other targets
$ curl -fsSL https://raw.githubusercontent.com/chrispaig3/axiom/trunk/scripts/install.sh | bash
 Copy
Early-stage language. Real compiler. See what’s ready today.
Why Axiom
 A small language. Serious capabilities.
 The expressiveness of functional programming, with a direct path to native code. Every design choice gives you something concrete to work with.
01 Ship the binary. That’s it.
 Your program compiles to a native executable, with its allocator included and direct calls to the kernel. No VM to provision. No garbage collector to tune.
 scripts/check-freestanding.sh
 02 Make side effects explicit.
 Keep computation separate from I/O. The compiler infers effects, checks restrict(no-io) , and requires functions that perform I/O to declare it.
 ;@axiom:restrict(no-io)
 03 Find the problem. Keep moving.
 Get a precise location, a stable error code, and often a fix your tools can apply. axiom explain has a page for each one of the 108 codes.
 axiom explain AX3005
 04 Built for you. And your agents.
 Uniform syntax keeps code generation predictable. Structured diagnostics, exact spans, and stable symbol IDs give your tools the same facts you use to review their work.
 --diagnostic-format=ai
 05 Read the compiler. In Axiom.
 The compiler is over 119,000 lines of Axiom. A clean checkout rebuilds it from committed LLVM IR with llc and a C linker, and stops unless two generations are byte-identical.
 scripts/bootstrap-from-seed.sh
 06 Bring Rust along.
 Keep useful Rust code within reach. Declare functions in an extern block; --crate builds and links the crate. Rust values are dropped when their last Axiom reference goes.
 axiom build --crate DIR
The tour
 Get a feel for the language.
 Ten working programs, from your first data type to calling Rust. Explore the code, follow the annotations, and see exactly what each program prints.
01 Types & matching 02 Records 03 Errors 04 Effects 05 Collections 06 Concurrency 07 Regions 08 Macros 09 Testing 10 Cereal 11 Dates & times 12 Task pools 13 Asset protection 14 Calling Rust
 01 / 14 · parcels.ax
 Shipment status report
 Sum types with named fields, matched exhaustively. Option is built in, so a missing value is a type rather than a null.
 L 6 A constructor can carry named fields.
 L 18 alert returns Option String , because some parcels need no action.
 L 31 optUnwrapOr supplies the default where there is no value.
 L 33 {id:<9} pads to nine columns. Format strings are compiled, not interpreted at run time.
 parcels.ax Copy
 1 ( import IO )
 2 ( import Err )
 3
 4 ( data Parcel
 5 ( Ordered )
 6 ( InTransit { carrier : String, days : Int } )
 7 ( Held { why : String } )
 8 ( Delivered ) )
 9
 10 ( :: status ( -> Parcel String ) )
 11 ( fn ( status p )
 12 ( match p
 13 ( ( Ordered ) "packing" )
 14 ( ( InTransit carrier days ) ( format " {carrier} , {days} days out" ) )
 15 ( ( Held why ) ( format "held at {why} " ) )
 16 ( ( Delivered ) "delivered" ) ) )
 17
 18 ( :: alert ( -> Parcel ( Option String ) ) )
 19 ( fn ( alert p )
 20 ( match p
 21 ( ( Ordered ) ( Some "not shipped yet" ) )
 22 ( ( InTransit _ _ ) None )
 23 ( ( Held why ) ( Some ( format "call about {why} " ) ) )
 24 ( ( Delivered ) None ) ) )
 25
 26 ( :: row ( -> String Parcel Int ) )
 27 ;@axiom:effect(io)
 28 ( fn ( row id p )
 29 ( let (
 30 ( s ( status p ) )
 31 ( a ( optUnwrapOr ( alert p ) "-" ) )
 32 )
 33 ( println " {id:<9} {s:<22} {a} " ) ) )
 34
 35 ( :: main Int )
 36 ;@axiom:effect(io)
 37 ( fn ( main )
 38 {
 39 ( println "parcel status action" )
 40 ( row "AX-1041" Ordered )
 41 ( row "AX-1042" ( InTransit "DHL" 2 ) )
 42 ( row "AX-1043" ( Held "customs" ) )
 43 ( row "AX-1044" Delivered )
 44 0
 45 } )
Show all 45 lines
 $ axiom run parcels.ax
 parcel status action
 AX-1041 packing not shipped yet
 AX-1042 DHL, 2 days out -
 AX-1043 held at customs call about customs
 AX-1044 delivered -
Read more: Pattern matching Next: Records
Performance
 Small binaries. Measured performance.
 In this Collatz benchmark, Axiom runs within milliseconds of C and Rust, with a binary close to C’s size. One workload, one machine, with the source and method available for you to reproduce.
Run time All three within 5 ms 3,000,000 Collatz sequences · hyperfine best of 20, interleaved Axiom 0.443 s
 Rust 0.448 s
 C 0.444 s
All three finish within five milliseconds of one another. Axiom emits LLVM IR, so a loop that is only arithmetic and branches gets the machine code the other two get.
 Compile to a native binary Axiom is the slowest, by 49 ms one file, cold · hyperfine best of 15, interleaved Axiom 0.166 s
 Rust 0.117 s
 C 0.151 s
Axiom is the slowest of the three, by forty-nine milliseconds against rustc at 1.42x, and fifteen behind clang at 1.10x. Published because it is what was measured, by the script beside the sources.
 Binary size 13× smaller than Rust, 7% over C the executable on disk Axiom 35,784 B
 Rust 469,608 B
 C 33,432 B
Thirteen times smaller than the Rust binary, and about seven percent larger than C, with no C runtime inside it at all.
 Undefined symbols 0 for Axiom, 70 for Rust, 1 for C nm -u  | wc -l Axiom 0
 Rust 70
 C 1
The whole program is in the file. Nothing is resolved at load time, because there is nothing left to resolve.
Apple M1, macOS 27.0.1, darwin-aarch64 · Axiom 0.7.8 · rustc 1.98.1 · clang 23.1.2 · timed with hyperfine 1.20.0 . All three print 428343467 .
 How it was measured, and the table behind the charts Collatz step counts for 1..3,000,000, summed and printed. Signed 64-bit integers, no allocation, no library call in the hot loop. Each figure is the best of its runs, not the mean: interference only ever makes a run slower, so the minimum is the closest estimate of the cost itself.
 The runs are interleaved , one repetition of each binary in turn, and that correction changed the answer. A first pass that ran each binary in a block put Axiom 1.6× behind Rust. It was an artefact: a background build starting midway taxes whichever block it lands on. Alternating gives every binary the same interference, and the three collapse onto each other.
 The three programs are in the repository, in web/bench/ , and run-bench.sh beside them produces every cell of this table, so it can be re-run rather than taken on trust. Go and Haskell are absent because no toolchain for either was on the machine, and this project publishes only numbers it has measured. One micro-benchmark says nothing about allocation-heavy work, which scripts/bench-datastructures.sh measures separately, and less flatteringly.
 axiom build --input collatz.ax --output out-axiom
 rustc -O collatz.rs -o out-rust
 clang -O2 collatz.c -o out-c
Run time, compile time, binary size and undefined symbol count for the same Collatz workload in Axiom, Rust and C. Measurement Axiom Rust C
 Run time 3,000,000 Collatz sequences · hyperfine best of 20, interleaved 0.443 s 0.448 s 0.444 s
 Compile to a native binary one file, cold · hyperfine best of 15, interleaved 0.166 s 0.117 s 0.151 s
 Binary size the executable on disk 35,784 B 469,608 B 33,432 B
 Undefined symbols nm -u  | wc -l 0 70 1
How it compares
 A different set of tradeoffs.
 Functional types, explicit effects, and native output in one language. See how Axiom’s choices sit alongside Rust, Go, and Haskell.
Axiom Rust Go Haskell
 Memory Bump allocation, reference counting, and regions when you choose the moment. No tracing collector, no borrow checker. Ownership and borrowing Tracing GC Tracing GC
 Inside the binary Your code, its allocator and raw syscalls. No C library function is called. std links the C library GC and scheduler runtime The GHC runtime system
 Side effects Inferred per function; declared or restricted with a tag the compiler checks. Not tracked Not tracked Tracked in types, by hand
 Macros Rewrite the program tree before type checking; hygienic. Token streams None Template Haskell
 Build and run axiom run f.ax : one step, no build file needed. cargo go build cabal or stack
Get started
 Your first native binary starts here.
 Axiom needs llc from LLVM and a C compiler for the final link. The compiler itself is written in Axiom, so there is no other toolchain to install first.
Install LLVM and a C compiler
macOS Debian & Ubuntu Anything else
 $ xcode-select --install
 Copy
 $ brew install llvm
 Copy
 $ export PATH="$(brew --prefix llvm)/bin:$PATH"
 Copy
 The Command Line Tools supply the C compiler for the final link; Homebrew's LLVM supplies llc , which is not on the default path.
Install Axiom
 A prebuilt archive where one exists; otherwise, build from the committed seed.
Installer From source
 $ curl -fsSL https://raw.githubusercontent.com/chrispaig3/axiom/trunk/scripts/install.sh | bash
 Copy
 $ export PATH="$HOME/.axiom/bin:$PATH"
 Copy
 For macOS and Linux on arm64. It verifies the archive's SHA-256, then builds and runs a program that imports the standard library with the new compiler before it replaces anything, and it only ever replaces an installation it made itself.
Start a project and run it
 axiom new writes a program and an axiom.pkg manifest. Inside a project, run and build need no file name.
$ axiom new hello && cd hello && axiom run
 Copy
 hello/Main.ax Copy
 ( import IO )
( :: main Int )
 ;@axiom:effect(io)
 ( fn ( main )
 {
 ( println "Hello from Axiom! 🚀" )
 0
 } )
$ axiom run
 Hello from Axiom! 🚀
The commands you will use most
 axiom check type-check and verify every effect claim, no code generation
 axiom build a native executable, named after the project
 axiom test every function whose name starts with test
 axiom fmt the one canonical layout
 axiom explain AX3005 the full explanation behind any diagnostic code
 axiom symbols Main.ax --calls declarations, effects, stable IDs and call edges in AXSYM
 axiom emit-llvm Main.ax -o Main.ll inspect the LLVM IR before assembly
 axiom build Main.ax --obfuscate -o app optional literal masking and internal symbol scrambling
 axiom repl an interactive session, compiled to native code line by line
 Set up your editor for highlighting, go-to-definition, hover and fixes.
 Imported modules come from the entry directory, package dependencies and explicit search paths. Set AXIOM_PATH for extra module roots and AXIOM_STDLIB to override the installed library. Module search and compiler inspection
Where it runs
 Target Prebuilt Notes
 darwin-aarch64 yes Apple silicon. Prebuilt archive.
 linux-aarch64 yes Prebuilt archive.
--target emits for any of them from any host; only the final link needs that target's linker. Source-only targets: baremetal-aarch64 , darwin-x86_64 , freebsd-aarch64 , freebsd-x86_64 , linux-x86_64 , windows-aarch64 , windows-x86_64 . --target emits for them, and CI doesn't run the test battery there. What "supported" means here .
 Bare-metal AArch64 uses a board-defined platform seam and an optional QEMU smoke run. The compiler doesn't run on Windows: cross-compile to it from Linux or macOS. Embedded targets
Status
 Know what’s ready. See what’s next.
 Axiom is 0.x : ready to explore, still evolving. Start with a tool, an experiment, or a contribution. Use this status map to decide where it fits; these rows reflect the project’s tested implementation status.
Complete
 Functions & types Complete Curried signatures, rigid type variables, exact return types.
 ADTs / data types Complete Sums with positional or named fields.
 Pattern matching ( match ) Complete Nested, exhaustive, checked in every function.
 Structs Complete Per-field mut , generic parameters, automatic rendering.
 Lambda / function values Complete Closures, partial application, _ holes.
 Loops Complete for over ranges and containers, while .
 Syscalls Complete No libc between your program and the kernel on any of the eight hosted targets.
 Module visibility Complete Only pub leaves a module.
 Self-hosting Done The Rust compiler it replaced has been deleted.
Working, with stated limits
 Effects Enforced; two limits stated Two inference gaps, both stated: unresolvable calls are marked incomplete, and constructor allocation is not counted.
 Macros Partial A template cannot generate import or a nested macro , or test two binders for sameness.
 Concurrency Language form, two lowerings parallel , channels, a mutex and task pools; taskFold reclaims each delivered answer under an explicit scalar-only callback contract.
 Region syntax Checked scope, and annotated signatures with the escape rule Scalars leave a region; typed promotion is planned.
 Resource ownership Functional Files, sockets, terminal modes, channels and mutexes close or free themselves when their last owner lets go.
 FFI Functional Rust through extern blocks, sealed owners and callbacks borrowed for the call.
 Standard library Functional Collections, cryptography, optional binary obfuscation, dates, JSON, networking and an embedded database.
 Error handling Functional; adopted at the syscall seam Result , the try form, and handlers that skip a bad record without unwinding.
 Editor support Functional Language server plus a tree-sitter grammar.
Removed
 Type classes Replaced By capability records: an interface is a struct of functions.
 Lists Removed Sequences are (Vec T) .
 Tuples Removed Products are struct , sums are data .
 Linear types Removed Deterministic reclamation is reference counting's job.
Not here yet: a package index and version pinning, async and a scheduler, a compiler that runs on Windows (it builds Windows executables from elsewhere), and prebuilt archives beyond arm64. The full table
FAQ
 A few things worth knowing.
 Is Axiom ready for production? Not for most teams yet. It is 0.x: the core language (types, matching, structs, loops, modules) is complete, the FFI, standard library and editor support are functional, and macros are partial. Every row of the status table names the test behind it.
 There is no package index and no green threads. What is here is a small language whose compiler you can read and whose claims are tested.
 Implementation status
 Does it have a garbage collector? No tracing collector. Memory comes from a bump allocator over mmap , and every heap block carries a reference count, so a value is freed the moment its last reference dies, with nothing written in the source. Files, sockets, channels and mutexes are owners too: each closes or frees itself when its last reference goes. When you want reclamation at a point of your choosing, (region r body) rolls the allocator back in one step.
 The memory model
 What does "no libc" actually mean? The code Axiom generates, and its standard library, reach the kernel through raw syscalls: printing, allocation, files, processes and sockets included. scripts/check-freestanding.sh fails the build if the generated IR calls a C library function or the executable imports one.
 The final link is done by your system C compiler, which on Linux adds the C runtime's startup code; on macOS arm64, nm -u on a compiled program is empty. An extern block to Rust is the one way out, and a no_std crate adds no C library function through it.
 The freestanding gate
 Why S-expressions? Because the program is already a tree. There is no operator precedence to memorise, no ambiguous parse, and macros operate on the same structure the compiler checks. That uniformity is also what makes the language easy for a tool or an agent to generate correctly.
 The editor side is covered: a tree-sitter grammar colours by syntactic role with rainbow brackets, and axiom fmt settles layout.
Can I make a distributed binary harder to inspect? Choose axiom build Main.ax --obfuscate -o app to mask string literals, scramble internal function names and strip local symbols. Fresh build seeds make each build differ. The mode retains opaque function entries through optimisation and omits source-level backtrace tables.
 Crypto.Obfuscate also packs authenticated encrypted assets with context binding, split key shares and explicit key erasure. These features make static inspection harder; someone inspecting the running process can recover embedded keys and decoded data. Static archives do not accept the compiler flag.
 Binary and asset obfuscation
 How can tools inspect my program? axiom --diagnostic-format=ai symbols Main.ax --calls emits AXSYM declarations, stable IDs, author tags, derived effects and call edges. Agent.Tags reads that stream, including effect and macro declarations. Use AI format for symbols; JSON format is refused.
 symbols --mir --axir exposes analysis and inspection records. Native builds compile the checked, expanded syntax tree to LLVM IR. Use emit-llvm to see that output.
 Follow a program through the compiler
 Do I have to annotate every function's effects? No. Four effects must be declared through the call chain: effect(io) , effect(entropy) , effect(spawn) and effect(block) . Allocation and mutation are inferred and reported. A function that performs a raw operation, calls an extern or casts a value into an unrelated reference type declares effect(unsafe) . A trusted wrapper contains that obligation for its callers. restrict(...) and pure add stronger checks where you need them.
 Effects in the reference
 Are there traits or type classes? They were replaced by capability records. An interface is a parameterised struct holding functions, and an instance is an ordinary value of it, passed where it is needed. Dispatch is application: no table, no resolution rules, and a function generic over an interface can call its methods.
 Capability records
 Is there a package manager? A project is an axiom.pkg file: axiom new writes one. A depend line names a directory of modules or a git URL, axiom fetch clones the URLs, and two dependencies may never provide the same module. There is no central index and no version pinning yet, and the compiler never fetches or runs another project's build on its own.
 Packages in the reference
 Why does the compiler have an "ai" output format? For agents and other tools. --diagnostic-format=ai prints one line per diagnostic with exact spans and any fix that applies, and axiom symbols prints one line per declaration with an id that survives reformatting, so a tool can learn what a file provides without reading it again. The human report is rendered from the same diagnostic, so the two cannot disagree.
 Diagnostics and AXSYM
From idea to executable
 Think in types.
 Build something native.
 Your first program is a few commands away. Try the language, inspect the compiler, and help shape what comes next.
 Get started Explore the source
(λ)
 A small language for ambitious ideas. Built in the open, with room for your contribution. Open an issue .
 Axiom 0.7.8 · MIT licensed · © 2026 Chris Paige
High-level thinking. Native-level control.
Learn
 Tour
 Language reference
 Docs overview
 Standard library
 Public API
 Examples
 Editor setup
 Calling Rust
 TCP networking
 Dates & times
 Cryptography
 Binary obfuscation
 Embedded database
 Specifications
 Memory model
 Error model
 Diagnostics
 Agent harness
 Compiler inspection
 Symbol metadata
 Compatibility
 Status
 Project
 GitHub
 Releases
 Changelog
 Contributing
 Security
 Issues

## 关联链接

- https://raw.githubusercontent.com/chrispaig3/axiom/trunk/scripts/install.sh

## 导航

- 项目页：[[10-项目/axiomlang.software_de3e2d4d]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`开发者工具`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
