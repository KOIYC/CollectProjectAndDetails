---
type: "project"
title: "Show HN: Duff's device, sleep sort and a quine, hung in a room you walk through"
project_url: "https://programmingmuseum.com/hall/curiosities"
first_seen: "2026-09-20T09:37:13+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_justbits
  - story_49713336
  - show_hn
lang: "en"
---

# Show HN: Duff's device, sleep sort and a quine, hung in a room you walk through

> [!info] 一句话导读
> Cabinet of Curiosities

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://programmingmuseum.com/hall/curiosities>
> 首次收录：2026-09-20T09:37:13+08:00
> 来源渠道：HN Show HN
> 标签：author_justbits, story_49713336, show_hn
> 最新指标：点赞=4 · 评论=0 · engagement_velocity=4

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-09-20T09:23:24+08:00 | HN Show HN | 点赞=4 · 评论=0 · engagement_velocity=4 | [[20-语料/posts/hn_show/2026-09-20/292837e70f6852b2_Show-HN-Duff's-device,-sleep-sort-and-a-quine,-hun]] |
| 2026-09-20T09:37:13+08:00 | HN Show HN | 点赞=4 · 评论=0 · engagement_velocity=4 | [[20-语料/posts/hn_show/2026-09-20/292837e70f6852b2_Show-HN-Duff's-device,-sleep-sort-and-a-quine,-hun]] |

## 摘要正文

Cabinet of Curiosities · Programming Museum  # Cabinet of Curiosities  Cabinet of Curiosities  ``` const s = "const s = %s;\nconsole.log(s.replace(\"%s\", JSON.stringify(s)));"; console.log(s.replace("%s", JSON.stringify(s))); ```  A Program That Writes Itself  ``` // Primality testing with a regular expression. // // The number n becomes a string of n ones. The pattern then asks whether // that string can be cut into two-or-more equal groups of two-or-more — // which is exactly the question of whether n has a non-trivial factor. const composite = /^1?$|^(11+?)\1+$/;  const isPrime = (n) => !composite.test("1".repeat(n));  const primes = []; for (let n = 2; primes.length < 12; n++) { 	if (isPrime(n)) primes.push(n); }  console.log(primes.join(" ")); ```  Primes, By Regular Expression  ``` /*  * Copy `count` shorts to a memory-mapped output register.  *  * Tom Duff, Lucasfilm, 1983. The loop is unrolled eight times to cut the  * cost of the test at the bottom -- and the leftover, the count modulo  * eight, is dealt with by jumping into the middle of the unrolled body.  */ void send(short *to, short *from, int count) {     int n = (count + 7) / 8;      switch (count % 8) {     case 0…
