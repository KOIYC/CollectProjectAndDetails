---
type: "corpus"
item_id: "c2946d3e737e8bc6"
title: "Cloudflare Quick Tunnels"
source: "hn_front"
source_name: "HN 首页（非 Show HN）"
url: "https://news.ycombinator.com/item?id=49754785"
project_url: "https://try.cloudflare.com/"
author: "jcbhmr"
published_at: "2026-09-18T14:18:41Z"
captured_at: "2026-09-20T03:28:02+08:00"
lang: "en"
kind: "post"
tags:
  - 语料
  - hn_front
  - author_jcbhmr
  - story_49754785
  - front_page
metrics: {"points": 792, "comments": 303, "engagement_velocity": 792}
comments_count: 303
comments_total: 303
discovered_via: "hn:front_page:2d"
archived: true
archived_at: "2026-09-20T09:21:32+08:00"
archive_reason: "渠道停用"
---

# Cloudflare Quick Tunnels

- **来源**：HN 首页（非 Show HN）　|　**kind**：post
- **原帖**：https://news.ycombinator.com/item?id=49754785
- **指标**：点赞=792 · 评论=303 · engagement_velocity=792
- **作者**：jcbhmr　|　**发布**：2026-09-18T14:18:41Z
- **项目链接**：https://try.cloudflare.com/
- **采集**：2026-09-20T03:28:02+08:00　|　**id**：`c2946d3e737e8bc6`

## 正文

Cloudflare Quick Tunnels

# Free, secure tunnel for everything you are building.

Preview and ship ideas globally in seconds with Quick Tunnels. Deploy your local application to the Internet with a single command.

## You're a single command away from sharing your project with the Internet.

Built on Cloudflare's global network, Quick Tunnels give you instant, secure access to your local development environment.

### Instant Setup

One command and you're live. No account creation, no configuration files, no waiting.

### Secure by Default

Automatic HTTPS, DDoS protection, and no exposed ports on your machine.

### Global Network

Traffic is routed through Cloudflare's edge network for fast, reliable connections worldwide.

## Start tunneling today.

Join thousands of developers delivering real-time previews with Quick Tunnels. No account needed. No DNS or certificates to configure. No open ports.

### Install cloudflared

Download the CLI for your platform from the Cloudflare dashboard, package manager or GitHub. No login required for Quick Tunnels.

### Run your local app

Start any web server or API on any port (e.g., localhost:8000). Quick Tunnels work with whatever tool you already use.

### Create the tunnel

Launch a secure ingress with one command. Cloudflare handles certificates, routing, and DDoS protection.

`cloudflared tunnel --url http://localhost:8000`

Share your generated trycloudflare.com preview URL with your team. Accelerate every feedback loop, from design reviews to automated QA.

# How To Write With An LLM — A Final Ward

## 评论（303/303）

**smalltorch** · 2026-09-18T14:52:41.000Z：

It's a nice ability, but I dont like the terms of use.

**user3939382** · 2026-09-18T15:15:51.000Z：

I just spent a week writing a harness around the existing tunnels to make this by hand.

**dangoodmanUT** · 2026-09-18T15:16:05.000Z：

Historically, we’ve found that their tunnels have really high latency variance. For example something that’s normally 30-50ms to ec2 is now 115ms-750ms

**ThrowawayTestr** · 2026-09-18T15:17:38.000Z：

No-ip gives out free dynamic DNS with a static URL. I use it for Sunshine desktop streaming when I travel.

**kincl** · 2026-09-18T15:19:30.000Z：

Is this their version of https://tailscale.com/tailcat ? I can't tell if you need to authedit: yeah, it says no account creation, neat!

**ZeroCool2u** · 2026-09-18T15:19:56.000Z：

This is handy, but I wonder how much it will cannibalize their services. I have a simple app deployed on cloudflare for a very niche single purpose use, but I wouldn't have bothered if I had this. Serving it from my own machine would have been fine.

**aliasxneo** · 2026-09-18T15:21:56.000Z：

Tunneling was something that recently fell out of the work I've been doing [1]. I've used Cloudflare Tunnels before but I just have low trust with them recently with how big they are getting. All of these nice things come at the cost of pushing _a lot_ of traffic through their systems.[1]: https://dntls.substack.com/p/the-new-internet

**whizzter** · 2026-09-18T15:23:51.000Z：

Don't all these free proxy services always fall prey to blacklists because scammers,etc abuse them until they're useless?

**JV00** · 2026-09-18T15:24:20.000Z：

Does this have a more generous allowance than ngrok? From what I can read no limits are mentioned

**Narciss** · 2026-09-18T15:34:31.000Z：

My AI discovered this days ago when I wanted to deploy a new vibe coded website (it was to keep score while playing whist and rentz)Thought it was very cool

**smalltorch** · 2026-09-18T15:36:57.000Z：

If your a hobbiest or dev just testing your services, it makes more sense to utilize onion services imho.It does the exact same thing, except supported by a global network of volunteers around the world.Sure, you get some latency, but this is actually ideal for testing. You should know how your service operates in non optimal lightning fast conditions.

**himata4113** · 2026-09-18T15:42:50.000Z：

This has existed for a long time and has been abused by quite a few people. I've seen some cc nodes using a random known cloudflare site and spoofing hostname to a temporary cloudflare site. IMO this should require a login at bare minimum.

**cute_boi** · 2026-09-18T15:52:16.000Z：

what a sloppy website, did cloudflare fired bunch of ui/ux designer? Every text is slop lol.

**xeornet** · 2026-09-18T15:53:22.000Z：

Looks like they straight up vibe coded the landing page lol.

**tombert** · 2026-09-18T15:55:18.000Z：

I like Cloudflare Tunnels a lot, but something that annoys me is that officially you're not allowed to use them for streaming video, meaning I can't put it in front of my Jellyfin without breaking TOS.I think that rule is more of a "we reserve the right to..." rule, but it makes me sad because I'd rather not open up ports on my router to expose my Jellyfin to my parents.

**rplnt** · 2026-09-18T15:55:33.000Z：

Are we in an age where no one even bothers to open the product pages they generate? The first subtitle with the font color almost matching the background. Or it's even worse that a human looked at it and said "yep, that's OK"?

**075326899532** · 2026-09-18T15:55:50.000Z：

[ad]

**israrkhan** · 2026-09-18T15:58:49.000Z：

For someone looking for an opensource solutions, following is an awesome resource for tunnellinghttps://github.com/anderspitman/awesome-tunnelingI have played around with frp, bore and ngrok.

**damsta** · 2026-09-18T16:00:48.000Z：

The website looks broken in dark mode on Firefox.

**ggg011012** · 2026-09-18T16:10:12.000Z：

Quick Tunnels look great for demos and temporary dev environments. I’d still be hesitant to make them part of a long-lived production setup.

**kelvinjps10** · 2026-09-18T16:11:18.000Z：

What's the difference between this and their previous Cloudflare Tunnels solution?

**singpolyma3** · 2026-09-18T16:16:31.000Z：

It looks like tunnels can do some non https stuff these days? But it's a bit unclear

**AtNightWeCode** · 2026-09-18T16:29:41.000Z：

Cool but the obvious flaw with this is that CF leaks DNS-records. So bots will find these urls instantly. Not sure why they have not fixed that or if it is even possible to fix.

**nullbyte** · 2026-09-18T16:37:14.000Z：

Love this, very cool.I used to use a service called ngrok for this, but it's nice that Cloudflare is offering one now.

**usewik** · 2026-09-18T16:41:37.000Z：

how long until someone's agent sets up a tunnel for the world to see one's most sensitive, private and embarrassing information or insecure work-in-progress app? granted, for the brew install some massive permissions are needed, so hopefully for those running their agent's in a sandbox, you should be safe.. should be..

**frankcostanza** · 2026-09-18T16:42:02.000Z：

So... Cloudflare built Ngrok?

**_pdp_** · 2026-09-18T16:43:55.000Z：

It will be nice if it had persistent URLs and and SDK for desktop applications. It could solve a lot of small issues for a project I am currently busy with.

**TIPSIO** · 2026-09-18T16:49:06.000Z：

My wife and I have a mobile group/shared bot system where we can make mini apps and collab.Anything from baby stuff, groceries, shopping, planning, wine tracker app, simple/fun/useful data things, etc…We have Tailscale on our phones and can instantly and privately see without deployment or anything crazy via our secure VPN.Think shared Claude Artifacts that don’t live @ Anthropic.Tried to first do this with Cloudflare Tunnels (because I love Cloudflare), but between the broken dashboard side of Zero Trust and nightmare of Warp… it was basically impossible to setup. I guess that’s all super enterprise, which seems to be very anti-Cloudflare philosophically to not be able to self do things.Will check out Quick Tunnels but I think it’s missing the bigger integration offerings Tailscale has/does still.

**dbmikus** · 2026-09-18T16:53:11.000Z：

Now that is one vibe-coded website

**afisxisto** · 2026-09-18T16:53:59.000Z：

