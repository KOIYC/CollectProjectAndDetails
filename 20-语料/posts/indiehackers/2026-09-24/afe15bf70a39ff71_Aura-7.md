---
type: "corpus"
item_id: "afe15bf70a39ff71"
title: "Aura 7"
source: "indiehackers"
source_name: "Indie Hackers 产品库"
url: "https://www.indiehackers.com/product/aura-7"
project_url: "https://auraplusplus.com/"
captured_at: "2026-10-28T09:43:59+08:00"
lang: "en"
kind: "project"
topic: "开发者工具"
shard: "2026-09-24"
tags:
  - 语料
  - indiehackers
metrics: {}
comments_count: 0
comments_total: 0
discovered_via: "ih:products"
---

# Aura 7

> [!info] 一句话导读
> Home Starting Up Case Studies DB Products Ideas DB Vibe Coding Tools Subscribe to IH+

> [!meta]- 语料信息（点开展开）
> 来源：Indie Hackers 产品库（project）
> 原帖：<https://www.indiehackers.com/product/aura-7>
> 指标：—
> 作者：—　|　发布：—
> 项目链接：<https://auraplusplus.com/>
> 采集：2026-10-28T09:43:59+08:00　|　id：`afe15bf70a39ff71`

## 正文

Home Starting Up Case Studies DB Products Ideas DB Vibe Coding Tools Subscribe to IH+
Starting Up Case Studies
 Ideas DB Products DB Sign in Join
Aura++
 Launch your project and increase online aura
Visit Website
Aura++ Launch your project and increase online aura
 Posts 42+
 Revenue $1K / mo
 Website Twitter
October 27, 2026
 14 of our articles were telling Google they were copies of the homepage, because of one line I never wrote
Last week I found a bug that had been sitting quietly on three of our launch sites, EarlyHunt, MakerHunt and SideHunt. Every article under /posts had a canonical tag pointing at the homepage. So 14 articles were basically telling Google "I'm just a copy of the homepage, you can ignore me".
 Nobody wrote that on purpose. The canonical was set in the Next.js root layout, and every route that doesn't override it just inherits it. The pages looked totally fine in the browser. Nothing broke, no error, nothing in the logs. You only see it if you view source. We fixed it on Oct 21 and each article now points at itself. I can't tell you yet if it changed anything in search, it's way too early, I'll look in Search Console in a few weeks.
 What bugged me more is how easy this is to miss. So I built a small free check for it on Aura++, and while testing it a few things surprised me:
 example.com doesn't declare a canonical at all. Not exactly wrong, but I expected the most famous test page on the internet to have one.
github.com does it the textbook way. One absolute canonical pointing at itself, og:url matches it, and the target returns 200.
A canonical can live in two places. The HTML head, or an HTTP Link header. If you only grep the HTML you can miss the second one.
A canonical pointing at a 404 or a redirect kind of cancels itself. So it's worth checking what the target actually returns, not just that the tag exists.
If you want to check one of your own pages, the free canonical tag checker on Aura++ takes a URL and tells you if there's a canonical, if it points at itself, how it compares with og:url and if the target returns 200. No signup. Or honestly just run curl on a deep page and grep for canonical, thats how I found ours.
 My rule now: any time I add a layout or template that sets metadata, I open one deep page, not the homepage, and check the canonical before I call it done.
 Have you ever checked what canonical your blog posts actually point to? Did anything surprise you?
Praneet Brar
7 Upvotes
9 Comments
October 26, 2026
 Four rules I wrote down before the second customer asked to pause instead of cancel
A pause request is one of the nicer support emails you can get. The person isn't leaving. They just don't want to pay for months they won't use. Think a tool for wedding photographers, and in November someone writes "season's done, can I pause till March, I don't want to lose my setup".
 The first time I looked at this in Stripe I found two different things called pause, and they do very different stuff. Pausing payment collection keeps the subscription active, keeps creating invoices, and the person keeps access. It's really a grace period. The newer "pause subscription" (Stripe added on-demand pause and resume in their changelog on Sep 30) changes the status to paused and stops invoices completely. Use the wrong one and you either quietly bill someone all winter or you lock out someone who only wanted a break.
 So under 50 customers my take is: don't wing it per email. Write a tiny policy once. Mine is four rules.
 "Away" and "can't pay" are different requests. Not using it gets a real pause. Still using it but money is tight gets paused collection, and I decide up front if I'm forgiving those months or they pay later.
