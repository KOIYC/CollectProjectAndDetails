---
type: "corpus"
item_id: "c541f5a56808b3b9"
title: "Btrfs/ZFS/bcachefs under workloads classic benchmarks skip"
source: "hn_front"
source_name: "HN 首页（非 Show HN）"
url: "https://news.ycombinator.com/item?id=49768833"
project_url: "https://bartosz.fenski.pl/modern-fs-benchmark"
author: "farlight"
published_at: "2026-09-19T18:11:40Z"
captured_at: "2026-09-20T03:41:55+08:00"
lang: "en"
kind: "post"
tags:
  - 语料
  - hn_front
  - author_farlight
  - story_49768833
  - front_page
metrics: {"points": 30, "comments": 23, "engagement_velocity": 30}
comments_count: 22
comments_total: 22
discovered_via: "hn:front_page:2d"
archived: true
archived_at: "2026-09-20T09:16:59+08:00"
archive_reason: "排除:无主题词"
---

# Btrfs/ZFS/bcachefs under workloads classic benchmarks skip

- **来源**：HN 首页（非 Show HN）　|　**kind**：post
- **原帖**：https://news.ycombinator.com/item?id=49768833
- **指标**：点赞=30 · 评论=23 · engagement_velocity=30
- **作者**：farlight　|　**发布**：2026-09-19T18:11:40Z
- **项目链接**：https://bartosz.fenski.pl/modern-fs-benchmark
- **采集**：2026-09-20T03:41:55+08:00　|　**id**：`c541f5a56808b3b9`

## 正文

modern-fs-benchmark

# modern-fs-benchmark

Multi-device CoW filesystems under workloads classic benchmarks skip — latest run 2026-09-07 13:24:30 UTC, kernel 7.0.0-1012-azure, 552 runs recorded · 141 trend points shown · repository

CI runs use loop devices on shared ephemeral VMs (one VM per filesystem): compare shapes and ratios, not absolute MB/s. Each job records a host-calibration anchor — see the table.

ext4/single ext4/md-raid10 ext4/lvm-raid10 xfs/single xfs/md-raid10 xfs/lvm-raid10 xfs/zvol xfs/lvm-raid10-int zfs/mirror zfs/mirror-8k zfs/single zfs/raidz2 zfs/raidz1 btrfs/raid1 btrfs/single btrfs/raid6 bcachefs/replicas2 bcachefs/single bcachefs/ec ext4/md-raid10-luks ext4/md-raid6 zfs/mirror-enc zfs/raidz1-enc zfs/raidz2-enc btrfs/raid1-luks bcachefs/replicas2-enc

## Summary indices

Score model v1: 100 = the selected cohort median. Metrics are normalized by direction, then geometric-meaned with equal subgroup and group weight. Using 8 recent complete selected-cohort runs; integrity is never averaged. Click a column header to sort; select a score to expand its normalized contributions.

