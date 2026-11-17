---
type: "corpus"
item_id: "fee8d3a3e07cc2f7"
title: "Show HN: One API and MCP Server to Publish to TikTok, Instagram and YouTube"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50524748"
project_url: "https://ugcapi.dev/"
author: "trynotsober"
published_at: "2026-11-16T22:59:33Z"
captured_at: "2026-11-17T11:09:12+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-11-17"
pub_day: "2026-11-16"
tags:
  - 语料
  - hn_show
  - author_trynotsober
  - story_50524748
  - show_hn
metrics: {"points": 2, "comments": 0, "engagement_velocity": 2}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:3d"
---

# Show HN: One API and MCP Server to Publish to TikTok, Instagram and YouTube

> [!info] 一句话导读
> Skip to content UGC API Product Why UGC API One call per campaign, any file fitted

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50524748>
> 指标：点赞=2 · 评论=0 · engagement_velocity=2
> 作者：trynotsober　|　发布：2026-11-16T22:59:33Z
> 项目链接：<https://ugcapi.dev/>
> 采集：2026-11-17T11:09:12+08:00　|　id：`fee8d3a3e07cc2f7`

## 正文

Skip to content UGC API Product Why UGC API One call per campaign, any file fitted
 Formats Video, slideshow, image, Story
 Use cases Agencies, creator networks, AI UGC apps
 Built with UGC API Products posting through us
 Compare UGC API vs other posting APIs
Docs AI agents Pricing Resources Blog Algorithms, timing, creators, AI UGC
 Guides How-tos for TikTok, Instagram and Shorts
Sign in Get API key Product
 Why UGC API Formats Use cases Built with UGC API Compare
 Docs AI agents Pricing Resources
 Blog Guides
UGC distribution · API, dashboard and MCP
 Post your UGC to every account and every platform. One click.
 UGC API fits each clip to every platform and fans it out as a TikTok, a Reel, a Facebook Reel and a YouTube Short across all your creator accounts, on the schedule you set. Then it shows which platform, creator and caption won.
 Get started: from $10 See how a campaign runs
 From $10 for 1,000 posts · down to 0.68¢ a post · credits never expire
@mia.tries
 Photo post + sound
✓ Live
@mia.tries
Carousel + Story
✓ Live
Desk Co.
 Page Reel
✓ Live
@deskco
 Short
✓ Live
POST /v1/posts
 "format" : "slideshow" , "accounts" : [ 4 ], "story" : true
TikTok Videos · photo posts · drafts instagram Reels · carousels · Stories facebook Page Reels · photo posts YouTube Shorts
 Why UGC teams switch
 A posting API posts. UGC API runs the whole campaign.
 One call: every account, every platform
 Target an account group, set each platform's options once, add caption variants and a cadence. One request schedules the whole campaign as TikToks, Reels plus Stories, Facebook Reels and YouTube Shorts, with a dry run first.
 How campaigns work
 Send any file, we fit it
 PNG or WebP to JPEG for Instagram, aspect ratios padded or cropped, captions and hashtags trimmed to each platform's limits, clips a platform can't take skipped. You see every change before it posts.
 Fit to platform
 See which platform, account and clip won
 Every clip keeps one id across platforms. Reports compare TikTok, Instagram, Facebook and YouTube by views per post, engagement, lift and cost per 1,000 views, by platform, creator, clip or caption. Breakouts repost themselves.
 Campaign reports
 Pay per post, not per account
 Credit packs from $10 for 1,000 posts down to 0.68¢ a post at 100,000, sized by posts, not accounts. One-time payment, credits never expire, failed posts refunded. 100 creator accounts cost exactly what one account does.
 Pricing
Why UGC API One request
 A whole campaign, every platform's settings, in one call.
 Name an account group instead of 40 account ids. Set TikTok privacy, Instagram Stories and YouTube visibility once. Rotate captions across creators. Preview it, then run it.
 ● targets: account groups (tags), optionally only some platforms
 ● defaults: each platform's options once, posts override
 ● caption_variants: rotated across accounts, compared in reports
 ● rules: repost a breakout clip to more creators automatically
 ● dry_run: every post, time, credit and file conversion before anything is scheduled
bash Copy
 curl https://ugcapi.dev/v1/campaigns \
 -H "Authorization: Bearer ugc_live_..." \
 -H "Content-Type: application/json" \
 -d '{
 "name": "Serum launch week 1",
 "targets": { "tags": ["skincare-creators"] },
 "defaults": {
 "tiktok": { "privacy": "PUBLIC_TO_EVERYONE" },
 "instagram": { "story": true },
 "youtube": { "privacy": "public" }
 },
 "posts": [{
 "format": "video",
 "media": ["https://cdn.you.com/serum-day3.mov"],
 "caption": "Day 3 update",
 "caption_variants": ["ok this actually works", "3 days in 👀"]
 }],
 "cadence": { "per_day": 2 }, "timezone": "America/New_York",
 "rules": [{ "when": "breakout", "action": "repost",
 "targets": { "tags": ["backup-creators"] }, "max": 10 }],
 "dry_run": true
 }'
 clip_7f3a9c21e04b8d10
 “Day 3 serum update”
 34 posts · 4 platforms · 1 report
