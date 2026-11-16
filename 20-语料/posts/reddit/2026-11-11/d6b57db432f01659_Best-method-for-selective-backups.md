---
type: "corpus"
item_id: "d6b57db432f01659"
title: "Best method for selective backups?"
source: "reddit"
source_name: "Reddit 独立开发版块"
url: "https://www.reddit.com/r/selfhosted/comments/1xkuvdz/best_method_for_selective_backups/"
author: "joninjax1"
published_at: "2026-11-01T13:18:11+08:00"
captured_at: "2026-11-11T13:38:46+08:00"
lang: "en"
kind: "post"
topic: AI 工具/Agent
shard: "2026-11-11"
pub_day: "2026-11-01"
tags:
  - 语料
  - reddit
  - r/selfhosted
  - Need Help
metrics: {"score": 14, "comments": 26, "upvote_ratio": 0.9375}
comments_count: 25
comments_total: 26
discovered_via: "reddit:14d+settle10"
---

# Best method for selective backups?

> [!info] 一句话导读
> I'm currently using a shell script and crontab to backup my ebooks and audiobooks to Mega using rclone, and it works, but I've got no notification built in, the…

> [!meta]- 语料信息（点开展开）
> 来源：Reddit 独立开发版块（post）
> 原帖：<https://www.reddit.com/r/selfhosted/comments/1xkuvdz/best_method_for_selective_backups/>
> 指标：得分=14 · 评论=26 · 赞踩比=0.9375
> 作者：joninjax1　|　发布：2026-11-01T13:18:11+08:00
> 项目链接：—
> 采集：2026-11-11T13:38:46+08:00　|　id：`d6b57db432f01659`

## 正文

I'm currently using a shell script and crontab to backup my ebooks and audiobooks to Mega using rclone, and it works, but I've got no notification built in, the only way I know if the job completed is to check the logs. I backup my containers using git, but I want to selectively back up my books, is a shell script the best method or is there a better way?

## 评论（25/26）

> **asimovs-auditor**（1 分） · 2026-11-01T13:18:21+08:00　
> Expand the replies to this comment to learn how AI was used in this post/project.

---

> **joninjax1**（1 分） · 2026-11-01T13:21:57+08:00　
> No AI

---

> **Previous_Tea_2250**（2 分） · 2026-11-01T13:32:32+08:00　
> Your script is a perfectly reasonable fit for a selective backup. The useful upgrade is to make it observable: send a notification only when rclone exits nonzero, and keep a dated log so a failed run is actionable rather than silent. A healthcheck-style ping or an ntfy notification can do that without replacing the script.
>
> I would also add a periodic restore test, not just a successful upload check. Pick a small file or directory, restore it somewhere temporary, and verify it opens or hashes correctly. That catches credential, retention, and restore-path surprises that a clean cron exit cannot.

---

> **ComputersGoBrr**（6 分） · 2026-11-01T13:52:42+08:00　
> Consider something like healthchecks.io, where your script pings on success. No ping? Notify.

---

> **petulantCALVADOS**（0 分） · 2026-11-01T15:36:37+08:00　
> Great idea!

---

> **vatood**（6 分） · 2026-11-01T15:59:40+08:00　
> moving to systemd timers instead of cron can help here too. it gives you much cleaner logging and you can trigger an on-failure service unit automatically whenever the backup script errors out

---

> **valinor4**（2 分） · 2026-11-01T16:30:03+08:00　
> If you are already using a lot of docker projects and also using something like portainer/arcane/komodo, you can also dockerize it.
>
> I have a docker project that uses https://github.com/aptible/supercronic to periodically run docker containers.
>
> That way I cronned a rclone container (rclone has an official image) to push everything I want to pcloud.
>
> It is a bit heavy if you only have 1 cron but fairly useful if you have several.
>
> That way you can use Arcane/Komodo system to notify you if there are issues.

---

> **nele_sauer92**（2 分） · 2026-11-01T17:20:49+08:00　
> Ran rclone backups for a year before adding anything. What caught the real problem was a wrapper that only mails me on a nonzero exit and a weekly job that restores one random file into /tmp. Three months of clean logs, then a remote flag broke and only the restore test showed it.

---

> **pixeladdie**（2 分） · 2026-11-01T19:42:36+08:00　
> I do almost the same but with restic and a file it reads from of paths to back up.
>
> For notifications I use pushover. The script reads exit codes and sends me the appropriate notification.

---

> **wvraven**（2 分） · 2026-11-01T20:32:55+08:00　
> This.  All of my restic backup scripts ping healthchecks.io.  After a certain number of backups daily success messages turn into static so message on failure with a weekly summary is much better.

---

