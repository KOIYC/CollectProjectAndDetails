---
type: "corpus"
item_id: "62caa9c7491e702a"
title: "Show HN: An Implementation of Scheme in Rust"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49500050"
project_url: "https://github.com/vinay/rscheme"
author: "vmmenon"
published_at: "2026-08-30T16:20:35Z"
captured_at: "2026-09-21T03:11:30+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-21"
pub_day: "2026-08-30"
tags:
  - 语料
  - hn_show
  - author_vmmenon
  - story_49500050
  - show_hn
metrics: {"points": 2, "comments": 0, "engagement_velocity": 2}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:52d"
---

# Show HN: An Implementation of Scheme in Rust

> [!info] 一句话导读
> An implementation of Scheme in Rust.

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49500050>
> 指标：点赞=2 · 评论=0 · engagement_velocity=2
> 作者：vmmenon　|　发布：2026-08-30T16:20:35Z
> 项目链接：<https://github.com/vinay/rscheme>
> 采集：2026-09-21T03:11:30+08:00　|　id：`62caa9c7491e702a`

## 正文

# vinay/rscheme

An implementation of Scheme in Rust.

- Stars: 0
- Forks: 0
- Watchers: 0
- Open issues: 0
- License: Other
- Default branch: main
- Created: 2026-08-30T15:37:16Z

## Languages

- Rust
- Scheme
- Tree-sitter Query

## Top Contributors

- vinay (2 contributions)

---

## README

# rscheme

ci

A Scheme interpreter written in Rust, sized for one purpose: running the code
from *Structure and Interpretation of Computer Programs*.

Everything the book's programs need is here — proper tail calls, `cons-stream`
and promises, mutable pairs, `set!` and local state, quasiquotation, and a
`read` that a driver loop can call. Everything they do not need has been left
out: there is no `call/cc`, no macro system, no exact rationals or bignums, no
continuations beyond the Rust stack. The book builds most of that *inside*
Scheme anyway, which is rather the point of chapters 2, 4 and 5.

Memory is reclaimed by a **mark-and-sweep garbage collector**, written from
scratch and deliberately kept small enough to read in one sitting.

The crate has **no dependencies** — not even for random numbers.

---

## Building and running

```sh
cargo build --release
./target/release/rscheme
```

```
rscheme> (define (square x) (* x x))
square
rscheme> (square 12)
144
rscheme> (define ones (cons-stream 1 ones))
ones
rscheme> (stream-head ones 5)
(1 1 1 1 1)
rscheme> (exit)
```

Files given on the command line are loaded first, then the REPL starts:

```sh
./target/release/rscheme sicp/ch4-mceval.scm      # load, then get a prompt
./target/release/rscheme -b -e '(display (+ 1 2))' # batch, no prompt
```

| option | meaning |
|---|---|
| `-e`, `--eval EXPR` | evaluate `EXPR` after loading the files |
| `-b`, `--batch` | do not start the REPL |
| `--gc-threshold N` | collect whenever `N` objects are live (default 100000) |
| `--gc-stress` | collect on *every* allocation and never reuse a slot |
| `--gc-trace` | print a line per collection |
| `--max-depth N` | recursion limit before the interpreter gives up (default 200000) |
| `-h`, `-V` | help, version |

Inside Scheme, `(gc)` forces a collection, `(gc-stats)` returns heap counters,
and `(gc-trace #t)` turns tracing on.

---

## Running the book's code

The `sicp/` directory holds the source files distributed with the book. Some
are complete programs; some are transcripts of a whole chapter.

**Complete programs** — load and use directly:

```sh
# 4.1  the metacircular evaluator
./target/release/rscheme sicp/ch4-mceval.scm
rscheme> (define the-global-environment (setup-environment))
rscheme> (eval '((lambda (x) (* x x)) 7) the-global-environment)

# 4.3  the nondeterministic evaluator
./target/release/rscheme sicp/ch4-ambeval.scm \
  -e '(define the-global-environment (setup-environment))' -e '(driver-loop)'

# 4.4  the query language
./target/release/rscheme sicp/ch4-query.scm \
  -e '(initialize-data-base microshaft-data-base)' -e '(query-driver-loop)'

# 5.2  the register-machine simulator
./target/release/rscheme sicp/ch5-regsim.scm

# 5.4  the explicit-control evaluator
./target/release/rscheme sicp/load-eceval.scm \
  -e '(define the-global-environment (setup-environment))' -e '(start eceval)'

# 5.5  the compiler, with its output run on the eceval machine
./target/release/rscheme sicp/load-eceval-compiler.scm sicp/ch5-compiler.scm \
  -e "(compile-and-go '(define (factorial n) (if (= n 1) 1 (* (factorial (- n 1)) n))))"
```

Two notes that apply to the book's code rather than to this interpreter:

* `ch4-mceval.scm` and its relatives leave the primitive list as an exercise
 (`;; more primitives`), so only `car`, `cdr`, `cons` and `null?` are
 available inside them until you extend `primitive-procedures`. The test
 suite shows how.