Example
 TikTok Video · 12 accounts 🏆
2.5× next platform
5.2k avg views
 Instagram Reel + Story · 12 accounts
10.5% engagement · 400 saves
2.1k avg views
 YouTube Short · 6 accounts
best 7-day tail
1.5k avg views
 Facebook Page Reel · 4 accounts
800 avg views
Results across platforms
 Which platform won? Which creator? Which caption?
 The same clip keeps one id wherever it went, so its numbers add up across TikTok, Instagram, Facebook and YouTube. One views number for TikTok views, Reel plays and Shorts views, and null where a platform doesn't report something.
 ● Group by platform, account, clip, caption variant or day
 ● Winner, lift over the campaign median, views at 1h, 1d and 7d
 ● Cost per 1,000 views from the credits you spent
 ● post.breakout webhook when a clip takes off
 Read the reports docs
 Send any file
 Creators shoot whatever. Every platform still gets what it accepts.
 Instagram rejects PNGs and odd aspect ratios, Facebook Reels stop at 90 seconds, each platform counts hashtags differently. You send the file once; UGC API converts, pads or crops, trims, or skips per placement, and the dry run shows each change.
 Fit to platform
 POST /v1/posts · "dry_run": true → warnings
 launch.png · 1080×1350
 → JPEG for Instagram
converted
 banner.webp · 3:1
 → Padded to 1.91:1
adjusted
 Caption · 38 hashtags
 → Trimmed to 30 on Instagram
adjusted
 unbox.mp4 · 94 s
 → Skipped as a Facebook Reel (90 s max), posted everywhere else
skipped
 Slideshow · 12 photos
 → First 10 as the Instagram carousel
adjusted
 Nothing is scheduled until you drop dry_run . Conversions run on our side at no extra cost.
@mia.tries · TikTok first 24 h
 +4 h post.breakout: 1.9k views, 3.2× this account’s median
 +4.5 h rule fires: repost to 5 backup-creators without this clip
 +5 h rule.reposted webhook, 5 new posts in the report
Breakouts
 A clip takes off. More creators post it, automatically.
 When a clip reaches 3× its account's median views within 48 hours you get a post.breakout webhook. Add a repost rule and it goes to the creators in a backup group who haven't posted it, after a delay and up to a limit you set.
 Repost breakouts
 Formats
 You send a format. We make every placement.
 You send TikTok Instagram Facebook YouTube
 Video Video post (or draft) Reel · trial or collab optional · optional Story Page Reel Short
 Slideshow Photo post with TikTok music, or a video Carousel up to 20, video slides kept · or a Reel Multi-photo post, or a Reel Short rendered from the slides, with music
 Image Photo post Single image · optional Story Photo post —
Details per network: TikTok , Instagram , Facebook , YouTube Shorts .
 For AI agents
 Ask your agent to post. Then ask it what won.
 Connect Claude, ChatGPT, Cursor or Gemini to our MCP server. They schedule campaigns across your creators, then answer “how did we do?”, “which caption won?” and “why did it fail?” with a table, a chart and a next step you approve.
 ● Answers with tables, charts and insights, not raw JSON
 ● A results card inline in apps that support MCP Apps
 ● Previews every campaign with dates, file fixes and credits first
 ● Same credits as the API: no extra fee for agents
 Connect your agent MCP docs
Example: your agent + UGC API ugcapi.dev/mcp
 How did we do? Which caption won? Plan next week Why did posts fail?
 How did our UGC do this week? Keep it short.
 ugcapi · get_results_summary
 TikTok won this week: 2,400 views per post, 2.3× Instagram. “Morning routine” was the top clip on all four platforms.
 Results Oct 16 → Oct 23
 86
 Published
142k
 Views
3
 Failed
$0.89
 Spent
Views per post
 🏆 TikTok 2.4k
 Instagram 1.1k
 YouTube 860
 Facebook 410
Top clip Platforms Views Engagement
 Morning routine 4 38k 8.1%
 3 days in 👀 3 27k 9.4%
 Desk reset 2 11k 6.0%
● “Morning routine” broke out on @mia.tries (3.4× her usual views).
 ● 3 Instagram posts failed: an expired connection on @deskco.
 Repost “Morning routine” to the 5 backup creators who don't have it yet?
 5 credits Approve Not now
Claude Connector + plugin GPT ChatGPT MCP connector Cursor Remote MCP Grok Grok Tool calling Gemini Gemini CLI MCP Copilot VS Code MCP Windsurf Remote MCP n8n HTTP node Make HTTP module Zapier Webhooks Claude Connector + plugin GPT ChatGPT MCP connector Cursor Remote MCP Grok Grok Tool calling Gemini Gemini CLI MCP Copilot VS Code MCP Windsurf Remote MCP n8n HTTP node Make HTTP module Zapier Webhooks
Built with UGC API
 Content apps that publish their users' posts through us.
