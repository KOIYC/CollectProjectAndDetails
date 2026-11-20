---
type: "corpus"
item_id: "5ebd9b0437bdd32b"
title: "Best Backup Strategy for My Home Server?"
source: "reddit"
source_name: "Reddit 独立开发版块"
url: "https://www.reddit.com/r/selfhosted/comments/1xs1ry3/best_backup_strategy_for_my_home_server/"
author: "Kooky_Big_4741"
published_at: "2026-11-10T03:51:00+08:00"
captured_at: "2026-11-20T09:47:05+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-11-20"
pub_day: "2026-11-10"
tags:
  - 语料
  - reddit
  - r/selfhosted
  - Need Help
metrics: {"score": 10, "comments": 31, "upvote_ratio": 0.8571428571428571}
comments_count: 27
comments_total: 31
discovered_via: "reddit:14d+settle10"
---

# Best Backup Strategy for My Home Server?

> [!info] 一句话导读
> I'm looking for advice on setting up a reliable, automated backup system for my Debian home server. I recently bought three additional 500 GB HDDs and I'm tryin…

> [!meta]- 语料信息（点开展开）
> 来源：Reddit 独立开发版块（post）
> 原帖：<https://www.reddit.com/r/selfhosted/comments/1xs1ry3/best_backup_strategy_for_my_home_server/>
> 指标：得分=10 · 评论=31 · 赞踩比=0.8571428571428571
> 作者：Kooky_Big_4741　|　发布：2026-11-10T03:51:00+08:00
> 项目链接：—
> 采集：2026-11-20T09:47:05+08:00　|　id：`5ebd9b0437bdd32b`

## 正文

Hi everyone,

I'm looking for advice on setting up a reliable, automated backup system for my Debian home server. I recently bought three additional 500 GB HDDs and I'm trying to figure out the best way to use them.

**My server:**

Lenovo ThinkCentre M710q Tiny

Intel Celeron G3930T (2C/2T)

16 GB RAM, Debian 13

Main drive: 500 GB WD Black 7200 RPM HDD

Additional drives: 3× Seagate BarraCuda 500 GB 5400 RPM (SMR)

Around 38 Docker containers, including Immich, Nextcloud AIO, Jellyfin, RomM, Sonarr, Radarr, Seerr, Pi-hole and others.

Everything currently runs from the main WD Black HDD, including Docker, databases and media files. I plan to keep all active services there.

**My planned setup**

**HDD 1 — Daily backup:** Always connected, automatic incremental backups with versioning.

**HDD 2 — Weekly backup:** Normally disconnected. I'll connect it every weekend, run a backup, then safely disconnect it.

**HDD 3 — Cold storage:** Rarely accessed files and archives, without continuous read/write activity.

I don't want RAID(in case tell me why should i use It). Both backup drives should contain independent, recoverable copies.

**What I want to back up**

**Immich:** Original photos/videos, PostgreSQL database and metadata.

**Nextcloud AIO:** User files, database and configuration.

**Docker:** Compose files, persistent configurations and databases for Jellyfin, Seerr, Sonarr, Radarr, RomM and other containers.

I **don't need to back up** Jellyfin movies/TV shows, RomM game files, torrents or other easily recoverable content.

My priority is protecting personal files and application configurations.

**What would you recommend?**

I've been considering **Backrest/Restic, Kopia, BorgBackup and Duplicati**, but I'm not sure which would fit best.

A few questions:

What's the best tool for managing two independent backup drives with different schedules?

Can backups start automatically when I connect the weekly USB HDD?

How should I handle consistent backups of Immich and Nextcloud databases?

Should I use Nextcloud AIO's built-in BorgBackup alongside another tool?

Are there any concerns about using SMR HDDs for incremental backups?

I'd prefer something **open-source, self-hosted, with a web UI**, and relatively easy to maintain.

Thanks for any advice!

## 评论（27/31）

