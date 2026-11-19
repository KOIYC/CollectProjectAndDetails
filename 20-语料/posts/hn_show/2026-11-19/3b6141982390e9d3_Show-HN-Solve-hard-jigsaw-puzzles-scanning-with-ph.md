---
type: "corpus"
item_id: "3b6141982390e9d3"
title: "Show HN: Solve hard jigsaw puzzles scanning with phone"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50553969"
project_url: "https://puzzle.cloudish.app/"
author: "javierluraschi"
published_at: "2026-11-18T23:45:16Z"
captured_at: "2026-11-19T09:43:31+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-11-19"
pub_day: "2026-11-18"
tags:
  - 语料
  - hn_show
  - author_javierluraschi
  - story_50553969
  - show_hn
metrics: {"points": 2, "comments": 2, "engagement_velocity": 2}
comments_count: 2
comments_total: 2
discovered_via: "hn:show_hn:3d"
---

# Show HN: Solve hard jigsaw puzzles scanning with phone

> [!info] 一句话导读
> A jigsaw puzzle solver for the hard ones

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50553969>
> 指标：点赞=2 · 评论=2 · engagement_velocity=2
> 作者：javierluraschi　|　发布：2026-11-18T23:45:16Z
> 项目链接：<https://puzzle.cloudish.app/>
> 采集：2026-11-19T09:43:31+08:00　|　id：`3b6141982390e9d3`

## 正文

Puzzle Solver
How it works
 What to expect
 FAQ
A jigsaw puzzle solver for the hard ones
That piece fits somewhere. Your phone knows where .
Scan your pieces one at a time on a printed card. Puzzle Solver traces each outline to a fraction of a millimetre, reads all four sides, and works out which pieces lock together. It's built for the hard ones: endless sky, swirling paint, hundreds of pieces that all look alike.
Sign in to start a puzzle
 Try the demo: 54 real pieces
No app to install. Your photos never leave your phone. Open source on GitHub . Or start without an account (it stays in this browser only).
Welcome back . What are we solving today?
Start a puzzle
or open a demo catalog of 54 real pieces →
The Starry Night , Vincent van Gogh, 1889: widely considered one of the hardest jigsaw puzzles you can attempt. Shown on the outlines of 54 real pieces from our demo, placed where the solver put them.
Your puzzles
1 printed card, used for every piece
1 piece at a time, numbered as you go
<1 mm outline detail, traced on your phone
0 photos uploaded: only the outline is saved
How it works
Four steps, from pile to picture
No dumping the box on a scanner, no magic photo of the whole pile. You scan each piece on its own, so the app can measure it properly. It sounds slow, but it's what makes the matches trustworthy.
01
 Print the scan card
Before your first scan, print our scan card page . It's one sheet with four 70 mm cards, each with a thick black frame. That frame is the scanner's ruler: it tells the app exactly how big each piece is and straightens out the camera angle, so every outline comes out true to size.
Print at 100% / actual size . A 50 mm check line on the sheet lets you confirm it.
Start with the magenta card ; after each scan the app tells you if another card shows that piece more clearly.
The card is required. The scanner waits until it sees the frame.
🖨 Open the printable card
02
 Scan one piece at a time
Put one piece face up in the middle of the card and hold your phone flat above it. A level shows how you're tilted. When the frame turns green and you hold still, the photo takes itself. The light switches on automatically where your phone allows it.
The outline is traced right on your phone at full camera resolution, with shadows filtered out. You get a preview to check before you move on.
Hold it flat , within 3°: the dot has to sit inside the small circle.
Get close , so the card fills the view. The app tells you if you're too far.
Prefer your camera app? Tap 🖼 to shoot at full resolution with flash.
03
 Number it, keep it
Each scan gets the next number: 1, 2, 3… Pencil it lightly on the back of the piece, or set the piece on a numbered sticky note or in an egg-carton slot. Later, when the app says " 42 goes just left of 28 " , you'll know exactly which piece to grab.
Every piece is saved the moment you scan it , so you can stop and pick up later.
Typo? Labels can be edited, and a bad scan can be redone.
04
 Match and solve
Open any piece to see its best partners for each side, ranked by how snugly they fit. Or tap Solve and the app assembles your catalog into groups: a map of numbered pieces, each in its place, ready for you to build from.
Every side is sorted as a tab , a blank or a flat edge , so corners and border pieces are found for you.
Scan on your phone, then open the solution on a bigger screen. With an account, your puzzles follow you.
What to expect
Honest expectations
Scanning is the slow part
It becomes a rhythm: place, hold, check, number, next. Budget an evening for a few hundred pieces and split big puzzles over several sessions. Solving takes seconds.
You don't have to scan everything
Only scanned pieces can be matched, so scan the part you're stuck on: all the sky, the border, one tricky colour. A few dozen pieces from the same area is plenty to start.
Shape is everything
Matching reads only the outline, never the picture. The swirls that make The Starry Night so hard by eye don't confuse it, and neither does a plain sky. It works best with grid-cut puzzles whose pieces differ in shape (Ravensburger-style). Cuts where many pieces look identical are harder.
Groups, not guesses
The solver is careful. It only joins pieces when every touching side agrees, so expect several solid groups rather than one risky answer. On a 500-piece reference set it put 489 pieces in one group, with 99.8% of neighbours right.
Your photos stay on your phone
The image is processed on your device and then thrown away. Only the outline, a list of points, and its number are saved.
Just a browser
Open this page on a recent phone with a camera. There's nothing to install. Allow camera access when asked, and you're scanning.
Under the hood
Why one piece at a time works
With a single piece on a known card, the app can afford to be precise. It corrects perspective with the card's frame and measures in real millimetres. It separates the piece from its shadow by colour rather than brightness, then traces the edge with sub-pixel accuracy.
The four corners split the outline into four sides. Each side is checked against every other side by fitting the two shapes together and measuring what's left over, allowing for the hairline gap real neighbours have. The solver then grows groups from the most certain matches and backs out a piece if its neighbours disagree.
It's all open source, with the details in the GitHub repository .
FAQ
Good questions
Do I need an account?
 Not to look around: the demo works without one. Sign in with Cloudish to keep your catalog safe and open it on any device, for example scanning on your phone and browsing the solution on a laptop. You can also start without an account, but then the puzzle is only remembered by that browser.
