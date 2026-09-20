---
type: "corpus"
item_id: "8a7c55ea364b5395"
title: "How I went from a Word document to my own local-first password manager for Android"
source: "reddit"
source_name: "Reddit 独立开发版块"
url: "https://www.reddit.com/r/buildinpublic/comments/1tsxpcl/how_i_went_from_a_word_document_to_my_own/"
project_url: "https://play.google.com/store/apps/details?id=com.nick.applab.silentsaver"
author: "Azaria77"
published_at: "2026-05-31T23:01:40+08:00"
captured_at: "2026-09-21T03:01:55+08:00"
lang: "en"
kind: "post"
topic: "开发者工具"
shard: "2026-09-21"
pub_day: "2026-05-31"
tags:
  - 语料
  - reddit
  - r/buildinpublic
metrics: {"score": 3, "comments": 3, "upvote_ratio": 1}
comments_count: 3
comments_total: 3
discovered_via: "reddit:144d+settle3"
---

# How I went from a Word document to my own local-first password manager for Android

> [!info] 一句话导读
> Hi ! i’m an indie dev and I wanted to share the journey of building my app, Keyri — a strict local-first digital vault for Android.

> [!meta]- 语料信息（点开展开）
> 来源：Reddit 独立开发版块（post）
> 原帖：<https://www.reddit.com/r/buildinpublic/comments/1tsxpcl/how_i_went_from_a_word_document_to_my_own/>
> 指标：得分=3 · 评论=3 · 赞踩比=1
> 作者：Azaria77　|　发布：2026-05-31T23:01:40+08:00
> 项目链接：<https://play.google.com/store/apps/details?id=com.nick.applab.silentsaver>
> 采集：2026-09-21T03:01:55+08:00　|　id：`8a7c55ea364b5395`

## 正文

Hi ! i’m an indie dev and I wanted to share the journey of building my app, Keyri — a strict local-first digital vault for Android.

**The Problem: Privacy vs Convenience**

I’ve always been pretty paranoid about privacy. For years, I refused to use cloud-based password managers (and seeing breaches at major companies didn’t exactly help).

So my solution was… honestly terrible.

I kept all my passwords inside a password-protected zipped Word document stored only on my PC.

And because I was also terrified of losing everything, I kept a backup copy on a USB drive too.

This made the whole process even more painful:

every password update had to be manually synchronized between the PC copy and the USB backup.

Every time I needed to log into something on my phone or update a password, I had to:

\- boot up my PC

\- unzip the file

\- enter the master password

\- search for the entry

\- update it manually

\- remember to update the USB backup too.

At some point I realized I desperately needed a mobile solution, but I still didn’t want my sensitive data sitting on someone else’s servers.

**The Journey: From Python Script to Flutter App**

I’ve always loved coding, but never really had the time to go deep into app development. So I used this problem as an excuse to finally learn.

The first version of Keyri was actually just a local Python script running on my PC. It worked, but it obviously didn’t solve the mobile problem.

That’s when I decided to learn Flutter.

I spent months rebuilding the logic into a proper Android app during evenings and weekends. As I kept adding features for myself, I realized there were probably other privacy-focused people looking for a completely local alternative too.

So eventually I polished it up and published it on the Play Store.

**Technical Challenges & Lessons Learned**

here are a few interesting problems I had to solve without relying on a backend:

Handling images locally

I wanted users to store ID cards, receipts, and sensitive documents. Images are compressed on-device, encrypted locally using ChaCha20, and stored entirely inside the app sandbox.

Password breach checks without exposing passwords

I integrated the HaveIBeenPwned API using k-anonymity. Passwords are hashed locally and only the first 5 hash characters are sent. The real password never leaves the device.

Barcode & QR scanning

I used Google ML Kit for barcode scanning while ensuring image processing stays entirely on-device.

Data migration without cloud sync

Since there’s no traditional cloud account system, I built encrypted JSON backup/import support and CSV import tools to migrate from browsers like Chrome.

Google Drive Backup \[NEW\] I’ve just rolled out optional encrypted backup integration with Google Drive. The challenge was keeping the app’s local-first philosophy intact. I designed it so that your data is already encrypted on-device before being uploaded and so not even Google has access to your data.

**What the app does today**

Keyri is now a full local-first digital vault for:

\- passwords

\- cards

\- barcodes/qrcodes

\- encrypted images

It also includes:

\- biometric unlock

\- Android Autofill integration

\- local breach checks

\- encrypted backups (now with Google Drive support)

\- zero ads

\- zero tracking

\- zero accounts

Play Store Link:

[https://play.google.com/store/apps/details?id=com.nick.applab.silentsaver](https://play.google.com/store/apps/details?id=com.nick.applab.silentsaver)

I’d genuinely love to hear your feedback, especially from people who care about privacy, security, or local-first software.

Thanks for reading!

## 评论（3/3）

> **Mission-Giraffe-7972**（1 分） · 2026-06-01T09:57:41+08:00　
> What specific algorithms or similarity metrics (e.g., Levenshtein distance, entropy calculations) did you implement to determine the strength of each pass?

---

> **Azaria77**（1 分） · 2026-06-01T16:28:42+08:00　
> It's a simple zxcvbn algorithm

---

> **LeaderAtLeading**（1 分） · 2026-06-01T22:28:53+08:00　
> Local first for passwords is the right call. Cloud breaches prove the market exists.

## 导航

- 项目页：[[10-项目/play.google.com_889ad790]]
- 渠道页：[[50-渠道/reddit]]
- 赛道：`开发者工具`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
