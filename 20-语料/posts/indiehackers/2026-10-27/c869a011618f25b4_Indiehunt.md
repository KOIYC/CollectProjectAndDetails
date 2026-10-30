---
type: "corpus"
item_id: "c869a011618f25b4"
title: "Indiehunt"
source: "indiehackers"
source_name: "Indie Hackers 产品库"
url: "https://www.indiehackers.com/product/indiehunt"
captured_at: "2026-10-30T09:49:51+08:00"
lang: "en"
kind: "project"
topic: "开发者工具"
shard: "2026-10-27"
tags:
  - 语料
  - indiehackers
metrics: {}
comments_count: 0
comments_total: 0
discovered_via: "ih:products"
---

# Indiehunt

> [!info] 一句话导读
> Home Starting Up Case Studies DB Products Ideas DB Vibe Coding Tools Subscribe to IH+

> [!meta]- 语料信息（点开展开）
> 来源：Indie Hackers 产品库（project）
> 原帖：<https://www.indiehackers.com/product/indiehunt>
> 指标：—
> 作者：—　|　发布：—
> 项目链接：—
> 采集：2026-10-30T09:49:51+08:00　|　id：`c869a011618f25b4`

## 正文

Home Starting Up Case Studies DB Products Ideas DB Vibe Coding Tools Subscribe to IH+
Starting Up Case Studies
 Ideas DB Products DB Sign in Join
Indiehunt
 Launch your product on Indiehunt to get discovered by indies
Visit Website
Indiehunt Launch your product on Indiehunt to get discovered by indies
 Posts 46+
 Revenue $500 / mo
 Website Twitter
October 29, 2026
 Three runway numbers I'd want written down before quitting a job to go indie
I'm close to going full time on my own stuff, so runway math has been on my mind a lot this month. The thing I noticed is that "how many months do I have" is the question everyone asks, and it's the least useful one on its own. These are the three numbers I'd want on paper before handing in notice.
 1. Months left at today's burn. The simple one. Cash divided by monthly net burn, where net burn is expenses minus whatever revenue is already coming in. With example numbers, $48,000 in the bank and $8,000 a month out is 6 months. Fine as a starting point, but it assumes nothing changes, and something always changes.
 2. Months left if burn creeps up. Going indie almost always means a few new monthly costs: health insurance, tools you used to get free at work, a coworking desk, maybe ads. Same example, but burn grows 5% a month, and the 6 months becomes about 5.4. Not dramatic, but that half month is exactly when you'd be waiting on a first big customer.
 3. The most I can spend per month and still reach month 12. This is the one I find most useful, because it turns runway into a budget. Flip the question: if I want 12 months no matter what, what's my max burn? $48,000 over 12 months is $4,000 a month flat. If costs creep 3% a month, the max starting burn drops to about $3,382. That's a number you can actually check your bank statement against every month.
 I put this math into a free runway calculator on IndieHunt . It does months left from cash and burn, an optional monthly burn change with a month by month table, and the reverse mode for max burn over N months. The formulas are written on the page, and it runs in your browser so nothing you type gets uploaded.
 For people who already made the jump: which number did you wish you'd taken more seriously, the runway or the burn creep?
Praneet Brar
5 Upvotes
Comment
October 28, 2026
 Three rules I'd write down before saying yes to a $2,736 pay-by-invoice request
Here's an email I think every small SaaS gets eventually. Say you sell a $19 per seat tool, most of your 40-ish customers pay monthly by card, and an office manager at a 12-person agency writes: "we want the annual plan for the whole team, but finance can't use a card. Can you send an invoice, net 30, bank transfer?"
 12 seats x $19 x 12 months is $2,736. At under 50 customers that might be your biggest payment of the year, so of course you want to say yes. I wrote up the full Stripe side of this on dev.to , but the decisions matter more than the API, so here are the three I'd make before replying.
 1. Invoices are for annual plans only. The fee math is the reason. With US list prices as I read them in October 2026, a card payment on $2,736 costs about $79.64. A USD bank transfer is 0.5% capped at $5. Around $75 saved on one invoice, nice. On a $19 monthly invoice the difference is pennies and the admin isn't worth it, so monthly stays on card.
 2. Decide access on purpose, because Stripe won't wait for the money. This is the one that surprised me. A subscription set to send_invoice is active the moment you create it, even if the first invoice is unpaid. If your paywall checks for "active", that agency has 12 seats for 30 days before a cent arrives. For a known company, access on trust is probably fine. For a stranger, I'd keep them locked until the first invoice is paid, or make the first one net 7 instead of net 30.
 3. Late means a personal email, not just a robot. Stripe can send reminders, but a $2,736 invoice 7 days late deserves a short note from me to whoever asked for it. Usually it's stuck in someone's approval queue. Access gets paused around 30 days, and I'd tell them that upfront.
 Write those three down once and the reply to the next agency takes five minutes instead of an evening.
 The longer version, with the bank transfer matching rules, underpayments and a paywall snippet, is in my post on handling a pay-by-invoice request when you have under 50 customers .
 If you already sell to teams, do you give access the day the invoice goes out, or only once it's paid?