Every pause has an end date. Max three months. "Until you resume it" is how a pause turns into an account nobody remembers, using the product free for a year.
Paused means read-only, nothing deleted. They can log in, look, export. I say that in the reply so they're not anxious about their data.
I email them a few days before it resumes. I didn't see anything in Stripe's pause docs about Stripe emailing the customer before a resume, so I put a reminder in my calendar and send a short "you're back on March 1, here's what you'll pay" note. Also if they had a discount, it keeps counting down during the pause, which I mention.
The reply then is boring in a good way: "Sure, paused from today until March 1. No charge before then, your projects stay as they are and you can still log in. First charge in March will be a bit lower because of the unused days this month. I'll email you before."
 Pause is for "not right now", cancel is for "not for me", and I keep them as two separate buttons in my head.
 The longer version with the Stripe fields, the cases where the pause button is greyed out, and what your paywall should check is in my write-up on handling a pause request with under 50 customers .
 Do you offer pause at all? Or do you just cancel people and hope they come back?
Praneet Brar
2 Upvotes
1 Comment
October 25, 2026
 Two of our launch sites had zero votes for a whole week. So I stopped adding features to the listing page
Honest numbers first. On MakerHunt and SideHunt, two of the five launch sites I run, the Oct 19 cohort got 0 upvotes and 0 real comments through day six. Not low. Zero. And those listing pages already had stats, a comment box, the maker's links, all of it.
 Someone here said yesterday that these sites look like the same directory five times over. I don't love hearing it but I get why it reads like that from the outside, and the zero is kind of the proof that a nicer listing page alone wasn't doing anything.
 So I looked at where votes actually came from on the one site that does get them. On Aura++ it's pretty clear. The launches that get votes are the ones where the founder shares the launch themselves. On Oct 19 one launch brought in 18 of the 36 visitors that whole cohort got, and 6 verified upvotes, because the maker posted it to their own people. Everyone else mostly waited for the site to send traffic.
 That changed what I was building. Instead of one more feature on our listing page, I built something for the maker's page.
 What shipped: every launch on all five sites now gets an embeddable badge the maker can put on their own site. It shows the launch status (live this week, launching, launched) and the real verified upvote count, refreshed about every five minutes, and it links back to the listing. The snippet sits on the maker's live stats page, one line of HTML to copy.
 Two small decisions I went back and forth on:
 the count is real even when it's tiny. A badge that says ▲ 1 is a bit awkward. But a static "Featured on" image says nothing at all, and inflating it would be worse than both.
no rank unless it's unambiguous. The "#N this week" line only shows when there's no tie. Two launches both on 2 votes calling themselves #1 felt dishonest.
What I'm not doing is claiming it works. I'm tracking clicks that come from the badge over the Oct 26 cohort week and I'll post what that says, even if it's nothing again.
 If you want to see what the embed box looks like, here's one maker's live stats page on Aura++ with the badge preview on it.
 Real question for anyone who has launched somewhere: would you put a badge on your homepage that shows ▲ 2? Or does a small honest number hurt more than having no badge?
Praneet Brar
2 Upvotes
2 Comments
October 24, 2026
 Is your launch link a 301 or a 302? I check it before I submit it anywhere now
Small admission first. The URL I paste into a launch form is usually just whatever is in my address bar. I'd never properly looked at what happens between someone clicking it and the page loading. Could be one hop, could be four.
 So this week I shipped a small free tool on Aura++ for exactly that, and the rule I'm keeping now is simple: before a URL goes into any submit form, I paste it in and look at every hop.
 Why I think it matters, in plain words:
 a 302 says "temporary". If you moved your site for good, from http to https, or from an old domain to a new one, that should be a 301. With a 302 you're telling Google the old URL is still the real one, so the old address can hang around in results longer than you want. It's easy to set a redirect in a hosting panel or plugin and never really choose which one you got.
every hop is a round trip. A visitor from a launch board is impatient already. Two or three extra hops before the first byte of your page isn't great, specially on mobile.
chains and loops grow quietly. You add https, then www, then a new homepage path, and each rule was fine on its own day.
Worked example from the real tests we ran while building it. Typing http://github.com gives one 301 to https://github.com/ in 17 ms, then a 200. That's the clean version, one permanent hop and done. A test URL we set up to return a 302 goes to https://example.com and then 200. Same result for a visitor, the page loads, but the second one is telling search engines "don't update anything, this is temporary".
 Now picture the common indie setup, as an example not a real site: http://yoursite.com goes to https://yoursite.com, then to https://www.yoursite.com, then to /home. That's three hops before anything useful. If one of them is a 302 left over from testing, you'd never notice in the browser. You'd only see it if you look at each status code.
 What the tool shows: every hop with its status code, the Location header and the time it took. It flags 301 vs 302, loops and long chains. Free, no signup. One thing it won't do on purpose: it refuses private and internal addresses like 127.0.0.1 or 169.254.169.254, so you can't use it to poke at someone's internal network.
 If you want to check the link you're about to submit somewhere, it's the free redirect checker on Aura++ . Takes about ten seconds.
 What I still don't know is how common this is out there. When you launch, do you submit your bare domain, the www version, or a specific landing page? And have you ever actually looked at what it redirects through?