I quite like pinggy for this. You don't need to install anything, since it uses a plain SSH tunnel.ssh -p 443 -R0:localhost:9051 free.pinggy.io(Free for 1h each session)

**scosman** · 2026-09-18T16:54:05.000Z：

The number of vibe coded apps accidentally hosted on dev laptops is about to explode.

**corvad** · 2026-09-18T16:54:42.000Z：

This is not anything new they have been around since the tunnels project launched. What is more concerning is the AI slop webpage and just the "AI" centered relaunch of an existing product.

**smetannik** · 2026-09-18T16:59:20.000Z：

So is this basically a ngrok from CF?

**adamfeldman** · 2026-09-18T17:04:52.000Z：

Cloudflare doesn't really seem to care about their tunnel product. "cloudflared service install broken on macOS" since 2021: https://github.com/cloudflare/cloudflared/issues/327

**rock_artist** · 2026-09-18T17:08:25.000Z：

What's surprised me, just earlier today I let Codex write a minor PR for simple open-source webapp. I needed HTTPS for testing secured context Web API. (Web Bluetooth)While testing it locally Codex by itself suggests using CF Tunnels but what's more interesting it actually used the Quick Tunnels.Coming from days where I get warnings of vibe-coded generated code using deprecated code or older APIs, I must say using something so fresh is quite impressive.

**everybodyknows** · 2026-09-18T17:08:34.000Z：

The page is a fine exemplar of marketing deception. Banner says:> Free, secure tunnel for everything you are building.> Preview and ship ideas globally in seconds with Quick Tunnels. Deploy your local application to the Internet with a single command.Clicking through Explore Cloudflare Tunnel leads us to:> Looking to expose public applications?
This documentation covers Cloudflare Tunnel use cases for private networking and Zero Trust, like VPN replacement and private network access. For publishing public web applications, APIs, and services to the Internet through Cloudflare refer to ...

**rinconrex** · 2026-09-18T17:10:42.000Z：

Oh I use this for testing and demos between my phone and computer. Ngrok is fine, probably better off using Tailscale, but it's very easy to just run a quick tunnel with "cloudflared tunnel --url localhost:XXXX".

**spprashant** · 2026-09-18T17:15:21.000Z：

Off-topic: That web page looks exactly like my vibe-coded utilities.

**superkuh** · 2026-09-18T17:16:51.000Z：

Cloudflare's only goal here is to put themselves between everyone and charge a toll. They are running a protection racket where they themselves are causing much of the damage they offer protection from. This is another example.

**bilater** · 2026-09-18T17:16:52.000Z：

So this is basically ngrok?

**bitlad** · 2026-09-18T17:17:07.000Z：

So it is ngrok 10 years later?

**skhameneh** · 2026-09-18T17:21:50.000Z：

There's a number of comments already about how this page looks vibe coded, I'd add that I'm actually shocked at how much this looks like the output of a one-shot prompt. It's not so much that an LLM was used, but a callout on just how generic this page is. How much iteration went into this? At surface it looks like nearly no iteration.Edit: Well, they just re-vibed it. Went from the most generic Claude 4.6 era to today’s models, quality wise. 
I wish I had saved a copy of the original, because it would have taken me actual solid effort to make a page that generic out of an LLM.

**infogulch** · 2026-09-18T17:25:16.000Z：

I made my own tunnel system with a $5/mo vps that runs kernel wireguard and accepts my nas' public key. Once connected it DNATs 80/443 traffic down the tunnel to the nas, where its routed to caddy.The vps runs a custom image that is 2.54 Megabytes. It has a custom kernel with almost everything but networking and wireguard disabled, a fixed-size fs with pre-allocated blocks and inodes to hold the vps wireguard key, and a single pid 1 binary that calls the kernel directly to set up the routing rules, generate a new wireguard key on first boot and save it to the fs, print out the wireguard public key to the console, and loops reap. Updating involves building and uploading a new image, assigning the vps to use it, reboot, wait for the public key in the console then set it on the nas so they can talk.

**general_reveal** · 2026-09-18T17:27:10.000Z：

Could we turn this into p2p cloud hosting for all?

**maipen** · 2026-09-18T17:39:36.000Z：

I'm sorry to be offtopic, but this website looks like an hallucination generated by chatgpt 4.This type of quality downgrade is scary, and it's everywhere now.

**rkovashikawa** · 2026-09-18T17:46:03.000Z：

cloudflare rocks

**mgw** · 2026-09-18T17:49:26.000Z：

Can anyone elaborate on what's new? This exact product has existed from Cloudflare for years. Is it just that they added a new marketing site for it?

**rcarmo** · 2026-09-18T18:01:07.000Z：

I want this with TOTP or passkeys. Just giving me a hostname doesn't cut it these days.

**partloyaldemon** · 2026-09-18T18:17:54.000Z：

Tailscale is one of the most profoundly useful technologies I’ve ever used as small business person. It’s also one I would have never thought to invent despite feeling its lack daily.

**ghoshbishakh** · 2026-09-18T18:22:48.000Z：

This is a very good solution for HTTP(S) tunneling - which is the most frequently needed tunnel. However if you want to play a game, or use SSH, then Pinggy tunnels are very simple to use. One command:ssh -p 443 -R0:localhost:443 tcp@free.pinggy.ioDisclosure: Co-founder of pinggy.io here.Edit: I meant TCP tunnels, UDP tunnels, or also TLS tunnels for end-to-end encryption.

**yuchi** · 2026-09-18T18:24:45.000Z：

I still remember when ngrok came out. The experience was more or less the same.It’s interesting that 10 (more?) years later the product has not evolved and, apparently, hasn’t found a way to finance itself without removing the pure free tunneling option.

**sparc24** · 2026-09-18T18:42:24.000Z：

Worst marketing ever. ngrok had a similar slogan:something like - "We help you put localhost on the Internet."What could possibly go wrong?

**_user_account** · 2026-09-18T18:46:02.000Z：

The main use case: cloud harnesses to access your local network; I highly recommend to run the harness in your local network instead, then you own the session, no tunnel needed.The other use case for webhooks is ok, but is exactly what ngrok already does since forever with a pretty high free quota.

**rvz** · 2026-09-18T18:52:48.000Z：

Seems like the quality of software engineering is now going to zero and just vibe coding unstable alternatives since 2023.

**nickgray** · 2026-09-18T18:55:46.000Z：

This is cool. I like it! Also Cloudflare design has stepped up so much over the past 2 years.

**emadabdulrahim** · 2026-09-18T19:13:43.000Z：

Does this make working with agents in cloud more interesting? Maybe now I can see my changes right away without waiting for the build and deploy? By running the dev server and tunneling from the sandbox giving me a direct url access somehow?Can someone chime in here?

**blocke** · 2026-09-18T19:26:34.000Z：

Ah yes. We can't let self hosted app traffic flow across the Internet in a way that escapes the vast Internet surveillance system run by the Americans called Cloudflare.Hmm, Tailscale is too convenient and that traffic is going dark from Cloudflare's all seeing eye.

**pocksuppet** · 2026-09-18T19:54:00.000Z：

This is obviously vibe written, and I can't wait to see how quickly it will be shut down after someone uses it in combination with Mullvad to host child pornography.Mullvad themselves already turned off port forwarding because people were using it to host child pornography. This is like Mullvad's port forwarding, but free.

**inconshreveable** · 2026-09-18T20:20:45.000Z：

hi y'all, ngrok creator/founder here.we removed anonymous usage of our product many years ago because it was far and away the largest source of abuse on our entire platform.i believe at this point that that anonymous, account-less tunneling services like this are net negative for the security of the internethappy to answer any questions from the community

**tobih** · 2026-09-18T20:59:16.000Z：

json output is nice, my agents always had to parse the text output before

**opengrass** · 2026-09-18T21:04:09.000Z：

This is my docker compose for sharing files with randoms online https://pastebin.com/raw/cYV7ksw9Don't pass -d, your tunnel URL prints in the console and you can download dirs as tarball.

**saejox** · 2026-09-18T21:19:07.000Z：

Needs to support tcp and udp

**dzonga** · 2026-09-18T21:23:14.000Z：

I have been considering using my other laptop as a place to run my agents in production since 1. my laptop is more powerful than the vps I can rent for cheap.then just use Cloudflare tunnels to connect to the laptop.

**cryptolobster** · 2026-09-18T21:24:31.000Z：

For small-scale personal or family applications serving just a few users, does it make sense to choose Quick Tunnels over Tailscale or Pangolin?

**jdthedisciple** · 2026-09-18T21:43:17.000Z：

Interesting but what a horribly vibe coded website that barely works on mobile

**girvo** · 2026-09-18T21:59:14.000Z：

This is super neat! I rely on normal Cloudflare Tunnels for my self-hosted website/web apps, works shockingly well all things considered.It was pretty easy to setup… but I cheated, and use Dokploy which handled most of it AFAICT

**JeremyJaydan** · 2026-09-18T22:10:41.000Z：

I used Cloudflared tunnels for a while in production, they worked very well but the config was a bit of a pain sometimes. It's nice to see a simpler version even if it's just for testing.

