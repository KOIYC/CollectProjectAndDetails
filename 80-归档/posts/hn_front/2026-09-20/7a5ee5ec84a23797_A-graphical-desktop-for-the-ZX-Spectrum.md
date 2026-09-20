---
type: "corpus"
item_id: "7a5ee5ec84a23797"
title: "A graphical desktop for the ZX Spectrum"
source: "hn_front"
source_name: "HN 首页（非 Show HN）"
url: "https://news.ycombinator.com/item?id=49766676"
project_url: "https://github.com/mindbox77/zxdesk"
author: "graemep"
published_at: "2026-09-19T14:01:58Z"
captured_at: "2026-09-20T09:20:18+08:00"
lang: "en"
kind: "post"
tags:
  - 语料
  - hn_front
  - author_graemep
  - story_49766676
  - front_page
metrics: {"points": 113, "comments": 89, "engagement_velocity": 113}
comments_count: 89
comments_total: 89
discovered_via: "hn:front_page:2d"
archived: true
archived_at: "2026-09-20T09:21:31+08:00"
archive_reason: "渠道停用"
---

# A graphical desktop for the ZX Spectrum

- **来源**：HN 首页（非 Show HN）　|　**kind**：post
- **原帖**：https://news.ycombinator.com/item?id=49766676
- **指标**：点赞=113 · 评论=89 · engagement_velocity=113
- **作者**：graemep　|　**发布**：2026-09-19T14:01:58Z
- **项目链接**：https://github.com/mindbox77/zxdesk
- **采集**：2026-09-20T09:20:18+08:00　|　**id**：`7a5ee5ec84a23797`

## 正文

# mindbox77/zxdesk

A GUI operating system for the 48K ZX Spectrum, in Z80 assembly

- Stars: 61
- Forks: 2
- Watchers: 61
- Open issues: 0
- License: MIT License
- Default branch: main
- Created: 2026-09-16T21:30:13Z

## Languages

- Assembly
- Python
- Shell

## Top Contributors

- mindbox77 (1 contributions)

---

## README

# ZX Desk

A graphical desktop for the ZX Spectrum 48K, written in Z80 assembly.

Overlapping windows with a z order and focus, pull down menus, a heap,
an event queue, a storage layer with swappable backends, dialogues,
controls, a notepad, a clock, a calendar, a two pane file manager, and
a settings panel that actually changes things. It all fits in 48K on a
machine from 1982, and it can drag a window inside a single 69,888 T
state frame.

It runs on the real thing, not just an emulator.

The desktop

---

## Why

Back in the eighties I wanted an Atari ST and couldn't afford one.
What I really wanted was
GEM: the
desktop, the windows, the menu bar that was always there, the feeling
that the machine was a place rather than a prompt. I had a Spectrum
instead, and I spent a long time wondering how much of that you could
do on it. I started writing bits of it, and never finished.

So this is that, finished. It isn't a port of GEM and doesn't pretend
to be. It's what the idea turns into when you push it up against a
3.5 MHz Z80, 48K of RAM, a one bit display with attribute clash, and a
video chip that steals cycles from the CPU while it paints. A lot of
the answers turned out to be more interesting than the question, and
nearly all of them came from measuring the machine rather than
reasoning about it.

It's a fun project and a labour of love, and the reason it's written
up at this length is that the measurements are the useful bit. If
you're building something on this hardware, the numbers below cost me
a lot of evenings. They're yours.

---

## What it does today

| | |
|---|---|
| **Windows** | Overlapping, z ordered, movable, resizable, with title bar, close box and grip. Focus is the front of the z order, so raising and focusing are one action. |
| **Menus** | A permanent menu bar with pull downs, save under, and hit testing. |
| **Input** | Kempston mouse, Kempston joystick, and the full keyboard matrix decoded across three tables with repeat. All of it arrives as events. |
| **Events** | A sixteen slot ring. The main loop contains no window specific code. |
| **Storage** | A registry of backends behind six vectors. RAM, tape (via the real ROM loader), and the 128K's spare banks as a RAM disk. esxDOS has a reserved id. |
| **Memory** | A real heap with an owner byte, 8,112 bytes, allocating window buffers sized to their windows. |
| **Applications** | A descriptor with init, event and paint, plus per instance state swapped in and out. Notepad, clock, calendar, commander, about. |
| **Persistence** | Settings written to storage with a magic byte and a version, and read back at boot. |

Screenshots:

| | |
|---|---|
| Two windows | Notepad |
| Two windows, z ordered | The notepad, with the Sinclair style shift-reporting cursor |
| Commander | Clock and calendar |
| Two pane commander, over devices rather than directories | Clock and calendar |

---

## Running it

The toolchain is local and small: pasmo
0.5.5, built from source into `tools/`.

 ./build.sh assemble src/zxdesk.asm to build/zxdesk.tap
 ./run.sh build and load onto the machine
 MACHINE=128 ./run.sh the same on a 128K, and put the setting back

esxDOS runs here too, on an emulated DivMMC with a 64MB card image.
`tools/` isn't in the repository because pasmo, the emulators and the
esxDOS ROM aren't mine to redistribute, so you'll need to build the
image yourself from an esxDOS release and a DivMMC card image. Once
it exists, launch `tools/esxdos/esxdos.szx` and esxDOS is already
resident; `Machine > NMI` gets you its file browser.

Build flags, all passed through `--equ`:

 DEMO=1 ./build.sh a self dragging build, for reproducible captures
 NOWAIT=1 with DEMO, the same drag with no beam scheduler
 SCRIPT=1 ./build.sh drive the desktop from synthetic input
 MOUSETEST=1 ./build.sh the raw Kempston mouse diagnostic

`build.sh` must pass `--name` explicitly, because pasmo takes the tape
header name from the output path exactly as written and would
otherwise put `build/zxde` in the header. It also refuses to build a
tape if the code has grown into the buffer region, because that overrun
is silent otherwise: the first window grab writes over the program and
a few seconds later the machine drops into BASIC with an unrelated
error.

**Dragging a window under Fuse needs the space bar, not the mouse
button.** Fuse for macOS, 1.9.2, stops delivering Kempston mouse
movement while a button is held, so the pointer freezes at the moment a
drag begins and the window never follows. Point at the title bar, hold
SPACE, move, release. The mouse is fine for everything else and the
buttons themselves register correctly; it is only movement that stops.

This is the emulator, not the desktop, and `MOUSETEST=1` is how I
proved it: it reads the mouse ports once each with nothing between the
port and the screen, and the counters still stand still while a button
is down. `RiBtn` in `ReadInput` is what makes SPACE work, and it's
there so the desktop is usable on a machine with no mouse at all. A
real Kempston mouse drags normally.

`SCRIPT=1` is the one worth knowing about. It drives the desktop from a
list of synthetic input events instead of the mouse, so an interaction
(open a menu, pick an item, drag the window over another one, type
into the field, save) runs the same way every time and can be compared
against the last run rather than watched.

---