| configuration | Overall Core | Core I/O | Responsiveness | Metadata | Integrity |
| --- | --- | --- | --- | --- | --- |
| ext4/single | 126 | 130 6/6 metrics | 116 4/4 metrics | 132 9/9 metrics | N/A |
| ext4/md-raid10 | 98 | 98 6/6 metrics | 87 4/4 metrics | 112 9/9 metrics | FAIL |
| ext4/lvm-raid10 | 124 | 98 6/6 metrics | 160 4/4 metrics | 121 9/9 metrics | FAIL |
| xfs/single | 121 | 120 6/6 metrics | 140 4/4 metrics | 106 9/9 metrics | N/A |
| xfs/md-raid10 | 101 | 105 6/6 metrics | 97 4/4 metrics | 103 9/9 metrics | LUCKY |
| xfs/lvm-raid10 | 162 | 108 6/6 metrics | 368 4/4 metrics | 107 9/9 metrics | FAIL |
| xfs/zvol | 80 | 95 6/6 metrics | 56 4/4 metrics | 97 9/9 metrics | PASS |
| xfs/lvm-raid10-int | 107 | 88 6/6 metrics | 137 4/4 metrics | 100 9/9 metrics | PASS |
| zfs/mirror | 67 | 90 6/6 metrics | 35 4/4 metrics | 97 9/9 metrics | PASS |
| zfs/mirror-8k | 131 | 135 6/6 metrics | 174 4/4 metrics | 97 9/9 metrics | PASS |
| zfs/single | 107 | 137 6/6 metrics | 93 4/4 metrics | 97 9/9 metrics | N/A |
| zfs/raidz2 | 73 | 91 6/6 metrics | 45 4/4 metrics | 96 9/9 metrics | PASS |
| zfs/raidz1 | 86 | 113 6/6 metrics | 59 4/4 metrics | 95 9/9 metrics | PASS |
| btrfs/raid1 | 106 | 93 6/6 metrics | 152 4/4 metrics | 83 9/9 metrics | PASS |
| btrfs/single | 135 | 98 6/6 metrics | 265 4/4 metrics | 94 9/9 metrics | N/A |
| btrfs/raid6 | 91 | 81 6/6 metrics | 105 4/4 metrics | 90 9/9 metrics | PASS |
| bcachefs/replicas2 | 159 | 157 6/6 metrics | 268 4/4 metrics | 96 9/9 metrics | PASS |
| bcachefs/single | 188 | 218 6/6 metrics | 304 4/4 metrics | 101 9/9 metrics | N/A |
| bcachefs/ec | 141 | 142 6/6 metrics | 232 4/4 metrics | 85 9/9 metrics | PASS |
| ext4/md-raid10-luks | 93 | 98 6/6 metrics | 69 4/4 metrics | 118 9/9 metrics | FAIL |
| ext4/md-raid6 | 101 | 83 6/6 metrics | 119 4/4 metrics | 104 9/9 metrics | FAIL |
| zfs/mirror-enc | 64 | 86 6/6 metrics | 33 4/4 metrics | 93 9/9 metrics | PASS |
| zfs/raidz1-enc | 83 | 110 6/6 metrics | 57 4/4 metrics | 93 9/9 metrics | PASS |
| zfs/raidz2-enc | 71 | 90 6/6 metrics | 48 4/4 metrics | 83 9/9 metrics | PASS |
| btrfs/raid1-luks | 101 | 85 6/6 metrics | 128 4/4 metrics | 93 9/9 metrics | PASS |
| bcachefs/replicas2-enc | 156 | 153 6/6 metrics | 260 4/4 metrics | 96 9/9 metrics | PASS |

## Latest run

One card per metric, sorted best-first — the per-card button switches to grouped matrix order. Every value also appears in the table below.

## Snapshot aging ?

Random-overwrite bandwidth (MB/s) per iteration while snapshots accumulate — flat is good, falling is CoW fragmentation cost. Snapshot counts differ by design: 100 where the technology allows, 10 for default-recordsize ZFS, 8 for LVM.

## Trends across runs

One card per metric, one point per run — the newest 100 runs individually, older runs collapsed to daily medians (full history on the results-data branch). Drag on a chart to zoom, double-click to reset; the y-axis rescales to what's visible.

An optional interactive view beside the existing charts. It uses the same compacted history and active filesystem filters; scroll or drag to zoom, and use the toolbox to restore or export.

## Table view

Latest run, all metrics — click a column header to sort. calib = host-disk anchor measured before the filesystem exists (VM noise indicator).

