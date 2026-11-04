---
type: "corpus"
item_id: "257ee7043d31f170"
title: "Your DEV posts have a beautiful new share card ✨"
source: "devto"
source_name: "dev.to"
url: "https://dev.to/devteam/your-dev-posts-have-a-beautiful-new-share-card-4be8"
project_url: "https://github.com/forem/forem/pull/19826"
author: "Jess Lee"
published_at: "2026-10-27T16:44:29Z"
captured_at: "2026-11-04T09:54:38+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-10-28"
pub_day: "2026-10-27"
tags:
  - 语料
  - devto
  - devto
  - showdev
  - opensource
  - design
metrics: {"reactions": 175, "comments": 36, "reading_time": 2}
comments_count: 36
comments_total: 36
discovered_via: "devto:showdev"
---

# Your DEV posts have a beautiful new share card ✨

> [!info] 一句话导读
> Your DEV posts have a beautiful new share card ✨

> [!meta]- 语料信息（点开展开）
> 来源：dev.to（post）
> 原帖：<https://dev.to/devteam/your-dev-posts-have-a-beautiful-new-share-card-4be8>
> 指标：reactions=175 · 评论=36 · reading_time=2
> 作者：Jess Lee　|　发布：2026-10-27T16:44:29Z
> 项目链接：<https://github.com/forem/forem/pull/19826>
> 采集：2026-11-04T09:54:38+08:00　|　id：`257ee7043d31f170`

## 正文

Skip to content
Powered by Algolia
Log in
Create account
DEV Community
Add reaction
Like
Unicorn
Exploding Head
Raised Hands
Fire
Jump to Comments
Save
Boost
Pick as gem
Copy link
Copied to Clipboard
Share to X
Share to LinkedIn
Share to Facebook
Share to Mastodon
Share Post via...
Report Abuse
Jess Lee
for The DEV Team
Posted on Oct 27
•
 Edited on Oct 27
•
AI-assisted
Your DEV posts have a beautiful new share card ✨
# devto
 # showdev
 # opensource
 # design
Shows post snippets and custom brand colors
The image that shows up when you share a DEV post just got a brand-new look!
I got to work on forem/forem#24071 last week and I'm so excited to see it live in production:
Redesign generated social images as quote cards that work on X and LinkedIn
#24071
jessleenyc
 posted on Oct 22, 2026