> **TaskToAgent**（2 分） · 2026-11-01T22:53:13+08:00　
> A shell script plus cron is honestly fine here, rclone already does the selective part. A filter file keeps it tidy:
>
>     + /Ebooks/**
>     + /Audiobooks/**
>     - **
>
> then `rclone sync /data mega:backup --filter-from books.txt`. Run it once with --dry-run, and think about --backup-dir on the remote so a sync doesn't happily mirror an accidental local delete.
>
> For the notification I'd flip it around: don't wait to be told it failed, get told when it didn't succeed. End the script with a ping that only fires if rclone exited cleanly, like `rclone sync ... && curl -fsS <your ping url>`, and point it at a dead man's switch (healthchecks.io's free tier, a self-hosted Healthchecks, or an Uptime Kuma push monitor). If the ping doesn't arrive on schedule you get an alert. That also catches the case where cron itself stopped running, which a "notify on error" line never will.

---

> **ImprovementOk3074**（1 分） · 2026-11-01T22:56:22+08:00　
> a tool that seems interesting : [https://www.plakar.io/](https://www.plakar.io/)

---

> **joninjax1**（2 分） · 2026-11-01T23:34:15+08:00　
> I am certainly going to do that if I keep it running as a script, it was mainly something I threw together without much thought about long term.

---

> **joninjax1**（2 分） · 2026-11-01T23:35:59+08:00　
> I have healhchecks, I didn't think about using it for the script, that makes complete sense too, that way I have notification if it doesn't work, and I don't go looking for a non-existent backup in 6 months when something fails

---

> **PhilosopherOk3419**（1 分） · 2026-11-02T03:13:56+08:00　
> your script is fine, just make it loud when it fails. one more catch beyond exit codes: rclone can 'succeed' and copy zero files if a path moved or a mount wasn't up, so i log the transferred count and alert if it's 0 several runs in a row. keep the folder list in a separate file the script reads, so changing what gets backed up doesn't mean editing the script

---

> **joninjax1**（1 分） · 2026-11-02T08:55:02+08:00　
> I added Healthchecks to the end of the script and modified the script to use systemd timers instead of crontab

---

> **winner_68**（2 分） · 2026-11-02T09:25:58+08:00　
> I kept a script like this for my ebooks too, and the part that actually saved me wasn't a fancier tool, it was making the script tell me when it silently did nothing. I had a run once where rclone exited clean but the source path had moved, so it happily backed up an empty folder.
>
> What I ended up doing was keeping the script, but adding a quick count check at the end: compare how many files it saw against the previous run, and fail loudly if that drops sharply. I also run rclone check against the remote once a week, just on a small subset, because an upload finishing is not the same as a restore working.
>
> Are you backing up the library database or metadata alongside the books themselves? That was the bit I forgot first, and it mattered more than the files when I had to rebuild.

---

> **joninjax1**（1 分） · 2026-11-02T10:19:39+08:00　
> Just the books, metadata and db is easy enough to rebuild if I have the books.

---

> **adrianlee_dev**（2 分） · 2026-11-02T10:45:23+08:00　
> A script combined with crontab is more than enough. There's no need to switch tools. The only thing missing is being able to know immediately when a problem occurs.
>
> Here's what I do:
>
> First, check rclone's exit code in the script. If it fails, send a notification (either via email or mobile push); if it succeeds, don't send a notification.
>
> Second, I add a "failed to run on schedule" alert: after each successful backup, the script sends a request to a heartbeat address. If no request arrives within a day, an alert is triggered. This way, I can detect issues even if the cron job itself fails to run.
>
> Third, after the backup is complete, I use \`rclone check\` to compare the source and destination to ensure file consistency.
>
> Fourth, periodically, I randomly select a few books and restore them from the cloud storage to verify that they open properly.

---

> **SelfHostedStack**（1 分） · 2026-11-02T20:31:55+08:00　
> Put the file list in a single --files-from file and let restic (or borg) handle the schedule, so you stop maintaining a custom script per folder. Back up the compose files and .env separately from the media itself, and keep the media backup append-only so a bad sync cannot delete the only copy. The part most people skip is the restore test: restore one book to a temp folder once a month and add a failure-only alert, so a silent failed job does not look like a working backup.

---

> **Msl_Akshat**（3 分） · 2026-11-03T01:16:10+08:00　
> I’d keep the script if it is working for you. Rclone --include and --exclude filters can handle selecting books and folders. And use copy rather than sync if you dont want local deletions mirrored to your Mega destination.
>
> For notifications, I would use something like Watchgoose, it gives your script a URL to ping after rclone succeeds, then alerts if later pings stop arriving. That catches cron quietly stopping too without complicating your existing setup.
>
> Oh and Git is handy for Compose files but make sure the containers data is backed up separately, if you have any. I think you can use DockerHub for free to store some images.

---

> **TheFlyingJeff**（1 分） · 2026-11-03T04:55:11+08:00　
> I'm using restic and backrest and just setup gotify triggers for all the exit codes

---

> **AssociateNo3312**（1 分） · 2026-11-03T07:11:58+08:00　
> This is the way.   I have 3 different restic backup containers.  That have different schedules and source dirs.
>
> Each has their own healthchecks slug

---

> **XAckermannX**（1 分） · 2026-11-06T03:08:55+08:00　
> does it have an ios app or way for phone notifs?

---

> **ComputersGoBrr**（1 分） · 2026-11-07T14:19:11+08:00　
> You can integrate a variety of push notification services. I use gotify. Previously I used pushover.

## 导航

- 项目页：—（本条不是项目，按设计不建实体页）
- 渠道页：[[50-渠道/reddit]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