## How it is built

From the bottom up.

**Device layer.** `DevFillRect`, `DevFillDesk`, `DeskFillCol`,
`AddrAt`, `BlitRect`, `RectGrab`. Everything above works in byte
columns and pixel rows and never touches the screen's third and
interleave layout directly. This is the boundary a port swaps out, and
I drew it on day one for exactly that reason.

**Frame discipline.** The main loop halts on the interrupt, does all
pointer work in the top border, waits for the beam if the window
moved, redraws, then reads input and dispatches at the end of the
frame. Input goes last so that the cost before the beam wait is
constant, which is what makes the scheduler exact.

**Event queue.** A sixteen slot ring of four byte events. `EvPoll`
turns raw input into pointer moves, button presses and keys; `EvDispatch`
drains it through a handler table.

**Hit testing.** A five byte row per control, front to back in z
order, `$FF` terminated, refilled from the model before every search so
there is no second copy of the window position to go stale. A closed
menu gets a height of zero, which can never match, so `HitTest` has no
special case for it.

**Transient surfaces.** A four deep arena, each surface up to 16 by 96,
pushed and popped. Two stacks rather than one, because the pixels under
a menu are pushed by something that has no panel record at all.

**Windows.** A record swapped into a live copy, the same trick as the
panel record, because the window position is referenced ninety three
times across six files. The z order is also the paint order reversed
and the hit test order.

**Storage.** A registry of backends, each a fourteen byte row of id,
capability bits and six entry points. The six operations are hand laid
`JP` instructions whose operands are patched on selection, so dispatch
costs ten T states and clobbers no registers.

**Controls.** A panel is a stack of rows and every control is a row, so
a row's index is three shifts rather than a search. Four types, of
which the useful one is a cycle: a checkbox is a cycle whose limit is
two, and a radio group is a cycle whose limit is N. The settings panel,
the file list and the save box are all the same code with different
tables.

### The memory map

 $6000-$727C the slow region: panels, the calendar, the file
 panels, the desktop setup, the commander
 $727D-$7FFF free, 3,460 bytes, contended
 $8000-$B1B7 the fast region: everything else
 $B1B8-$BCFF free, 2,889 bytes
 $BD00 stack top
 $BDBD interrupt handler
 $BE00-$BEFF interrupt vector table
 $C000-$C63F the RAM disk, its directory, and the tape buffer
 $C640-$C74F the live notepad state
 $C750-$DF4F four transient surfaces
 $DF50-$FEFF the heap, 8,112 bytes
 $FF00-$FFFF deliberately unused

Two things in that map are worth explaining.

The slow region exists because the ULA steals cycles below `$8000`
while the display is being painted, so code there runs perhaps a third
slower. The rule for it is one line: nothing in it may run inside a
frame. Nothing there is on the drag path, the pointer path or in the
interrupt, and the timings were unchanged to the T state across
the move. It starts at `$6000` rather than at the top of the system
variables because the tape loader indexes the system variable area
through IY and the BASIC loader itself lives just above it, and a CODE
block that overwrote the program doing the loading would be a novel way
to fail.

The heap stops a page short of the top of memory rather than at
`$FFFF`. Every walk computes the next block as address plus header plus
size, and a block ending at `$10000` would wrap to nought and compare
as below the base of the heap. Stopping at `$FF00` costs 256 bytes of
8,272 and removes the entire class of failure.

---

## What was measured

This is the part I'd want if I were reading someone else's repo.
Every figure below was measured by running the code and timing it
against the machine's own clock. None of it comes from counting
instructions, and the few claims that are derived say so.

Timings, on the machine

### The clock you can trust

The 48K interrupt period is exactly 69,888 T states and nothing a
program does can move it, so it is the only usable clock on the
machine. So a timing run syncs on `HALT`, optionally delays a known
number of T states to place the routine at a chosen point in the frame,
calls it, then counts turns of a sixteen T loop until the next
interrupt. Comparing against an empty calibration run cancels every
fixed overhead:

 cost = (K - K0) * (69888 - 118) - 16 * (C - C0) - delay

118 T is the exact cost of the returning interrupt path, counted
instruction by instruction. It is exact rather than estimated because
the handler, its variables, the counting loop and the stack all live
above `$8000`, where the ULA never steals a cycle. Only the routine
being timed touches contended memory.

Measured blind against three delays of known length:

| nominal | measured | error |
|---|---|---|
| 2,599 T | 2,592 T | −7 T |
| 51,999 T | 52,000 T | +1 T |
| 103,999 T | 103,994 T | −5 T |

Worst error is 7 T in 104,000, or 0.007%. The third crosses a frame
boundary, which is what confirms the 118 T figure.

### Contention costs 14.7%, not 50%

Every budget in the project started from a pessimistic 50% penalty on
screen writes, taken from the folklore. Sweeping a 1,024 byte fill
across the frame:

| start | cost |
|---|---|
| top border | 11,744 T |
| 10,399 T | 12,913 T |
| 20,799 T | 13,441 T |
| 31,199 T | 13,473 T |
| 41,599 T | 13,441 T |
| 51,999 T | 12,369 T |
| bottom border | 11,745 T |

The two border figures agree to 1 T, which is the uncontended cost. The
worst case inside the display is 13,473 T. That is 14.7%, or about
1.7 T per contended byte written. Budgets built on the 50% figure are
roughly a third too conservative, and mine were.

### Half the cost of drawing a window is three short strings

`WinDraw` split into its four phases and each timed separately. The
phases sum to within 330 T of the whole, which is the four call and
return pairs plus the sixteen T counting granularity.

| phase | top of frame | mid display | share |
|---|---|---|---|
| text | 35,872 T | 35,969 T | 50% |
| edges | 19,552 T | 19,841 T | 27% |
| fills | 14,688 T | 16,641 T | 21% |
| close box | 832 T | 849 T | 1% |
| **whole** | **71,274 T** | **73,099 T** | |

Twenty seven characters of title and body text, at roughly 1,330 T
each. The fills, which I had assumed were the problem, are a fifth of
it. Optimising the fill would have bought a few per cent of a drag
frame and I'd have spent a week on it.

### A benchmark that measured the wrong thing

An earlier note recorded the cell aware push fill at 7.4 T per byte.
The real routine costs 11.5 T per byte, 54% more. The benchmark had
measured the technique; the routine carries per row address arithmetic
the benchmark never paid. Of the 183 T a row costs, 88 T is the push
chain actually writing pixels and 95 T is the register exchange, the
address step, the cell boundary test and the loop.

Over half the cost of the fastest fill on the machine is not writing
pixels. That generalises: on this processor, per row overhead is the
thing to attack, not per byte throughput.

### Interrupts are lost, not deferred

This is the one I'd most like other people on this hardware to know
about, because it produces a fault that looks like anything except its
cause.

The fills held `DI` for their whole run, because SP walks through
screen memory and stops being a stack. The received wisdom is that this
delays the interrupt. It does not. The Spectrum asserts INT for only
32 T states and then withdraws it, so a `DI` window that covers those
32 T destroys the interrupt rather than postponing it.