Praneet Brar
1 Upvote
Comment
October 27, 2026
 Every marketing channel gets 30 days and 3 hours a week from me. Then I ask it three questions
I used to add marketing channels the way people open browser tabs. A new subreddit, a newsletter, one more directory, a second social account. None of them ever got closed, they just quietly ate my evenings.
 So now there's a rule. A new channel gets 30 days and a cap of 3 hours a week. If it costs money, the money cap gets decided before I start, not after I've spent it. When the 30 days are up I sit down for ten minutes and ask three questions.
 1. Did anyone act like a buyer? Not likes, not followers. A signup that actually did something, or a message like "does it do X?" or "how much is it". Zero of those in 30 days is a pretty clear answer for a small product.
 2. Was I actually there for the 30 days? Sometimes the channel didn't fail, I posted twice and disappeared. That's not a no, it's a "didn't test". It gets one more month only if I'm honest that I'll show up this time.
 3. Would I keep doing it if it was my only channel? This one kills the "it's good for awareness" stuff fast. If the answer is no, it was a nice-to-have, and nice-to-haves are exactly where the hours go.
 The cut is the important bit. A channel that fails goes to zero hours, not "a bit less". A bit less is how you end up with a bunch of half-alive accounts you feel guilty about.
 The other thing that helped: 3 hours times 4 weeks is 12 hours. That's the real price of one test. Once I wrote it as a number it got much easier to say no to the next shiny channel, and I keep max two tests running at the same time.
 Paid works the same way, just with dollars instead of hours. If you're about to try search ads, the IndieHunt guide on running your first Google Ads test on a small budget has the same idea: pick the budget and a stop date first, then make a kill or keep call.
 Which channel did you keep way longer than you should have? And what finally made you drop it?
Praneet Brar
5 Upvotes
4 Comments
October 26, 2026
 Three reasons I won't sell a lifetime deal until 20 people pay me monthly
Every few weeks someone suggests I do a lifetime deal. Quick cash, a pile of users, some feedback. I get the appeal, especially when the monthly revenue chart is flat and you're tired of looking at it.
 My rule though is no lifetime deal before 20 people are paying monthly. Not because LTDs are evil, some founders do them really well. It's because before that point I don't know enough to price one, and an LTD is a price you can never change.
 1. I don't know what one user costs me yet. With a handful of customers I can't tell you what a heavy user costs in support time, hosting, or AI calls over three years. A lifetime buyer pays once and then costs that forever. If I don't know the cost, I'm guessing the price, and guessing wrong here doesn't get fixed next month.
 2. It sets the anchor for everyone after. Once a few hundred people got the thing for one payment, the monthly price starts to look like a bad deal to anyone who heard about the LTD. With under 20 monthly customers, the LTD crowd would be most of my users, and their price becomes "the real price" in people's heads.
 3. The loudest users would be the ones paying nothing ongoing. LTD buyers are often great, very engaged. But if they are most of the user base, the roadmap starts bending toward people who will never pay again, and the monthly customers I actually need to keep get quieter.
 What I do instead while I'm under 20: I put an annual plan next to monthly. It's still upfront cash, it still says "this person is committed", but I get to change the price next year once I know what things cost.
 And when I do get past 20, the plan isn't "LTD, go". It's caps written down before launch: what "lifetime" means, which limits apply, which future products are not included. Boring fine print, but it's the part that saves you later.
 If you're thinking about one right now, the IndieHunt blog has a decent breakdown of how to run a lifetime deal without wrecking your indie SaaS , including the 3-year cost math and the guardrails.
 Anyone here did an LTD early and still glad about it? Or the opposite. I'd like to hear the number of paying customers you had when you did it.
Praneet Brar
1 Upvote
3 Comments
October 25, 2026
 Three questions I ask before I build an integration a customer asked for