> **asimovs-auditor**（1 分） · 2026-11-10T03:51:15+08:00　
> Expand the replies to this comment to learn how AI was used in this post/project.

---

> **Kooky_Big_4741**（1 分） · 2026-11-10T03:52:44+08:00　
> Ai was used to translate some parts of the text, as my English Is not very good

---

> **vogelke**（2 分） · 2026-11-10T03:58:29+08:00　
> I've installed restic and tried it out -- works fine.
>
> For a nice comparison:
> https://stickleback.dk/borg-or-restic/

---

> **TheKitof**（1 分） · 2026-11-10T04:03:07+08:00　
> I think I tested them all. I kept Restic/Backrest. More user-friendly, more efficient, more reliable.

---

> **cachodjc**（1 分） · 2026-11-10T04:04:59+08:00　
> Zerobyte

---

> **TheKitof**（1 分） · 2026-11-10T04:09:18+08:00　
> You literally mentioned it in your original post

---

> **Kooky_Big_4741**（1 分） · 2026-11-10T04:15:51+08:00　
> My bad, i've made the draft days ago and totally forgot about that Sorry, now i Remember what It is

---

> **themouseandthemask**（2 分） · 2026-11-10T04:16:17+08:00　
> Backrest container and a backblaze B2 bucket. Makes the backup process so easy. I back up my complete immich library, all container settings and config and all other local db data encrypted. Snapshots allow you to view backup states nicely in the backrest ui too. I'd say go for this, sitting at about 2 cents a day for this storage.

---

> **wvraven**（4 分） · 2026-11-10T04:17:17+08:00　
> I restic all of my backups to my NAS in a backup folder.  That folder then gets synced to b2.  One nice thing is that b2 can be accessed directly from restic instead of the nas as long as I have a backup of all my keys.  Make sure you have your key's backed up...   I keep mine in a password manager and printed.
>
> If you want you could rotate one of your three drives into a safety deposit box.  They're usually pretty cheap.   One drive always online, one at home offline, third drive in the box.   If you rotate them weekly that would mean you lose at most three weeks worth of data.  A safety deposit box is also a great place for a printed copy of your key's and master passwords.  Basically a break glass in case of emergency way to recover data if you lose everything.
>
> Combine that with a cloud based backup configured with object locking and you're pretty solidly covered against things like crypto lockers or whatever as well as catastrophic damage to your home or system.
>
> My compose files are controlled in gitlab and my repos are backed up nightly.   In docker I have a script that backups up important data volumes for things I actually care about.  That scripts shuts down each container before backing up it's data volumes which is fine for the databases I need to protect.
>
> If you have databases running elsewhere you will want to either use their native tools to export data or script shutting down/backing up those files.  You should not backup a running database unless it has a native tool that supports doing so safely.
>
> Make sure you periodically test restoring from your backups, otherwise you don't really have backups.

---

> **npeeters**（3 分） · 2026-11-10T04:20:02+08:00　
> How much of you main drive is in use? Because when it’s almost full and you only have 500 GB for backups as well, you won’t be able to keep lots of snapshots.
>
> How important are the files you store? Especially your Nextcloud and Immich files? Maybe think about doing an offsite backup, just in case. Following the 3-2-1 rule.
>
> So what I would do: use two drives as local backup targets. Either create one large volume across both or separate by topic: one for half of the services and one for the other have. Make daily backups and keep x daily, y weekly, …
>
> Then do an offsite backup of the files you think are most important. Either bring the third drive to a friend or rent some storage online. You should be able to get 1TB for <5$ a month. When using restic or borg, everything is encrypted.
>
> Regarding AIO: I personally use the build in both backup of aio. Works great for me and I trust the Nextcloud team more than myself to do it right.

---