It was observed before it was understood. A fill placed at 62,399 T
into the frame reported crossing no frame boundary when it plainly
crossed one. Rescoring it as a lost interrupt gives 11,745 T against
11,744 T for the same fill in the top border, and the two agreeing to
1 T is what confirmed the diagnosis.

Then it was measured properly. With an interrupt injected after every
single instruction of an 8 by 24 fill, the interrupt was refused at 458
of 500 instruction boundaries in one fill routine and 710 of 752 in the
other.

**The obvious fix does not work.** Re-enabling interrupts between rows
sounds right and fails, because the interrupt is not pending, it is
gone. An `EI` window a few T states wide, once every 236 T, catches it
about one row in thirty. Making the `DI` region short is not the same
as making it absent, and only absent is a fix.

**What works is owing the last push.** The fills now run with
interrupts enabled throughout. What `DI` was protecting was SP, so the
fix is to guarantee that the two bytes of return address always land
somewhere that is about to be overwritten anyway. SP takes two kinds of
value: inside the rectangle, where a push writes exactly what the
chain's next push will write, and the low point after the last push of
a row, which the chain never returns to. So the chain is made one push
shorter than the row, and the leftmost two bytes are **owed** — paid one
iteration later, once SP has moved into the next row and can no longer
reach them.

Afterwards: 0 of 607 and 0 of 904 instruction boundaries destroy the
interrupt, the rectangle is byte for byte identical every time, nothing
outside it is touched, and the screen checksums are unchanged
either side of the change.

| | before | after | |
|---|---|---|---|
| 16×96 rectangle fill | 17,414 T | 22,068 T | +48 T a row |
| 16×96 desktop fill | 25,351 T | 30,125 T | +50 T a row |

That's a real cost, and it's worth it. The drag path is mostly the
column fill, which writes through HL, never touched SP and was never at
risk.

### The watchdog that was caught by the thing it was built to catch

A frame watchdog counts interrupts in the handler and frames in the
main loop; the difference is frames dropped. The handler is the awkward
half, because it fires inside a fill where the stack is not a stack.

The first version borrowed IX and counted with `INC (IX+0)`, and the
interrupt sweep above failed on its first run. That instruction sets
the flags, and a fill holds a live carry across the address step that
finds the end of a row and the branch that decides whether the row
crossed a boundary. An interrupt in that gap stole the carry and the
row stepped to the wrong address.

`INC IX` is a sixteen bit increment and sixteen bit increments leave
the flags alone. So the counter is a word, the handler is transparent,
and it costs 104 T fifty times a second with not one flag or register
altered. The roadmap had predicted that a watchdog would have caught
the interrupt bug earlier. What actually happened is that the interrupt
test caught the watchdog.

**Letting the handler push is also a dead end.** A handler that pushes
AF uses four bytes below SP rather than two, so the owed region has to
double and every row pays another 22 T.

### Getting a drag inside one frame

The starting position was hopeless: a full erase and redraw of a window
cost 96,010 T against a frame of 69,888 T. That is 137% of a frame, and
it is why dragging ran at 25 Hz. Four changes, in order, each measured:

| change | effect |
|---|---|
| **Off screen buffer.** Compose once into a buffer, blit per frame. The expensive work is composition, not transfer. | redraw 71,274 T → 26,048 T |
| **Faster text.** Rewriting the pixel text renderer. | 1,307 T → 622 T a character, 2.10× |
| **Damage rectangles.** Erase only the strip the window has vacated, not the whole window. | erase 19,664 T → 1,456 T |
| **A narrow desktop fill.** Two bytes straight through HL with the pattern held in registers, unrolled four ways so no row works out its phase. | single column strip 14,256 T → 5,712 T |
| **Chasing the beam** rather than waiting for it to clear the whole window. | a further 16,128 T |

A drag frame now ends at **59,858 T**, inside the frame, and dragging
runs at 50 Hz.

The beam scheduler counts scan lines rather than T states, because one
line is exactly 224 T and the top border is exactly 64 lines, so the
target is an eight bit addition rather than a division. It measured
36,576 T for 163 lines against 36,353 T counted by hand.

The text rewrite is worth a note because measuring it proved both of
my guesses wrong. The address routine was called once per character, not
once per pixel row, and crossing a cell boundary cost nothing. The real
costs were 232 T re-testing an inversion flag on every pixel row, 344 T
on eight calls to a row stepping routine, and 126 T recomputing an
address that was one byte to the right of the previous one. The
replacement makes the inversion a self modified `XOR` operand set once
per string, walks one address across the whole string, and splits the
eight pixel rows either side of the single cell boundary they can
cross.

**Damage aware blitting does not follow.** When a window moves
vertically every row still has to be written, because the pixels
underneath are the same window at the wrong offset. Damage shrinks the
erase only. A per row signature built at grab time would let uniform
interiors be skipped, worth perhaps 9,700 T on this window, but it only
pays for windows with large flat areas. Held in reserve rather than
rejected.

**The stack based blit does not follow either.** Popping eight register
pairs from the buffer and pushing them to the screen costs about 212 T
a row against `LDI`'s 256, but the pointer bookkeeping needs `LD (nn),SP`
and a reload each row, which puts it back at roughly 304 T against the
current 327. It also needs `DI`, which reintroduces the lost interrupt
hazard, and running it with interrupts on via the owed push technique
costs 48 T a row, which makes the arithmetic worse rather than better.

### The interrupt is not 50 Hz

The 48K frame is exactly 69,888 T at 3.5 MHz, so the rate is 50.0801 Hz.
Ticking a second every fifty interrupts gains 0.16%, which is two
minutes eighteen seconds a day. The clock instead makes a second fifty
interrupts and, every so often, fifty one, decided by accumulating a
hundredth each second and demanding an extra interrupt when it carries.
Driven for an hour it takes 180,287 interrupts against a true
180,288, which is half a second a day.

On a 128K the frame is 70,908 T at 3.5469 MHz, so the rate is 50.0211 Hz
and the addend differs. Machine detection has already run by the time
the clock initialises.

What the clock counts is the interrupt counter that the watchdog built
to notice dropped frames, read as a difference since the last look, so
a frame the main loop missed still advances the time — because the
interrupt happened whether or not anything was listening.

### A calendar with no division

Day of the week is counted forward from 1 January 1980, a Tuesday,
rather than by Zeller
or Sakamoto,
because both of those want division
by 4, 100 and 400 and this machine has no divide instruction. A year is
1 modulo 7, or 2 in a leap year, so walking a century is at most a
hundred additions, and it happens once per repaint.

The century rule never fires, and that is a property of the range
rather than a corner being cut: 1980 to 2079 contains one century year
and 2000 is a leap year, so within that range a leap year is exactly a
year divisible by four. All 1,200 months it can display are checked
against Python's `datetime` for both the first weekday and the length.

