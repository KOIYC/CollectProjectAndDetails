---
type: "corpus"
item_id: "5af0d2b1ea9e5e33"
title: "Show HN: Shrinking my 159-byte x86-64 Hello World ELF to 153 bytes"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50230693"
project_url: "https://blog.lohr.dev/hello-world-contd"
author: "michidk"
published_at: "2026-10-25T12:00:06Z"
captured_at: "2026-10-26T09:42:36+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-10-25"
pub_day: "2026-10-25"
tags:
  - 语料
  - hn_show
  - author_michidk
  - story_50230693
  - show_hn
metrics: {"points": 3, "comments": 0, "engagement_velocity": 3}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:3d"
---

# Show HN: Shrinking my 159-byte x86-64 Hello World ELF to 153 bytes

> [!info] 一句话导读
> Skip to main content Hashnode Michi's Blog

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50230693>
> 指标：点赞=3 · 评论=0 · engagement_velocity=3
> 作者：michidk　|　发布：2026-10-25T12:00:06Z
> 项目链接：<https://blog.lohr.dev/hello-world-contd>
> 采集：2026-10-26T09:42:36+08:00　|　id：`5af0d2b1ea9e5e33`

## 正文

Skip to main content Hashnode Michi's Blog
Back to My Website Back to My Website
 Search Ctrl K ⌘K Toggle theme Write Open menu
Smallest "Hello World" continued
 Updated October 10, 2026 · 13 min read · Markdown
M Michael Lohr
On this page
 Loading the first syscall number directly Loading the message's address directly Loading the message length directly Pushing the syscall number onto the stack Never fail Settling the bill Failing gracefully, for free On to new waters What about Zig?