> **Adventurous_Sun_4768**（1 分） · 2026-11-10T11:57:38+08:00　
> SMR is fine for what you're planning. Incremental backups are mostly sequential writes, which is what SMR handles well — the pain is random rewrites, and that's mostly restic prune/repack or Borg compaction churning through the repo. So two habits: run prune/forget on its own, not while a backup is writing, and don't panic if a prune takes much longer than the backup itself — that's the SMR tax, not a dying disk. Your no-RAID plan is the right call here too, SMR rebuilds are where those drives really fall apart.

---

> **nicktheone**（1 分） · 2026-11-10T15:55:25+08:00　
> If I may, I initially had a setup like yours, where I used Backrest to backup to a folder on a HDD and then the backup was synced to my Storage Box with Hetzner. Then one day I fucked up some stuff on my system without realizing and the backup got corrupted and the script I used happily synced the corrupted data to my cloud instance. This way I lost a few days of stuff.
>
> I think it'd be much better if you connected restic directly to B2 and just replicated the job you already have only with B2 as a target. This way you'll have to independent backups.

---

> **wvraven**（2 分） · 2026-11-10T20:14:07+08:00　
> It’s certainly something that could happen.   That’s where versioning, lifecycle management, object locking, and integrity checks come into play.   First, I keep 30 days of versioned backups to guard against this kind of issue.   My backup scripts also do targeted test restores to verify backup integrity on the NAS.

---

> **nicktheone**（1 分） · 2026-11-10T20:20:49+08:00　
> I definitely need to implement some form of automated test restore! It's something that I keep postponing again and again. Do you have any resource to start researching the best way of doing it? I'm especially interested in checking the integrity of my Immich backups. I also regularly check the integrity of my whole backup (10% every week). Do you recommend more?
>
> As for my approach, I know it's more computationally intensive because it means running two different chains of backups parallel to each other but I feel safer knowing that I'm not copying over to my cloud any possible corruption, even with all the possible safeguards.

---

> **Dhanni-Asmus**（1 分） · 2026-11-10T21:58:55+08:00　
> Are you planning to stop the containers during the daily window, or just run hot backups? With 38 containers on a spinning disk, running heavy deduplication at the same time as live database writes might bottleneck your disk I/O pretty hard

---

> **Kooky_Big_4741**（1 分） · 2026-11-10T22:51:28+08:00　
> I Will stop them during night for a backup

---

> **wvraven**（2 分） · 2026-11-11T00:27:44+08:00　
> I restore targeted files and compare a hash of the production file against a hash of the restored file.  I do it this way so I can compare non text files.   I don't specifically test images since I handle those backups differently but it should work for you with immich.  Just pick one or two random images to restore and compare.
>
> You could list your images and grab two or three older file names and two or three of the latest file names so you get a good mix to check.

---

> **nicktheone**（1 分） · 2026-11-11T00:28:44+08:00　
> Thank you for the idea!

---