---

## Bugs worth writing down

Every real discovery in this project came from running code, not from
reading it. These are the ones that generalise.

**A bug that repaired itself in front of me.** The heap's free routine
had one `DEC HL` too many, so it cleared the used flag and then wrote a
nought into the high byte of the block's size. The heap should have
been ruined on the first free. It was not, because the coalescer then
found a short free block, looked past it into a payload that happened
to be all zeros, read those zeros as an empty free block, and absorbed
them four bytes at a time until it arrived back at exactly the true
total. Every number agreed. It only surfaced when a freed block held
something other than zeros — the first block big enough to have held
window pixels — and then the walk went into the pixels and the heap
came back 2,619 bytes short.

The lesson is about the test rather than the allocator. A heap test
that frees blocks it never wrote to is testing a zero fill. It writes
`$A5` over the payload before freeing now, and asserts on the header
directly rather than through a total that can heal.

**The register that carries the answer must not be the register that
carries the argument.** This family accounted for five separate bugs.
A search routine held its index in `AF` across the compare that decided
whether it had found anything, so the `POP AF` restored the flags from
before the compare and it never matched. A digit printer used B to
count tens and was called twice with the other digit in B, so the
calendar's year came out as 2050. Two routines ending in `LDIR` return
with A clobbered and BC zero, which produced a second window that was
an exact copy of the first and a panel whose row count was nought.
Loading a `DJNZ` counter before calling a routine that uses B as a row
counter makes the loop run 256 times, which has now happened twice.

On the Z80 the flags are a register too. If a value must survive a
call, it goes in memory or on the stack. That rule is not learnable as
"watch out for B".

**A row step that subtracts only from E.** The blit did this from the
day it was written. The `LDI`s advance DE sixteen bits, so when a
rectangle's row start plus its width crosses 256, D has already been
incremented and incrementing it again puts the next row a page too
high. The only window in the system lived at column 8 and was eight
bytes short of crossing, so it never showed until a second window moved
to column 16. Anything walking a rectangle a row at a time has to
handle the borrow.

**A number that reads backwards.** Timings are taken by counting a
sixteen T loop until the next interrupt, so a slower routine leaves
*fewer* turns. That was misread twice in one session, once reporting a
16 T saving as a 1 T loss, and once reporting a 1,216 T cost as a 76 T
saving — which meant a real regression went unnoticed for being
displayed as an improvement. Anything that reports a derived quantity
should report it in the units people will reason in.

**A corrupt block size hangs the machine rather than failing.** Every
heap walk computes the next block as address plus header plus size, and
a garbage size wraps past `$FFFF`, lands below the base and compares as
still inside the heap, so the walk loops forever. Nothing can produce a
garbage size now, so no guard was added, but it is the shape of the
next failure and it is worth knowing it presents as a freeze.

**Earlier, and in the same spirit:** an LFSR shifting the wrong
direction gave a period of 71 instead of 65,535; a register clobber
rendered the wrong card in the patience game that was this project's
proving ground; a raster timing bug made the pointer invisible in the
upper half of the display on real hardware but not in the emulator; and
a sign bit underflow teleported windows to the top of the screen the
moment Y exceeded 127.

---

## How the work was done

Every piece of work went through the same three passes, in one
sitting.

1. **Research.** Find the prior art before writing anything. The
 Spectrum demoscene, the ULA and floating bus documentation, the
 esxDOS API notes, the Next register list. Half of these problems
 were solved by somebody in 1987, and the demoscene answer is usually
 faster than the textbook one.
2. **Build.** The smallest thing that can be measured, with the way to
 measure it committed alongside the routine.
3. **Critique.** Argue against the result before accepting it. Look for
 the clobbered register, the boundary case at the screen edge, and
 the figure from a previous session that's no longer true.

I tried to play three parts in every session: the critic who argues
the change is wrong, the researcher who goes looking for the 1987
answer, and the measurer who won't accept a performance claim without
a timing or a correctness claim without a screen checksum.

Three rules that earned their place:

- **It isn't done because it looks right on screen.** The pointer that
 vanished in the upper half of the display looked right on screen.
- **Anything that couldn't be observed directly is labelled derived,
 not measured.** Raster behaviour especially, which is why every
 raster derived claim in this repository says so. That distinction is
 what eventually explained the invisible pointer.
- **One commit per verified piece of work, with the acceptance numbers
 in the commit message.** The numbers in this document are the ones
 from those commits.

---

## What is not finished

**esxDOS is written and passes.** For a long time it couldn't be,
because I had no DivMMC and I don't commit code I haven't run. An
emulated DivMMC with esxDOS resident unblocked it in September 2026,
after three dead ends.

**The Next didn't turn into a port.** It became its own system, in its
own repository, because the window model is different: it tiles rather
than overlaps, so the compositor, the save under arena and most of the
damage machinery have nothing to do there. Everything below the window
model carried across. It isn't published yet.

**Known gaps.** A clock behind another window holds its last time
until it's raised, because window buffers are grabbed from the screen
rather than composed into. An application can't refuse to close,
because there's no teardown vector that can say no, and adding one
before anything needed it would have been guessing. Every notepad is
titled from its application rather than its document. The notepad has
no selection, clipboard, undo or word wrap. Mouse presence detection
is still a heuristic, and I can't test it because I don't have a
machine without a mouse.

**No known live bugs.** The last one closed with the interrupt safe
fills and nothing since has opened another.

---

## The ZX Spectrum Next

The 48K system was built with a port in mind from the first commit,
and the bet was that the device layer boundary would hold. It held for
storage, esxDOS, the application model and the settings record. It
didn't hold for the window model, which is why ZX Desk Next is a second
system rather than a port: on a 28 MHz Z80 with Layer 2, a tilemap,
hardware sprites and a DMA, the right desktop tiles, and a tiling
desktop has no use for a compositor built to sort out overlap.

It lives in its own repository and will be published separately. I
don't have a Next yet, only 48K and 128K machines, and I'm not going to
build it blind on an emulator, so it waits until one arrives.

---

## Repository layout

 build.sh, run.sh assemble, and load onto the machine
 tstates.py, taplant.py timing arithmetic, and tape block planting

 src/zxdesk.asm the desktop
 src/damage.inc damage rectangles and the narrow desktop fill
 src/saveunder.inc transient surfaces
 src/events.inc the event ring and dispatch
 src/kbd.inc the keyboard matrix and decode
 src/hittest.inc the region table, z order, what was hit
 src/menus.inc the menu bar and pull downs
 src/panel.inc panels and their rows
 src/dialog.inc the alert and the confirm
 src/storage.inc the storage layer and the RAM backend
 src/tape.inc the tape backend, via the real ROM loader
 src/bank.inc the 128K's spare banks as a RAM disk
 src/heap.inc the heap and its owner byte
 src/app.inc application descriptors and the state swap
 src/resize.inc the grip, the outline drag, the realloc
 src/note.inc the notepad
 src/clock.inc the clock
 src/calendar.inc the calendar
 src/commander.inc the two pane file manager
 src/desktop.inc desktop shortcuts
 src/filemgr.inc the file panels
 src/settings.inc the settings record
 src/script.inc scripted input, for end to end verification
 images/ the screenshots above