**narmiouh** · 2026-09-18T22:21:59.000Z：

I'm not sure how safe this is...vibe coded app with may be no security and now available from the internet for anyone to RCE into my laptop?

**dools** · 2026-09-18T22:27:12.000Z：

I’ve been using cloudflare tunnels quite a bit in places where I would have traditionally gone for a reverse port forward and they’re working really well. The quick tunnel concept seems really great but the non-quick tunnels are also very useful and can be entirely automated.

**noname120** · 2026-09-18T22:41:38.000Z：

Cloudflare Quick Tunnels have existed for more than 5 years (yes, including the anonymous quick tunnels). I copy-pasted the url of the HN link in archive.org, see for yourself: https://web.archive.org/web/20211202005430/http://try.cloudf...Is a new vibe-coded landing page for a 5-year old product really worthy of being on the front page nowadays? There should at least be a [2021] in the title.

**greyhound1** · 2026-09-18T23:19:16.000Z：

i find it hard to read any text when the site has many animations that can't be stopped

**nojvek** · 2026-09-19T00:57:25.000Z：

I so hate codex speak.

**nyxtom** · 2026-09-19T01:05:24.000Z：

I've used these tunnels all the time when I wasn't at my computer. Insanely helpful when doing agentic work on the go

**mintflow** · 2026-09-19T01:18:10.000Z：

perhaps this is the most easy to use networking product that ever shipped, but given ngrok did this many years before, maybe they just think for the agentic era? though one must take care for the authentificationI also think it seems cloudflare enter into a stage keep adding products and make the portal looks like a maze to get more advanced features configuredDo you still remember cloudflare mesh and use and stick to it?

**reddec** · 2026-09-19T02:40:12.000Z：

I have been developing for my own use something like that but self hosted. There are other solutions, but this one simple, reliable and secure in a way I see it.Originally didn't want to share but here it is https://github.com/reddec/tunnel-meUI: fully LLM assisted (not vibe coded, but guided with a lot of iterations).
Backend: hand written, but before release polished via LLM.
Docs: me - input, LLM - output.The things I am proud:- it very reliable- its single binary with reasonable defaults and low memory usage- SSO out of the box (cause I am using pocketid in my homelab)- very simple backend

**Nevin1901** · 2026-09-19T02:47:48.000Z：

Cloudflare tunnels are really useful when dealing with webhooks. Way better than Ngrok and you can set it up on a custom subdomain you own. eg: site.yourdomain.com

**geroge_kyaw** · 2026-09-19T04:52:59.000Z：

Lol Codex UI!!!

**shmde** · 2026-09-19T05:06:36.000Z：

I have used this extensively previously when I had to quickly share a UI prototype with my Product manager. There used to be all sorts of cors error when I also had a backend. Then I realised its just better to make a branch and deploy it in amplify and add the cors origin in the backend. But its good for quick UI sharing

**cliftonc** · 2026-09-19T05:07:12.000Z：

I use this a lot, but find it a bit hard to manage if you want a persistent tunnel locally to use for dev (e.g. webhooks etc), so I added a wrapper around it that you can easily use: https://github.com/cliftonc/cfld

**itvision** · 2026-09-19T07:09:15.000Z：

The RAM pricing crisis is doing wonders to the software industry. Amazing.

**cbsmith** · 2026-09-19T09:04:21.000Z：

What could possibly go wrong? ;-)

**peter_retief** · 2026-09-19T12:21:23.000Z：

I have been using CF tunnels for quite some time, very useful if you want to ingest mail on a local server without a public IP and hosting anything locally.They are providing this for free up to a point, I wonder if all developers are aware of this amazing offering?

**adamch** · 2026-09-19T14:45:20.000Z：

Lovely to see Cloudflare Tunnel frontpage on HN. Working on Tunnel was the highlight of my career. It was a fun product with a lot of bugs to fix, features to add, architecture to design. We were all working in-person, solving incidents together, getting lunch together every day. Taught me so many important skills that have helped me in every other project I've ever worked on.

**abalashov** · 2026-09-19T14:49:00.000Z：

Ah, an ngrok competitor. It's what we elderly (~40 myself), yelling-at-clouds types call "reverse SSH tunnels", but this is an anachronism from the era of knowing how to do things rather than paying for managed SaaS products to do them. Don't mind me, just yelling at clouds...

**ZeroCool2u** · 2026-09-18T15:18:35.000Z：

Anything specific to watch out for?

**whizzter** · 2026-09-18T15:22:16.000Z：

On what url were those? Or Cloudflare's TOS in general ?

**hackernud3s** · 2026-09-18T23:13:26.000Z：

Because it travels along their edge. It's apples and oranges to your AWS tunnel.

**cuu508** · 2026-09-18T15:26:10.000Z：

Yeah, but then you are always exposing your public IP.

**hermanradtke** · 2026-09-18T15:23:17.000Z：

feels more like an ngrok competitor

**alasano** · 2026-09-18T16:00:29.000Z：

More like their version of Tailscale funnel I think

**Tepix** · 2026-09-18T16:17:30.000Z：

I believe with tailscale you don’t have to trust a 3rd party with your cleartext traffic

**aniviacat** · 2026-09-18T15:27:02.000Z：

Cloudflare Tunnels has been a free service of Cloudflare for quite a while now. What's new is being able to use them without needing an account.

**roncesvalles** · 2026-09-18T15:35:14.000Z：

Not many people run their local machine 24/7.

**danserfaty** · 2026-09-18T15:57:58.000Z：

Maybe it's a nice way to quickly test a new service or change over the internet without going through the git process, same way one would use ngrok - I could see that being helpful when prototyping / pocs, etc - before deploying changes to your app via the proper channel, especially if you are already using cloudflare for your domains/apps. As other people said, it probably would not be practical or scalable for most people to run an app 24/7 from their laptop using their home or office internet connection.

**afzalive** · 2026-09-18T15:44:46.000Z：

This is pretty great and I think this will be quite important in the age where everyone has their self-hosted services.

**simonw** · 2026-09-18T15:54:44.000Z：

If there's any company in the world that can survive a lot of extra traffic being pushed through their systems it's Cloudflare.I bet these new tunnels end up being a fraction of a percentage point of their network traffic.

**pstoll** · 2026-09-18T16:13:20.000Z：

Reality check - you are not pushing “_a lot_” of traffic relative to any hyperscaler or large scale CDN. They push hundreds of Tbps sustained. You don’t peak at a few Mbps.They can monitor extreme outliers. It’s not an issue for them.

**inopinatus** · 2026-09-18T16:17:05.000Z：

Cloudflare want you to push traffic through their systems. This is yet another traffic generator to drive up Cloudflare’s leverage when negotiating peering with carriers & service providers, in order to drive down the marginal cost of bandwidth for Cloudflare’s actual product viz. the enterprise DDoS protection.

**Perz1val** · 2026-09-18T16:48:54.000Z：

Interesting how 4/4 other replies didn't get the centralisation concern despite it being a fairly often discussed topic

**t_mahmood** · 2026-09-18T16:52:21.000Z：

Yeah, it reminds me of Google. Fool me twice ...I'm not trusting any of these corporates any more

**done_lurking** · 2026-09-18T18:01:16.000Z：

There are other reasons not to trust them as well, especially if you've seen how their sales team operates https://news.ycombinator.com/item?id=40481808

**ozozozd** · 2026-09-18T20:46:38.000Z：

Your opening piqued my interest, but:“The substrate itself consists of a few systems…”I doubt that this is how wordy your communication is.“It consists of a few systems” would be adequate. And if we had prior context about what else exists that surrounds “the substrate” the “substrate itself” distinction would be meaningful, but it’s not, because you are referring to one object, which is the system you built, and I doubt any enzymes act on it, so it’s likely not a substrate.

**Imustaskforhelp** · 2026-09-18T15:27:10.000Z：

Yes they actually do, but because its cloudflare which is offering this, blacklisting it might lead to blacklisting can be more negative and cloudflare has a much higher incentive to not make these tunnels useless. They are also more powerful and can fix things which would be harder for smaller companies to handle (atleast within the context of cloudflare tunnels)

**axus** · 2026-09-18T15:34:33.000Z：

Wow, exfiltrating data has never been easier!

**srichard16** · 2026-09-18T17:17:19.000Z：

Can confirm. Coming from ngrok, the main reason we had to make tunneling not anonymized etc was because of scammers, etc on the internet. Other players in the space bypass this by open sourcing the tech, or separating the architecture entirely. This is cool and all, but ultimately gives nefarious actors on the internet more opportunities.

**uxjw** · 2026-09-18T17:20:37.000Z：

Probably why they used the trycloudflare.com domain as they expect it to be blocked.

**daemonologist** · 2026-09-18T15:28:03.000Z：

I don't know if there's an overall limit, but their regular tunnels have a limit of 100 MB per request which breaks stuff like Immich.

**raahelb** · 2026-09-18T16:23:54.000Z：