* `ch1.scm`, `ch2.scm`, `ch3.scm`, `ch4.scm` and `ch5.scm` are chapter
 transcripts, not libraries. They redefine names as the text develops them —
 `ch1.scm` ends with exercise 1.9's Peano `+` and exercise 1.8's `square`
 defined as `(exp (double (log x)))`, and `ch2.scm` redefines `cons`, `car`
 and `cdr` for the Church-pair exercise. `ch2tests.scm` is a transcript of
 test sessions taken at *several different points* in chapter 2 — it checks
 Ben's rectangular representation and then Alyssa's polar one under the same
 names — so it cannot run start-to-finish in any Scheme; replay the section
 you are working through. `ch4.scm` and `ch5.scm` also contain
 illustrative fragments (a bare `(cond ((> x 0) x) ...)`, a `(controller ...)`
 sketch) that are not meant to be evaluated at all, so those two stop with an
 unbound-variable error partway through, exactly as they would in MIT Scheme.
 Load a chapter file to browse it; type the programs in to run them.

---

## The language

**Special forms.** `quote` `quasiquote`/`unquote`/`unquote-splicing` `if`
`define` (including `(define (f . args) ...)` and the curried
`(define ((f a) b) ...)`) `set!` `lambda` (fixed, rest and whole-list
parameters) `begin` `let` `let*` `letrec` named `let` `cond` (with `else` and
`=>`) `case` `and` `or` `when` `unless` `delay` `cons-stream`.

**Primitives.** Numbers (`+ - * / = < > <= >= abs quotient remainder modulo
gcd lcm min max expt sqrt exp log sin cos tan asin acos atan floor ceiling
round truncate number? integer? exact? inexact? zero? positive? negative?
even? odd? exact->inexact inexact->exact number->string string->number random
square cube 1+ -1+`), pairs and lists (`cons car cdr set-car! set-cdr!` all
twenty-eight `c…r` accessors, `list cons* length append reverse list-ref
list-tail list-head last-pair list-copy memq memv member assq assv assoc
list?`), equivalence (`eq? eqv? equal? not`), type tests (`null? pair? symbol?
string? char? boolean? vector? procedure? promise? eof-object?`), strings,
symbols and characters (`string-length string-ref substring string-append
string-copy string=? string? string-null? string->symbol
symbol->string string->list list->string string make-string string-upcase
string-downcase symbol-append string-search-forward char->integer
integer->char char=? char list list->vector
vector-fill! vector-grow subvector`), higher-order procedures (`apply eval map
for-each filter reduce fold-left fold-right`), streams (`stream-car stream-cdr
stream-null? stream-pair? force make-promise list->stream stream->list
stream-head`, plus `the-empty-stream`), and input/output (`display write
write-string write-line newline read read-line load error exit runtime
real-time`). `true`, `false` and `nil` are bound, as the book assumes, and so
are `user-initial-environment` and `system-global-environment` -- the query
system's `lisp-value` evaluates its predicates with
`(eval expr user-initial-environment)`, and both work here.

**Deliberate simplifications**, all of them visible rather than hidden:

* **Numbers** are exact 64-bit integers and inexact doubles, nothing else.
 `(/ 6 3)` is the exact `2`; `(/ 1 3)` cannot be represented exactly and
 becomes the inexact `.3333333333333333` rather than the rational `1/3`. An
 integer operation that would overflow 64 bits produces a double instead of
 wrapping.
* **`eq?` and `eqv?` are the same test.** The book relies on `eq?` over
 symbols and small integers, both of which behave.
* **Symbols fold to lower case** when read, as in R5RS and MIT Scheme, so
 `'Bitdiddle` prints as `bitdiddle`.
* **Printing is bounded.** Exercise 3.13 asks you to build a circular list;
 printing one stops after 100 000 elements rather than looping forever.
* **`define` returns the symbol it bound**, so the REPL echoes the name.

---

## How it works

```
src/
  main.rs        command line; runs the interpreter on a 512 MB stack
  repl.rs        the `rscheme> ` loop, sharing its input with `read`
  lib.rs         crate documentation and module map

  lexer.rs       text    -> tokens
  reader.rs      tokens  -> Scheme data (real heap pairs, not a syntax tree)
  eval.rs        data    -> values: the evaluator
  printer.rs     values  -> text

  value.rs       how a value is represented; heap object kinds
  heap.rs        the object table and the mark-and-sweep collector
  symbol.rs      the symbol interner
  interp.rs      environments, equality, `force`, `load`, and the whole state
  error.rs       Scheme errors
  builtins/      the primitive procedures, one module per family
```

### Values

A `Value` is two machine words and `Copy`. Booleans, integers, doubles,
characters, symbols, the empty list and primitive procedures live *inside* the
value and are invisible to the collector. Pairs, strings, vectors, compound
procedures, environment frames and promises live in the heap and are named by a
`Handle`, which is an index into the heap's object table — not a pointer.
Copying a value therefore never affects an object's lifetime; only reachability
does.

### The evaluator, and tail calls