Praneet Brar
1 Upvote
4 Comments
October 23, 2026
 Should "delete my account" be as easy to find as "upgrade"? I think it should
Here's a small test I like doing on any SaaS I sign up for, including my own. Open settings and try to find how to delete the account. Not cancel the plan, delete the whole thing, data and all. Time how long it takes.
 On a lot of small products the answer is "you can't, email us". Or there's a link buried three screens deep under Advanced. I get why founders do it. Nobody wants to build the button that makes users disappear. But I think hiding it costs more trust than it saves users.
 My rule now: the delete option sits on the same settings page as billing, it's visible without scrolling much, and it says plainly what happens.
 Why I think this matters before you have many users:
 people check before they sign up, not after. Someone careful about their data will look for an exit before they paste anything real in. If they can't find one, some of them just don't start.
"email us to delete" reads like a trap, even when it isn't. It suggests someone will try to talk them out of it.
it's partly not optional anyway. If you have an iOS app with account creation, Apple has required in-app account deletion since mid 2022. And if you have users in the EU they already have a right to ask for erasure, so you're doing the work either way, the button just makes it self-serve.
Worked example, framed as an example. Say you run a small invoicing tool. A decent delete section could be:
 one line: "Deleting removes your clients, invoices and uploads. Paid invoices you already sent stay with the people you sent them to."
a "download everything first" button that gives a CSV or zip, right above the delete button
if there's an active subscription, say clearly it stops renewing today and what happens to the time already paid for
a confirm step where they type the account email, not a guilt screen with a sad face
an email afterwards that says it's done and when backups age out, so they're not left wondering
What I'd skip: the "are you SURE? you'll lose everything!!" modal, a 30 day "we'll keep it just in case" that nobody asked for (unless you say so up front and let them skip it), and a survey they have to fill before the button works. One optional question is fine.
 The odd thing is how this changes the rest of the product. Once leaving is easy, you stop relying on friction to keep people and you have to rely on the product being worth staying for. That's uncomfortable, and probably healthy.
 It's the same idea as a fair cancel flow, which I wrote up longer in how to design a SaaS cancel flow without dark patterns . Delete is just the step after cancel that most of us forget to design at all.
 Genuine question though: does an easy delete button make you more likely to try a new tool, or do you never even look for it?
Praneet Brar
2 Upvotes
5 Comments
October 22, 2026
 Our own backlink spreadsheet was wrong about which directory links were dofollow
Small admission. We keep a spreadsheet of the directories and launch sites where our products are listed, with a column for "dofollow / nofollow". I assumed that column was right.
 On Tuesday I ran our own listings through the dofollow link checker we shipped on Aura++ last week, and the spreadsheet was wrong in a way I didn't expect.
 What it actually found, on three real listings:
 SaaSHub: 3 links to Aura++ on the one page. The main "Visit website" link has no rel at all, so it's dofollow. The "Official pricing" and "Blog" links are nofollow. Our spreadsheet had SaaSHub down as nofollow.
PeerPush: 1 link, and the only thing on it is rel="noopener". That's a security thing for new tabs, it has no SEO meaning. So that one is dofollow too.
BetaList (our SideHunt listing): 0 links to sidehunt.io in the server HTML. The buttons go through a redirect on BetaList's own domain, so there's no direct link to us on that page at all, follow or not.
So the lesson for me is that "is this directory dofollow" is the wrong question. One page can have a dofollow link and two nofollow ones next to it, and some buttons that look like links to you never point at your domain.
 Couple of things I learned while building it, in case they save someone a search:
 there's no such thing as rel="dofollow". A link is dofollow when it doesn't say nofollow, ugc or sponsored
Google has treated those three as hints, not hard rules, since 2019, so even a nofollow link isn't automatically worthless
check the server HTML, not what you see in devtools after scripts run, because that's closer to what a crawler gets first
If you want to check your own listings, the free dofollow link checker takes a page URL plus your domain and lists every link to you with its rel value and anchor text. No signup. It counts www and subdomains as your site. It only reads server HTML, so links injected later by JavaScript won't show up, which is a real limit.
 And if you're still deciding whether directory links are worth chasing at all, I wrote a plain explainer on what domain rating means for a small startup , because DR is usually the other number people are paying for.
 Question for anyone who tracks backlinks: do you check each link, or do you trust the "this site is dofollow" lists going around? I trusted mine and it was off.