---

## Thanks

To Fuse and to César
Hernández Baño's ZEsarUX,
which are how this was developed before it ever ran on the real thing.
To Julián Albo's pasmo, which is small and
does exactly what it says.
To the Spectrum community, whose thirty years of documentation about
contention, the floating bus and the ROM entry points is the reason
this took months rather than years. And to whoever wrote the ULA timing
notes I kept going back to: your figures were right and my assumptions
were not.

To Inkbox's NES-OS, which is the
proof that this kind of thing is worth doing.

And to a machine that was never meant to do any of this, and does.

---

## Licence

MIT, see `LICENSE`. Nothing here is derived from anyone else's code.
The toolchain, emulators and ROMs it uses aren't distributed with it.


# What Zig felt like, coming from Rust | besok

## 评论（89/89）

**j4cobgarby** · 2026-09-19T14:27:24.000Z：

It _does_ look really cool, genuinely, but calling it a "labour of love" and then having AI write the readme/docs seems conflicting.

**Andrew2565** · 2026-09-19T15:13:59.000Z：

Can anyone suggest a simple high-level graphical desktop (perhaps written in a mix of assembly and C) that comes with good documentation, or even an associated textbook?

**jameshart** · 2026-09-19T15:32:26.000Z：

It’s Claude’s earnestness that’s so disingenuous in this kind of write up. This voice Claude has where it believes the work is important and deserves to be taken seriously, and where it takes ever part of the process where it has to adjust its approach because of a thing it figured out as a great insight which is incredibly valuable and that people should be made aware of…I feel like vibecoded projects need Claude to pick up on a sense of ‘this is just me messing around’, and a project like this where there does appear to be genuine digging into the art of performance tuning Z80 assembly needs Claude to understand ‘this is impractical hacking for hacking’s sake not groundbreaking research’I don’t have a problem with projects which are, essentially ‘Claude and I burned a lot of tokens for giggles to see just how far you can push something’. But the write up needs to reflect that spirit.

**vilaca** · 2026-09-19T15:43:25.000Z：

Wow I did so many of those when i was 12 or around that age. Mostly I tried copying the Amiga Workbench on my +2A (the gray one).Obviously at that age my knowledge of coding and window managers wasn't exactly deep and i mostly only had seen other OS from magazines. I don't think I even knew what 'drag-n-drop' was and was a bit confused at what the Trash bin should do (i loaded code from tapes).Good times i guess :)

**NinjaTrance** · 2026-09-19T15:48:40.000Z：

AI slop.

**shevy-java** · 2026-09-19T15:50:42.000Z：

Assembly seems overkill though.

**kalleboo** · 2026-09-19T16:15:43.000Z：

> Three rules that earned their place:> One commit per verified piece of work, with the acceptance numbers in the commit messageProject: One single commit: "ZX Desk, first release"???

**pmg101** · 2026-09-19T16:55:31.000Z：

I had fun playing around in Claude getting it to write 6502 assembler for the BBC Micro. It is fun to imagine what we could have built on those old machines with these new coding agents! But it is kind of hollow isn't it.

**jakzurr** · 2026-09-19T17:02:29.000Z：

Sure are cute little pieces of history:https://duckduckgo.com/?q=zx+spectrum&ia=images&iax=images

**alt227** · 2026-09-19T17:20:13.000Z：

I hate the fact there is more discussion on things on HN about whether or not its vibe coded than the actual merits of the project itself. I really dont understand peoples attitude of immediately turning off something once they know ai is involved. These people are going to become pretty conflicted when somebody finally vibe codes some software they really like or have wanted forever.As far as this project goes, the spectrum was the computer of my youth, and seeing this and getting to mess around with it brings my heart joy and my mind lots of nostalgic thoughts. Thanks for sharing!

**unnah** · 2026-09-19T17:34:50.000Z：

Related: The SymbOS operating system and graphical desktop for Amstrad CPC, MSX and some other Z80 machines was coded entirely manually - the first release was in 2006. https://www.symbos.org/Of course for the Commodore 64 the GEOS desktop was already released as a commercial product in 1986. https://en.wikipedia.org/wiki/GEOS_(8-bit_operating_system)

**veltas** · 2026-09-19T17:38:43.000Z：

This is the sort of thing I've wanted to write for a long time. Yes it looks like this is vibe coded but I'm glad this was made because it's cool to see what can be done, and it's interesting seeing how AI can be used as a compiler essentially given the output is assembly.I'd be interested if the author would tell us more about what they did here and what went into the design and evolution, rather than the AI README.

**beeforpork** · 2026-09-19T18:47:57.000Z：

Written in the best programming language ever!

**noir_lord** · 2026-09-19T14:29:12.000Z：

I'm at the point as soon as I think "was this written with AI help?" is in doubt I immediately hit the back button.Have been for a while, it's exhausting.> The clock you can trust*Bleh*

**in_absentia** · 2026-09-19T14:39:16.000Z：

Long-form comments in the code are AI-written too, so I assume the whole thing is vibecoded. I guess my question is why. This is obviously not a piece of software anyone will ever use. If the author didn't do this for themselves - to learn, to show off their skills - then why bring it to life?In business, there's this saying that "when a metric becomes a target, it ceases to be a good metric". I guess LLMs also make that true for hobby projects that used to make up a good portion of HN. We'd celebrate a project like that not because it's useful, but because it's a triumph of human ingenuity and a celebration of a personal achievement for the author. But now, it isn't, so is it still something we ought to celebrate?

**api** · 2026-09-19T14:47:44.000Z：