Do I really have to print the card?
 Yes. The black frame is how the scanner knows the true size of a piece and corrects for the camera angle. Without it, two photos of the same piece would differ and matching would suffer. One sheet is enough for a whole puzzle; if you don't have a printer, any copy shop or library can print it.
Why one piece at a time instead of a photo of the whole pile?
 Precision. Matching depends on outlines being right to a fraction of a millimetre. One piece, centred on a known card and photographed flat at full resolution, gets there. A crowded table photo doesn't.
Which puzzles work best?
 Classic grid-cut puzzles where each piece has four sides with tabs and blanks, and the shapes vary from piece to piece. Puzzles with many identical shapes, or irregular "random cut" pieces, are much harder because shape is all the app looks at. What's hard by eye is fine: night skies, oceans, paintings like The Starry Night . That's where the app helps most.
What if a scan comes out wrong?
 You see every outline before you move on, so just scan it again. From the catalog you can also re-scan, relabel or delete any piece later.
Are my pictures uploaded anywhere?
 No. Photos are processed on your phone and then discarded. The server only receives each piece's outline and label, and uses them to compute matches.
Is it open source?
 Yes, under the MIT license. The scanner, the matcher and the solver are all on GitHub . Stars, issues and pull requests are welcome.
Clear the table. Grab a pencil. Let's find where it goes.
Sign in to start a puzzle
 Try the demo
Don't forget to print the scan card first.
Start a puzzle
 🖨 Print the scan card
Puzzle Solver
 Scan your pieces. See what fits.
How it works
 Scan card
 FAQ
Hosted on cloudish.ai . Thanks to Cloudish for hosting and sign-in.
Open source under the MIT license. The original analysis and solver, the reference solutions used for validation, and the demo pieces come from jigsawlutioner by Michael Wolf (MIT). Headings are set in Fraunces (OFL). The Starry Night by Vincent van Gogh (1889, Museum of Modern Art) is in the public domain; image via Wikimedia Commons .
1 · Scan
 2 · Catalog 0
 3 · Solve
🖨 First: print the scan card
Scanning needs the printed scan card (print at 100%). Its black frame tells the scanner the exact size of each piece and corrects the perspective. Start with the magenta card; the app tells you when another card would show a piece more clearly.
📷 Scan pieces
 Next label: 1 – you can change it in the scanner.
Put one piece face up in the middle of the card.
Hold the phone flat so the card fills the view. When its frame turns green and you hold still, the photo is taken automatically (or tap ●).
Check the outline, write the number on the back of the piece, tap Next piece .
For the sharpest edges: soft light or the 🔦 light (shadows are removed, but less shadow is better), or 🖼 to take the photo with your phone's camera app at full resolution.
All
 Corners
 Edges
 Inner
 Failed
⤓ export
Solve puzzle
 Match 3 pieces
run
 labels
 changes
 match quality
 single pieces
 zoom
 find
×

## 评论（2/2）

> **javierluraschi** · 2026-11-18T23:45:41.000Z　
> I got a super hard jigsaw puzzle and got frustrated by it. I tried some of the apps and services out there but nothing worked, mostly cause this puzzle was close to single color so the only way to match the pieces was by shape.This project started with an existing PHP solver (https://github.com/byWulf/jigsawlutioner) but after trying it many things were broken, the phone outlines not accurate enough, I found out direct geometric side matching worked better, so I rewrote it from scratch (with AI obviously) in plain Node with no deps and used the old results just as a reference.Scanning took the most time. Problem was that live segmentation overheated the phone, so I changed it so it only finds the card live and does the outline after the photo.Shadows were bad as well, part—early edges included dark crescents and came out 7-9% too big. So switched to printing a PDF to scan the cards and then also change snapping the edge at full res.Ended up printing a few card colors because some pieces vanish against certain backgrounds, but then found out most reliable to scan the pieces from the back for consistency.Assembly is strongest-first with some local backtracking when groups almost close but conflict.There’s a 54-piece demo that solves cleanly; it also does okay on a 1000-piece set.Still rough on pieces that are close in color to the card, and the gap can be sensitive to how you scan.The “match these three pieces” thing was added later for when you just want the missing corner of a 2x2 ranked. Which was useful cause even this algorithm was not able to match everything.The last few pieces of the puzzle I matched them by hand (so this project won’t match all the pieces) but that was the remaining 10% of the puzzle and was quite fun and enjoyable.Repo: https://github.com/javierluraschi/puzzle

---

> **javierluraschi** · 2026-11-18T23:47:36.000Z　
> Here is a timelapse worth sharing: https://x.com/javierluraschi/status/2113799709911634272

## 导航

- 项目页：[[10-项目/puzzle.cloudish.app_22cc655d]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