| filesystem | Sequential write MB/s | Random write, 4k + fsync IOPS | Random write, 4 threads IOPS | fsync p99 latency ms | fsync p99.9 latency ms | Random read, 4k cold cache IOPS | Random read, 4 threads IOPS | Sequential read MB/s | Trivial-op p99, idle ms | Trivial-op p99 under streaming write ms | Trivial-op worst case under load ms | Trivial ops completed under load ops | Create 20k-file tree ms | Create 20k-file tree, 4 workers ms | cp -r 20k-file tree, cold ms | rm -rf 20k-file tree ms | ftruncate empty file to 1G ms | Bytes allocated for sparse 1G B | ftruncate 256M file to 512M ms | Create 100k files in one directory ms | Enumerate 100k names, cold ms | Stat 100k files, cold ms | Stat 100k files, warm ms | Delete 100k-file directory ms | Snapshot create ms | Snapshot delete (all) ms | Space reclaim after delete s | Write during reclaim MB/s | zstd compression ratio x | Compressible-data write MB/s | Reflink copy of 2G ms | Overwrite plain file MB/s | Overwrite fresh reflink clone MB/s | Overwrite freshly-snapshotted file MB/s | Degraded random write IOPS | Degraded random read IOPS | Rebuild after device loss s | Scrub after corruption s | Write near full (95% target) MB/s | Write near full (99% target) MB/s | Snapshot create at 500 snaps ms | Remount with 500 snaps ms | Delete 500 snapshots ms | scrub errors found | scrub repaired | data intact after corruption | FIEMAP shows shared extents | delete at 100% full | writable after delete | calib seq MB/s | calib rand IOPS | tools / module version |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ext4/single | 354 | 6,770 | 12,120 | 16.6 | 31.6 | 7,016 | 9,604 | 418 | 1.2 | — | 27,998 | 5 | 1,619 | 725 | 1,787 | 448 | 8.12 | 0 | 0.75 | 3,417 | 82 | 1,306 | 333 | 1,406 | — | — | — | — | — | — | — | 67.0 | — | — | — | — | — | — | 162 | 167 | — | — | — | — | — | — | — | yes | yes | 413 | 14,722 | mke2fs 1.47.2 (1-Jan-2025) |
| ext4/md-raid10 | 171 | 3,223 | 4,726 | 37.5 | 41.2 | 5,731 | 19,324 | 334 | 3.26 | — | 4,753 | 12 | 5,150 | 1,095 | 2,541 | 442 | 9.64 | 0 | 0.76 | 3,389 | 94 | 1,366 | 314 | 1,376 | — | — | — | — | — | — | — | 38.4 | — | — | 11,322 | 5,932 | 86 | 167 | 89.8 | 86.7 | — | — | — | 4,194,304 | 0 | NO | — | yes | yes | 407 | 14,729 | mke2fs 1.47.2 (1-Jan-2025) |
| ext4/lvm-raid10 | 189 | 3,083 | 4,561 | 33.4 | 38.5 | 5,270 | 18,337 | 375 | 8.03 | 59.0 | 60.4 | 138 | 1,680 | 976 | 2,660 | 446 | 20.3 | 0 | 1 | 3,485 | 98 | 1,346 | 311 | 1,405 | 287 | 2,360 | 4 | 34.6 | — | — | — | 37.9 | — | 33.8 | 9,352 | 5,450 | 43 | 83 | 89.3 | 84.4 | 3,267 | 62 | 301,094 | 4,192,256 | 0 | NO | — | yes | yes | 411 | 14,675 | mke2fs 1.47.2 (1-Jan-2025) |
| xfs/single | 358 | 6,385 | 8,484 | 7.83 | 22.7 | 7,221 | 9,768 | 416 | 1.55 | — | 28,605 | 2 | 5,311 | 1,439 | 1,643 | 807 | 88.5 | 0 | 0.15 | 2,635 | 67 | 1,126 | 326 | 2,776 | — | — | — | — | — | — | 4 | 71.0 | 19.3 | — | — | — | — | — | 179 | 157 | — | — | — | — | — | — | yes | yes | yes | 412 | 14,689 | mkfs.xfs version 6.18.0 |
| xfs/md-raid10 | 173 | 2,944 | 6,654 | 35.4 | 39.1 | 5,646 | 18,999 | 334 | 1.93 | — | 4,239 | 12 | 4,111 | 1,135 | 872 | 532 | 49.2 | 0 | 0.51 | 1,319 | 74 | 692 | 196 | 1,244 | — | — | — | — | — | — | 5 | 40.5 | 18.7 | — | 9,835 | 6,001 | 87 | 167 | 90.7 | 93.6 | — | — | — | 4,194,304 | 0 | yes 

# Why I Think You Should Almost Never Use AI to Write Anything Substantive

## 评论（22/22）

**farlight** · 2026-09-19T18:11:40.000Z：

https://github.com/fenio/modern-fs-benchmark

**Farmadupe** · 2026-09-19T18:48:47.000Z：

@farlight assuming that you're the creator do you think you'd be able to rework the HTML/CSS? I'm sure you've got good data but speaking on behalf of my eyeballs, the results page is... hard to read!

**skerit** · 2026-09-19T18:49:06.000Z：

Oh, so bcachefs is doing pretty well.

**blop** · 2026-09-19T18:54:50.000Z：

For peace of mind I'm still using zfs (since the last 15+ years) but I'm definitely not impressed by the performance...

**loeg** · 2026-09-19T19:01:24.000Z：

What is md-raid10 doing that is so much worse than lvm-raid10? In terms of "I/O" and "responsiveness." It's not really obvious to me from either the linked page or https://github.com/fenio/modern-fs-benchmark . In principle they should be similar?

**Farmadupe** · 2026-09-19T19:05:19.000Z：

> CI runs use loop devices on shared ephemeral VMs (one VM per filesystem): compare shapes and ratios, not absolute MB/s. Each job records a host-calibration anchor — see the table.I think if you're not using baremetal for such tests, it's likely that the results are simply not comparable at all? What if another tenant is also using the disk?

**blop** · 2026-09-19T19:19:39.000Z：

I think the reviews should also include the social aspect of these filesystems...There is and have been many promising and exciting FS to replace the old boring ones, but for storage you not only want to avoid technical issues but also maintainer(s) drama...

**markhahn** · 2026-09-19T19:30:07.000Z：