I wonder: was there a time when using a compiler was considered cheating? "Real men" code everything in ASM!I do recall a whole era when using a GUI was considered cheating and denigrated as a "point and drool" interface (a play on "point and click").Is using a combine cheating in farming? Is a nail gun or using prefab wall sections cheating in home construction? Is a 3D printer cheating in fabrication? If someone prints something with a 3D printer, do we say "you didn't make that, the printer did!"I find it weird for people who like technology to be so averse to tools that automate labor since that is literally what all technology is, and a tool to automate intellectual labor is literally what a computer is. A machine is a thing whose purpose is to provide leverage to amplify human effort and more rapidly realize human intent in some domain.Maybe it comes from a category error. AI is kind of a hand-wavey term, since most people think it means the thing is sentient. It's not. It has zero intent, zero motivation, zero ability to choose anything not already in its training data, and it will go precisely where its context window (and training data) guide it. It's a tool, a machine, and like any other machine it is set in motion by the user and guided by the user. The "choices" it makes are latent in its data or structure, or implied by its prompt. (Yes sometimes they can be surprising, but that's true of all complex machines.)Actual sentient AI does not exist. It might someday but it does not today. I suspect it requires a very different kind of system with continuous learning, dynamical state, and feedback, and a goal function tied somehow to thermodynamics in the real physical world the way ours is, but that's pure hypothesis on my part. We don't even have rigorous definitions for such things.

**tahoemph999** · 2026-09-19T14:59:03.000Z：

Thinking of and expressing the functionality of the thing might be the labor of love for this person. Their definition of labor doesn't have to be yours.

**ghusto** · 2026-09-19T15:18:27.000Z：

Why do you say it's written by AI?

**progbits** · 2026-09-19T17:01:15.000Z：

> Licence
>
> MIT, see LICENSE. Nothing here is derived from anyone else's code.Right... Except the whole thing being generated by a model derived from everyone's code.I'm not even sure I'm against licensing it as MIT but maybe stop with the ridiculous claims on top of that?

**calvinmorrison** · 2026-09-19T15:53:24.000Z：

rio?and there's a detailed write uphttps://aryx.github.io/assets/pdfs/Windows-7.pdf

**calvinmorrison** · 2026-09-19T15:32:48.000Z：

> It runs on the real thing, not just an emulator.Wow!!!!

**zekodun** · 2026-09-19T15:42:36.000Z：

agreed, the only issue here is that Claude is targeted to enterprise engineering teams so its language model is trained for SoCal startup culture.Would take three times the token cost to actually get it to fight with itself in the correct voice tone.Honestly think self hosted models is more valuable here. At least then one can train it with the right system prompt.

**orangecat** · 2026-09-19T16:40:37.000Z：

That's an excellent way of putting it. It's like an enthusiastic student who points out all the really smart stuff it did so that the teacher will be impressed and give it a gold star...which is basically what its RL environments were.

**Sharlin** · 2026-09-19T18:38:17.000Z：

I have called it Claude's "iamverysmart" voice, but as you said, maybe it's more of a "thisisveryimportant" voice.

**badsectoracula** · 2026-09-19T18:53:03.000Z：

TBH even if you're messing around you may still want the code to be performant and taken seriously :-P

**gizajob** · 2026-09-19T16:00:55.000Z：

Laughable to ignore the actual work done and that had to be done by a human to make this happen and work, and only focus on the AI assistance.

**dainiusse** · 2026-09-19T16:01:45.000Z：

I don't understand the negativity. Someone had great time. Why being so negative. Of course no one would have invested time, if not llm's - that wouldn't even exist.

**snvzz** · 2026-09-19T18:03:12.000Z：

Cannot put the genie back in the bottle.

**djmips** · 2026-09-19T16:07:30.000Z：

For an 8 bit Z80 based hardware project like this, assembly is a valid choice. The reason is performance. You'll lose significant performance with a compiler or interpreter.

**flohofwoe** · 2026-09-19T16:22:34.000Z：

There is practically no other choice on a Z80. C compilers really don't like the Z80 ISA and create both slow and bloated output, at least compared to manually written asm. And on top, you can do many optimization tricks in assembly that simply are not possible in a high level language (self-modifying code, jumping into the middle of an instruction, etc...).Forth might work better than C, but tbh, assembly code is more straightforward and easier to read than Forth ;)

**MobiusHorizons** · 2026-09-19T17:41:59.000Z：

I believe most of the 8bit microcontrollers from this era have no good optimizing compilers that get close to what competent practitioners achieve with assembly. I think it has to do with having complex addressing modes making the C stack fairly inefficient.

**varjag** · 2026-09-19T18:56:55.000Z：

The quickest way to redraw a screen or otherwise copy a memory region on Spectrum of is to use POP/PUSH instructions while flipping the stack pointer. Good luck getting that with C.

**Marazan** · 2026-09-19T19:04:44.000Z：

assembly is the only choice. The Z80 processor is a twisty collection of registers, none alike. It is pretty much the opposite of what a, for example, C compiler is looking for.In fact C compilers are _notoriously_ bad at producing code for the Z80.

**flohofwoe** · 2026-09-19T16:27:53.000Z：

Maybe Claude one-shotted the project ;)

**throwaway_side_** · 2026-09-19T17:27:43.000Z：

maybe they have a day job in a jurisdiction where their employer could claim ownership of the code if work was done during hours they paid for. it would be safer to scrub commit times if you’re worried about an aggressive employer.

**reaperducer** · 2026-09-19T17:01:06.000Z：

It is fun to imagine what we could have built on those old machines with these new coding agents! But it is kind of hollow isn't it.It's the difference between building a table yourself and telling someone else to build a table for you.If you've never done anything for yourself, usually with your own hands, you don't understand the pleasure and satisfaction that comes from doing it.And since "AI" isn't human, it can't know that feeling, either.

**leidenfrost** · 2026-09-19T17:25:14.000Z：

Not for me. I do like having an agent at my disposition that accelerates the way into making those little experiments a reality.
A sloppy reality? Maybe. But It's just tinkering, there's no other use case for this outside of saying "So this can be done, huh? Okay time to go to for a walk".While it's totally respectable to treat your code as your personal zen garden, I like the idea of having a highway where I can make reality anything that comes from my imagination, and also having time for family, friends, work and exercising out of sedentarism.

**vinc** · 2026-09-19T18:07:23.000Z：

I think it's an issue for hobby projects. The other day I had a neat idea, looked into it and realized I would not have time to do it but still wanted to use it so I vibe coded it over an evening and there it was. But the code is not mine, I feel bad about it, it's completely hollow, I wish I had the time to do it properly. I'm glad I'm still hand coding my main hobby projects to avoid that.

**Narishma** · 2026-09-19T19:33:29.000Z：

Claude?

**gizajob** · 2026-09-19T15:55:20.000Z：

No, I think it’s cool AF. Is it work that needed to be done? Certainly not. Is it work that could have been done by humans? Yeah maybe with a year or two of free time. AI gives us these admittedly pretty useless capabilities but it’s still fun to do, to get a new advanced tool to make us a kind of hauntological version of something that could have existed. You sound like the fun police and someone who should stick to programming in raw, unadulterated machine code rather than using any kind of assistance.

**shevy-java** · 2026-09-19T15:52:48.000Z：

> why bring it to life?I think all AI projects should die, but if your question is aimed as to "why to publish it on github", then why not? Others could look at the code and learn from it (perhaps); and it is easier to distribute it that way too, in many cases. So I don't fully agree with the assumption that it would be automatically useless. Personally I won't use AI slop projects. It already annoys me to no ends that AI skynet successfully took over ruby development. I don't feel like even giving any feedback, as a few ruby devs such as Hiroshi Shibata, only interact with other beings via AI slop spam via claude; suddenly newly gained "perfect english language skills". It is all so fake now when AI infiltrates projects.

**gizajob** · 2026-09-19T15:58:09.000Z：

>Why bring it to life?Why not? The author wanted it, and had wanted it for about four decades since trying and failing as a child due to the difficulty of the task. If you’re in a certain frame of mind, then “why bring it to life?” can be directed at any kind of cultural work to negate it out of existence.

