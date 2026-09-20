---
type: "corpus"
item_id: "292837e70f6852b2"
title: "Show HN: Duff's device, sleep sort and a quine, hung in a room you walk through"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49713336"
project_url: "https://programmingmuseum.com/hall/curiosities"
author: "justbits"
published_at: "2026-09-15T14:44:32Z"
captured_at: "2026-09-20T09:37:13+08:00"
lang: "en"
kind: "post"
topic: "移动 App"
shard: "2026-09-20"
pub_day: "2026-09-15"
tags:
  - 语料
  - hn_show
  - author_justbits
  - story_49713336
  - show_hn
metrics: {"points": 4, "comments": 0, "engagement_velocity": 4}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:90d"
---

# Show HN: Duff's device, sleep sort and a quine, hung in a room you walk through

> [!info] 一句话导读
> Cabinet of Curiosities

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49713336>
> 指标：点赞=4 · 评论=0 · engagement_velocity=4
> 作者：justbits　|　发布：2026-09-15T14:44:32Z
> 项目链接：<https://programmingmuseum.com/hall/curiosities>
> 采集：2026-09-20T09:37:13+08:00　|　id：`292837e70f6852b2`

## 正文

Cabinet of Curiosities · Programming Museum

# Cabinet of Curiosities

Cabinet of Curiosities

```
const s = "const s = %s;\nconsole.log(s.replace(\"%s\", JSON.stringify(s)));";
console.log(s.replace("%s", JSON.stringify(s)));
```

A Program That Writes Itself

```
// Primality testing with a regular expression.
//
// The number n becomes a string of n ones. The pattern then asks whether
// that string can be cut into two-or-more equal groups of two-or-more —
// which is exactly the question of whether n has a non-trivial factor.
const composite = /^1?$|^(11+?)\1+$/;

const isPrime = (n) => !composite.test("1".repeat(n));

const primes = [];
for (let n = 2; primes.length < 12; n++) {
	if (isPrime(n)) primes.push(n);
}

console.log(primes.join(" "));
```

Primes, By Regular Expression

```
/*
 * Copy `count` shorts to a memory-mapped output register.
 *
 * Tom Duff, Lucasfilm, 1983. The loop is unrolled eight times to cut the
 * cost of the test at the bottom -- and the leftover, the count modulo
 * eight, is dealt with by jumping into the middle of the unrolled body.
 */
void send(short *to, short *from, int count)
{
    int n = (count + 7) / 8;

    switch (count % 8) {
    case 0: do { *to = *from++;
    case 7:      *to = *from++;
    case 6:      *to = *from++;
    case 5:      *to = *from++;
    case 4:      *to = *from++;
    case 3:      *to = *from++;
    case 2:      *to = *from++;
    case 1:      *to = *from++;
```

The Loop That Starts in the Middle

```
/*
 * Rule 110. A line of cells, each alive or dead. To make the next line,
 * look at each cell with its two neighbours -- eight possible arrangements
 * -- and read off what to do from the bits of the number 110.
 *
 * That is the whole of it, and it is enough to compute anything at all.
 */

const WIDTH = 64;
const GENERATIONS = 32;
const RULE = 110;

let cells = Array(WIDTH).fill(0);
cells[WIDTH - 1] = 1; // one living cell, at the right-hand end

for (let gen = 0; gen < GENERATIONS; gen++) {
  console.log(cells.map((c) => (c ? "#" : " ")).join(""));

  cells = cells.map((_, i) => {
    const left = cells[(i - 1 + WIDTH) % WIDTH];
```

Eight Rules Is Enough

```
// The Y combinator: recursion for a language that has none.
//
// Nothing below names itself. `fact` never says "fact", and yet it recurs.
const Y = (f) => ((x) => x(x))((x) => f((...args) => x(x)(...args)));

const fact = Y((recur) => (n) => (n <= 1 ? 1 : n * recur(n - 1)));

console.log([1, 2, 3, 4, 5, 6].map(fact).join(" "));
```

Recursion Without a Name

```
/*
 * One over the square root of a number, to about two decimal places,
 * without a square root and without a division.
 */
float Q_rsqrt(float number)
{
    long  i;
    float x2, y;
    const float threehalfs = 1.5F;

    x2 = number * 0.5F;
    y  = number;

    i  = *(long *) &y;                  /* read the float as an integer   */
    i  = 0x5f3759df - (i >> 1);         /* what the ... ?                 */
    y  = *(float *) &i;                 /* read it back as a float        */

    y  = y * (threehalfs - (x2 * y * y));   /* one step of Newton-Raphson */

    return y;
```

The Number Nobody Could Explain

```
#!/usr/bin/env bash
#
# Sort a list of numbers without comparing any two of them.

sleepsort() {
    for n in "$@"; do
        (
            sleep "$n"
            printf '%s\n' "$n"
        ) &
    done
    wait
}

sleepsort 5 3 9 1 7 2 8
```

Sorted by Waiting

```
/**
 * Arithmetic with no numbers in it, performed entirely by the type checker.
 * Nothing below runs. All of it is computed before the program exists.
 */

/** A tuple of exactly N members: counting, done by building a thing to count. */
type Tally<N extends number, T extends unknown[] = []> =
  T["length"] extends N ? T : Tally<N, [...T, unknown]>;

/** Addition. Lay two tallies end to end and ask how long the result is. */
type Add<A extends number, B extends number> =
  [...Tally<A>, ...Tally<B>]["length"];

/** Subtraction. Take A apart until what remains is exactly B long. */
type Sub<A extends number, B extends number> =
  Tally<A> extends [...infer Rest, ...Tally<B>] ? Rest["length"] : never;

/** Multiplication is repeated addition, so it is repeated concatenation. */
type Mul<A extends number, B extends number, Acc extends unknown[] = []> =
  B extends 0 ? Acc["length"] : Mul<A, Sub<B, 1>, [...Acc, ...Tally<A>]>;
```

Arithmetic with No Numbers

Shown as a list, because your system asks for reduced motion.

## 导航

- 项目页：[[10-项目/programmingmuseum.com_695c1577]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`移动 App`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