All stories
 Hook generator
 UGCHooks
 100 posts per link
AI content engine
 Postraid
 30 days from one brief
Trend remix app
 VTrends
 4 networks, one tap
Built for UGC at volume
 Not another social media scheduler. A publishing pipe for teams that post a lot.
 One format, every placement
 Send a slideshow once. It lands as a TikTok photo post, an Instagram carousel plus Story frames, and a Facebook photo post. No per-platform code.
Spread across accounts
 UGC is many accounts. Give us 100 posts, 5 accounts and “1 a day each”: we schedule them round-robin, minutes apart, over 20 days.
White-label connect links
 Send creators a connect link with your own external_id. Map every account to your user without building OAuth for four platforms.
Drafts, AI label, music
 TikTok drafts so creators add a trending sound, the AI-generated content label when you need it, auto music on photo posts.
Media hosting included
 Pass any https URL or upload to us. We serve files to every platform from one domain and delete them after they're posted.
Webhooks and results
 post.published, post.failed and post.breakout with the public URL per account. Failed posts refund their credit automatically.
Who it's for
 UGC agencies
 Run dozens of creator accounts from one schedule.
UGC generator apps
 Add a “post everywhere” button to your product.
Creator networks
 Let creators connect once; you publish on a cadence.
Slideshows that travel
 Carousel, photo post, Story frames and a Short from one call.
Pricing
 From $10 for 1,000 posts. Down to 0.68¢ a post.
 Unlimited posts from $39 a month: Pro for up to 10 accounts, Agency $79 for any number. Or pay as you go with one-time packs from 1,000 to 100,000 posts whose credits never expire.
 See pricing
 1,000 posts $10
 10,000 posts $85
 50,000 posts $365
 100,000 posts $675
Questions
 What counts as a post? One piece of content published to one account. A slideshow to 3 accounts is 3 posts; each Instagram Story frame counts as one post. Failed posts are refunded.
 Which platforms and formats? TikTok (videos, photo posts, drafts), Instagram (Reels, carousels, single images, Stories), Facebook Pages (Reels, photo posts) and YouTube Shorts.
 Do I need to resize images or convert files for each platform? No. Send JPEG, PNG or WebP at any aspect ratio and MP4 or MOV video. UGC API makes the JPEG Instagram needs, pads or crops to its 4:5–1.91:1 range, trims captions and hashtags to each platform's limits, and skips placements a file can't go to. A dry run lists every change first.
 Can I compare how a clip did on TikTok vs Instagram vs YouTube? Yes. Every clip keeps one id across platforms. The campaign report compares platforms, accounts, clips and caption variants by views per post, engagement, lift and cost per 1,000 views, and names the winner.
 Do my creators share passwords? No. Each creator connects through the platform's own login. We store their access tokens encrypted and never see passwords.
 How does pricing work? Start with 10 free posts. Then a monthly plan with unlimited posts: Pro $39 for up to 10 accounts, Agency $79 for any number. Or pay as you go with one-time packs: $10 for 1,000 posts, $85 for 10,000, $675 for 100,000, credits never expire. No seat fees, failed posts refunded, and dry runs are free.
 Can Claude, ChatGPT or other AI agents post through UGC API? Yes. Add our remote MCP server (https://ugcapi.dev/mcp) to Claude, ChatGPT, Cursor, VS Code, Windsurf or Gemini CLI and they can publish, schedule and report, after you approve. Autonomous agents call the REST API as tools with an API key.
 Are you approved by TikTok, Meta and YouTube? Yes on TikTok and YouTube. TikTok approved our app and our Direct Post audit, so posts publish straight to the creator's profile (or go to their inbox as a draft if you set tiktok.draft). Google approved our YouTube access and raised our upload quota. Instagram and Facebook accounts connect through our own Meta app.
UGC API UGC distribution: every account, every platform . One call posts your video, slideshow or image to every account you manage.
 hello@ugcapi.dev
 Product
 Why UGC API
 Pricing
 Campaign reports
 Dashboard
 Docs
 API errors
 Webhooks
Formats
 Slideshow API
 UGC video API
 Instagram Story API
 TikTok photo carousel
Platforms
 TikTok
 Instagram
 Facebook
 YouTube Shorts
AI agents
 MCP server
 Claude
 ChatGPT
 Cursor & coding agents
 Grok
 Agent frameworks
Learn
 Blog
 Guides
 Use cases
 Built with UGC API
 Compare
 Campaigns
© 2026 UGC API Terms Privacy Data deletion TikTok, Instagram, Facebook and YouTube are trademarks of their owners. UGC API is not affiliated with them.

## 关联链接

- https://cdn.you.com/serum-day3.mov
- https://ugcapi.dev/mcp
- https://ugcapi.dev/v1/campaigns

## 导航

- 项目页：[[10-项目/ugcapi.dev_23e113ba]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