**derac** · 2026-09-19T15:58:43.000Z：

AI assisted or not, you have no idea how much of his personal effort went into the project.

**dainiusse** · 2026-09-19T16:04:02.000Z：

For the fun of it. Why not. And otoh, isn't it impressive that llm's can do it.

**walrus01** · 2026-09-19T16:35:00.000Z：

> I guess my question is why. This is obviously not a piece of software anyone will ever use.My best theory would be it's something that was built as like a novelty/proof of concept, that a current state of the art LLM can do tedious tasks like assembly on a ridiculously old/low resource platform and turn out something that actually looks coherent. I don't personally know a lot of people who enjoy building large things in assembly but LLMs aren't bothered by doing tedious tasks. Due to the tiny size of the thing it can probably very rapidly iterate on "this doesn't work, change a thing, run it again" thousands of times.

**reaperducer** · 2026-09-19T17:05:07.000Z：

If the author didn't do this for themselves - to learn, to show off their skills - then why bring it to life?Likes. Clicks. Vanity. Being able to list GitHub on a resume.The usual stuff we get from anything adjacent to A.I.We went to the moon with slide rules. Now we boil the oceans for "likes."

**kejdjejxjejdj** · 2026-09-19T17:26:41.000Z：

> If the author didn't do this for themselves - to learn, to show off their skills - then why bring it to life?Why not?What if the person just wanted to see if it could be done and how it would look like, but wasn’t interested in the nitty-gritty bits in between?There’s so much elitism and “you can’t sit with us” energy here that I feel like I just lost 4 decades of my life just reading this—and not in a good way.Yeah, there certainly is AI slop. But there’s also very good uses of AI. So how about we stop shaming people for just building things they wanted to build using the tools at their disposal?> But now, it isn't, so is it still something we ought to celebrate?Why isn’t it? Don’t “having an idea and acting on it” count anymore? You guys seem so utterly insecure it’s depressing.

**leidenfrost** · 2026-09-19T17:44:34.000Z：

> then why bring it to life?Like many things in life, the answer is just "because I want to" and "because I can". Not everything has to be a linear progression or a level-up mechanic like a mmorpg.Sometimes you want to create something out of creativity and you like seeing it done. The same way a painter wants to create something, not to show off skills, not to linearly progress onto something, but because they like making something out of nothing.

**robin_reala** · 2026-09-19T14:57:32.000Z：

The critical difference I think is deterministic vs non-deterministic. A compiler isn’t the correct comparison, it’s reading out your desired specs to a team member who does the actual engineering work.

**flohofwoe** · 2026-09-19T15:29:54.000Z：

For me the red line is obviously AI generated readmes. If the author can't even be arsed to write obviously human facing text by himself I immediately lose all interest too.

**dosisking** · 2026-09-19T15:34:20.000Z：

Your analogies are completely non-sensical.

**gizajob** · 2026-09-19T15:56:51.000Z：

I just derived this exact line of thought from a different comment above so I’ve no idea why you’re getting downvoted for it.

**tarkin2** · 2026-09-19T15:45:39.000Z：

Their labour didn’t involve coding. When we equate labour to creating a load of prompts then it feels hollow to me.Was this, then, done to impress others rather than enrich the coders skills and experience?The futuristic equivalent of pressing the “demo” button on old electronic keyboard and pretending to play

**flohofwoe** · 2026-09-19T15:27:34.000Z：

Not the parent, but it reads a lot like written by AI. It has that typical breathless style that's exhausting just from reading.Also, looking at the code, the whole project looks vibe coded, no human would write such comments. Everything in a single git commit also looks "suspicious". It's cool that LLMs can write Z80 asm now, but yeah "labour of love"... tsk tsk tsk...

**jameshart** · 2026-09-19T15:34:15.000Z：

Claude’s written voice is so distinctive, anyone who has spent time working with Claude instantly recognizes it.Which, if you think about it too hard, says something slightly profound and a little disturbing about identity…

**vinc** · 2026-09-19T18:11:10.000Z：

I use claude at work, I have to read its wall of text all day long, it's instantly recognizable. Like many others I'm developing an aversion toward it. The OP's project is pretty cool but I just couldn't read the readme.

**jameshart** · 2026-09-19T16:31:55.000Z：

You can do a lot with custom agent prompts. Just telling Claude ‘this is only a personal project, we’re messing around here’ changes its tone somewhat already. It’s still Business Claude, but more Casual Friday Claude, less Monday Morning Standup Meeting Claude.

**reaperducer** · 2026-09-19T17:11:24.000Z：

the only issue here is that Claude is targeted to enterprise engineering teams so its language model is trained for SoCal startup culture.SV is SoCal now? I missed the earthquake.

**kalleboo** · 2026-09-19T16:35:59.000Z：

I want to hear about the great time they had. That would be interesting.Instead I hear about the great time Claude had being prompted to do it.edit: noticed the person who posted this here is not the same as the author. the author appears to have just randomly made the project public without any kind of announcement. so we don't know their intentions.

**kalleboo** · 2026-09-19T18:23:34.000Z：

Would love to see a corporation claiming ownership of a ZX Spectrum GUI, that would be performance art

**kejdjejxjejdj** · 2026-09-19T17:17:51.000Z：

> If you've never done anything for yourself, usually with your own hands, you don't understand the pleasure and satisfaction that comes from doing it.That’s an absurd thing to say.Doesn’t matter what “AI” feels or doesn’t feel. AI is a tool. You can derive as much pleasure from having an ideia, planning it, working on it from a higher level, and seeing it come to life as you do when you get down and dirty with it and do it from the low level up.Let’s talk like adults here. Please.

**Someone** · 2026-09-19T17:21:00.000Z：

Designing a table and letting somebody else build it can be enjoyable, too.There are plenty of people enjoying designing, for example people who 3D print objects they design, or people designing PCBs or even entire gadgets but outsourcing production.With LLMs, I guess a factor is how much direction you give the machine. “Build me a graphical desktop” likely isn’t very enjoyable, but I can see co-working with a LLM being enjoyable. Examples- think of some novel UI interaction, and let the LLM code it- spending hours to speed up the GUI or to make it use less memory

**alt227** · 2026-09-19T17:29:12.000Z：

I have coded big projects manually for a long time. Being able to get ai to do it, then step back and marvel at knowing how much work that would have taken manually is very satisfying.

**leidenfrost** · 2026-09-19T17:39:46.000Z：

You can say the same for building computers. You didn't actually "built" a computer from the ground up. You just bought the pre-made hardware and plugged it in the places that are made to be easily pluggable.Everything in tech is about standing in the shoulders of what came before.

**alt227** · 2026-09-19T17:27:59.000Z：

Thats your life and your opinion which you are fully entitled to, but dont make the mistake of thinking your life and opinion is better than anyone elses. It suits you, thats whats important.

**noir_lord** · 2026-09-19T16:14:31.000Z：