SICP's iterative processes are tail-recursive procedures, and its driver loops
never return. An evaluator that used a Rust call for every Scheme call would
run out of stack on them, so `Interp::eval` is a **trampoline**: a loop holding
the current expression and environment. A form in tail position — the last
expression of a body, the taken branch of an `if`, the final `and`/`or` operand
— overwrites those and goes round the loop again instead of recursing. A
million-iteration loop runs in constant space, and so does a loop running
*inside* the metacircular evaluator, two levels up.

Non-tail sub-expressions do use Rust recursion, which is what Scheme requires.
That is bounded by `--max-depth` so a runaway recursion reports
`Aborting!: maximum recursion depth exceeded` and returns you to the prompt,
rather than overflowing the stack and killing the process.

### The garbage collector

The whole collector is in `src/heap.rs`. Objects live in slots of one big
`Vec `; a collection has two phases.

**Mark.** Starting from the roots, follow every reference and set a mark bit.
The trace uses an explicit worklist rather than recursion, so a list a million
elements long cannot overflow the stack *while collecting it*.

**Sweep.** Walk the slot table. Every allocated slot that is unmarked is
unreachable: overwrite it with `Obj::Free` — which drops the Rust-side buffers
it held — and put its slot number on the free list. The next collection is
scheduled at twice the surviving population.

Because it traces rather than counts references, it collects cycles. Chapter
3's circular lists, and the mutually referring environment-and-closure pairs
that every recursive procedure creates, are reclaimed the moment they become
unreachable.

**Roots** are the interesting part. There are exactly two sources: the global
environment, and a *shadow stack* of values the evaluator is currently working
with. The rule the rest of the interpreter follows is one sentence:

> If you hold a `Value` in a Rust local across a call that might allocate, that
> value must also be on the shadow stack.

Evaluator code takes a mark on entry, pushes what it needs to keep, and
truncates back to the mark on exit. The shadow stack doubles as the argument
stack while a call is being assembled, so arguments already evaluated are
protected while the remaining ones are computed — the same trick a real VM
uses.

**Catching a missing root** is the hard part of writing a collector, because
the bug only shows when a collection lands at exactly the wrong moment.
`--gc-stress` removes the luck: it collects on every single allocation *and
never recycles a slot*, so a value that lost its last root is permanently
`Obj::Free` and the next use of the stale handle aborts with a message naming
the problem, instead of quietly returning some other object. `tests/scheme/
stress.scm` exercises every rooting path in the evaluator under that mode.

For everything else there is `--gc-threshold N`, which collects roughly every
`N` objects with slots reused as normal — cheap enough that the entire test
suite runs that way on every `cargo test`.

---

## Tests

```sh
cargo test --release
```

Twelve integration tests, taking about fifteen seconds:

| test | what it covers |
|---|---|
| `scheme_suites_pass` | the Scheme suites in `tests/scheme/` |
| `scheme_suites_pass_with_frequent_collection` | all of them again, collecting every 200 objects |
| `no_root_is_missing_under_gc_stress` | `stress.scm` under `--gc-stress` |
| `book_files_load` | every self-contained file in `sicp/` reads and loads |
| `explicit_control_evaluator_runs` | section 5.4 computes `8!` |
| `compiler_runs` | section 5.5 compiles `factorial` and runs it on the eceval machine |
| `amb_evaluator_backtracks` | section 4.3 finds `(3 4 5)`, then `(5 12 13)` on `try-again` |
| `query_system_answers` | section 4.4 answers a fact query and a rule query |
| `query_lisp_value_works` | section 4.4's `lisp-value`, through the host's `eval` |
| `process_survives_hostile_input` | non-ASCII input, multi-line strings, dotted special forms |
| `bom_files_load` | a file starting with a UTF-8 byte-order mark |
| `repl_behaves` | prompt, multi-line input, error recovery |

The Scheme suites themselves:

| file | contents |
|---|---|
| `01-core.scm` | the core language: 89 checks |
| `02-sicp-ch1.scm` | Newton's method, counting change, Fermat test, fixed points, `deriv` |
| `03-sicp-ch2.scm` | rationals, trees, sequence operations, eight queens, symbolic differentiation, Huffman coding, data-directed dispatch |
| `04-sicp-ch3.scm` | bank accounts, queues, tables, memoisation, the sieve of Eratosthenes, the implicit Fibonacci stream |
| `05-gc.scm` | reclamation, survival of live data, closures, unforced stream tails, and cycles |
| `06`–`08` | the book's metacircular, analyzing and lazy evaluators |
| `09-regsim.scm` | the GCD, factorial and Fibonacci machines of figures 5.4, 5.11 and 5.12 |
| `10-regressions.scm` | pins past fixes: 64-bit edge cases, `cond =>` tail calls, `append!`, exact comparisons |
| `stress.scm` | every rooting path, small enough to run under `--gc-stress` |

---

## License

The interpreter is MIT-licensed; see LICENSE. The book's code in
`sicp/` is by the SICP authors and MIT Press, redistributed under the
Creative Commons Attribution-ShareAlike 4.0 International License — see
sicp/README.md.

## 导航

- 项目页：[[10-项目/github.com_6ca7c61e]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