Nearly two years ago, I wrote about the smallest possible "Hello World!" program . It's one of my most read blog posts. Recently, I started playing around a lot with AI (like almost everybody else), so I thought: let's fact-check my previous blog posts! Turns out I was wrong: I actually did not create the smallest possible 'Hello World' program!
Buuut, I was pretty close! To summarize the rules of this challenge:
runs on modern 64-bit x86 Linux
executes directly, without a separate program or decompression step
is a proper, specification-compliant executable
keeps instructions outside the ELF header and program headers
prints Hello, World!\n (14 bytes) to stdout and exits with status 0
My previous result: 159 bytes (or 121 bytes in the 32-bit version). How did I get there? Using assembly and manually constructed ELF headers. These rules are important, as people have gotten as small as 77 bytes by hacking the ELF header. That example also needs five-level paging and permissive memory-overcommit settings, so it doesn't run on every modern x86-64 Linux machine. Header instructions aren't automatically invalid ELF, which is why I'm explicitly excluding them here.
My previous solution—can you spot what's wrong with it?
https://gist.github.com/michidk/aaf08c7678e02b574973556d0fba741e
Codex Astra found a better solution that was able to reach 153 bytes .
Loading the first syscall number directly
To print the message, I first put the write syscall number, 1 , into rax . My original version used push 1; pop rax , which takes 3 bytes .
But in this directly loaded static Linux executable, rax starts at zero: it receives the successful exec return value. So we only need to change its lowest byte!
While eax is a 32-bit subregister of the 64-bit rax , there is another one: al is the lowest 8 bits of the rax register, so just one byte (= 8 bits, duh)! The constant also fits in one byte, making mov al, 1 just 2 bytes long.
; Before: 3 bytes
push 1
pop rax
; After: 2 bytes
mov al, 1
That's 1 byte saved . It relies on Linux's startup behavior, which is fine for our Linux-specific challenge. It isn't a general guarantee for an entry point reached through some other loader.
Loading the message's address directly
I used lea to calculate a pointer to the message bytes and put it into the lower 32 bits of the rsi register, which is the register the write syscall expects for its buffer pointer. It calculates the address from the instruction pointer plus a relative offset and requires 6 bytes to encode the assembly instruction.
By using mov instead, I directly embed the address as a 32-bit constant, only taking up 5 bytes (1 byte less). This works because my executable loads at the fixed address 0x400000 , so the message's address is known and fits within 32 bits. Writing esi also clears the upper half of rsi , producing the correct 64-bit pointer. The exact address isn't special, but it needs to be fixed and fit within 32 bits. The original lea esi also truncates its result to 32 bits.
; Before: 6 bytes
lea esi, [rel msg]
; After: 5 bytes
mov esi, msg
Loading the message length directly
For the message length, I used another stack operation: push 14; pop rdx , taking 3 bytes .
Linux also starts rdx at zero in this executable. So, just like with rax , we can set only its lowest byte. That byte is called dl .
; Before: 3 bytes
push 14
pop rdx
; After: 2 bytes
mov dl, 14
This takes 2 bytes , saving another byte! The rest of rdx stays zero, leaving the whole register equal to 14.
These initial register values come from Linux's ELF initialization . Our program doesn't have a dynamic loader that could change them before our code runs.
Pushing the syscall number onto the stack
To exit the application gracefully, one calls the exit syscall, whose number is 60 . For that I used mov eax, 60 , which takes up 5 bytes .
Instead of using mov , one can also push that number onto the stack and then just pop it into the rax register. push can encode the small constant with a one-byte immediate, taking 2 bytes . pop rax adds 1 byte , setting the entire register to 60 and restoring the stack pointer within just 3 bytes .
That saves 2 bytes , though it accesses the stack. Unlike mov al, 60 , it remains correct even if the preceding write syscall returned a negative error code.
; Before: 5 bytes
mov eax, 60
; After: 3 bytes
push 60
pop rax
Wait, didn't we previously replace push and pop with mov ? Yes! At startup, we knew the registers were zero. After write , rax contains the syscall's return value. Different starting values, different optimizations.
Nice! There is another improvement, though:
Never fail
We can shave off one more byte from exactly that piece of code we just optimized. But it's a bit hacky:
; Before: 3 bytes
push 60
pop rax
; After: 2 bytes
mov al, 60
Just like mov al, 1 , this instruction is only 2 bytes long. This time, though, we need the preceding write to leave the upper bits of rax at zero.
This works when write succeeds and returns 14. Linux puts 0x000000000000000E into the whole rax register, so all its upper bits are zero. Replacing its lowest byte with 60 then leaves rax equal to 60. In fact, any return value from 0 to 255 would work this way, although only a complete 14-byte write prints our whole message.
However, if write fails, the raw syscall returns a negative error code whose upper bits are set. Changing only al leaves an invalid syscall number in the low 32 bits, which Linux uses to dispatch the call. Linux rejects that syscall with -ENOSYS , so our program continues past its final instruction and, in this executable, causes a segmentation fault.
Is this compliant with our rules, though? I'd say yes, if we explicitly assume that stdout accepts all 14 bytes in one successful write. If it can't accept our message, we can't print the required "Hello World" anyway. With the original startup code, we'd need the 156-byte version to also exit with status 0 after a returned write error. But we'll fix that below without adding any bytes! Neither version retries partial writes.
Settling the bill
So with all five changes, we are down to 153 bytes for the 64-bit version! Three one-byte savings in the setup for write , plus another three bytes saved in the setup for exit : 159 − 1 − 1 − 1 − 2 − 1 = 153 .
Here's the final 64-bit version, including the improved exit setup explained below:
https://gist.github.com/michidk/a2d048a126956ec4f6cf335f9782c37a
The 32-bit version gets even smaller: 114 bytes , down from 121! It already used mov for the pointer, but the startup tricks work here too: mov al, 4 for write , mov dl, 14 for the length, and a one-byte inc ebx to turn the initial zero into stdout's file descriptor, 1. Two one-byte xchg instructions prepare exit(0) even after a returned write error. Unlike the 64-bit version, the exit syscall number is already 1, so we don't need another mov al ! The 32-bit version is a separate comparison and needs Linux's 32-bit compatibility support. You can find it here .
Of course, this doesn't prove that we've reached the absolute minimum. More assumptions, more bytes saved!
Failing gracefully, for free
We got smaller, but our exit setup still depends on write succeeding. Can we fix that without making the program bigger? Turns out, yes!
So far, we've only looked at setting the exit syscall number. But exit also needs an exit status in edi . Our code used xor edi, edi to set it to zero: XORing a value with itself makes every bit zero. This takes 2 bytes and also clears the upper half of rdi . Together with mov al, 60 , that's 4 bytes to prepare exit(0) .
Linux also starts rbx at zero, and our program never changes it before this point. Meanwhile, edi still contains 1 , the stdout file descriptor. The write syscall preserves those registers.
Meet xchg , short for exchange! It swaps the values of its two operands. So xchg eax, ebx puts the old value of ebx into eax and the old value of eax into ebx , without needing a temporary register. These swaps don't access the stack or memory.
There's also a handy encoding trick: when one of the registers is eax , x86 has a special short form. Both xchg eax, ebx and xchg eax, edi take just 1 byte each!
We can use those two instructions to swap our values into place:
; Before: 4 bytes
mov al, 60
xor edi, edi
; After: 4 bytes
xchg eax, ebx
xchg eax, edi
mov al, 60
The first exchange puts zero into eax and moves write 's return value into ebx . The second puts 1 into eax and zero into edi , which is our exit status.
Now rax has a known value again, so mov al, 60 safely sets it to 60. This works even when write returned a negative error code! The exchanges write 32-bit registers, which also clear their upper halves.
Each xchg takes just 1 byte , and mov al, 60 takes 2 bytes . That's the same four bytes as our previous exit setup. We stay at 153 bytes , but no longer need the successful-write assumption for the exit syscall. We still need a complete write to print the whole message, of course.
On to new waters
In the last post, we also wondered what the smallest Rust and Zig versions would be.
The answer is not that easy.
The safe version is:
https://gist.github.com/michidk/8af37f2f21a943522b35110857ae76d5
With 4,506,168 bytes (about 4.3 MiB ) on Rust 1.98.1 , compiled directly with rustc and no optimization flags, this is quite large! That only counts the executable; its shared system libraries aren't included.
But if we allow assembly, we can just use Rust as a wrapper and write our own assembly inside Rust. Furthermore, we want to use no_std (so no Rust standard library), use no_main , and define our own entry point _start , as well as calling Linux syscalls to help reduce the overhead:
https://gist.github.com/michidk/0addb0fdcb7de291033027e742f44522
Can we use our new assembly tricks here too? Yes! We make _start a naked function with #[unsafe(naked)] and put the entire instruction sequence in naked_asm! . That gives us control over every instruction: Rust doesn't add a function prologue or epilogue, so Linux's initial register values reach our assembly untouched. Rust documents naked assembly here .
This one takes up 1,616 bytes without size optimizations. It still needs -Cpanic=abort , -Crelocation-model=static , -Clink-arg=-nostartfiles , and -Clink-arg=-static , so these aren't completely default compiler flags. Static relocation lets us embed the fixed message address, and static linking keeps the dynamic loader from changing the initial registers before our code runs. This unoptimized build uses Rust's default LLD selection.
It also uses our two xchg instructions, so a returned write error no longer breaks the exit syscall!
But we can further get this down to 209 bytes by playing around with the compiler flags.
These measurements use Rust 1.98.1 , with GNU ld 2.47.20260726 for the optimized builds. Other compiler and linker versions might produce different sizes.
The Cargo.toml settings control compilation:
opt-level = "z" optimizes for small code rather than maximum speed
panic = "abort" disables panic unwinding, which this build requires
strip = "symbols" removes symbol names and debugging information
lto = true lets LLVM optimize across crate boundaries
codegen-units = 1 keeps the crate in one compilation unit, giving the optimizer more visibility
We also want to set the following rustflags in .cargo/config.toml :
https://gist.github.com/michidk/86cd97a26c4fe05638340ba9bf8a485c
Save that gist's config.toml as .cargo/config.toml .
-Cforce-unwind-tables=no avoids forcing the generation of stack-unwinding metadata
-Crelocation-model=static generates code suitable for fixed addresses rather than position-independent loading
-Clinker-features=-lld disables Rust's automatic LLD selection. On our machine, this selects GNU ld, whose layout and options produced the measured result
The next two options are passed through -Clink-arg :
-nostartfiles skips the usual C startup objects. Our program supplies _start itself
-static prevents linking against shared libraries. Since this program needs no external libraries, it also avoids dynamic-loader machinery
The long -Wl,... argument forwards these comma-separated options to GNU ld:
--build-id=none omits the build-identification note
-z noseparate-code allows code and read-only data to share a load segment, avoiding extra headers and page-alignment padding
-z nosectionheader omits the section-header table. Linux can execute the file using its ELF and program headers
--no-eh-frame-hdr omits the unwind-information search header and its program-header entry, but doesn't by itself remove all unwind data
With these files in place, cargo build --release produces the 209-byte version. The settings apply to the release profile, so an ordinary cargo build won't produce this size.
We can even supply our own linker instructions to arrive at 153 bytes :
https://gist.github.com/michidk/dce89c57c0837fb89c81211bad7fcb64
Save it as minimal.ld and enable -Clink-arg=-Wl,-T,minimal.ld in the rustflags array.
The script removes the 56-byte PT_GNU_STACK program-header entry and keeps the complete headers, code, and message together without overlapping them. This also drops explicit stack-permission metadata. No custom packer or post-link trimming needed!
What about Zig?
In Zig 0.17.0 , we can achieve something similar by setting a few custom parameters (see build-zig.sh ) and using the same linker script:
https://gist.github.com/michidk/743dc2b06fc3cdc95ab06604111f1a65
This version has no handwritten assembly and uses Zig's standard-library syscall wrappers. It results in 157 bytes and still exits with status 0 after a returned write error.
Why can't we apply the same tricks here? Those wrappers initialize their syscall registers explicitly. The compiler doesn't know that Linux supplies zero initial values for this particular entry point, and ordinary Zig code can't directly ask for mov al , mov dl , or those register exchanges. So this version stays at 157 bytes . The same tricks can't be transplanted into our Rust versions without handwritten assembly, either: their dynamic loader, startup code, and library calls don't preserve the kernel's initial register state.
But if we allow inline assembly ( hello-inline.zig ), we can use callconv(.naked) and apply all the same tricks! That gets Zig down to 153 bytes with our linker script, or 209 bytes with GNU ld's default script. Zig documents naked functions here .
The Rust and Zig assembly versions now use the same instruction sequence as our handwritten 64-bit version: 19 bytes of instructions , plus the 14-byte message and 120 bytes of ELF headers . All three reach 153 bytes , and all three still exit with status 0 after a returned write error. Nice!
You can find all the files and build instructions here .
# assembly
 # rust
 # zig
 # linux
 # optimization
 239 views