> **wvraven**（2 分） · 2026-11-11T02:39:47+08:00　
> I had a moment at lunch so I dug out the code for my verification step on docker.  It always verifies the stack file plus a couple random files.  Use or abuse at your own risk.
>
> The function:
> verify\_snapshot() {
>
> local dir=$1 name=$2; shift 2
>
> local snap tmp f rc=0
>
> local -a fixed=() sample=() inc=()
>
> snap=$(restic snapshots --host "$HOST\_SHORT" --tag "stack:$name" --latest 1 --json |
>
> jq -r 'max\_by(.time).id') || return 1
>
> for f in "$dir"/{compose.yaml,compose.yml,docker-compose.yaml,docker-compose.yml,.env}; do
>
> \[\[ -f $f \]\] && fixed+=("$f")
>
> done
>
> mapfile -t sample < <(timeout 30 find "$@" -xdev -type f -size -50M 2>/dev/null | shuf -n 2)
>
> for f in "${fixed\[@\]}" "${sample\[@\]}"; do inc+=(--include "$f"); done
>
> tmp=$(mktemp -d /var/tmp/backup-verify.XXXXXX)
>
> restic restore "$snap" --target "$tmp" "${inc\[@\]}" >/dev/null || { rm -rf "$tmp"; return 1; }
>
> for f in "${fixed\[@\]}"; do
>
> \[\[ $(sha256sum <"$f") == $(sha256sum <"$tmp$f" 2>/dev/null) \]\] ||
>
> { log "  VERIFY FAIL (fixed): $f"; rc=1; }
>
> done
>
> for f in "${sample\[@\]}"; do
>
> if \[\[ ! -e $tmp$f \]\]; then log "  verify: sample not in snapshot (excluded?): $f"
>
> elif \[\[ $(sha256sum <"$f") != $(sha256sum <"$tmp$f") \]\]; then log "  VERIFY FAIL (sample): $f"; rc=1
>
> fi
>
> done
>
> rm -rf "$tmp"
>
> return $rc
>
> }
>
> Then after the backup while the container is stopped I call:
> (( rc == 0 || rc == 3 )) && ! verify\_snapshot "$dir" "$name" "${paths\[@\]}" && FAILED+=("verify:$name")

---

> **Responsible_Mud_6209**（1 分） · 2026-11-11T03:08:40+08:00　
> For the weekly USB disk, make the job check that the disk is actually mounted before it starts. If the disk is missing, the mountpoint can just be an ordinary folder on your main drive, and a script may happily write the 'backup' there instead. Mounting by UUID and checking the expected device before running the job would be worth adding whichever backup tool you choose.

---

> **nicktheone**（1 分） · 2026-11-11T06:56:07+08:00　
> I'll try it tomorrow. Thank you!

---

> **alexwbaule**（3 分） · 2026-11-11T19:59:26+08:00　
> Two things before the drive rotation. All three disks in the same box protect you from a disk failure but not from theft, fire or a power surge, so I'd make one of them (the weekly one) live somewhere else, or at least in a different room. I'd use restic or borg rather than plain rsync, since you get versioning and deduplication, and with 500 GB drives that matters. For the databases (Immich's Postgres, Nextcloud), don't just copy the live files. Nextcloud AIO has a built-in borg backup you can point at a mounted drive, and Immich writes its own DB dumps that you can include. The SMR drives are fine for sequential backup writes, but I'd avoid RAID or ZFS resilvering on them. Also, I'd leave out anything re-downloadable like the arr media so it all fits in 500 GB.

---

> **TheFlyingJeff**（1 分） · 2026-11-12T01:04:10+08:00　
> Restic and backrest is great, I'm a little more cloud based and I'm not storing that much data.
>
> I back up everything thing to backblase, storing 16gb for the past few months has cost technically £0.25  but actually 0 as it's under the charge amount.
>
> It depends on how much data you think actually needs backing up.

---

> **Kooky_Big_4741**（1 分） · 2026-11-12T03:55:49+08:00　
> Well in my case i have more then 100GB of videos and photos to backup

---

> **Kooky_Big_4741**（1 分） · 2026-11-12T03:59:03+08:00　
> Currently i have a bit more of 100GB of files to backup, the others are series and films from Jellyfin, wich i have no interest in backing up. Also i think i Will use One hdd for Daily backups with restic and the other One for weekly backups, and maybe in the future I Will try backblase

---

> **Kooky_Big_4741**（1 分） · 2026-11-12T04:02:50+08:00　
> I think I Will follow your suggestion, also i will think about moving the second hdd to another place. Thanks for helping

---

> **ShemarMarks**（1 分） · 2026-11-13T21:46:53+08:00　
> The hash check is handy. I’d also try restoring the DB and media into a separate Immich instance, then open a few photos from different dates. In my own restore lab, the app came up fine on the replacement server.

## 导航

- 项目页：—（本条不是项目，按设计不建实体页）
- 渠道页：[[50-渠道/reddit]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