Integration requests are the hardest ones for me to say no to. They sound small ("just connect it to Notion"), they come from people who are actually paying, and they look great on a features page. They're also the stuff that quietly eats a month and then breaks every time the other company changes their API.
 So I have a short rule now. Before any integration goes on the roadmap it has to get through three questions. If it fails one, it waits.
 1. Has it been asked for twice, by people who don't know each other? One request is a preference. Two independent ones is a pattern. I keep a plain list with the request, who asked, and the exact words they used, and I only count it again when a different customer brings it up without me hinting.
 2. What are they doing today instead? I ask this straight back to them. Very often the honest answer is "I copy it over by hand once a week" or "I export a CSV". If the workaround takes them five minutes a week, a CSV export or a webhook might solve 80% of it, and I own that code fully.
 3. Would I still keep it alive if the person who asked churned next month? This one kills the most. An integration is not a one-off build, it's a small permanent job. Auth tokens expire, scopes change, the other side deprecates an endpoint. If the only reason it exists is one customer, it becomes my job forever for one account.
 Worked example, made-up numbers to show how it plays out. Say 4 customers ask for a Slack integration in a quarter, 3 of them independently. Today they forward an email into a channel. That passes question 1, and question 2 says a simple outgoing webhook covers most of it. So instead of a full Slack app with OAuth and slash commands, I'd ship a webhook URL field and a short guide for pasting it into Slack. A day or two of work instead of a few weeks, and if Slack changes something, the webhook still works.
 And the reply to the customer when it doesn't pass is honest, not "it's on the roadmap":
 "Not building this one yet. You're the first to ask, and I'd rather do it properly once more people need it. I wrote it down with your exact use case. Meanwhile here's how to do it with an export."
 People are surprisingly fine with that. What annoys them is a vague yes that never ships.
 The bigger version of this, sorting support requests into what actually goes next, is written up in how to turn support tickets into product priorities on the IndieHunt blog.
 Curious what others do here. Which integration did you build early that you wish you hadn't? Or the opposite, one you held back on for too long?
Praneet Brar
2 Upvotes
Comment
October 24, 2026
 I made a five-column sheet the night before launch so I stop typing UTM tags from memory
A decision I made after looking at my own launch reports one too many times. I don't type UTM tags on the spot anymore. Not on launch day, not in a reply, not at 11pm when I'm tired and someone asks for the link.
 The reason is boring. Launch week is the week I post the same link in the most places. A board, a few directories, Reddit, X, a newsletter, the waitlist email, my bio. And it's also the week I tagged worst. utm_source=Reddit on Monday, reddit on Tuesday, r-saas on Wednesday. Ten days later the report shows three small rows instead of one, and the only question I actually cared about, which place sent people who paid, had no clear answer.
 A few things I learned the annoying way:
 in GA4 the UTM values are case sensitive in reports, so Reddit and reddit are two sources. I just use lowercase for everything now
if you invent a medium like launchpost, GA4's default channel rules don't recognise it and it lands in Unassigned. I only use social, email or referral
never tag your own internal links, it overwrites where the visitor really came from
if you post on X and also put the link in your X bio, both say source x. utm_content is what splits them
So the fix is one sheet, written the night before. Five columns: where the link goes, source, medium, campaign, content. One row per place I plan to post. Then every link gets pasted from the sheet, never from my head.
 Worked example, how a weekly launch sheet looks for me:
 indiehunt / referral / launch-oct-2026 / listing
x / social / launch-oct-2026 / post
x / social / launch-oct-2026 / bio
waitlist / email / launch-oct-2026 / first-email
waitlist / email / launch-oct-2026 / reminder
One campaign name for the whole launch, so a week later I filter once and see it all side by side.
 Two honest limits. Some boards strip the query string from the URL you submit, so hover the button on the live listing once to check. If it's gone it's fine, the board still shows as a referrer. And word of mouth never gets tagged, a link pasted in a group chat lands as Direct whatever you do.
 The other part of the decision: I don't judge sources on launch evening. I wait about a week and look at signups or the first real action per source, not visits. A board can send 300 people who bounce and a small newsletter 12 who stay.
 On a weekly board like IndieHunt the listing stays up all week, so that one-week wait fits anyway. I wrote the longer version, with where you can and can't tag, in why I stopped typing UTM tags by hand in launch week .
 Question for you: on your last launch, did your analytics know which place sent the people who paid, or did you only find out by asking them?
Praneet Brar
1 Upvote
1 Comment
October 23, 2026
 All five of our launch sites now have maker stats pages. On two of them the weekly #1 had zero votes
