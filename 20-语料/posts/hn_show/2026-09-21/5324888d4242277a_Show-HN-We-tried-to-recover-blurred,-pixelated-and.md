---
type: "corpus"
item_id: "5324888d4242277a"
title: "Show HN: We tried to recover blurred, pixelated and redacted text (480 cases)"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49508614"
project_url: "https://datablur.app/blog/blur-recovery-study"
author: "legitimate_key"
published_at: "2026-08-31T12:01:36Z"
captured_at: "2026-09-21T03:11:23+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-21"
pub_day: "2026-08-31"
tags:
  - 语料
  - hn_show
  - author_legitimate_key
  - story_49508614
  - show_hn
metrics: {"points": 4, "comments": 0, "engagement_velocity": 4}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:52d"
---

# Show HN: We tried to recover blurred, pixelated and redacted text (480 cases)

> [!info] 一句话导读
> Skip to content DataBlur // 3.0

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49508614>
> 指标：点赞=4 · 评论=0 · engagement_velocity=4
> 作者：legitimate_key　|　发布：2026-08-31T12:01:36Z
> 项目链接：<https://datablur.app/blog/blur-recovery-study>
> 采集：2026-09-21T03:11:23+08:00　|　id：`5324888d4242277a`

## 正文

Skip to content DataBlur // 3.0
 DataBlur AI Blur image Redact PDF Blog Pro
en
Back to blog Framework August 18, 2026 · 9 min read
 We tried to recover blurred, pixelated and redacted text. Here's what came back.
 Free browser extension
 Blur sensitive data on your screen in one click.
 100% local — no cloud, no sign-up. Works in live demos, calls, and screen recordings.
