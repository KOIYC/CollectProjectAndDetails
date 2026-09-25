---
type: "corpus"
item_id: "b48e4e470507e26c"
title: "Stamp Image Cropper"
source: "indiehackers"
source_name: "Indie Hackers 产品库"
url: "https://www.indiehackers.com/product/stamp-image-cropper"
project_url: "https://alstamps.com/image-cropper"
captured_at: "2026-09-25T00:00:28+08:00"
lang: "en"
kind: "project"
topic: "AI 工具/Agent"
shard: "2026-09-24"
tags:
  - 语料
  - indiehackers
metrics: {}
comments_count: 0
comments_total: 0
discovered_via: "ih:products"
---

# Stamp Image Cropper

> [!info] 一句话导读
> Home Starting Up Case Studies DB Products Ideas DB Vibe Coding Tools Subscribe to IH+

> [!meta]- 语料信息（点开展开）
> 来源：Indie Hackers 产品库（project）
> 原帖：<https://www.indiehackers.com/product/stamp-image-cropper>
> 指标：—
> 作者：—　|　发布：—
> 项目链接：<https://alstamps.com/image-cropper>
> 采集：2026-09-25T00:00:28+08:00　|　id：`b48e4e470507e26c`

## 正文

Home Starting Up Case Studies DB Products Ideas DB Vibe Coding Tools Subscribe to IH+
Starting Up Case Studies
 Ideas DB Products DB Sign in Join
Stamp Image Cropper
 Turn flatbed stamp scans into individual cropped images
Visit Website
Stamp Image Cropper Turn flatbed stamp scans into individual cropped images
 Post 1
 Revenue $0 / mo
 Website
September 22, 2026
 I built a stamp image cropper that turned a 10-15 minute job into under 20 seconds
I sell stamps on eBay. A single full A4 flatbed scan can contain around 15–20 stamps, and cropping, straightening and saving them as individual images used to take me 10–15 minutes.
 It is a necessary part of preparing listings, but it is also repetitive. Every batch involves essentially the same process: find each stamp in the scan, crop it consistently, correct any slight rotation and save it separately.
 So I built a Python desktop tool to automate that part of the workflow.
 The tool uses OpenCV and Pillow to identify individual stamps placed against a black background, separate them, correct minor rotation and create consistently cropped images.
 Under normal conditions, a full A4 scan containing around 15–20 stamps that might take me 10–15 minutes to process manually can now be completed in less than 20 seconds.
 That was enough to make the tool worthwhile before anyone else could use it. Saving roughly 10 minutes on a job I repeat regularly adds up quickly.
 Turning the desktop tool into a web utility
 Once the desktop version was working well in my own workflow, I decided to adapt it into a browser-based version.
 The aim was to let other stamp collectors and sellers use the same process without installing Python or image-editing software. I wasn’t trying to invent a different cropping system for the website. I wanted to retain the core process that I was already using.
 I treated the desktop tool as the reference implementation. While adapting it, I used reference scans and known-good outputs to check that moving the processing online had not silently changed the cropping behaviour.
 The resulting workflow is deliberately simple:
 1. Scan several stamps together against a black background.
 2. Upload the scan.
 3. The cropper identifies and separates the stamps.
 4. It corrects minor rotation.
 5. It creates the individual JPEG images.
 6. It returns them together in a ZIP file.
 There are no accounts, no registration and no software to install. The live cropper is here for anyone wanting to try it:
 https://www.alstamps.com/image-cropper/
 The web architecture
 I kept the web implementation relatively small.
 The existing Python processing sits behind a Flask API, served by Gunicorn and hosted on Heroku. The public interface is part of my existing WordPress site, but the WordPress server does not handle the image processing.
 Broadly, the flow is:
 WordPress/browser interface → Python API on Heroku → crop and straighten images → create ZIP → return ZIP to the browser
 Temporary upload and output files are deleted automatically after processing.
 There is no AI dependency. It is the same core image-processing approach as the desktop tool, made accessible through a browser.
 Narrow constraints are fine
 The cropper works best when the input follows a few straightforward rules:
 - Use a black background.
 - Leave visible gaps between the stamps.
 - Keep the stamps reasonably square and upright.
 - Preferably scan at 600 dpi.
 It can handle minor rotation, but it is not intended to straighten stamps placed at arbitrary angles or rescue a badly arranged scan.
 That limitation became part of the design rather than something I needed to eliminate. The tool does not have to solve every possible image-segmentation problem. It needs to solve the particular job it was built for reliably.
 The other useful lesson for me was that the tool proved its value before it became a public web project. I did not start with plans for a SaaS, user acquisition or a large potential market. I had a repetitive bottleneck in an existing business workflow, built something to remove it and measured a clear time saving.
 Only after that did I consider making it available to other people.
 I have made the web version free because I originally built the cropper for myself, and there seemed little point keeping it entirely private once I had adapted it for browser use. Other collectors and stamp sellers may have the same repetitive task, and the tool costs them nothing to try.
 I’m curious what other indie builders would do with a utility this narrow: keep it as one focused free tool under the existing specialist website, or build a small collection of related tools around the same workflow?
Dan Williams
4 Likes
5 Comments
Say something nice…
Post Comment
1
“Thanks for sharing this. I’d be interested to know how you measure whether your SEO efforts are actually bringing qualified visitors.”
Aurangzeb
·
2 days ago
 ·
Reply
1
“This is helpful. Do you think the strategy works equally well for new websites, or does it depend on having some existing authority?”
Aurangzeb
·
2 days ago
 ·
Reply
1
“Good point about focusing on the right audience. How did you identify your ideal customers in the beginning?”
Aurangzeb
·
2 days ago
 ·
Reply
1
“I found the customer acquisition section particularly useful. How long did it take before you started seeing measurable results?
Aurangzeb
·
2 days ago
 ·
Reply
1
Now that it's public, are collectors mainly using the cropper as a one-off utility, or are you seeing recurring usage that points toward adjacent tools?
Aryan Sinh
·
2 days ago
 ·
Reply
About
 I built it to save time in my stamp selling workflow. Cropping and straightening 15–20 stamps took 10–15 minutes; my Python tool cut that to under 20 seconds. I made the web version free for other collectors and sellers.
 People
 Dan Williams Founder
Stay informed as an indie hacker.
 Market insights that help you start and grow your business.
Subscribe
Follow @IndieHackers on X for stories and insights about founders building profitable online businesses, and to connect with others in the Indie Hackers community.
 © Indie Hackers, Inc. · FAQ · Terms · Privacy · Cookie Settings / Policy ·
Community
 Top Today Top This Week Top This Month Join
Products
 All Products Highest Revenue Add Yours
Databases
 Ideas Products Stories

## 关联链接

- https://www.alstamps.com/image-cropper/

## 导航

- 项目页：[[10-项目/Stamp-Image-Cropper_4dcbd986]]
- 渠道页：[[50-渠道/indiehackers]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