> No, I think it’s cool AF.That is of course your right.> You sound like the fun police and someone who should stick to programming in raw, unadulterated machine code rather than using any kind of assistance.You felt the need to write that so allow me keep the response short: go fuck yourself.

**gizajob** · 2026-09-19T16:26:49.000Z：

You’ve officially reached the “you pesky kids get off my lawn” stage in your interest in computing.

**kejdjejxjejdj** · 2026-09-19T17:36:58.000Z：

Not all AI-assisted projects are AI-slop. The fact that you think so only tells me that you’re deeply insecure about your knowledge of a subject that you’re interested in.

**in_absentia** · 2026-09-19T16:27:32.000Z：

> Why not?You're only addressing one half of my argument. The answer to this is obvious: the default state is that things don't get done unless we have a reason. So there is a motivation at play and it's perfectly OK to inquire about it, especially if the author appears to be cagey about how the project came to be. If your answer is "it was the author's childhood dream", fair.But that brings me to the second half of the argument: I think we upvote this article in large part because of the historical association of a "crazy 8-bit software project" with "something that took perseverance and skill and our community should reward it". That link is severed now.

**mzi** · 2026-09-19T16:23:39.000Z：

Nothing else than a bit of prompting went in to this.

**kejdjejxjejdj** · 2026-09-19T17:44:38.000Z：

> Instead I hear about the great time Claude had being prompted to do it.I don’t think anyone is talking or even considering how much fun Claude had coming up with the code for this.Fun is subjective. “A great time” is subjective. The author could have had bucket loads of fun discussing, architecting, rethinking, planning and bringing the project to life through Claude. Or they could have had a miserable time with Claude but just wanted to see the thing working. Maybe both? Maybe neither?The point is: chill. AI is nothing more than a tool. A tool that requires an operator. And like every other tool in human history, it can produce bad results or wonderful results, it all depends on who’s operating it and how much domain knowledge they have.Things aren’t so black and white. Open up your mind a little (crazy concept, I know) and just let people enjoy things.

**MobiusHorizons** · 2026-09-19T17:32:16.000Z：

You are arguing against a very well known phenomenon. Technical people often avoid getting promoted to management precisely because they love doing the thing themselves. Despite the higher potential for impact in a management position, losing the detailed view of a practitioner is a real loss. This phenomenon is less obvious in big tech because there are so many people who really wanted to be managers the whole time, but had to be engineers first or never really cared about the work, but want a promotion for the better pay.

**alt227** · 2026-09-19T17:32:01.000Z：

This.Knowing your limitations of building, but being good at designing and watching somebody/something else realise your vision is incredibly satisfying.I see it like 3D printing. Nobody can extrude molten plastic out of their bodies to make things, but the skill of designing the construction well and then watch the machine execute it is certainly a good feeling. I dont really see how this is different to designing some software verbally and prompting an ai to build it for you.

**gizajob** · 2026-09-19T16:22:26.000Z：

I only accept responses in Hex I’m afraid.

**onraglanroad** · 2026-09-19T16:56:22.000Z：

I genuinely found it funny that you thought "go fuck yourself" would be either effective or off-putting to someone with the username "gizajob".You know Boys from the Black Stuff right?

**alt227** · 2026-09-19T17:17:44.000Z：

I think you just proved the parents point.

**gizajob** · 2026-09-19T16:40:12.000Z：

Even a cursory flick through the GitHub page until you reach “Why” shows that to be the answer.

**alt227** · 2026-09-19T17:22:51.000Z：

> The default state is that things don't get done unless we have a reason.What about art? People make art and inventions just for the hell of it and to satisfy come itch. Whether or not other people then like it or find it useful is subjective and up to the individual. IMO taking away peoples right to make stuff for no reason and enjoy doing it is to take away our humanity.I upvoted the article because it brought me some nostalgia and entertained me for a bit while I played with it and knowing how to code a spectrum myself, marvelled at the complexity of the code and the project itself. Maybe people have more reasons to enjoy things than your narrow viewpoint allows for?

**kejdjejxjejdj** · 2026-09-19T17:31:45.000Z：

> But that brings me to the second half of the argument: I think we upvote this article in large part because of the historical association of a "crazy 8-bit software project" with "something that took perseverance and skill and our community should reward it". That link is severed now.There’s the problem: you are assuming everyone else thinks in elitist terms like you. It still is a crazy 8-bit software project. It still rather impressive and fun to see.Your “historical reason” reads a lot more like whining than anything else and it does come across as a display of insecurity.AI is just a freaking tool. The dev used to tool to bring his vision to life. That’s the extent of it. Stop making such a fuss over something that quite literally was just made for fun.Let people have fun in peace. Let people enjoy things in peace.

**grugagag** · 2026-09-19T16:29:58.000Z：

How about the desire to steer LLMs to a point of their choosing? LLMs wouldn't do this by themselves...

**jameshart** · 2026-09-19T16:41:10.000Z：

If you’re familiar with the way in which documentation artifacts like this fall out of a Claude project, you will recognize that every place where Claude says ‘this changes everything’ or ‘this is the load bearing insight’ most likely resulted from a human looking at what Claude had done, and redirecting it towards a more fruitful line of inquiry. When Claude gets ‘excited’ about a thing like ‘we figured out which clock measurement approach helps us actually optimize performance’ - excited enough to explain it in this level of detail - it usually results from the user pulling Claude out of a rabbit hole where it was going about things the wrong way.

**alt227** · 2026-09-19T17:26:10.000Z：

"A bit of prompting" is subjective, and can indeed take a lot of work to craft accurate prompts which produce genuinely useful output.

**kejdjejxjejdj** · 2026-09-19T17:34:08.000Z：

I think you severely lack in domain knowledge if you think “nothing else than a bit of prompting went in to this”.

**kalleboo** · 2026-09-19T18:11:45.000Z：

My point is more this was posted without context.I may be interested to read a blog post about the trials and tribulations the creator had, I'm sure there was something interesting going on getting LLMs writing Z80 assembly and testing things on real devices.Not interested in reading an uncurated Claude context summary.

**kejdjejxjejdj** · 2026-09-19T17:53:59.000Z：

You either replied to the wrong comment or didn’t and proved my point exactly: some people like the technical low level approach, others prefer the higher level architectural work.There’s space for both and there’s a need for both.

**varjag** · 2026-09-19T18:37:56.000Z：

If you don't know how the artefact you ordered works you haven't built it in any meaningful sense of the word.

**Frenchgeek** · 2026-09-19T16:56:20.000Z：

+++ Out Of Cheese Error +++ +++ Redo From Start +++

**gizajob** · 2026-09-19T17:04:35.000Z：

10/10 great knowledge.

**InsideOutSanta** · 2026-09-19T18:07:02.000Z：

Yeah, I think this is interesting independently of how it was made, because it reveals a kind of "what could have been" alternative history. It's fun to imagine a past where the Speccy got a desktop, and it's fun to see what it could have looked like running on real hardware (or on an emulator).