Praneet Brar
3 Upvotes
4 Comments
October 21, 2026
 Four things I keep off my pricing page until ten people have paid
Confession: the first pricing pages I made were mostly costume. Three tiers, a "most popular" badge on the middle one, a big comparison grid, an enterprise box. For a product nobody had paid for yet.
 Nothing on that page was a lie exactly. It just wasn't true yet either, and people can smell that. So now I have a rule for anything new: until ten people have actually paid, these four things stay off the pricing page.
 A "most popular" badge. Popular with who? If zero or two people bought, the badge is a guess dressed up as social proof. I'd rather write one plain line under the plan, like "this is the one I'd pick if I was you, because X".
The "contact us" enterprise tier. It looks grown up, but at this stage it mostly invites discount asks and custom builds a solo founder can't support. One paid plan and a free option is enough to learn if anyone pays at all.
A countdown or "launch price ends Friday". Fake urgency on a page with no buyers reads like a scam to the exact careful people I want early. If the price is going up, I just say the month and why.
A 25 row feature grid. Early on most rows are things I'm still figuring out, and the grid makes people compare checkboxes instead of asking "does this do my one job". Three or four lines in plain words beat it.
What stays on the page: the price, what you get, what you don't get yet, how to cancel in one sentence, and my name. That's it.
 A worked example so this isn't just vibes. Say you're selling a small $12/mo tool that cleans up messy CSV exports. The costume version has Starter / Pro / Team, Pro marked popular, and a grid listing "API access (coming soon)". The honest version says: $12 a month, cleans up to 500 files a month, no API yet, cancel from settings in two clicks, questions go to my email. The second one looks smaller. It's also the one where a stranger can decide in ten seconds without wondering what's hidden.
 After ten payers you actually have data. Which plan they picked, what they asked before buying, who wanted a team seat. Then the badge can be real and the extra tier can be built around a real request instead of a template.
 Picking the number is a harder problem. I wrote up how I think about it in how to price your first SaaS when you have almost no data on the Aura++ blog, the short version is pick a number you can explain out loud and change it later with a note to existing users.
 I know some people will say three tiers is basic anchoring and it works. Maybe it does once you have traffic. So I'm curious: what's on your pricing page right now that you'd quietly delete if nobody was watching?
Praneet Brar
8 Upvotes
8 Comments
October 20, 2026
 Three things I stopped counting as marketing time
For a while my weekly "marketing hours" looked great on paper. Then I actually wrote down what I did in those hours and a big chunk of it was me feeling productive near marketing, not doing marketing.
 So now I have a rule: an hour only counts as marketing if a stranger could see the result, or if it ended with someone new knowing the product exists. Everything else goes in a different bucket, even if it feels like marketing. These are the three that got kicked out first.
 Tweaking the landing page with zero new visitors. Changing the hero line for the fourth time when 30 people saw the last version is not marketing, it's building. Sometimes it's the right thing to do, fine, but I log it as build time. Otherwise I tell myself I "did marketing" all week and nobody new came.
Reading other founders' growth threads. This one hurt. Some of it is useful, but most of it is just comfortable. If I read for an hour and didn't change anything I'm doing this week, that was entertainment. Now it counts as nothing. Not build, not marketing.
Setting up tools. Scheduling apps, analytics dashboards, a new UTM sheet, picking the perfect email tool. All of it feels like progress. None of it puts the product in front of anyone. I give it one block a month and log it as admin.
What's left in the marketing bucket is kind of boring. Replying to people in threads where my kind of user already hangs out. Writing one honest post. Sending a couple of personal emails to people who might actually care. Submitting to a launch site and then being there on the day. Asking a happy user if I can quote them.
 The weird result is my marketing hours went down after I started doing this, and the stuff that actually brings people in went up, simply because I can see it now. When the number was inflated I never felt the need to protect the real hours.
 The test I use at the end of the week is simple. For every hour I called marketing, can I point at a thing someone outside my laptop saw? If not, it moves.
 I'm not saying never polish the landing page or set up tools. Just don't let them hide inside the marketing number. If you want a starting point for how to split the week depending on your stage, there's a longer write-up on how much time a solo founder should spend on marketing vs building on the Aura++ blog, including a small two-week time audit you can copy.
 Curious what's on your list. What's something you used to count as marketing that you quietly don't anymore?
Praneet Brar
13 Upvotes
6 Comments
October 19, 2026
 My dashboard's empty state was the first screen every new user saw, and it said nothing