what does "integrity" fail mean in the first table? that the case didn't recover from the 2G corruption?

**sippingabonedry** · 2026-09-19T19:36:39.000Z：

So two filesystems that are essentially shunned from the Linux kernel and permanent second-class citizens, and one that is a ticking time bomb. Oh boy which do I choose?I'm saying ZFS on another OS.

**Farmadupe** · 2026-09-19T18:53:11.000Z：

> 2G of random garbage is written directly onto one member device (behind the filesystem's back, offset 1G — python injector; uutils dd mis-seeks on dm devices), caches dropped, then a full scrub: btrfs scrub -B, zpool scrub + wait, bcachefs scrub, md/lvm sync-action 'check' (which can only COUNT mismatches — no checksums to know which copy is right).I'm not sure that nuking 2G of the underlying block device is a recoverable error on any filesystem that I'm aware of? Can you confirm if any ofthe filesystems really came out of the other side in a usable state after scrubbing?-----> Trivial-op p99, idle (ms) # A trivial operation — one 4k write + fsync every 200ms (like a shell appending history or an editor updating its swap file) — run alone for 10s. p99 of the fsync completionIn fact, if it's OK for me to ask, are any of the metrics tht you used standard industry metrics? It looks like several of the tests are bypassing the kernel's page cache? -- which I worry may fall into the trap of "I modified the system to be unrepresentative of reality and then tested it".----> kernel 7.0.0-1012-azureCan you confirm if you tested on a bare metal machine? were you the only tenant?

**tarruda** · 2026-09-19T18:59:59.000Z：

Except for the fact that the developer has sabotaged the project into being removed from mainline?

**slyfox125** · 2026-09-19T18:58:48.000Z：

Different tools for different jobs; use ZFS for your data store and ext4 for your primary drive.

**walrus01** · 2026-09-19T19:11:19.000Z：

It's a fair point but it's also possible the person running the tests has a dedicated test hypervisor for this , so that different configurations of filesystems and VMs can be created and destroyed quickly in an automated manner.If it's something as simple as a KVM hypervisor that only runs 1 test VM at a time (with no other load from anything else other than the basic systemd daemons, ssh daemon etc running on the hypervisor), the results could be very close to bare metal.I can see it being very time consuming and annoying to do repeated manual bare metal OS installs and new partitioning/filesystem creation for such a large variety of tests.The author does also say that performance isn't really the main thing but rather, data integrity:https://github.com/fenio/modern-fs-benchmark

**vlovich123** · 2026-09-19T18:56:29.000Z：

1 device out of the replica set I’m assuming so all of them should recover.

**hlieberman** · 2026-09-19T18:59:17.000Z：

The integrity check is only on the tests which are either RAID or the filesystem equivalent.

**AceJohnny2** · 2026-09-19T19:15:17.000Z：

that's not necessarily a sabotage.

**tombert** · 2026-09-19T19:32:17.000Z：

It's relatively easy to get it working as a kernel module at least. I got it set up on a NixOS box without too much trouble.

**irusensei** · 2026-09-19T19:36:58.000Z：

That might be the best thing happened to the project since now development can happen at its own pace without the clicky bait influencers.In fact they delivered the erasure coding for parity raid back in march this year.The thing is that as soon as you seriously give a chance to Bcachefs you see how good it is. I can only tell you that mixing different device tiers and having a per-file/directory replication setting is a god send specially in these times where storage costs more than gold.

**blop** · 2026-09-19T19:14:16.000Z：

yes indeed, zfs for my nas basically

**Farmadupe** · 2026-09-19T19:20:55.000Z：

> compare shapes and ratios, not absolute MB/sIn this case, given that the author's own disclaimer (above) already disclaims the numeric readings, I'm not sure how it's possible to make any inference on "shapes and ratios" derived from the numeric readings.

**toast0** · 2026-09-19T19:22:39.000Z：

> I can see it being very time consuming and annoying to do repeated manual bare metal OS installs.Well don't do that then. There's lots of other options. Probably the simplest is a single bare metal install on a simple filesystem on one device. run the filesystems under test on other storage dedicated to testing.You could also boot into a network install and use local storage exclusively for testing.

**Farmadupe** · 2026-09-19T19:25:33.000Z：

Yes exactly. The issueThe epherrality of the VMs isn't an issue, it's the _shared_ part that's the concern here. Going by the fact that the kernel is listed as "kernel 7.0.0-1012-azure" I feel like it's a fair risk that there may have been noisy neighbours.

## 关联链接

- https://bartosz.fenski.pl/modern-fs-benchmark/