When I shipped the first maker live stats page on Aura++ on Oct 15, I thought of it as a feature for makers. Now that it's on all five of our launch sites, the thing I didn't expect is what it shows about us.
 Quick recap so this makes sense. Every launch on Aura++, IndieHunt, EarlyHunt, MakerHunt and SideHunt now has its own stats page: verified upvotes, guest votes on a separate line (they don't count for winners), clicks out to the maker's site, comments, and project page visitors. The four that came after Aura++ also show the rank this week and a link to reply to comments, and the rule on those pages is that nothing is estimated. If a number isn't recorded it says "Not tracked yet" instead of a guess. Order it went out: Aura++ Oct 15, IndieHunt Oct 17, EarlyHunt Oct 18, MakerHunt Oct 19, SideHunt Oct 20.
 I already posted about single sites here. What's new is that with all five live I can look across them, and it's a bit humbling.
 Some real snapshots from the morning each one was checked:
 MakerHunt, Oct 19: the week's #1 had 0 verified upvotes, 0 guest votes, 3 outbound clicks. Rank #1 of 22.
SideHunt, Oct 21: the #1 of 24 had 0 upvotes and 0 clicks. A launch sitting at #4 had 0 upvotes and 45 clicks to its site.
EarlyHunt, Oct 18: the #1 had 2 verified upvotes and 6 clicks, while #3 had 1 verified plus 1 guest vote and 8 clicks.
IndieHunt, Oct 17: the #1 of 26 had 1 verified upvote, 4 clicks, 1 comment.
So the honest admission: on two of our sites, the weekly #1 at that moment was a launch with zero verified votes. Votes on small boards are thin. If we only showed makers a vote count, a lot of them would look at a 0 and think nothing happened, when in one case 45 people had clicked through to their site.
 That's why I care more about the clicks line than the rank. The click is the thing a maker actually came for.
 Other limits I'd rather say out loud:
 on the four newer sites visitor counting only started the day the page shipped, so earlier visits aren't there and those numbers start near zero
guest votes are shown but stay separate until the voter signs in, and they never decide winners
these were single morning snapshots, ranks move during the week
on those four the stats pages are noindex, so they don't compete with the listing itself in Google
What I'm not going to claim: that this got anyone more upvotes or more replies. I don't have numbers for that and I'm not going to guess.
 If you've launched with us, your stats page link is on your own project page. If you haven't, IndieHunt runs weekly launches and the page comes with every one.
 Question for anyone who's launched on a few boards: would you rather see a rank, or how many people clicked through? Because those two clearly don't agree.
Praneet Brar
2 Upvotes
Comment
October 22, 2026
 I stopped asking for upvotes on launch day. I send three messages and ask for a click
Most launch day advice I see still boils down to "message everyone you know and ask them to upvote". It feels productive and it's kind of awful for the people receiving it.
 I wrote the long version of this on Medium, but here's the decision I made and why it stuck.
 The thing that changed my mind is how small most launch boards really are. On a smaller board the #1 spot can be won with something like 2 votes. So begging 200 people for upvotes is wildly out of proportion to what the board needs, and the people you begged mostly click, vote, and leave. They never see the product.
 So now I send my own audience three messages across the day instead of one "please upvote":
 Morning: one specific ask. Not "support us". Something like "if you ever export invoices to a spreadsheet, try the CSV thing and tell me if it breaks". A person who has that problem clicks. Everyone else can ignore it without guilt.
Midday: proof with real numbers. A short update with what actually happened so far, visits, clicks, the first bug someone found. Boards like IndieHunt now have a live stats page per launch, so I can link something people can watch instead of a screenshot of a vote count.
Evening: replies. Answer every question that came in, publicly where possible, and thank people by what they said, not just "thanks for the support".
The ask in all three is the click to the product, not the upvote. If someone likes it, they vote anyway. If they don't, a pity vote helps nobody.
 Worked example. Say you have 60 people on a list and launch on a Monday week. The blast version: 60 identical DMs saying please upvote, maybe 30 votes, 5 people actually open the app. New version: one email to the 60 with a specific use case, a midday note with "41 visits, 6 signups, someone found a bug in the date picker, fixed", and an evening reply round. Fewer votes maybe, but the people who show up came for the product.
 The full piece with the three messages written out is here: stop sending "please upvote" on launch day, send people something to watch . And if you're picking a weekly board to try it on, IndieHunt runs Monday to Monday, which gives the three messages room to breathe.
 Honest question: has a "please upvote" blast ever got you a real user? I'm sure it works for some people, I just don't see how it beats one person who came for the product.
Praneet Brar
4 Upvotes
1 Comment
October 21, 2026
 Unpopular rule: I hold one finished feature back from a weekly launch until Thursday
This one usually gets pushback when I say it out loud, so let me just put it here.
 When I launch on a weekly board, I don't ship everything I have ready on Monday. I keep one small, finished feature in a branch and ship it on Thursday. On purpose.
 The reason is how weekly launches actually behave. On a weekly board like IndieHunt the week starts Monday 8:00am UTC and runs seven days. Monday is loud, Tuesday is ok, and then by Wednesday the listing is mostly quiet. People who saw it once already decided "cool, maybe later". Nothing new is happening, so nobody has a reason to look again.
 The Thursday feature is the reason. It's not marketing really, it's giving the listing a second day.
 Worked example. Say I'm launching a little invoice tool. Monday it goes out with the core thing: make an invoice, send it, get paid. I already have CSV export done and working, and I hold it back. Monday and Tuesday I'm in the comments. If anyone asks about export, I say honestly "it's done, shipping Thursday". Thursday morning I ship it, then I:
 reply under the launch listing with one line on what shipped and who asked for it
email the people who signed up that week, short, just "the export you asked about is live"
update the listing description if the board lets me
That's three reasons for someone who already saw it to come back, and none of them is "please upvote".
 Some rules so this doesn't become a trick:
 the held feature must be finished and tested, not a promise
it can't be the main thing. If the core product is weak on Monday, holding stuff back makes it worse
if someone needs it on Monday for real, they get it. I'll just send them the build
The obvious counter argument is "ship everything, first impression is all you get". I get it. But a weekly board isn't a first impression, it's seven days, and most launches I see have nothing to say after day two. The dropoff after the first days is a pattern, not bad luck. There's a longer piece on what happens when launch week traffic fades on the IndieHunt blog if you want the why behind it.
 If you're launching on a Monday week anyway, IndieHunt is where I try this, but the rule works on any board that runs longer than a day.
 So tell me where I'm wrong. Would you rather show everything on day one, or have you seen a mid-week ship actually bring people back?
Praneet Brar
1 Upvote
Comment
October 20, 2026
 I shipped a domain checker that says "can't check" for .io and .co instead of guessing
Yesterday I added a small free domain name checker to IndieHunt. You type a startup name and it checks six endings: .com, .io, .co, .app, .dev and .ai. No signup.
 The part I want to talk about is the honest answer it gives for two of those six. When you check a name, .io and .co come back as "Can't check via RDAP". Not available, not taken. Just can't check.
 Quick background on why. The checker uses RDAP, which is basically the modern structured version of WHOIS. IANA publishes a bootstrap file that says which RDAP server handles which ending. The tool loads that, and for each ending it asks that registry's server about the name. If the server says 404, the name is likely available. If it says 200, it's registered, and you often get the registrar and the registration date too. A timeout or anything else, it says it couldn't check.
 And .io and .co simply don't have an RDAP server in that bootstrap file. So there's nothing reliable to ask.
 A lot of domain checkers will still show you a green tick or a red cross for those endings. I don't know exactly how each one does it, but if there's no source to ask, the answer is coming from somewhere else, maybe a registrar search, maybe a guess. I didn't want to ship a guess, so it says so instead. Same reason the launch stats pages say "Not tracked yet" instead of a made-up number.
 What it shows on a real name, I ran "google" through it on Oct 19:
 google.com : registered, registrar MarkMonitor, registration date 15 Sept 1997 (straight from Verisign's RDAP server)
google.ai : registered Dec 2017
google.app : registered March 2018
google.dev : registered June 2018
google.io and google.co : Can't check via RDAP
Also worth saying: "likely available" is a strong hint, not a promise. The registrar you buy from has the final say, and a name can be reserved or premium priced even when the registry says 404.
 If you're naming something this week you can try the free domain name checker on IndieHunt . For .io and .co you'll still need to check at a registrar, sorry, I'd rather tell you that than fake it.
 Question for people who've named a few products: do you still insist on the .com, or have you stopped caring as long as the name is easy to say out loud?
Praneet Brar
3 Upvotes
4 Comments
About
 We built IndieHunt because launching as an indie maker is still too noisy and unfair. Most platforms favor already-established products with large audiences, making it hard for early-stage builders to get visibility.
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

## 导航

- 项目页：[[10-项目/Indiehunt_c869a011]]
- 渠道页：[[50-渠道/indiehackers]]
- 赛道：`开发者工具`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