These are the limitations mentioned on the docs [1]. Quick Tunnels are subject to a hard limit on the number of concurrent requests that can be proxied at any point in time. Currently, this limit is 200 in-flight requests. If a Quick Tunnel hits this limit, the HTTP response will return a 429 status code. Quick Tunnels do not support Server-Sent Events (SSE).[1]: https://developers.cloudflare.com/cloudflare-one/networks/co...

**thenewnewguy** · 2026-09-18T15:44:04.000Z：

I honestly can't tell if you're trolling or this is an HN out of touch moment.The obvious difference (and thus massive advantage) of the cloudfare product is that it is accessible over the normal internet without needing to install a tor client.I'm sure that works for some subset of the population where all potential users are already comfortable using Tor; but imagine trying to share your PoC website with the designer/client and you are asking them to install Tor browser.

**booi** · 2026-09-18T16:24:12.000Z：

if you think people won't abuse it because you're making them log in with a free email address...

**usewik** · 2026-09-18T16:43:04.000Z：

yep, and all those fired and remaining are busy ai-native proofing their careers and tokenmaxxing everything including copy

**cub-creature** · 2026-09-18T16:50:13.000Z：

I swear if I see one more "pill-badge callout -> header -> subtitle" with gradient background and hover-cards landing page I'm going to crash out

**rozab** · 2026-09-18T15:59:26.000Z：

I find it quite shocking that orgs with some great designers like cloudflare are doing this. Broken layouts, trios of random uppercase words sprinkled around. It's crazy. How does it inspire confidence in a product, knowing that the landing page was created in 10 seconds?

**TonyStr** · 2026-09-18T16:03:41.000Z：

I discovered and set this up the other day, added jellyfin, immich and forgejo and was really happy about the result for five minutes, before I discovered that limitation in the TOS. Now I only use it for forgejo. Have you found a different solution to exposing jellyfin?

**tamimio** · 2026-09-18T16:13:17.000Z：

Use pangolin (you can self host), been using it for a while and it’s great, under the hood it’s a vpn+reverse proxy which you can do yourself too. 
In pangolin you can have public or private resources, where private ones you need to authenticate through pangolin first (either pass or others like pin number for your parents so easy to remember). When you link your domain for public ones, I suggest you make a sub domain for it, so your apps will be a sub to your subdomain, that way you keep control of your main domain while having automatic assignment for your apps rather than manually, and if you didn’t issue a certificate, that sub.subdomain is basically invisible on the internet unless you host a service to expose it.

**bityard** · 2026-09-18T16:16:44.000Z：

Bandwidth costs money and streaming video costs several orders of magnitude more than just your random web/dev apps. Asking CF to foot the bill for entertainment streaming is really quite a lot.

**mitxela** · 2026-09-18T23:42:36.000Z：

You can put nginx with basic auth in front of jellyfin

**reaperducer** · 2026-09-18T15:57:23.000Z：

Are we in an age where no one even bothers to open the product pages they generate?We live in an age of monkey-see-monkey-do management.When Microsoft axed its QA team, it gave permission for everyone else to make the same stupid mistake.

**lkbm** · 2026-09-18T15:59:16.000Z：

It's fine on light mode. It's just the dark mode that's terrible. Seems likely they only tested the former.

**jeremyjh** · 2026-09-18T21:32:23.000Z：

I find it shocking that they shipped this claudecopy.

**drdexebtjl** · 2026-09-18T16:35:25.000Z：

frp is nice. I have the tiniest Amazon Lightsail instance running a tunnel to a Minecraft server in my basement. It’s cheaper than getting a fixed IP from my ISP, at sufficiently low traffic.

**pstoll** · 2026-09-18T16:20:37.000Z：

You should be more than hesitant - don’t do it. They literally market them for quick demos. And not long lived production.

**rinconrex** · 2026-09-18T17:13:41.000Z：

I use for the exact same thing. Running "cloudflared tunnel" sets up a temp solution. No log in needed, pretty convenient.

**raahelb** · 2026-09-18T16:28:09.000Z：