What type of PR is this? (check all applicable)
[ ] Refactor
[x] Feature
[x] Bug Fix
[x] Optimization
[ ] Documentation Update
Description
Articles without a cover image get a generated share image ( articles.social_image ). In the last 30 days on DEV, that was 73% of published posts. The old card had two problems:
It repeated the title. X, LinkedIn and Slack already show the title as text next to the image.
X's title label covered the byline. X overlays the post title in a dark label inset at the bottom-left of link cards, right on top of the author's name and date.
New design: the card quotes the opening of the post inside a browser-window frame over a soft mesh gradient. A byline row shows the avatar, name, date and reading time, and the community's horizontal header logo ( Settings::General.resized_logo , falling back to logo_png ) sits in the window's title bar.
One image for every platform: the card is sized so its top and bottom margins both equal X's 80px keep-clear zone.
X's title label covers only the gradient.
The card is vertically centered where nothing is overlaid (LinkedIn, Slack, iMessage, …).
A spec enforces both. No schema change and no view change.
Quote ( Images::SocialImageQuote ):
Uses top-level opening paragraphs. Skips paragraphs that are entirely italic (challenge "This is a submission for…" intros), paragraphs that repeat the title, and headings, code, images and blockquotes. Blockquotes usually quote someone else, and the card attributes the text to the author.
Joins short paragraphs until there are at least 80 characters, then cuts at the last sentence end within 180 characters, or at a word with "…".
Falls back to the title when the post has no usable paragraph.
Colors:
The author's brand color ( brand_color1 , or the organization's bg_color_hex ) becomes an analogous palette.
Otherwise one of four Forem gradient palettes is chosen from the article ID, so cards vary. Only about 6% of authors with coverless posts set a brand color.
Regeneration: in addition to title, publish date and author (#24063), Article#generate_social_image now also fires when:
the reading time changes,
a body edit changes the quote. Old and new quotes are compared, so edits further down the post don't re-render.
Bug fixes along the way
Text escaping: user text is now rendered with label: / caption: and escaped, never with -draw text .
Through MiniMagick, -draw runs in mogrify, which takes the escapes literally. A name like @jess or 50% showed \@jess / 50\% on today's cards.
In caption: / label: , an unescaped leading @ makes ImageMagick read a file into the image. This was verified locally, and a spec covers it.
Stylized Unicode names: names such as 𝐓𝐡𝐞 𝐋𝐚𝐳𝐲 𝐆𝐢𝐫𝐥 rendered blank (Noto Sans has no math-alphanumeric glyphs). They're now NFKC-normalized. Emoji are dropped from the name and quote for the same reason.
Fonts: font / fill are set before each draw. Previously they came after the draw calls, so the date had no font set.
Wrapping uses real glyph widths ( caption: plus a shrink-to-fit loop) instead of character-count heuristics.
Performance
About 1–2s per article on my machine.
Intermediate steps use uncompressed MIFF, so PNG is encoded once. Per-step PNG encoding was the bottleneck.
The gradient is drawn at 400×209 and scaled up.
Output is 8-bit RGB PNG, about 100KB.
No external services or AI are involved; it's ImageMagick only.
Production runs ImageMagick 6 (Debian bullseye), so the generator sticks to IM6-compatible operations: xc: , simple draws, blur, resize, caption: / label: , Over compositing, and the existing rounded_mask.png for avatars.
Related Tickets & Documents
Builds on forem/forem#24063 (regenerates the image when an article's author changes), which is merged into this branch. Its author-change trigger is kept.
QA Instructions, Screenshots, Recordings
Publish a post without a cover image and let Images::SocialImageWorker run. Check article.social_image .
Paste the post URL into X's composer and into LinkedIn's post preview. The quote and byline should be fully visible on both, with X's title label over the gradient only.
Edit the first paragraph → the image regenerates. Edit only a later paragraph (same reading time) → no regeneration.
Before / after
Simulated X and LinkedIn link-card previews. Each post is rendered with today's generator and with this PR's generator. The X frame follows X's current layout (the title label inset at the bottom-left) and was checked against a real X post. The long-title example also shows a bug in today's card: long titles run off the right edge.
The design was reviewed an
d signed off by @jessleenyc.
Known limitation (pre-existing): Noto Sans has no CJK glyphs, so CJK text still renders as boxes, as it did in the old title-based card.
Added/updated tests?
[x] Yes
Images::SocialImageQuote : paragraph selection, skip rules, sentence/word cuts, Unicode cleanup, title fallback.
Images::GenerateSocialImageMagickally : stored image for Article/User/Organization; X keep-clear and vertical centering; a real ImageMagick render at 1200×627; the @file escaping regression; palette, accent, name and meta helpers; read_files and logo caching.
Article#generate_social_image : quote-change, later-edit and reading-time triggers.
Local test status: the DB-free SocialImageQuote examples pass, and real renders were checked locally on ImageMagick 7. The DB-backed specs rely on CI, because the current schema needs pgvector, which my local Postgres lacks. CI also exercises the real-render spec on ImageMagick 6.
[optional] Are there any post deployment tasks we need to perform?
None. No migration, and no backfill: existing images update when a post's title, date, author, reading time or opening changes.
View on GitHub
Meet the new card
Every post now gets a quote card. It pulls the opening of your post and sets it inside a little browser-window frame over a gradient. Below that sits your profile pic, name, publish date, and reading time.
Most places that unfurl a link already show its title, so I wanted to remove the redundancy. It shows the first lines of your post instead. That's where your voice is, and now it's the first thing people see when your post is shared!
Color comes from your profile's brand color if you've set one. If not, the card uses one of our four palettes, so a page full of shared posts feels varied and bright.
One image, everywhere
There's one image, and it unfurls anywhere your link gets shared. It's sized with roomy top and bottom margins, so even when a platform (ahem, X) lays its own label over the image, your name and details stay clear.
A few extra touches
While we were in there, we polished a few more things:
Names with @ or % display cleanly, without stray backslashes.
Names in stylized Unicode (𝓯𝓪𝓷𝓬𝔂 𝓽𝓮𝔁𝓽 like this) render properly.
The image refreshes when your reading time or opening quote changes, so it stays current after you edit.
Thank you to Ben for the review and merge!
A little history
Back in 2018, Ben wrote about how DEV generated social images in the first place:
How dev.to dynamically generates social images
Ben Halpern
Ben Halpern
Ben Halpern
Follow
Feb 26 '18
How dev.to dynamically generates social images
# meta
 # ruby
 # webdev
97 reactions
22 comments
3 min read
In August 2023, Ben moved generation in-house with ImageMagick ( #19949 ). It was a great cost savings to host every post's card ourselves, on our own infrastructure, instead of handing it to a third-party service. Everything in this redesign builds on that foundation.
Go see yours
Share one of your posts (without a cover image) and take a look at your new card. Tag us ( @thepracticaldev ) or me ( @jessleenyc ) on X so I can admire it. If anything looks off, like a name that renders strangely or a quote that cuts off in a weird spot, let me know in the comments!
Top comments (35)
Subscribe
Personal
 Trusted User
Create template
Templates let you quickly answer FAQs or store snippets for re-use.
Submit
 Preview
 Dismiss
FrancisTRᴅᴇᴠ
FrancisTRᴅᴇᴠ
FrancisTRᴅᴇᴠ
Follow
Senior Full-Stack Developer and a Community Curator on DEV!
"ᴀ ꜱᴍᴏᴏᴛʜ ꜱᴇᴀ ɴᴇᴠᴇʀ ᴍᴀᴅᴇ ᴀ ꜱᴋɪʟʟᴇᴅ ꜱᴀɪʟᴏʀ" - ꜰʀᴀɴᴋʟɪɴ ᴅ. ʀᴏᴏꜱᴇᴠᴇʟᴛ
Location
United States
Education
🎓 Master's in Software Engineering 🎓
Pronouns
He/Him
Work
☕ Senior Full-Stack Developer at CALEC ☕
Joined
Jan 14, 2026
•
Oct 27
Copy link
Hide
So pretty card displays!
5 likes
Like
Reply
Giorgi Kobaidze
Giorgi Kobaidze
Giorgi Kobaidze
Follow
🏆2x Hackathon Winner
Location
Tbilisi, Georgia
Education
San Diego State University
Work
Engineering Manager at Flutter CEE
Joined
Jan 29, 2018
•
Oct 27
Copy link
Hide
I love this! Great job, team!
5 likes
Like
Reply
Varshith V Hegde
Varshith V Hegde
Varshith V Hegde
Follow
A simple programmer fond of learning
Email
varshithvh@gmail.com
Location
Bangalore,India
Education
Mangalore Institute of Technology and Engineering
Work
Member of Technial Staff@DevRev
Joined
Jun 30, 2022
•
Oct 28
Copy link
Hide
Nice one . Love this !!!
3 likes
Like
Reply
Thomas Bonnet
Thomas Bonnet
Thomas Bonnet
Follow
French web developer mainly but touches everything. Volunteer admin mod here at DEV. I learn AI and Astro at this moment and databases. — Addict to Cappuccino and Music
Location
France
Pronouns
He/him
Work
IAM Consultant @ Ariovis
Joined
May 5, 2017
•
Oct 27
Copy link
Hide
oooh that super fresh, awesome!
4 likes
Like
Reply
nyaomaru
nyaomaru
nyaomaru
Follow
React / Vue / TypeScript / OSS
Frontend engineer with 7+ years of experience.
Building code simpler and more understandable architecture.
Email
nyaonyao0725@gmail.com
Location
Heerlen, the Netherlands
Education
Ritsumeikan University
Joined
Apr 19, 2024
•
Oct 27
Copy link
Hide
This is such a nice improvement! 😸✨
The new share card looks much cleaner, and showing the opening lines instead of repeating the title makes a lot of sense.
I really like this update! 😸
5 likes
Like
Reply
𝐓𝐡𝐞 𝐋𝐚𝐳𝐲 𝐆𝐢𝐫𝐥
𝐓𝐡𝐞 𝐋𝐚𝐳𝐲 𝐆𝐢𝐫𝐥
𝐓𝐡𝐞 𝐋𝐚𝐳𝐲 𝐆𝐢𝐫𝐥
Follow
Hi, I am Divyanshi (Divya) | Software Engineer | Techno Gamerz Fan | Doraemon Lover
Education
Indian Institute of Technology Bombay
Pronouns
She/her
Work
Microsoft
Joined
Jun 10, 2026
•
Oct 27
Copy link
Hide
Awesome 🥰
5 likes
Like
Reply
leob
leob
leob
Follow
Pronouns
he/him
Joined
Aug 4, 2017
•
Oct 29
Copy link
Hide
Well done, great improvement!
3 likes
Like
Reply
Jess Lee
The DEV Team
Jess Lee
The DEV Team
Jess Lee
Follow
Building DEV with everyone here. What do we have if not community?
Email
jess@majorleaguehacking.com
Location
USA / TAIWAN
Pronouns
she/they
Work
Founder-in-Residence at Major League Hacking, Co-Founder at DEV
Joined
Jul 29, 2016
•
Oct 27
Copy link
Hide
😀😀😀😀😀😀
8 likes
Like
Reply
Jess Lee
The DEV Team
Jess Lee
The DEV Team
Jess Lee
Follow
Building DEV with everyone here. What do we have if not community?
Email
jess@majorleaguehacking.com
Location
USA / TAIWAN
Pronouns
she/they
Work
Founder-in-Residence at Major League Hacking, Co-Founder at DEV
Joined
Jul 29, 2016
•
Oct 27
• Edited on Oct 27
 • Edited
Copy link
Hide
😐😐😐😐😐😐
6 likes
Like
Reply
Peter Vivo
Peter Vivo
Peter Vivo
Follow
The Vibe Archeologist.
Creator of mordorjs + hexaw
|> and touch bar fanatic from Hungary.
God speed you!
1John1 + 5John17 |> 1Moses1 = (1Moses2 ... 4.22John21);
alpha & omega = !![];
Location
Csobánka, Hungary
Education
streetwise
Work
full stack developer at TCS
Joined
Jul 24, 2020
•
Oct 28
Copy link
Hide
I really like this!
Do these new cards also work when I use a video instead of a cover image for an article? Because currently, the video appears as a blank space when shared elsewhere.
Also, I'm not sure where to suggest this, but I think it would be great if we could provide both an image and a video for an article. That way, external shares could display the image instead of a blank video placeholder.
1 like
Like
Reply
View full discussion (35 comments)
Some comments may only be visible to logged-in visitors. Sign in to view all comments.
Code of Conduct
 •
 Report abuse
Are you sure you want to hide this comment? It will become hidden in your post, but will still be visible via the comment's permalink .
Hide child comments as well
Confirm
For further actions, you may consider blocking this person and/or reporting abuse
The DEV Team
Follow
The hardworking team behind DEV ❤️
Want to contribute to open source and help make the DEV community stronger?
The code that powers DEV is called Forem and is freely available on GitHub.
You're welcome to jump in!
Contribute to Forem
More from The DEV Team
That's a Wrap on Hacktoberfest 2026! 🎃👻
# hacktoberfest
 # hf26challenge
 # opensource
 # ai
Hacktoberfest 2026 DEV Challenges: Five Challenges, One Prompt, a New Theme Every Week
# devchallenge
 # hf26challenge
 # hacktoberfest
 # opensource
DEV Community — A space to discuss and keep up software development and manage your software career
Home
DEV Challenges
DEV++
Videos
DEV Education Tracks
DEV Help
Advertise on DEV
Organization Accounts
DEV Showcase
About
Contact
Free Postgres Database
DEV Shop
MLH
Code of Conduct
Privacy Policy
Terms of Use
Built on Forem — the open source software that powers DEV and other inclusive communities.
Made with love and Ruby on Rails . DEV Community © 2016 - 2026.
We're a place where coders share, stay up-to-date and grow their careers.
Log in
Create account

## 评论（36/36）

> **Jess Lee** · 2026-10-27T16:48:46Z　
> 😐😐😐😐😐😐

---

> **Jess Lee** · 2026-10-27T16:53:58Z　
> 😀😀😀😀😀😀

---

> **Giorgi Kobaidze** · 2026-10-27T16:55:19Z　
> I love this! Great job, team!

---

> **FrancisTRᴅᴇᴠ** · 2026-10-27T17:02:57Z　
> So pretty card displays!

---

> **nyaomaru** · 2026-10-27T17:07:08Z　
> This is such a nice improvement! 😸✨
>
> The new share card looks much cleaner, and showing the opening lines instead of repeating the title makes a lot of sense.
>
> I really like this update! 😸

---

> **𝐓𝐡𝐞 𝐋𝐚𝐳𝐲 𝐆𝐢𝐫𝐥 ** · 2026-10-27T18:02:31Z　
> Awesome 🥰

---

> **Odinaka Robert Nnamani** · 2026-10-27T18:07:46Z　
> Quoting the opening line instead of repeating the title is a nice touch. The byline getting covered was an odd bug to ship with.

---

> **Thomas Bonnet** · 2026-10-27T20:32:42Z　
> oooh that super fresh, awesome!

---

> **Emily Woods** · 2026-10-27T21:09:43Z　
> The quote selection rules are the part I'd keep beside the visual examples. An intro that starts with inline code or a link would make an interesting fixture: I'd want the card to read naturally after formatting disappears, while still attributing only my own words. Could the editor eventually show the selected excerpt before I share? That would make awkward cuts easier to catch.

---

> **Logan Jenkins** · 2026-10-28T04:39:00Z　
> The new share cards look clean — the type scale got much better.

---

> **Peter Vivo** · 2026-10-28T05:35:03Z　
> I really like this!
>
> Do these new cards also work when I use a video instead of a cover image for an article? Because currently, the video appears as a blank space when shared elsewhere.
>
> Also, I'm not sure where to suggest this, but I think it would be great if we could provide both an image and a video for an article. That way, external shares could display the image instead of a blank video placeholder.

---

> **Petra** · 2026-10-28T06:00:48Z　
> Thanks

---

> **Stefan** · 2026-10-28T06:25:00Z　
> 73% of posts had no cover image? That's a lot of authors getting a better preview without having to design anything. Skipping blockquotes is a thoughtful detail too. Someone else's words could look very different with my name underneath them.

---

> **Ntombizakhona Mabaso** · 2026-10-28T07:41:27Z　
> i would love a cool one for sharing to Instagram and Facebook stories & highlights. 🥺

---

> **Varshith V Hegde** · 2026-10-28T07:51:05Z　
> Nice one . Love this !!!

---

> **Sheraz Manzoor** · 2026-10-28T12:15:51Z　
> Cool update.

---

> **KC** · 2026-10-28T13:18:43Z　
> Mind blowing

---

> **Timothy Thomas** · 2026-10-28T19:11:55Z　
> This is sick

---

> **FuriLabs** · 2026-10-29T08:54:55Z　
> I really like this! Cool update.

---

> **Maame Afua A. P. Fordjour ** · 2026-10-29T11:05:02Z　
> This looks amazing!

---

> **Alex Shev** · 2026-10-29T12:21:03Z　
> Nice improvement. Share cards are part of a post’s distribution surface, so it would be helpful to know how title length, code blocks, and non-Latin text are handled. Those edge cases decide whether the new design stays polished outside the happy path.

---

> **leob** · 2026-10-29T13:44:26Z　
> Well done, great improvement!

---

> **Shubhra Pokhariya** · 2026-10-29T15:56:43Z　
> Love this, Jess! Showing the opening lines instead of repeating the title is such a nice touch. And the extra space so X’s label doesn’t cover the author’s name and details is a thoughtful detail too. Great work! 😊

---

> **G-type** · 2026-10-29T18:13:23Z　
> So great. I love this new design and well, it looks amazing in my emails and messages.

---

> **Jessica Doering** · 2026-10-29T19:02:47Z　
> Awesome!

---

> **Alex Shev** · 2026-10-29T20:27:25Z　
> This is a small visual change with a real distribution effect. Consistent share cards make a post legible before anyone reads it; it would be interesting to see an accessible fallback checklist too, especially for titles that become dense at social-preview sizes.

---

> **Klaudia Grzondziel** · 2026-10-29T22:09:57Z　
> I just noticed the change while sharing a post with a colleague, and now I found this article 😄 Very cool improvement, thank you for your work! 🚀

---

> **Earl Grey** · 2026-10-29T22:25:48Z　
> Thanks so much!

---

> **janer ruiz** · 2026-10-30T04:35:19Z　
> youtube.com/shorts/VQQiUCJmOG0?fea...

---

> **Jesse Gamble** · 2026-10-30T06:13:34Z　
> Do you expect the opening-line quote to change which posts get clicked, or is it mainly a cleaner presentation?

---

> **janer ruiz** · 2026-10-30T12:22:30Z　
> instagram.com/reel/DfG8mQLtoO5/?ps...

---

> **Earl Grey** · 2026-10-30T18:58:16Z　
> Seeing these cards out in the wild, example X, has been awesome. They look so, so good! #swagger

---

> **v🐸** · 2026-10-30T19:27:32Z　
> looks cool

---

> **Bogdan** · 2026-10-30T20:44:55Z　
> These look incredibly sharp! The custom brand colors feature is a huge plus for creators trying to build a consistent identity while sharing snippets. DEV is really setting the standard for what a modern developer community should look like. Great update, team!

---

> **llzzz** · 2026-11-01T01:53:53Z　
> Great work!

---

> **Elmar Chavez** · 2026-11-01T16:07:29Z　
> Oh this is quite cool. Correct me if I'm wrong, if the post already has a banner image, the image will be shown instead of the quote? Love the design btw.

## 导航

- 项目页：[[10-项目/github.com_069d229a]]
- 渠道页：[[50-渠道/devto]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