Download for Google Chrome Also available for Edge Brave, Comet Firefox
Short answer: if a screenshot gives an attacker what screenshots usually give (a known UI font, a known text size, a guessable filter), then light gaussian blur and small-block pixelation are not redaction. In our 480-case test, blur with a radius of 2 to 4 px gave the original text back exactly 92 to 100% of the time. Four-pixel pixelation gave it back 71% of the time. A 20%-opacity "transparent" overlay gave it back every single time. Saving the result as JPEG afterwards, the way a chat app does, barely helped. The only treatment that leaked nothing was a solid, flat box over the text.
 The rule that fell out of the data is simple. If the blur radius or the pixel block is smaller than about 0.3 times the font size in pixels, assume the text can be read back. At 0.4 to 0.6 times you still leak a third to a half of the characters, and for a card number or an API key that is a breach, not a blur. Recovery only dropped to chance at 0.8 times and above. By then the blur is so heavy that a solid box looks better anyway.
 Everything here is reproducible. The code, the 480 treated images and the results table are published under CC-BY; link at the end.
 Why we ran this
 "Don't blur, redact" is old advice. dheera.net made the case in 2014, Depix showed pixelated passwords being read back in 2020, and security.stackexchange has been saying it for a decade. What we could not find was a parametric answer: how much blur is enough, at what text size, and what happens after the image goes through a messenger that recompresses it. People pick a blur radius by eye. We wanted numbers.
 Method
 Samples. Six fields of the kind that actually leak on shared screens: an e-mail address, a card number, an IBAN, a phone number, an API key ( sk_live_... ) and a person's name. Each rendered in two fonts, Arial (proportional) and Menlo (monospace), at 14 px and 20 px, on a dark UI background, at 2x device pixel ratio, i.e. a Retina screenshot. That is 24 source images.
 Treatments, ten of them. Gaussian blur with sigma 2, 4, 8 and 12 px. Pixelation with 4, 8, 12 and 16 px blocks. "Transparent": text drawn at 20% opacity over the background, which some tools call a soft mask. And a solid box in the foreground colour, which we call redact. Every treated image was also saved once more as JPEG at quality 80. 24 x 10 x 2 = 480 cases.
 The attacker. We assumed what a screenshot of a known product gives away for free: the font, the size, the position of the field, and its character set (digits for a card, [a-z0-9._@-] for an e-mail). The attacker knows or guesses the treatment and its strength. Recovery is a beam search over characters: render a candidate string with the same font, apply the same treatment, compare with the target, keep the six best prefixes, extend by one character, repeat. This is the principled version of what Depix does for pixelation, and it works the same way for blur and for transparency. No machine learning, no GPU. A full run takes about 25 minutes on a laptop.
 Scoring. Character error rate (CER; 0 is perfect recovery, 1 is nothing right) and whether the recovered string matched exactly. Redact is scored as CER 1.0 by construction: every candidate renders to the same flat box, so there is nothing to compare.
 Results
 By treatment
 Transparent (20% opacity): Mean CER 0.00 · Exact recovery 100% · After JPEG q80 0.00 / 100%
 Blur sigma 2 px: Mean CER 0.00 · Exact recovery 100% · After JPEG q80 0.00 / 100%
 Blur sigma 4 px: Mean CER 0.03 · Exact recovery 92% · After JPEG q80 0.10 / 88%
 Pixelate 4 px: Mean CER 0.11 · Exact recovery 71% · After JPEG q80 0.11 / 71%
 Pixelate 8 px: Mean CER 0.49 · Exact recovery 8% · After JPEG q80 0.49 / 8%
 Blur sigma 8 px: Mean CER 0.57 · Exact recovery 21% · After JPEG q80 0.64 / 17%
 Pixelate 12 px: Mean CER 0.63 · Exact recovery 21% · After JPEG q80 0.63 / 21%
 Pixelate 16 px: Mean CER 0.83 · Exact recovery 0% · After JPEG q80 0.84 / 0%
 Blur sigma 12 px: Mean CER 0.84 · Exact recovery 4% · After JPEG q80 0.87 / 0%
 Solid redaction: Mean CER 1.00 · Exact recovery 0% · After JPEG q80 1.00 / 0%
 The transparent overlay is the one that surprised us least and worries us most. Drawing text at 20% opacity is just drawing it with less contrast. A levels adjustment brings it back, and our search got all 48 cases. Some screenshot tools offer this as a privacy mode. It is not one.
 Light blur and small pixels are fully reversible. Sigma 2 and sigma 4 blur, and 4 px pixelation, gave the text back most of the time. Not approximately. Exactly.
 JPEG does not save you. Recompression added a few errors to the sigma 4 case and changed nothing for pixelation: the blocks are large and flat, which is precisely what JPEG preserves well.
 By strength relative to text size
 Absolute numbers depend on the font size, so the useful way to read them is as a ratio of the blur sigma (or the pixel block) to the font size in pixels:
 up to 0.2: Blur: mean CER / exact 0.00 / 100% · Pixelate: mean CER / exact 0.01 / 92%
 about 0.3: Blur: mean CER / exact 0.07 / 83% · Pixelate: mean CER / exact 0.20 / 50%
 about 0.4: Blur: mean CER / exact 0.37 / 33% · Pixelate: mean CER / exact 0.42 / 8%
 about 0.6: Blur: mean CER / exact 0.80 / 8% · Pixelate: mean CER / exact 0.40-0.56 / 8-42%
 0.8 and above: Blur: mean CER / exact 0.87 / 0% · Pixelate: mean CER / exact 0.80-0.87 / 0%
 Below about 0.3 the text comes back. Between 0.4 and 0.6 it comes back partly, and partly is the dangerous region: in 46% of the 8 px pixelation runs and 33% of the sigma 8 blur runs, at least half of the characters were correct. Half of a card number, or the first twelve characters of a live API key, is not privacy. Only at 0.8 and above did results sit near chance (for a digits-only field, chance is a CER around 0.9).
 Monospace and large text are easier to recover
 Menlo at 20 px with 12 px pixelation, blocks more than half the text height, still came back with a CER of 0.02. Fixed-pitch fonts give the search a grid; larger text gives every character more pixels to leave a signature in. This matters because terminals, IDEs, log viewers and most admin tables use exactly that combination.
 By field
 Card numbers were the easiest target (mean CER 0.22, 64% exact across the blur, pixelate and transparent treatments, no JPEG): a ten-symbol alphabet and a fixed length. E-mail addresses and API keys were the hardest, at a CER around 0.47, because the search space per character is larger. "Hardest" still meant 36% of them came back exactly.
 What this means in practice
 You can act on both findings right now: our free image blur tool shows how strong a blur really needs to be, and the PDF redaction tool applies the one treatment that leaked nothing — solid, flattened redaction. Both run entirely in your browser.
 Redact, don't blur, when the content is the point. A solid box was the only treatment in this test that leaked nothing, in every font, size and compression. It is also the only one whose safety does not depend on a parameter you have to get right.
 If you must blur, go heavy and size it to the text: sigma of at least 0.8 times the font size, or pixel blocks of at least 0.8 times the font size. The ratio is what matters, not the absolute pixel count; measure both in the same units. For a 14 px UI font that is a sigma of 11 px or more, which is far heavier than any default.
 Never trust opacity. A transparent overlay is a colour change, not a removal.
 Don't count on the messenger to finish the job. JPEG recompression left pixelation untouched and blur almost untouched.
 The safest blur is the one that never hits the screen. Anything obfuscated after capture can be attacked from the captured pixels. Hiding the value before it is drawn, in the page, before the share or the recording starts, removes the pixels the attack needs. That is the approach DataBlur takes, and it is why we ran this study in the first place. For what the alternative looks like — a tool that blurs only after the page has painted — see DataBlur vs Blur It .
 This post is the data. For the how-to side — how recovery actually works and how to redact so nothing comes back — see our guide Can blurred or redacted text be recovered? .
 Limitations
 This is a known-font, known-treatment attacker. That is realistic for screenshots of common UIs, where the font and size are public, but an unusual font raises the bar. It does not remove it; the attacker can still try the likely candidates.
 Two fonts, two sizes, one background. Light themes, anti-aliasing differences and subpixel rendering will move the numbers. We do not expect them to move the thresholds much, but we have not measured it.
 No real-world noise beyond JPEG q80. No screen-to-phone photos, no video compression. Video codecs are a separate study.
 The attack is a simple beam search. Better attacks exist (learned priors, larger beams, dictionary constraints on e-mails and names). Our numbers are a floor on what an attacker can do, not a ceiling.
 We scored recovery of text the attacker expects to be there. Hidden text of unknown length is harder to locate, though the field box is usually visible in the blurred image anyway.
 Data and code
 All 480 treated images, the results table ( results.csv ) and the experiment script ( experiment.py , Python with Pillow and NumPy) are published at github.com/yochef17/blur-recovery-study under CC BY 4.0. Re-running the full matrix takes about 25 minutes on a laptop. If you extend it, with more fonts, light themes or video, tell us: support@datablur.app.
 Published by DataBlur. DataBlur is a browser extension that blurs or redacts sensitive data on a page before it is shared or recorded. We ran this study to find out how much of the word "blur" in that sentence protects anything. None of the conclusions depend on the product.
DataBlur Pro
 Keep your blurs. Drop the watermark.
 Blurring is always free. Pro saves your blur profiles, lifts the keyword-list limit and removes the watermark. One product, your choice of plan.
 See Pro plans
 Keep reading
 How to Hide Sensitive Information When Sharing Your Screen 8 min read
 ZeroBlur Alternative: Which Screen Blur Extension Should You Use? 7 min read
 What's New in DataBlur 3.0 4 min read
DataBlur // 3.0 Blur image Redact PDF Blog Pro About Privacy Terms
© 2026 DataBlur · built for privacy 100% Local | No Cloud | No AI

## 导航

- 项目页：[[10-项目/datablur.app_2341ad3d]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