From their docs [0]:> Free tunnels are meant to be used for testing and development, not for deploying a production website.[0: https://developers.cloudflare.com/cloudflare-one/networks/co...

**awwaiid** · 2026-09-18T18:53:40.000Z：

As far as I can tell, the difference is that they made a new website? The cloudflared instant tunnels have been around for years, including json output as far as I know.

**opengrass** · 2026-09-18T22:17:30.000Z：

This gives a random trycloudflare.com subdomain each run, the other requires a domain and tunnel key on your account.

**yodon** · 2026-09-18T16:54:47.000Z：

That's handled by all the prior releases of cloudflare tunnels

**srichard16** · 2026-09-18T17:21:46.000Z：

ngrok does this free, but with an account

**cmacleod4** · 2026-09-18T18:06:41.000Z：

I've been running a couple of websites* on a home machine behind a Cloudflare tunnel for 2-3 years now. The only thing I had to pay for was the DNS registration. There are limits on the traffic you can serve on their free plan, but I'm nowhere near reaching those. I don't know what an SDK would add, you just set up a web server using whatever method suits you, then configure the cloudflared to connect to that. I did find that the online dashboard could not support all the options I wanted, so I switched to using the config file method - it would have been easier if I used that method from the start.One caveat - there is an option to inject Javascript into your pages for traffic measurement which is ON BY DEFAULT, you have to go to "Web Analytics" and turn this off if you don't want it!* https://cmacleod.me.uk & https://newsgrouper.org

**noir_lord** · 2026-09-18T16:52:24.000Z：

Only reason I have it (cloud flare tunnels) setup for personal use is because I had to do it for work years ago and yeah, Enterprise(tm) is a good description, haven't touched it in years so when it breaks I'll likely use something else.Getting it to do what I wanted with a traefik front router with cloudflared talking to arbitrary subdomain that is spun up and broadcast from the other project side was very painful in a "this could be more friendly" way.It has been truly bulletproof though since then so that's almost enough to make me go reread all the docs.

**nemosaltat** · 2026-09-18T16:56:11.000Z：

Us too, consider using your bots to migrate your tailnet to headscale. Daily driving Headscale + Headplane + Tailscale’s graciously provided/compatible native apps makes me feel like my devices are truly under my control.

**_blk** · 2026-09-18T16:58:58.000Z：

So you have a phone to phone VPN and each runs services or just a regular rapid/synology at home with containers?

**cbsks** · 2026-09-18T17:00:23.000Z：

> My wife and I have a mobile group/shared bot system where we can make mini apps and collab.> Anything from baby stuff, groceries, shopping, planning, wine tracker app, simple/fun/useful data things, etc…Can you elaborate on this? Sounds really cool!

**FridayCuriousit** · 2026-09-18T17:00:54.000Z：

Interested in the the bot system and how your self publishing app artifacts that you've got running. Care to share more?

**theturtletalks** · 2026-09-18T17:05:08.000Z：

Tailscale is truly a cheat code. I have a web app that I run locally to control terminals on my Mac. I access the website on my phone using the 100.xx IP address and can code on the go. No need for a Mac or iOS app.You can also use Tailscale serve to get a HTTPS url like Cloudflared but it's only visible to your tailnet. Be careful using Cloudflare tunnels because they are public and bots start poking around immediately.

**roberttod** · 2026-09-18T19:06:19.000Z：

Does this work with remote agents though? I want my claude.ai agents running on my phone to be able to hit my local MCPs on my Mac Mini - my understanding is that tailscale wouldn't work because the execution is being called remotely. But seems like these tunnels would support that.

**gopalv** · 2026-09-18T19:10:41.000Z：

> it’s missing the bigger integration offerings Tailscale has/does still.Until I had tailscale serve generating valid certs, I had a good reason to use Cloudflare tunnels.But in general I don't want to put everything on the internet side of things.Mostly, I don't want something open, but more like a "share with" for people who are in the same office (virtually over tailnet, not physically on the same LAN).This still works great for a demo instead of a product pitch, to send an link out to see something.I'd still use a real host over a laptop for those.

**unixhero** · 2026-09-18T20:18:42.000Z：

That's really cool! I really want something like that. Care to share what your stack is? My wife would love having that super power.

**nijave** · 2026-09-18T23:28:31.000Z：

Don't think we had any issues with Warp but Cloudflare APIs are a bit of a mess. Seems like they've cobbled together and then renamed/rearranged things multiple times now and it's a bit hard to keep up.Terraform has worked decently well especially since there's a few random settings here and there that aren't exposed anywhere in the UI (facepalm)

**ramoz** · 2026-09-19T01:18:57.000Z：

> Think shared Claude Artifacts that don’t live @ Anthropic.Shameless plug, I've built a self-hosted capability here with things like live collaboration for humans and agents. There is a native cloudflare deplyoment and integration with Cloudflare Artifacts. PR for tunnel would be appreciated.https://github.com/plannotator/artifact-server

**gibs0ns** · 2026-09-19T01:46:52.000Z：

I have really enjoyed the experience of OpenZiti for this purpose. Being able to host dark services and impose granular access controls and routing for different clients is a game changer.For the few services I host that require SSL (eg; WebUSB), I serve the dark service via a standard domain (example.com) so I can still get a LetsEncrypt cert, but public access to that domain resolves to a static page; "Plz connect to OpenZiti & try again". This allows me to have SSL on required dark services without requiring to install a private CA for each client.

**allthetime** · 2026-09-19T02:55:04.000Z：

I use public dns routed to private Tailscale ips for all my home services. If i want to expose something for friends who don’t use Tailscale I connect a cloudflare tunnel… it’s pretty much a couple clicks and typing in a subdomain name once cloudflared is running on a server… what were you having trouble with?

**ezst** · 2026-09-19T04:56:00.000Z：

I would say that I've been doing most of that already with a reverse proxy+SSO/IDP for a very long time. Not the same, but close-enough and open to the "traditional internet" in a manner that does not require my users to install and configure tailscale, which is a massive plus. I do appreciate tailscale for the option to keep my effective host IP address hidden/local, but then I've been having a front on the internet (with a public IP/domain/...) for decades and I don't see a problem continuing.

**pbreit** · 2026-09-19T05:22:54.000Z：

How do I get this more persistent?

**epolanski** · 2026-09-19T07:15:17.000Z：

I never found cloudflare appealing for the small developer.

**ghoshbishakh** · 2026-09-18T18:12:29.000Z：

Thanks for sharing.- Co-founder of Pinggy.

**mitxela** · 2026-09-18T23:35:36.000Z：

You can also do this on any server you have:ssh -R 0.0.0.0:80:localhost:9051 myserverMake sure server sshd config has: GatewayPorts yes

**keeganpoppen** · 2026-09-18T17:39:11.000Z：

yeah am i crazy or could it not like already do this as well? i swear i’ve seen somesuch similar in the cloudflared options. maybe not. but i can second having had some problems over the year getting cloudflared to install/set up correctly. tbf the actual feature works amazing once you get it working.

**st3fan** · 2026-09-18T19:00:47.000Z：

Huh I brew installed it and got a working tunnel in like 15 seconds.

**awwaiid** · 2026-09-18T18:51:06.000Z：

As far as I know this has been a provided feature of cloudflare for several years. I don't understand why it was posted today.

**PufPufPuf** · 2026-09-18T17:32:41.000Z：

Group of three cards, each with a left-aligned icon, heading and subheading stacked -- that's the m-dash of web design.

**vlyan** · 2026-09-18T17:34:22.000Z：

I'll take that over corporate memphis of the previous decade.(idk if it's really declining or I simply haven't noticed it in a while)

**ruuda** · 2026-09-18T20:22:10.000Z：

"Traffic rides Cloudflare's network" Oh, hello Claude.

**ttul** · 2026-09-19T16:16:38.000Z：

I’m not sure your comment is load-bearing enough…

**RedCinnabar** · 2026-09-18T18:55:49.000Z：

Very cool, do you use some kind of an atomic distro like nix or something entirely self built using Yocto/Buildroot? I do something similar with a simple SSH tunnel and a NFT rule. Though, I don’t need your kind of ephemeral setup and so I just use Debian.

**cyberamirul** · 2026-09-19T06:57:43.000Z：

Self hosting might win on control, but it’s harder to manage so I went managed (CF Tunnel). Edge terminates TLS, my Caddy only speaks HTTP, nothing to cert renew (unless you cerbot, but that’s not a guarantee if Let’s encrypt is down).

**mitxela** · 2026-09-18T23:43:51.000Z：

No, by definition it's not P2P because it's all going through Cloudflare.

**6thbit** · 2026-09-18T18:16:06.000Z：

"quick" tunnels you can make by installing cloudflare software and running a command, without a cloudflare account, using a fixed "trycloudflare.com" domain and not your own domain.existing (slow) tunnels you can create once you've set up your own domain for cloudflare to manage its DNS, installing cloudflare software, logging in to your account, and running a similar command.edit: my bad, quick ones aren't new at all

**mmoustafa** · 2026-09-18T18:48:10.000Z：

Nothing is new, quick tunnels were launched in 2021https://blog.cloudflare.com/quick-tunnels-anytime-anywhere/

**tonymet** · 2026-09-18T18:37:29.000Z：

i love this! never understood why a proxy app was needed

**caymanjim** · 2026-09-18T19:01:59.000Z：

What kind of usage limits?

**gpugreg** · 2026-09-19T18:14:35.000Z：

When running this ssh command in qterminal, I can not click on the URL because it refreshes faster than I can right-click and click on "Open Link". Do I have to type the URL by hand or is there a workaround?EDIT: Found a workaround. Double-click the URL and paste it with middle-click.

**m00x** · 2026-09-18T18:46:02.000Z：

How many ways can you convey doing the same thing? All the banks out there have almost identical slogans because they do very similar things.

**hashstring** · 2026-09-18T18:50:44.000Z：

Hm, yeah, depends who you’re marketing this to.Also, the “0 ports opened” marketing is misleading. It still binds to a port and then also lets people access your resources over it.I dislike that Cloudflare Engineering has become more… marketingy as of late. Also with their Cloudflare OS misnomer. Their products used to make more sense, what happened?

**throawayonthe** · 2026-09-18T19:55:37.000Z：

they've been running the tunnels service for yearsand they also provide web hosting..

**jeremyjh** · 2026-09-18T21:34:42.000Z：

Would you ever ship a product where all the ad copy was written by an AI and read by no one?

**Gigachad** · 2026-09-18T21:50:12.000Z：

The marketing from Cloudflare around this being for agents feels like the intended use case is for agents to exfiltrate data off your laptop without pesky hurdles like asking the user to set up an account first.

**opengrass** · 2026-09-18T22:04:40.000Z：

It's not a security issue, it's a liability issue!

**mitxela** · 2026-09-18T23:33:39.000Z：

I'd expect an anonymous inbound tunnel to be better than an anonymous outbound proxy and we have plenty of the latter.

**Gigachad** · 2026-09-18T21:45:05.000Z：

It's broken on desktop too...

**malfist** · 2026-09-18T22:50:10.000Z：

I did not know about them and I have a good use for them today. So I found it useful though I agree it needs the date disclaimer

**nijave** · 2026-09-18T23:30:15.000Z：

Didn't these used to be called Argo Tunnels a long time ago? I think Argo Tunnels got repositioned for connecting to origin servers without needing an incoming connection to the origin but I thought they originally did something like this/ngrokYeah, I just checked the page
>can connect their server to the Internet with Argo Tunnel for free

**jofzar** · 2026-09-19T01:18:56.000Z：

5 years ago imo it was less relevant, if you showed me this then I would be like "cool tech, but other then a specific scenario, why would I care"

**makingstuffs** · 2026-09-19T08:40:50.000Z：

I saw the post and was literally thinking "I have been using these tunnels extensively for a couple years now"

**kqp** · 2026-09-19T09:57:06.000Z：

Why do you think it’s vibe coded? Just asking to see if I can learn something. I can see it’s very standard corpo-aesthetic, uses callouts for the sake of callouts, and is horribly laggy, but corpo websites were doing all that long before AI. It also seems to be using a bunch of Cloudflare-specific terminology that I’d think would take longer to review and correct an AI on than to type yourself.

**peter_retief** · 2026-09-19T12:22:16.000Z：

Yet so many developers do not know about it.

**hypercube33** · 2026-09-19T14:04:51.000Z：

They are useful for taking local llm models and delivering them with HTTPS to harnesses that expect it or to another machine. Other than that I'm not sure what I'd personally use them for.

**dangoodmanUT** · 2026-09-19T00:47:09.000Z：

No, they claim their edge is better for residential connections to your backend. We tried multiple SF to us-east-1 and it was always substantially worse

**monster_truck** · 2026-09-18T15:41:40.000Z：

Exposing it to what exactly? The internet? Yes that's how it works

**israrkhan** · 2026-09-18T16:00:42.000Z：

This is a crowded space with lots of solutions (oss and commercial)https://github.com/anderspitman/awesome-tunneling

**athrowaway3z** · 2026-09-18T17:39:56.000Z：

But you do seem to get to host a https version of your app in case you need features locked behind secure context.

**spwa4** · 2026-09-18T17:48:00.000Z：

That can't be right. If they're hosting on a different DNS they have an absolute need to MITM ssl/tls traffic. Can't work otherwise.So cloudflare sees your plaintext. Btw: tailscale does not (but ssl errors and warnings are unavoidable)

**bakugo** · 2026-09-18T15:33:43.000Z：

It's not new. Maybe this page is new, but being able to set up a quick tunnel on trycloudflare.com without an account has been a thing for years.

**berofeev** · 2026-09-18T15:50:18.000Z：

What does reality look like on this nowadays?My initial thought was desktops generally run 24/7, with laptops running when in use. At least for the customer at the market intersection for this type of product.

**sophacles** · 2026-09-18T16:15:00.000Z：

There are people who turn off their computer?

**cmacleod4** · 2026-09-18T18:09:05.000Z：

You do if you're hosting a website on it :-)

**aliasxneo** · 2026-09-18T15:56:47.000Z：

Yeah, I don't doubt their infrastructure at all. In fact, I rate them fairly high in terms of reliability and performance. I've honestly been a fan of them for a very long time - it's just I'm watching all of this centralization happen and it sets my Spidey sense off. Like I'm waiting for the other shoe to drop.

**eli** · 2026-09-18T16:00:16.000Z：

Don’t the free tunnels have explicit limits on bandwidth and streaming?

**bix6** · 2026-09-18T16:03:12.000Z：

It’s a concentration of power issue.

**ceejayoz** · 2026-09-18T16:03:15.000Z：

I didn't take it as a capacity concern, but a "how much data do they get to look at" one.

**Tepix** · 2026-09-18T16:15:15.000Z：

They see all the traffic in cleartext. Plus you have to trust them not to maliciously alter your traffic. As a US company, their options may be limited if they are coerced by their government to do so.

**ijustlovemath** · 2026-09-18T16:22:31.000Z：

I think they're talking about market capture risks

**aliasxneo** · 2026-09-18T16:24:50.000Z：

In hindsight, that was probably a confusing sentence. I was more pointing out how much traffic flows trough their systems which ends up making it an attractive honeypot, especially as a U.S. company.

**mitxela** · 2026-09-18T23:32:46.000Z：

True. Same reason Hurricane Electric peers promiscuously. I'm surprised more networks don't, to be honest - wouldn't say DTAG prefer that you peer with DTAG than peer with HE upstream of DTAG?

**mitxela** · 2026-09-18T23:34:27.000Z：

Spain blacklisted Cloudflare and everyone hates it, but it proves it can happen.

**noname120** · 2026-09-18T22:31:06.000Z：

How does “open sourcing the tech” “give nefarious actors on the internet more opportunities”? Sounds like a paltry excuse for not open sourcing your tech.

**smalltorch** · 2026-09-18T15:57:07.000Z：

>hobbiest or dev just testing your servicesIs different than sharing your work with a client.I personally wouldnt make it SOP to utilize a complely free service like this to share my work. I'm not saying it's not convient, it definitely is.But you shouldn't subject a clients product to terms they probably aren't aware of.

**himata4113** · 2026-09-18T16:25:22.000Z：

This requires zero effort and you can deploy hundreds to thousands while maintaining 1000 gmail, proton etc takes resources and money.

**maipen** · 2026-09-18T17:41:20.000Z：

AI took all the effort, so I guess nobody sees value in these little pages anymore. Not even those being paid. It's actually scary.

**tombert** · 2026-09-18T16:10:45.000Z：

I have a proxy set up with the Oracle Always Free VMs they provide. It works well enough.

**madeforhnyo** · 2026-09-18T16:13:44.000Z：

For free idk, I personally use a VPS (with unlimited traffic) and Tailscale. Someone has to pay for the public IP and proxy.

**guluarte** · 2026-09-18T16:53:34.000Z：

i just use wireguard or tailscale, provision a subdomain with a custom ssl and resolve to a nat ip.

**tombert** · 2026-09-18T16:18:59.000Z：

I know. I'm not "upset" over it, just that it makes the service less useful for me.

**rvz** · 2026-09-18T19:06:05.000Z：

We are in the age of where hype beats reasoning.

**rplnt** · 2026-09-18T16:06:40.000Z：

I see, good point. Some might be confused about my comment then.

**brazukadev** · 2026-09-18T19:29:32.000Z：

which proves the point OP is making.

**Gigachad** · 2026-09-18T21:46:19.000Z：

I'm viewing the site on lightmode, clicked one of the #links which scrolled down the page, when I scrolled back up all the sections lost their content and were unusable.I've never seen someone fail a static page like this. And from a huge company like Cloudflare too..

**eranation** · 2026-09-18T23:40:36.000Z：

I’m raising my eyebrows…

**brazukadev** · 2026-09-19T12:52:23.000Z：

Cloudflare is going full vibecoding for at least one year. They are high on AI psychosis.

**DaSHacka** · 2026-09-18T20:52:17.000Z：

If only headscale supported tailnet lock and multiple control servers. They consider both features "enterprise" even though the former is arguably a bare minimum and the latter nice even for home users in the event their lab gets taken offline.

**SwamyM** · 2026-09-18T17:35:58.000Z：

Seconded.

**dizzard** · 2026-09-18T18:38:54.000Z：

Not OP- I think there’s been some cool solutions popping up around hosting personal apps. On the front page this week was Capsule (https://withcapsule.app/). My personal solution is Exhibit (https://github.com/momja/Exhibit) which also has the goal of being a self-hostable artifact store.

**rambleraptor** · 2026-09-18T18:45:07.000Z：

I’ve been building something similar with [Homestead](https://myhomestead.dev). It’s my OSS solution for building mini apps. Each mini app is a Resct frontend and the backend (storage, auth, MCP, API, etc) just comes for free.

**ilusion** · 2026-09-19T04:11:31.000Z：

I have my own solution here that also works for sharing stuff with clients with configurable whitelists at artifacts.iofold.com (also open-source for self hosting on cf workers for almost free, github linked on the homepage)

**U4E4** · 2026-09-18T18:41:20.000Z：

I run something similar, and in my system an app artifact is typically just a rich react component in a React Native client. They usually start as prototypes in chat, similar to what the labs provide in their native apps. If I or someone else in my user group wants more depth than a chat widget, then the artifacts can grow into a “workspace”. Oddly enough my richest workspaces have most been for entertainment. DnD, MtG deck building, HN comment thread parsing. And system management. Intrusion detection, feature life cycle/LLM handoff management, call telemetry. I do have a workspace for public county permit lookup which has been handy too. Reach out and I can share more.

**SparkyMcUnicorn** · 2026-09-18T17:57:14.000Z：

> You can also use Tailscale serve to get a HTTPS url like Cloudflared but it's only visible to your tailnetFor public access, similar to these cloudflare tunnels, there's Tailscale Funnel.https://tailscale.com/docs/features/tailscale-funnel

**0x1ch** · 2026-09-18T18:04:05.000Z：

Alternatively, Netbird has been a dream to use over the last half year or so. I think their server software has had some hiccups on new releases, but I stagger those updates anyways. All self hosted, similar concept to Tailscale, very good management UI baked into the self hosted product.

**_user_account** · 2026-09-18T18:47:26.000Z：

just use wireguard; tailscale is just the SSO enterprise overlay with a pricing tab.

**dlopes7** · 2026-09-18T19:41:33.000Z：

I use tailscale on my steam deck to play stardew valley with my son on my laptop, it truly is amazing

**girvo** · 2026-09-18T22:01:58.000Z：

I love TailScale but was getting crazy battery drain on my iPhone with it installed and setup. Still use it, just not from my phone now

**prtmnth** · 2026-09-19T00:45:45.000Z：

Using Tailscale in exactly the same way. It has been such a blessing!

**timwis** · 2026-09-19T09:46:07.000Z：

Fyi you can point a domain/subdomain (eg lan.mysite.com) at that 100.x IP and it will only work for those on your tailnet.

**peter_retief** · 2026-09-19T12:24:06.000Z：

I use both (also Headscale)

**parthdesai** · 2026-09-18T19:26:16.000Z：

if both your mac mini and your phone are on the same tailnet, can't you just ssh to your mac mini from your phone's terminal emulator and have claude code/codex run on it?

**threecheese** · 2026-09-18T19:36:05.000Z：

If by local MCP you mean stdio, then a tailnet won't help you unless you proxy the local MCP using something like mcp-proxy: https://github.com/sparfenyuk/mcp-proxy . That local mcp is only exposed to apps on the machine.
 The flow is Phone client --> agent harness or whatev --> Tailnet --> Mac Mini --> mcp-proxy http listener --> local mcp. But you need to wrap the local mcp runner in the proxy (check the docs).EDIT you don't mean running on your actual phone lol, you mean in the web browser at Claude.ai. Anyway, if you use mcp-proxy for a stdio mcp, or if it's an http mcp alone, then you would need a public endpoint for Claude.ai to connect to. Tailscale will only help you if you use Funnel, but this cloudflare thing is exactly what you need (w/o Tailscale).

**dalberto** · 2026-09-18T20:52:04.000Z：

I built something for this exact use-case using Cloudflare Tunnels:https://github.com/dalberto/mcp-ferryI also use CF managed auth to make auth easier.

**pruneau** · 2026-09-19T03:05:38.000Z：

I use NextDNS instead of public DNS to do the same thing.

**robertlagrant** · 2026-09-18T18:33:11.000Z：

As I understand it you can make a tunnel, but it's under a domain you control and it's a few clicks in the dashboard to set up, and then a something to run in CLI. That's what my homelab uses. This is just a single CLI command and the whole thing is set up.

**lysace** · 2026-09-18T21:15:30.000Z：

Install via brew worked. Getting the hostname to resolve took 30 mins of waiting. Have they heard of wildcard DNS?

**hackernud3s** · 2026-09-18T23:11:21.000Z：

How would you say that? I can't think of a clearer way to say it TBH.

**infogulch** · 2026-09-19T00:35:32.000Z：

Thanks! The build system is nix, but the result is more of an appliance than a distro. (linuxManualConfig from tinyconfig + fragment, static musl Rust PID 1, mke2fs -d) Updates are rebuild-redeploy with the provider API; it can't update itself. The filesystem is a fixed-size image (even omitting resize2fs, so no growing onto the VPS disk), and it remounts read-only after boot. The boot log is 270 kernel lines then 4 userspace: 1 nftables loaded, 2 printing the gate's wg0 public key, 1 remounting ro.

**misnome** · 2026-09-18T18:21:04.000Z：

This has been the behaviour when you launch but don’t connect a specific tunnel for at least a couple of years

**mmoustafa** · 2026-09-18T18:46:49.000Z：

Quick tunnels have existed since at least 2022 (when I was using them)

**fragmede** · 2026-09-18T18:43:31.000Z：

So you don't know my IP (DDoS target), and because of NAT.

**ghoshbishakh** · 2026-09-18T19:15:00.000Z：

A free session runs for 60 seconds after which it has to be restarted and the address changes.You can get the address with an API call.. but we charge for convenience. Pays the infra bills.

**mitxela** · 2026-09-18T23:37:18.000Z：

Marketing is meant to be misleading. That's how it works.

**kalcode** · 2026-09-18T19:58:51.000Z：

It's the AI witch-hunt these days. Salam trails coming soon to you're nearest artist! "That's AI!!!"Sigh... HN littered with it these days.

**wbl** · 2026-09-19T16:25:07.000Z：

There was a problem with the name: toxic mine trailings weren't what was wanted. https://en.wikipedia.org/wiki/Argo_Tunnel

**stingraycharles** · 2026-09-19T05:31:12.000Z：

Why is it more relevant today?

**tefkah** · 2026-09-19T10:18:42.000Z：

Other than the general vibe, there's a number of extremely specific Claude-isms you could pick up on:1. the blinking "now with JSON output for coding agents". It loves to create these blinking badges2. "Some text, and then <Text in a different color>"Then further along the page, the "Your agent needs a URL, not a laptop" has a lot of tells of just being a straight Claude (design) output- The small all-caps "built for the agent era" eyebrow. Once you start noticing this it's EVERYWHERE- The 01 02 03 listIf you have access to Claude you should try have it generate a landing page for a tech product. It will almost always look like this.

**efortis** · 2026-09-19T12:37:42.000Z：

One tell is: if you can code that hero there's no excuse for the silly bugs.For example, the hero is fairly impressive in mobile but it's broken in desktop. And then you scroll down to the next section and there's overflowing text.IOW, the skill level is inconsistent.

**johng** · 2026-09-18T16:06:09.000Z：

This requires no port forwarding, so someone brute force scanning your IP won't find this and your open port. they also might have a harder time figuring out what service has been exposed since the port number itself will be unknown.

**cuu508** · 2026-09-18T17:23:05.000Z：

If somebody learns that such-and-such DynDNS URL is mine, they can always do a DNS lookup to find my current IP address. They can:- find my approximate physical location- regularly scan ports on my IP and wait for me to accidentally expose a service I didn't mean to- track me in any access logs they have access to

**JavierFlores09** · 2026-09-18T16:17:37.000Z：

I often tell my dev colleagues to avoid having their PC turned on all the time, be it because of the electricity bill cost, environmental impact or simply to make the longevity of the hardware a little longer. Granted almost everyone just ignores those things even if they're conscious of it, so I'd say you're right

**roncesvalles** · 2026-09-18T16:37:12.000Z：

Very few people own desktops anymore. Generally people only buy desktops if they need to run a GPU, such as for gaming or running a local model.

**SoftTalker** · 2026-09-18T17:35:02.000Z：

Yeah my desktop is on 24/7. Laptop is on when in use. Phone is on all the time too, of course, but I don't use it for browsing or work nearly as much as my desktop.

**simonw** · 2026-09-18T16:44:21.000Z：

Gotcha, that totally makes sense.

**swozey** · 2026-09-18T17:34:31.000Z：

The "centralization" which is cloudflare basically running its own walled garden version of the interent (how often do you see a cloudflare page checking if you're human?) is exactly why a lot of people do NOT like cloudflare. And if you've known about CF and its leadership since their inception you'd be even more wary of sticking your stuff over there.I've migrated many companies off of cloudflare, usually because they end up pissing off companies when a contract renewal comes up and they slam them with massively increased bills and almost useless support if you aren't very high paying enterprise. I don't know how many CF support tickets I've just given up on over the last 15 years, usually related to their admin page, workers or some weird thing their system does that wasn't documented and I just stop getting responses and definitely don't get fixes.If you ever worked in webhosting the Cloudflare wordpress/etc extensions are everywhere and back when I did work in hosting tons of support tickets were made because of CF. Could be way better now, I don't go near that industry these days.The casual CF user sticking it in front of a blog they rarely look at and the business forced CF user has a very different experience. I cringe and seriously consider if I'm interviewing for an infra role and they use cloudflare. Usually it's startups that grew into larger businesses.

**robertlagrant** · 2026-09-18T20:44:00.000Z：

Given they seem to mostly offer services that are about as easy to switch away from as you could hope for, compared to, say, companies who write loads of CF that only runs on AWS, and I can't imagine why this keeps on being said for Cloudflare specifically. What power do they have?

**insanitybit** · 2026-09-18T16:17:28.000Z：

Just use TLS / mTLS over the tunnel, no?

**pstoll** · 2026-09-19T01:19:51.000Z：

Sure any centralization of infra is an obvious risk for a myriad of reasons eg DoS, manipulation, honeypots, etc.But again my point applies - the chances they get enough people using it that it becomes a meaningfully worse security target than lots of other existing things seems … super low.It’s a big world, people make many choices I can’t understand (nix? Haskell? Php? <flame wars to /dev/null>). Even if this product nailed it - the number of people who can use it is minuscule - yes even as we add Claude-enabled PMs to the software dev ranks.Alt view with the old saying - “put all your eggs in one basket … and watch that basket!”

**booi** · 2026-09-18T16:43:54.000Z：

They already do this. the email accounts already exist

**pocksuppet** · 2026-09-19T18:49:54.000Z：

Since before 2016 actually

**U4E4** · 2026-09-18T18:29:17.000Z：

I’m not GP, but run something that’s pretty close to GPs description. It’s been a fun journey to set up.The core is chat+audio/video call server running locally on my m3 Mac Studio. Centrifugo has handled the chat concerns very well. LiveKit was a really nice foundation for video and audio calls. There are a few different options for local STT if you want that.I used RN via expo for the client and have my friends and family on TestFlight as beta testers. Utility over polish.With messages and call transcripts on my own box, I can prompt Claude code or Codex to operate on any message or transcript content. And follow up in chat with a message. I do most of that from Claude or ChatGPT mobile apps via remote control to my sessions running in the box.From there, if I give enough of a specc, anything that happens in chat or call transcripts can become an additional custom workspace in the main app. I think GP calls these mini apps. But they’re essentially rich clients under the main app umbrella. There’s other details, but yeah it’s a strange new world. Check my profile and reach out directly if you want.

**nacs** · 2026-09-18T18:11:24.000Z：

Tailscale funnel works well but you can only have 1 per Tailscale instance (1 per machine) at the https endpoint so if you want to have a few apps, the others will go on non-https, custom-port URLs.

**garettmd** · 2026-09-18T18:33:07.000Z：

Netbird's great. I've been using Pangolin (https://pangolin.net/) lately for my homelab. It's very similar in functionality to Netbird, but I like the UX of it better.

**drcongo** · 2026-09-18T19:51:20.000Z：

I switched from Tailscale to Netbird purely because of Tailscale's bizarre pricing tiers - I wanted just the SSH features, with multiple users, but the paid tier up from free didn't include the SSH features.

**drakenot** · 2026-09-19T02:27:25.000Z：

For those who use Netbird or Pangolin, I'm trying to understand where it would come in handy over my Wireguard-Easy setup with my phone & laptops configured to connect to my Wireguard network externally.Is this primarily for multi-user scenarios or complex setups?

**herpdyderp** · 2026-09-18T18:50:10.000Z：

I pay Tailscale nothing, why switch?

**titularcomment** · 2026-09-18T19:23:49.000Z：

I think an important feature for homelabs is NAT traversal

**matthewmacleod** · 2026-09-18T19:26:21.000Z：

No, it’s not. It handles the keys, provisioning, DNS, NAT traversal, and a bunch of other stuff. WireGuard is a great technology - Tailscale is like a usability layer on top of it.

**pocksuppet** · 2026-09-18T19:55:28.000Z：

Wireguard is great for a point-to-point or multipoint VPN set up by a competent network administrator between machines with static addresses. But that's the only thing it does. It does not handle authentication or mobility very well.

**jallmann** · 2026-09-19T09:34:47.000Z：

git : github :: wireguard : tailscale

**tenuousemphasis** · 2026-09-18T23:47:58.000Z：

Strange, battery use is negligible on Android, particularly when the tunnel is not in active use.

**eloisius** · 2026-09-18T23:57:08.000Z：

I have the same experience and I once found a GitHub issue about it. I don’t think it sounded like they planned to fix it anytime soon. I just added the Tailscale toggle button to my phone’s quick control panel and turn it on whenever I want to check all my syncthing nodes or something. I keep meaning to see if I can script up something with Shortcuts to make it turn back off automatically.

**devilbunny** · 2026-09-19T01:58:14.000Z：

Were you using an exit node? Because that really does hammer the battery, but vanilla TS without a bunch of traffic doesn't seem to do much to mine.The only always-on TS service on my phone is Immich for photo backup, and I don't take enough photos for that to matter much.

**wildzzz** · 2026-09-18T20:58:33.000Z：

I just use /remote-control. You can't do everything from remote but it's was easier just opening the Claude app than using ssh. And I don't need to be on my tailnet either.

**judge2020** · 2026-09-18T23:13:03.000Z：

Cloudflare isn't going to wildcard every domain on their platform just to cure stale cache DNS issues.

**jofzar** · 2026-09-19T01:20:52.000Z：

"Traffic routes via Cloudflare's network"?

**tefkah** · 2026-09-19T10:22:43.000Z：

Claude has a habit of always talking in an overly active voice, sort of personifying subjects that feels off. I don't think many people would choose to say "Traffic rides" here.

**tonymet** · 2026-09-18T19:09:16.000Z：

any app will connect with an IP am I missing something . a socket is exactly (IP, port) (src, target) tuple

**tredre3** · 2026-09-18T19:54:09.000Z：

I think tonymet meant he didn't understand why cloudflare didn't allow using ssh -R instead of cloudflared to create the tunnel, not not using a tunnel at all.

**ghoshbishakh** · 2026-09-19T05:57:59.000Z：

*60 minutes

**hashstring** · 2026-09-19T10:02:15.000Z：

No, marketing is about communicating valuable offers.Misleading communication is what I am describing, that is a subset of all communications.

**rgoulter** · 2026-09-19T14:01:45.000Z：

The punch and profound-sounding phrasing is also Claude; but pre-LLM it might make sense for a marketing page."Your laptop stays private.
The URL goes everywhere."A URL ... goes, does it?I've seen it pointed out (& have noticed) that anthorpomorphising like this is an LLM smell.In this case, although "URL goes" can be valid, it's just awkward here.

**mitxela** · 2026-09-18T23:44:35.000Z：

They can, and do, do this with or without DynDNS.

**seabrookmx** · 2026-09-18T18:42:03.000Z：

There's pros and cons on the longevity side. 24/7 use causes more wear to mechanical parts (fans for instance) but can be better for the electronics, as heat cycles are a big part of the problem there.

**mitxela** · 2026-09-18T23:31:48.000Z：

It doesn't matter that they're easy to switch away from. It matters that people haven't actually switched away from them.

**himata4113** · 2026-09-19T12:23:46.000Z：

It's the same reason that exists for PoW captcha, it's just way more annoying. Also accounts offer traceability versus a new identity every time you want to do something unless you want to go through hundreds of accounts a day.

**MattCruikshank** · 2026-09-18T19:06:05.000Z：

That's why I keep using tsnet directly, where you can have as many virtual machines, doing sharing or funneling, as you want to.The CLI doesn't let you do as much as the go library does.

**bakkoting** · 2026-09-18T19:33:43.000Z：

You can set up paths that route to different local ports. As long as your apps don't need to live at the root path you can have as many as you like. And you can still have something on the root path as long as it doesn't need the subpath.Here's `tailscale funnel status` on my machine: $ tailscale funnel status
 
 # Funnel on:
 # - https://my-machine.tailXXXX.ts.net
 
 https://my-machine.tailXXXX.ts.net (Funnel on)
 |-- / proxy http://localhost:3000
 |-- /foo proxy http://localhost:3001
 |-- /bar proxy http://localhost:3002
 |-- /baz proxy http://localhost:4004

**justinc8687** · 2026-09-19T03:48:20.000Z：

I have multiple funnels running at once. I just put a tailscale container into my compose stack and that way each compose stack gets its own tailscale instance and thus its own funnel. Happy to share the setup if at all interested.

**havnagiggle** · 2026-09-19T04:40:44.000Z：

Reverse proxy to additional endpoints.

**0x1ch** · 2026-09-18T19:53:35.000Z：

Also a very good alternative. I went on a spree and tried out all of the self hostable alternatives and this was definitely a runner up to netbird. The self hosted tailscale is also good, just not as polished as these two projects are.

**nickspacek** · 2026-09-19T02:08:32.000Z：

Switched from Pangolin to Netbird recently and enjoy Netbird more!

**0x1ch** · 2026-09-18T19:55:14.000Z：

I think Tailscale would've fit my needs perfectly fine, but the management makes access control and grouping dead simple in netbird. It also generates a nice little map of your peers, their groups, and connected nodes etc. Quick visual on your topology.

**allthetime** · 2026-09-19T02:56:00.000Z：

What ssh features? You can have a hundred devices connected for free and they can all just ssh to each other directly

**usagisushi** · 2026-09-19T05:27:13.000Z：

Both support multi-user setups with SSO or built-in auth.Beyond that, compared to a typical hub-and-spoke WireGuard setup, the main advantage is peer-to-peer connectivity. Clients connect directly to each other when possible, which lowers latency by bypassing a central relay.AFAIK, they also have different origins:Pangolin started as an internet-facing reverse proxy (Traefik) combined with a WireGuard server for backend nodes. It has gradually added VPN-like features, including client device access and an internal HTTPS proxy similar to Tailscale Serve.NetBird is a self-hostable Tailscale alternative that started as a mesh VPN focused on P2P traffic. It recently added its own reverse proxy features (Traefik-based, coincidentally), also similar to Tailscale Serve.Pangolin is centered on endpoint and ingress management, while NetBird focuses on mesh networking, though their feature sets are increasingly converging.

**aborsy** · 2026-09-19T02:25:24.000Z：

You should compare battery consumption of TS exit node with something like WG app which low

**girvo** · 2026-09-19T10:25:29.000Z：

I wasn't, no. I'm not the only one whos hit it either, not sure what the cause is :(

**lysace** · 2026-09-19T02:36:03.000Z：

That wasn’t the ask though.The product is falsely advertised as is:"Cloudflare Quick Tunnels"This is on one (or two) particular domain(s) where setting up wildcard DNS should be relatively trivial, if they actually cared enough about the UX of this product to make a special case in their code.I don't understand how people can launch stuff like this.

**hackernud3s** · 2026-09-19T01:58:06.000Z：

It routes from closest PoP to visitor -> closest PoP to origin. Your way doesn't convey that as clearly IMHO.

**c0wb0yc0d3r** · 2026-09-18T19:38:18.000Z：

For me, it’s as much about ease of use as much as it is about minimizing attack surface area.Also the lifetime I need the connection open. For something quick, ssh tunnel. For something normies use, reverse proxy. Ain’t trying to teach my parents about IP addresses and port numbers.

**tonymet** · 2026-09-18T21:24:54.000Z：

precisely (thanks!)

**judge2020** · 2026-09-18T23:21:12.000Z：

cloudflared is a bit unique in that it makes multiple outbound connections to CF DCs to do the tunneling and fails over if a DC has an issue (or, more likely, when a DC is near-capacity and they need to divert lower-tier traffic away from it[0]). SSH would reintroduce a single point of failure to this.Also, the _main_ use case of `cloudflared` tunneling is using it as a long-term way to host production websites on your own hostname. the ability to create ad-hoc tunnels is more of a gimmick / advertising opportunity.0: https://github.com/judge2020/cloudflare-connectivity-test/wi...

**cuu508** · 2026-09-19T08:39:16.000Z：

Do you mean by getting the information from Cloudflare, or some other way? With DynDNS though, finding out my IP is trivial and does not require any special powers or skills, it is just a DNS lookup.PS. Just re-watched your matrix LED pendant video. It is so well done, both the project, and the accompanying video!

**robertlagrant** · 2026-09-19T12:16:04.000Z：

Can you explain why it doesn't matter that they're easy to switch away from?

**BOOSTERHIDROGEN** · 2026-09-19T03:57:31.000Z：

Which features do you specifically benefit from?

**devilbunny** · 2026-09-19T04:47:48.000Z：

WG gonna punch through NAT for me?My endpoint is a pretty stable (though technically dynamic) IPv4 on one end, but the other might be a cell phone with CGNAT, some random WiFi, blah blah etc. TS does that. If you don't want to use it, cool. Don't. I'm willing to make the tradeoffs to use TS for now. That could change in the future.

**inemesitaffia** · 2026-09-19T14:39:26.000Z：

Works on someone's computer.It's "free". That's all you need to understand.

**tonymet** · 2026-09-18T21:25:18.000Z：

tredre3 explained it above

**mitxela** · 2026-09-19T13:04:57.000Z：

They're scanning all IPs all the time. If your home router has a public IP and a firewall log, check it

**mitxela** · 2026-09-19T13:05:22.000Z：

Because it only matters whether people actually switch away from them.