For a long time the first thing a new user saw after signing up was a grey box that said "No projects yet" and a button that said "New project". That's it. I'd spent weeks on the landing page and maybe ten minutes on the screen people actually land on.
 The problem is that empty screen is where trust gets decided. They just gave you an email, maybe a card. Now they're alone with a blank page and they have to guess what "done" looks like. A lot of people don't guess. They close the tab and tell themselves they'll come back, and they don't.
 So I rewrote it, and these are the four things I check now on any empty state before I call onboarding finished:
 Show a finished example, not a blank. A greyed out sample of what a real filled-in project looks like, clearly labeled as an example. People copy what they can see much faster than they follow instructions.
One action, in their words. Not "Create resource". Whatever the user would say out loud, like "Add your first product". If there are three buttons on an empty screen, there's really zero.
Say how long it takes. "Takes about 2 minutes" next to the button. Sounds silly, but an unknown amount of work is exactly what makes people postpone it.
Tell them what you'll do with their stuff. If the first step asks for a URL, an API key or a file, one plain line about what happens to it. Nobody reads the privacy page at this moment, but they do read one sentence right next to the input.
What I don't put there anymore: a product tour with seven tooltips, a welcome video, a "complete your profile" bar at 10%. All of those are me talking. The empty state should be the user doing the first thing.
 The way I test it is boring. I make a fresh account in a private window, don't read anything I wrote, and see if I know what to do in five seconds. Then I ask one person who has never seen the product to do the same while I keep my mouth shut. The second test is the one that hurts, and the useful one.
 I wrote longer about the emails side of this, the ones that go out after the first screen, in this guide on onboarding emails that get people to a first win . But honestly fix the empty screen first. An email can't rescue someone who already decided your app is confusing.
 Curious what yours shows right now. If you open your own app in a private window today, what's the first thing a stranger sees?
Praneet Brar
5 Upvotes
15 Comments
October 18, 2026
 Two weeks after a launch I ask my three happiest users for a review, on one site only
Launch week gives you a bunch of nice comments that nobody outside that thread will ever see. Two weeks later the comments are buried and the people who wrote them are just... users. So around day 14 I do one small thing, and I keep it small on purpose.
 I pick three people. Not the loudest ones from launch day, the ones who actually came back. Logged in more than once in week two, used the thing for real work, maybe replied to an email. If I can't find three people like that, that's my answer, and I go fix onboarding instead of collecting reviews.
 Then I pick one review site. Just one. For a B2B tool that's usually whichever one buyers in that niche already check, G2 or Capterra most of the time. Sending three people to five different sites gets you one review on each and a profile that looks dead everywhere. Three reviews in one place at least looks like a product somebody uses.
 The ask is a plain email, written by me, sent one at a time:
 one line on what they did with the product (so they know it's not a blast)
the direct link to the review form, not the profile page
"two or three sentences is plenty, say what you used it for"
no discount, no gift card, nothing in exchange. The review sites have rules about incentives and honestly a bribed review reads like one anyway
If someone says no or ignores it, that's fine, I don't follow up more than once. And if one of them writes back with a complaint instead of a review, that's the more useful email of the two.
 Why day 14 and not launch day: on launch day people are reacting to the idea. Two weeks in they're reacting to the product, and that's what a buyer reading reviews wants to hear about.
 The Aura++ Studio has a longer write-up on getting your first G2 and Capterra reviews if you want the setup side (claiming the profile, categories, all that).
 Curious how others do this. Do you ask right after launch while people are excited, or wait until they've actually used it for a while?
Praneet Brar
4 Upvotes
3 Comments
About
 I’m building Aura++ because I kept seeing great products struggle to get noticed. Launching is easier than ever, but getting real visibility is still incredibly hard, especially for early-stage founders without an audien
People
 Praneet Brar Founder
Stay informed as an indie hacker.
 Market insights that help you start and grow your business.
Subscribe
Follow @IndieHackers on X for stories and insights about founders building profitable online businesses, and to connect with others in the Indie Hackers community.
 © Indie Hackers, Inc. · FAQ · Terms · Privacy · Cookie Policy ·
Community
 Top Today Top This Week Top This Month Join
Products
 All Products Highest Revenue Add Yours
Databases
 Ideas Products Stories

## 关联链接

- http://github.com
- http://yoursite.com
- https://example.com
- https://github.com/
- https://www.yoursite.com,
- https://yoursite.com,

## 导航

- 项目页：[[10-项目/Aura-7_6bcffd81]]
- 渠道页：[[50-渠道/indiehackers]]
- 赛道：`开发者工具`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