About the author
 M Michael Lohr
 Passionate about software development and architecture, web and cloud technologies, as well as game development.
Comments
 Join the discussion
 No comments yet. Be the first to comment.
More from this blog
 My Favorite IaC Tool Just Got Discontinued
 Why CDKTF was my favorite IaC tool
 Dec 23, 2025 · 10 min read · 507 views
The New Age of Web Development
 Less Code, Faster Iteration: AI and Smarter Tools Accelerate Productivity in Modern Web Development
 Sep 10, 2025 · 9 min read · 470 views
The Smallest Hello World Program
 Understanding how executable binaries actually work
 Dec 30, 2024 · 9 min read · 17K views
Talking To Your Mailserver Is Not as Hard as You Think!
 Learning how the IMAP protocol actually works
 Dec 22, 2024 · 7 min read · 21K views
Michi's Blog
 35 posts
Passionate about software development and architecture, web and cloud technologies, as well as game development.
Legal Notice | Privacy Statement
© 2026 Michi's Blog
 Archive
 Privacy
 Terms
 Sitemap
 RSS
 Powered by Hashnode

## 关联链接

- https://gist.github.com/michidk/0addb0fdcb7de291033027e742f44522
- https://gist.github.com/michidk/743dc2b06fc3cdc95ab06604111f1a65
- https://gist.github.com/michidk/86cd97a26c4fe05638340ba9bf8a485c
- https://gist.github.com/michidk/8af37f2f21a943522b35110857ae76d5
- https://gist.github.com/michidk/a2d048a126956ec4f6cf335f9782c37a
- https://gist.github.com/michidk/aaf08c7678e02b574973556d0fba741e
- https://gist.github.com/michidk/dce89c57c0837fb89c81211bad7fcb64

## 导航

- 项目页：[[10-项目/blog.lohr.dev_cc6b8e6d]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
